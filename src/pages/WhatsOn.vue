<script setup>
import EventList from '../components/EventList.vue'
import FaqList from '../components/FaqList.vue'
import { groups } from '../lib/events.js'
import { img, url, site } from '../lib/site.js'

const confirmify = (s) => s.replace(/\[CONFIRM:[^\]]+\]/g, (m) => `<span class="confirm">${m}</span>`)
const parentFaqs = [
  { q: 'Do I need to stay with my child?', a: '<p><span class="confirm">[CONFIRM: whether parents stay, and for which ages]</span></p>' },
  { q: 'Who runs the workshops?', a: '<p>Our own staff. <span class="confirm">[CONFIRM: who supervises, DBS checks]</span></p>' },
  { q: 'What should we bring?', a: '<p>Clothes that can get messy, and a coat if it is cold. We provide materials. <span class="confirm">[CONFIRM]</span></p>' },
  { q: 'Are workshops accessible?', a: '<p>Tell us what your child needs when you book and we will plan for it. <span class="confirm">[CONFIRM]</span></p>' },
  { q: 'Can I get a refund?', a: '<p><span class="confirm">[CONFIRM: refund and cancellation policy]</span></p>' },
]
</script>

<template>
  <section class="pb-16 pt-10 lg:pb-24 lg:pt-16" aria-labelledby="page-title">
    <div class="wrap grid items-end gap-10 lg:grid-cols-12">
      <div class="lg:col-span-7" v-reveal>
        <h1 id="page-title" class="text-display" data-r>What's on</h1>
        <p class="mt-6 max-w-[44ch] text-lead text-soft" data-r>Workshops for children and adults, and weekly groups anyone can join. Book online, or just turn up to a group.</p>
      </div>
      <div class="flex gap-3 lg:col-span-5 lg:justify-end" aria-hidden="true">
        <Pic :name="'bird-box-joinery-sm'" alt="" class="leaf-frame h-28 w-28 object-cover sm:h-36 sm:w-36" />
        <Pic :name="'primroses-sm'" alt="" class="leaf-frame-r h-28 w-28 object-cover sm:h-36 sm:w-36" />
        <Pic :name="'squash-polytunnel-sm'" alt="" class="leaf-frame h-28 w-28 object-cover sm:h-36 sm:w-36" />
      </div>
    </div>
  </section>

  <section class="section pt-0" aria-labelledby="workshops-title">
    <div class="wrap">
      <h2 id="workshops-title" class="text-title">Workshops</h2>
      <p class="mt-4 max-w-[60ch] text-soft">Booking opens our online shop. Workshops are the only things sold online: plants are in store only.</p>
      <EventList filters class="mt-10" />
    </div>
  </section>

  <section class="pb-24 lg:pb-40" aria-label="Photos from our workshops and groups">
    <div class="wrap grid grid-cols-12 items-end gap-3">
      <figure class="col-span-12 sm:col-span-7">
        <Pic :name="'group-planting-workshop'" alt="Four people smiling as they plant up pots together in the workshop." loading="lazy" class="leaf-frame-soft aspect-[4/3] w-full object-cover" />
        <figcaption class="mt-3 text-sm text-soft">Planting up in the workshop.</figcaption>
      </figure>
      <figure class="col-span-12 sm:col-span-5">
        <Pic :name="'veg-harvest'" alt="Crates of squash, peppers and greens harvested by the fruit and veg group." loading="lazy" class="leaf-frame-r aspect-[4/5] w-full object-cover" />
        <figcaption class="mt-3 text-sm text-soft">A Monday harvest from the fruit and veg group.</figcaption>
      </figure>
    </div>
  </section>

  <section class="section bg-forest text-white on-dark" aria-labelledby="regular-title">
    <div class="wrap">
      <div class="grid gap-6 lg:grid-cols-12" v-reveal>
        <h2 id="regular-title" class="text-title text-white lg:col-span-5" data-r>Every week, every month</h2>
        <p class="max-w-[46ch] text-lead text-leaf-pale lg:col-span-6 lg:col-start-7" data-r>Free to join unless we say otherwise. <span class="confirm">[CONFIRM: costs]</span></p>
      </div>
      <ul class="mt-14 grid gap-3 md:grid-cols-3" v-reveal>
        <li v-for="(g, i) in groups" :key="g.title" class="flex flex-col rounded-leaf-lg p-7" :class="i === 0 ? 'bg-gold text-ink' : 'bg-forest-700'" data-r>
          <h3 class="text-lead font-bold" :class="i === 0 ? 'text-forest' : 'text-white'">{{ g.title }}</h3>
          <p class="mt-4 font-bold" v-html="confirmify(g.when)"></p>
          <p class="mt-1" :class="i === 0 ? 'text-ink' : 'text-leaf-pale'">{{ g.where }}</p>
          <a :href="url(g.href)" class="mt-8 inline-flex min-h-[2.75rem] items-center self-start font-bold underline decoration-2" :class="i === 0 ? 'text-forest' : 'text-white decoration-gold'">More about this group</a>
        </li>
      </ul>
      <p class="mt-12" v-reveal><a :href="site.facebook" class="btn btn-white" rel="noopener" data-r>Latest news on Facebook</a></p>
    </div>
  </section>

  <FaqList :items="parentFaqs" id="parents-faq" title="For parents and carers" />
</template>
