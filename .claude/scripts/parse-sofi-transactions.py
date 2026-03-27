#!/usr/bin/env python3
"""
parse-sofi-transactions.py
Parses SoFi CSV exports and updates 05 Areas/Finances/finances-overview.md

Usage:
  python parse-sofi-transactions.py [path/to/csv]
  If no path given, looks for newest *.csv in Vox Arcanum folder.

Drops processed CSV into vault imports folder, updates finances-overview.md.
"""

import csv
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Fix Windows console encoding
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

VAULT = Path("F:/My Drive/Obsidian/Codex.os")
VOX_ARCANUM = Path("C:/Users/aspor/Documents/Vox Arcanum")
FINANCES_FILE = VAULT / "05 Areas/Finances/finances-overview.md"
FINANCES_JSON = VAULT / "05 Areas/Finances/finances-data.json"
FINANCES_HISTORY = VAULT / "05 Areas/Finances/finances-history.json"
IMPORTS_DIR = VAULT / "05 Areas/Finances/imports"

# --- Monthly budget targets (edit these to set your goals) ---
MONTHLY_BUDGETS = {
    "Housing: Mortgage":       1677,
    "Utilities: Electric":      300,  # high this period — target avg
    "Utilities: Water":         130,
    "Utilities: City":           85,
    "Bills: Phone":             183,
    "Bills: Internet":           45,
    "Dining: Fast Food":        300,
    "Groceries":                300,
    "Gas":                      150,
    "Shopping: Amazon":         200,
    "Shopping: Convenience":     30,
    "Shopping: Thrift":          50,
    "Personal: Tobacco":        150,
    "Personal: Grooming":        25,
    "Subscriptions: Claude":     20,
    "Subscriptions: ChatGPT":    20,
    "Subscriptions: Audible":    17,
    "Subscriptions: Midjourney": 10,
    "Subscriptions: Google":      5,
    "Health: Pharmacy":          25,
    "City: Parking/Fees":        15,
}

