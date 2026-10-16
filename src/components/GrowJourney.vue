<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import LeafMark from './LeafMark.vue'
import { ScrollTrigger, reduceMotion } from '../lib/reveal.js'
import { webglAvailable } from '../three/support.js'
import { url } from '../lib/site.js'

// How to join, in four steps. The pot on the left grows as each step scrolls
// past; by step four the plant carries the three leaves of the roundel.
defineProps({ compact: Boolean })
const steps = [
  { title: 'Get in touch', body: 'Fill in the form, phone us or email. You can do this yourself, or a family member, carer or social worker can do it for you.', tip: 'We reply within', confirm: '[CONFIRM: 2 working days]' },
  { title: 'Come and see us', body: 'Visit Thompson Park, meet the team and try a taster session. Bring someone with you if that helps.', confirm: '[CONFIRM: taster session offer]' },
  { title: 'Agree your days', body: 'Together we choose the days, the activities and the support that suit you. We talk about funding with you or your referrer.', confirm: '[CONFIRM: funding routes]' },
  { title: 'Start growing', body: 'Your first day. A member of staff meets you, shows you round and works alongside you.' },
]
const active = ref(0)
const root = ref(null)
const canvas = ref(null)
const fallback = ref(false)
const still = ref(false)
let scene, triggers = []

onMounted(async () => {
  still.value = reduceMotion()
  if (!webglAvailable()) { fallback.value = true }
  else {
    const { createGrowScene } = await import('../three/growScene.js')
    scene = createGrowScene(canvas.value, { animate: !still.value })
  }
  if (still.value) { active.value = steps.length - 1; return }

  const items = root.value.querySelectorAll('[data-step]')
  triggers.push(ScrollTrigger.create({
    trigger: root.value.querySelector('[data-steps]'),
    start: 'top 65%',
    end: 'bottom 55%',
    scrub: true,
    onUpdate: (s) => { if (scene) scene.state.progress = s.progress },
  }))
  items.forEach((el, i) => {
    triggers.push(ScrollTrigger.create({
      trigger: el, start: 'top 60%', end: 'bottom 60%',
      onToggle: (s) => s.isActive && (active.value = i),
    }))
  })
})
onBeforeUnmount(() => { triggers.forEach((t) => t.kill()); scene?.dispose() })
</script>

<template>
  <section ref="root" class="section bg-leaf-pale" aria-labelledby="join-title">
    <div class="wrap">
      <div class="grid gap-6 lg:grid-cols-12" v-reveal>
        <h2 id="join-title" class="text-title lg:col-span-5" data-r>How to join, in four steps</h2>
        <p class="max-w-[52ch] text-lead text-soft lg:col-span-6 lg:col-start-7" data-r>
          No forms to fill in on the first day and nothing to decide alone. Each step is a conversation.
        </p>
      </div>

      <div class="mt-16 grid gap-10 lg:mt-24 lg:grid-cols-12">
        <!-- Sticky growing plant -->
        <div class="sticky top-20 z-20 -mx-4 h-[34svh] bg-leaf-pale sm:mx-0 lg:top-28 lg:col-span-6 lg:h-[72svh]">
          <canvas v-if="!fallback" ref="canvas" class="h-full w-full" aria-hidden="true"></canvas>
          <LeafMark v-else class="h-full w-full p-10" />
          <p class="sr-only">An illustration of a seed in a plant pot growing into a plant with three leaves as you move through the steps.</p>
        </div>

        <ol data-steps class="relative space-y-6 lg:col-span-5 lg:col-start-8 lg:space-y-[24svh] lg:py-[12svh]">
          <li
            v-for="(s, i) in steps"
            :key="s.title"
            data-step
            class="rounded-leaf-lg p-6 transition-colors duration-500 sm:p-8"
            :class="active === i ? 'bg-forest text-white on-dark' : 'bg-ground text-ink'"
          >
            <p class="text-sm font-bold" :class="active === i ? 'text-gold' : 'text-soft'">Step {{ i + 1 }} of 4</p>
            <h3 class="mt-2 text-lead font-bold" :class="active === i ? 'text-white' : 'text-forest'">{{ s.title }}</h3>
            <p class="mt-3">{{ s.body }}</p>
            <p v-if="s.confirm" class="mt-3"><span v-if="s.tip">{{ s.tip }} </span><span class="confirm">{{ s.confirm }}</span></p>
          </li>
        </ol>
      </div>

      <div class="mt-16 flex flex-wrap gap-3" v-reveal>
        <a :href="url('day-opportunities.html') + '#register'" class="btn btn-forest" data-r>Register your interest</a>
        <a href="tel:+441915499444" class="btn btn-white" data-r>Call 0191 549 9444</a>
      </div>
    </div>
  </section>
</template>
