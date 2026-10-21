import '../main.css'
import { createPage } from './app.js'
import { speedUpNavigation } from './nav.js'

export function mountPage(Page, opts) {
  // The HTML is already prerendered; this hydrates it rather than rebuilding the page.
  createPage(Page, opts).mount('#app')
  speedUpNavigation()
}
