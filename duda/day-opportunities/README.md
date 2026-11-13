# Day opportunities page (for service users, families and referrers)

The team want more service users, so this page makes it easy to say "yes, tell me more": a free trial visit is offered from the first screen to the last, and the page ends with a short register-interest form.

## 1. Create the page
1. In the editor: **Pages → Add page → Blank page**. Name it **Day opportunities** and set its URL to **`day-opportunities`**. The footer's "Day opportunities" and "Make a referral" links already point there.
2. Open the new page in **Developer Mode**, select all its HTML and paste `after/day-opportunities.html`.
3. In the page's own settings, **Head HTML**, add:
   ```html
   <link rel="stylesheet" href="https://finify.github.io/homegrown/duda/day.css">
   ```
4. **The form (important):** click the form on the page, open its settings, and check where submissions are sent (the "send to" email) and the email subject ("Day opportunities: new interest"). I copied the settings from the Home page form so it should already go to the same inbox. **After publishing, send one test entry** and check it arrives.
5. Add it to the **top menu**. It's worth putting it near the start, for example straight after Home.
6. Preview desktop, tablet and phone, then **Publish**.

## 2. Home page: the call to action
Paste `../home/after/day-cta-row.html` into the Home page HTML **just below the hero row** (after the row that starts `<div class="dmRespRow shg-home__hero shg-video-hero"`, so it's the first thing after the video). The styles are already in `home.css`.

It's a deep green panel: "What if the right place could help someone grow?", four ticks (free trial visits, group and one-to-one support, fully wheelchair accessible, referrals welcome), a gold **Book a free trial visit** button and **Find out more**.

**Optional, in the editor:** in the "Who are you here for?" cards on the Home page, change these two links:
- "Ask about a place" → `/day-opportunities`
- "Talk to us about a referral" → `/day-opportunities#register`

(`../home/after/home.html` already has all of this, for anyone pasting the whole Home page.)

## 3. Footer
"Make a referral" now goes to `/day-opportunities#register`. Change that one link in the footer in the editor, or re-paste `../footer/after/footer.html`.

## What's on the page
1. **Hero:** "What if the right place could help someone grow?", the flyer's strapline, **Book a free trial visit** (scrolls to the form) and **Call 0191 549 9444**, three ticks (Established over 11 years, Free trial visits, Referrals welcome), and the photo of Michelle and Lesley.
2. **About:** the flyer's paragraph and three photos from the site (they swipe sideways on phones).
3. **What you gain:** seven tiles with icons.
4. **Meaningful work-based activities:** five cards on a deep green band.
5. **True endorsements:** Michelle's and Andy's words, as on the flyer.
6. **Why families choose us** (ticks) and **Referrals welcome from** (list).
7. **Support that fits** and **Tailored support plans and funding.**
8. **Ready to start your journey?** Contact details beside the form. The form has name, phone, email, "I am" (myself, family member or carer, social worker, support coordinator, supported living provider, someone else), "I would like to" (book a free trial visit, make a referral, ask a question) and a box to tell us about the person.

Every block is a normal Duda text or image widget. The lists are ordinary bullet lists, so add or remove a line in the editor. Buttons linking to `#register` scroll to the form and put the cursor in the first box; this also works when arriving from the Home page (`/day-opportunities#register`).

## Please check before publishing
- **"Over 11 years":** the flyer says over 11 years, but the rest of the site says "since 2017" (about 9 years). One of them needs changing. It appears in the hero ticks, the about paragraph and "Why families choose us".
- **Address:** the flyer says **Unit 10, Thompson Park, Southwick, Sunderland SR5 2PL**. The rest of the site says **SR5 1SF**. I used the flyer's address on this page. Which is right?
- **Facebook:** linked as facebook.com/SunderlandHomeGrownCIC, from the flyer. Check it opens your page.
- **Permission:** please confirm Michelle and Andy (or their families) are happy for their names and words to be on the website, and Michelle and Lesley for the photo.
- **The flyer's own typos are fixed** ("usi a Direct Payment", "wheelchair insesent accessible").

## How it was tested
On the live preview (another page with this HTML swapped in, and the Home page with the new row), at desktop 1440px, tablet 820px and iPhone:
- no sideways scrolling and every photo loads;
- the form shows all six fields;
- "Book a free trial visit" scrolls to the form and puts the cursor in the name box.

It hasn't been submitted for real: do the test entry in step 1.4.
