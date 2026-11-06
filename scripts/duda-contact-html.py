"""Generates duda/contact/after/contact.html (editor-safe Contact & find us page).

Every editable block is ONE Duda widget whose outer element carries the styling class (Duda keeps
it); the content inside is plain text, bold, links and line breaks, because Duda's text editor
rewrites anything inside a widget when it's edited. Duda's own form and map widgets are kept
(same ids) and styled from outside. New ids are checked against the live page to avoid clashes.
Run: python3 scripts/duda-contact-html.py
"""
import pathlib, random, re, urllib.request

try:
    live = urllib.request.urlopen('https://www.sunderlandhomegrown.co.uk/contact', timeout=20).read().decode('utf8', 'ignore')
except Exception:
    live = ''
taken = set(re.findall(r'\bid="(\d+)"', live))
random.seed(1683814473)

def nid():
    while True:
        n = str(random.randint(1500000000, 1999999999))
        if n not in taken:
            taken.add(n)
            return n

def text(cls, inner, tag='div', align='left'):
    return (f'<{tag} class="dmNewParagraph {cls}" data-element-type="paragraph" dmle_widget="paragraph" '
            f'data-uialign="{align}" data-version="5" id="{nid()}" style="transition:opacity 1s ease-in-out;">\n{inner}\n</{tag}>')

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

CDN = 'https://irp.cdn-website.com/0432dc74/dms3rep/multi/'

# Duda's own form widget: same ids as before, so its settings (recipients, captcha) carry over.
FORM = '''<div class="u_1409582723 dmform default shg-contact__form" preserve_css="true" dmle_widget="dudaContactUsRespId" id="1409582723" data-element-type="dContactUsRespId" data-require-captcha="true" data-captcha-position="bottomleft" captcha="true">
 <h3 class="dmform-title dmwidget-title" id="1523795847" hide="true"></h3>
 <div class="dmform-wrapper" preserve_css="true" id="1286867403">
  <form method="post" class="dmRespDesignRow" locale="ENGLISH" id="1534120495">
   <div class="dmforminput required  small-12 dmRespDesignCol medium-6 large-6" id="1940220924">
    <label for="dmform-0" id="1743058908">Your name</label>
    <input type="text" class="" name="dmform-0" id="1947248170" autocomplete="name"/>
    <input type="hidden" name="label-dmform-0" value="Name" id="1583117237" class=""/>
   </div>
   <div class="dmforminput required  small-12 dmRespDesignCol medium-6 large-6" id="1752187664">
    <label for="dmform-2" id="1240522905">Phone</label>
    <input type="tel" class="" name="dmform-2" id="1249999350" autocomplete="tel"/>
    <input type="hidden" name="label-dmform-2" value="Phone" id="1675183536" class=""/>
   </div>
   <div class="dmforminput required  small-12 dmRespDesignCol medium-12 large-12" id="1594714742">
    <label for="dmform-1" id="1639935624">Email</label>
    <input type="email" class="" name="dmform-1" id="1920320209" autocomplete="email"/>
    <input type="hidden" name="label-dmform-1" value="Email" id="1821811301" class=""/>
   </div>
   <div class="dmforminput large-12 medium-12 dmRespDesignCol" id="1336493176">
    <label for="dmform-3" id="1057153175">Your message</label>
    <textarea name="dmform-3" id="1410846120"></textarea>
    <input type="hidden" name="label-dmform-3" value="Message" id="1153947142" class=""/>
   </div>
   <span id="1336493176_clear" class="dmWidgetClear" dmle_clear="true"></span>
   <span id="1336493176_clear_clear" class="dmWidgetClear" dmle_clear="true"></span>
   <div class="dmformsubmit dmWidget R" preserve_css="true" id="1134676897">
    <input class="" name="submit" type="submit" value="Send message" id="1355265213"/>
   </div>
   <input name="dmformsendto" type="hidden" preserve_css="true" id="1396290210" class=""/>
   <input class="dmActionInput" type="hidden" name="action" value="/_dm/s/rt/widgets/dmform.submit.jsp" id="1785739195"/>
   <input name="dmformfrom" type="hidden" preserve_css="true" id="1095323630" class=""/>
   <input name="dmformsubject" type="hidden" value="Website enquiry" preserve_css="true" id="1369553659" class="" data-email-subject="Website enquiry"/>
  </form>
 </div>
 <div class="dmform-success" style="display:none" preserve_css="true" id="1927585599">Thank you, your message has been sent.<br id="1838163965"/>We'll get back to you as soon as we can.</div>
 <div class="dmform-error" style="display:none" preserve_css="true" id="1009543277">Sorry, your message didn't send.<br id="1856207570"/>Please try again, or call us on 0191 549 9444.</div>
</div>'''

