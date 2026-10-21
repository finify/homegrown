// Writes the server-rendered HTML of every page into dist/*.html, so content shows
// before any JavaScript runs. Run after `vite build` and the SSR build (see package.json).
import { readFileSync, writeFileSync } from 'node:fs'
import { pathToFileURL } from 'node:url'
import { resolve } from 'node:path'

const { pages, render } = await import(pathToFileURL(resolve('.ssr/entry-server.js')).href)
for (const file of Object.keys(pages)) {
  const path = `dist/${file}.html`
  const html = readFileSync(path, 'utf8')
  const body = await render(file)
  if (!html.includes('<div id="app"></div>')) throw new Error(`No #app placeholder in ${path}`)
  writeFileSync(path, html.replace('<div id="app"></div>', `<div id="app">${body}</div>`))
  console.log(`prerendered ${path} (${(body.length / 1024).toFixed(0)} KB)`)
}