# --- Category rules (description keyword → category) ---
CATEGORY_MAP = [
    # Income
    (["CRUNCHTIME INFOR", "DIRECT_DEPOSIT"], "Income: Paycheck"),
    (["BONUS", "INTEREST_EARNED", "SOFI PLUS", "SoFi Rewards", "Miscellaneous Credit"], "Income: Other"),

    # Housing
    (["NEWREZ", "SHELLPOIN"], "Housing: Mortgage"),

    # Utilities
    (["DUKEENERGY", "DUKE ENERGY"], "Utilities: Electric"),
    (["AMERICAN WATER", "WATER WORKS"], "Utilities: Water"),
    (["CITY OF JEFFERSONVILLE"], "Utilities: City"),
    (["SPECTRUM MOBILE"], "Bills: Phone"),
    (["SPECTRUM"], "Bills: Internet"),

    # Subscriptions
    (["CLAUDE.AI", "ANTHROPIC"], "Subscriptions: Claude"),
    (["OPENAI", "CHATGPT"], "Subscriptions: ChatGPT"),
    (["MIDJOURNEY"], "Subscriptions: Midjourney"),
    (["AUDIBLE"], "Subscriptions: Audible"),
    (["GOOGLE *"], "Subscriptions: Google"),

    # Tobacco (Valero = almost always cigarettes)
    (["VALERO"], "Personal: Tobacco"),

    # Gas
    (["CIRCLE K", "SHELL", "EXXON", "BP ", "MARATHON", "SPEEDWAY", "SUNOCO"], "Gas"),

    # Convenience stores (office vending, snacks)
    (["365 MARKET"], "Shopping: Convenience"),

    # Groceries
    (["KROGER", "ALDI", "WALMART", "SAM'S CLUB"], "Groceries"),

    # Fast Food / Dining Out
    (["TACO BELL", "MCDONALD", "BURGER KING", "SUBWAY", "ARBY", "WENDY", "CHICK-FIL",
      "PANDA EXPRESS", "ZAXBY", "MARCOS PIZZA", "QDOBA", "JAGGERS", "MCALISTER",
      "MOBY DICK", "DOORDASH", "DD *", "UBER EATS", "GRUBHUB", "DOMINO", "PIZZA HUT",
      "CHIPOTLE", "POPEYES", "JACK IN THE BOX", "LITTLE CAESARS", "KFC",
      "FAZOLIS", "CAPTAIN D", "CAPTAINDS", "COLD STONE", "PENN STATION",
      "CULVER", "RAISING CANE", "STEAK N SHAKE",
      "TSTKING", "TSTPIZZA", "TSTSTATION PIZZ"], "Dining: Fast Food"),

    # Sit-down Restaurants
    (["CHILIS", "CHILI'S", "OLIVE GARDEN", "PANERA", "CHUY", "STAR SUSHI",
      "TAZIKIS", "LIANGFU"], "Dining: Restaurants"),

    (["NOBS ROUTINES"], "Personal: Grooming"),

    # Shopping
    (["AMAZON", "AMZN"], "Shopping: Amazon"),
    (["EBAY"], "Shopping: eBay"),
    (["THRIFT", "GOODWILL", "VENDORS VILLAGE"], "Shopping: Thrift"),
    (["TORRID"], "Shopping: Clothing"),
    (["LOWE'S", "LOWES", "HOME DEPOT", "MENARD", "MNRD-"], "Shopping: Home Improvement"),
    (["FIVE BELOW", "DOLLAR TREE", "DOLLAR GENERAL", "TARGET"], "Shopping: Retail"),
    (["ZZOUNDS", "BETTER DAYS RECORDS", "HALF PRICE BOOKS"], "Shopping: Media"),

    # Subscriptions
    (["PATREON"], "Subscriptions: Patreon"),
    (["APPLE.COM/BILL", "APPLE COM/BILL"], "Subscriptions: Apple"),
    (["MOLTEN HOSTING"], "Subscriptions: Hosting"),
    (["ZIP* APP PAY LATER", "ZIP* 2 INSTALL"], "Transfers: BNPL"),

    # Entertainment
    (["FANDANGO"], "Entertainment"),

    # Family
    (["GREATER CLARK COUNTY SC"], "Family: School"),

    # Health / Pharmacy
    (["PHARMACY", "CVS", "WALGREEN", "RITE AID", "AMZNPHARMA", "VISION FIRST"], "Health: Pharmacy"),

    # Transfers / Cash
    (["CASH APP", "VENMO", "ZELLE"], "Transfers: People"),
    (["To ", "From ", "WITHDRAWAL", "DEPOSIT"], "Transfers: Internal"),

    # City/Parking
    (["IN403", "JEFFERSONVILLE PARKING"], "City: Parking/Fees"),
]

def categorize(description, tx_type):
    desc_upper = description.upper()
    for keywords, category in CATEGORY_MAP:
        for kw in keywords:
            if kw.upper() in desc_upper:
                return category
    if tx_type == "DIRECT_DEPOSIT":
        return "Income: Paycheck"
    if tx_type in ("DIRECT_PAY",):
        return "Bills: Auto-Pay"
    return "Uncategorized"

