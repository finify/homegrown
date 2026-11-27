# What's On page, with workshops from the CMS

The page: `after/whats-on.html`. The workshop list comes from a **collection** (123-reg's CMS, which is Duda's) shown with a **Dynamic Repeater**, so you add, edit or hide workshops without touching the page. Styles are in `base.css`, already linked site-wide.

## 1. Create the collection: Workshops
In the editor: **Content** (left panel) → **Collections** → **New collection** → name it **Workshops**.

Easiest: **Import** `workshops-collection.csv` (12 workshops and courses from the shop; the two dates already past are hidden). Or create these fields and add rows by hand:

| Field | Type | What goes in it |
|---|---|---|
| `item` | Text (the title field) | Workshop name, e.g. "Christmas wreath workshop, Sat 5 Dec 2026" |
| `image` | Image | The photo |
| `image_alt` | Text | A short description of the photo, for screen readers |
| `date_label` | Text | When, as you want it shown, e.g. "Sat 5 Dec 2026, 1pm" |
| `price_label` | Text | e.g. "£25", "Free", "Ask us" |
| `description` | Text | One or two sentences |
| `link` | Link | **Shop product page** (copy the address from the product in your shop, e.g. `https://www.sunderlandhomegrown.co.uk/store/...`) **or any external website** |
| `link_text` | Text | The button words: "Book a place", "Find out more", "Sold out: see the shop" |
| `status` | Text | Available, Sold out or Past (for your own reference, or to filter) |
| `show_on_site` | Yes/No | Untick to hide a workshop without deleting it |
| `sort_order` | Number | Order on the page (1 first) |

## 2. Paste the page
Open **What's On** in Developer Mode, replace all its HTML with `after/whats-on.html`, save.

The page has: a header with "Visit the shop", an **Upcoming workshops** heading, the list, **Regular groups** (fruit and vegetables, beekeeping, local history; fixed text), and a "Questions about a workshop?" panel.

Under "Upcoming workshops" there's a dashed box saying "Our next workshops will be listed here soon…". It hides itself once the repeater is there, so if the list is ever empty visitors see a phone number instead of a gap.

## 3. Add the Dynamic Repeater (the list)
1. In **Widgets**, find **Dynamic Repeater** (search "repeater") and drag it into the dashed box under "Upcoming workshops".
2. Connect it to the **Workshops** collection.
3. Design **one** card in the repeater, with these widgets **in this order** (the styling relies on the order):
   1. **Image** → connect to `image` (and its alt text to `image_alt`, if offered)
   2. **Text** → connect to `item` (the title)
   3. **Text** → connect to `date_label`. Insert `price_label` in the same text too, if you like, e.g. "Sat 5 Dec 2026, 1pm · £25"
   4. **Text** → connect to `description`
   5. **Button** → link connected to `link`, button text connected to `link_text`

   To connect a widget, select it and use its **Connect to data** option, then pick the field. You don't need to style anything: fonts, colours, the rounded white card, the date label, the photo shape and the gold full-width button all come from `base.css`.
4. In the repeater's settings:
   - **Layout → Items per row:** 3 (2 on tablet and 1 on phones, if it lets you set them per device).
   - **Navigation:** Load More (or Pagination), showing 9 at a time.
   - **Filter & Sort:** filter where `show_on_site` is on (true), and sort by `sort_order`, lowest first.
5. Preview on desktop, tablet and phone, then **Publish**. If a collection change doesn't show on the live site, publish again.

## Adding, changing or hiding a workshop
- **Add:** Content → Collections → Workshops → add a row. Fill in the photo, title, date, description and link, and tick `show_on_site`.
- **Link to the shop:** open the product in your shop and copy its address. **Link elsewhere:** paste any full web address (https://…).
- **Sold out:** change `link_text` to "Sold out: see the shop" (the shop shows it as sold out), or untick `show_on_site`.
- **When it's over:** untick `show_on_site` (or delete the row).

## Please check
- The **Junior Joiners** course ran 9 to 30 November, so it's probably no longer bookable. Untick it if so.
- The dates and sold-out status were copied from the shop on 5 November. Check them against the shop before publishing.
- The Dynamic Repeater couldn't be added from here, so the list was tested with a stand-in built from Duda's own widgets in the same order. Check the real one on the preview; if anything looks off, send me a screenshot.

## Files
- `after/whats-on.html`: the page. `after/wo.css`: its styles (built into `base.css`).
- `workshops-collection.csv`: the lean Workshops collection (made by `scripts/duda-workshops-csv.py`).
- `whats-on-collection.csv`, `whats-on-collection-TEST.csv`, `template-original.csv`: the earlier, fuller version (includes the regular groups), kept for reference.
