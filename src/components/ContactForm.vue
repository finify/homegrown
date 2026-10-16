<script setup>
import { reactive, ref, nextTick, onMounted } from 'vue'
import { url } from '../lib/site.js'

// General enquiry form with routing by type. Preselect with ?type=hire etc.
const types = [
  ['garden', 'Garden centre'], ['trade', 'Trade and wholesale'], ['day', 'Day opportunities'],
  ['workshops', 'Workshops'], ['hire', 'Hire us'], ['volunteer', 'Volunteering'], ['other', 'Something else'],
]
const f = reactive({ type: '', name: '', email: '', phone: '', message: '', consent: false })
const errors = ref({})
const sent = ref(false)
const box = ref(null)

onMounted(() => {
  const t = new URLSearchParams(location.search).get('type')
  if (types.some(([k]) => k === t)) f.type = t
})

async function submit() {
  const e = {}
  if (!f.type) e.type = 'Choose what your enquiry is about.'
  if (!f.name.trim()) e.name = 'Enter your name.'
  if (!f.email.trim() && !f.phone.trim()) e.email = 'Enter an email address or a phone number, so we can reply.'
  else if (f.email.trim() && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(f.email.trim())) e.email = 'Enter an email address like name@example.com.'
  if (!f.message.trim()) e.message = 'Tell us a little about your enquiry.'
  if (!f.consent) e.consent = 'Tick the box to say we can store these details to reply to you.'
  errors.value = e
  if (!Object.keys(e).length) sent.value = true
  await nextTick()
  if (sent.value) box.value?.focus()
  else document.getElementById(`c-${Object.keys(e)[0]}`)?.focus()
}
</script>

<template>
  <div>
    <div v-if="sent" ref="box" tabindex="-1" role="status" class="rounded-leaf-lg bg-leaf-pale p-8 outline-none">
      <p class="text-title font-bold text-forest">Thank you. Message received.</p>
      <p class="mt-4 text-lead">We'll reply within <span class="confirm">[CONFIRM: 2 working days]</span>.</p>
      <p class="mt-6 text-sm text-soft">Prototype only: this form does not send anything yet.</p>
    </div>
    <form v-else novalidate class="grid gap-7" @submit.prevent="submit">
      <div>
        <label for="c-type" class="field-label">What is your enquiry about? (required)</label>
        <select id="c-type" v-model="f.type" class="field" :aria-invalid="!!errors.type" :aria-describedby="errors.type ? 'ce-type' : undefined">
          <option value="" disabled>Choose one</option>
          <option v-for="[k, l] in types" :key="k" :value="k">{{ l }}</option>
        </select>
        <p v-if="errors.type" id="ce-type" class="field-error">{{ errors.type }}</p>
        <p v-if="f.type === 'day'" class="mt-3 rounded-leaf bg-gold-pale p-4">
          For day opportunities, the <a :href="url('day-opportunities.html') + '#register'" class="link">register your interest form</a> asks the right questions and is quicker for us to act on.
        </p>
      </div>
      <div>
        <label for="c-name" class="field-label">Your name (required)</label>
        <input id="c-name" v-model="f.name" type="text" autocomplete="name" class="field" :aria-invalid="!!errors.name" :aria-describedby="errors.name ? 'ce-name' : undefined" />
        <p v-if="errors.name" id="ce-name" class="field-error">{{ errors.name }}</p>
      </div>
      <div class="grid gap-7 sm:grid-cols-2">
        <div>
          <label for="c-email" class="field-label">Email</label>
          <input id="c-email" v-model="f.email" type="email" autocomplete="email" class="field" :aria-invalid="!!errors.email" aria-describedby="ch-reach ce-email" />
          <p v-if="errors.email" id="ce-email" class="field-error">{{ errors.email }}</p>
        </div>
        <div>
          <label for="c-phone" class="field-label">Phone</label>
          <input id="c-phone" v-model="f.phone" type="tel" autocomplete="tel" class="field" aria-describedby="ch-reach" />
        </div>
        <p id="ch-reach" class="-mt-4 text-sm text-soft sm:col-span-2">Give us at least one of these.</p>
      </div>
      <div>
        <label for="c-message" class="field-label">Your message (required)</label>
        <textarea id="c-message" v-model="f.message" rows="5" class="field" :aria-invalid="!!errors.message" :aria-describedby="errors.message ? 'ce-message' : undefined"></textarea>
        <p v-if="errors.message" id="ce-message" class="field-error">{{ errors.message }}</p>
      </div>
      <div class="rounded-leaf bg-stone p-5">
        <label class="flex cursor-pointer gap-4">
          <input id="c-consent" v-model="f.consent" type="checkbox" class="choice mt-0.5 rounded" :aria-invalid="!!errors.consent" :aria-describedby="errors.consent ? 'ce-consent' : undefined" />
          <span><strong class="text-forest">(Required)</strong> I agree to Sunderland Home Grown storing these details to respond to this enquiry. Read our <a :href="url('privacy.html')" class="link">privacy policy</a>.</span>
        </label>
        <p v-if="errors.consent" id="ce-consent" class="field-error ml-10">{{ errors.consent }}</p>
      </div>
      <button type="submit" class="btn btn-forest w-full sm:w-auto sm:px-10">Send message</button>
    </form>
  </div>
</template>
