<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import HeroLeaves from '../components/HeroLeaves.vue'
import Crossfade from '../components/Crossfade.vue'
import OpenNow from '../components/OpenNow.vue'
import GrowJourney from '../components/GrowJourney.vue'
import EventList from '../components/EventList.vue'
import { img, url, site } from '../lib/site.js'
import { gsap, reduceMotion } from '../lib/reveal.js'

const heroImages = [
  { src: img('polytunnel-group-potting'), alt: 'A group potting up bedding plants together on a long bench in the polytunnel.' },
  { src: img('staff-with-hanging-baskets'), alt: 'Two members of the team holding up hanging baskets full of flowers in the nursery.' },
  { src: img('hanging-baskets'), alt: 'Hanging baskets of red and purple petunias for sale in the garden centre.' },
]

const day = [
  { title: 'Potting and propagating', body: 'Sowing seeds, taking cuttings and potting on in the nursery and polytunnels.', image: 'plug-plant-roots', alt: 'A young plant lifted out of its tray, showing a healthy ball of roots.' },
  { title: 'Growing food', body: 'Raised beds of onions, squash and greens. The harvest is shared and some goes to Sunderland Soup Kitchen.', image: 'veg-harvest', alt: 'Crates of freshly harvested squash, peppers and greens laid out on the path between raised beds.' },
  { title: 'Working in the shop', body: 'Real retail work experience in the garden centre: watering, displays, helping customers.', image: 'shop-doorway', alt: 'The open doorway of the Home Grown shop with pots and gifts on wooden shelves and a dog lying inside.' },
  { title: 'Learning together', body: 'Workshops, joinery and beekeeping with a horticultural trainer and health mentors alongside.', image: 'group-planting-workshop', alt: 'Four people smiling as they plant up pots at a bench in the workshop.' },
  { title: 'Looking after the bees', body: 'Suited up, checking the hives and learning how a colony works.', image: 'beekeepers-hive', alt: 'Two people in beekeeping suits inspecting a frame of honeycomb covered in bees.' },
]

const proof = [
  { name: 'Durham Cathedral', note: 'Plants supplied' },
  { name: 'Palace Green', note: 'World Heritage Site, Durham' },
  { name: 'Lumley Castle', note: 'Plants supplied' },
  { name: 'Sherburn Village', note: 'Britain in Bloom Gold' },
]

const groups = [
  { name: 'Fruit and veg growing', when: 'Mondays, 10am to 12 noon', img: 'onion-beds' },
  { name: 'Community gardening', when: 'Southwick, Fulwell and the city centre', img: 'komatsu-floral-display' },
  { name: 'Beekeeping', when: 'Learn to keep bees on site', img: 'beekeepers-hive' },
  { name: 'Local history and heritage', when: 'Twice a month at the Park Café', img: 'site-clearing-2016' },
  { name: 'Health and wellbeing', when: 'Time outdoors, at your own pace', img: 'salvia-and-bee' },
  { name: 'Healthy eating', when: 'Grow it, cook it, share it', img: 'squash-polytunnel' },
]

// Horizontal scroll through "a day here" on large screens; native swipe on phones.
const track = ref(null)
const daySection = ref(null)
let mm
onMounted(() => {
  if (reduceMotion()) return
  mm = gsap.matchMedia()
  mm.add('(min-width: 1024px)', () => {
    const el = track.value
    const distance = () => el.scrollWidth - el.clientWidth
    gsap.to(el, {
      x: () => -distance(),
      ease: 'none',
      scrollTrigger: { trigger: daySection.value, start: 'top top', end: () => `+=${distance()}`, scrub: 0.8, pin: true, invalidateOnRefresh: true },
    })
  })
})
onBeforeUnmount(() => mm?.revert())
</script>

