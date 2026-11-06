# Home page (video hero)

`before/home.html` is the home page as it was (your backup). `after/home.html` is the new page.

## Install
1. **Page HTML:** open the Home page in Developer Mode. Select the page's main content HTML (the block that starts `<div dm:templateorder="170" … id="1716942098">`), delete it, and paste `after/home.html`.
2. **Page Head HTML:** in the Home page's settings (Page settings > Head HTML), paste:
   ```html
   <link rel="stylesheet" href="https://finify.github.io/homegrown/duda/home.css">
   ```
   That one file covers desktop, tablet and mobile.
3. **Site-wide links:** the video comes from `site.js`, and its player styles from `base.css`. Both are already in your site-wide links (`LINK-SETUP.html`), so there's nothing extra to add.
4. **Preview** with the editor's desktop, tablet and phone icons, then **Publish**.

## The video hero
- **Video:** the YouTube film plays muted and looping behind the tagline "Growing plants, nurturing people since 2017."
- **Changing it:** the video is whichever YouTube link is in the "Watch our film with The Big Issue" text. Change that link in the editor (any YouTube address works) and the background changes with it.
- **The photo underneath** shows while the video loads, and stays if it can't play. Replace it like any other image (click it, then **Replace**). It shows on:
  - phones in Low Power Mode;
  - visitors who've asked their device to reduce motion, or who are on data saver (they can press **Play**);
  - the editor itself, which doesn't run the video.
- **Pause / Play button** in the corner. Moving video that plays for more than five seconds needs a way to stop it (WCAG 2.2.2).
- The video **pauses while scrolled out of view**, to save battery and data, and carries on when you scroll back.
- **"Watch our film"** opens the full film with sound on YouTube, and credits The Big Issue.
- **Please check with The Big Issue** that they're happy for their film to be used this way (it's their YouTube upload). If you have the original file, a short silent clip uploaded to the site would load faster and show no YouTube branding.

## Sections
1. **Video hero:** tagline, "Get in touch" and "Visit the shop".
2. **We grow plants and people:** who you are.
3. **Who are you here for?:** individuals and families, professionals and referrers, gardeners and visitors.
4. **What a day here looks like:** nursery, growing food, garden centre, bees. On phones the cards swipe sideways.
5. **Our plants grow at:** Durham Cathedral, Palace Green, Lumley Castle, Sherburn Village.
6. **Groups anyone can join**.
7. **Quote** from Gary.
8. **Youth Investment Fund**.
9. **Get in touch:** your **existing Duda form**, unchanged (same widget, so its email settings carry over), restyled to match the Contact page.

All wording comes from the current site. Links go to pages that exist now: `/contact`, `/store`, `/fruit-vegetables-group` and `/youth-investment-fund`. Point them at new pages (such as Day opportunities) once those are live.

## Editing in the editor
- Every heading, paragraph and button is a normal text widget, and every photo a normal image widget. Edit them in the editor and the design stays.
- Each row's column sizes add up to 12, so the editor accepts the HTML.

## How it was tested
The page was checked in mock-ups of the live home page at 1440, 1280 and 820px wide, and at iPhone 13 and 320px phone widths:
- nothing overflows the screen;
- every link, button and field is at least 44px;
- layouts change as intended at each size;
- the design is unchanged after simulating the editor rewriting the text.

**The video in testing:** YouTube won't stream into the test machine, so the video controls were checked with a stand-in player:
- the video fades in only once it's playing;
- Pause and Play work;
- it pauses off screen and resumes on return;
- there's no autoplay when reduce motion is on.

**Check after publishing:** the real video playing on a phone and a computer.
