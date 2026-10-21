<script setup>
import { computed, useAttrs } from 'vue'
import manifest from '../lib/images.json'
import { base } from '../lib/site.js'

// Responsive photo: AVIF first, WebP fallback, sized by `sizes` so phones get small files.
// `name` is the photo's base name; a trailing "-sm" marks a thumbnail slot.
defineOptions({ inheritAttrs: false })
const props = defineProps({
  name: { type: String, required: true },
  sizes: String,
  eager: Boolean,
})
const attrs = useAttrs()

const info = computed(() => {
  const small = props.name.endsWith('-sm')
  const key = small ? props.name.slice(0, -3) : props.name
  const entry = manifest[key] || { w: [800], ratio: 4 / 3 }
  const url = (w, ext) => `${base}img/opt/${key}-${w}.${ext}`
  const set = (ext) => entry.w.map((w) => `${url(w, ext)} ${w}w`).join(', ')
  const fallbackW = entry.w.find((w) => w >= (small ? 400 : 800)) || entry.w[entry.w.length - 1]
  return {
    avif: set('avif'),
    webp: set('webp'),
    src: url(fallbackW, 'webp'),
    sizes: props.sizes || (small ? '(min-width: 1024px) 18vw, 40vw' : '(min-width: 1024px) 50vw, 100vw'),
    width: fallbackW,
    height: Math.round(fallbackW / entry.ratio),
  }
})
</script>

<template>
  <picture class="contents">
    <source type="image/avif" :srcset="info.avif" :sizes="info.sizes" />
    <source type="image/webp" :srcset="info.webp" :sizes="info.sizes" />
    <img
      v-bind="attrs"
      :src="info.src"
      :width="attrs.width || info.width"
      :height="attrs.height || info.height"
      :loading="eager ? 'eager' : attrs.loading || 'lazy'"
      :fetchpriority="eager ? 'high' : undefined"
      decoding="async"
    />
  </picture>
</template>
