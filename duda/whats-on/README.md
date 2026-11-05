# What's On: Duda collection

`whats-on-collection.csv` is ready to import into a Duda **collection**, so the What's On page can be built from it and updated in the CMS without editing the page.

- **Rows (15):** the Junior Joiners course and the 11 Christmas wreath dates from the live shop (checked 5 Nov 2026), plus the three regular groups.
- **Data rules:** prices, dates, times, sold-out status, booking links and photos are all taken from the shop. Anything the shop doesn't say (end times for wreath sessions, what to bring, accessibility notes) is left **blank**, ready to fill in, rather than guessed.
- **Your template:** `template-original.csv` is the template you sent. Its test row's `uuid` is reused for the first row, so the import **updates** that row instead of leaving a stray "1" behind. Its empty `New field` column isn't included.
- **Regenerating:** `scripts/duda-whats-on-csv.py` rebuilds the CSV.

## Test first: things not yet confirmed in the Duda CMS
The CSV keeps the columns from your Duda export (`uuid`, `item`). These import details couldn't be checked without access to the editor:
- **Field creation:** whether the import creates fields or needs them to exist first. If it needs them, create each field below (exact name, matching type) before importing.
- **Formats:**
  - date fields: `2026-11-25` was used;
  - Yes/No fields: `true`/`false` was used;
  - Link fields: a plain URL was used.
- **Images:** whether image URLs are copied into Duda's media library or linked.

**Import `whats-on-collection-TEST.csv` (3 rows) first.**
- **If it all imports cleanly,** import the full file.
- **If something won't import,** export that collection from Duda with one sample row filled in by hand. That shows the exact formats Duda uses, and the CSV can be regenerated to match. A field that refuses a format can also be switched to Text.

## Fields (set these types when Duda asks during import)

| Field | Duda type | What it's for |
|---|---|---|
| `item` | Text (the collection's title field) | Name shown on the card, e.g. "Christmas wreath workshop, Wed 25 Nov 2026" |
| `slug` | Text | Short unique name, used for a dynamic page address if you add one |
| `category` | Text | Workshop, Course, Group or Event. Use it to filter |
| `audience` | Text | Adults, Young people, Children, Families, Everyone. Use it to filter |
| `age_range` | Text | e.g. "11 to 13" (blank = all ages) |
| `schedule_type` | Text | **Single date**, **Date range**, **Weekly course**, **Weekly**, **Daily**, **Monthly**, **Ongoing** |
| `start_date` / `end_date` | Date | First and last day (the same day for single dates; blank for ongoing groups). Sort by `start_date`, and hide rows once `end_date` has passed |
| `start_time` / `end_time` | Text (24-hour, e.g. 13:00) | Blank when unknown |
| `recurrence` | Text | e.g. "Every Monday", "Twice a month", "Every Monday for 4 weeks" |
| `date_label` / `time_label` | Text | Ready-to-show wording, e.g. "Mondays, 9 Nov to 30 Nov 2026" and "1pm to 2:30pm". Easier than formatting dates in the widget |
| `price` | Number | Pounds, without the £ (blank = ask us) |
| `price_label` | Text | What to show: "£20", "Free", "Ask us" |
| `price_note` | Text | e.g. "Weekday sessions £20, weekend sessions £25" |
| `is_free` | Yes/No (Boolean) | Lets you filter or show a "Free" badge |
| `booking_required` | Yes/No (Boolean) | Whether people must book |
| `booking_url` | Link | The shop product to book, or `/contact` for groups |
| `booking_button_text` | Text | "Book a place", "Book the course", "Ask about joining" |
| `status` | Text | **Available**, **Sold out**, **Ongoing**, **Cancelled**, **Past**. Hide the book button or show a badge with it |
| `location` | Text | Address shown on the card |
| `short_description` | Text | One line for the card |
| `description` | Rich text | Longer text for a detail page or expanded card |
| `what_to_bring` | Text | e.g. "Stout footwear and gloves" |
| `accessibility_notes` | Text | Blank for now; worth filling in for families |
| `image` | Image | Photo URL (not yet confirmed whether Duda copies it into the media library or links to it) |
| `image_alt` | Text | Description of the photo for screen readers |
| `featured` | Yes/No (Boolean) | Pin to the top or show on the home page |
| `show_on_site` | Yes/No (Boolean) | Untick to hide a row without deleting it |
| `sort_order` | Number | Manual order (dated events first, soonest first, then groups) |

## Setting it up in Duda
1. **Open the collection:** in the editor, go to **Content > Collections** and open your Workshop collection (or create one).
2. **Import:** choose **Import CSV** and select `whats-on-collection.csv`. Match each column to a field, creating new fields with the types above.
3. **Add the list:** on the What's On page, add a **dynamic list** (or **collection gallery**) widget connected to the collection, then:
   - **Show** `image`, `item`, `date_label`, `time_label`, `price_label`, `short_description`, and a button linked to `booking_url` with the text from `booking_button_text`.
   - **Filter** `show_on_site` = Yes. Optionally filter `category` or `audience` for separate "Workshops" and "Groups" lists.
   - **Sort** by `sort_order` (or `start_date`).
4. **From then on, update the collection, not the page:**
   - **New workshop:** add a row.
   - **Sold out:** set `status` to Sold out.
   - **After an event:** set `show_on_site` to No (or `status` to Past).

## Still to confirm with staff
- Wreath sessions: how long each one lasts (`end_time`), what's included, and what to bring.
- Groups: costs, times for the heritage and beekeeping groups, and a photo for the heritage group.
- Accessibility notes for each activity.
- Wreath dates 08 and 13 weren't listed in the shop, so they're not in the CSV.
