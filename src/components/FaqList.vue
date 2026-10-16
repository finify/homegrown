<script setup>
// Accordion of filled tiles. Native <details> so it works without script.
defineProps({ title: { type: String, default: 'Questions people ask' }, items: Array, id: { type: String, default: 'faq' } })
</script>

<template>
  <section class="section" :aria-labelledby="`${id}-title`">
    <div class="wrap grid gap-10 lg:grid-cols-12">
      <div class="lg:col-span-4">
        <h2 :id="`${id}-title`" class="text-title lg:sticky lg:top-32">{{ title }}</h2>
      </div>
      <div class="space-y-2 lg:col-span-8" v-reveal>
        <details v-for="q in items" :key="q.q" :name="id" class="group rounded-leaf bg-stone open:bg-gold" data-r>
          <summary class="flex min-h-[4.5rem] cursor-pointer list-none items-center justify-between gap-6 rounded-leaf px-6 py-4 text-lead font-bold text-forest [&::-webkit-details-marker]:hidden">
            {{ q.q }}
            <span class="relative h-4 w-4 shrink-0" aria-hidden="true">
              <span class="absolute left-0 top-[6.5px] h-[3px] w-4 rounded bg-forest"></span>
              <span class="absolute left-0 top-[6.5px] h-[3px] w-4 rotate-90 rounded bg-forest transition-transform duration-300 group-open:rotate-0"></span>
            </span>
          </summary>
          <div class="max-w-[60ch] px-6 pb-6 text-ink" v-html="q.a"></div>
        </details>
      </div>
    </div>
  </section>
</template>
