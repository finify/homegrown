"""Generates duda/grow/after/grow-rows.html: "How to join, in four steps" with a plant that grows as you scroll.

Two editor-safe rows (heading, then the plant and the steps) for the Day opportunities page
(paste just above the "Ready to start your journey?" register row). Optional on the Home page.
The plant is drawn by site.js into the left-hand column; styles are in base.css.
Words come from the day opportunities flyer: nothing new is promised.
Run: python3 scripts/duda-grow-html.py
"""
import glob, pathlib, random, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
taken = set()
for f in glob.glob(str(ROOT / 'duda/**/*.html'), recursive=True):
    if 'grow/after' in f:
        continue
    taken |= set(re.findall(r'\b1\d{9}\b', open(f).read()))
random.seed(20261127)

def nid():
    while True:
        n = str(random.randint(1000000000, 1999999999))
        if n not in taken:
            taken.add(n)
            return n

def text(cls, inner, tag='div'):
    return (f'<{tag} class="dmNewParagraph {cls}" data-element-type="paragraph" dmle_widget="paragraph" '
            f'data-uialign="left" data-version="5" id="{nid()}" style="transition:opacity 1s ease-in-out;">\n{inner}\n</{tag}>')

def col(classes, extra, *widgets):
    return (f' <div class="dmRespCol {classes} {extra}" id="{nid()}">\n  <!-- *** INSERT YOUR HTML BELOW *** -->\n'
            + '\n'.join(widgets) + '\n </div>')

def row(extra, *cols):
    return (f'<div class="dmRespRow {extra}" id="{nid()}">\n <div class="dmRespColsWrapper" id="{nid()}">\n'
            + '\n'.join(cols) + '\n </div>\n</div>')

steps = [
    ('Get in touch', 'Fill in our short form, call 0191 549 9444 or email us. You can do this yourself, or a family member, carer, social worker or support coordinator can do it for you.'),
    ('Book a free trial visit', 'Come to Thompson Park, meet the team and see for yourself. There’s no need to decide straight away.'),
    ('Agree your support', 'Group or individual one-to-one support, with flexible attendance to meet your needs. You may be able to use a Direct Payment or Personal Budget.'),
    ('Start growing', 'Grow plants and vegetables, learn woodworking, explore arts and crafts, care for the bees and gain hands-on nursery experience.'),
]

head = row('shg-grow-band shg-grow-head',
    col('large-6 medium-12 small-12', 'shg-grow__head-title',
        text('shg-grow__eyebrow', 'How to join'),
        text('shg-grow__title', 'Four steps to your first day', 'h2')),
    col('large-6 medium-12 small-12', 'shg-grow__head-lead',
        text('shg-grow__lead', 'Book a free trial visit and see for yourself. No need to decide straight away.')))

journey = row('shg-grow-band shg-grow',
    col('large-6 medium-12 small-12', 'shg-grow__art',
        text('shg-grow__art-note', 'As you scroll, a seed in a pot grows into a plant with three leaves, one step at a time.')),
    col('large-6 medium-12 small-12', 'shg-grow__steps',
        *[text('shg-grow__step', f'<b>{t}</b><br/>{b}') for t, b in steps],
        text('shg-grow__button', '<a href="/day-opportunities#register">Book a free trial visit</a>')))

html = ('<!--\n'
        '  SUNDERLAND HOME GROWN REDESIGN: "HOW TO JOIN, IN FOUR STEPS" (plant grows as you scroll)\n'
        '  Two rows. Paste them on the Day opportunities page, just ABOVE the row that starts\n'
        '  <div class="dmRespRow shg-day__register" (the "Ready to start your journey?" form).\n'
        '  Styles are in base.css and the growing plant is drawn by site.js, so nothing else to link.\n'
        '  Each step is one text widget: bold first line = the step\'s title.\n'
        '-->\n' + head + '\n' + journey + '\n')
out = ROOT / 'duda/grow/after/grow-rows.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(html)
ids = re.findall(r'\bid="(\d+)"', html)
print(f'{out.name}: {len(ids)} ids, unique={len(ids) == len(set(ids))}')
