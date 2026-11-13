"""Generates the Day opportunities (service users) page and the matching home page call to action.

  duda/day-opportunities/after/day-opportunities.html   the whole page (paste into a new page at /day-opportunities)
  duda/home/after/day-cta-row.html                      one row for the Home page

Words come from the team's day opportunities flyer (typos fixed, nothing added). Every editable
block is ONE Duda text or image widget with its class on the widget; the register form is Duda's
own form widget, built from the same markup as the Home page form.
Run: python3 scripts/duda-day-html.py
"""
import glob, pathlib, random, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
taken = set()
for f in glob.glob(str(ROOT / 'duda/**/*.html'), recursive=True):
    taken |= set(re.findall(r'\b1\d{9}\b', open(f).read()))
random.seed(2026_11_13)

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
TEL = 'tel:+441915499444'
PAGE = '/day-opportunities'

# ---------- Hero ----------
hero = row('shg-day__hero',
    col('large-7 medium-12 small-12', 'shg-day__hero-text',
        text('shg-day__eyebrow', 'Day opportunities for adults'),
        text('shg-day__title', 'What if the right place could help someone grow?', 'h1'),
        text('shg-day__lead', 'Meaningful work-based day opportunities for adults with disabilities and additional support needs.'),
        text('shg-day__button', '<a href="#register">Book a free trial visit</a>'),
        text('shg-day__button shg-day__button--quiet', f'<a href="{TEL}">Call 0191 549 9444</a>'),
        text('shg-day__badges', '<ul><li>Established over 11 years</li><li>Free trial visits</li><li>Referrals welcome</li></ul>')),
    col('large-5 medium-12 small-12', 'shg-day__hero-media',
        image('shg-day__hero-img', C + 'Michelle+and+lesley.jpg',
              'Two women smiling under a striped parasol, one holding up a pot of white flowers she has planted.')))

# ---------- Intro + photo strip ----------
intro = row('shg-day__intro',
    col(FULL, 'shg-day__intro-col',
        text('shg-day__statement', 'For over 11 years, Sunderland Home Grown has provided meaningful work-based day opportunities for adults with disabilities and additional support needs. Based in the heart of Thompson Park, we help people develop practical skills, confidence, independence and friendships through real, purposeful activities in a welcoming community.')))
strip = row('shg-day__strip',
    col('large-4 medium-4 small-12', 'shg-day__shot',
        image('shg-day__shot-img', C + 'IMG_20220216_135314-bccdc096.jpg', 'Four people smiling as they plant up pots together.')),
    col('large-4 medium-4 small-12', 'shg-day__shot',
        image('shg-day__shot-img', C + 'IMG_20211201_114040-40d4b2e3-30ddf696.jpg', 'A smiling woman in a Home Grown fleece giving a thumbs up in the potting shed.')),
    col('large-4 medium-4 small-12', 'shg-day__shot',
        image('shg-day__shot-img', C + 'IMG_3377.png', 'Two men in the workshop with a wooden bird table they have built, one holding a drill.')))

# ---------- What you gain ----------
gains = [('confidence', 'Confidence'), ('independence', 'Independence'), ('skills', 'Practical work skills'),
         ('friends', 'New friendships'), ('routine', 'Routine'), ('wellbeing', 'Improved wellbeing'),
         ('purpose', 'A sense of purpose')]
gain_head = row('shg-day__head',
    col(FULL, 'shg-day__head-col', text('shg-day__h2', 'What you gain', 'h2')))
gain_row = row('shg-day__gains',
    col(FULL, 'shg-day__gain-list',
        *[text(f'shg-day__gain shg-day__gain--{k}', label) for k, label in gains]))

# ---------- Activities (forest band) ----------
acts = [('plants', 'Grow and care for plants and vegetables'),
        ('wood', 'Learn woodworking and construction'),
        ('arts', 'Explore arts and crafts with a qualified therapist'),
        ('bees', 'Care for bees and learn about their role'),
        ('nursery', 'Gain hands-on nursery experience')]
act_head = row('shg-day__acts-head',
    col('large-6 medium-12 small-12', 'shg-day__acts-title', text('shg-day__h2', 'Meaningful work-based activities', 'h2')),
    col('large-6 medium-12 small-12', 'shg-day__acts-intro',
        text('shg-day__lead-light', 'Real, purposeful work in our nursery, workshop, gardens and garden centre.')))
act_row = row('shg-day__acts',
    col(FULL, 'shg-day__act-list',
        *[text(f'shg-day__act shg-day__act--{k}', label) for k, label in acts]))

# ---------- Endorsements ----------
quotes_head = row('shg-day__head',
    col(FULL, 'shg-day__head-col', text('shg-day__h2', 'True endorsements', 'h2')))
