<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import LeafMark from './LeafMark.vue'
import { gsap, ScrollTrigger, reduceMotion } from '../lib/reveal.js'
import { webglAvailable, saveData, whenIdleAndNear } from '../three/support.js'

// The roundel's three leaves in 3D. They unfurl on load, follow the pointer
// gently, and turn and lift as the hero scrolls away.
const props = defineProps({ trigger: { type: String, default: null } })
const canvas = ref(null)
const fallback = ref(false)
let scene, st, onMove, cancel, gone = false

onMounted(() => {
  if (!webglAvailable() || saveData()) { fallback.value = true; return }
  cancel = whenIdleAndNear(canvas.value, start, '0px')
})

async function start() {
  const still = reduceMotion()
  const { createHeroLeaves } = await import('../three/heroLeaves.js')
  if (gone) return
  scene = createHeroLeaves(canvas.value, { animate: !still })
  if (still) return

  gsap.to(scene.state, { open: 1, duration: 2.2, ease: 'elastic.out(1, 0.6)', delay: 0.2 })
  st = ScrollTrigger.create({
    trigger: props.trigger || canvas.value,
    start: 'top top',
    end: 'bottom top',
    scrub: 0.6,
    onUpdate: (s) => (scene.state.scroll = s.progress),
  })
  onMove = (e) => {
    scene.state.px = (e.clientX / window.innerWidth) * 2 - 1
    scene.state.py = (e.clientY / window.innerHeight) * 2 - 1
  }
  window.addEventListener('pointermove', onMove, { passive: true })
}

onBeforeUnmount(() => {
  gone = true
  cancel?.()
  st?.kill()
  window.removeEventListener('pointermove', onMove)
  scene?.dispose()
})
</script>

<template>
  <div aria-hidden="true">
    <canvas v-if="!fallback" ref="canvas" class="block h-full w-full"></canvas>
    <LeafMark v-else class="h-full w-full p-8" />
  </div>
</template>
