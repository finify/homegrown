"""Builds duda/whats-on/whats-on-collection.csv for import into a Duda collection.

Data comes from the live store (Workshops and Christmas categories, checked 5 Nov 2026) and the
What's On page. Unknown details are left blank rather than guessed: fill them in, in Duda.
Run: python3 scripts/duda-whats-on-csv.py
"""
import csv, datetime as dt, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'duda/whats-on/whats-on-collection.csv'
STORE = 'https://www.sunderlandhomegrown.co.uk/store/'
CDN = 'https://irp.cdn-website.com/0432dc74/dms3rep/multi/'
TODAY = dt.date(2026, 11, 5)
HOME_GROWN = 'Sunderland Home Grown, Thompson Park, Southwick, Sunderland SR5 1SF'

FIELDS = [
    'uuid', 'item', 'slug', 'category', 'audience', 'age_range',
    'schedule_type', 'start_date', 'end_date', 'start_time', 'end_time', 'recurrence', 'date_label', 'time_label',
    'price', 'price_label', 'price_note', 'is_free',
    'booking_required', 'booking_url', 'booking_button_text', 'status',
    'location', 'short_description', 'description', 'what_to_bring', 'accessibility_notes',
    'image', 'image_alt', 'featured', 'show_on_site', 'sort_order',
]

def nice_date(d):
    return d.strftime('%a %-d %b %Y')

rows = []

# ---- Christmas wreath workshops (store: Christmas category) ----
wreaths = [
    # (number, date, price, sold out?, product id, url slug, image)
    ('01', dt.date(2026, 11, 25), 20, False, '778355403', '%E2%80%8B%F0%9F%8E%84%E2%9C%A8-Christmas-Wreath-Workshop-01%E2%9C%A8%F0%9F%8E%84Wednesday-25th-November-1PM-%E2%9C%A8', '5139642772'),
    ('02', dt.date(2026, 11, 26), 20, False, '778358775', '%F0%9F%8E%84%E2%9C%A8-Christmas-Wreath-Workshop-02-%F0%9F%8E%84-Thursday-26th-November-1PM-%E2%9C%A8', '5139674171'),
    ('03', dt.date(2026, 11, 27), 20, False, '595061055', '%F0%9F%8E%84%E2%9C%A8-Christmas-Wreath-Workshop-03-%E2%9C%A8Friday-27th-November-1PM-%E2%9C%A8%F0%9F%8E%84', '3272328750'),
    ('04', dt.date(2026, 11, 28), 25, False, '600136264', '%F0%9F%8E%84%E2%9C%A8-Christmas-Wreath-Workshop-04-%F0%9F%8E%84Saturday-28th-November-1PM-%E2%9C%A8%F0%9F%8E%84', '3272328750'),
    ('05', dt.date(2026, 11, 29), 25, True, '500544153', '%F0%9F%8E%84-Christmas-Wreath-Workshop-05-%E2%9C%A8-Sunday-29th-November-1PM%F0%9F%8E%84', '3272322806'),
    ('06', dt.date(2026, 12, 2), 20, True, '600136269', '%F0%9F%8E%84%E2%9C%A8-Christmas-Wreath-Workshop-06-%E2%9C%A8Wednesday-December-2nd-1PM%F0%9F%8E%84', '3272328750'),
    ('07', dt.date(2026, 12, 3), 20, True, '600091857', '%F0%9F%8E%84-Christmas-Wreath-Workshop-07%E2%9C%A8Thursday-December-3rd-1PM%F0%9F%8E%84', '3272322558'),
    ('09', dt.date(2026, 12, 5), 25, False, '500544800', '%F0%9F%8E%84Christmas-Wreath-Workshop-09%E2%9C%A8-Saturday-December-5th-1PM%F0%9F%8E%84', '3272322565'),
    ('10', dt.date(2026, 12, 6), 25, False, '500544154', '%F0%9F%8E%84%E2%9C%A8-Christmas-Wreath-Workshop-10%E2%9C%A8Sunday-December-6th-1PM%F0%9F%8E%84', '3272328750'),
    ('11', dt.date(2026, 12, 9), 20, True, '600080669', '%E2%9C%A8-Christmas-Wreath-Workshop-11%F0%9F%8E%84Wednesday-December-9th-1PM-%E2%9C%A8', '3272327504'),
    ('12', dt.date(2026, 12, 10), 20, True, '778385784', '%E2%80%8B%E2%9C%A8-Christmas-Wreath-Workshop-12%F0%9F%8E%84%E2%80%8B-Thursday-December-10th-1PM-%E2%9C%A8', '5139707464'),
]
for n, d, price, sold, pid, url_slug, img in wreaths:
    rows.append({
        'item': f'Christmas wreath workshop, {nice_date(d)}',
        'slug': f'christmas-wreath-workshop-{d.isoformat()}',
        'category': 'Workshop', 'audience': 'Adults', 'age_range': '',
        'schedule_type': 'Single date', 'start_date': d.isoformat(), 'end_date': d.isoformat(),
        'start_time': '13:00', 'end_time': '', 'recurrence': '',
        'date_label': nice_date(d), 'time_label': '1pm',
        'price': price, 'price_label': f'£{price}', 'price_note': 'Weekday sessions £20, weekend sessions £25',
        'is_free': 'false', 'booking_required': 'true',
        'booking_url': f'{STORE}{url_slug}-p{pid}', 'booking_button_text': 'Book a place',
        'status': 'Sold out' if sold else 'Available',
        'location': HOME_GROWN,
        'short_description': 'Make your own Christmas wreath to take home.',
        'description': '<p>A hands-on Christmas wreath-making session at Sunderland Home Grown in Thompson Park. Book your place online.</p>',
        'what_to_bring': '', 'accessibility_notes': '',
        'image': f'https://d2j6dbq0eux0bg.cloudfront.net/images/27206052/products/{pid}/{img}.jpg',
        'image_alt': 'A finished Christmas wreath of holly and greenery',
        'featured': 'true' if n == '01' else 'false', 'show_on_site': 'true',
    })

