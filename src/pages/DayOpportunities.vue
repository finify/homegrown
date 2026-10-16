<script setup>
import { ref, onMounted } from 'vue'
import PageHero from '../components/PageHero.vue'
import PlantLabel from '../components/PlantLabel.vue'
import GrowJourney from '../components/GrowJourney.vue'
import FaqList from '../components/FaqList.vue'
import ReferralForm from '../components/ReferralForm.vue'
import { img, site } from '../lib/site.js'

// Three readers, three tabs. The tab follows the URL hash so cards on the home page can deep-link.
const tabs = [
  { id: 'for-you', label: 'For you', sub: 'Easy Read' },
  { id: 'families', label: 'For families and guardians' },
  { id: 'professionals', label: 'For professionals' },
]
const active = ref('for-you')
const tabRefs = ref([])
const select = (id, focus = false) => {
  active.value = id
  history.replaceState(null, '', `#${id}`)
  if (focus) tabRefs.value[tabs.findIndex((t) => t.id === id)]?.focus()
}
const onKey = (e, i) => {
  const n = tabs.length
  const map = { ArrowRight: (i + 1) % n, ArrowLeft: (i - 1 + n) % n, Home: 0, End: n - 1 }
  if (e.key in map) { e.preventDefault(); select(tabs[map[e.key]].id, true) }
}
onMounted(() => {
  const h = location.hash.slice(1)
  if (tabs.some((t) => t.id === h)) {
    active.value = h
    requestAnimationFrame(() => document.getElementById('audiences')?.scrollIntoView())
  }
})

const easyRead = [
  { text: 'You can grow plants.', image: 'plug-plant-roots', alt: 'A small plant with its roots, held in a hand.' },
  { text: 'You can work in our shop.', image: 'shop-doorway', alt: 'The door of the Home Grown shop.' },
  { text: 'You can make friends.', image: 'group-planting-workshop', alt: 'People smiling and planting pots together.' },
  { text: 'You can learn new skills.', image: 'bird-box-joinery', alt: 'Two people holding a bird box they made.' },
  { text: 'Our staff will help you.', image: 'staff-with-hanging-baskets', alt: 'Two staff members holding flower baskets.' },
]

const dayPlan = [
  ['Arrive', 'A member of staff meets you. Tea, a chat and the plan for the day.', '[CONFIRM: start time]'],
  ['Morning', 'Work in the nursery, polytunnels or veg beds, in a small group.', ''],
  ['Lunch', 'A break together.', '[CONFIRM: bring a packed lunch or provided?]'],
  ['Afternoon', 'The shop, a workshop or a project in the park, depending on the season.', ''],
  ['Home time', 'A quick look back at the day. Staff can update families or carers.', '[CONFIRM: finish time]'],
]

const activities = [
  ['Nursery and propagation', 'Sowing, pricking out, potting on and caring for thousands of bedding plants.', 'bedding-trays'],
  ['Vegetable gardens', 'Raised beds and polytunnels of onions, squash, salad and greens.', 'onion-beds'],
  ['Landscaping', 'Planting schemes and floral displays, from the first sketch to the last plant.', 'komatsu-floral-display'],
  ['Community gardening', 'Out and about in Southwick and Fulwell, working with Friends of Thompson Park.', 'garden-centre-yard'],
  ['Retail work experience', 'Serving customers, stock and displays in our garden centre.', 'garden-centre-display'],
  ['Beekeeping', 'Suiting up to look after our hives.', 'beekeepers-hive'],
]

const proRows = [
  ['Who it is for', 'Young people and adults with learning disabilities and/or mental health challenges.'],
  ['Days and times', '<span class="confirm">[CONFIRM: session days and times]</span>'],
  ['Daily rate', '<span class="confirm">[CONFIRM: daily rate]</span>'],
  ['Funding', 'Direct payments, personal budgets, local authority commissioning. <span class="confirm">[CONFIRM: routes accepted]</span>'],
  ['Training', 'Accredited and non-accredited horticulture training, and supported work placements.'],
  ['Staffing', 'Health mentors and a horticultural trainer. <span class="confirm">[CONFIRM: ratios]</span>'],
  ['Capacity', '<span class="confirm">[CONFIRM: places available]</span>'],
  ['Response', 'We reply to referrals within <span class="confirm">[CONFIRM: 2 working days]</span>.'],
]

