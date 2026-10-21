// Kept separate from the scenes so pages can check for WebGL without loading three.js.
export function webglAvailable() {
  try {
    const c = document.createElement('canvas')
    return !!(window.WebGLRenderingContext && (c.getContext('webgl2') || c.getContext('webgl')))
  } catch {
    return false
  }
}

/** Visitors who asked to save data get the flat SVG leaves instead of the 3D scenes. */
export const saveData = () => navigator.connection?.saveData === true

/**
 * Run `cb` only once the page has finished loading, the browser is idle, and `el`
 * is within `margin` of the viewport. Keeps three.js (the heaviest script) off the
 * critical path: it never delays the first paint or the photos.
 */
export function whenIdleAndNear(el, cb, margin = '600px') {
  let io, cancelled = false
  const idle = window.requestIdleCallback || ((f) => setTimeout(f, 300))
  const watch = () => idle(() => {
    if (cancelled) return
    io = new IntersectionObserver(([e]) => {
      if (e.isIntersecting) { io.disconnect(); cb() }
    }, { rootMargin: margin })
    io.observe(el)
  })
  if (document.readyState === 'complete') watch()
  else window.addEventListener('load', watch, { once: true })
  return () => { cancelled = true; io?.disconnect() }
}
