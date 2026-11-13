# Gallery page

## Install (one paste)
1. Open the **Gallery** page in Developer Mode (the page HTML).
2. Find the gallery row. It starts `<div class="u_1228955510 dmRespRow ...`.
3. Paste `after/gallery-header-row.html` **just above** that line.
4. Save, preview, then **Publish**:
   `https://websitebuilder.123-reg.co.uk/site/0432dc74/gallery?preview=true&insitepreview=true&dm_device=desktop` (change `desktop` to `tablet` or `mobile`).

There's no stylesheet to link: the styles are in `base.css` and the lightbox is in `site.js`, both already linked site-wide.

## What changes
- **Header:** "Life at the nursery", a large "Gallery" title and a short line about the page, matching the Blog page.
- **Photos:** Duda's own gallery widget, untouched, so add, remove, reorder and caption photos in the editor as usual.
  - Even 16px gaps, rounded corners and a soft shadow.
  - On hover the photo lifts and zooms slightly (replacing Duda's zoom-out effect).
  - Captions (a photo's title and text in the editor) sit on a soft dark shade at the bottom of the photo.
- **Lightbox:** selecting a photo opens it full size, with its caption, "5 of 12", arrows, swipe, arrow keys and Esc. It also covers the photos "View more" reveals.
- **View more / View less:** a gold button, full width on phones.
- **Accessibility:**
  - Every photo can be reached and opened with the keyboard, with a clear focus ring.
  - "View more" works as a button.
  - No fade-in or zoom for people who've asked their device to reduce motion.

## Worth doing in the editor
- **Alt text:** the photos have no descriptions, so screen readers just say "photo". In the gallery settings, give each photo a short description (for example "Two volunteers holding a bird box they've built").
- **Phones show 2 photos** before "View more". That's the gallery's mobile "rows to show" setting, which you can raise if you'd like more.
