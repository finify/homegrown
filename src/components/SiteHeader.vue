<script setup>
import { ref, watch, nextTick, onMounted, onBeforeUnmount } from 'vue'
import { nav, url, base } from '../lib/site.js'

const props = defineProps({ current: String })
const open = ref(false)
const scrolled = ref(false)
const menuBtn = ref(null)
const panel = ref(null)

const onScroll = () => (scrolled.value = window.scrollY > 8)
const onKey = (e) => {
  if (e.key === 'Escape' && open.value) { open.value = false; menuBtn.value?.focus() }
}
onMounted(() => { window.addEventListener('scroll', onScroll, { passive: true }); window.addEventListener('keydown', onKey); onScroll() })
onBeforeUnmount(() => { window.removeEventListener('scroll', onScroll); window.removeEventListener('keydown', onKey) })

watch(open, async (v) => {
  document.documentElement.style.overflow = v ? 'hidden' : ''
  if (v) { await nextTick(); panel.value?.querySelector('a')?.focus() }
})
</script>

<template>
  <header class="sticky top-0 z-50 bg-ground transition-colors" :class="scrolled && 'bg-ground/[.97]'">
    <div class="wrap flex h-20 items-center justify-between gap-6 lg:h-24">
      <a :href="url('index.html')" class="shrink-0 rounded-sm" aria-label="Sunderland Home Grown, home page">
        <img :src="`${base}img/logo-lozenge.png`" alt="" width="728" height="163" class="h-11 w-auto lg:h-[3.25rem]" />
      </a>

      <nav aria-label="Main" class="hidden xl:block">
        <ul class="flex items-center gap-1">
          <li v-for="item in nav" :key="item.key">
            <a
              :href="url(item.href)"
              :aria-current="props.current === item.key ? 'page' : undefined"
              class="relative flex min-h-[3rem] items-center rounded-leaf px-3.5 font-bold text-forest no-underline transition-colors hover:bg-stone"
              :class="[
                item.key === 'day' && 'text-forest',
                props.current === item.key && 'bg-leaf-pale',
              ]"
            >
              <span v-if="item.key === 'day'" class="leaf-bullet mr-2" aria-hidden="true"></span>
              {{ item.label }}
            </a>
          </li>
        </ul>
      </nav>

      <div class="flex items-center gap-3">
        <a :href="url('day-opportunities.html') + '#register'" class="btn btn-primary hidden sm:inline-flex">Make an enquiry</a>
        <button
          ref="menuBtn"
          type="button"
          class="btn btn-forest xl:hidden"
          :aria-expanded="open ? 'true' : 'false'"
          aria-controls="mobile-menu"
          @click="open = !open"
        >
          <span aria-hidden="true" class="relative block h-4 w-5">
            <span class="absolute left-0 h-[3px] w-5 rounded bg-current transition-transform" :class="open ? 'top-[7px] rotate-45' : 'top-0'"></span>
            <span class="absolute left-0 top-[7px] h-[3px] w-5 rounded bg-current transition-opacity" :class="open && 'opacity-0'"></span>
            <span class="absolute left-0 h-[3px] w-5 rounded bg-current transition-transform" :class="open ? 'top-[7px] -rotate-45' : 'top-[14px]'"></span>
          </span>
          {{ open ? 'Close' : 'Menu' }}
        </button>
      </div>
    </div>

    <div
      v-show="open"
      id="mobile-menu"
      ref="panel"
      class="on-dark fixed inset-x-0 bottom-0 top-20 overflow-y-auto bg-forest px-4 pb-10 pt-6 text-white sm:px-6 xl:hidden"
    >
      <nav aria-label="Main (mobile)">
        <ul class="space-y-1">
          <li v-for="item in nav" :key="item.key">
            <a
              :href="url(item.href)"
              :aria-current="props.current === item.key ? 'page' : undefined"
              class="flex min-h-[3.5rem] items-center gap-3 rounded-leaf px-3 text-[1.625rem] font-bold text-white no-underline hover:bg-forest-700"
              :class="props.current === item.key && 'bg-forest-700'"
            >
              <span class="leaf-bullet" :class="item.key === 'day' ? 'bg-gold' : 'bg-leaf'" aria-hidden="true"></span>
              {{ item.label }}
            </a>
          </li>
        </ul>
      </nav>
      <div class="mt-8 grid gap-3">
        <a :href="url('day-opportunities.html') + '#register'" class="btn btn-primary w-full">Make an enquiry</a>
        <a href="tel:+441915499444" class="btn btn-white w-full">Call 0191 549 9444</a>
      </div>
    </div>
  </header>
</template>
