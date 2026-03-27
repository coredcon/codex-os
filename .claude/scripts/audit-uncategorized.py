#!/usr/bin/env python3
"""Audit uncategorized spending across all Chime PDFs."""
import sys, re, glob, pypdf
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

VOX_ARCANUM = Path('C:/Users/aspor/Documents/Vox Arcanum')
KNOWN_TYPES = ['Round Up Transfer','Purchase','Deposit','Transfer','Adjustment','Fee','SpotMe']

CATS = [
    (['CRUNCHTIME','QSR AUTOMATIONS','PAYROLL','DIRECT DEP'], 'Income: Paycheck'),
    (['MY PAY ADVANCE','DAVE INC','EARNIN','BRIGIT','ALBERT INSTANT'], 'Transfers: Advance'),
    (['SOFI PLUS','INTEREST','BONUS','MISCELLANEOUS CREDIT','CHECK DEPOSIT'], 'Income: Other'),
    (['VISA MONEY TRANSFER'], 'Transfers: Internal'),
    (['NEWREZ','SHELLPOIN'], 'Housing: Mortgage'),
    (['DUKE ENERGY','DUKEENERGY'], 'Utilities: Electric'),
    (['AMERICAN WATER','WATER WORKS'], 'Utilities: Water'),
    (['CITY OF JEFFERSONVILLE'], 'Utilities: City'),
    (['SPECTRUM MOBILE'], 'Bills: Phone'),
    (['SPECTRUM'], 'Bills: Internet'),
    (['CLAUDE.AI','ANTHROPIC'], 'Subscriptions: Claude'),
    (['OPENAI','CHATGPT'], 'Subscriptions: ChatGPT'),
    (['MIDJOURNEY'], 'Subscriptions: Midjourney'),
    (['AUDIBLE'], 'Subscriptions: Audible'),
    (['GOOGLE '], 'Subscriptions: Google'),
    (['PEACOCK','CBS INTERACT','ROKU'], 'Subscriptions: Streaming'),
    (['PLAYST','SIE PLAYST','NINTENDO','XBOX'], 'Subscriptions: Gaming'),
    (['VALERO','ELECTRIC LADYLAND','HIFIINDY','HIFI FAST','VAPE','TOBACCO'], 'Personal: Tobacco'),
    (['CIRCLE K','SHELL','EXXON','BP ','MARATHON','SPEEDWAY','SUNOCO'], 'Gas'),
    (['365 MARKET'], 'Shopping: Convenience'),
    (['KROGER','ALDI','WALMART','SAM\'S CLUB'], 'Groceries'),
    (['TACO BELL','MCDONALD','BURGER KING','SUBWAY','ARBY','WENDY','CHICK-FIL',
      'PANDA EXPRESS','ZAXBY','MARCOS PIZZA','QDOBA','JAGGERS','MCALISTER',
      'MOBY DICK','DOORDASH','DD *','UBER EATS','GRUBHUB','DOMINO','PIZZA HUT',
      'CHIPOTLE','POPEYES','CULVER','RAISING CANE','STEAK N SHAKE'], 'Dining: Fast Food'),
    (['NOBS ROUTINES'], 'Personal: Grooming'),
    (['AMAZON','AMZN'], 'Shopping: Amazon'),
    (['THRIFT','GOODWILL'], 'Shopping: Thrift'),
    (['PHARMACY','CVS','WALGREEN','RITE AID','LAKE SUBSTANCE'], 'Health: Other'),
    (['CASH APP','VENMO','ZELLE'], 'Transfers: People'),
    (['ROUND UP','TRANSFER TO CHIME','TRANSFER FROM CHIME'], 'Transfers: Internal'),
    (['JEFFERSONVILLE PARKING','IN403'], 'City: Parking/Fees'),
]

def categorize(description):
    d = description.upper()
    for kws, cat in CATS:
        for kw in kws:
            if kw in d:
                return cat
    return 'Uncategorized'

date_re = re.compile(r'^\d{1,2}/\d{1,2}/\d{4}$')
amount_re = re.compile(r'^-?\$[\d,]+\.\d{2}$')

uncategorized = defaultdict(lambda: {'count': 0, 'total': 0.0, 'raw': ''})

pdfs = sorted(glob.glob(str(VOX_ARCANUM / 'Chime-Checking-Statement-*.pdf')))
for pdf_path in pdfs:
    reader = pypdf.PdfReader(pdf_path)
    text = '\n'.join(page.extract_text() or '' for page in reader.pages)

    tx_start = text.find('TRANSACTION DATE\nDESCRIPTION')
    if tx_start == -1:
        tx_start = text.find('Transactions\n')
    if tx_start != -1:
        text = text[tx_start:]
        header_end = text.find('\n', text.find('SETTLEMENT DATE'))
        if header_end != -1:
            text = text[header_end + 1:]

    lines = [l.strip() for l in text.split('\n')]
    lines = [l for l in lines if l and not l.startswith('Member Services') and not l.startswith('Page ')]

    i = 0
    while i < len(lines):
        if not date_re.match(lines[i]):
            i += 1
            continue
        i += 1
        desc_lines = []
        tx_type = None
        while i < len(lines):
            line = lines[i]
            matched = next((t for t in KNOWN_TYPES if line == t), None)
            if matched:
                tx_type = matched
                i += 1
                break
            if date_re.match(line):
                break
            desc_lines.append(line)
            i += 1
        if not tx_type or not desc_lines:
            continue
        if i >= len(lines) or not amount_re.match(lines[i]):
            continue
        amount = float(lines[i].replace('$','').replace(',',''))
        i += 1
        if i < len(lines) and amount_re.match(lines[i]):
            i += 1
        if i < len(lines) and date_re.match(lines[i]):
            i += 1

        description = max(desc_lines, key=len)
        cat = categorize(description)
        if cat == 'Uncategorized' and amount < 0:
            key = re.sub(r'\s+[A-Z]{2}US$', '', description.upper()).strip()
            key = re.sub(r'\s+\d{3}-\d{3}-\d{4}', '', key).strip()
            key = re.sub(r'#\w+\s*', '', key).strip()
            key = re.sub(r'\*[A-Z0-9]+\s*', '', key).strip()
            uncategorized[key]['count'] += 1
            uncategorized[key]['total'] += abs(amount)
            uncategorized[key]['raw'] = description

sorted_unk = sorted(uncategorized.items(), key=lambda x: -x[1]['total'])
print(f'{"Description":<55} {"Total":>9}  {"Count":>5}')
print('-' * 75)
for key, v in sorted_unk[:60]:
    print(f'{key[:54]:<55} ${v["total"]:>8,.2f}  {v["count"]:>5}x')
