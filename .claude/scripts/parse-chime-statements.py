#!/usr/bin/env python3
"""
parse-chime-statements.py
Parses Chime PDF bank statements and appends each period to finances-history.json.

Usage:
  python parse-chime-statements.py            # process all Chime PDFs in Vox Arcanum
  python parse-chime-statements.py path.pdf   # process a specific PDF
"""

import sys
import re
import json
import glob
from datetime import datetime
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import pypdf

VAULT = Path("F:/My Drive/Obsidian/Codex.os")
VOX_ARCANUM = Path("C:/Users/aspor/Documents/Vox Arcanum")
FINANCES_HISTORY = VAULT / "05 Areas/Finances/finances-history.json"
IMPORTS_DIR = VAULT / "05 Areas/Finances/imports"

# Transaction type keywords (order matters — longer phrases first)
KNOWN_TYPES = [
    "Round Up Transfer",
    "Purchase",
    "Deposit",
    "Transfer",
    "Adjustment",
    "Fee",
    "SpotMe",
]

# Category rules — shared with SoFi parser
CATEGORY_MAP = [
    # Income / Payroll
    (["CRUNCHTIME", "QSR AUTOMATIONS", "PAYROLL", "DIRECT DEP"], "Income: Paycheck"),
    (["MY PAY ADVANCE", "MY PAY REPAYMENT", "MY PAY INSTANT", "DAVE INC", "INSTANT LOAN PAYMENT",
      "EARNIN", "BRIGIT", "ALBERT INSTANT"], "Transfers: Advance"),
    (["SOFI PLUS", "INTEREST", "BONUS", "MISCELLANEOUS CREDIT", "CHECK DEPOSIT"], "Income: Other"),
    (["VISA MONEY TRANSFER", "MOVED TO SECURED", "SECURED DEPOSIT ACCOUNT"], "Transfers: Internal"),

    # Housing
    (["NEWREZ", "SHELLPOIN"], "Housing: Mortgage"),

    # Utilities
    (["DUKE ENERGY", "DUKEENERGY", "SPI-ENERGY", "SPI ENERGY"], "Utilities: Electric"),
    (["AMERICAN WATER", "WATER WORKS"], "Utilities: Water"),
    (["CITY OF JEFFERSONVILLE"], "Utilities: City"),
    (["JEFFERSONVILLE WASTE", "WASTE MANAGEMENT", "REPUBLIC SERVICES"], "Utilities: Trash"),
    (["SPECTRUM MOBILE"], "Bills: Phone"),
    (["SPECTRUM"], "Bills: Internet"),

    # Subscriptions
    (["CLAUDE.AI", "ANTHROPIC"], "Subscriptions: Claude"),
    (["OPENAI", "CHATGPT"], "Subscriptions: ChatGPT"),
    (["MIDJOURNEY"], "Subscriptions: Midjourney"),
    (["AUDIBLE"], "Subscriptions: Audible"),
    (["GOOGLE "], "Subscriptions: Google"),
    (["PEACOCK", "CBS INTERACT", "ROKU"], "Subscriptions: Streaming"),
    (["PLAYST", "SIE PLAYST", "NINTENDO", "XBOX"], "Subscriptions: Gaming"),
    (["PATREON"], "Subscriptions: Patreon"),
    (["APPLE.COM/BILL", "APPLE COM/BILL", "APPLE COM CUPERT"], "Subscriptions: Apple"),
    (["MOLTEN HOSTING"], "Subscriptions: Hosting"),
    (["ZIP* APP PAY LATER", "ZIP* 2 INSTALL"], "Transfers: BNPL"),

    # Tobacco / Vape
    (["VALERO", "ELECTRIC LADYLAND", "HIFIINDY", "HIFI FAST", "VAPE", "TOBACCO"], "Personal: Tobacco"),

    # Gas
    (["CIRCLE K", "SHELL", "EXXON", "BP ", "MARATHON", "SPEEDWAY", "SUNOCO", "BUC-EE"], "Gas"),

    # Convenience
    (["365 MARKET"], "Shopping: Convenience"),

    # Groceries
    (["KROGER", "ALDI", "WALMART", "SAM'S CLUB"], "Groceries"),

    # Fast Food / Dining
    (["TACO BELL", "MCDONALD", "BURGER KING", "SUBWAY", "ARBY", "WENDY", "CHICK-FIL",
      "PANDA EXPRESS", "ZAXBY", "MARCOS PIZZA", "QDOBA", "JAGGERS", "MCALISTER",
      "MOBY DICK", "DOORDASH", "DD *", "UBER EATS", "UBER * EATS", "GRUBHUB", "DOMINO",
      "PIZZA HUT", "CHIPOTLE", "POPEYES", "CULVER", "RAISING CANE", "STEAK N SHAKE",
      "JACK IN THE BOX", "LITTLE CAESARS", "KFC", "PENN STATION",
      "FAZOLIS", "CAPTAIN D", "CAPTAINDS", "COLD STONE",
      "TSTKING", "TSTPIZZA", "TSTSTATION PIZZ", "TSTFEED"], "Dining: Fast Food"),

    # Sit-down Restaurants
    (["CHILIS", "CHILI'S", "OLIVE GARDEN", "PANERA", "CHUY", "STAR SUSHI",
      "TAZIKIS", "LIANGFU"], "Dining: Restaurants"),

    # Grooming
    (["NOBS ROUTINES"], "Personal: Grooming"),

    # Shopping
    (["AMAZON", "AMZN"], "Shopping: Amazon"),
    (["EBAY"], "Shopping: eBay"),
    (["THRIFT", "GOODWILL", "VENDORS VILLAGE"], "Shopping: Thrift"),
    (["TORRID", "SP MAISON FITCH", "CATHOUSE HOLLYWOOD"], "Shopping: Clothing"),
    (["LOWE'S", "LOWES", "HOME DEPOT"], "Shopping: Home Improvement"),
    (["MENARD", "MNRD-"], "Shopping: Home Improvement"),
    (["KIRKLAND", "BATH AND BODY", "BATHANDBODYWORKS"], "Shopping: Home"),
    (["FIVE BELOW", "DOLLAR TREE", "DOLLAR GENERAL"], "Shopping: Retail"),
    (["ZZOUNDS", "BETTER DAYS RECORDS", "HALF PRICE BOOKS"], "Shopping: Media"),
    (["SP PETKIT"], "Pets"),

    # Entertainment
    (["FANDANGO", "CLARKSVILLE STRIKE", "SQ GREAT ESCAPE"], "Entertainment"),

    # Family / School
    (["GREATER CLARK COUNTY SC"], "Family: School"),

    # Health
    (["PHARMACY", "CVS", "WALGREEN", "RITE AID", "LAKE SUBSTANCE", "VISION FIRST"], "Health: Other"),

    # Transfers / Cash
    (["CASH APP", "VENMO", "ZELLE"], "Transfers: People"),
    (["ROUND UP", "TRANSFER TO CHIME", "TRANSFER FROM CHIME"], "Transfers: Internal"),

    # City/Parking
    (["JEFFERSONVILLE PARKING", "IN403"], "City: Parking/Fees"),
]


