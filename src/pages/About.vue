<script setup>
import PageHero from '../components/PageHero.vue'
import { img, supporters, url } from '../lib/site.js'

const team = [
  { name: 'Gary Hillery', role: 'Manager and Director', note: '[CONFIRM: one line and photo permission]' },
  { name: '[CONFIRM: name]', role: '[CONFIRM: role, e.g. Horticultural trainer]', note: '' },
  { name: '[CONFIRM: name]', role: '[CONFIRM: role, e.g. Health mentor]', note: '' },
  { name: '[CONFIRM: name]', role: '[CONFIRM: role, e.g. Garden centre lead]', note: '' },
]
const gallery = [
  ['site-clearing-2016', 'The start: clearing the old council maintenance yard.'],
  ['polytunnel-benches', 'Inside a polytunnel, benches full of young plants.'],
  ['beekeepers-hive', 'Beekeepers inspecting the hive.'],
  ['hanging-baskets', 'Hanging baskets ready for sale.'],
  ['bird-box-joinery', 'A finished bird box from the joinery workshop.'],
  ['squash-polytunnel', 'Squash plants taking over the polytunnel.'],
]
const isConfirm = (s) => s.startsWith('[CONFIRM')
</script>

<template>
  <PageHero
    title="About us"
    lead="Sunderland Home Grown is a community interest company. Since 2017 we have turned a former council maintenance yard into a nursery, garden centre and training site."
    :image="img('staff-with-hanging-baskets')"
    alt="Two members of the Home Grown team holding up full hanging baskets in the nursery."
  >
    <template #actions><a href="#story" class="btn btn-primary">Read our story</a></template>
  </PageHero>

  <section id="story" class="section scroll-mt-24 pt-8" aria-labelledby="story-title">
    <div class="wrap grid gap-14 lg:grid-cols-12">
      <div class="lg:col-span-5" v-reveal>
        <h2 id="story-title" class="text-title" data-r>From bare ground to growing</h2>
        <div class="mt-8 space-y-5" data-r>
          <p>In 2017 we took on a former council maintenance site in Thompson Park, Southwick. It was rubble and bare earth.</p>
          <p>Support from Power to Change transformed the site. Today it holds polytunnels, raised beds, a garden centre and a training base.</p>
          <p>Our plants now grow at Durham Cathedral, Lumley Castle, Palace Green and Sherburn Village. More importantly, so do the people who raise them.</p>
        </div>
      </div>
      <div class="grid grid-cols-2 gap-3 lg:col-span-6 lg:col-start-7">
        <figure class="col-span-2">
          <img :src="img('site-clearing-2016')" alt="A digger clearing a large heap of soil on bare ground, the site before work began." loading="lazy" class="leaf-frame-soft aspect-[16/9] w-full object-cover" />
          <figcaption class="mt-3 text-sm text-soft">Where it started: clearing the site.</figcaption>
        </figure>
        <figure class="col-span-2">
          <img :src="img('garden-centre-yard')" alt="The garden centre today, full of shrubs and flowering plants, with the shop building behind." loading="lazy" class="leaf-frame-r aspect-[16/9] w-full object-cover" />
          <figcaption class="mt-3 text-sm text-soft">The same ground today. <span class="confirm">[CONFIRM: photo date]</span></figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="section bg-forest text-white on-dark" aria-labelledby="mission-title">
    <div class="wrap grid gap-10 lg:grid-cols-12" v-reveal>
      <h2 id="mission-title" class="text-title text-white lg:col-span-4" data-r>What we do</h2>
      <ul class="grid gap-3 sm:grid-cols-3 lg:col-span-8" data-r>
        <li class="rounded-leaf-lg bg-leaf p-7 text-forest"><p class="text-lead font-bold">A garden centre and plant nursery</p><p class="mt-3 text-ink">Retail and wholesale bedding, hanging baskets and perennials.</p></li>
        <li class="rounded-leaf-lg bg-gold p-7 text-forest"><p class="text-lead font-bold">Therapeutic horticulture</p><p class="mt-3 text-ink">Training and work for young people and adults with learning disabilities and mental health challenges.</p></li>
        <li class="rounded-leaf-lg bg-berry p-7"><p class="text-lead font-bold text-white">A community hub</p><p class="mt-3">Interest groups, workshops and community gardening.</p></li>
      </ul>
    </div>
  </section>

  <section id="team" class="section scroll-mt-24" aria-labelledby="team-title">
    <div class="wrap">
      <div class="grid gap-6 lg:grid-cols-12" v-reveal>
        <h2 id="team-title" class="text-title lg:col-span-5" data-r>The team</h2>
        <p class="max-w-[46ch] text-lead text-soft lg:col-span-6 lg:col-start-7" data-r>Friendly faces help families feel at ease. If staff would rather not be photographed, role cards work just as well.</p>
      </div>
      <ul class="mt-14 grid grid-cols-2 gap-x-3 gap-y-10 lg:grid-cols-4" v-reveal>
        <li v-for="(t, i) in team" :key="i" data-r>
          <div class="leaf-frame flex aspect-square items-center justify-center" :class="['bg-leaf', 'bg-gold', 'bg-berry', 'bg-leaf-pale'][i]">
            <span class="sr-only">Photo to come</span>
          </div>
          <h3 class="mt-4 text-lead font-bold"><span :class="isConfirm(t.name) && 'confirm'">{{ t.name }}</span></h3>
          <p class="mt-1"><span :class="isConfirm(t.role) && 'confirm'">{{ t.role }}</span></p>
          <p v-if="t.note" class="mt-1 text-sm"><span class="confirm">{{ t.note }}</span></p>
        </li>
      </ul>
    </div>
  </section>

  <section class="section bg-leaf-pale" aria-labelledby="facilities-title">
    <div class="wrap grid items-center gap-14 lg:grid-cols-12">
      <div class="lg:col-span-5" v-reveal>
        <h2 id="facilities-title" class="text-title" data-r>Our site</h2>
        <p class="mt-6 text-lead text-soft" data-r>A Youth Investment Fund grant of over £468,000 is funding new facilities and training for young people. <span class="confirm">[CONFIRM: which works are complete; update to present tense]</span></p>
        <ul class="mt-8 space-y-3" data-r>
          <li v-for="f in ['Community workshop', 'Commercial glasshouse', 'Classroom and training centre', 'Tarmacked paths for wheelchair access', 'Off-grid garden centre with solar power and rainwater harvesting', 'Polytunnel']" :key="f" class="flex gap-3"><span class="leaf-bullet mt-2"></span>{{ f }}</li>
        </ul>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <img :src="img('polytunnel-benches')" alt="A long polytunnel with metal staging full of young plants." loading="lazy" class="leaf-frame-soft aspect-[4/3] w-full object-cover" />
      </div>
    </div>
  </section>

  <section id="gallery" class="section scroll-mt-24" aria-labelledby="gallery-title">
    <div class="wrap">
      <h2 id="gallery-title" class="text-title">Gallery</h2>
      <ul class="mt-12 grid grid-cols-2 gap-x-3 gap-y-8 lg:grid-cols-3">
        <li v-for="([im, cap], i) in gallery" :key="im">
          <figure>
            <img :src="img(im + '-sm')" alt="" loading="lazy" class="aspect-square w-full object-cover" :class="i % 2 ? 'leaf-frame-r' : 'leaf-frame'" />
            <figcaption class="mt-3 text-sm text-soft">{{ cap }}</figcaption>
          </figure>
        </li>
      </ul>
    </div>
  </section>

  <section id="supporters" class="section scroll-mt-24 bg-stone" aria-labelledby="sup-title">
    <div class="wrap grid gap-10 lg:grid-cols-12">
      <div class="lg:col-span-4">
        <h2 id="sup-title" class="text-title">Our supporters and partners</h2>
        <p class="mt-6 text-soft">Thank you to everyone who has helped us grow. <span class="confirm">[CONFIRM: current list; remove ended programmes such as CLLD]</span></p>
      </div>
      <ul class="grid grid-cols-2 gap-2 sm:grid-cols-3 lg:col-span-8">
        <li class="col-span-2 flex min-h-[8rem] items-center justify-center rounded-leaf bg-white p-6 sm:col-span-1">
          <img :src="img('logo-national-lottery-sm')" alt="The National Lottery Community Fund" class="max-h-16 w-auto" loading="lazy" />
        </li>
        <li class="flex min-h-[8rem] items-center justify-center rounded-leaf bg-white p-6">
          <img :src="img('logo-youth-investment-fund-sm')" alt="Youth Investment Fund" class="max-h-16 w-auto" loading="lazy" />
        </li>
        <li v-for="s in supporters.filter((s) => !s.includes('Lottery') && !s.includes('Youth'))" :key="s" class="flex min-h-[8rem] items-end rounded-leaf bg-white p-5 text-lead font-bold text-forest">{{ s }}</li>
      </ul>
    </div>
  </section>

  <section class="section" aria-labelledby="about-cta">
    <div class="wrap flex flex-col gap-8 lg:flex-row lg:items-end lg:justify-between" v-reveal>
      <h2 id="about-cta" class="text-title" data-r>Come and see us</h2>
      <div class="flex flex-wrap gap-3" data-r>
        <a :href="url('contact.html')" class="btn btn-primary">Contact and find us</a>
        <a :href="url('day-opportunities.html')" class="btn btn-quiet">Day opportunities</a>
      </div>
    </div>
  </section>
</template>
