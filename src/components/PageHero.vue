<script setup>
// Inner-page hero: headline and one sentence on the ground, one leaf-framed photograph.
defineProps({ title: String, lead: String, image: String, alt: String, tone: { type: String, default: 'leaf' } })
</script>

<template>
  <section class="relative overflow-hidden pb-16 pt-10 lg:pb-28 lg:pt-16" aria-labelledby="page-title">
    <div class="wrap grid items-center gap-10 lg:grid-cols-12">
      <div class="lg:col-span-6" v-reveal>
        <h1 id="page-title" class="text-display" data-r>{{ title }}</h1>
        <p class="mt-6 max-w-[40ch] text-lead text-soft" data-r>{{ lead }}</p>
        <div class="mt-8 flex flex-wrap gap-3" data-r><slot name="actions" /></div>
        <div class="mt-8" data-r><slot name="extra" /></div>
      </div>
      <div class="relative lg:col-span-6">
        <div
          class="absolute -right-24 -top-10 h-[120%] w-[120%] sm:-right-32"
          :class="tone === 'gold' ? 'bg-gold' : tone === 'berry' ? 'bg-berry' : 'bg-leaf'"
          style="border-radius: 0 100% 0 100% / 0 100% 0 100%"
          aria-hidden="true"
        ></div>
        <div class="leaf-frame-soft relative aspect-[4/5] overflow-hidden bg-stone sm:aspect-[5/4] lg:aspect-[4/5]">
          <div class="h-full w-full" v-parallax="0.1"><Pic :name="image" :alt="alt" eager sizes="(min-width: 1024px) 45vw, 100vw" class="h-full w-full object-cover" /></div>
        </div>
      </div>
    </div>
  </section>
</template>
