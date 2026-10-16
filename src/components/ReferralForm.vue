<script setup>
import { reactive, ref, computed, nextTick } from 'vue'
import { url } from '../lib/site.js'

// Register interest / make a referral. Mirrors spec 6.2 field-for-field so it
// can be rebuilt in the builder's native form widget. Front-end validation only.
const roles = ['The person themselves', 'A family member or guardian', 'A social worker', 'A care manager', 'Another professional']
const professional = (r) => ['A social worker', 'A care manager', 'Another professional'].includes(r)
const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

const f = reactive({
  role: '', name: '', organisation: '', email: '', phone: '', contactBy: '',
  person: '', age: '', days: [], support: '', heard: '', consent: false, updates: false,
})
const errors = ref({})
const sent = ref(false)
const summary = ref(null)
const thanks = ref(null)

const isPro = computed(() => professional(f.role))
const forSomeoneElse = computed(() => f.role && f.role !== 'The person themselves')

function validate() {
  const e = {}
  if (!f.role) e.role = 'Choose who you are, so we know how to reply.'
  if (!f.name.trim()) e.name = 'Enter your name.'
  if (isPro.value && !f.organisation.trim()) e.organisation = 'Enter your organisation.'
  if (!f.email.trim()) e.email = 'Enter your email address.'
  else if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(f.email.trim())) e.email = 'Enter an email address like name@example.com.'
  const digits = f.phone.replace(/[^\d+]/g, '')
  if (!f.phone.trim()) e.phone = 'Enter a phone number.'
  else if (digits.replace('+', '').length < 10) e.phone = 'Enter a phone number with at least 10 digits, like 0191 549 9444.'
  if (!f.consent) e.consent = 'Tick the box to say we can store these details to reply to you.'
  return e
}

async function submit() {
  errors.value = validate()
  if (Object.keys(errors.value).length) {
    await nextTick()
    summary.value?.focus()
    return
  }
  // Prototype: nothing is sent. In the builder, the native form posts to the domain inbox
  // and the thank-you state fires the analytics conversion.
  sent.value = true
  await nextTick()
  thanks.value?.focus()
}
const err = (k) => errors.value[k]
const fieldOrder = ['role', 'name', 'organisation', 'email', 'phone', 'consent']
</script>

