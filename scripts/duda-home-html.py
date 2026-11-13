"""Generates duda/home/after/home.html (editor-safe Home page with a video hero).

Same approach as About and Contact: every editable block is ONE Duda text or image widget with its
styling class on the widget itself; content inside is plain text, bold, links and line breaks.
Duda's own contact form is kept exactly as it was (same ids and hidden settings), with a class added.
Only facts from the live site are used.

The hero video is not in the HTML (Duda's editor would strip an iframe). site.js finds the row with
class shg-video-hero, reads the YouTube link from the "Watch our film" text widget, and plays it
muted behind the text. Change that link in the editor to change the video.

Run: python3 scripts/duda-home-html.py
"""
import pathlib, random, re, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
try:
    live = urllib.request.urlopen('https://www.sunderlandhomegrown.co.uk/', timeout=20).read().decode('utf8', 'ignore')
except Exception:
    live = ''
before = (ROOT / 'duda/home/before/home.html').read_text()
taken = set(re.findall(r'\bid="(\d+)"', live)) | set(re.findall(r'\bid="(\d+)"', before))
random.seed(20171)

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

FULL = 'large-12 medium-12 small-12'
C = 'https://irp.cdn-website.com/0432dc74/dms3rep/multi/'
VIDEO = 'https://www.youtube.com/watch?v=aIMDsVXcNeE'
PHONE = '0191 549 9444'
TEL = 'tel:+441915499444'

# ---------- Hero: video background (added by site.js), poster photo, tagline ----------
hero = row('shg-home__hero shg-video-hero',
    col(FULL, 'shg-home__hero-inner',
        image('shg-home__poster', C + '20220616_091531.jpg', ''),
        text('shg-home__eyebrow', 'Sunderland Home Grown CIC, Thompson Park'),
        text('shg-home__title', 'Growing plants, nurturing people since 2017.', 'h1'),
        text('shg-home__lead', 'Therapeutic horticulture, training and a garden centre open to everyone, on a former council yard in Southwick, Sunderland.'),
        text('shg-home__button', '<a href="/contact">Get in touch</a>'),
        text('shg-home__button shg-home__button--glass', '<a href="/store">Visit the shop</a>'),
        text('shg-home__video-link shg-video-link', f'<a href="{VIDEO}" target="_blank" rel="noopener">Watch our film with The Big Issue</a>')))

# ---------- Statement ----------
intro = row('shg-home__intro',
    col('large-7 medium-12 small-12', 'shg-home__intro-text',
        text('shg-home__statement', 'We grow plants and people.', 'h2'),
        text('shg-home__body', 'We’re a community interest company providing social and therapeutic horticulture and horticulture training for young people and adults with learning disabilities and mental health challenges.<br/><br/>We’ve turned a former council maintenance site in Thompson Park into a growing and training facility that’s open to everyone.')),
    col('large-5 medium-12 small-12', 'shg-home__intro-media',
        image('shg-leaf-soft shg-home__intro-img', C + '20230522_115601--281-29-11c20b21-297c9d0e-5a74a4e1.jpg', 'Someone working among young tomato plants tied to tall canes in a polytunnel, with hanging baskets overhead.')))

# ---------- Who are you here for? ----------
def route(mod, img, alt, title, body, link):
    return col('large-4 medium-4 small-12', f'shg-home__route shg-home__route--{mod}',
        image('shg-leaf-soft shg-home__route-img', C + img, alt),
        text('shg-home__route-title', title, 'h3'),
        text('shg-home__route-text', body),
        text('shg-home__route-link', link))

routes_head = row('shg-home__routes-head',
    col(FULL, 'shg-home__head',
        text('shg-home__h2', 'Who are you here for?', 'h2'),
        text('shg-home__lead-dark', 'Choose the route that fits, and we’ll take it from there.')))
routes = row('shg-home__routes',
    route('leaf', 'IMG_20211201_114040-40d4b2e3-30ddf696.jpg', 'A smiling woman in a Home Grown fleece giving a thumbs up in the potting shed.', 'For individuals and families',
          'Supported days of gardening, training and work experience in a relaxed, friendly place.',
          '<a href="/day-opportunities">Ask about a place</a>'),
    route('gold', 'IMG_4422.jpeg', '', 'For professionals and referrers',
          'Places for young people and adults with learning disabilities and mental health challenges.',
          '<a href="/day-opportunities#register">Make a referral</a>'),
    route('berry', 'IMG_20220322_084417-10f6db23-7603fe64.jpg', '', 'For gardeners and visitors',
          'Bedding, hanging baskets and perennials, grown here. Open seven days a week.',
          '<a href="/store">Visit the shop</a>'))

