// Generates one HTML entry per page with the titles and descriptions from the audit's SEO plan.
// Run with `node scripts/gen-html.mjs` after changing a title, description or the <head>.
import { writeFileSync } from 'node:fs'
const ORIGIN = 'https://finify.github.io/homegrown/'
const pages = [
  ['index', 'Home', 'home', 'Garden Centre & Day Opportunities, Sunderland | Home Grown', 'Plant nursery, garden centre and therapeutic horticulture in Thompson Park, Sunderland. Training and day opportunities for adults and young people.', 'polytunnel-group-potting'],
  ['day-opportunities', 'DayOpportunities', 'day', 'Day Opportunities for Adults with Learning Disabilities, Sunderland', 'Supported horticulture, training and work experience in Sunderland. For individuals, families and referrers. Register interest online.', 'participant-smiling'],
  ['garden-centre', 'GardenCentre', 'garden', 'Garden Centre & Plant Nursery, Thompson Park Sunderland', 'Bedding, hanging baskets and perennials grown on site. Open 7 days. Trade and wholesale enquiries welcome.', 'garden-centre-perennials'],
  ['whats-on', 'WhatsOn', 'whats', 'Workshops & Events | Sunderland Home Grown', "Christmas wreath workshops, children's crafts, Junior Joiners and weekly growing groups in Thompson Park, Sunderland.", 'primroses'],
  ['community', 'Community', 'community', 'Community Gardening & Groups, Sunderland | Home Grown', 'Fruit and veg growing, beekeeping, heritage and wellbeing groups in Southwick, Sunderland.', 'veg-harvest'],
  ['about', 'About', 'about', 'About Sunderland Home Grown CIC', 'A community interest company transforming a former council site in Thompson Park into a thriving nursery and training centre since 2017.', 'site-clearing-2016'],
  ['contact', 'Contact', 'contact', 'Contact & Find Us | Sunderland Home Grown, SR5 1SF', 'Opening times, directions, parking and how to get in touch.', 'shop-doorway'],
  ['privacy', 'Privacy', 'privacy', 'Privacy & Accessibility | Sunderland Home Grown', 'How Sunderland Home Grown CIC uses your information, and how we make this website accessible.', 'polytunnel-benches'],
]
// Prefetch every internal page early, and fully prerender one as soon as its link is hovered or
// pressed, so moving between pages is near-instant in Chrome and Edge.
const speculation = {
  prefetch: [{ where: { href_matches: '/homegrown/*' }, eagerness: 'eager' }],
  prerender: [{ where: { href_matches: '/homegrown/*' }, eagerness: 'moderate' }],
}
const jsonLd = {
  '@context': 'https://schema.org', '@type': ['GardenStore', 'LocalBusiness'], name: 'Sunderland Home Grown CIC',
  url: 'https://www.sunderlandhomegrown.co.uk/', telephone: '+44 191 549 9444', foundingDate: '2017',
  address: { '@type': 'PostalAddress', streetAddress: 'Thompson Park, Southwick', addressLocality: 'Sunderland', postalCode: 'SR5 1SF', addressCountry: 'GB' },
  openingHoursSpecification: [
    { '@type': 'OpeningHoursSpecification', dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], opens: '10:00', closes: '16:00' },
    { '@type': 'OpeningHoursSpecification', dayOfWeek: ['Saturday', 'Sunday'], opens: '09:30', closes: '15:30' },
  ],
  sameAs: ['https://www.facebook.com/sunderlandhomegrown'],
}
for (const [file, comp, key, title, desc, og] of pages) {
  writeFileSync(`src/entries/${file}.js`, `import { mountPage } from '../lib/mount.js'\nimport Page from '../pages/${comp}.vue'\n\nmountPage(Page, { current: '${key}' })\n`)
  const canonical = ORIGIN + (file === 'index' ? '' : `${file}.html`)
  writeFileSync(`${file}.html`, `<!doctype html>
<html lang="en-GB">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>${title}</title>
    <meta name="description" content="${desc}" />
    <link rel="canonical" href="${canonical}" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Sunderland Home Grown" />
    <meta property="og:title" content="${title}" />
    <meta property="og:description" content="${desc}" />
    <meta property="og:image" content="${ORIGIN}img/${og}.jpg" />
    <meta property="og:locale" content="en_GB" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="theme-color" content="#173A22" />
    <link rel="icon" type="image/png" href="favicon.png" />
    <link rel="preload" href="fonts/atkinson-hyperlegible-next-latin.woff2" as="font" type="font/woff2" crossorigin />
    <script type="speculationrules">${JSON.stringify(speculation)}</script>
${file === 'index' ? `    <script type="application/ld+json">${JSON.stringify(jsonLd)}</script>\n` : ''}  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/entries/${file}.js"></script>
  </body>
</html>
`)
}
writeFileSync('public/sitemap.xml', `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${pages.map(([f]) => `  <url><loc>${ORIGIN}${f === 'index' ? '' : f + '.html'}</loc></url>`).join('\n')}\n</urlset>\n`)
writeFileSync('public/robots.txt', `User-agent: *\nAllow: /\nSitemap: ${ORIGIN}sitemap.xml\n`)
