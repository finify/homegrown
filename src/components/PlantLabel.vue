<script setup>
// Key facts set as a nursery plant label: the tag that sits in every pot.
defineProps({ title: String, rows: Array, tone: { type: String, default: 'white' } })
</script>

<template>
  <div class="relative">
    <div
      class="relative px-6 pb-16 pt-8 sm:px-8"
      :class="tone === 'gold' ? 'bg-gold' : 'bg-white'"
      style="clip-path: polygon(0 0, 100% 0, 100% calc(100% - 2.5rem), 50% 100%, 0 calc(100% - 2.5rem)); border-radius: 1.5rem 0.25rem 0 0"
    >
      <span class="absolute right-6 top-6 h-4 w-4 rounded-full bg-ground" aria-hidden="true"></span>
      <h3 class="text-lead font-bold text-forest">{{ title }}</h3>
      <dl class="mt-6 divide-y-2" :class="tone === 'gold' ? 'divide-forest/20' : 'divide-stone'">
        <div v-for="r in rows" :key="r[0]" class="grid gap-1 py-3 sm:grid-cols-[9rem_1fr] sm:gap-4">
          <dt class="font-bold text-forest">{{ r[0] }}</dt>
          <dd><slot :name="r[0]"><span v-html="r[1]"></span></slot></dd>
        </div>
      </dl>
    </div>
  </div>
</template>