const faqs = [
  { q: 'Who can come?', a: '<p>Young people and adults with learning disabilities and/or mental health challenges. <span class="confirm">[CONFIRM: age range and any eligibility criteria]</span></p>' },
  { q: 'How much does it cost, and who pays?', a: '<p>There is a daily rate of <span class="confirm">[CONFIRM: rate]</span>. Places are often paid for through a personal budget, direct payments or the local authority. If you are not sure what funding you have, ask us or your social worker and we will help.</p>' },
  { q: 'Do I need a referral from a social worker?', a: '<p>No. You can contact us yourself, or a family member can. Professionals can also refer. <span class="confirm">[CONFIRM]</span></p>' },
  { q: 'Can I visit before deciding?', a: '<p>Yes. Come and look round, meet the team and try a taster session. <span class="confirm">[CONFIRM: taster session details]</span></p>' },
  { q: 'Is the site accessible?', a: '<p>We have tarmacked paths for wheelchair users. <span class="confirm">[CONFIRM: paths complete, accessible toilet, parking]</span> Tell us what you need and we will plan around it.</p>' },
  { q: 'What about transport?', a: '<p><span class="confirm">[CONFIRM: whether transport is provided or arranged]</span> We are in Thompson Park, Southwick, SR5 1SF. See <a class="link" href="contact.html#getting-here">getting here</a>.</p>' },
  { q: 'What should I wear or bring?', a: '<p>Clothes for the weather and sturdy shoes or boots. We provide gloves and tools. <span class="confirm">[CONFIRM: lunch, waterproofs]</span></p>' },
  { q: 'Can I get a qualification?', a: '<p>Yes, if you would like one. We offer accredited and non-accredited horticulture training. <span class="confirm">[CONFIRM: awarding body and levels]</span></p>' },
]
</script>

