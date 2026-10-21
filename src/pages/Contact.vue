<script setup>
import ContactForm from '../components/ContactForm.vue'
import OpenNow from '../components/OpenNow.vue'
import { site, img } from '../lib/site.js'

const mapSrc = 'https://www.google.com/maps?q=Sunderland+Home+Grown,+Thompson+Park,+Southwick,+Sunderland+SR5+1SF&output=embed'
// Photos of the way in help first-time visitors, especially anyone anxious about somewhere new.
const arrive = [
  ['garden-centre-yard', 'The garden centre yard, with plants on benches and the shop building behind.', 'The garden centre yard. Start here.'],
  ['shop-doorway', 'The open door of the Home Grown shop, with shelves of pots inside.', 'The shop, where you can ask for anyone.'],
  ['polytunnel-benches', 'Inside a polytunnel: long benches of young plants.', 'The polytunnels, where most of the growing happens.'],
  ['onion-beds', 'Raised vegetable beds full of onions, beside a path.', 'The veg beds, home of the Monday group.'],
]
const gettingHere = [
  ['Address', 'Thompson Park, Southwick, Sunderland SR5 1SF. <span class="confirm">[CONFIRM: which park entrance, and where we are in the park]</span>'],
  ['By car', 'Car park <span class="confirm">[CONFIRM: location, spaces, blue badge bays]</span>'],
  ['By bus', '<span class="confirm">[CONFIRM: bus routes and nearest stop]</span>'],
  ['By Metro', '<span class="confirm">[CONFIRM: nearest Metro station and walking time]</span>'],
  ['Access', 'Tarmacked paths for wheelchair users. <span class="confirm">[CONFIRM: paths complete, accessible toilet]</span>'],
]
</script>

<template>
  <section class="pb-16 pt-10 lg:pb-24 lg:pt-16" aria-labelledby="page-title">
    <div class="wrap grid gap-14 lg:grid-cols-12">
      <div class="lg:col-span-5" v-reveal>
        <h1 id="page-title" class="text-display" data-r>Contact and find us</h1>
        <p class="mt-6 max-w-[36ch] text-lead text-soft" data-r>Call, email or send a message. We reply within <span class="confirm">[CONFIRM: 2 working days]</span>.</p>

        <div class="mt-10 space-y-6" data-r>
          <a :href="site.phoneHref" class="btn btn-forest text-lead">Call {{ site.phone }}</a>
          <div>
            <h2 class="text-base font-bold text-forest">Email</h2>
            <p class="mt-1 break-words"><a :href="`mailto:${site.emails[0]}`" class="link link-block">{{ site.emails[0] }}</a></p>
            <p class="mt-1 break-words"><a :href="`mailto:${site.emails[1]}`" class="link link-block">{{ site.emails[1] }}</a></p>
          </div>
          <div class="rounded-leaf bg-stone p-6">
            <h2 class="text-base font-bold text-forest">Opening times</h2>
            <dl class="mt-3 space-y-1">
              <div v-for="h in site.hours" :key="h.days" class="flex flex-wrap gap-x-3"><dt class="font-bold">{{ h.days }}</dt><dd>{{ h.time }}</dd></div>
            </dl>
            <OpenNow class="mt-4" />
          </div>
        </div>
      </div>
      <div class="rounded-leaf-lg bg-white p-6 sm:p-10 lg:col-span-6 lg:col-start-7">
        <h2 class="text-lead font-bold">Send us a message</h2>
        <ContactForm class="mt-8" />
      </div>
    </div>
  </section>

  <section class="section pt-8" aria-labelledby="arrive-title">
    <div class="wrap">
      <div class="grid gap-6 lg:grid-cols-12" v-reveal>
        <h2 id="arrive-title" class="text-title lg:col-span-5" data-r>What you'll see when you arrive</h2>
        <p class="max-w-[46ch] text-lead text-soft lg:col-span-6 lg:col-start-7" data-r>Coming for the first time? These photos show the way in. <span class="confirm">[CONFIRM: add a photo of the park entrance]</span></p>
      </div>
      <ul class="mt-12 grid grid-cols-2 gap-x-3 gap-y-8 lg:grid-cols-4" v-reveal>
        <li v-for="([im, alt, cap], i) in arrive" :key="im" data-r>
          <Pic :name="im + '-sm'" :alt="alt" class="aspect-[4/5] w-full object-cover" :class="i % 2 ? 'leaf-frame-r' : 'leaf-frame-soft'" />
          <p class="mt-4 text-lead font-bold text-forest">{{ cap }}</p>
        </li>
      </ul>
    </div>
  </section>

  <section id="getting-here" class="section scroll-mt-24 bg-leaf-pale" aria-labelledby="here-title">
    <div class="wrap grid gap-14 lg:grid-cols-12">
      <div class="lg:col-span-5">
        <h2 id="here-title" class="text-title">Getting here</h2>
        <dl class="mt-10 space-y-2" v-reveal>
          <div v-for="[k, v] in gettingHere" :key="k" class="grid gap-1 rounded-leaf bg-ground p-5 sm:grid-cols-[7rem_1fr] sm:gap-5" data-r>
            <dt class="font-bold text-forest">{{ k }}</dt><dd v-html="v"></dd>
          </div>
        </dl>
        <p class="mt-8"><a href="https://www.google.com/maps/dir/?api=1&destination=Thompson+Park+Southwick+Sunderland+SR5+1SF" class="btn btn-forest" rel="noopener">Directions in Google Maps</a></p>
      </div>
      <div class="lg:col-span-7">
        <div class="leaf-frame-soft aspect-[4/3] overflow-hidden bg-stone">
          <iframe :src="mapSrc" title="Map showing Sunderland Home Grown in Thompson Park, Southwick" class="h-full w-full border-0" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <p class="mt-3 text-sm text-soft">The pin is placed by postcode. <span class="confirm">[CONFIRM: exact pin location]</span></p>
      </div>
    </div>
  </section>
</template>