quotes = row('shg-day__quotes',
    col('large-6 medium-6 small-12', 'shg-day__quote-col',
        text('shg-day__quote', '“Michelle has accessed our service since 2018. Michelle’s mam commented, ‘Her confidence and independence have greatly improved, she loves going to Sunderland Home Grown no matter what the weather.’”'),
        text('shg-day__quote-name', 'Michelle, with us since 2018')),
    col('large-6 medium-6 small-12', 'shg-day__quote-col',
        text('shg-day__quote', '“Andy first attended with his support worker but now attends with our staff supporting him. His carers noted a huge change in his attitude after being supported by our staff, noting that he feels like everyone else, and having a break from his carers has been a great improvement in his mental health and wellbeing.”'),
        text('shg-day__quote-name', 'Andy')))

# ---------- Why families choose us / referrals ----------
why = row('shg-day__why',
    col('large-6 medium-12 small-12', 'shg-day__panel',
        text('shg-day__h3', 'Why families choose us', 'h3'),
        text('shg-day__ticks', '<ul><li>Over 11 years’ experience</li><li>DBS-checked, experienced staff</li><li>A safe, welcoming environment</li><li>Trial visits available</li><li>Individual support available</li></ul>')),
    col('large-6 medium-12 small-12', 'shg-day__panel',
        text('shg-day__h3', 'Referrals welcome from', 'h3'),
        text('shg-day__dots', '<ul><li>Families</li><li>Local authorities</li><li>Social workers</li><li>Support coordinators</li><li>Direct Payment holders</li><li>Supported living providers</li></ul>')))

# ---------- Support and funding ----------
support = row('shg-day__support',
    col('large-6 medium-12 small-12', 'shg-day__card shg-day__card--support',
        text('shg-day__h3', 'Support that fits', 'h3'),
        text('shg-day__body', 'We offer group and individual one-to-one support, with flexible attendance options to meet your needs. We are fully wheelchair accessible.')),
    col('large-6 medium-12 small-12', 'shg-day__card shg-day__card--funding',
        text('shg-day__h3', 'Tailored support plans and funding', 'h3'),
        text('shg-day__body', 'You may be able to use a Direct Payment or Personal Budget to pay for our service. Ask your social worker or local council about your eligibility.')))

# ---------- Register interest: Duda's form widget ----------
home_before = open(ROOT / 'duda/home/before/home.html').read()
sendto = re.search(r'<input name="dmformsendto"[^>]*/>', home_before).group(0)
params = re.search(r'<input name="dmformsubmitparams"[^>]*/>', home_before).group(0)

def field(kind, label, name, cls, required=True, auto=None, options=None, hint=None):
    i, l, h = nid(), nid(), nid()
    req = 'required ' if required else ''
    ac = f' autocomplete="{auto}"' if auto else ''
    if kind == 'textarea':
        ctrl = f' <textarea name="{name}" id="{i}"></textarea> \n'
    elif kind == 'select':
        opts = ''.join(f'<option value="{o}">{o}</option>' for o in options)
        ctrl = f'<select class="" name="{name}" id="{i}">{opts}</select>'
    else:
        ctrl = f'<input type="{kind}" class="" name="{name}" id="{i}"{ac}/>'
    return (f' <div class="dmforminput {req} {cls} dmRespDesignCol" id="{nid()}"> '
            f'<label for="{i}" id="{l}" data-dm-for="{name}">{label}</label> \n'
            f'{ctrl}<input type="hidden" name="label-{name}" value="{label}" id="{h}" class=""/></div> \n')

fields = [
    field('text', 'Your name', 'dmform-0', 'small-12 medium-6 large-6', auto='name'),
    field('tel', 'Phone', 'dmform-1', 'small-12 medium-6 large-6', auto='tel'),
    field('email', 'Email', 'dmform-2', 'small-12 medium-12 large-12', auto='email'),
    field('select', 'I am', 'dmform-3', 'small-12 medium-6 large-6',
          options=['Interested for myself', 'A family member or carer', 'A social worker', 'A support coordinator',
                   'A supported living provider', 'Someone else']),
    field('select', 'I would like to', 'dmform-4', 'small-12 medium-6 large-6',
          options=['Book a free trial visit', 'Make a referral', 'Ask a question']),
    field('textarea', 'Tell us a little about the person and the support they need', 'dmform-5', 'small-12 medium-12 large-12', required=False),
]
form = (f'<div class="dmform default native-inputs shg-day__form" id="{nid()}" data-layout="layout-1" data-element-type="dContactUsRespId"> '
        f'<h3 class="dmform-title dmwidget-title" id="{nid()}" hide="true"></h3> \n'
        f' <div class="dmform-wrapper" id="{nid()}" captcha-lang="en"> <form method="post" class="dmRespDesignRow" locale="ENGLISH" id="{nid()}">'
        + ''.join(fields) +
        f' <div class="dmformsubmit dmWidget R" id="{nid()}"><input class="" name="submit" type="submit" value="Register interest" id="{nid()}"/></div> \n'
        f'{sendto}<input class="dmActionInput" type="hidden" name="action" value="/_dm/s/rt/widgets/dmform.submit.jsp" id="{nid()}"/>'
        f'<input name="dmformsubject" type="hidden" value="Day opportunities: new interest" id="{nid()}"/>{params}</form> \n'
        f'</div> \n'
        f' <div class="dmform-success" style="display:none" id="{nid()}">Thank you for getting in touch.<br id="{nid()}"/>We will contact you soon to talk about the next steps.</div> \n'
        f' <div class="dmform-error" style="display:none" id="{nid()}">Sorry, your details could not be sent.<br id="{nid()}"/>Please try again, or call us on 0191 549 9444.</div> \n'
        f'</div>')
