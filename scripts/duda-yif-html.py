"""Generates duda/youth-investment-fund/after/youth-investment-fund.html (editor-safe redesign).

Words are the old page's own (lightly tidied, split into headed sections); nothing new is claimed.
Dropped: "We're aiming to finish all the building work by early autumn 2023" (out of date).
Styled by base.css (already linked site-wide). Run: python3 scripts/duda-yif-html.py
"""
import glob, pathlib, random, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'duda/youth-investment-fund/after/youth-investment-fund.html'
taken = set()
for f in glob.glob(str(ROOT / 'duda/**/*.html'), recursive=True):
    if pathlib.Path(f) != OUT:
        taken |= set(re.findall(r'\b1\d{9}\b', open(f).read()))
random.seed(46800)

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
STORY = 'https://youthinvestmentfund.org.uk/resource/come-in-and-smell-the-roses-nurturing-wellbeing-in-sunderland/'

hero = row('shg-yif__hero',
    col('large-7 medium-12 small-12', 'shg-yif__hero-text',
        image('shg-yif__logo', C + 'Youth-Investment-Fund-YIF-e1659353410541.png', 'Youth Investment Fund'),
        text('shg-yif__title', 'Over £468K to help young people thrive', 'h1'),
        text('shg-yif__lead', f'A <a href="{STORY}" target="_blank" rel="noopener">Youth Investment Fund</a> grant of over £468K will create exciting new initiatives to help young people thrive.'),
        text('shg-yif__body', 'Sunderland Home Grown is a rich environment to help young people and adults with learning disabilities and mental health problems to thrive and enjoy life, by creating training and employment opportunities and promoting social and therapeutic horticulture.'),
        text('shg-yif__button', f'<a href="{STORY}" target="_blank" rel="noopener">Read our story on the Youth Investment Fund website</a>')),
    col('large-5 medium-12 small-12', 'shg-yif__hero-media',
        image('shg-yif__hero-img', C + 'IMG_5888-36cbe15a.jpeg', 'A young man watering rows of young plants with a hose in the polytunnel.')))

quote1 = row('shg-yif__quote shg-yif__quote--forest',
    col(FULL, 'shg-yif__quote-col',
        text('shg-yif__quote-text', '“Everyone who comes to Sunderland Home Grown has a unique contribution to make and no matter what they do, whether they are potting plants or working in the shop, they all play a significant role in growing our produce. Young people love being here and get real joy out of seeing that they have grown something and made it happen. It’s quite remarkable given that many young people who live in the city don’t know how vegetables are produced. And everyone who comes here always leaves with a big smile on their face.”'),
        image('shg-yif__avatar', C + 'IMG_20211125_143711_2CS-1b466a43.jpg', 'Gary Hillery smiling in a Home Grown beanie hat in the greenhouse.'),
        text('shg-yif__quote-name', '<b>Gary Hillery</b><br/>Manager and Director, Sunderland Home Grown CIC')))

offer = row('shg-yif__split',
    col('large-6 medium-12 small-12', 'shg-yif__split-text',
        text('shg-yif__eyebrow', 'Training and work placements'),
        text('shg-yif__h2', 'What we offer young people', 'h2'),
        text('shg-yif__body', 'We offer young people accredited and non-accredited horticulture training programmes and supported work placements, including:'),
        text('shg-yif__chips', '<ul><li>Practice-based horticulture</li><li>Site maintenance</li><li>Producing plants and produce</li><li>Retail experience</li><li>Dealing with the public</li></ul>'),
        text('shg-yif__body', 'Young people are supported by health mentors and a horticultural trainer. Over the years we have developed links with schools, colleges and academies, and can offer young people new life experiences as well as the joy of growing produce.')),
    col('large-6 medium-12 small-12', 'shg-yif__split-media',
        image('shg-yif__img', C + 'IMG_20220216_135314-bccdc096.jpg', 'Four people smiling as they plant up pots together.')))

build_head = row('shg-yif__head',
    col('large-6 medium-12 small-12', 'shg-yif__head-title',
        text('shg-yif__eyebrow', 'What the grant is building'),
        text('shg-yif__h2', 'New spaces to learn, work and grow', 'h2')),
    col('large-6 medium-12 small-12', 'shg-yif__head-lead',
        text('shg-yif__lead-dark', 'Spaces designed to cater to the diverse needs and aspirations of our community members.')))
builds = [
    ('workshop', 'A community workshop'),
    ('glass', 'A spacious commercial glasshouse'),
    ('class', 'A classroom and training centre'),
    ('access', 'Tarmacked outdoor areas, smoother for wheelchair users'),
    ('solar', 'An off-grid garden centre, with solar panels on the storage containers'),
    ('water', 'A huge water tank to collect rainwater'),
]
build_row = row('shg-yif__builds',
    col(FULL, 'shg-yif__build-list', *[text(f'shg-yif__build shg-yif__build--{k}', t) for k, t in builds]))