def parse_csv(filepath):
    transactions = []
    with open(filepath, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                amount = float(row['Amount'])
                date = datetime.strptime(row['Date'].strip(), '%Y-%m-%d')
                balance_str = row.get('Current balance', '').strip()
                balance = float(balance_str) if balance_str else None
                transactions.append({
                    'date': date,
                    'description': row['Description'].strip(),
                    'type': row['Type'].strip(),
                    'amount': amount,
                    'balance': balance,
                    'status': row['Status'].strip(),
                    'category': categorize(row['Description'], row['Type'].strip()),
                })
            except (ValueError, KeyError):
                continue
    return sorted(transactions, key=lambda x: x['date'])

def summarize(transactions):
    income = defaultdict(float)
    spending = defaultdict(float)
    transfers = defaultdict(float)

    for tx in transactions:
        cat = tx['category']
        amt = tx['amount']
        if cat.startswith("Income"):
            income[cat] += amt
        elif cat.startswith("Transfers"):
            transfers[cat] += abs(amt)
        elif amt < 0:
            spending[cat] += abs(amt)

    return income, spending, transfers

def format_summary(transactions, filepath):
    if not transactions:
        return "No transactions found."

    income, spending, transfers = summarize(transactions)
    start = transactions[0]['date'].strftime('%Y-%m-%d')
    end = transactions[-1]['date'].strftime('%Y-%m-%d')

    total_in = sum(income.values())
    total_out = sum(spending.values())
    latest_balance = next((t['balance'] for t in reversed(transactions) if t['balance'] is not None), None)

    lines = []
    lines.append(f"\n## Import: {start} → {end}")
    lines.append(f"> Parsed: {datetime.now().strftime('%Y-%m-%d %H:%M')} | Source: `{Path(filepath).name}`\n")

    if latest_balance is not None:
        lines.append(f"**Current Balance:** ${latest_balance:,.2f}")
    lines.append(f"**Total In:** ${total_in:,.2f}  |  **Total Out:** ${total_out:,.2f}  |  **Net:** ${total_in - total_out:,.2f}\n")

    lines.append("### Spending by Category")
    lines.append("| Category | Amount |")
    lines.append("|---|---|")
    for cat, amt in sorted(spending.items(), key=lambda x: -x[1]):
        lines.append(f"| {cat} | ${amt:,.2f} |")
    lines.append(f"| **TOTAL** | **${total_out:,.2f}** |\n")

    lines.append("### Income")
    lines.append("| Source | Amount |")
    lines.append("|---|---|")
    for cat, amt in sorted(income.items(), key=lambda x: -x[1]):
        lines.append(f"| {cat} | ${amt:,.2f} |")
    lines.append(f"| **TOTAL** | **${total_in:,.2f}** |\n")

    if transfers:
        lines.append("### Transfers (excluded from spending)")
        for cat, amt in transfers.items():
            lines.append(f"- {cat}: ${amt:,.2f}")
        lines.append("")

    # Flag large/unusual transactions
    big = [t for t in transactions if t['amount'] < -200 and not t['category'].startswith(("Housing", "Transfers", "Income"))]
    if big:
        lines.append("### Flagged Transactions (>$200, non-housing)")
        for t in big:
            lines.append(f"- {t['date'].strftime('%m-%d')} | {t['description'][:40]} | ${abs(t['amount']):.2f} | {t['category']}")
        lines.append("")

    return "\n".join(lines)

def run(filepath=None):
    # Find CSV if not specified
    if not filepath:
        csvs = sorted(VOX_ARCANUM.glob("SOFI*.csv"), key=os.path.getmtime, reverse=True)
        if not csvs:
            print("No SoFi CSV found in Vox Arcanum folder.")
            sys.exit(1)
        filepath = csvs[0]

    print(f"Parsing: {filepath}")
    transactions = parse_csv(filepath)
    print(f"  {len(transactions)} transactions found.")

    summary = format_summary(transactions, filepath)

    # Ensure imports dir exists
    IMPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Move CSV to imports
    dest = IMPORTS_DIR / Path(filepath).name
    if Path(filepath) != dest:
        import shutil
        shutil.copy2(filepath, dest)
        print(f"  Copied to: {dest}")

    # Update finances-overview.md
    if FINANCES_FILE.exists():
        existing = FINANCES_FILE.read_text(encoding='utf-8')
    else:
        existing = """---
area: finances
tags: [finances, budget]
last_updated: 2026-03-26
---

# Finances Overview

## Recurring Bills
| Bill | Amount | Due | Auto-Pay |
|---|---|---|---|
| Mortgage (NewRez/Shellpoint) | ~$1,677 | ~27th | Yes |
| Duke Energy (Electric) | ~$760 | ~16th | Yes |
| American Water Works | ~$128 | ~15th | Yes |
| City of Jeffersonville | ~$83 | ~15th | Yes |
| Spectrum Mobile (Phone) | ~$183 | ~14th | Yes |
| Spectrum (Internet) | ~$45 | ~1st | Yes |
| Audible | ~$17 | ~15th | Yes |
| Midjourney | $10 | ~15th | Yes |
| ChatGPT | $20 | ~1st | Yes |
| Claude.ai | $20 | ~3rd | Yes |

**Monthly Fixed Bills Total: ~$2,943**

## Pay Schedule
- Bi-weekly direct deposit (Crunchtime) — approx $2,500–2,600/paycheck
- Pay dates: typically 12th and 26th of month

## Budget Notes

"""

    with open(FINANCES_FILE, 'w', encoding='utf-8') as f:
        # Strip any previous import sections before appending fresh one
        import_marker = "\n## Import:"
        cut = existing.find(import_marker)
        base = existing[:cut] if cut != -1 else existing
        f.write(base.rstrip() + "\n")
        f.write(summary)

    print(f"  Updated: {FINANCES_FILE}")

    # Write structured JSON sidecar for FinancesPanel
    import json
    income, spending, transfers = summarize(transactions)
    start_date = transactions[0]['date'].strftime('%Y-%m-%d') if transactions else ''
    end_date   = transactions[-1]['date'].strftime('%Y-%m-%d') if transactions else ''
    latest_balance = next((t['balance'] for t in reversed(transactions) if t['balance'] is not None), None)
    big = [t for t in transactions if t['amount'] < -200 and not t['category'].startswith(("Housing", "Transfers", "Income"))]

    spending_list = []
    for cat, amt in sorted(spending.items(), key=lambda x: -x[1]):
        spending_list.append({
            "category": cat,
            "amount": round(amt, 2),
            "budget": MONTHLY_BUDGETS.get(cat)
        })

    data = {
        "period": {"start": start_date, "end": end_date},
        "parsedAt": datetime.now().strftime('%Y-%m-%d %H:%M'),
        "source": Path(filepath).name,
        "balance": round(latest_balance, 2) if latest_balance is not None else None,
        "totalIn": round(sum(income.values()), 2),
        "totalOut": round(sum(spending.values()), 2),
        "net": round(sum(income.values()) - sum(spending.values()), 2),
        "spending": spending_list,
        "income": [{"source": k, "amount": round(v, 2)} for k, v in income.items()],
        "transfers": [{"type": k, "amount": round(v, 2)} for k, v in transfers.items()],
        "flagged": [
            {
                "date": t['date'].strftime('%m-%d'),
                "description": t['description'][:40],
                "amount": round(abs(t['amount']), 2),
                "category": t['category']
            }
            for t in big
        ]
    }

    with open(FINANCES_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"  JSON: {FINANCES_JSON}")

    # Update finances-history.json (deduped by period start)
    start_dt = transactions[0]['date'] if transactions else None
    end_dt = transactions[-1]['date'] if transactions else None
    if start_dt and end_dt:
        if start_dt.month == end_dt.month:
            label = start_dt.strftime('%b %Y')
        else:
            label = f"{start_dt.strftime('%b')}–{end_dt.strftime('%b %Y')}"
        history_entry = {
            "label": label,
            "period": {"start": start_date, "end": end_date},
            "totalIn": round(sum(income.values()), 2),
            "totalOut": round(sum(spending.values()), 2),
            "net": round(sum(income.values()) - sum(spending.values()), 2),
            "spending": {cat: round(amt, 2) for cat, amt in spending.items()}
        }
        if FINANCES_HISTORY.exists():
            with open(FINANCES_HISTORY, 'r', encoding='utf-8') as f:
                history = json.load(f)
        else:
            history = []
        # Replace existing entry for same period start, or append
        history = [h for h in history if h.get("period", {}).get("start") != start_date]
        history.append(history_entry)
        # Sort chronologically by period start
        history.sort(key=lambda h: h["period"]["start"])
        with open(FINANCES_HISTORY, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2)
        print(f"  History: {FINANCES_HISTORY} ({len(history)} periods)")

    print("\nDone.")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else None
    run(path)
