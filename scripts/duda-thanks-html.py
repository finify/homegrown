"""Generates duda/thanks/after/thanks.html (editor-safe "Special thanks" / Acknowledgements page).

Same approach as the About page: every editable block is ONE Duda text or image widget with its
styling class on the widget itself. Words are the page's own (lightly tidied); nothing is added
about a supporter that the old page didn't say. Styled by base.css (already linked site-wide).
Run: python3 scripts/duda-thanks-html.py
"""
import pathlib, random, re, urllib.request

try:
    live = urllib.request.urlopen('https://www.sunderlandhomegrown.co.uk/thanks-to', timeout=20).read().decode('utf8', 'ignore')
except Exception:
    live = ''
taken = set(re.findall(r'\bid="(\d+)"', live)) | {'1716942098'}
random.seed(20171716)

def nid():
    while True:
        n = str(random.randint(1500000000, 1999999999))
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

hero = row('shg-thanks__hero',
    col('large-7 medium-12 small-12', 'shg-thanks__intro',
        text('shg-thanks__eyebrow', 'Our supporters'),
        text('shg-thanks__title', 'Special thanks', 'h1')),
    col('large-5 medium-12 small-12', 'shg-thanks__intro-text',
        text('shg-thanks__lead', 'We are very grateful for the fantastic support from these organisations.'),
        text('shg-thanks__body', 'Meet the organisations who have helped make it all happen. They have seen big potential in every moment, and care deeply about what we do every day. This reflects the passion they have for our work in the community.')))
photo = row('shg-thanks__photo', col('large-12 medium-12 small-12', 'shg-thanks__photo-col',
    image('shg-thanks__hero-img', C + 'IMG_20210608_115423-7df48e44.jpg',
          'The Home Grown team and volunteers outside the garden centre, several of them holding new rucksacks.')))

supporters = [
    ('downloadsunderland+cc.png', 'Sunderland City Council logo', 'Sunderland City Council',
     'Sunderland City Council continue to support the project, from its development through to what it is today.'),
    ('EU2-4d816920-adfa849e-a3f8abd8-808af943-32d1b3e1.jpg', 'Sunderland CLLD and European Union, European Structural and Investment Funds logos',
     'Sunderland Community Led Local Development (CLLD)',
     'Currently funding our CLLD programme. The Sunderland Community Led Local Development Programme is a five-year programme to deliver local jobs and economic growth, supported with funding from the European Structural Investment Fund.'),
    ('coalfields-18465533.jpg', 'The Coalfields Regeneration Trust logo', 'Coalfields Regeneration Trust',
     'Support from the Coalfields Regeneration Trust helps employ a member of staff to work with and train local volunteers.'),
    ('Barclays-22d10348-b68e9c02-0b53feb3.jpg', 'Barclays logo', 'Barclays',
     'We are still working with Barclays. Their staff offer a wide range of professional help, advising our business on everything from marketing to accounts.'),
]
cards_head = row('shg-thanks__head', col('large-12 medium-12 small-12', 'shg-thanks__head-col',
    text('shg-thanks__h2', 'How they help', 'h2')))
cards = row('shg-thanks__cards',
    *[col('large-6 medium-6 small-12', 'shg-thanks__card',
          image('shg-thanks__logo', C + f, alt),
          text('shg-thanks__name', name, 'h3'),
          text('shg-thanks__text', body)) for f, alt, name, body in supporters])

more = [
    ('big+issue.png', 'Big Issue Invest logo', 'Big Issue Invest'),
    ('Social_Investment_Business_Logo.png', 'Social Investment Business logo', 'Social Investment Business'),
    ('LOTTERY-COMMUNITY-FUND-LOGO.jpg', 'The National Lottery Community Fund logo', 'The National Lottery Community Fund'),
]
more_head = row('shg-thanks__head shg-thanks__head--more', col('large-12 medium-12 small-12', 'shg-thanks__head-col',
    text('shg-thanks__h2', 'With thanks also to', 'h2')))
more_row = row('shg-thanks__more',
    *[col('large-4 medium-4 small-12', 'shg-thanks__tile',
          image('shg-thanks__logo', C + f, alt),
          text('shg-thanks__tile-name', name)) for f, alt, name in more])

cta = row('shg-thanks__cta',
    col('large-7 medium-12 small-12', 'shg-thanks__cta-text',
        text('shg-thanks__h2', 'Interested in supporting our work?', 'h2'),
        text('shg-thanks__body', 'We would love to hear from you.')),
    col('large-5 medium-12 small-12', 'shg-thanks__cta-actions',
        text('shg-thanks__button', '<a href="/contact">Get in touch</a>')))

html = f'''<!-- *** ADD OR EDIT HTML INSIDE OF THE dmRespCol DIVS, SEE DOCUMENTATION FOR GUIDELINES *** -->
<!--
  Sunderland Home Grown redesign: SPECIAL THANKS page (page name in the editor: Acknowledgements, URL /thanks-to)
  Replaces the whole page HTML. Styled by base.css, which is already linked site-wide.
  Every block is a normal Duda text or image widget: edit words and logos in the editor.
  To add a supporter: copy a card (or a logo tile) in the editor, then change the logo, name and text.
-->
<div dm:templateorder="170" class="dmHomeRespTmpl mainBorder dmRespRowsWrapper dmFullRowRespTmpl shg-thanks" id="1716942098">
{hero}
{photo}
{cards_head}
{cards}
{more_head}
{more_row}
{cta}
</div>
'''
out = pathlib.Path(__file__).resolve().parent.parent / 'duda/thanks/after/thanks.html'
out.write_text(html)
ids = re.findall(r'\bid="(\d+)"', html)
print(f'{out.name}: {len(ids)} ids, unique={len(ids) == len(set(ids))}, text widgets={html.count("dmNewParagraph")}, images={html.count("data-element-type=\"image\"")}')