# ---------- A day here (forest band, cards swipe sideways on phones) ----------
def day(img, alt, title, body):
    return col('large-3 medium-6 small-12', 'shg-home__card',
        image('shg-leaf-soft shg-home__card-img', C + img, alt),
        text('shg-home__card-title', title, 'h3'),
        text('shg-home__card-text', body))

day_head = row('shg-home__day-head',
    col('large-6 medium-12 small-12', 'shg-home__day-title', text('shg-home__h2', 'What a day here looks like', 'h2')),
    col('large-6 medium-12 small-12', 'shg-home__day-intro',
        text('shg-home__lead-light', 'A relaxed and friendly place to work, with a variety of tasks through the day in the nursery, the vegetable gardens and the garden centre.')))
days = row('shg-home__days',
    day('IMG_5888-36cbe15a.jpeg', 'A young man watering rows of young plants with a hose in the polytunnel.',
        'In the nursery', 'Potting, watering and caring for bedding and perennials in the polytunnels.'),
    day('20220831_095855.jpg', 'Crates of freshly picked squash, peppers, chard and a pumpkin laid out along a path, with two growers behind.',
        'Growing food', 'Fruit and vegetables in the raised beds and polytunnels.'),
    day('IMG_20210523_091218.jpg', 'The open doorway of the Home Grown shop, with pots, gifts and a small dog sitting inside.',
        'In the garden centre', 'Retail work experience, helping deliver our high standard of customer service.'),
    day('293257885_1131507570902878_3452411455125337265_n-60ab1dd9.jpg', 'Two people in beekeeping suits inspecting a frame of honeycomb.',
        'With the bees', 'Beekeeping and beehive management.'))

# ---------- Our plants grow at ----------
def place(name, note):
    return col('large-3 medium-6 small-6', 'shg-home__place',
        text('shg-home__place-name', name),
        text('shg-home__place-note', note))

proof_head = row('shg-home__proof-head',
    col('large-6 medium-12 small-12', 'shg-home__proof-title', text('shg-home__h2', 'Our plants grow at', 'h2')),
    col('large-6 medium-12 small-12', 'shg-home__proof-intro',
        text('shg-home__lead-dark', 'Our team grow a huge amount of spring and summer bedding, hanging baskets and perennials, for retail and wholesale.')))
proof = row('shg-home__proof',
    place('Durham Cathedral', 'Durham'),
    place('Palace Green', 'World Heritage Site, Durham'),
    place('Lumley Castle', 'Chester-le-Street'),
    place('Sherburn Village', 'Gold Award, Britain in Bloom'))

# ---------- Groups anyone can join ----------
groups = row('shg-home__groups',
    col('large-6 medium-12 small-12', 'shg-home__groups-text',
        text('shg-home__h2', 'Groups anyone can join', 'h2'),
        text('shg-home__lead-dark', 'We work with Friends of Thompson Park, Sunderland City Council and other community groups in Southwick, Fulwell and the city centre.'),
        *[text('shg-home__group', g) for g in [
            '<a href="/fruit-vegetables-group">Fruit and vegetable growing</a>',
            'Community gardening',
            'Beekeeping and beehive management',
            'Local history and heritage: the Thompson Park Heritage group meets twice a month at the Park Café',
            'Health and wellbeing',
            'Healthy eating']],
        text('shg-home__button shg-home__button--forest', '<a href="/contact">Ask about a group</a>')),
    col('large-6 medium-12 small-12', 'shg-home__groups-media',
        image('shg-leaf-r shg-home__groups-img', C + '20230522_113141-8d0bb07d-e5602a81-f6f71114.jpg', 'Five members of a community group standing behind a raised bed of young plants, one watering with a hose.')))

# ---------- Quote ----------
quote = row('shg-home__quote',
    col(FULL, 'shg-home__quote-col',
        text('shg-home__quote-text', 'Young people “always leave with a big smile on their face.”'),
        text('shg-home__quote-cite', 'Gary Hillery, Manager and Director')))

