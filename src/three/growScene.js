import { Group, Vector2, LatheGeometry, Mesh, MeshStandardMaterial, DoubleSide, CircleGeometry, SphereGeometry, CatmullRomCurve3, Vector3, TubeGeometry } from 'three'
import { makeStage, makeLeaf, LEAF_COLOURS, loopWhileVisible, smoothstep } from './leafKit.js'

/**
 * "How to join" scene: a pot in the colour of the roundel's hand.
 * As the visitor scrolls through the four steps, a seed sprouts and the
 * three roundel leaves open one by one. Step four completes the logo.
 */
export function createGrowScene(canvas, { animate = true } = {}) {
  const stage = makeStage(canvas, { fov: 30, z: 7.4 })
  const { scene, camera, renderer } = stage
  camera.position.y = 1.0
  camera.lookAt(0, 0.7, 0)

  const plant = new Group()
  plant.position.y = -1.4
  scene.add(plant)

  // Pot: a lathe profile, slightly tapered with a rolled rim.
  const profile = [
    [0.0, 0], [0.62, 0], [0.66, 0.05], [0.84, 1.15], [0.95, 1.18], [0.97, 1.36], [0.9, 1.4], [0.82, 1.36],
  ].map(([x, y]) => new Vector2(x, y))
  const pot = new Mesh(
    new LatheGeometry(profile, 64),
    new MeshStandardMaterial({ color: 0xc5ab86, roughness: 0.85, side: DoubleSide }),
  )
  plant.add(pot)

  const soil = new Mesh(
    new CircleGeometry(0.84, 48),
    new MeshStandardMaterial({ color: 0x3b2a1e, roughness: 1 }),
  )
  soil.rotation.x = -Math.PI / 2
  soil.position.y = 1.24
  plant.add(soil)

  const seed = new Mesh(
    new SphereGeometry(0.11, 24, 16),
    new MeshStandardMaterial({ color: 0x7a5a33, roughness: 0.7 }),
  )
  seed.scale.set(1, 0.72, 0.8)
  seed.position.set(0, 1.3, 0)
  plant.add(seed)

  // Stem: a gentle S-curve; drawn progressively via drawRange.
  const stemCurve = new CatmullRomCurve3([
    new Vector3(0, 1.24, 0),
    new Vector3(0.06, 1.8, 0.02),
    new Vector3(-0.05, 2.45, 0),
    new Vector3(0.0, 3.0, 0),
  ])
  const stemGeo = new TubeGeometry(stemCurve, 64, 0.045, 8)
  const stem = new Mesh(stemGeo, new MeshStandardMaterial({ color: 0x2f8a22, roughness: 0.6 }))
  plant.add(stem)
  const stemIndexCount = stemGeo.index.count

  const leafSpecs = [
    { colour: LEAF_COLOURS.green, at: 0.55, fan: 0.95, len: 1.15, from: 0.3, to: 0.5 },
    { colour: LEAF_COLOURS.gold, at: 1.0, fan: 0.05, len: 1.4, from: 0.55, to: 0.75 },
    { colour: LEAF_COLOURS.berry, at: 0.78, fan: -0.95, len: 1.2, from: 0.78, to: 0.96 },
  ]
  const leaves = leafSpecs.map((s, i) => {
    const pivot = new Group()
    pivot.add(makeLeaf(s.colour, { length: s.len, width: s.len * 0.38, fold: 0.2, curl: 0.25 }))
    pivot.position.copy(stemCurve.getPoint(s.at))
    plant.add(pivot)
    return { pivot, ...s, phase: i * 2.1 }
  })

  const state = { progress: animate ? 0 : 1 }
  let shown = state.progress

  const render = (t = 0) => {
    const time = t / 1000
    shown += (state.progress - shown) * (animate ? 0.08 : 1)
    const p = shown

    // Step 1 (0–0.25): the seed settles in. Step 2: the stem rises.
    seed.scale.setScalar(1 - smoothstep(0.25, 0.4, p))
    seed.position.y = 1.3 + Math.sin(time * 2) * 0.01 * (animate ? 1 : 0)
    const grow = smoothstep(0.2, 0.9, p)
    stem.geometry.setDrawRange(0, Math.max(0, Math.floor((stemIndexCount * grow) / 3) * 3))

    leaves.forEach((l) => {
      const k = smoothstep(l.from, l.to, p)
      l.pivot.scale.setScalar(Math.max(0.0001, k))
      const sway = animate ? Math.sin(time * 1.1 + l.phase) * 0.04 * k : 0
      l.pivot.rotation.set(0.35 * k - 0.2, l.fan * 0.4, l.fan * k + sway)
    })

    plant.rotation.y = -0.4 + p * 0.9 + (animate ? Math.sin(time * 0.3) * 0.05 : 0)
    camera.position.y = 1.0 + p * 0.5
    camera.lookAt(0, 0.6 + p * 0.55, 0)
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
