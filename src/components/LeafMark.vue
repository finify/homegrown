<script setup>
// The roundel's three leaves as flat SVG: fallback for the 3D scenes and the footer mark.
defineProps({ title: { type: String, default: '' } })
const leaf = 'M0 0 C 36 -20 36 -78 0 -104 C -36 -78 -36 -20 0 0 Z'
</script>

<template>
  <svg viewBox="-120 -125 240 135" :role="title ? 'img' : undefined" :aria-hidden="title ? undefined : 'true'" :aria-label="title || undefined">
    <path :d="leaf" fill="#3DB82A" transform="rotate(-34) scale(.92)" />
    <path :d="leaf" fill="#934F4E" transform="rotate(34) scale(.95)" />
    <path :d="leaf" fill="#E9B82B" transform="scale(1.12)" />
  </svg>
</template>