spaces = row('shg-yif__split shg-yif__split--flip',
    col('large-6 medium-12 small-12', 'shg-yif__split-media',
        image('shg-yif__img', C + 'Shop+Build.png', 'Three members of the team waving from the doorway and windows of the new garden centre shop building, with a small dog at the door.')),
    col('large-6 medium-12 small-12', 'shg-yif__split-text',
        text('shg-yif__h3', 'A workshop, glasshouse and training centre', 'h3'),
        text('shg-yif__body', 'We are constructing a vibrant community workshop, a spacious commercial glasshouse, and a classroom and training centre.'),
        text('shg-yif__body', 'In our commitment to inclusivity, we’re taking additional measures to ensure accessibility for everyone. Our outdoor areas are being tarmacked, creating a smoother and more user-friendly experience, particularly for wheelchair users.')))

garden = row('shg-yif__split',
    col('large-6 medium-12 small-12', 'shg-yif__split-text',
        text('shg-yif__h3', 'An off-grid, sustainable garden centre', 'h3'),
        text('shg-yif__body', 'The second part of the initiative is a new garden centre designed to be off-grid and sustainable, using fewer resources. Our storage containers will have solar panels, and there’s a huge water tank to collect rainwater.'),
        text('shg-yif__body', 'Our new polytunnel, canopy and fencing have already been set up, creating a nurturing environment for our plants and visitors alike. The whole garden centre shop was assembled from a flat-pack kit, an efficient way of building that fits our sustainability goals.')),
    col('large-6 medium-12 small-12', 'shg-yif__split-media',
        image('shg-yif__img', C + 'Polytunnels-5997a5ce-a5e2d411.png', 'Two large new white polytunnels joined by a canopy, on fresh tarmac under a blue sky.')))

quote2 = row('shg-yif__quote shg-yif__quote--gold',
    col(FULL, 'shg-yif__quote-col',
        text('shg-yif__quote-text', '“The news of securing a Youth Investment Fund grant is still sinking in. We’re such a small company and the difference it will make is mind-blowing. It means we can reach more young people, create more joy, and be there for future generations. Sunderland Home Grown is a place of mindfulness and wellness: it’s not just about learning new skills, it’s also a chance to come in and smell the roses.”')))

photos = row('shg-yif__photos',
    col('large-6 medium-6 small-12', 'shg-yif__photo',
        image('shg-yif__img', C + '293257885_1131507570902878_3452411455125337265_n-60ab1dd9.jpg', 'Two people in beekeeping suits inspecting a frame of honeycomb.')),
    col('large-6 medium-6 small-12', 'shg-yif__photo',
        image('shg-yif__img', C + 'IMG_20211201_114040-40d4b2e3-30ddf696.jpg', 'A smiling woman in a Home Grown fleece giving a thumbs up in the potting shed.')))

cta = row('shg-yif__cta',
    col('large-7 medium-12 small-12', 'shg-yif__cta-text',
        text('shg-yif__h2', 'Know a young person who could thrive here?', 'h2'),
        text('shg-yif__lead-light', 'Talk to us about training, work placements and what a day here looks like.')),
    col('large-5 medium-12 small-12', 'shg-yif__cta-actions',
        text('shg-yif__button', '<a href="/contact">Get in touch</a>'),
        text('shg-yif__button shg-yif__button--light', '<a href="tel:+441915499444">Call 0191 549 9444</a>')))

html = f'''<!-- *** ADD OR EDIT HTML INSIDE OF THE dmRespCol DIVS, SEE DOCUMENTATION FOR GUIDELINES *** -->
<!--
  Sunderland Home Grown redesign: YOUTH INVESTMENT FUND page (/youth-investment-fund)
  Replaces the whole page HTML. Styled by base.css (already linked site-wide).
  Every block is a normal Duda text or image widget: edit words and photos in the editor.
-->
<div dm:templateorder="170" class="dmHomeRespTmpl mainBorder dmRespRowsWrapper dmFullRowRespTmpl shg-yif" id="1716942098">
{hero}
{quote1}
{offer}
{build_head}
{build_row}
{spaces}
{garden}
{quote2}
{photos}
{cta}
</div>
'''
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html)
ids = re.findall(r'\bid="(\d+)"', html)
print(f'{OUT.name}: {len(ids)} ids, unique={len(ids) == len(set(ids))}, text widgets={html.count("dmNewParagraph")}')
