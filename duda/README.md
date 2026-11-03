# Redesign for 123-reg Website Builder (Duda Developer Mode)

Paste-in files that bring the prototype's header, colours, type, buttons, leaf photos and footer colours to the live 123-reg site.
**Folders:** `menu/before/` holds the original header and CSS exactly as copied from the editor (your backup). `menu/after/` holds the new files to paste in.

The menu stays Duda's **dynamic menu**: pages are still added, renamed, ordered and hidden in the **Pages** panel.

| File | Where it goes in the editor | What to do |
|---|---|---|
| `menu/after/1-head-html.html` | Site Settings > Head HTML | Paste at the end |
| `menu/after/2-header.html` | Developer Mode > HTML > the **header** file | **Replace** everything |
| `menu/after/3-css-all-devices.css` | Developer Mode > CSS > "…AFFECTS ALL DEVICES" | Paste at the **end** |
| `menu/after/4-css-desktop-and-tablet.css` | Developer Mode > CSS > "…AFFECTS DESKTOP AND TABLET DEVICES" | Delete one old line (below), then paste at the **end** |
| `menu/after/5-css-mobile.css` | Developer Mode > CSS > "…AFFECTS MOBILE DEVICES" | Paste at the **end** |
| `menu/after/6-body-end-html.html` *(optional)* | Site Settings > Body end HTML | Paste at the end (opens leaf photos as you scroll on phones) |
| `menu/after/7-mobile-menu-body-end.html` *(recommended)* | Site Settings > Body end HTML | Paste at the end. Gives phones the prototype's header: logo left, Menu button right, full-screen green menu with the X animation. Links still come from the Pages panel. |
| `menu/after/8-css-shop.css` | Developer Mode > CSS > "…AFFECTS ALL DEVICES" | Paste at the **end**, after file 3. Styles the shop (/store) to match: leaf photos that open on hover, forest titles and prices, gold buttons, berry "Sold out" label, matching fields. |

## Before you start
1. **Back up.** Copy the current header HTML and all three CSS panels into a text file, so you can paste them back if anything goes wrong.
2. **Switch the site from the left sidebar to a top header.**
   - The live site currently uses a **sidebar layout**: the menu you see is in the sidebar, not in the header file.
   - Until the layout is changed, the header file isn't shown, so editing it changes nothing.
   - In the editor, look for **Layout**, **Site layout** or **Header layout** (often under Design, or by clicking the sidebar). Choose a layout with the header across the top.
   - If your plan can't change the layout, stop and ask: the sidebar needs a different set of CSS.
3. **Hide "Home" from the menu** in the Pages panel (the logo already links home). That keeps the desktop menu on one row.
4. **Name the new page's address `/day-opportunities`.** The header button and the leaf marker next to "Day opportunities" in the menu rely on that address.

## Install
1. Head HTML: paste `menu/after/1-head-html.html`.
2. Header file: select all, delete, paste `menu/after/2-header.html`.
3. CSS **all devices**: paste `menu/after/3-css-all-devices.css` at the end.
4. CSS **desktop and tablet**:
   - delete this old line: `*.stickyHeaderSpacer { height:292.8999938964844px !important; }`
   - then paste `menu/after/4-css-desktop-and-tablet.css` at the end.
5. CSS **mobile**: paste `menu/after/5-css-mobile.css` at the end.
6. Optional: Body end HTML: paste `menu/after/6-body-end-html.html`.
7. **Preview** on desktop, tablet and mobile in the editor before you press **Publish**.

## Using the design on other parts of the site
- **Leaf-shaped photos:** in Developer Mode, add `shg-leaf`, `shg-leaf-soft` or `shg-leaf-r` to an image widget's outer `<div class="… imageWidget …">`. On a computer the leaf opens to the full photo on hover; on phones it opens as you scroll past (needs file 6).
- **Buttons** turn gold with dark green text automatically. Add `shg-btn-forest` to a button for the dark green version.
- **Colours** are available as CSS variables, for example `var(--shg-forest)`, `var(--shg-gold)`, `var(--shg-leaf-pale)`.

## What each screen size looks like
| Screen | Header |
|---|---|
| Desktop, 1280px and wider | One row: logo, menu, gold "Make an enquiry" button |
| Tablet and small laptops (768–1279px) | Logo and button on top, full menu underneath |
| Mobile | Logo and a short "Enquire" button, then the menu as one swipeable row (drop-downs hidden; sub-pages are reached from their parent page) |

**Phones use Duda's separate mobile layout.** Duda doesn't show the header file on phones. It uses its own header bar, hamburger button and slide-out menu, which is why the old menu still appeared on mobile.
- The second half of `menu/after/5-css-mobile.css` restyles those parts: logo in the bar, a dark green leaf-shaped hamburger, and a forest-green slide-out menu with white text and leaf bullets.
- The slide-out menu lists whatever is in the **Pages** panel. Hide the old pages there (Gallery, Blog, Acknowledgements, Privacy Policy and so on) to get down to the six new items.
- To add a "Make an enquiry" button on phones, add a button widget at the top of each page in the editor's mobile view. Duda's mobile header doesn't accept extra links from CSS.

**If Duda also shows its own hamburger menu on mobile,** you'll see two menus. Keep one: the last lines of `menu/after/5-css-mobile.css` show how to hide the swipe row.

## How it was tested
Before handing over, the CSS was checked in a mock-up that loads the live site's own Duda stylesheets, plus the old custom CSS from the panels, with the menu rendered the way Duda outputs it. It was tested at 1440, 1300, 1100, 820, 390 and 360px wide:
- menu items are 48px tall (44px on phones);
- drop-downs appear on hover and when tabbing with the keyboard;
- nothing overflows the screen.

**Still needs a real-editor check:** the layout switch, how Duda's mobile menu behaves, and the sticky header spacing.
