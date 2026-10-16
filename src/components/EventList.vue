<script setup>
import { ref, computed } from 'vue'
import { events } from '../lib/events.js'
import { img } from '../lib/site.js'

// Upcoming workshops with a simple filter. Each "Book" goes to the existing Ecwid product.
const props = defineProps({ limit: Number, filters: Boolean })
const filter = ref('all')
const options = [['all', 'Everything'], ['children', 'Children and young people'], ['adults', 'Adults']]
const list = computed(() => {
  const l = events.filter((e) => filter.value === 'all' || e.audience === filter.value)
  return props.limit ? l.slice(0, props.limit) : l
})
const confirmify = (s) => s.replace(/\[CONFIRM:[^\]]+\]/g, (m) => `<span class="confirm">${m}</span>`)
</script>

<template>
  <div>
    <fieldset v-if="filters" class="mb-10">
      <legend class="mb-3 font-bold text-forest">Show</legend>
      <div class="flex flex-wrap gap-2">
        <label v-for="[v, l] in options" :key="v" class="flex min-h-[3rem] cursor-pointer items-center gap-3 rounded-leaf bg-stone px-5 font-bold text-forest transition-colors has-[:checked]:bg-forest has-[:checked]:text-white has-[:focus-visible]:outline has-[:focus-visible]:outline-[3px] has-[:focus-visible]:outline-offset-2 has-[:focus-visible]:outline-forest">
          <input v-model="filter" type="radio" name="event-filter" :value="v" class="sr-only" /> {{ l }}
        </label>
      </div>
      <p class="sr-only" aria-live="polite">{{ list.length }} events shown</p>
    </fieldset>

    <ul class="grid gap-x-10 gap-y-14 md:grid-cols-2">
      <li v-for="e in list" :key="e.title + e.date" class="group grid grid-cols-[5.5rem_1fr] gap-5 sm:grid-cols-[7.5rem_1fr]">
        <div class="leaf-frame aspect-square bg-stone">
          <img :src="img(e.img + '-sm')" alt="" width="800" height="800" class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105" />
        </div>
        <div>
          <h3 class="text-lead font-bold">{{ e.title }}</h3>
          <dl class="mt-3 grid grid-cols-[auto_1fr] gap-x-4 gap-y-1">
            <dt class="font-bold text-forest">When</dt><dd><span v-html="confirmify(e.date)"></span>, <span v-html="confirmify(e.time)"></span></dd>
            <dt class="font-bold text-forest">Who</dt><dd>{{ e.who }}</dd>
            <dt class="font-bold text-forest">Price</dt><dd v-html="confirmify(e.price)"></dd>
          </dl>
          <p v-if="e.note" class="mt-2 text-soft">{{ e.note }}</p>
          <p class="mt-4">
            <span v-if="e.soldOut" class="inline-flex min-h-[3rem] items-center rounded-leaf bg-berry-pale px-5 font-bold text-berry">Sold out</span>
            <a v-else :href="e.href" class="btn btn-forest" rel="noopener">Book {{ e.title.toLowerCase() }}<span class="sr-only">, {{ e.date }}</span></a>
          </p>
        </div>
      </li>
    </ul>
  </div>
</template>