<template>
  <!-- Hero -->
  <section id="hero" class="relative overflow-hidden pb-16 lg:pb-24" aria-labelledby="hero-title">
    <div class="wrap grid gap-10 pt-6 lg:min-h-[calc(100svh-6rem)] lg:grid-cols-12 lg:items-center lg:gap-6 lg:pt-0">
      <div class="relative z-10 lg:col-span-6" v-reveal>
        <h1 id="hero-title" class="text-[clamp(2.6rem,4.9vw,4.75rem)] font-bold leading-[1] tracking-[-0.035em]" data-r>Growing skills and community</h1>
        <p class="mt-6 max-w-[34ch] text-lead text-soft" data-r>
          Confidence, training and real work for young people and adults, at our garden centre and nursery in Thompson Park, Sunderland.
        </p>
        <div class="mt-9 flex flex-wrap gap-3" data-r>
          <a :href="url('day-opportunities.html')" class="btn btn-primary">Day opportunities</a>
          <a :href="url('garden-centre.html')" class="btn btn-quiet">Visit the garden centre</a>
        </div>
        <OpenNow class="mt-8" data-r />
      </div>

      <div class="relative lg:col-span-6 lg:col-start-7">
        <div class="relative ml-auto aspect-[4/5] w-[88%] sm:aspect-[5/4] lg:aspect-[7/8] lg:max-h-[calc(100svh-8rem)] lg:w-full">
          <Crossfade :images="heroImages" frame="leaf-frame-soft" eager />
        </div>
        <HeroLeaves trigger="#hero" class="pointer-events-none absolute -bottom-12 -left-6 aspect-square w-[60%] sm:-left-10 lg:bottom-[-2%] lg:-left-[22%] lg:w-[58%]" />
      </div>
    </div>
  </section>

  <!-- Statement with inline photographs -->
  <section class="bg-ground py-24 lg:py-36" aria-label="What we do">
    <div class="wrap" v-reveal>
      <p class="max-w-[30ch] text-[1.5rem] font-bold leading-[1.3] text-forest sm:text-[2rem] lg:text-[2.25rem]" data-r>
        We grow plants
        <img :src="img('lobelia-close-up-sm')" alt="" class="leaf-frame mx-1 inline-block h-[0.95em] w-[1.3em] object-cover align-[-0.1em]" />
        and people
        <img :src="img('participant-smiling-sm')" alt="" class="leaf-frame mx-1 inline-block h-[0.95em] w-[1.3em] object-cover align-[-0.1em]" />
        on a former council yard in Thompson Park.
      </p>
    </div>
  </section>

  <!-- Who it is for -->
  <section class="section pt-0" aria-labelledby="who-title">
    <div class="wrap grid gap-10 lg:grid-cols-12">
      <div class="lg:col-span-3" v-reveal>
        <h2 id="who-title" class="text-title" data-r>Who are you here for?</h2>
        <p class="mt-5 max-w-[30ch] text-soft" data-r>Choose the route that fits. Each one has the details you need and a way to get in touch.</p>
      </div>
      <ul class="grid gap-3 sm:grid-cols-2 sm:grid-rows-2 lg:col-span-9" v-reveal>
        <li class="sm:row-span-2" data-r>
          <a :href="url('day-opportunities.html') + '#for-you'" class="group flex h-full flex-col rounded-leaf-lg bg-leaf p-3 no-underline">
            <span class="leaf-frame-soft block aspect-[4/5] overflow-hidden sm:aspect-auto sm:flex-1">
              <img :src="img('participant-smiling')" alt="" loading="lazy" class="h-full min-h-[18rem] w-full object-cover transition-transform duration-700 group-hover:scale-[1.04]" />
            </span>
            <span class="block px-3 pb-3 pt-6">
              <span class="block text-lead font-bold text-forest group-hover:underline">For individuals and families</span>
              <span class="mt-2 block text-ink">Supported days of gardening, training and work experience. See what a day is like.</span>
            </span>
          </a>
        </li>
        <li data-r>
          <a :href="url('day-opportunities.html') + '#professionals'" class="group grid h-full grid-cols-[1fr_7rem] items-end gap-4 rounded-leaf-lg bg-gold p-6 no-underline sm:grid-cols-[1fr_8rem]">
            <span>
              <span class="block text-lead font-bold text-forest group-hover:underline">For professionals and referrers</span>
              <span class="mt-2 block text-ink">Who it suits, funding routes, and how to make a referral.</span>
            </span>
            <span class="leaf-frame block aspect-square"><img :src="img('gardener-portrait')" alt="" loading="lazy" class="h-full w-full object-cover" /></span>
          </a>
        </li>
        <li data-r>
          <a :href="url('garden-centre.html')" class="group grid h-full grid-cols-[1fr_7rem] items-end gap-4 rounded-leaf-lg bg-berry p-6 text-white no-underline on-dark sm:grid-cols-[1fr_8rem]">
            <span>
              <span class="block text-lead font-bold group-hover:underline">For gardeners and visitors</span>
              <span class="mt-2 block text-white">Bedding, baskets and perennials, grown here. Open seven days.</span>
            </span>
            <span class="leaf-frame block aspect-square"><img :src="img('primroses-sm')" alt="" loading="lazy" class="h-full w-full object-cover" /></span>
          </a>
        </li>
      </ul>
    </div>
  </section>

  <!-- A day here: pinned horizontal scroll on desktop -->
  <section ref="daySection" class="overflow-hidden bg-forest py-24 text-white on-dark lg:flex lg:h-[100svh] lg:flex-col lg:justify-center lg:py-0" aria-labelledby="day-title">
    <div class="wrap">
      <div class="grid gap-6 lg:grid-cols-12" v-reveal>
        <h2 id="day-title" class="text-title text-white lg:col-span-5" data-r>What a day here looks like</h2>
        <p class="max-w-[46ch] text-lead text-leaf-pale lg:col-span-6 lg:col-start-7" data-r>Real work with real plants, alongside staff who know you. Every day is a little different, depending on the season.</p>
      </div>
    </div>
    <p class="wrap mt-10 text-leaf-pale lg:hidden" aria-hidden="true">Swipe to see more</p>
    <div class="mt-6 lg:mt-16">
      <ul ref="track" class="flex snap-x snap-mandatory gap-5 overflow-x-auto px-4 pb-4 sm:px-6 lg:snap-none lg:overflow-visible lg:px-10 lg:pb-0" tabindex="0" aria-label="A day at Home Grown, scroll sideways">
        <li v-for="(d, i) in day" :key="d.title" class="w-[80vw] shrink-0 snap-start sm:w-[46vw] lg:w-[30vw]">
          <div class="aspect-[4/3] overflow-hidden bg-forest-700" :class="i % 2 ? 'leaf-frame-r' : 'leaf-frame-soft'">
            <img :src="img(d.image)" :alt="d.alt" loading="lazy" width="1600" height="1200" class="h-full w-full object-cover" />
          </div>
          <h3 class="mt-6 text-lead font-bold text-white">{{ d.title }}</h3>
          <p class="mt-2 max-w-[36ch] text-leaf-pale">{{ d.body }}</p>
        </li>
        <li class="flex w-[80vw] shrink-0 snap-start flex-col justify-center sm:w-[46vw] lg:w-[26vw]">
          <p class="text-lead font-bold text-white">Want to see it for yourself?</p>
          <a :href="url('day-opportunities.html')" class="btn btn-primary mt-6 self-start">Read about day opportunities</a>
        </li>
      </ul>
    </div>
  </section>

  <!-- Proof -->
  <section class="section" aria-labelledby="proof-title">
    <div class="wrap">
      <ul class="grid grid-cols-2 gap-2 lg:grid-cols-4" v-reveal>
        <li class="col-span-2 flex min-h-[12rem] flex-col justify-between rounded-leaf-lg bg-gold p-6 sm:p-8 lg:row-span-2 lg:min-h-0" data-r>
          <h2 id="proof-title" class="text-title">Our plants grow at</h2>
          <p class="mt-6 max-w-[34ch] text-ink">Bedding and displays raised in our polytunnels by our trainees and team, supplied to some of the North East's best-loved places.</p>
        </li>
        <li v-for="p in proof" :key="p.name" class="flex min-h-[9rem] flex-col justify-between rounded-leaf-lg bg-stone p-5 sm:min-h-[11rem] sm:p-7" data-r>
          <p class="text-lead font-bold text-forest">{{ p.name }}</p>
          <p class="mt-3 text-sm text-soft">{{ p.note }}</p>
        </li>
      </ul>
    </div>
  </section>

  <GrowJourney />

  <!-- Garden centre teaser on a gold field -->
  <section class="section bg-gold" aria-labelledby="gc-title">
    <div class="wrap grid items-center gap-12 lg:grid-cols-12">
      <div class="relative lg:col-span-6">
        <div class="leaf-frame-soft aspect-[5/4] overflow-hidden bg-gold-pale">
          <img :src="img('garden-centre-perennials')" alt="Benches of flowering perennials and bedding in the outdoor garden centre, with polytunnels behind." loading="lazy" width="1600" height="865" class="h-full w-full object-cover" v-parallax="0.12" />
        </div>
      </div>
      <div class="lg:col-span-5 lg:col-start-8" v-reveal>
        <h2 id="gc-title" class="text-title" data-r>The garden centre</h2>
        <p class="mt-6 text-lead text-ink" data-r>Bedding, hanging baskets and perennials, most of it grown a few metres from the till.</p>
        <div class="mt-8 rounded-leaf bg-gold-pale p-6" data-r>
          <OpenNow />
          <dl class="mt-4 space-y-1">
            <div v-for="h in site.hours" :key="h.days" class="flex flex-wrap gap-x-3"><dt class="font-bold text-forest">{{ h.days }}</dt><dd>{{ h.time }}</dd></div>
          </dl>
        </div>
        <p class="mt-6" data-r>In season now: <span class="confirm">[CONFIRM: autumn stock, for example pansies, violas and spring bulbs]</span></p>
        <div class="mt-8 flex flex-wrap gap-3" data-r>
          <a :href="url('garden-centre.html')" class="btn btn-forest">Plan your visit</a>
          <a :href="url('contact.html') + '?type=trade'" class="btn btn-white">Trade enquiries</a>
        </div>
      </div>
    </div>
  </section>

  <!-- What's on -->
  <section class="section" aria-labelledby="whats-title">
    <div class="wrap">
      <div class="flex flex-wrap items-end justify-between gap-6" v-reveal>
        <h2 id="whats-title" class="text-title" data-r>Coming up</h2>
        <a :href="url('whats-on.html')" class="link link-block text-lead" data-r>See everything on</a>
      </div>
      <EventList :limit="4" class="mt-14" />
    </div>
  </section>

  <!-- Community groups: menu with photo bullets -->
  <section class="section bg-stone" aria-labelledby="groups-title">
    <div class="wrap">
      <div class="grid gap-6 lg:grid-cols-12" v-reveal>
        <h2 id="groups-title" class="text-title lg:col-span-5" data-r>Groups anyone can join</h2>
        <p class="max-w-[46ch] text-lead text-soft lg:col-span-6 lg:col-start-7" data-r>We work with Friends of Thompson Park and Sunderland City Council in Southwick, Fulwell and the city centre.</p>
      </div>
      <ul class="mt-16 grid gap-x-16 gap-y-9 md:grid-cols-2" v-reveal>
        <li v-for="g in groups" :key="g.name" class="grid grid-cols-[4rem_1fr] items-center gap-5" data-r>
          <img :src="img(g.img + '-sm')" alt="" loading="lazy" class="leaf-frame h-16 w-16 object-cover" />
          <div>
            <h3 class="text-lead font-bold">{{ g.name }}</h3>
            <p class="text-soft">{{ g.when }}</p>
          </div>
        </li>
      </ul>
      <p class="mt-14" v-reveal><a :href="url('community.html')" class="btn btn-forest" data-r>Find a group</a></p>
    </div>
  </section>

  <!-- Testimonial -->
  <section class="section bg-berry text-white on-dark" aria-label="What our manager says">
    <div class="wrap grid items-center gap-12 lg:grid-cols-12">
      <figure class="lg:col-span-7" v-reveal>
        <blockquote class="text-[1.5rem] font-bold leading-[1.3] sm:text-[2rem] lg:text-[2.25rem]" data-r>
          <p>Young people “always leave with a big smile on their face.”</p>
        </blockquote>
        <figcaption class="mt-8 text-lead" data-r>Gary Hillery, Manager and Director</figcaption>
        <p class="mt-3 text-sm text-berry-pale" data-r>From our Youth Investment Fund page. <span class="confirm">[CONFIRM: full quote, plus a family quote used with permission]</span></p>
      </figure>
      <div class="lg:col-span-4 lg:col-start-9">
        <div class="leaf-frame aspect-square overflow-hidden bg-berry-pale">
          <img :src="img('group-planting-workshop')" alt="Four people smiling as they plant up pots together in the workshop." loading="lazy" class="h-full w-full object-cover" />
        </div>
      </div>
    </div>
  </section>

  <!-- Referral band -->
  <section class="section" aria-labelledby="refer-title">
    <div class="wrap grid gap-10 lg:grid-cols-12 lg:items-end" v-reveal>
      <h2 id="refer-title" class="text-title lg:col-span-6" data-r>Thinking about a place for someone?</h2>
      <div class="lg:col-span-5 lg:col-start-8" data-r>
        <p class="text-lead text-soft">Register your interest online or give us a call. There's no commitment, and we'll explain everything.</p>
        <div class="mt-8 flex flex-wrap gap-3">
          <a :href="url('day-opportunities.html') + '#register'" class="btn btn-primary">Register your interest</a>
          <a :href="site.phoneHref" class="btn btn-quiet">Call {{ site.phone }}</a>
        </div>
      </div>
    </div>
  </section>
</template>
