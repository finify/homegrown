// Sunderland Home Grown prototype: offline-friendly caching.
// GitHub Pages only lets browsers cache files for 10 minutes, so without this every page
// change re-downloads scripts and photos. Strategy:
//   - hashed build assets, photos and fonts: cache first (their URLs change when content does)
//   - pages (HTML): always try the network first so new deploys show straight away;
//     fall back to the cached copy if the network is slow (over 2.5s) or offline
const VERSION = 'shg-v1'
const SCOPE = new URL(self.registration.scope).pathname

self.addEventListener('install', () => self.skipWaiting())
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  )
})

const isStatic = (path) => /\/(assets|img|fonts)\//.test(path) || path.endsWith('.png')

self.addEventListener('fetch', (event) => {
  const { request } = event
  const url = new URL(request.url)
  if (request.method !== 'GET' || url.origin !== location.origin || !url.pathname.startsWith(SCOPE)) return

  if (isStatic(url.pathname)) {
    event.respondWith(
      caches.open(VERSION).then(async (cache) => {
        const hit = await cache.match(request)
        if (hit) return hit
        const res = await fetch(request)
        if (res.ok) cache.put(request, res.clone())
        return res
      }),
    )
    return
  }

  if (request.mode === 'navigate' || request.headers.get('accept')?.includes('text/html')) {
    const key = url.pathname.endsWith('/') ? url.pathname + 'index.html' : url.pathname
    event.respondWith(
      caches.open(VERSION).then(async (cache) => {
        const network = fetch(request).then((res) => {
          if (res.ok) cache.put(key, res.clone())
          return res
        })
        const slow = new Promise((resolve) => setTimeout(resolve, 2500)).then(() => cache.match(key))
        try {
          return (await Promise.race([network, slow])) || (await network)
        } catch {
          return (await cache.match(key)) || Response.error()
        }
      }),
    )
  }
})