<template>
  <PageHero
    title="Day opportunities"
    lead="Supported gardening, training and work experience for young people and adults with learning disabilities or mental health challenges."
    :image="img('participant-smiling')"
    alt="A smiling woman in a Home Grown fleece in the polytunnel, holding up her fist in celebration."
    tone="gold"
  >
    <template #actions>
      <a href="#register" class="btn btn-primary">Register your interest</a>
      <a :href="site.phoneHref" class="btn btn-quiet">Call {{ site.phone }}</a>
    </template>
    <template #extra>
      <p class="text-soft">Easy Read version: choose <a href="#for-you" class="link" @click="select('for-you')">For you</a> below.</p>
    </template>
  </PageHero>

  <!-- Three readers -->
  <section id="audiences" class="scroll-mt-24 pb-24 lg:pb-40" aria-label="Information for you, your family, or professionals">
    <div class="wrap">
      <div role="tablist" aria-label="Who is reading?" class="flex flex-col gap-2 sm:flex-row">
        <button
          v-for="(t, i) in tabs"
          :id="`tab-${t.id}`"
          :key="t.id"
          :ref="(el) => (tabRefs[i] = el)"
          role="tab"
          type="button"
          :aria-selected="active === t.id ? 'true' : 'false'"
          :aria-controls="`panel-${t.id}`"
          :tabindex="active === t.id ? 0 : -1"
          class="min-h-[4rem] flex-1 rounded-leaf px-6 py-3 text-left text-lead font-bold transition-colors"
          :class="active === t.id ? 'bg-forest text-white on-dark' : 'bg-stone text-forest hover:bg-leaf-pale'"
          @click="select(t.id)"
          @keydown="onKey($event, i)"
        >
          {{ t.label }}<span v-if="t.sub" class="block text-sm font-bold" :class="active === t.id ? 'text-gold' : 'text-soft'">{{ t.sub }}</span>
        </button>
      </div>

      <!-- Easy Read -->
      <div v-show="active === 'for-you'" id="panel-for-you" role="tabpanel" aria-labelledby="tab-for-you" tabindex="0" class="mt-12">
        <h2 class="text-title">Come and grow with us</h2>
        <ul class="mt-12 grid gap-10 sm:grid-cols-2 lg:grid-cols-3">
          <li v-for="e in easyRead" :key="e.text" class="flex items-center gap-6 sm:flex-col sm:items-start">
            <img :src="img(e.image + '-sm')" :alt="e.alt" loading="lazy" class="leaf-frame-soft aspect-square w-32 shrink-0 object-cover sm:w-full sm:max-w-[16rem]" />
            <p class="text-[1.75rem] font-bold leading-tight text-forest">{{ e.text }}</p>
          </li>
          <li class="flex flex-col justify-center gap-5 rounded-leaf-lg bg-gold p-8">
            <p class="text-[1.75rem] font-bold leading-tight text-forest">Want to come?</p>
            <p class="text-lead">Ask someone to help you fill in the form. Or phone us.</p>
            <a :href="site.phoneHref" class="btn btn-forest self-start text-lead">Phone {{ site.phone }}</a>
            <a href="#register" class="link link-block text-lead">Fill in the form</a>
          </li>
        </ul>
      </div>

      <!-- Families -->
      <div v-show="active === 'families'" id="panel-families" role="tabpanel" aria-labelledby="tab-families" tabindex="0" class="mt-12">
        <div class="grid gap-14 lg:grid-cols-12">
          <div class="lg:col-span-6">
            <h2 class="text-title">A typical day</h2>
            <ol class="mt-10 space-y-2">
              <li v-for="[when, what, c] in dayPlan" :key="when" class="grid gap-1 rounded-leaf bg-stone p-5 sm:grid-cols-[8rem_1fr] sm:gap-6">
                <span class="font-bold text-forest">{{ when }}</span>
                <span>{{ what }} <span v-if="c" class="confirm">{{ c }}</span></span>
              </li>
            </ol>
          </div>
          <div class="space-y-10 lg:col-span-5 lg:col-start-8">
            <div>
              <h3 class="text-lead font-bold">Support and supervision</h3>
              <p class="mt-3">Our health mentors and horticultural trainer work alongside everyone, every day. Support is planned with you before the first day. <span class="confirm">[CONFIRM: staff ratios, training such as first aid and safeguarding, DBS checks]</span></p>
            </div>
            <div>
              <h3 class="text-lead font-bold">Safety</h3>
              <p class="mt-3">The site is fenced and staffed whenever people are here. <span class="confirm">[CONFIRM]</span> Tools are introduced step by step.</p>
            </div>
            <div>
              <h3 class="text-lead font-bold">Getting here</h3>
              <p class="mt-3">Thompson Park, Southwick, SR5 1SF. <span class="confirm">[CONFIRM: transport offered]</span></p>
            </div>
            <div>
              <h3 class="text-lead font-bold">Keeping you in the loop</h3>
              <p class="mt-3">We tell families and carers how things are going. <span class="confirm">[CONFIRM: how and how often]</span></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Professionals -->
      <div v-show="active === 'professionals'" id="panel-professionals" role="tabpanel" aria-labelledby="tab-professionals" tabindex="0" class="mt-12">
        <div class="grid gap-14 lg:grid-cols-12">
          <div class="lg:col-span-5">
            <h2 class="text-title">For social workers and care managers</h2>
            <p class="mt-6 text-lead text-soft">A structured, outdoor day service with real work, training and progression. Our Youth Investment Fund programme adds supported work placements and links with schools and colleges.</p>
            <div class="mt-8 flex flex-wrap gap-3">
              <a href="#register" class="btn btn-forest">Make a referral</a>
              <a :href="site.phoneHref" class="btn btn-quiet">Call {{ site.phone }}</a>
            </div>
            <p class="mt-8"><strong class="text-forest">Outcomes we track:</strong> <span class="confirm">[CONFIRM: e.g. skills, confidence, qualifications, progression into work or volunteering]</span></p>
          </div>
          <div class="lg:col-span-6 lg:col-start-7">
            <PlantLabel title="Key facts for referrers" :rows="proRows" />
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Activities: menu with photo bullets -->
  <section class="section bg-stone" aria-labelledby="act-title">
    <div class="wrap">
      <div class="grid gap-6 lg:grid-cols-12" v-reveal>
        <h2 id="act-title" class="text-title lg:col-span-5" data-r>What you can do here</h2>
        <p class="max-w-[46ch] text-lead text-soft lg:col-span-6 lg:col-start-7" data-r>Choose what you enjoy. Most people try a bit of everything, then find their favourite.</p>
      </div>
      <ul class="mt-16 grid gap-x-16 gap-y-10 md:grid-cols-2" v-reveal>
        <li v-for="[t, b, im] in activities" :key="t" class="grid grid-cols-[5rem_1fr] items-center gap-6" data-r>
          <img :src="img(im + '-sm')" alt="" loading="lazy" class="leaf-frame h-20 w-20 object-cover" />
          <div><h3 class="text-lead font-bold">{{ t }}</h3><p class="mt-1 text-soft">{{ b }}</p></div>
        </li>
      </ul>
    </div>
  </section>

  <GrowJourney />

  <!-- Testimonial and our site -->
  <section class="section" aria-labelledby="site-title">
    <div class="wrap grid gap-16 lg:grid-cols-12">
      <figure class="rounded-leaf-lg bg-berry p-8 text-white on-dark sm:p-12 lg:col-span-6" v-reveal>
        <blockquote class="text-[1.5rem] font-bold leading-[1.3] sm:text-[2rem]" data-r><p>Young people “always leave with a big smile on their face.”</p></blockquote>
        <figcaption class="mt-6 text-lead" data-r>Gary Hillery, Manager and Director</figcaption>
        <p class="mt-8 text-berry-pale" data-r>Family quote: <span class="confirm">[CONFIRM: a quote from a family, used with permission]</span></p>
      </figure>
      <div class="lg:col-span-5 lg:col-start-8" v-reveal>
        <h2 id="site-title" class="text-title" data-r>Our site</h2>
        <p class="mt-6 text-lead text-soft" data-r>Funding from the Youth Investment Fund has paid for new facilities. <span class="confirm">[CONFIRM: which are complete]</span></p>
        <ul class="mt-8 space-y-3" data-r>
          <li v-for="f in ['A community workshop', 'A commercial glasshouse', 'A classroom and training centre', 'Tarmacked paths for wheelchair access', 'An off-grid garden centre with solar power and rainwater harvesting', 'A new polytunnel']" :key="f" class="flex gap-3"><span class="leaf-bullet mt-2"></span>{{ f }}</li>
        </ul>
      </div>
    </div>
  </section>

  <FaqList :items="faqs" id="day-faq" />
  <ReferralForm />
</template>
