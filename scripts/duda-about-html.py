"""Generates duda/about/after/about.html (editor-safe About us page).

Same approach as the Contact page: every editable block is ONE Duda text or image widget with its
styling class on the widget itself; content inside is plain text, bold, links and line breaks.
Only verified facts are used; nothing invented goes live (team: only Gary Hillery is named).
Run: python3 scripts/duda-about-html.py
"""
import pathlib, random, re, urllib.request

try:
    live = urllib.request.urlopen('https://www.sunderlandhomegrown.co.uk/our-team', timeout=20).read().decode('utf8', 'ignore')
except Exception:
    live = ''
taken = set(re.findall(r'\bid="(\d+)"', live))
random.seed(1716942098)

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

hero = row('shg-about__hero',
    col('large-6 medium-12 small-12', 'shg-about__intro',
        text('shg-about__title', 'About us', 'h1'),
        text('shg-about__lead', 'Sunderland Home Grown is a community interest company. Since 2017 we have turned a former council maintenance site in Thompson Park into a nursery, garden centre and training site.'),
        text('shg-about__button', '<a href="/contact">Come and see us</a>')),
    col('large-6 medium-12 small-12', 'shg-about__hero-media',
        image('shg-leaf-soft shg-about__hero-img', C + '20220616_091531.jpg', 'Two members of the Home Grown team holding up full hanging baskets in the nursery.')))

story = row('shg-about__story',
    col('large-5 medium-12 small-12', 'shg-about__story-text',
        text('shg-about__h2', 'From bare ground to growing', 'h2'),
        text('shg-about__body', 'In 2017 we took on a former council maintenance site in Thompson Park, Southwick, and started clearing it.<br/><br/>Support from Power to Change transformed the site. Today it has polytunnels, raised beds, a garden centre and a training base.<br/><br/>Our plants now grow at Durham Cathedral, Lumley Castle, Palace Green and Sherburn Village. More importantly, so do the people who raise them.')),
    col('large-7 medium-12 small-12', 'shg-about__story-media',
        image('shg-leaf-soft shg-about__wide', C + '20161003_092150.jpg', 'A digger clearing a large heap of soil on bare ground: the site before work began.'),
        text('shg-about__caption', 'Where it started: clearing the site.'),
        image('shg-leaf-r shg-about__wide', C + '20220408_151811.jpg', 'The garden centre today, full of shrubs and flowering plants, with the shop building behind.'),
        text('shg-about__caption', 'The garden centre today.')))

what = row('shg-about__what',
    col('large-3 medium-12 small-12', 'shg-about__what-head', text('shg-about__h2', 'What we do', 'h2')),
    col('large-3 medium-4 small-12', 'shg-about__tile shg-about__tile--leaf',
        text('shg-about__tile-title', 'A garden centre and plant nursery'),
        text('shg-about__tile-text', 'Retail and wholesale bedding, hanging baskets and perennials, grown on site.')),
    col('large-3 medium-4 small-12', 'shg-about__tile shg-about__tile--gold',
        text('shg-about__tile-title', 'Therapeutic horticulture'),
        text('shg-about__tile-text', 'Training and work for young people and adults with learning disabilities and mental health challenges.')),
    col('large-3 medium-4 small-12', 'shg-about__tile shg-about__tile--berry',
        text('shg-about__tile-title', 'A community hub'),
        text('shg-about__tile-text', 'Interest groups, workshops and community gardening in Southwick, Fulwell and the city centre.')))

quote = row('shg-about__quote',
    col('large-12 medium-12 small-12', 'shg-about__quote-col',
        text('shg-about__quote-text', 'Young people “always leave with a big smile on their face.”'),
        text('shg-about__quote-cite', 'Gary Hillery, Manager and Director')))

team_head = row('shg-about__team-head',
    col('large-12 medium-12 small-12', 'shg-about__head',
        text('shg-about__h2', 'The team', 'h2'),
        text('shg-about__lead', 'Our health mentors and horticultural trainer work alongside everyone who comes here.')))