def categorize(description: str) -> str:
    desc_upper = description.upper()
    for keywords, category in CATEGORY_MAP:
        for kw in keywords:
            if kw.upper() in desc_upper:
                return category
    return "Uncategorized"


def extract_text(pdf_path: str) -> str:
    reader = pypdf.PdfReader(pdf_path)
    return '\n'.join(page.extract_text() or '' for page in reader.pages)


def parse_period(text: str):
    m = re.search(r'\((\w+ \d+, \d{4}) - (\w+ \d+, \d{4})\)', text)
    if not m:
        return None, None
    fmt = '%B %d, %Y'
    try:
        start = datetime.strptime(m.group(1), fmt)
        end = datetime.strptime(m.group(2), fmt)
        return start, end
    except ValueError:
        return None, None


def parse_transactions(text: str):
    """
    Parse Chime PDF transaction text into a list of dicts.
    Format per transaction:
      DATE
      SHORT_DESCRIPTION [optional truncated]
      [LONG_DESCRIPTION] [optional full caps]
      TYPE
      AMOUNT
      NET_AMOUNT
      SETTLEMENT_DATE
    """
    # Trim to the transactions section
    tx_start = text.find("TRANSACTION DATE\nDESCRIPTION")
    if tx_start == -1:
        tx_start = text.find("Transactions\n")
    if tx_start != -1:
        # Skip past the header line(s)
        text = text[tx_start:]
        # Skip the column header block
        header_end = text.find('\n', text.find('SETTLEMENT DATE'))
        if header_end != -1:
            text = text[header_end + 1:]

    date_re = re.compile(r'^\d{1,2}/\d{1,2}/\d{4}$')
    amount_re = re.compile(r'^-?\$[\d,]+\.\d{2}$')

    lines = [l.strip() for l in text.split('\n')]
    lines = [l for l in lines if l and not l.startswith('Member Services') and not l.startswith('Page ')]

    transactions = []
    i = 0
    while i < len(lines):
        # Look for a transaction date
        if not date_re.match(lines[i]):
            i += 1
            continue

        tx_date_str = lines[i]
        i += 1

        # Collect description lines until we hit a known type
        desc_lines = []
        tx_type = None
        while i < len(lines):
            line = lines[i]
            matched_type = None
            for t in KNOWN_TYPES:
                if line == t:
                    matched_type = t
                    break
            if matched_type:
                tx_type = matched_type
                i += 1
                break
            # Stop if we hit another date (malformed block)
            if date_re.match(line):
                break
            desc_lines.append(line)
            i += 1

        if not tx_type or not desc_lines:
            continue

        # Amount
        if i >= len(lines) or not amount_re.match(lines[i]):
            continue
        amount_str = lines[i].replace('$', '').replace(',', '')
        amount = float(amount_str)
        i += 1

        # Net amount (skip)
        if i < len(lines) and amount_re.match(lines[i]):
            i += 1

        # Settlement date (skip)
        if i < len(lines) and date_re.match(lines[i]):
            i += 1

        # Use the longest (most informative) description line
        description = max(desc_lines, key=len) if desc_lines else ''

        try:
            tx_date = datetime.strptime(tx_date_str, '%m/%d/%Y')
        except ValueError:
            continue

        transactions.append({
            'date': tx_date,
            'description': description,
            'type': tx_type,
            'amount': amount,
            'category': categorize(description),
        })

    return transactions


