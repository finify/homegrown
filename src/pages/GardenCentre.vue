<script setup>
import PageHero from '../components/PageHero.vue'
import OpenNow from '../components/OpenNow.vue'
import PlantLabel from '../components/PlantLabel.vue'
import FaqList from '../components/FaqList.vue'
import { img, url, site } from '../lib/site.js'

const season = [
  ['Bedding plants', 'Grown from plugs in our own polytunnels, in trays and pots.', 'bedding-trays'],
  ['Hanging baskets', 'Planted up on site. Petunias, trailing lobelia and more.', 'hanging-baskets'],
  ['Perennials', 'Salvias, scabious, daisies and cottage-garden favourites.', 'salvia-and-bee'],
  ['Spring colour', 'Primroses and polyanthus in every shade.', 'primroses'],
]
const tradeProof = ['Durham Cathedral', 'Palace Green, a World Heritage Site', 'Lumley Castle', 'Sherburn Village, Britain in Bloom Gold']
const visitRows = [
  ['Address', 'Thompson Park, Southwick, Sunderland SR5 1SF'],
  ['Open', 'Monday to Friday 10am to 4pm<br />Saturday and Sunday 9:30am to 3:30pm'],
  ['Parking', '<span class="confirm">[CONFIRM: car park details]</span>'],
  ['Paying', '<span class="confirm">[CONFIRM: card and cash]</span>'],
  ['Dogs', '<span class="confirm">[CONFIRM: dogs welcome?]</span>'],
]
const faqs = [
  { q: 'Can I buy plants online?', a: '<p>Not at the moment. Plants are sold in person at the garden centre. <span class="confirm">[CONFIRM]</span> You can book workshops online in our <a class="link" href="https://www.sunderlandhomegrown.co.uk/store">shop</a>.</p>' },
  { q: 'Do you deliver?', a: '<p><span class="confirm">[CONFIRM: delivery or collection options, especially for trade orders]</span></p>' },
  { q: 'Can you plant up my own baskets or containers?', a: '<p><span class="confirm">[CONFIRM: basket refill service and prices]</span></p>' },
  { q: 'Is the garden centre accessible?', a: '<p>Paths around the site are tarmacked for wheelchair users. <span class="confirm">[CONFIRM: complete]</span> Ask staff if you need a hand with heavy items.</p>' },
]
</script>

<template>
  <PageHero
    title="The garden centre"
    lead="Bedding, hanging baskets and perennials, most of them grown here in Thompson Park. Open seven days a week."
    :image="img('garden-centre-display')"
    alt="A garden centre display table crowded with purple and white flowering plants, with shelves of pots behind."
    tone="berry"
  >
    <template #actions>
      <a :href="url('contact.html') + '#getting-here'" class="btn btn-primary">Get directions</a>
      <a :href="url('contact.html') + '?type=trade'" class="btn btn-quiet">Trade enquiries</a>
    </template>
    <template #extra><OpenNow class="text-lead" /></template>
  </PageHero>

  <section class="section pt-0" aria-labelledby="season-title">
    <div class="wrap grid gap-10 lg:grid-cols-12">
      <div class="lg:col-span-3" v-reveal>
        <h2 id="season-title" class="text-title" data-r>Grown here</h2>
        <p class="mt-5 text-soft" data-r>What's on the benches changes through the year. <span class="confirm">[CONFIRM: current stock]</span></p>
      </div>
      <ul class="grid grid-cols-2 gap-x-3 gap-y-10 lg:col-span-9 lg:grid-cols-4" v-reveal>
        <li v-for="([t, b, im], i) in season" :key="t" data-r>
          <div class="aspect-[4/5] p-3" :class="['bg-leaf', 'bg-gold', 'bg-berry', 'bg-leaf-pale'][i]" style="border-radius: 1.5rem 0.25rem">
            <img :src="img(im + '-sm')" alt="" loading="lazy" class="leaf-frame-soft h-full w-full object-cover" />
          </div>
          <h3 class="mt-4 text-lead font-bold">{{ t }}</h3>
          <p class="mt-1 text-soft">{{ b }}</p>
        </li>
      </ul>
    </div>
  </section>

  <!-- Every purchase -->
  <section class="bg-forest py-24 text-white on-dark lg:py-32" aria-label="Why buying here matters">
    <div class="wrap grid items-center gap-10 lg:grid-cols-12" v-reveal>
      <p class="text-[1.5rem] font-bold leading-[1.3] sm:text-[2rem] lg:col-span-8 lg:text-[2.25rem]" data-r>
        Every plant you buy helps fund training and work experience for the people who grew it.
      </p>
      <p class="text-leaf-pale lg:col-span-3 lg:col-start-10" data-r><span class="confirm">[CONFIRM: wording]</span> Home Grown is a community interest company: profits go back into our work.</p>
    </div>
  </section>

  <!-- Trade -->
  <section class="section" aria-labelledby="trade-title">
    <div class="wrap grid gap-14 lg:grid-cols-12">
      <div class="lg:col-span-5" v-reveal>
        <h2 id="trade-title" class="text-title" data-r>Trade and wholesale</h2>
        <p class="mt-6 text-lead text-soft" data-r>We grow bedding and displays in volume for councils, businesses, villages and heritage sites.</p>
        <div class="mt-10 aspect-[4/3] overflow-hidden leaf-frame-soft" data-r>
          <img :src="img('komatsu-floral-display')" alt="A large floral display bed spelling out a company name in blue and yellow flowers, outside a business site." loading="lazy" class="h-full w-full object-cover" />
        </div>
        <p class="mt-3 text-sm text-soft" data-r>A floral display bed planted for a local business. <span class="confirm">[CONFIRM: project and permission to show]</span></p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7" v-reveal>
        <h3 class="text-lead font-bold" data-r>Our plants grow at</h3>
        <ul class="mt-6 grid gap-2 sm:grid-cols-2" data-r>
          <li v-for="t in tradeProof" :key="t" class="flex min-h-[7rem] items-end rounded-leaf bg-stone p-5 text-lead font-bold text-forest">{{ t }}</li>
        </ul>
        <div class="mt-10 rounded-leaf-lg bg-gold p-8" data-r>
          <p class="text-lead font-bold text-forest">Need plants in quantity?</p>
          <p class="mt-3">Tell us what you need, how many and when. <span class="confirm">[CONFIRM: minimum order, lead times]</span></p>
          <div class="mt-6 flex flex-wrap gap-3">
            <a :href="url('contact.html') + '?type=trade'" class="btn btn-forest">Send a trade enquiry</a>
            <a :href="site.phoneHref" class="btn btn-white">Call {{ site.phone }}</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Visit -->
  <section class="section bg-leaf-pale" aria-labelledby="visit-title">
    <div class="wrap grid items-start gap-14 lg:grid-cols-12">
      <div class="lg:col-span-5" v-reveal>
        <h2 id="visit-title" class="text-title" data-r>Plan your visit</h2>
        <OpenNow class="mt-6 text-lead" data-r />
        <div class="mt-10 aspect-square max-w-md overflow-hidden leaf-frame" data-r>
          <img :src="img('shop-dog-pansies')" alt="A French bulldog sitting among trays of pansies in the garden centre." loading="lazy" class="h-full w-full object-cover" />
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <PlantLabel title="Visiting the garden centre" :rows="visitRows" />
      </div>
    </div>
  </section>

  <FaqList :items="faqs" id="gc-faq" title="Before you visit" />
</template>
