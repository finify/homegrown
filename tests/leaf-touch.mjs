const pw = await import(process.env.PW)
const b = await pw.chromium.launch()
const ctx = await b.newContext({ ...pw.devices['iPhone 13'], })
const pages = ['index', 'day-opportunities', 'garden-centre', 'whats-on', 'community', 'about', 'contact']
let ok = 0, wrong = []
for (const pg of pages) {
  const p = await ctx.newPage()
  await p.goto('http://localhost:4173/homegrown/' + pg + '.html', { waitUntil: 'networkidle' })
  console.log(pg, 'hover:none =', await p.evaluate(() => matchMedia('(hover: none)').matches))
  const h = await p.evaluate(() => document.body.scrollHeight)
  for (let y = 0; y < h; y += 350) {
    await p.evaluate((y) => window.scrollTo(0, y), y); await p.waitForTimeout(250)
    const res = await p.evaluate(() => {
      const vh = innerHeight, out = []
      document.querySelectorAll('.leaf-frame, .leaf-frame-soft, .leaf-frame-r').forEach((el) => {
        const r = el.getBoundingClientRect(); if (!r.width) return
        const inBand = r.bottom > vh * 0.3 && r.top < vh * 0.7
        const open = el.classList.contains('leaf-open')
        // ignore the hero slideshow images that only exist after idle, and sticky edge cases
        out.push([inBand, open])
      })
      return out
    })
    for (const [inBand, open] of res) inBand === open ? ok++ : wrong.push(pg + '@' + y)
  }
  await p.close()
}
console.log(`checks passed: ${ok}, mismatches: ${wrong.length}`, [...new Set(wrong)].slice(0, 10))
await b.close()