# ---- Junior Joiners (store: Workshops category) ----
jj_start = dt.date(2026, 11, 9)
jj_end = jj_start + dt.timedelta(weeks=3)  # four Mondays
rows.append({
    'item': 'Junior Joiners, 4-week course (ages 11 to 13)',
    'slug': f'junior-joiners-11-13-{jj_start.isoformat()}',
    'category': 'Course', 'audience': 'Young people', 'age_range': '11 to 13',
    'schedule_type': 'Weekly course', 'start_date': jj_start.isoformat(), 'end_date': jj_end.isoformat(),
    'start_time': '13:00', 'end_time': '14:30', 'recurrence': 'Every Monday for 4 weeks',
    'date_label': f'Mondays, {jj_start.strftime("%-d %b")} to {jj_end.strftime("%-d %b %Y")}', 'time_label': '1pm to 2:30pm',
    'price': 80, 'price_label': '£80', 'price_note': 'Price for the full 4-week course',
    'is_free': 'false', 'booking_required': 'true',
    'booking_url': f'{STORE}Workshop-JUNIOR-JOINERS-11-13-Years-old-Monday-9th-November-1-00-2-30-4-Week-course-p793425131',
    'booking_button_text': 'Book the course', 'status': 'Available',
    'location': HOME_GROWN,
    'short_description': 'A four-week joinery course for young people aged 11 to 13.',
    'description': '<p>Junior Joiners is a four-week joinery course for young people aged 11 to 13, every Monday from 1pm to 2:30pm.</p>',
    'what_to_bring': '', 'accessibility_notes': '',
    'image': 'https://d2j6dbq0eux0bg.cloudfront.net/images/27206052/products/793425131/6311537416.jpg',
    'image_alt': 'Junior Joiners workshop',
    'featured': 'true', 'show_on_site': 'true',
})

# ---- Regular groups (What's On page) ----
groups = [
    {
        'item': 'Fruit and vegetables group', 'slug': 'fruit-and-vegetables-group', 'category': 'Group',
        'audience': 'Everyone', 'schedule_type': 'Weekly', 'start_time': '10:00', 'end_time': '12:00',
        'recurrence': 'Every Monday', 'date_label': 'Every Monday', 'time_label': '10am to 12 noon',
        'short_description': 'Learn to grow your own fruit and vegetables alongside our team.',
        'description': '<p>Learn propagation, succession planting, pest control, feeding and pruning. The produce is shared with volunteers and some is donated to Sunderland Soup Kitchen.</p>',
        'what_to_bring': 'Stout footwear and gloves',
        'image': CDN + '20230522_113141-8d0bb07d-e5602a81-f6f71114.jpg', 'image_alt': 'Raised vegetable beds at Home Grown',
        'location': HOME_GROWN, 'booking_url': '/contact', 'booking_button_text': 'Ask about joining',
    },
    {
        'item': 'Local history and heritage group', 'slug': 'local-history-and-heritage-group', 'category': 'Group',
        'audience': 'Everyone', 'schedule_type': 'Monthly', 'recurrence': 'Twice a month',
        'date_label': 'Twice a month', 'time_label': '',
        'short_description': 'Explore the history and heritage of Southwick and Thompson Park.',
        'description': '<p>Our local history and heritage group meets twice a month at the Park Café in Thompson Park.</p>',
        'image': '', 'image_alt': '',
        'location': 'The Park Café, Thompson Park, Southwick, Sunderland', 'booking_url': '/contact', 'booking_button_text': 'Ask about joining',
    },
    {
        'item': 'Beekeeping group', 'slug': 'beekeeping-group', 'category': 'Group',
        'audience': 'Everyone', 'schedule_type': 'Ongoing', 'recurrence': '',
        'date_label': 'Ask us for dates', 'time_label': '',
        'short_description': 'Learn how to look after our hives.',
        'description': '<p>Suit up and learn how a honeybee colony works with our beekeeping group.</p>',
        'image': CDN + '293257885_1131507570902878_3452411455125337265_n-60ab1dd9.jpg', 'image_alt': 'Two beekeepers inspecting a frame of honeycomb',
        'location': HOME_GROWN, 'booking_url': '/contact', 'booking_button_text': 'Ask about joining',
    },
]
for g in groups:
    rows.append({
        'age_range': '', 'start_date': '', 'end_date': '', 'start_time': g.get('start_time', ''), 'end_time': g.get('end_time', ''),
        'price': '', 'price_label': 'Ask us', 'price_note': '', 'is_free': '',
        'booking_required': 'false', 'status': 'Ongoing', 'what_to_bring': g.get('what_to_bring', ''),
        'accessibility_notes': '', 'featured': 'false', 'show_on_site': 'true', **g,
    })

# Order: dated events first (soonest first), then regular groups.
rows.sort(key=lambda r: (r['start_date'] == '', r['start_date'], r['start_time']))
for i, r in enumerate(rows, 1):
    r['sort_order'] = i
    r['uuid'] = ''
# Reuse the template's existing row id for the first row, so importing updates that test row
# instead of leaving it behind.
rows[0]['uuid'] = '4badc2b1-1cc3-4641-bd11-4d3c7e439155'

with OUT.open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, '') for k in FIELDS})
print(f'{OUT.relative_to(ROOT)}: {len(rows)} rows, {len(FIELDS)} fields')