assert form.count('<div') == form.count('</div>')

register = row('shg-day__register',
    col('large-5 medium-12 small-12', 'shg-day__register-text',
        text('shg-day__eyebrow shg-day__eyebrow--light', 'Register interest'),
        text('shg-day__h2', 'Ready to start your journey?', 'h2'),
        text('shg-day__lead-light', 'Book a free trial visit and see for yourself. No need to decide straight away.'),
        text('shg-day__contact', f'<b>Call</b> <a href="{TEL}">0191 549 9444</a><br/>'
                                 '<b>Email</b> <a href="mailto:deb.homegrown@aol.com">deb.homegrown@aol.com</a><br/>'
                                 '<a href="mailto:gary.homegrown@aol.com">gary.homegrown@aol.com</a><br/>'
                                 '<b>Find us</b> Unit 10, Thompson Park, Southwick, Sunderland SR5 2PL<br/>'
                                 '<b>Facebook</b> <a href="https://www.facebook.com/SunderlandHomeGrownCIC" target="_blank" rel="noopener">SunderlandHomeGrownCIC</a>')),
    col('large-7 medium-12 small-12', 'shg-day__register-form',
        text('shg-day__form-title', 'Tell us who you are and we’ll call you back', 'h3'),
        form,
        text('shg-day__form-note', 'We only use these details to reply to you about day opportunities.')))

page = f'''<!-- *** ADD OR EDIT HTML INSIDE OF THE dmRespCol DIVS, SEE DOCUMENTATION FOR GUIDELINES *** -->
<!--
  Sunderland Home Grown redesign: DAY OPPORTUNITIES page (for service users, families and referrers)
  Paste into a NEW page whose URL is /day-opportunities. Styled by day.css (this page's Head HTML).
  Every block is a normal Duda text or image widget; the form at the end is Duda's own form widget.
  Buttons that go to "#register" scroll down to the form.
-->
<div dm:templateorder="170" class="dmHomeRespTmpl mainBorder dmRespRowsWrapper dmFullRowRespTmpl shg-day" id="1716942098">
{hero}
{intro}
{strip}
{gain_head}
{gain_row}
{act_head}
{act_row}
{quotes_head}
{quotes}
{why}
{support}
{register}
</div>
'''
out = ROOT / 'duda/day-opportunities/after/day-opportunities.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(page)
ids = re.findall(r'\bid="(\d+)"', page)
print(f'{out.name}: {len(ids)} ids, unique={len(ids) == len(set(ids))}, text widgets={page.count("dmNewParagraph")}, images={page.count(chr(34)+"image"+chr(34))}')

# ---------- Home page call to action (one row) ----------
cta = row('shg-home__day-cta',
    col('large-7 medium-12 small-12', 'shg-home__day-cta-text',
        text('shg-home__day-cta-eyebrow', 'Day opportunities for adults'),
        text('shg-home__day-cta-title', 'What if the right place could help someone grow?', 'h2'),
        text('shg-home__day-cta-lead', 'Meaningful work-based day opportunities for adults with disabilities and additional support needs, in the heart of Thompson Park.'),
        text('shg-home__day-cta-points', '<ul><li>Free trial visits</li><li>Group and one-to-one support</li><li>Fully wheelchair accessible</li><li>Referrals welcome</li></ul>'),
        text('shg-home__day-cta-button', f'<a href="{PAGE}#register">Book a free trial visit</a>'),
        text('shg-home__day-cta-button shg-home__day-cta-button--quiet', f'<a href="{PAGE}">Find out more</a>')),
    col('large-5 medium-12 small-12', 'shg-home__day-cta-media',
        image('shg-home__day-cta-img', C + 'Michelle+and+lesley.jpg',
              'Two women smiling under a striped parasol, one holding up a pot of white flowers she has planted.')))
cta_ids = re.findall(r'\bid="(\d+)"', cta)
assert not set(cta_ids) & set(ids)
(ROOT / 'duda/home/after/day-cta-row.html').write_text(
    '<!--\n  SUNDERLAND HOME GROWN REDESIGN: HOME PAGE, DAY OPPORTUNITIES CALL TO ACTION (one row)\n'
    '  Paste just below the hero row of the Home page (see duda/day-opportunities/README.md).\n'
    '  Styled by home.css. Links go to the Day opportunities page (/day-opportunities).\n-->\n' + cta + '\n')
print(f'day-cta-row.html: {len(cta_ids)} ids')