def summarize(transactions):
    income = defaultdict(float)
    spending = defaultdict(float)
    transfers = defaultdict(float)

    for tx in transactions:
        cat = tx['category']
        amt = tx['amount']
        if cat.startswith("Income"):
            income[cat] += amt
        elif cat.startswith("Transfers") or tx['type'] in ('Round Up Transfer', 'Transfer'):
            transfers[cat] += abs(amt)
        elif amt < 0:
            spending[cat] += abs(amt)

    return income, spending, transfers


def make_label(start: datetime, end: datetime) -> str:
    if start.month == end.month:
        return start.strftime('%b %Y')
    return f"{start.strftime('%b')}–{end.strftime('%b %Y')}"


def load_history() -> list:
    if FINANCES_HISTORY.exists():
        with open(FINANCES_HISTORY, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_history(history: list):
    history.sort(key=lambda h: h['period']['start'])
    with open(FINANCES_HISTORY, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2)


def process_pdf(pdf_path: str):
    print(f"\nParsing: {pdf_path}")
    text = extract_text(pdf_path)
    start_dt, end_dt = parse_period(text)
    if not start_dt:
        print("  Could not find statement period — skipping.")
        return

    period_start = start_dt.strftime('%Y-%m-%d')
    period_end = end_dt.strftime('%Y-%m-%d')
    label = make_label(start_dt, end_dt)
    print(f"  Period: {period_start} → {period_end} ({label})")

    transactions = parse_transactions(text)
    print(f"  {len(transactions)} transactions parsed")

    income, spending, transfers = summarize(transactions)
    total_in = sum(income.values())
    total_out = sum(spending.values())
    net = total_in - total_out

    print(f"  In: ${total_in:,.2f}  Out: ${total_out:,.2f}  Net: ${net:,.2f}")

    # Show categories found
    for cat, amt in sorted(spending.items(), key=lambda x: -x[1])[:8]:
        print(f"    {cat}: ${amt:,.2f}")

    entry = {
        "label": label,
        "period": {"start": period_start, "end": period_end},
        "totalIn": round(total_in, 2),
        "totalOut": round(total_out, 2),
        "net": round(net, 2),
        "spending": {cat: round(amt, 2) for cat, amt in sorted(spending.items(), key=lambda x: -x[1])}
    }

    # Copy PDF to imports folder
    IMPORTS_DIR.mkdir(parents=True, exist_ok=True)
    import shutil
    dest = IMPORTS_DIR / Path(pdf_path).name
    if Path(pdf_path) != dest:
        shutil.copy2(pdf_path, dest)

    history = load_history()
    history = [h for h in history if h.get('period', {}).get('start') != period_start]
    history.append(entry)
    save_history(history)
    print(f"  → History updated ({len(history)} periods total)")


def main():
    if len(sys.argv) > 1:
        pdfs = sys.argv[1:]
    else:
        pdfs = sorted(glob.glob(str(VOX_ARCANUM / "Chime-Checking-Statement-*.pdf")))

    if not pdfs:
        print("No Chime PDFs found in Vox Arcanum.")
        sys.exit(1)

    print(f"Found {len(pdfs)} Chime statement(s) to process.")
    for pdf in pdfs:
        process_pdf(pdf)

    history = load_history()
    print(f"\nDone. finances-history.json now has {len(history)} period(s).")
    for h in history:
        print(f"  {h['label']:20s} In: ${h['totalIn']:>8,.2f}  Out: ${h['totalOut']:>8,.2f}  Net: ${h['net']:>+8,.2f}")


if __name__ == "__main__":
    main()
