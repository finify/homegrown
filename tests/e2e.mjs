const pw = await import(process.env.PW)
import { readFileSync } from 'node:fs'
const axe = readFileSync('node_modules/axe-core/axe.min.js', 'utf8')
const B = 'http://localhost:4173/homegrown/'
const pages = ['index', 'day-opportunities', 'garden-centre', 'whats-on', 'community', 'about', 'contact', 'privacy']
const browser = await pw.chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] })
const results = []
const ok = (name, pass, info = '') => results.push(`${pass ? 'PASS' : 'FAIL'}  ${name}${info ? '  — ' + info : ''}`)

for (const w of [375, 768, 1440]) {
  const ctx = await browser.newContext({ viewport: { width: w, height: 900 }, reducedMotion: 'reduce' })
  for (const p of pages) {
    const page = await ctx.newPage(); const errs = []
    page.on('pageerror', (e) => errs.push(e.message)); page.on('console', (m) => m.type() === 'error' && errs.push(m.text()))
    await page.goto(B + p + '.html', { waitUntil: 'networkidle' })
    const over = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth)
    ok(`${p} @${w} no horizontal overflow`, over <= 0, over > 0 ? `${over}px` : '')
    if (w === 1440 || w === 375) {
      const small = await page.evaluate(() => [...document.querySelectorAll('a, button, select, input:not([type=checkbox]):not([type=radio]), summary')].filter((e) => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width && r.height && cs.display !== 'inline' && r.height < 44 && !e.closest('.sr-only') }).map((e) => (e.textContent || e.id).trim().slice(0, 30)))
      ok(`${p} @${w} tap targets ≥44px (block-level)`, small.length === 0, small.slice(0, 5).join(' | '))
    }
    if (w === 1440) {
      await page.addScriptTag({ content: axe })
      const r = await page.evaluate(async () => (await axe.run(document, { runOnly: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa', 'best-practice'] })).violations.map((v) => `${v.id}(${v.nodes.length}): ${v.nodes[0].target}`))
      ok(`${p} axe WCAG 2.2 AA`, r.length === 0, r.join(' ; '))
      const h1 = await page.locator('h1').count(); ok(`${p} exactly one h1`, h1 === 1, String(h1))
      const noalt = await page.evaluate(() => [...document.images].filter((i) => !i.hasAttribute('alt')).length); ok(`${p} all images have alt`, noalt === 0, String(noalt))
    }
    ok(`${p} @${w} no console errors`, errs.length === 0, errs.join(' | '))
    await page.close()
  }
  await ctx.close()
}

// Interactions
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } })
const page = await ctx.newPage()
await page.goto(B + 'day-opportunities.html#register', { waitUntil: 'networkidle' })
await page.click('#register button[type=submit]')
const errCount = await page.locator('#register [role=alert] li').count()
ok('Referral form: empty submit shows error summary', errCount === 5, `${errCount} errors`)
ok('Referral form: focus moves to error summary', await page.evaluate(() => document.activeElement?.getAttribute('role') === 'alert'))
await page.selectOption('#f-role', 'A social worker')
ok('Referral form: organisation appears for professionals', await page.locator('#f-organisation').isVisible())
await page.fill('#f-name', 'Sam Test'); await page.fill('#f-organisation', 'Council'); await page.fill('#f-email', 'garbage@'); await page.fill('#f-phone', '12')
await page.click('#register button[type=submit]')
const msgs = await page.locator('#register .field-error').allTextContents()
ok('Referral form: garbage email and phone rejected', msgs.some((m) => m.includes('email address like')) && msgs.some((m) => m.includes('10 digits')), msgs.join(' / '))
await page.fill('#f-email', 'sam@example.com'); await page.fill('#f-phone', '0191 549 9444'); await page.check('#f-consent')
await page.click('#register button[type=submit]')
ok('Referral form: valid submit shows thank-you', await page.getByText('Thank you, Sam.').isVisible())

await page.goto(B + 'day-opportunities.html', { waitUntil: 'networkidle' })
await page.focus('#tab-for-you'); await page.keyboard.press('ArrowRight')
ok('Tabs: arrow key moves to families panel', await page.locator('#panel-families').isVisible() && await page.evaluate(() => document.activeElement.id === 'tab-families'))
await page.goto(B + 'index.html'); await page.goto(B + 'day-opportunities.html#professionals', { waitUntil: 'networkidle' })
ok('Tabs: #professionals deep link opens that panel', await page.locator('#panel-professionals').isVisible())

await page.goto(B + 'contact.html?type=hire', { waitUntil: 'networkidle' })
ok('Contact: ?type=hire preselects enquiry type', (await page.inputValue('#c-type')) === 'hire')
await page.click('form button[type=submit]')
ok('Contact: empty submit shows errors', (await page.locator('.field-error').count()) >= 3)

await page.goto(B + 'whats-on.html', { waitUntil: 'networkidle' })
const all = await page.locator('section[aria-labelledby=workshops-title] li h3').count()
await page.click('label:has-text("Adults")')
const adults = await page.locator('section[aria-labelledby=workshops-title] li h3').count()
ok("What's on: filter reduces list", adults < all, `${all} -> ${adults}`)

await page.goto(B + 'community.html', { waitUntil: 'networkidle' })
await page.click('#membership button[type=submit]')
ok('Newsletter: empty submit shows error', await page.locator('#membership [role=alert]').isVisible())

const m = await browser.newPage({ viewport: { width: 390, height: 844 } })
await m.goto(B + 'index.html', { waitUntil: 'networkidle' })
await m.click('button[aria-controls=mobile-menu]')
ok('Mobile menu opens and focuses first link', await m.locator('#mobile-menu').isVisible() && await m.evaluate(() => document.activeElement.closest('#mobile-menu') !== null))
await m.keyboard.press('Escape')
ok('Mobile menu closes on Escape, focus returns', !(await m.locator('#mobile-menu').isVisible()) && await m.evaluate(() => document.activeElement.getAttribute('aria-controls') === 'mobile-menu'))

const links = await page.evaluate(() => 0)
await browser.close()
console.log(results.join('\n'))
console.log(`\n${results.filter((r) => r.startsWith('FAIL')).length} failures of ${results.length}`)
