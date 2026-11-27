# What's On page, with workshops from the CMS

The page: `after/whats-on.html`. The workshop list comes from a **collection** (123-reg's CMS, which is Duda's) shown with a **Dynamic Repeater**, so you add, edit or hide workshops without touching the page. Styles are in `base.css`, already linked site-wide.

## 1. Create the collection: Workshops
In the editor: **Content** (left panel) → **Collections** → **New collection** → name it **Workshops**.

**Create the fields first.** The import won't create fields: a CSV column with no matching field fails with "CSV contains fields that are not present in the collection".
1. In the collection, add each field below with **exactly** this name (lower case, underscores) and type. Rename the empty `New field` to one of them, for example `image`.
2. Import `workshops-collection-TEST.csv` (2 rows) first. Its first row reuses the uuid of your test row "1", so that row is updated rather than left behind.
3. If that works, import `workshops-collection.csv` (all 12; the two dates already past have `show_on_site` = false). Use the same uuid trick: the full file's first row is the same Junior Joiners row.
4. If one field rejects its values (most likely `image`, `link` or `show_on_site`), change that field to **Text** and import again. Or fill one row in by hand, export it, and send me the export: I'll match the CSV to its exact format.

The fields:

| Field | Type | What goes in it |
|---|---|---|
| `item` | Text (the title field) | Workshop name, e.g. "Christmas wreath workshop, Sat 5 Dec 2026" |
| `image` | Image | The photo |
| `image_alt` | Text | A short description of the photo, for screen readers |
| `date_label` | Text | When, as you want it shown, e.g. "Sat 5 Dec 2026, 1pm" |
| `price_label` | Text | e.g. "£25", "Free", "Ask us" |
| `description` | Text | One or two sentences |
| `link_type` | Text (or a dropdown/selection field, if the editor offers one, with the options **Internal** and **External**) | **Internal** = a page on this site, such as a shop product. **External** = another website (e.g. a partner's booking page) |
| `link` | Link | **Internal:** copy the address of the product from your shop, e.g. `https://www.sunderlandhomegrown.co.uk/store/...`. **External:** paste the full address of the other website (`https://…`) |
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
- **Link to the shop:** set `link_type` to **Internal**, open the product in your shop and copy its address into `link`.
- **Link to another website:** set `link_type` to **External** and paste the full address (https://…) into `link`. On the page, external links open in a new tab and their button gets a small ↗ (worked out from the address, so it works even if `link_type` is left blank; the field is there to make the list clear to whoever edits it).
- **Sold out:** change `link_text` to "Sold out: see the shop" (the shop shows it as sold out), or untick `show_on_site`.
- **When it's over:** untick `show_on_site` (or delete the row).

## Please check
- The **Junior Joiners** course ran 9 to 30 November, so it's probably no longer bookable. Untick it if so.
- The dates and sold-out status were copied from the shop on 5 November. Check them against the shop before publishing.
- The Dynamic Repeater couldn't be added from here, so the list was tested with a stand-in built from Duda's own widgets in the same order. Check the real one on the preview; if anything looks off, send me a screenshot.

## Files
- `after/whats-on.html`: the page. `after/wo.css`: its styles (built into `base.css`).
- `workshops-collection.csv`: the lean Workshops collection (made by `scripts/duda-workshops-csv.py`). All 12 current rows are **Internal** (they link to the shop).
- `whats-on-collection.csv`, `whats-on-collection-TEST.csv`, `template-original.csv`: the earlier, fuller version (includes the regular groups), kept for reference.
