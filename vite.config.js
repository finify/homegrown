import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'node:path'

// Each page is its own HTML entry so titles, meta descriptions and URLs
// mirror the page structure the client will rebuild in their site builder.
const pages = ['index', 'day-opportunities', 'garden-centre', 'whats-on', 'community', 'about', 'contact', 'privacy']

export default defineConfig(({ isSsrBuild }) => ({
  // GitHub Pages serves the repo at /homegrown/
  base: process.env.BASE_PATH ?? '/homegrown/',
  plugins: [vue()],
  // The SSR build is only used at build time to prerender each page's HTML.
  ssr: { noExternal: ['gsap'] },
  build: isSsrBuild ? {} : {
    chunkSizeWarningLimit: 600,
    rollupOptions: {
      input: Object.fromEntries(pages.map((p) => [p, resolve(__dirname, `${p}.html`)])),
      output: {
        manualChunks: { gsap: ['gsap', 'gsap/ScrollTrigger'] },
      },
    },
  },
}))
