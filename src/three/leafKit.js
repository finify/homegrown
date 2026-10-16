import {
  Shape, ShapeGeometry, MeshStandardMaterial, Mesh, DoubleSide, CatmullRomCurve3, Vector3, TubeGeometry,
  Color, Group, WebGLRenderer, SRGBColorSpace, NeutralToneMapping, Scene, PerspectiveCamera,
  HemisphereLight, DirectionalLight,
} from 'three'

/**
 * Procedural leaves taken from the Home Grown roundel: green, gold and berry.
 * Each leaf is a flat shape folded along its midrib and curled back at the tip,
 * so it reads as a real leaf rather than a flat icon.
 */
export const LEAF_COLOURS = { green: 0x3db82a, gold: 0xe9b82b, berry: 0x934f4e }

export function makeLeafGeometry(length = 1, width = 0.42, fold = 0.18, curl = 0.22) {
  const s = new Shape()
  s.moveTo(0, 0)
  s.bezierCurveTo(width * 1.15, length * 0.18, width * 0.95, length * 0.72, 0, length)
  s.bezierCurveTo(-width * 0.95, length * 0.72, -width * 1.15, length * 0.18, 0, 0)
  const geo = new ShapeGeometry(s, 28)

  // Split into more rows so the fold and curl bend smoothly.
  const pos = geo.attributes.position
  for (let i = 0; i < pos.count; i++) {
    const x = pos.getX(i), y = pos.getY(i)
    const t = y / length
    const z = Math.abs(x) * fold * 2.2 * (1 - t * 0.4) + curl * t * t
    pos.setZ(i, z)
  }
  geo.computeVertexNormals()
  return geo
}

export function makeLeaf(colour, opts = {}) {
  const { length = 1, width = 0.42 } = opts
  const geo = makeLeafGeometry(length, width, opts.fold, opts.curl)
  const mat = new MeshStandardMaterial({ color: colour, roughness: 0.55, metalness: 0, side: DoubleSide })
  const mesh = new Mesh(geo, mat)

  // Midrib: a thin, slightly darker vein along the centre.
  const ribCurve = new CatmullRomCurve3(
    Array.from({ length: 8 }, (_, i) => {
      const t = i / 7
      return new Vector3(0, t * length * 0.94, (opts.curl ?? 0.22) * t * t + 0.004)
    }),
  )
  const rib = new Mesh(
    new TubeGeometry(ribCurve, 24, 0.008 * length, 5),
    new MeshStandardMaterial({ color: new Color(colour).multiplyScalar(0.72), roughness: 0.6 }),
  )
  const group = new Group()
  group.add(mesh, rib)
  return group
}

/** Shared renderer setup with sensible limits for phones. */
export function makeStage(canvas, { fov = 32, z = 5 } = {}) {
  const renderer = new WebGLRenderer({ canvas, antialias: true, alpha: true, powerPreference: 'low-power' })
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2))
  renderer.outputColorSpace = SRGBColorSpace
  renderer.toneMapping = NeutralToneMapping
  renderer.toneMappingExposure = 1.15

  const scene = new Scene()
  const camera = new PerspectiveCamera(fov, 1, 0.1, 100)
  camera.position.set(0, 0, z)

  scene.add(new HemisphereLight(0xfffdf2, 0x4a6a50, 2.4))
  const sun = new DirectionalLight(0xffffff, 2.2)
  sun.position.set(2.5, 4, 5)
  scene.add(sun)
  const rim = new DirectionalLight(0xe9f5d0, 1.0)
  rim.position.set(-4, 1, -3)
  scene.add(rim)

  const resize = () => {
    const { clientWidth: w, clientHeight: h } = canvas
    if (!w || !h) return
    renderer.setSize(w, h, false)
    camera.aspect = w / h
    camera.updateProjectionMatrix()
  }
  const ro = new ResizeObserver(resize)
  ro.observe(canvas)
  resize()

  const dispose = () => {
    ro.disconnect()
    scene.traverse((o) => {
      o.geometry?.dispose()
      if (o.material) [].concat(o.material).forEach((m) => m.dispose())
    })
    renderer.dispose()
  }
  return { renderer, scene, camera, resize, dispose }
}

/** Run a render loop only while the canvas is on screen and the tab is visible. */
export function loopWhileVisible(el, tick) {
  let raf = 0, visible = false
  const run = (t) => { tick(t); raf = requestAnimationFrame(run) }
  const start = () => { if (!raf && visible && !document.hidden) raf = requestAnimationFrame(run) }
  const stop = () => { cancelAnimationFrame(raf); raf = 0 }
  const io = new IntersectionObserver(([e]) => { visible = e.isIntersecting; visible ? start() : stop() })
  io.observe(el)
  const onVis = () => (document.hidden ? stop() : start())
  document.addEventListener('visibilitychange', onVis)
  return () => { stop(); io.disconnect(); document.removeEventListener('visibilitychange', onVis) }
}

export const smoothstep = (a, b, x) => {
  const t = Math.min(1, Math.max(0, (x - a) / (b - a)))
  return t * t * (3 - 2 * t)
}
