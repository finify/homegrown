import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)
export const reduceMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches

/**
 * v-reveal: the parts of a section ([data-r] children) rise in order as the section enters.
 * Content is visible by default; motion is only added when the script runs and motion is allowed.
 */
export const reveal = {
  mounted(el) {
    if (reduceMotion()) return
    if (el.getBoundingClientRect().top < window.innerHeight) return
    const parts = el.querySelectorAll('[data-r]')
    const targets = parts.length ? parts : [el]
    el._tween = gsap.from(targets, {
      y: 28, autoAlpha: 0, duration: 0.8, ease: 'power3.out', stagger: 0.08,
      scrollTrigger: { trigger: el, start: 'top 82%', once: true },
    })
  },
  unmounted(el) { el._tween?.scrollTrigger?.kill(); el._tween?.kill() },
}

/** v-parallax="0.15": a slow drift on photographs tied to scroll. */
export const parallax = {
  mounted(el, { value = 0.12 }) {
    if (reduceMotion()) return
    el._tween = gsap.fromTo(el, { yPercent: -value * 50, scale: 1.08 }, {
      yPercent: value * 50, scale: 1.08, ease: 'none',
      scrollTrigger: { trigger: el.parentElement, start: 'top bottom', end: 'bottom top', scrub: true },
    })
  },
  unmounted(el) { el._tween?.scrollTrigger?.kill(); el._tween?.kill() },
}

export { gsap, ScrollTrigger }
