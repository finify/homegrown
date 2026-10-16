import { createApp, h } from 'vue'
import '../main.css'
import Layout from '../components/Layout.vue'
import { reveal, parallax } from './reveal.js'

export function mountPage(Page, { current } = {}) {
  const app = createApp({ render: () => h(Layout, { current }, { default: () => h(Page) }) })
  app.directive('reveal', reveal)
  app.directive('parallax', parallax)
  app.mount('#app')
}