# ---------- Youth Investment Fund ----------
yif = row('shg-home__yif',
    col('large-6 medium-12 small-12', 'shg-home__yif-media',
        image('shg-leaf-soft shg-home__yif-img', C + 'Polytunnels-5997a5ce-a5e2d411.png', 'Two large new white polytunnels on a cleared, gravelled site under a blue sky.')),
    col('large-6 medium-12 small-12', 'shg-home__yif-text',
        text('shg-home__h2', 'Growing for young people', 'h2'),
        text('shg-home__body', 'A Youth Investment Fund grant is helping us expand, with new facilities and programmes designed around the needs of young people in our community.'),
        text('shg-home__button shg-home__button--forest', '<a href="/youth-investment-fund">About the Youth Investment Fund</a>')))

# ---------- Get in touch: Duda's own form, unchanged ----------
m = re.search(r'<div class="u_1176957292 dmform[^"]*"[^>]*>', before)
start, depth = m.start(), 0
for t in re.finditer(r'<div\b|</div>', before[start:]):
    depth += 1 if t.group() != '</div>' else -1
    if depth == 0:
        end = start + t.end()
        break
form = before[start:end].replace('class="u_1176957292 dmform default native-inputs"',
                                 'class="u_1176957292 dmform default native-inputs shg-home__form"', 1)
for name, ac in [('dmform-0', 'name'), ('dmform-1', 'email'), ('dmform-2', 'tel')]:
    form = re.sub(rf'(<input type="[a-z]+" class="" name="{name}")', rf'\1 autocomplete="{ac}"', form, count=1)
assert form.count('<div') == form.count('</div>')

contact = row('shg-home__contact',
    col('large-5 medium-12 small-12', 'shg-home__contact-text',
        text('shg-home__h2', 'Thinking about a place for someone?', 'h2'),
        text('shg-home__lead-dark', 'Send us a message or give us a call. There’s no commitment, and we’ll explain everything.'),
        text('shg-home__call', f'<a href="{TEL}">Call {PHONE}</a>')),
    col('large-7 medium-12 small-12', 'shg-home__contact-form', form))

# ---------- Day opportunities call to action (made by scripts/duda-day-html.py) ----------
_cta_file = pathlib.Path(__file__).resolve().parent.parent / 'duda/home/after/day-cta-row.html'
day_cta = re.sub(r'^<!--[\s\S]*?-->\n', '', _cta_file.read_text()).strip() if _cta_file.exists() else ''

html = f'''<div dm:templateorder="170" class="dmHomeRespTmpl mainBorder dmRespRowsWrapper dmFullRowRespTmpl shg-home" id="1716942098">
<!--
  SUNDERLAND HOME GROWN REDESIGN: HOME PAGE
  Replaces the whole home page HTML. Styled by home.css (linked in this page's Head HTML).
  The hero video comes from site.js: change the "Watch our film" link to change the video.
-->
{hero}
{day_cta}
{intro}
{routes_head}
{routes}
{day_head}
{days}
{proof_head}
{proof}
{groups}
{quote}
{yif}
{contact}
</div>
'''
out = ROOT / 'duda/home/after/home.html'
out.write_text(html)
ids = re.findall(r'\bid="(\d+)"', html)
print(f'{out.name}: {len(ids)} ids, unique={len(ids) == len(set(ids))}, text widgets={html.count("dmNewParagraph")}, '
      f'images={html.count(chr(100) + "ata-element-type=" + chr(34) + "image" + chr(34))}')
# Column sizes in every row must add up to a multiple of 12 (Duda's editor checks this)
for rm in re.finditer(r'<div class="dmRespRow ([^"]*)"', html):
    seg = html[rm.end():]
    nx = re.search(r'<div class="dmRespRow ', seg)
    seg = seg[:nx.start()] if nx else seg
    cols = re.findall(r'class="dmRespCol ([^"]*)"', seg)
    for k in ('large', 'medium', 'small'):
        total = sum(int(re.search(k + r'-(\d+)', c).group(1)) for c in cols)
        assert total % 12 == 0, (rm.group(1), k, total)
print('column sizes ok')
