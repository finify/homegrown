<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { reduceMotion } from '../lib/reveal.js'

// Signature move: the main photograph slowly changes, like light shifting.
// Pauses when the tab is hidden; under reduced motion only the first image shows.
const props = defineProps({ images: Array, frame: { type: String, default: 'leaf-frame-soft' }, eager: Boolean, sizes: String })
const i = ref(0)
let t
const tick = () => { if (!document.hidden) i.value = (i.value + 1) % props.images.length }
onMounted(() => { if (!reduceMotion() && props.images.length > 1) t = setInterval(tick, 5600) })
onBeforeUnmount(() => clearInterval(t))
</script>

<template>
  <figure class="relative h-full w-full bg-stone" :class="frame">
    <img
      v-for="(im, n) in images"
      :key="im.src"
      :src="im.src"
      :alt="n === 0 ? im.alt : ''"
      :aria-hidden="n === 0 ? undefined : 'true'"
      :loading="eager && n === 0 ? 'eager' : 'lazy'"
      :fetchpriority="eager && n === 0 ? 'high' : undefined"
      width="1600" height="1200"
      class="absolute inset-0 h-full w-full object-cover transition-opacity duration-[1600ms] ease-in-out"
      :class="i === n ? 'opacity-100' : 'opacity-0'"
    />
    <figcaption class="sr-only">{{ images[0].alt }}</figcaption>
  </figure>
</template>
