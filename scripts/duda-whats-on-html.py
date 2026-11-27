"""Generates duda/whats-on/after/whats-on.html: the What's On page, built around a Duda Dynamic Repeater.

The workshop list itself is a Dynamic Repeater connected to the Workshops collection: it is added in
the editor (it can't be pasted as HTML), inside the row with the class shg-wo__list. base.css styles
whatever card is designed in it (image, title, date, description, button).
Run: python3 scripts/duda-whats-on-html.py
"""
import glob, pathlib, random, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'duda/whats-on/after/whats-on.html'
taken = set()
for f in glob.glob(str(ROOT / 'duda/**/*.html'), recursive=True):
    if pathlib.Path(f) != OUT:
        taken |= set(re.findall(r'\b1\d{9}\b', open(f).read()))
random.seed(2026_12)

def nid():
    while True:
        n = str(random.randint(1000000000, 1999999999))
        if n not in taken:
            taken.add(n)
            return n

def text(cls, inner, tag='div'):
    return (f'<{tag} class="dmNewParagraph {cls}" data-element-type="paragraph" dmle_widget="paragraph" '
            f'data-uialign="left" data-version="5" id="{nid()}" style="transition:opacity 1s ease-in-out;">\n{inner}\n</{tag}>')

def image(cls, src, alt):
    return (f'<div class="imageWidget align-center {cls}" editablewidget="true" data-element-type="image" '
            f'dmle_widget="image" data-widget-type="image" id="{nid()}">\n <a id="{nid()}">\n'
            f'  <img src="{src}" alt="{alt}" id="{nid()}" class="" data-dm-image-path="{src}"/>\n </a>\n</div>')

def col(classes, extra, *widgets):
    return (f' <div class="dmRespCol {classes} {extra}" id="{nid()}">\n  <!-- *** INSERT YOUR HTML BELOW *** -->\n'
            + '\n'.join(widgets) + '\n </div>')

def row(extra, *cols):
    return (f'<div class="dmRespRow {extra}" id="{nid()}">\n <div class="dmRespColsWrapper" id="{nid()}">\n'
            + '\n'.join(cols) + '\n </div>\n</div>')

C = 'https://irp.cdn-website.com/0432dc74/dms3rep/multi/'
FULL = 'large-12 medium-12 small-12'

hero = row('shg-wo__hero',
    col('large-7 medium-12 small-12', 'shg-wo__hero-text',
        text('shg-wo__eyebrow', 'What’s on'),
        text('shg-wo__title', 'Workshops at the nursery', 'h1'),
        text('shg-wo__lead', 'Hands-on workshops and courses in Thompson Park. Choose one below and book your place in our shop.'),
        text('shg-wo__button', '<a href="/store">Visit the shop</a>')),
    col('large-5 medium-12 small-12', 'shg-wo__hero-media',
        image('shg-wo__hero-img', C + 'IMG_20220216_135314-bccdc096.jpg', 'Four people smiling as they plant up pots together.')))

list_head = row('shg-wo__head',
    col('large-6 medium-12 small-12', 'shg-wo__head-title', text('shg-wo__h2', 'Upcoming workshops', 'h2')),
    col('large-6 medium-12 small-12', 'shg-wo__head-lead',
        text('shg-wo__lead-dark', 'Places are limited, so book early. Sold-out dates stay listed in case a place comes free.')))

# The Dynamic Repeater goes in this column. The note shows only while the column has nothing else in it.
workshops = row('shg-wo__list',
    col(FULL, 'shg-wo__list-col',
        text('shg-wo__placeholder', 'Our next workshops will be listed here soon. Call <a href="tel:+441915499444">0191 549 9444</a> to ask what’s coming up.')))

def group(title, when, body, link, label):
    return col('large-4 medium-4 small-12', 'shg-wo__group',
        text('shg-wo__group-when', when),
        text('shg-wo__group-title', title, 'h3'),
        text('shg-wo__group-text', body),
        text('shg-wo__group-link', f'<a href="{link}">{label}</a>'))

groups_head = row('shg-wo__head shg-wo__head--groups',
    col('large-6 medium-12 small-12', 'shg-wo__head-title', text('shg-wo__h2', 'Regular groups', 'h2')),
    col('large-6 medium-12 small-12', 'shg-wo__head-lead',
        text('shg-wo__lead-dark', 'Groups that meet through the year. Ask us about joining.')))
groups = row('shg-wo__groups',
    group('Fruit and vegetables group', 'Every Monday, 10am to 12 noon', 'Learn to grow your own fruit and vegetables alongside our team.', '/fruit-vegetables-group', 'More about the group'),
    group('Beekeeping group', 'Ask us for dates', 'Learn how to look after our hives.', '/contact', 'Ask about joining'),
    group('Local history and heritage group', 'Twice a month', 'Explore the history and heritage of Southwick and Thompson Park.', '/contact', 'Ask about joining'))

cta = row('shg-wo__cta',
    col('large-7 medium-12 small-12', 'shg-wo__cta-text',
        text('shg-wo__h2', 'Questions about a workshop?', 'h2'),
        text('shg-wo__lead-light', 'We’re happy to help with dates, places and access.')),
    col('large-5 medium-12 small-12', 'shg-wo__cta-actions',
        text('shg-wo__button', '<a href="tel:+441915499444">Call 0191 549 9444</a>'),
        text('shg-wo__button shg-wo__button--light', '<a href="/contact">Contact us</a>')))

html = f'''<!-- *** ADD OR EDIT HTML INSIDE OF THE dmRespCol DIVS, SEE DOCUMENTATION FOR GUIDELINES *** -->
<!--
  Sunderland Home Grown redesign: WHAT'S ON page (/whats-on)
  Replaces the whole page HTML. Styled by base.css (already linked site-wide).
  The workshop list: add a Dynamic Repeater inside the "Upcoming workshops" list row and connect it to
  the Workshops collection (see duda/whats-on/README.md). The note in that row hides itself once the
  repeater is there.
-->
<div dm:templateorder="170" class="dmHomeRespTmpl mainBorder dmRespRowsWrapper dmFullRowRespTmpl shg-wo" id="1716942098">
{hero}
{list_head}
{workshops}
{groups_head}
{groups}
{cta}
</div>
'''
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html)
ids = re.findall(r'\bid="(\d+)"', html)
print(f'{OUT.name}: {len(ids)} ids, unique={len(ids) == len(set(ids))}')
