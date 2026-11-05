# Footer: before and after

- `before/`: the original footer HTML and the three CSS panels, as copied from the editor (your backup).
- `after/`: the new footer.

Unlike the header, **this footer file is used on every device**, phones included. So one HTML file plus three CSS additions covers everything.

| File | Where it goes | What to do |
|---|---|---|
| `after/footer.html` | Developer Mode > HTML > the **footer** file | **Replace** everything |
| `after/css-all-devices.css` | CSS > "…AFFECTS ALL DEVICES" | Paste at the **end**, after the menu files |
| `after/css-desktop-and-tablet.css` | CSS > "…AFFECTS DESKTOP AND TABLET DEVICES" | Paste at the **end** |
| `after/css-mobile.css` | CSS > "…AFFECTS MOBILE DEVICES" | Paste at the **end** |

You don't need to delete the old footer CSS. It targets the old footer's elements, which are gone.

## Why the old version lost its styling when edited
Duda's text editor rewrites the HTML inside a text widget as soon as you click into it:
- it removes inner class names;
- it turns headings and lists into its own markup;
- it wraps text in `<span>` and `<font>` tags with inline styles.

The first version styled those inner elements, so editing wiped the design. This version is **editor-safe**:
- each editable block is a single Duda widget, with its class on the widget itself (Duda keeps that);
- the content inside is plain text, bold, links and line breaks;
- the CSS styles whatever ends up inside each widget.

Tested by simulating the editor's rewrite (inner classes stripped, text wrapped in Arial/14px/black spans): the design didn't change.

## How to edit in the editor
- **Text:** click the block and type. Font, size and colour come from the design, so ignore the toolbar's font and colour options.
- **Links:** select the words and use the toolbar's link button. In a link list, put each link on its own line.
- **Pictures:** click the image and choose **Replace**.
- **Don't** open the widget's own HTML view and paste markup into it. If something does go wrong, paste `after/footer.html` into the footer file again.

## Everything is editable in the editor
- **Text:** all 20 text blocks are normal Duda text widgets. Click to change words, links, opening times or contact details.
- **Pictures:** the leaves graphic and both funder logos are normal Duda image widgets. Click to replace them from the media library.
  - The leaves graphic starts from `https://finify.github.io/homegrown/duda/footer-leaves.svg`. Swap it for a copy in the site's own media library so the site doesn't depend on the GitHub repo. The file is `public/duda/footer-leaves.svg` in this repo.
  - The two logos (National Lottery Community Fund, Youth Investment Fund) already come from the site's own media library.
- **Supporters without a logo** (Sunderland City Council, Coalfields Regeneration Trust, Barclays, Power to Change) are text tiles. To use a logo instead, delete the text in that tile and drop an image widget in its place. Add the class `shg-footer__tile--logo` to the column in Developer Mode for the white background.

## Links to check
The footer links point to the new pages' addresses: `/garden-centre`, `/whats-on`, `/day-opportunities`, `/community`, `/about`. Existing pages are linked where they're still used: `/store`, `/contact`, `/blog`, `/gallery`, `/thanks-to` and `/privacy-policy`. If a page ends up with a different address, edit the link in the editor.

## Layout by screen size
| Screen | Layout |
|---|---|
| Desktop | Name built large with the leaves on the right; five columns (Visit, Take part, About, Opening times, Find us); six supporter tiles in a row; copyright and links along the bottom |
| Tablet (under 1024px) | Three link columns, then Opening times and Find us side by side; supporter tiles three across |
| Phone | Everything stacked; link lists two across; supporter tiles two across |

Tested by swapping it into copies of the live desktop and mobile pages, with the existing CSS still in place, at 1440px, 900px and iPhone width:
- no overflow;
- every link at least 32px tall, most 44px;
- the site font loads.

See `after/preview-*.png`.
