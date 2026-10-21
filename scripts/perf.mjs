// Measures FCP, LCP and bytes per page under "Slow 4G"-like throttling, cold cache and a click-through navigation.
const pw = await import(process.env.PW)
const BASE = process.argv[2] || 'https://finify.github.io/homegrown/'
const b = await pw.chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] })
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } })
const p = await ctx.newPage()
const cdp = await ctx.newCDPSession(p)
await cdp.send('Network.enable')
await cdp.send('Network.emulateNetworkConditions', { offline: false, latency: 150, downloadThroughput: 1.6e6 / 8, uploadThroughput: 750e3 / 8 })
await cdp.send('Emulation.setCPUThrottlingRate', { rate: 4 })
let bytes = 0
cdp.on('Network.loadingFinished', (e) => (bytes += e.encodedDataLength))
await p.addInitScript(() => {
  window.__lcp = 0
  new PerformanceObserver((l) => { for (const e of l.getEntries()) window.__lcp = e.startTime }).observe({ type: 'largest-contentful-paint', buffered: true })
})
const measure = async (label, nav) => {
  bytes = 0
  const t0 = Date.now()
  await nav()
  await p.waitForLoadState('load')
  const tLoad = Date.now() - t0
  await p.waitForTimeout(1500)
  const m = await p.evaluate(() => ({ fcp: performance.getEntriesByName('first-contentful-paint')[0]?.startTime || 0, lcp: window.__lcp }))
  console.log(`${label.padEnd(34)} FCP ${String(Math.round(m.fcp)).padStart(5)}ms  LCP ${String(Math.round(m.lcp)).padStart(5)}ms  load ${String(tLoad).padStart(5)}ms  ${(bytes / 1024).toFixed(0)} KB`)
}
await measure('home (cold)', () => p.goto(BASE))
await measure('-> day-opportunities (click)', () => p.click('header a[href*="day-opportunities"]:visible >> nth=0').catch(() => p.goto(BASE + 'day-opportunities.html')))
await measure('-> contact (nav)', () => p.goto(BASE + 'contact.html'))
await measure('-> home again', () => p.goto(BASE))
await b.close()
