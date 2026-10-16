import { Group } from 'three'
import { makeStage, makeLeaf, LEAF_COLOURS, loopWhileVisible } from './leafKit.js'

/**
 * Hero scene: the three roundel leaves, fanned out from one stem point.
 * state.open   0 = closed bud, 1 = fanned out like the logo
 * state.scroll 0..1 as the hero scrolls away (leaves turn and lift)
 */
export function createHeroLeaves(canvas, { animate = true } = {}) {
  const stage = makeStage(canvas, { fov: 30, z: 7.6 })
  const { scene, camera, renderer } = stage

  const root = new Group()
  root.position.set(0, -1.45, 0)
  scene.add(root)

  // Order and angles follow the roundel: green left, gold up the middle, berry right.
  const specs = [
    { colour: LEAF_COLOURS.green, length: 2.05, width: 0.86, fan: 0.62, tilt: 0.28, curl: 0.3 },
    { colour: LEAF_COLOURS.gold, length: 2.55, width: 0.92, fan: 0.0, tilt: -0.12, curl: 0.38 },
    { colour: LEAF_COLOURS.berry, length: 2.15, width: 0.88, fan: -0.66, tilt: 0.22, curl: 0.32 },
  ]
  const leaves = specs.map((s, i) => {
    const pivot = new Group()
    const leaf = makeLeaf(s.colour, { length: s.length, width: s.width, fold: 0.07, curl: s.curl })
    pivot.add(leaf)
    pivot.position.z = (i - 1) * -0.06
    root.add(pivot)
    return { pivot, leaf, ...s, phase: i * 1.7 }
  })

  const state = { open: animate ? 0 : 1, scroll: 0, px: 0, py: 0 }
  let tx = 0, ty = 0

  const render = (t = 0) => {
    const time = t / 1000
    tx += (state.px - tx) * 0.05
    ty += (state.py - ty) * 0.05
    leaves.forEach((l) => {
      const sway = animate ? Math.sin(time * 0.9 + l.phase) * 0.035 : 0
      l.pivot.rotation.z = l.fan * state.open + sway
      l.pivot.rotation.x = l.tilt * state.open - 0.25 * (1 - state.open)
      l.pivot.rotation.y = (l.fan * 0.5) * state.open
      const s = 0.55 + 0.45 * state.open
      l.pivot.scale.setScalar(s)
    })
    root.rotation.y = -0.12 + tx * 0.3 + state.scroll * 1.1
    root.rotation.x = 0.12 + ty * 0.15 - state.scroll * 0.3
    root.position.y = -1.45 + state.scroll * 0.5
    camera.position.z = 7.6 - state.scroll * 0.8
    renderer.render(scene, camera)
  }

  const stop = animate ? loopWhileVisible(canvas, render) : () => {}
  render()

  return {
    state,
    render,
    dispose() { stop(); stage.dispose() },
  }
}
