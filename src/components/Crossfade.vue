<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { reduceMotion } from '../lib/reveal.js'

// Signature move: the main photograph slowly changes, like light shifting.
// Only the first photo loads with the page; the others are fetched once the page is idle,
// so they never compete with the first paint. Pauses when the tab is hidden; under reduced
// motion only the first image shows.
const props = defineProps({ images: Array, frame: { type: String, default: 'leaf-frame-soft' }, eager: Boolean, sizes: String })
const i = ref(0)
const ready = ref(false)
let t
const tick = () => { if (!document.hidden) i.value = (i.value + 1) % props.images.length }
onMounted(() => {
  if (reduceMotion() || props.images.length < 2) return
  const start = () => {
    ready.value = true
    t = setInterval(tick, 5600)
  }
  const idle = window.requestIdleCallback || ((cb) => setTimeout(cb, 1200))
  if (document.readyState === 'complete') idle(start)
  else window.addEventListener('load', () => idle(start), { once: true })
})
onBeforeUnmount(() => clearInterval(t))
</script>

<template>
  <figure class="relative h-full w-full bg-stone" :class="frame">
    <template v-for="(im, n) in images" :key="im.name">
      <Pic
        v-if="n === 0 || ready"
        :name="im.name"
        :sizes="sizes"
        :alt="n === 0 ? im.alt : ''"
        :aria-hidden="n === 0 ? undefined : 'true'"
        :eager="eager && n === 0"
        class="absolute inset-0 h-full w-full object-cover transition-opacity duration-[1600ms] ease-in-out"
        :class="i === n ? 'opacity-100' : 'opacity-0'"
      />
    </template>
    <figcaption class="sr-only">{{ images[0].alt }}</figcaption>
  </figure>
</template>
