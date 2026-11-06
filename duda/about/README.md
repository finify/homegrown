# About us page (Our Team)

`before/about.html` is the page as it was (your backup). `after/about.html` is the new page.

## Install
1. **Page HTML:** open the About / Our Team page in Developer Mode, select the page's main content HTML, delete it, and paste `after/about.html`.
2. **Page Head HTML:** in that page's settings (Page settings > Head HTML), paste:
   ```html
   <link rel="stylesheet" href="https://finify.github.io/homegrown/duda/about.css">
   ```
   That one file covers desktop, tablet and mobile. It uses the colours from `base.css`, which is already linked site-wide.
3. **Preview** on desktop, tablet and mobile, then **Publish**.

## Editing in the editor
- Every heading, paragraph and button is a normal text widget. Click it and type; the design stays.
- Every photo is a normal image widget. Click it and choose **Replace**.
- **Gary's photo:** the logo is a placeholder. Replace it with a portrait.
- **Add a team member:** in the team row, duplicate Gary's column, then change the photo, name and role.
- **Gallery:** duplicate or delete a column to add or remove photos.
  - Clicking or tapping a gallery photo opens it full size in a **lightbox**. It shows the caption and "2 of 6", with arrows to step through, swipe on phones, arrow keys and Esc.
  - New photos join the lightbox automatically, and the caption is the text under each photo.
  - It comes from `site.js` and `base.css`, which are already linked, so there's nothing to paste.

## Sections
Hero, our story, what we do (three tiles), quote, the team, our site (Youth Investment Fund), gallery, and a closing call to action.

## Still to confirm with staff
- Portraits, names and roles for the rest of the team.
- Whether the YIF grant items are finished or still in progress.

## How it was tested
The page was checked in a mock-up of the live page at 1440px, 820px and iPhone width:
- every link and button is at least 44px tall;
- nothing overflows the screen;
- the layout and text styles are unchanged after simulating the editor rewriting the text (extra spans, fonts and inline styles).
