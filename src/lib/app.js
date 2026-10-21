import { createSSRApp, h } from 'vue'
import Layout from '../components/Layout.vue'
import Pic from '../components/Pic.vue'
import { reveal, parallax } from './reveal.js'

// Shared by the browser (hydration) and the build-time prerender.
export function createPage(Page, { current } = {}) {
  const app = createSSRApp({ render: () => h(Layout, { current }, { default: () => h(Page) }) })
  app.directive('reveal', reveal)
  app.directive('parallax', parallax)
  app.component('Pic', Pic)
  return app
}
