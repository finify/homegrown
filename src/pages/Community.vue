<script setup>
import PageHero from '../components/PageHero.vue'
import PlantLabel from '../components/PlantLabel.vue'
import NewsletterForm from '../components/NewsletterForm.vue'
import { img, url } from '../lib/site.js'

const fvRows = [
  ['When', 'Every Monday, 10am to 12 noon'],
  ['Where', 'Home Grown, Thompson Park, SR5 1SF'],
  ['Cost', '<span class="confirm">[CONFIRM: free or a small charge?]</span>'],
  ['Who', 'Anyone who wants to grow food. No experience needed. <span class="confirm">[CONFIRM: age limits]</span>'],
  ['Bring', 'Stout footwear and gloves'],
]
const learn = ['Propagation: growing new plants from seed and cuttings', 'Succession planting, for a harvest all season', 'Pest control without harsh chemicals', 'Feeding and watering', 'Pruning']
const interest = [
  ['Fruit and veg growing', 'Every Monday morning.', 'onion-beds'],
  ['Community gardening', 'Planting and caring for green spaces around the city.', 'garden-centre-yard'],
  ['Beekeeping', 'Learn how to look after a hive.', 'beekeepers-hive'],
  ['Local history and heritage', 'Meets twice a month at the Park Café.', 'site-clearing-2016'],
  ['Health and wellbeing', 'Fresh air, gentle activity and good company.', 'salvia-and-bee'],
  ['Healthy eating', 'From growing food to cooking it.', 'veg-harvest'],
]
const places = [
  ['Southwick', 'Thompson Park, with Friends of Thompson Park'],
  ['Fulwell', 'Sea Road'],
  ['City centre', 'Bamford Street'],
]
const hire = [
  ['Garden maintenance and planting schemes', 'For businesses, schools and councils.'],
  ['Bedding and floral displays', 'Designed, grown and planted by our team.'],
  ['Workshop and space hire', 'Our classroom and workshop for your group.'],
  ['Team volunteering days', 'Bring your colleagues to help out for a day.'],
]
</script>

