const pw = await import(process.env.PW)
const BASE = process.argv[2] || 'http://localhost:4173/homegrown/'
const b = await pw.chromium.launch()
const pages = ['index', 'day-opportunities', 'garden-centre', 'whats-on', 'community', 'about', 'contact', 'privacy']
let total = 0, bad = []
for (const pg of pages) {
  const p = await b.newPage({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' })
  await p.goto(BASE + pg + '.html', { waitUntil: 'networkidle' })
  // also include photos that are leaf-shaped via inline styles or other classes
  const n = await p.evaluate(() => {
    const els = [...document.querySelectorAll('main *')].filter((e) => {
      const cs = getComputedStyle(e)
      const isPhoto = e.tagName === 'IMG' || e.tagName === 'FIGURE' || e.querySelector?.(':scope > picture > img, :scope > img, :scope > div > picture > img')
      return isPhoto && /%/.test(cs.borderTopRightRadius + cs.borderTopLeftRadius) && e.getBoundingClientRect().width > 0
    })
    els.forEach((e, i) => e.setAttribute('data-leaf-test', i))
    return els.length
  })
  const visibleTabs = await p.$$('[role=tabpanel]')
  for (let i = 0; i < n; i++) {
    const sel = `[data-leaf-test="${i}"]`
    const el = p.locator(sel)
    if (!(await el.isVisible())) continue
    total++
    await el.scrollIntoViewIfNeeded()
    const before = await el.evaluate((e) => getComputedStyle(e).borderTopRightRadius + '|' + getComputedStyle(e).borderTopLeftRadius)
    await el.hover({ force: true }); await p.waitForTimeout(80)
    const after = await el.evaluate((e) => getComputedStyle(e).borderTopRightRadius + '|' + getComputedStyle(e).borderTopLeftRadius)
    if (/%/.test(after)) bad.push(`${pg}: ${await el.evaluate((e) => e.className.toString().slice(0, 80) + ' ' + (e.getAttribute('alt') || e.querySelector('img')?.getAttribute('alt') || '').slice(0, 40))}  (${before} -> ${after})`)
    await p.mouse.move(1, 1)
  }
  await p.close()
}
console.log(`checked ${total} leaf photos; ${bad.length} did not open`)
bad.forEach((x) => console.log('  ' + x))
await b.close()
