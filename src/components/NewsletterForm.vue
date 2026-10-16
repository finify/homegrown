<script setup>
import { reactive, ref } from 'vue'
import { url } from '../lib/site.js'

// Free membership / newsletter. Deliberately collects no health data and no birthday (audit 5.6).
const postcodes = ['SR1', 'SR2', 'SR3', 'SR4', 'SR5', 'SR6', 'SR7', 'SR8', 'SR9', 'DH3', 'DH4', 'NE9', 'NE36', 'NE37', 'NE38', 'Somewhere else']
const f = reactive({ name: '', email: '', area: '', consent: false })
const error = ref('')
const done = ref(false)
function submit() {
  error.value = !f.name.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(f.email.trim())
    ? 'Enter your name and an email address like name@example.com.'
    : !f.consent ? 'Tick the box to say you would like our emails.' : ''
  if (!error.value) done.value = true
}
</script>

<template>
  <div>
    <p v-if="done" role="status" class="text-lead font-bold text-forest">You're on the list. Welcome to Home Grown.</p>
    <form v-else novalidate class="grid gap-6" @submit.prevent="submit">
      <div class="grid gap-6 sm:grid-cols-2">
        <div><label for="n-name" class="field-label">Name</label><input id="n-name" v-model="f.name" autocomplete="name" class="field" /></div>
        <div><label for="n-email" class="field-label">Email</label><input id="n-email" v-model="f.email" type="email" autocomplete="email" class="field" /></div>
      </div>
      <div>
        <label for="n-area" class="field-label">Postcode area (optional)</label>
        <select id="n-area" v-model="f.area" class="field"><option value="">Prefer not to say</option><option v-for="p in postcodes" :key="p">{{ p }}</option></select>
      </div>
      <label class="flex cursor-pointer gap-4">
        <input v-model="f.consent" type="checkbox" class="choice mt-0.5 rounded" />
        <span>Yes, email me the newsletter, member discounts, events and workshops. You can unsubscribe at any time. <a :href="url('privacy.html')" class="link">Privacy policy</a>.</span>
      </label>
      <p v-if="error" class="field-error" role="alert">{{ error }}</p>
      <button type="submit" class="btn btn-forest w-full sm:w-auto">Join for free</button>
    </form>
  </div>
</template>
