# Blog: landing page and single posts

`before/blog.html` is the Blog page as it was (your backup). `after/blog.html` is the new one.

## Install
1. **Blog landing page:** open the Blog page in Developer Mode, select all its HTML, delete it and paste `after/blog.html`.
2. **Nothing else.** The styles are in `base.css`, which is already linked site-wide. That's deliberate: single blog posts share one Duda template and have no page HTML of their own, so a site-wide file is the only way to reach them.
3. **Preview** desktop, tablet and mobile, then **Publish**:
   `https://websitebuilder.123-reg.co.uk/site/0432dc74/blog?preview=true&insitepreview=true&dm_device=desktop`
   (change `desktop` to `tablet` or `mobile`).

## Landing page
- **Header:** "News and growing tips", the "Home Grown Blog" title, a short line about the blog, and Duda's own search box restyled as a large rounded field.
- **Post list:** Duda's own blog list widget (same id), so new posts appear automatically.
  - **Featured post:** the newest post runs across the full width, with a large photo.
  - **Grid:** the rest sit 3 across on desktop, 2 on tablet and 1 on phones.
  - **Cards:** whole card clickable, date with a leaf marker, 3-line summary and a "Read more" link. The photo zooms gently on hover.
  - **More posts:** a gold button.
- **List settings changed in the HTML:** 7 posts shown (1 featured + 6), "Read more" switched on, 3-line summaries, and Duda's own image hover effect off (the CSS adds its own).

## Single posts (CSS only, applies to every post automatically)
- **Header:** the post's own header photo, under a deep green shade, with a large white title and the date in a small label.
- **Text:** one comfortable reading column (about 46rem wide) at 19px, even when the post was written in two columns.
- **Photos:** rounded, with their captions underneath.
- **Closing note:** a post's last single-paragraph row (such as "Want to learn more… join our weekly Garden group") becomes a pale green box.
- **Navigation:** "Older post / Newer post" become buttons.
- **More from the blog:** the related posts underneath get that heading and the same cards as the landing page.

**One for the post template:** Duda's post titles are an `h3`, not an `h1`, so screen readers find no main heading. If the blog post layout lets you change the title's heading level, set it to H1.

## Also fixed while checking the preview: the tablet menu
The tablet preview uses Duda's own **tablet layout**, which wasn't showing our menu bar.
- Tablets now get the same bar as phones: logo, "Menu" button and the full-screen green menu.
- The links come from the Pages panel, respecting each page's "show on tablet" setting.
- It's in `site.js`, so there's nothing to paste.

## How it was tested
On the **live preview** (desktop 1440px, tablet layout, and iPhone), with the new styles swapped in:
- the landing page restructured as the new HTML will make it;
- the Callicarpa post.

The checks:
- columns are 3, 2 and 1 across;
- the featured post's layout is right;
- nothing overflows the screen;
- buttons and the search field are at least 44px.
