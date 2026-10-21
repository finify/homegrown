// Touch-screen version of the hover reveal: phones and tablets can't hover, so each
// leaf-shaped photo opens out to the full picture while it sits in the middle band of the
// screen, and folds back into a leaf as it scrolls away.
const FRAMES = '.leaf-frame, .leaf-frame-soft, .leaf-frame-r'

export function revealLeavesOnScroll() {
  if (!window.matchMedia('(hover: none)').matches || !('IntersectionObserver' in window)) return

  const io = new IntersectionObserver(
    (entries) => entries.forEach((e) => e.target.classList.toggle('leaf-open', e.isIntersecting)),
    { rootMargin: '-30% 0px -30% 0px' }, // the middle 40% of the screen
  )
  const watch = (root) => {
    if (root.matches?.(FRAMES)) io.observe(root)
    root.querySelectorAll?.(FRAMES).forEach((el) => io.observe(el))
  }
  watch(document)

  // Photos added later (the hero slideshow, filtered event lists, tab panels) are picked up too.
  new MutationObserver((records) => records.forEach((r) => r.addedNodes.forEach((n) => n.nodeType === 1 && watch(n))))
    .observe(document.getElementById('app') || document.body, { childList: true, subtree: true })
}
