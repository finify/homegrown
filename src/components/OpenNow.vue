<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { openStatus } from '../lib/hours.js'

// The one live thing: is the garden centre open right now (UK time)?
defineProps({ dark: Boolean })
const status = ref(null)
let timer
onMounted(() => {
  status.value = openStatus()
  timer = setInterval(() => (status.value = openStatus()), 30000)
})
onBeforeUnmount(() => clearInterval(timer))
</script>

<template>
  <p class="flex min-h-[1.6em] items-center gap-3" role="status" aria-live="polite">
    <template v-if="status">
    <span
      class="relative inline-block h-4 w-4 shrink-0"
      :class="status.open ? 'bg-leaf' : 'bg-berry'"
      style="border-radius: 0 100% 0 100%"
      aria-hidden="true"
    ></span>
    <span>
      <strong :class="dark ? 'text-white' : 'text-forest'">{{ status.text }}.</strong>
      {{ status.detail }}.
    </span>
    </template>
  </p>
</template>