<template>
  <PageHero
    title="Community"
    lead="Groups to join, places we look after, and ways to get involved, whether you have an hour a week or a whole team for a day."
    :image="img('veg-harvest')"
    alt="Crates of freshly picked squash, peppers and greens on the path between raised vegetable beds."
  >
    <template #actions>
      <a href="#fruit-veg" class="btn btn-primary">Join the fruit and veg group</a>
      <a href="#hire" class="btn btn-quiet">Hire us</a>
    </template>
  </PageHero>

  <!-- Fruit & veg -->
  <section id="fruit-veg" class="section scroll-mt-24 bg-leaf-pale" aria-labelledby="fv-title">
    <div class="wrap grid gap-14 lg:grid-cols-12">
      <div class="lg:col-span-6" v-reveal>
        <h2 id="fv-title" class="text-title" data-r>Weekly fruit and vegetables group</h2>
        <p class="mt-6 text-lead text-soft" data-r>Learn to grow your own food alongside our team. The produce is shared with volunteers and some is donated to Sunderland Soup Kitchen.</p>
        <h3 class="mt-10 text-lead font-bold" data-r>What you'll learn</h3>
        <ul class="mt-4 space-y-3" data-r>
          <li v-for="l in learn" :key="l" class="flex gap-3"><span class="leaf-bullet mt-2"></span>{{ l }}</li>
        </ul>
        <div class="mt-10 grid grid-cols-2 gap-3" data-r>
          <img :src="img('onion-beds-sm')" alt="Rows of onions growing in a raised bed." loading="lazy" class="leaf-frame aspect-square w-full object-cover" />
          <img :src="img('squash-polytunnel-sm')" alt="Large squash plants growing in the polytunnel." loading="lazy" class="leaf-frame-r aspect-square w-full object-cover" />
        </div>
      </div>
      <div class="lg:col-span-5 lg:col-start-8">
        <PlantLabel title="Fruit and veg group" :rows="fvRows" tone="gold" />
        <div class="mt-8 flex flex-wrap gap-3">
          <a :href="url('contact.html') + '?type=volunteer'" class="btn btn-forest">Join the group</a>
          <a href="tel:+441915499444" class="btn btn-white">Call to ask</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Interest groups -->
  <section id="groups" class="section scroll-mt-24" aria-labelledby="groups-title">
    <div class="wrap">
      <h2 id="groups-title" class="text-title" v-reveal><span data-r class="block">Interest groups</span></h2>
      <ul class="mt-14 grid gap-x-16 gap-y-10 md:grid-cols-2" v-reveal>
        <li v-for="[t, b, im] in interest" :key="t" class="grid grid-cols-[5rem_1fr] items-center gap-6" data-r>
          <img :src="img(im + '-sm')" alt="" loading="lazy" class="leaf-frame h-20 w-20 object-cover" />
          <div><h3 class="text-lead font-bold">{{ t }}</h3><p class="mt-1 text-soft">{{ b }}</p></div>
        </li>
      </ul>
    </div>
  </section>

  <!-- Where we work -->
  <section class="section bg-gold" aria-labelledby="where-title">
    <div class="wrap grid gap-12 lg:grid-cols-12">
      <div class="lg:col-span-5" v-reveal>
        <h2 id="where-title" class="text-title" data-r>Where we garden</h2>
        <p class="mt-6 text-lead" data-r>We work with Friends of Thompson Park and Sunderland City Council to look after green spaces across the city.</p>
      </div>
      <ol class="grid gap-2 sm:grid-cols-3 lg:col-span-7" v-reveal>
        <li v-for="[p, d] in places" :key="p" class="flex min-h-[11rem] flex-col justify-between rounded-leaf-lg bg-gold-pale p-6" data-r>
          <span class="text-lead font-bold text-forest">{{ p }}</span><span>{{ d }}</span>
        </li>
      </ol>
    </div>
  </section>

  <!-- Volunteering -->
  <section id="volunteer" class="section scroll-mt-24" aria-labelledby="vol-title">
    <div class="wrap grid items-center gap-14 lg:grid-cols-12">
      <div class="aspect-[4/3] overflow-hidden leaf-frame-soft lg:col-span-6">
        <img :src="img('polytunnel-benches')" alt="Long rows of staging in a polytunnel, filled with young plants." loading="lazy" class="h-full w-full object-cover" v-parallax="0.1" />
      </div>
      <div class="lg:col-span-5 lg:col-start-8" v-reveal>
        <h2 id="vol-title" class="text-title" data-r>Volunteer with us</h2>
        <p class="mt-6 text-lead text-soft" data-r>Help in the nursery, the veg beds or the garden centre. Volunteers share in the harvest. <span class="confirm">[CONFIRM: roles, times, any checks needed]</span></p>
        <a :href="url('contact.html') + '?type=volunteer'" class="btn btn-forest mt-8" data-r>Ask about volunteering</a>
      </div>
    </div>
  </section>

  <!-- Hire us -->
  <section id="hire" class="section scroll-mt-24 bg-forest text-white on-dark" aria-labelledby="hire-title">
    <div class="wrap">
      <div class="grid gap-6 lg:grid-cols-12" v-reveal>
        <h2 id="hire-title" class="text-title text-white lg:col-span-5" data-r>Hire us</h2>
        <p class="max-w-[46ch] text-lead text-leaf-pale lg:col-span-6 lg:col-start-7" data-r>Our team can plant, maintain and grow for you. Every job supports our training programme. <span class="confirm">[CONFIRM: which services are offered]</span></p>
      </div>
      <ul class="mt-14 grid gap-3 sm:grid-cols-2" v-reveal>
        <li v-for="([t, b], i) in hire" :key="t" class="rounded-leaf-lg p-7" :class="i === 0 ? 'bg-gold text-ink' : 'bg-forest-700'" data-r>
          <h3 class="text-lead font-bold" :class="i === 0 ? 'text-forest' : 'text-white'">{{ t }}</h3>
          <p class="mt-2" :class="i === 0 ? '' : 'text-leaf-pale'">{{ b }}</p>
        </li>
      </ul>
      <a :href="url('contact.html') + '?type=hire'" class="btn btn-primary mt-12" v-reveal><span data-r>Send a hire enquiry</span></a>
    </div>
  </section>

  <!-- Membership -->
  <section id="membership" class="section scroll-mt-24" aria-labelledby="member-title">
    <div class="wrap grid gap-14 lg:grid-cols-12">
      <div class="lg:col-span-5" v-reveal>
        <h2 id="member-title" class="text-title" data-r>Free membership</h2>
        <p class="mt-6 text-lead text-soft" data-r>Join for free and get our newsletter, member discounts, and first news of events and workshops.</p>
      </div>
      <div class="rounded-leaf-lg bg-stone p-6 sm:p-10 lg:col-span-6 lg:col-start-7">
        <NewsletterForm />
      </div>
    </div>
  </section>
</template>