team = row('shg-about__team',
    col('large-3 medium-4 small-6', 'shg-about__person',
        image('shg-leaf shg-about__portrait', C + 'Sunderland_Homegrown_Mainlogo+circle+colour.jpg', 'Sunderland Home Grown logo (replace with a photo of Gary)'),
        text('shg-about__person-name', 'Gary Hillery'),
        text('shg-about__person-role', 'Manager and Director')))

site_points = ['A community workshop', 'A commercial glasshouse', 'A classroom and training centre',
               'Tarmacked paths for wheelchair access', 'An off-grid garden centre with solar power and rainwater harvesting', 'A polytunnel']
site = row('shg-about__site',
    col('large-5 medium-12 small-12', 'shg-about__site-text',
        text('shg-about__h2', 'Our site', 'h2'),
        text('shg-about__lead', 'A Youth Investment Fund grant of over £468,000 is funding new facilities and training for young people, including:'),
        *[text('shg-about__point', p) for p in site_points]),
    col('large-7 medium-12 small-12', 'shg-about__site-media',
        image('shg-leaf-soft shg-about__wide', C + '20220406_150924.jpg', 'A long polytunnel with metal staging full of young plants.')))

gallery_items = [
    ('293257885_1131507570902878_3452411455125337265_n-60ab1dd9.jpg', 'Beekeepers inspecting a frame of honeycomb.', 'Beekeepers inspecting the hive.'),
    ('288018422_761800808167117_2606533825217059722_n.webp', 'Hanging baskets of red and purple petunias.', 'Hanging baskets ready for sale.'),
    ('IMG_3377.png', 'Two people holding up a wooden bird box they made.', 'A bird box from the joinery workshop.'),
    ('20220801_081919.jpg', 'Large squash plants filling a polytunnel bed.', 'Squash taking over the polytunnel.'),
    ('IMG_20220322_084417-10f6db23-7603fe64.jpg', 'Trays of primroses in many bright colours.', 'Spring primroses on the benches.'),
    ('IMG_20220216_135314-bccdc096.jpg', 'Four people smiling as they plant up pots together.', 'Planting up in the workshop.'),
]
gallery_head = row('shg-about__gallery-head', col('large-12 medium-12 small-12', 'shg-about__head', text('shg-about__h2', 'Gallery', 'h2')))
gallery = row('shg-about__gallery',
    *[col('large-4 medium-4 small-6', 'shg-about__shot',
          image('shg-leaf' if i % 2 == 0 else 'shg-leaf-r', C + f, alt),
          text('shg-about__caption', cap)) for i, (f, alt, cap) in enumerate(gallery_items)])

cta = row('shg-about__cta',
    col('large-7 medium-12 small-12', 'shg-about__cta-text', text('shg-about__h2', 'Come and see us', 'h2')),
    col('large-5 medium-12 small-12', 'shg-about__cta-actions',
        text('shg-about__button', '<a href="/contact">Contact and find us</a>'),
        text('shg-about__button shg-about__button--quiet', '<a href="/day-opportunities">Day opportunities</a>')))

html = f'''<!-- *** ADD OR EDIT HTML INSIDE OF THE dmRespCol DIVS, SEE DOCUMENTATION FOR GUIDELINES *** -->
<!--
  Sunderland Home Grown redesign: ABOUT US page (editor-safe)
  Replaces the whole page HTML. Styled by about.css (linked in this page's Head HTML).
  Every block is a normal Duda text or image widget: edit words, links and photos in the editor.
  To add a team member: copy Gary's column in the editor, then change the photo, name and role.
-->
<div dm:templateorder="170" class="dmHomeRespTmpl mainBorder dmRespRowsWrapper dmFullRowRespTmpl shg-about" id="1716942098">
{hero}
{story}
{what}
{quote}
{team_head}
{team}
{site}
{gallery_head}
{gallery}
{cta}
</div>
'''
out = pathlib.Path(__file__).resolve().parent.parent / 'duda/about/after/about.html'
out.write_text(html)
ids = re.findall(r'\bid="(\d+)"', html)
print(f'{out.name}: {len(ids)} ids, unique={len(ids) == len(set(ids))}, text widgets={html.count("dmNewParagraph")}, images={html.count("data-element-type=\"image\"")}')
