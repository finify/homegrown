<script setup>
import LeafMark from './LeafMark.vue'
import { site, supporters, url } from '../lib/site.js'
import OpenNow from './OpenNow.vue'

const year = new Date().getFullYear()
const cols = [
  { title: 'Visit', links: [['Garden centre', 'garden-centre.html'], ["What's on", 'whats-on.html'], ['Shop & book workshops', site.store], ['Contact & find us', 'contact.html']] },
  { title: 'Take part', links: [['Day opportunities', 'day-opportunities.html'], ['Make a referral', 'day-opportunities.html#register'], ['Community groups', 'community.html'], ['Free membership', 'community.html#membership']] },
  { title: 'About', links: [['Our story', 'about.html'], ['News & growing tips', 'https://www.sunderlandhomegrown.co.uk/blog'], ['Gallery', 'about.html#gallery'], ['Supporters', 'about.html#supporters']] },
]
const href = (l) => (l.startsWith('http') ? l : url(l))
</script>

<template>
  <footer class="on-dark bg-forest text-white" aria-labelledby="footer-title">
    <div class="wrap pt-24 lg:pt-32">
      <!-- The mark, built large -->
      <div class="grid items-end gap-10 lg:grid-cols-12">
        <div class="lg:col-span-8">
          <p id="footer-title" class="text-display font-bold text-white">Sunderland<br />Home Grown</p>
          <p class="mt-6 max-w-[38ch] text-lead text-leaf-pale">Growing plants, nurturing people. In Thompson Park since 2017.</p>
        </div>
        <LeafMark class="w-56 justify-self-start lg:col-span-4 lg:w-full lg:max-w-sm lg:justify-self-end" />
      </div>

      <div class="mt-20 grid gap-12 lg:mt-28 lg:grid-cols-12">
        <nav aria-label="Footer" class="grid grid-cols-2 gap-10 sm:grid-cols-3 lg:col-span-7">
          <div v-for="c in cols" :key="c.title">
            <h2 class="text-base font-bold text-gold">{{ c.title }}</h2>
            <ul class="mt-4 space-y-2">
              <li v-for="[label, to] in c.links" :key="label">
                <a :href="href(to)" class="inline-flex min-h-[2.75rem] items-center text-white underline decoration-white/30 decoration-2 hover:decoration-gold">{{ label }}</a>
              </li>
            </ul>
          </div>
        </nav>

        <div class="grid gap-10 sm:grid-cols-2 lg:col-span-5">
          <div>
            <h2 class="text-base font-bold text-gold">Opening times</h2>
            <dl class="mt-4 space-y-2">
              <div v-for="h in site.hours" :key="h.days">
                <dt class="font-bold">{{ h.days }}</dt>
                <dd>{{ h.time }}</dd>
              </div>
            </dl>
            <OpenNow dark class="mt-4 text-sm" />
          </div>
          <div>
            <h2 class="text-base font-bold text-gold">Find us</h2>
            <address class="mt-4 not-italic">
              {{ site.name }}<br />
              <template v-for="line in site.address" :key="line">{{ line }}<br /></template>
            </address>
            <p class="mt-4"><a :href="site.phoneHref" class="inline-flex min-h-[2.75rem] items-center font-bold text-white underline decoration-gold decoration-2">{{ site.phone }}</a></p>
            <p class="mt-1 break-words"><a :href="`mailto:${site.emails[0]}`" class="inline-flex min-h-[2.75rem] items-center text-white underline decoration-white/30 decoration-2 hover:decoration-gold">{{ site.emails[0] }}</a></p>
            <p class="mt-1 break-words"><a :href="`mailto:${site.emails[1]}`" class="inline-flex min-h-[2.75rem] items-center text-white underline decoration-white/30 decoration-2 hover:decoration-gold">{{ site.emails[1] }}</a></p>
            <p class="mt-4"><a :href="site.facebook" class="inline-flex min-h-[3rem] items-center gap-2 font-bold text-white underline decoration-gold decoration-2" rel="noopener">Follow us on Facebook</a></p>
          </div>
        </div>
      </div>

      <section id="footer-supporters" aria-labelledby="supported-by" class="mt-20 rounded-leaf-lg bg-forest-900 p-6 sm:p-10">
        <h2 id="supported-by" class="text-lead font-bold text-white">Supported by</h2>
        <ul class="mt-6 grid grid-cols-2 gap-2 sm:grid-cols-3 lg:grid-cols-6">
          <li v-for="s in supporters" :key="s" class="flex min-h-[6rem] items-end rounded-leaf bg-forest-700 p-4 font-bold leading-snug">{{ s }}</li>
        </ul>
        <p class="mt-4 text-sm text-leaf-pale">Logos to be added with permission. <span class="confirm">[CONFIRM: current funders list]</span></p>
      </section>

      <div class="flex flex-col gap-4 py-10 text-sm text-leaf-pale sm:flex-row sm:items-center sm:justify-between">
        <p>© {{ year }} Sunderland Home Grown CIC. Community interest company no. <span class="confirm">[CONFIRM: CIC number]</span></p>
        <ul class="flex flex-wrap gap-x-6 gap-y-2">
          <li><a :href="url('privacy.html')" class="inline-flex min-h-[2.75rem] items-center text-white underline decoration-white/30 decoration-2 hover:decoration-gold">Privacy policy</a></li>
          <li><a :href="url('privacy.html') + '#accessibility'" class="inline-flex min-h-[2.75rem] items-center text-white underline decoration-white/30 decoration-2 hover:decoration-gold">Accessibility</a></li>
          <li><a href="#main" class="inline-flex min-h-[2.75rem] items-center text-white underline decoration-white/30 decoration-2 hover:decoration-gold">Back to top</a></li>
        </ul>
      </div>
    </div>
  </footer>
</template>