<template>
  <section id="register" class="section scroll-mt-24" aria-labelledby="register-title">
    <div class="wrap">
      <!-- Clip-out coupon: a filled card with a perforation between the promise and the form. -->
      <div class="relative grid overflow-hidden rounded-leaf-lg bg-forest text-white on-dark lg:grid-cols-12">
        <div class="relative p-6 sm:p-10 lg:col-span-5 lg:p-14">
          <h2 id="register-title" class="text-title text-white">Register your interest</h2>
          <p class="mt-6 max-w-[36ch] text-lead text-leaf-pale">For yourself, for someone you care for, or as a referrer. It takes about five minutes.</p>
          <ul class="mt-10 space-y-4">
            <li class="flex gap-3"><span class="leaf-bullet mt-2 bg-gold"></span><span>We reply by phone or email within <span class="confirm">[CONFIRM: 2 working days]</span>.</span></li>
            <li class="flex gap-3"><span class="leaf-bullet mt-2 bg-gold"></span><span>Registering does not commit you to anything.</span></li>
            <li class="flex gap-3"><span class="leaf-bullet mt-2 bg-gold"></span><span>Prefer to talk? Call <a href="tel:+441915499444" class="font-bold text-white underline decoration-gold decoration-2">0191 549 9444</a>.</span></li>
          </ul>
          <div class="pointer-events-none absolute -bottom-24 -left-16 hidden h-72 w-72 bg-forest-700 lg:block" style="border-radius: 0 100% 0 100%" aria-hidden="true"></div>
        </div>

        <!-- Perforation -->
        <div class="pointer-events-none absolute bottom-0 top-0 hidden border-l-[5px] border-dotted border-ground/40 lg:left-[41.666%] lg:block" aria-hidden="true">
          <span class="absolute -left-[17px] -top-[14px] h-7 w-7 rounded-full bg-ground"></span>
          <span class="absolute -bottom-[14px] -left-[17px] h-7 w-7 rounded-full bg-ground"></span>
        </div>

        <div class="bg-white p-6 text-ink sm:p-10 lg:col-span-7 lg:m-3 lg:rounded-leaf lg:p-12">
          <div v-if="sent" ref="thanks" tabindex="-1" class="outline-none" role="status">
            <p class="text-title font-bold text-forest">Thank you, {{ f.name.split(' ')[0] }}.</p>
            <p class="mt-6 text-lead">We have your details. We'll {{ f.contactBy === 'Email' ? 'email' : f.contactBy === 'Phone' ? 'call' : 'call or email' }} you within <span class="confirm">[CONFIRM: 2 working days]</span>.</p>
            <p class="mt-4">If anything is urgent, phone <a href="tel:+441915499444" class="link">0191 549 9444</a>.</p>
            <p class="mt-8 text-sm text-soft">Prototype only: this form does not send anything yet.</p>
          </div>

          <form v-else novalidate @submit.prevent="submit" aria-describedby="form-intro">
            <p id="form-intro" class="mb-8 text-soft">Questions marked <strong class="text-forest">(required)</strong> must be answered. Everything else is optional.</p>

            <div v-if="Object.keys(errors).length" ref="summary" tabindex="-1" class="mb-8 rounded-leaf border-4 border-berry bg-berry-pale p-6 outline-none" role="alert" aria-labelledby="err-title">
              <h3 id="err-title" class="text-lead font-bold text-berry">Please check {{ Object.keys(errors).length === 1 ? 'one answer' : Object.keys(errors).length + ' answers' }}</h3>
              <ul class="mt-3 list-disc space-y-1 pl-6">
                <li v-for="k in fieldOrder.filter((k) => errors[k])" :key="k"><a :href="`#f-${k}`" class="font-bold text-berry underline">{{ errors[k] }}</a></li>
              </ul>
            </div>

            <div class="grid gap-7">
              <div>
                <label for="f-role" class="field-label">I am… (required)</label>
                <select id="f-role" v-model="f.role" class="field" :aria-invalid="!!err('role')" :aria-describedby="err('role') ? 'e-role' : undefined">
                  <option value="" disabled>Choose one</option>
                  <option v-for="r in roles" :key="r">{{ r }}</option>
                </select>
                <p v-if="err('role')" id="e-role" class="field-error">{{ err('role') }}</p>
              </div>

              <div class="grid gap-7 sm:grid-cols-2">
                <div>
                  <label for="f-name" class="field-label">Your name (required)</label>
                  <input id="f-name" v-model="f.name" type="text" autocomplete="name" class="field" :aria-invalid="!!err('name')" :aria-describedby="err('name') ? 'e-name' : undefined" />
                  <p v-if="err('name')" id="e-name" class="field-error">{{ err('name') }}</p>
                </div>
                <div v-if="isPro">
                  <label for="f-organisation" class="field-label">Organisation (required)</label>
                  <input id="f-organisation" v-model="f.organisation" type="text" autocomplete="organization" class="field" :aria-invalid="!!err('organisation')" :aria-describedby="err('organisation') ? 'e-organisation' : undefined" />
                  <p v-if="err('organisation')" id="e-organisation" class="field-error">{{ err('organisation') }}</p>
                </div>
              </div>

              <div class="grid gap-7 sm:grid-cols-2">
                <div>
                  <label for="f-email" class="field-label">Email (required)</label>
                  <input id="f-email" v-model="f.email" type="email" autocomplete="email" inputmode="email" class="field" :aria-invalid="!!err('email')" :aria-describedby="err('email') ? 'e-email' : undefined" />
                  <p v-if="err('email')" id="e-email" class="field-error">{{ err('email') }}</p>
                </div>
                <div>
                  <label for="f-phone" class="field-label">Phone (required)</label>
                  <input id="f-phone" v-model="f.phone" type="tel" autocomplete="tel" inputmode="tel" class="field" :aria-invalid="!!err('phone')" :aria-describedby="err('phone') ? 'e-phone' : undefined" />
                  <p v-if="err('phone')" id="e-phone" class="field-error">{{ err('phone') }}</p>
                </div>
              </div>

              <fieldset>
                <legend class="field-label">How should we contact you?</legend>
                <div class="flex flex-wrap gap-x-8 gap-y-3">
                  <label v-for="o in ['Phone', 'Email', 'Either']" :key="o" class="flex min-h-[2.75rem] cursor-pointer items-center gap-3">
                    <input v-model="f.contactBy" type="radio" name="contactBy" :value="o" class="choice" /> {{ o }}
                  </label>
                </div>
              </fieldset>

              <div v-if="forSomeoneElse">
                <label for="f-person" class="field-label">Name of the person interested</label>
                <input id="f-person" v-model="f.person" type="text" class="field" />
              </div>

              <div>
                <label for="f-age" class="field-label">Age group</label>
                <select id="f-age" v-model="f.age" class="field" aria-describedby="h-age">
                  <option value="">Prefer not to say</option>
                  <option>16 to 18</option><option>19 to 25</option><option>26 or over</option>
                </select>
                <p id="h-age" class="mt-2 text-sm text-soft"><span class="confirm">[CONFIRM: age bands]</span></p>
              </div>

              <fieldset>
                <legend class="field-label">Days you are interested in</legend>
                <p class="-mt-1 mb-3 text-sm text-soft">Tick any that might work. <span class="confirm">[CONFIRM: session days]</span></p>
                <div class="flex flex-wrap gap-2">
                  <label v-for="d in days" :key="d" class="flex min-h-[3rem] cursor-pointer items-center gap-3 rounded-leaf bg-stone px-4 has-[:checked]:bg-leaf-pale">
                    <input v-model="f.days" type="checkbox" :value="d" class="choice rounded" /> {{ d }}
                  </label>
                </div>
              </fieldset>

              <div>
                <label for="f-support" class="field-label">Is there anything we should know to support them?</label>
                <p id="h-support" class="-mt-1 mb-3 text-sm text-soft">Optional. You do not need to share a diagnosis. Tell us whatever helps us make the first visit go well.</p>
                <textarea id="f-support" v-model="f.support" rows="4" class="field" aria-describedby="h-support"></textarea>
              </div>

              <div>
                <label for="f-heard" class="field-label">How did you hear about us?</label>
                <select id="f-heard" v-model="f.heard" class="field">
                  <option value="">Choose one</option>
                  <option>Social worker or care manager</option><option>School or college</option><option>Facebook</option>
                  <option>Search engine</option><option>Friend or family</option><option>Visited the garden centre</option><option>Other</option>
                </select>
              </div>

              <div class="rounded-leaf bg-stone p-5">
                <label class="flex cursor-pointer gap-4">
                  <input id="f-consent" v-model="f.consent" type="checkbox" class="choice mt-0.5 rounded" :aria-invalid="!!err('consent')" :aria-describedby="err('consent') ? 'e-consent' : undefined" />
                  <span><strong class="text-forest">(Required)</strong> I agree to Sunderland Home Grown storing these details to respond to this enquiry. Read our <a :href="url('privacy.html')" class="link">privacy policy</a>.</span>
                </label>
                <p v-if="err('consent')" id="e-consent" class="field-error ml-10">{{ err('consent') }}</p>
                <label class="mt-4 flex cursor-pointer gap-4">
                  <input v-model="f.updates" type="checkbox" class="choice mt-0.5 rounded" />
                  <span>Keep me updated by email about workshops and events. You can stop at any time.</span>
                </label>
              </div>

              <button type="submit" class="btn btn-forest w-full sm:w-auto sm:px-10">Send my details</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
