import { renderToString } from 'vue/server-renderer'
import { createPage } from './lib/app.js'
import Home from './pages/Home.vue'
import DayOpportunities from './pages/DayOpportunities.vue'
import GardenCentre from './pages/GardenCentre.vue'
import WhatsOn from './pages/WhatsOn.vue'
import Community from './pages/Community.vue'
import About from './pages/About.vue'
import Contact from './pages/Contact.vue'
import Privacy from './pages/Privacy.vue'

// Used only at build time (scripts/prerender.mjs) to write each page's HTML.
export const pages = {
  index: [Home, 'home'],
  'day-opportunities': [DayOpportunities, 'day'],
  'garden-centre': [GardenCentre, 'garden'],
  'whats-on': [WhatsOn, 'whats'],
  community: [Community, 'community'],
  about: [About, 'about'],
  contact: [Contact, 'contact'],
  privacy: [Privacy, 'privacy'],
}

export function render(file) {
  const [Page, current] = pages[file]
  return renderToString(createPage(Page, { current }))
}
