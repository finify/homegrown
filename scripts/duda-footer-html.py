"""Generates duda/footer/after/footer.html.

Editor-safe structure: every editable block is ONE Duda widget whose outer element carries the
styling class (Duda keeps those). Content inside is plain text, bold, links and line breaks only,
because Duda's text editor rewrites anything inside a widget when you edit it.
Run: python3 scripts/duda-footer-html.py  (ids are checked against the live site to avoid clashes)
"""
import pathlib, random, re, urllib.request

try:
    live = urllib.request.urlopen('https://www.sunderlandhomegrown.co.uk/', timeout=20).read().decode('utf8', 'ignore')
except Exception:
    live = ''
taken = set(re.findall(r'\bid="(\d+)"', live))
random.seed(19430484)

def nid():
    while True:
        n = str(random.randint(1500000000, 1999999999))
        if n not in taken:
            taken.add(n)
            return n

def text(cls, inner, align='left'):
    return (f'<div class="dmNewParagraph {cls}" data-element-type="paragraph" dmle_widget="paragraph" '
            f'data-uialign="{align}" data-version="5" id="{nid()}" style="transition:opacity 1s ease-in-out;">\n{inner}\n</div>')

def image(cls, src, alt):
    return (f'<div class="imageWidget align-center {cls}" editablewidget="true" data-element-type="image" '
            f'dmle_widget="image" data-widget-type="image" id="{nid()}">\n <a id="{nid()}">\n'
            f'  <img src="{src}" alt="{alt}" id="{nid()}" class="" data-dm-image-path="{src}"/>\n </a>\n</div>')

def col(classes, extra, *widgets):
    body = '\n'.join(widgets)
    return f' <div class="dmRespCol {classes} {extra}" id="{nid()}">\n  <!-- *** INSERT YOUR HTML BELOW *** -->\n{body}\n </div>'

def row(extra, *cols):
    return (f'<div class="dmRespRow {extra}" id="{nid()}">\n <div class="dmRespColsWrapper" id="{nid()}">\n'
            + '\n'.join(cols) + '\n </div>\n</div>')

def link_list(items):
    return '<br/>\n'.join(f'<a href="{h}">{t}</a>' for t, h in items)

LEAVES = 'https://finify.github.io/homegrown/duda/footer-leaves.svg'
LOTTERY = 'https://irp.cdn-website.com/0432dc74/dms3rep/multi/LOTTERY-COMMUNITY-FUND-LOGO.jpg'
YIF = 'https://irp.cdn-website.com/0432dc74/dms3rep/multi/Youth-Investment-Fund-YIF-e1659353410541.png'
link_col = lambda title, items: col('large-2 medium-4 small-12', 'shg-footer__col',
                                    text('shg-footer__heading', title), text('shg-footer__links', link_list(items)))

html = f'''<!-- *** ADD OR EDIT HTML INSIDE OF THE dmRespCol DIVS, SEE DOCUMENTATION FOR GUIDELINES *** -->
<!--
  Sunderland Home Grown redesign: FOOTER (editor-safe version)
  Replaces the whole footer file. Used on desktop, tablet AND phones.
  Every block is a normal Duda text or image widget: click it in the editor to change words,
  links or pictures. The design comes from the widget's class, so editing never loses it.
-->
<div dm:templateorder="250" class="dmFooterResp generalFooter shg-footer" id="1943048428">
{row('shg-footer__brand',
     col('large-8 medium-8 small-12', 'shg-footer__col',
         text('shg-footer__name', 'Sunderland<br/>Home Grown'),
         text('shg-footer__tagline', 'Growing plants, nurturing people. In Thompson Park since 2017.')),
     col('large-4 medium-4 small-12', 'shg-footer__col shg-footer__mark', image('shg-footer__leaves', LEAVES, '')))}
{row('shg-footer__nav',
     link_col('Visit', [('Garden centre', '/garden-centre'), ("What's on", '/whats-on'), ('Shop &amp; book workshops', '/store'), ('Contact &amp; find us', '/contact')]),
     link_col('Take part', [('Day opportunities', '/day-opportunities'), ('Make a referral', '/contact'), ('Community groups', '/community'), ('Free membership', 'http://eepurl.com/icXnHv')]),
     link_col('About', [('Our story', '/about'), ('News &amp; growing tips', '/blog'), ('Gallery', '/gallery'), ('Supporters', '/thanks-to')]),
     col('large-3 medium-6 small-12', 'shg-footer__col',
         text('shg-footer__heading', 'Opening times'),
         text('shg-footer__info', '<b>Monday to Friday</b><br/>10am to 4pm<br/><br/><b>Saturday and Sunday</b><br/>9:30am to 3:30pm')),
     col('large-3 medium-6 small-12', 'shg-footer__col',
         text('shg-footer__heading', 'Find us'),
         text('shg-footer__info', 'Sunderland Home Grown CIC<br/>Thompson Park, Southwick<br/>Sunderland SR5 1SF'),
         text('shg-footer__links shg-footer__contact', '<a href="tel:+441915499444"><b>0191 549 9444</b></a><br/>\n<a href="mailto:deb.homegrown@aol.com">deb.homegrown@aol.com</a><br/>\n<a href="mailto:gary.homegrown@aol.com">gary.homegrown@aol.com</a><br/>\n<a href="https://www.facebook.com/sunderlandhomegrown" target="_blank" rel="noopener">Follow us on Facebook</a>')))}
{row('shg-footer__support', col('large-12 medium-12 small-12', 'shg-footer__col', text('shg-footer__support-heading', 'Supported by')))}
{row('shg-footer__support-tiles',
     col('large-2 medium-4 small-6', 'shg-footer__tile shg-footer__tile--logo', image('shg-footer__logo', LOTTERY, 'The National Lottery Community Fund')),
     col('large-2 medium-4 small-6', 'shg-footer__tile shg-footer__tile--logo', image('shg-footer__logo', YIF, 'Youth Investment Fund')),
     *[col('large-2 medium-4 small-6', 'shg-footer__tile', text('shg-footer__tile-text', n)) for n in ['Sunderland City Council', 'Coalfields Regeneration Trust', 'Barclays', 'Power to Change']])}
{row('shg-footer__base',
     col('large-6 medium-6 small-12', 'shg-footer__col', text('shg-footer__copy', '© Sunderland Home Grown CIC. A community interest company.')),
     col('large-6 medium-6 small-12', 'shg-footer__col', text('shg-footer__legal', '<a href="/privacy-policy">Privacy policy</a> <a href="#">Back to top</a>', 'right')))}
</div>
'''
out = pathlib.Path(__file__).resolve().parent.parent / 'duda/footer/after/footer.html'
out.write_text(html)
ids = re.findall(r'\bid="(\d+)"', html)
print(f'{out.name}: {len(ids)} ids, unique={len(ids) == len(set(ids))}, text widgets={html.count("paragraph")//2}, images={html.count("data-element-type=\"image\"")}')