# Duda's own map widget: same id; the pin is set from these coordinates (Thompson Park).
MAP = '''<!-- *** This is a dynamic element, it transforms into a map when the page renders *** -->
<span dmle_extension="mapextension" wr="true" modedesktop="map" modemobile="map" modetablet="map" data-display-type="block" icon="true" surround="true" description="Find Us" class="u_1791714273 default dmDefaultGradient align-center shg-contact__map" adwords="" icon-name="icon-map-marker" street="Thompson Park, Southwick" city="Sunderland" country="GB" country_full="United Kingdom" state="" zip="SR5 1SF" provider="mapbox" lon="-1.38692" lat="54.92273" geocompleteaddress="Thompson Park, Southwick, Sunderland SR5 1SF, United Kingdom" addresstodisplay="Sunderland Home Grown, Thompson Park, Southwick, Sunderland SR5 1SF" id="1791714273" layout="layout4" color-scheme="#173A22" data-popup-display-desktop="" data-popup-display-mobile="" data-popup-title="" data-popup-title-visible="false" data-popup-description="" data-popup-description-visible="false" data-popup-show="false">
</span>'''

photos = [
    ('20220408_151811.jpg', 'The garden centre yard, with plants on benches and the shop building behind.', 'The garden centre yard.'),
    ('IMG_20210523_091218.jpg', 'The open door of the Home Grown shop, with shelves of pots inside.', 'The shop.'),
    ('20220406_150924.jpg', 'Inside a polytunnel: long benches of young plants.', 'The polytunnels.'),
    ('20220617_112022.jpg', 'Raised vegetable beds full of onions, beside a path.', 'The veg beds.'),
]

html = f'''<!-- *** ADD OR EDIT HTML INSIDE OF THE dmRespCol DIVS, SEE DOCUMENTATION FOR GUIDELINES *** -->
<!--
  Sunderland Home Grown redesign: CONTACT & FIND US page (editor-safe)
  Replaces the whole page HTML. Styled by contact.css (linked in this page's Head HTML).
  Every block is a normal Duda text, image, form or map widget: edit them in the editor.
-->
<div dm:templateorder="100" class="dmAboutusRespTmpl mainBorder shg-contact" id="1683814473">
 <div class="innerPageTmplBox dmRespRowsWrapper" id="1396310947">
{row('shg-contact__hero',
     col('large-5 medium-12 small-12', 'shg-contact__intro',
         text('shg-contact__title', 'Contact and find us', tag='h1'),
         text('shg-contact__lead', "Call, email or send us a message. We'd love to hear from you."),
         text('shg-contact__call', '<a href="tel:+441915499444">Call 0191 549 9444</a>'),
         text('shg-contact__label', 'Email'),
         text('shg-contact__links', '<a href="mailto:deb.homegrown@aol.com">deb.homegrown@aol.com</a><br/>\n<a href="mailto:gary.homegrown@aol.com">gary.homegrown@aol.com</a><br/>\n<a href="https://www.facebook.com/sunderlandhomegrown" target="_blank" rel="noopener">Message us on Facebook</a>'),
         text('shg-contact__hours', '<b>Opening times</b><br/>\n<b>Monday to Friday:</b> 10am to 4pm<br/>\n<b>Saturday and Sunday:</b> 9:30am to 3:30pm')),
     col('large-7 medium-12 small-12', 'shg-contact__form-col',
         text('shg-contact__form-title', 'Send us a message', tag='h2'),
         FORM))}
{row('shg-contact__arrive',
     col('large-12 medium-12 small-12', 'shg-contact__head',
         text('shg-contact__section-title', "What you'll see when you arrive", tag='h2'),
         text('shg-contact__section-lead', 'Coming for the first time? These photos show the way in.')))}
{row('shg-contact__photos',
     *[col('large-3 medium-6 small-6', 'shg-contact__photo',
           image('shg-leaf-soft' if i % 2 == 0 else 'shg-leaf-r', CDN + f, alt),
           text('shg-contact__caption', cap)) for i, (f, alt, cap) in enumerate(photos)])}
{row('shg-contact__find',
     col('large-5 medium-12 small-12', 'shg-contact__getting-here',
         text('shg-contact__section-title', 'Getting here', tag='h2'),
         text('shg-contact__address', '<b>Sunderland Home Grown CIC</b><br/>\nThompson Park, Southwick<br/>\nSunderland SR5 1SF'),
         text('shg-contact__note', 'If you need directions, or help with access when you visit, give us a call and we will help.'),
         text('shg-contact__directions', '<a href="https://www.google.com/maps/dir/?api=1&amp;destination=Thompson+Park+Southwick+Sunderland+SR5+1SF" target="_blank" rel="noopener">Directions in Google Maps</a>')),
     col('large-7 medium-12 small-12', 'shg-contact__map-col', MAP))}
 </div>
</div>
'''
out = pathlib.Path(__file__).resolve().parent.parent / 'duda/contact/after/contact.html'
out.write_text(html)
ids = re.findall(r'\bid="(\d+)"', html)
print(f'{out.name}: {len(ids)} ids, unique={len(ids) == len(set(ids))}, text widgets={html.count("dmNewParagraph")}, images={html.count("data-element-type=\"image\"")}')
