<script setup>
import SiteHeader from './SiteHeader.vue'
import SiteFooter from './SiteFooter.vue'
defineProps({ current: String })
</script>

<template>
  <a href="#main" class="btn btn-primary sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[60]">Skip to main content</a>
  <SiteHeader :current="current" />
  <main id="main" tabindex="-1" class="outline-none">
    <slot />
  </main>
  <SiteFooter />
</template>
