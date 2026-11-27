"""Builds duda/whats-on/workshops-collection.csv: a lean Workshops collection for the What's On page.

Source: duda/whats-on/whats-on-collection.csv (checked against the shop on 5 Nov 2026).
Only workshops and courses (the regular groups are a fixed section on the page).
Dates before TODAY are kept but hidden (show_on_site = false).
Run: python3 scripts/duda-workshops-csv.py
"""
import csv, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TODAY = datetime.date(2026, 11, 27)
src = list(csv.DictReader(open(ROOT / 'duda/whats-on/whats-on-collection.csv', encoding='utf-8')))
rows = []

def link_type(url):
    """Internal = a page on our own site (shop product pages included); External = any other website."""
    u = (url or '').strip().lower()
    return 'Internal' if (u.startswith('/') or 'sunderlandhomegrown.co.uk' in u) else 'External'
for r in src:
    if r['category'] not in ('Workshop', 'Course'):
        continue
    end = r['end_date'] or r['start_date']
    past = bool(end) and datetime.date.fromisoformat(end) < TODAY
    date = r['date_label'] + (f", {r['time_label']}" if r['time_label'] else '')
    rows.append({
        'item': r['item'],
        'image': r['image'],
        'image_alt': r['image_alt'],
        'date_label': date,
        'price_label': r['price_label'],
        'description': r['short_description'],
        'link_type': link_type(r['booking_url']),
        'link': r['booking_url'],
        'link_text': 'Sold out: see the shop' if r['status'] == 'Sold out' else (r['booking_button_text'] or 'Find out more'),
        'status': 'Past' if past else r['status'],
        'show_on_site': 'false' if past else 'true',
        'sort_order': len(rows) + 1,
    })
out = ROOT / 'duda/whats-on/workshops-collection.csv'
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print(out.name, len(rows), 'rows;', sum(r['show_on_site'] == 'true' for r in rows), 'shown')
for r in rows: print(' ', r['show_on_site'], r['link_type'], r['status'], '|', r['item'])
