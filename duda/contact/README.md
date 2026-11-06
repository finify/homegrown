# Contact & find us page: before and after

- `before/contact.html`: the page HTML as it was (your backup).
- `after/contact.html`: the new page HTML. Paste it once to replace the whole page's HTML in Developer Mode.
- `after/contact.css`: **one** stylesheet for desktop, tablet and phone (tablet and phone are media queries inside it). It's published at `https://finify.github.io/homegrown/duda/contact.css`.

## Install
1. **Page HTML:** in Developer Mode, open the Contact page's HTML, replace it all with `after/contact.html`, and save.
2. **Page Head HTML:** open the Contact page's own settings (not the site-wide settings). Find **Head HTML** (sometimes under Advanced or SEO), and add:
   ```html
   <link rel="stylesheet" href="https://finify.github.io/homegrown/duda/contact.css">
   ```
   It uses the colours from `base.css`, which the site-wide Head HTML already loads (see `../LINK-SETUP.html`).
   If the page settings have no Head HTML box, add the same line to the site-wide Head HTML instead. It only affects the Contact page, because every rule is scoped to it.
3. **Preview** on desktop, tablet and phone, then **Publish**.

## Editor-safe, like the header and footer
- **Text:** every piece of text is one Duda text widget with its class on the widget itself (17 of them). Click and type: fonts, sizes and colours come from the stylesheet, so editing can't wipe them.
- **Photos:** the four arrival photos are normal image widgets. Click one and choose **Replace**. The leaf shapes come from `base.css`.
- **Form and map:** Duda's own widgets, kept with the same IDs, so their settings (who receives messages, captcha) carry over. They're styled from outside.

Tested by simulating Duda's editor rewrite on every text widget: inner classes stripped, and text wrapped in a bright-green Arial/14px inline style like the old heading had. Measured at 1440px, 820px and phone width, the design didn't change.

## Layout
| Screen | Layout |
|---|---|
| Desktop | Title, contact details and opening times on the left; the form in a white card on the right; four arrival photos; the "Getting here" panel with the map |
| Tablet (≤1024px) | Everything in one column; photos two across; map 380px tall |
| Phone (≤767px) | One column; full-width form fields and send button; photos two across; map 300px tall |

## Please also do in the editor
- **Fix the map pin.** The old map was set to **SR5 1JN**, but the address is **SR5 1SF**. The new HTML sets the address text and keeps the Thompson Park coordinates. Open the map widget's settings, re-enter "Thompson Park, Southwick, Sunderland SR5 1SF", and check the pin is in the right place.
- **Add two fields in the form widget's own settings** (Duda builds the fields itself; the stylesheet already styles drop-downs and tick boxes):
  - **"What is your enquiry about?"**: a drop-down with Garden centre, Trade and wholesale, Day opportunities, Workshops, Hire us, Volunteering, Something else. This helps route messages.
  - **A consent tick box (required):** "I agree to Sunderland Home Grown storing these details to respond to my enquiry", with a link to the privacy policy.
- **Check who receives the form's messages.** The form's email subject is now "Website enquiry".
