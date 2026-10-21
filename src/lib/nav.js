// Make moving between pages feel instant.
// 1. Browsers with Speculation Rules (Chrome, Edge) prerender a page as soon as a link is hovered
//    or pressed; the rules live in each page's <head>.
// 2. Everywhere else, prefetch the next page's HTML on hover or touch so it is already cached.
// 3. A small service worker keeps assets and photos cached between visits, because GitHub Pages
//    only lets the browser cache files for ten minutes.
export function speedUpNavigation() {
  const supportsRules = HTMLScriptElement.supports?.('speculationrules')
  if (!supportsRules) {
    const done = new Set()
    const prefetch = (e) => {
      const a = e.target.closest?.('a[href]')
      if (!a || a.origin !== location.origin || a.pathname === location.pathname || done.has(a.pathname)) return
      done.add(a.pathname)
      const l = document.createElement('link')
      l.rel = 'prefetch'
      l.href = a.pathname
      document.head.appendChild(l)
    }
    document.addEventListener('pointerover', prefetch, { passive: true })
    document.addEventListener('touchstart', prefetch, { passive: true })
  }

  if ('serviceWorker' in navigator && import.meta.env.PROD) {
    window.addEventListener('load', () => navigator.serviceWorker.register(`${import.meta.env.BASE_URL}sw.js`).catch(() => {}))
  }
}
