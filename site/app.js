// The Human Empire: eight books on a desk, and a reader that opens one of them.
// Everything is drawn with three.js. The pages are images made from the designed PDF by build/site.py.
import * as THREE from 'three';

const INK = '#2f2a26', PAPER = '#faf6ee', TINT = '#f3ecdd', SOFT = '#8a8178', ACC = '#b5523b';
const W = 1.48, H = 2.10;            // one page, in scene units (A5 in decimetres)
const CT = 0.035;                    // thickness of a cover board
const SERIF = '"Palatino Linotype", "Book Antiqua", Palatino, "P052", "URW Palladio L", Georgia, serif';
const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;
const SLOW = Number(new URLSearchParams(location.search).get('slow')) || 1;   // ?slow=4 to study the animations

const $ = (id) => document.getElementById(id);
const canvas = $('stage');

// ------------------------------------------------------------------ data
const parts = await fetch('parts.json', { cache: 'no-cache' }).then((r) => r.json());   // always the current list; each part's `v` stamps its files

// plain links first: they work whatever happens to WebGL
{
  const ul = document.createElement('ul');
  for (const p of parts) {
    const li = document.createElement('li');
    li.append(p.title ? `Part ${p.roman}: ${p.title} ` : `Part ${p.roman} `);
    if (p.released) {
      const b = document.createElement('button'); b.type = 'button'; b.textContent = 'Read'; b.dataset.part = p.n; li.append(b);
      for (const [k, label] of [['pdf', 'PDF'], ['epub', 'EPUB']]) {
        if (p[k]) { const a = document.createElement('a'); a.href = p[k]; a.download = ''; a.textContent = label; li.append(a); }
      }
    } else { const s = document.createElement('span'); s.className = 'soon'; s.textContent = 'not yet released'; li.append(s); }
    ul.append(li);
  }
  $('parts').append(ul);
}

let renderer;
try {
  renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
} catch (e) {
  document.body.classList.add('flat');
  throw e;
}
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const MAX_ANISO = renderer.capabilities.getMaxAnisotropy();

const scene = new THREE.Scene();
scene.background = new THREE.Color('#1d1815');
const camera = new THREE.PerspectiveCamera(32, 1, 0.1, 100);
camera.up.set(0, 0, -1);            // 'up' on screen is the far edge of the desk, so the camera can look straight down

scene.add(new THREE.AmbientLight('#fff4e6', 1.85));
const sun = new THREE.DirectionalLight('#fff6ea', 1.55);
sun.position.set(-4.5, 11, 4);
sun.castShadow = true;
sun.shadow.mapSize.set(2048, 2048);
Object.assign(sun.shadow.camera, { left: -9, right: 9, top: 7, bottom: -7, near: 1, far: 30 });
sun.shadow.radius = 6; sun.shadow.bias = -0.0005;
scene.add(sun);

// the desk: dark, with a pool of light in the middle
{
  const c = document.createElement('canvas'); c.width = c.height = 512;
  const g = c.getContext('2d');
  const grad = g.createRadialGradient(256, 256, 30, 256, 256, 256);
  grad.addColorStop(0, '#4a3d33'); grad.addColorStop(0.55, '#2c241f'); grad.addColorStop(1, '#1d1815');
  g.fillStyle = grad; g.fillRect(0, 0, 512, 512);
  const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace;
  const desk = new THREE.Mesh(new THREE.PlaneGeometry(44, 44).rotateX(-Math.PI / 2),
    new THREE.MeshStandardMaterial({ map: tex, roughness: 1 }));
  desk.receiveShadow = true;
  scene.add(desk);
}

// ------------------------------------------------------------------ small helpers
const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
const easeOut = (t) => 1 - Math.pow(1 - t, 3);
const lerp = (a, b, t) => a + (b - a) * t;
const tweens = new Set();
function tween(seconds, step, curve = ease) {
  if (REDUCED) seconds = Math.min(seconds, 0.01);
  seconds *= SLOW;
  return new Promise((done) => {
    const tw = { t0: performance.now(), d: seconds * 1000, step, curve, done };
    tweens.add(tw);
  });
}
function runTweens(now) {
  for (const tw of tweens) {
    const t = Math.min(1, (now - tw.t0) / tw.d);
    tw.step(tw.curve(t), t);
    if (t >= 1) { tweens.delete(tw); tw.done(); }
  }
}
const wait = (s) => tween(s, () => {});

function canvasTexture(w, h, draw) {
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  draw(c.getContext('2d'), w, h);
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = MAX_ANISO;
  return t;
}
function flat(w, h) { return new THREE.PlaneGeometry(w, h).rotateX(-Math.PI / 2); }   // lies on the desk, top of the image away from the viewer

// a cover for a part that has no PDF yet, laid out like the real ones (cover() in build/book.typ)
function drawnCover(part) {
  return canvasTexture(740, 1050, (g, w, h) => {
    const col = part.colour || ACC;
    g.fillStyle = TINT; g.fillRect(0, 0, w, h);
    g.fillStyle = col; g.fillRect(0, 0, 45, h);                       // the strip at the spine
    g.save(); g.globalAlpha = 0.2; g.textAlign = 'right'; g.font = `400 440px ${SERIF}`;
    g.fillText(part.roman, w + 20, h - 150); g.restore();              // the pale numeral behind
    g.textAlign = 'left'; g.fillStyle = INK; g.font = `400 20px ${SERIF}`;
    g.fillText('THE HUMAN EMPIRE'.split('').join('\u200a\u2009'), 100, 118);
    g.fillStyle = col; g.fillRect(100, 133, 150, 4);
    g.font = `400 19px ${SERIF}`; g.fillText(`PART ${part.roman}`.split('').join('\u200a\u2009'), 100, 308);
    g.fillStyle = INK;
    let size = 124; g.font = `400 ${size}px ${SERIF}`;
    while (g.measureText(part.title || '').width > w - 130 && size > 60) { size -= 4; g.font = `400 ${size}px ${SERIF}`; }
    g.fillText(part.title || '', 96, 420);
    g.fillStyle = SOFT; g.font = `400 19px ${SERIF}`;
    g.fillText('IN PREPARATION'.split('').join('\u200a\u2009'), 100, 962);
    g.fillStyle = 'rgba(40, 33, 28, 0.34)'; g.fillRect(0, 0, w, h);   // unopened books sit in shadow
  });
}

const paperEdge = canvasTexture(64, 64, (g) => {
  g.fillStyle = '#ece3cf'; g.fillRect(0, 0, 64, 64);
  for (let y = 0; y < 64; y += 2) { g.fillStyle = `rgba(120,100,70,${0.10 + 0.12 * Math.random()})`; g.fillRect(0, y, 64, 1); }
});
const gutterShade = canvasTexture(256, 4, (g) => {
  const gr = g.createLinearGradient(0, 0, 256, 0);
  gr.addColorStop(0, 'rgba(60,45,30,0)'); gr.addColorStop(0.46, 'rgba(60,45,30,0.20)'); gr.addColorStop(0.5, 'rgba(40,28,18,0.42)');
  gr.addColorStop(0.54, 'rgba(60,45,30,0.20)'); gr.addColorStop(1, 'rgba(60,45,30,0)');
  g.fillStyle = gr; g.fillRect(0, 0, 256, 4);
});
const blankPage = canvasTexture(8, 8, (g) => { g.fillStyle = PAPER; g.fillRect(0, 0, 8, 8); });

const loader = new THREE.TextureLoader();
function pageTexture(url) {
  const t = loader.load(url);
  t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = MAX_ANISO;
  return t;
}

// ------------------------------------------------------------------ a book
// Local frame: the spine runs along z at x = 0, the desk is y = 0, and the closed book covers 0 <= x <= W.
// Opened, the front cover and the pages already read lie over -W <= x <= 0.
class Book {
  constructor(part, slot) {
    this.part = part; this.slot = slot;
    this.pages = part.pages || 150;
    // Thickness of the block of pages, true to scale: a leaf of paper is a tenth of a millimetre.
    // A thicker block would stand nearer the camera and make the right-hand page look larger than the left.
    this.T = 0.012 + this.pages * 0.0005;
    this.spreads = Math.ceil(this.pages / 2);     // spread s shows page 2s+1 on the left and 2s+2 on the right; page 1 is the cover
    this.s = 0; this.f = 0; this.textures = new Map();
    this.group = new THREE.Group();
    this.lift = new THREE.Group();                // hover and opening move this, the slot moves the group
    this.group.add(this.lift);

    const board = new THREE.MeshStandardMaterial({ color: part.released ? '#efe6d3' : '#a39a8b', roughness: 0.85 });
    const edge = new THREE.MeshStandardMaterial({ map: paperEdge, roughness: 1 });
    const add = (mesh, parent = this.lift) => { mesh.castShadow = true; mesh.receiveShadow = true; mesh.userData.book = this; parent.add(mesh); return mesh; };

    this.back = add(new THREE.Mesh(new THREE.BoxGeometry(W + 0.05, CT, H + 0.08), board));
    this.back.position.set(W / 2 + 0.005, CT / 2, 0);
    this.spine = add(new THREE.Mesh(new THREE.BoxGeometry(CT, 1, H + 0.08), new THREE.MeshStandardMaterial({ color: part.released ? '#b5523b' : '#7d5548', roughness: 0.8 })));

    const unit = new THREE.BoxGeometry(W, 1, H);
    this.right = add(new THREE.Mesh(unit, edge));
    this.left = add(new THREE.Mesh(unit, edge));
    this.rightPage = add(new THREE.Mesh(flat(W, H), new THREE.MeshStandardMaterial({ map: blankPage, roughness: 1 })));
    this.leftPage = add(new THREE.Mesh(flat(W, H), new THREE.MeshStandardMaterial({ map: blankPage, roughness: 1 })));
    this.rightPage.castShadow = this.leftPage.castShadow = false;
    this.gutter = new THREE.Mesh(flat(0.9, H), new THREE.MeshBasicMaterial({ map: gutterShade, transparent: true, depthWrite: false }));
    this.gutter.visible = false; this.lift.add(this.gutter);

    // the front cover turns on a hinge at the spine
    this.hinge = new THREE.Group(); this.lift.add(this.hinge);
    this.cover = add(new THREE.Mesh(new THREE.BoxGeometry(W + 0.05, CT, H + 0.08), board), this.hinge);
    this.cover.position.set(W / 2 + 0.005, CT / 2, 0);
    const art = part.released ? pageTexture(`pages/${part.n}/001.webp?v=${part.v || 0}`) : drawnCover(part);
    this.art = add(new THREE.Mesh(flat(W + 0.05, H + 0.08), new THREE.MeshStandardMaterial({ map: art, roughness: 0.75 })), this.hinge);
    this.art.position.set(W / 2 + 0.005, CT + 0.002, 0); this.art.castShadow = false;

    this.openAmount = 0;
    this.layout();
    scene.add(this.group);
  }

  // place every piece for the current opening (0 closed, 1 open) and the share of pages already read
  layout() {
    const o = this.openAmount, T = this.T, f = this.f;
    // Open, the two piles are drawn level, so both pages are the same distance from the eye and the same size.
    const tr = lerp(T, T / 2, o), tl = T / 2;
    this.right.scale.y = tr; this.right.position.set(W / 2, CT + tr / 2, 0);
    this.left.scale.y = tl; this.left.position.set(-W / 2, CT + tl / 2, 0);
    this.left.visible = this.leftPage.visible = o > 0.98;
    this.rightPage.position.set(W / 2, CT + tr + 0.0015, 0);
    this.leftPage.position.set(-W / 2, CT + tl + 0.0015, 0);
    this.gutter.position.set(0, CT + Math.max(tr, tl) + 0.004, 0);
    this.gutter.visible = o > 0.98;
    // closed, the hinge sits on top of the pages; open, it has dropped to the desk so the cover lies flat
    this.hinge.position.set(0, lerp(CT + T, CT, o), 0);
    this.hinge.rotation.z = Math.PI * o;
    const sh = lerp(2 * CT + T, CT, o);
    this.spine.scale.y = sh; this.spine.position.set(lerp(-CT / 2, 0, o), sh / 2, 0);
  }

  pageOf(side, s = this.s) { const p = side === 'left' ? 2 * s + 1 : 2 * s + 2; return s < 0 || (s === 0 && side === 'left') ? 0 : (p <= this.pages ? p : 0); }
  tex(p) {
    if (!p) return blankPage;
    if (!this.textures.has(p)) this.textures.set(p, pageTexture(`pages/${this.part.n}/${String(p).padStart(3, '0')}.webp?v=${this.part.v || 0}`));
    return this.textures.get(p);
  }
  // keep the pages near the reader in memory and let the rest go
  warm() {
    const keep = new Set();
    for (let d = -2; d <= 3; d++) for (const side of ['left', 'right']) {
      const s = this.s + d; if (s < 0 || s > this.spreads) continue;
      const p = this.pageOf(side, s); if (p) { keep.add(p); this.tex(p); }
    }
    for (const [p, t] of this.textures) if (!keep.has(p)) { t.dispose(); this.textures.delete(p); }
  }
  show() {
    this.leftPage.material.map = this.tex(this.pageOf('left'));
    this.rightPage.material.map = this.tex(this.pageOf('right'));
    this.f = this.spreads ? this.s / this.spreads : 0;
    this.layout(); this.warm();
  }
}

// a single leaf in the air: a strip of quads bent as it turns about the spine
const SEG = 28;
class Leaf {
  constructor() {
    const g = new THREE.PlaneGeometry(W, H, SEG, 1).rotateX(-Math.PI / 2).translate(W / 2, 0, 0);
    const gb = g.clone();
    const uv = gb.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setX(i, 1 - uv.getX(i));   // the back reads the right way round
    gb.setAttribute('position', g.attributes.position); gb.setAttribute('normal', g.attributes.normal);
    this.geo = g;
    this.front = new THREE.Mesh(g, new THREE.MeshStandardMaterial({ map: blankPage, roughness: 1, side: THREE.FrontSide }));
    this.backM = new THREE.Mesh(gb, new THREE.MeshStandardMaterial({ map: blankPage, roughness: 1, side: THREE.BackSide }));
    this.mesh = new THREE.Group(); this.mesh.add(this.front, this.backM);
    this.front.castShadow = true;
    this.mesh.visible = false;
  }
  // theta: 0 lying on the right-hand pages, pi lying on the left-hand pages
  bend(theta, y0) {
    const pos = this.geo.attributes.position, step = W / SEG;
    let x = 0, y = y0;
    const curl = 0.95 * Math.sin(theta);
    for (let i = 0; i <= SEG; i++) {
      if (i > 0) {
        const r = (i - 0.5) / SEG;
        const phi = Math.min(Math.PI, Math.max(0, theta + curl * (r - 0.38) * 1.5));
        x += Math.cos(phi) * step; y += Math.sin(phi) * step;
      }
      // PlaneGeometry lays its vertices in two rows of SEG + 1
      pos.setXYZ(i, x, y, pos.getZ(i)); pos.setXYZ(i + SEG + 1, x, y, pos.getZ(i + SEG + 1));
    }
    pos.needsUpdate = true; this.geo.computeVertexNormals();
  }
}

// ------------------------------------------------------------------ the desk of eight books
const books = parts.map((p, i) => new Book(p, i));
const leaf = new Leaf();
let mode = 'desk';            // desk | moving | reading
let current = null, hovered = null, single = false, zoom = 1;
const pan = new THREE.Vector2();
const camPos = new THREE.Vector3(), camLook = new THREE.Vector3();
const FOV_T = Math.tan(THREE.MathUtils.degToRad(camera.fov / 2));

let deskScroll = 0, deskRange = 0, deskK = 1;
function slotPosition(i, cols) {
  const rows = Math.ceil(8 / cols), gx = W + 0.62, gz = H + 0.62;
  const c = i % cols, r = Math.floor(i / cols);
  return new THREE.Vector3((c - (cols - 1) / 2) * gx - W / 2, 0, (r - (rows - 1) / 2) * gz);
}
function deskView() {
  const aspect = innerWidth / innerHeight;
  const cols = aspect > 1.15 ? 4 : aspect > 0.62 ? 3 : 2;
  const rows = Math.ceil(8 / cols);
  const gw = cols * (W + 0.62), gh = rows * (H + 0.62);
  const tilt = 0.42;
  // the books fill the band between the title and the caption, whatever the size of the window
  const top = Math.min(0.6, ($('intro').getBoundingClientRect().bottom + 14) / innerHeight), bottom = 0.93;
  const band = bottom - top, centre = (top + bottom) / 2;
  // on a phone the books are two across at a readable size, and the rest are reached by scrolling
  const scrolls = cols === 2;
  const dist = scrolls ? gw / (2 * FOV_T * aspect) * 1.04
    : Math.max(gh / (2 * FOV_T * band) * 1.12, gw / (2 * FOV_T * aspect) * 1.1);
  const K = 2 * dist * FOV_T / Math.cos(tilt);                 // desk covered by the height of the screen
  let z = -(centre - 0.5) * K;
  deskRange = 0; deskK = K;
  if (scrolls) {
    const start = -gh / 2 - (top - 0.5) * K, end = gh / 2 - (bottom - 0.5) * K;
    if (end > start) { deskRange = end - start; deskScroll = Math.max(0, Math.min(deskRange, deskScroll)); z = start + deskScroll; }
  }
  if (!deskRange) deskScroll = 0;
  $('intro').style.setProperty('--fade', String(Math.max(0, 1 - deskScroll / (0.18 * K))));
  const look = new THREE.Vector3(0, 0, z);
  const pos = look.clone().add(new THREE.Vector3(0, Math.cos(tilt), Math.sin(tilt)).multiplyScalar(dist));
  return { cols, pos, look };
}
function readView() {
  const aspect = innerWidth / innerHeight;
  single = aspect < 1.05;
  // straight down onto the page: a tilted page keeps the eye correcting for perspective, which is tiring to read
  const tilt = 0, width = single ? W : 2 * W;
  const dist = Math.max((H / 2) / FOV_T * 1.2, (width / 2) / (FOV_T * aspect) * 1.1) / zoom;
  const cx = single ? (viewSide === 'left' ? -W / 2 : W / 2) : 0;
  const look = new THREE.Vector3(cx + pan.x, 0.1, pan.y);
  const pos = look.clone().add(new THREE.Vector3(0, Math.cos(tilt), Math.sin(tilt)).multiplyScalar(dist));
  return { pos, look };
}
let viewSide = 'right';

function placeBooks(immediate) {
  const { cols } = deskView();
  for (const b of books) {
    const p = slotPosition(b.slot, cols);
    b.home = p;
    if (immediate || mode === 'desk') { if (b !== current) b.group.position.copy(p); }
  }
}

function resize() {
  renderer.setSize(innerWidth, innerHeight, false);
  camera.aspect = innerWidth / innerHeight; camera.updateProjectionMatrix();
  placeBooks(false);
  const v = mode === 'reading' ? readView() : mode === 'desk' ? deskView() : null;
  if (v) { camPos.copy(v.pos); camLook.copy(v.look); }
}
addEventListener('resize', resize);
resize();
camera.position.copy(camPos);

// ------------------------------------------------------------------ pointing at things
const ray = new THREE.Raycaster(), mouse = new THREE.Vector2();
function pick(ev) {
  mouse.set((ev.clientX / innerWidth) * 2 - 1, -(ev.clientY / innerHeight) * 2 + 1);
  ray.setFromCamera(mouse, camera);
  const hit = ray.intersectObjects(books.map((b) => b.group), true).find((h) => h.object.userData.book && h.object.userData.book.group.visible);
  return hit ? { book: hit.object.userData.book, point: hit.point } : null;
}
const released = parts.filter((p) => p.released).map((p) => p.roman);
const OUT_NOW = released.length
  ? `${released.length > 1 ? 'Parts' : 'Part'} ${released.join(released.length > 2 ? ', ' : ' and ')} ${released.length > 1 ? 'are' : 'is'} out. Choose a book to read it here.`
  : 'The first part is on its way.';
function caption(book) {
  $('caption').innerHTML = book
    ? `<i>Part ${book.part.roman}</i><b>${book.part.title}</b> &nbsp;&middot;&nbsp; ${book.part.released ? 'click to open' : 'not yet released'}`
    : OUT_NOW + (deskRange ? ' Scroll for the rest.' : '');
}
caption(null);

let down = null, dragged = false;
canvas.addEventListener('pointermove', (ev) => {
  if (mode === 'desk' && down && deskRange) {
    const dy = ev.clientY - down.y;
    if (Math.abs(dy) > 6) dragged = true;
    if (dragged) { deskScroll = down.s - dy / innerHeight * deskK; const v = deskView(); camPos.copy(v.pos); camLook.copy(v.look); }
  } else if (mode === 'desk') {
    const h = pick(ev); const b = h ? h.book : null;
    if (b !== hovered) { hovered = b; caption(b); canvas.style.cursor = b ? 'pointer' : ''; }
  } else if (mode === 'reading' && pinch && touches.has(ev.pointerId)) {
    // two fingers: pinch to zoom
    touches.set(ev.pointerId, { x: ev.clientX, y: ev.clientY });
    if (touches.size === 2) {
      zoom = Math.min(3.2, Math.max(1, pinch.zoom * spread() / pinch.d));
      if (zoom <= 1.01) pan.set(0, 0);
      clampPan(); applyView();
    }
  } else if (mode === 'reading' && down) {
    const dx = ev.clientX - down.x, dy = ev.clientY - down.y;
    if (Math.abs(dx) + Math.abs(dy) > 6) dragged = true;
    if (dragged && zoom > 1.01) {
      const k = (2 * camera.position.distanceTo(camLook) * FOV_T) / innerHeight;
      pan.set(down.px - dx * k, down.py - dy * k); clampPan(); applyView();
    }
  }
});
const touches = new Map(); let pinch = null;
const spread = () => { const [a, b] = [...touches.values()]; return Math.hypot(a.x - b.x, a.y - b.y); };
canvas.addEventListener('pointerdown', (ev) => {
  touches.set(ev.pointerId, { x: ev.clientX, y: ev.clientY });
  canvas.setPointerCapture(ev.pointerId);
  if (touches.size === 2) { pinch = { d: spread(), zoom }; dragged = true; return; }
  down = { x: ev.clientX, y: ev.clientY, px: pan.x, py: pan.y, s: deskScroll }; dragged = false;
});
canvas.addEventListener('pointercancel', (ev) => { touches.delete(ev.pointerId); pinch = null; down = null; });
canvas.addEventListener('pointerup', (ev) => {
  touches.delete(ev.pointerId);
  if (pinch) { if (!touches.size) pinch = null; down = null; return; }
  const was = down; down = null;
  if (!was) return;
  if (mode === 'desk') {
    if (dragged) return;
    const h = pick(ev);
    if (h) (h.book.part.released ? openBook(h.book) : nudge(h.book));
  } else if (mode === 'reading') {
    if (dragged) {
      // a sideways swipe turns the page when the view is not zoomed
      const dx = ev.clientX - was.x;
      if (zoom <= 1.01 && Math.abs(dx) > 50) turn(dx < 0 ? 1 : -1);
      return;
    }
    // one page on screen: the side of the screen decides; two pages: the page that was clicked
    if (single) { turn(ev.clientX > innerWidth / 2 ? 1 : -1); return; }
    const h = pick(ev);
    if (h && h.book === current) turn(h.point.x > current.group.position.x ? 1 : -1);
  }
});
canvas.addEventListener('wheel', (ev) => {
  if (mode === 'desk' && deskRange) {
    ev.preventDefault(); deskScroll += ev.deltaY / innerHeight * deskK;
    const v = deskView(); camPos.copy(v.pos); camLook.copy(v.look); return;
  }
  if (mode !== 'reading') return;
  ev.preventDefault();
  zoom = Math.min(3.2, Math.max(1, zoom * Math.exp(-ev.deltaY * 0.0015)));
  if (zoom <= 1.01) pan.set(0, 0);
  clampPan(); applyView();
}, { passive: false });
function clampPan() {
  const m = 1 - 1 / zoom;
  pan.x = Math.max(-W * 1.1 * m, Math.min(W * 1.1 * m, pan.x));
  pan.y = Math.max(-H * 0.6 * m, Math.min(H * 0.6 * m, pan.y));
}
function applyView() { const v = readView(); camPos.copy(v.pos); camLook.copy(v.look); }

// a book that is not out yet shakes its head
async function nudge(book) {
  if (book.busy) return; book.busy = true;
  await tween(0.5, (e, t) => { book.lift.rotation.y = Math.sin(t * Math.PI * 4) * 0.05 * (1 - t); book.lift.position.y = Math.sin(t * Math.PI) * 0.08; }, (t) => t);
  book.lift.rotation.y = 0; book.lift.position.y = 0; book.busy = false;
}

// ------------------------------------------------------------------ opening and closing
async function openBook(book, startPage) {
  if (mode !== 'desk') return;
  mode = 'moving'; current = book; hovered = null; zoom = 1; pan.set(0, 0); viewSide = startPage > 2 && startPage % 2 ? 'left' : 'right';
  canvas.style.cursor = '';
  document.body.classList.add('reading');
  $('reader').hidden = false;
  fillReaderChrome(book);
  book.s = startPage ? Math.floor((startPage - 1) / 2) : 0;
  book.warm();
  book.rightPage.material.map = book.tex(book.pageOf('right'));
  book.leftPage.material.map = book.tex(book.pageOf('left'));

  // the others slide off into the dark
  for (const b of books) if (b !== book) {
    const from = b.group.position.clone(), away = from.clone().add(new THREE.Vector3(from.x + W / 2, 0, from.z).normalize().multiplyScalar(14));
    tween(0.9, (e) => b.group.position.lerpVectors(from, away, e), (t) => t * t).then(() => { b.group.visible = false; });
  }
  // the chosen one rises, turns once in the air and comes down in the middle
  const from = book.group.position.clone(), mid = new THREE.Vector3(-W / 2, 0, 0);
  const v = readView();
  const c0 = camera.position.clone(), l0 = camLook.clone();
  const fly = tween(1.25, (e, t) => {
    book.group.position.lerpVectors(from, mid, e);
    book.lift.position.y = Math.sin(t * Math.PI) * 1.5;
    book.lift.rotation.y = e * Math.PI * 2;
    book.lift.rotation.x = Math.sin(t * Math.PI) * -0.35;
  });
  const cam = tween(1.9, (e) => { camPos.lerpVectors(c0, v.pos, e); camLook.lerpVectors(l0, v.look, e); });
  await fly;
  book.lift.rotation.set(0, 0, 0); book.lift.position.y = 0;
  // the cover swings over and the book slides so that its spine is in the middle
  await tween(1.05, (e) => {
    book.openAmount = e; book.layout();
    book.group.position.x = lerp(-W / 2, 0, e);
  });
  book.openAmount = 1; book.show();
  await cam;
  applyView();
  mode = 'reading'; updateFolio();
  history.replaceState(null, '', `#part-${book.part.n}`);
}

async function closeBook() {
  if (mode !== 'reading' || flipping) return;
  mode = 'moving';
  const book = current;
  $('contents').hidden = true; $('contents-btn').setAttribute('aria-expanded', 'false');
  document.body.classList.remove('reading');
  zoom = 1; pan.set(0, 0);
  book.s = 0; book.show();
  const v = deskView(), c0 = camera.position.clone(), l0 = camLook.clone();
  const cam = tween(1.7, (e) => { camPos.lerpVectors(c0, v.pos, e); camLook.lerpVectors(l0, v.look, e); });
  await tween(0.8, (e) => { book.openAmount = 1 - e; book.layout(); book.group.position.x = lerp(0, -W / 2, e); });
  book.openAmount = 0; book.layout();
  const from = book.group.position.clone();
  for (const b of books) if (b !== book) {
    b.group.visible = true; const a = b.group.position.clone();
    tween(1.0, (e) => b.group.position.lerpVectors(a, b.home, e), easeOut);
  }
  await tween(0.95, (e, t) => { book.group.position.lerpVectors(from, book.home, e); book.lift.position.y = Math.sin(t * Math.PI) * 0.9; });
  book.lift.position.y = 0;
  await cam;
  for (const [, t] of book.textures) t.dispose(); book.textures.clear();
  current = null; mode = 'desk'; $('reader').hidden = true; caption(null);
  history.replaceState(null, '', location.pathname);
}

// ------------------------------------------------------------------ turning pages
let flipping = false, queued = 0;
scene.add(leaf.mesh);
async function turn(dir, target) {
  if (mode !== 'reading') return;
  const book = current;
  // on a narrow screen one page is shown at a time: move across the spread before turning the leaf
  if (single && target === undefined) {
    if (dir > 0 && viewSide === 'left' && book.pageOf('right')) { viewSide = 'right'; updateFolio(); return glide(); }
    if (dir < 0 && viewSide === 'right' && book.s > 0) { viewSide = 'left'; updateFolio(); return glide(); }
  }
  const to = target !== undefined ? target : book.s + dir;
  if (to < 0 || to > book.spreads || to === book.s) return;
  if (flipping) { if (target === undefined) queued = Math.max(-3, Math.min(3, queued + dir)); return; }
  flipping = true;
  const fwd = to > book.s, from = book.s;
  const top = () => CT + book.T / 2 + 0.003;
  const fa = from / book.spreads, fb = to / book.spreads;
  // the leaf carries the page that is leaving on one face and the page that is arriving on the other
  leaf.front.material.map = book.tex(fwd ? book.pageOf('right', from) : book.pageOf('right', to));
  leaf.backM.material.map = book.tex(fwd ? book.pageOf('left', to) : book.pageOf('left', from));
  for (const d of [0, 1]) { book.tex(book.pageOf('left', to + d * dir)); book.tex(book.pageOf('right', to + d * dir)); }
  leaf.mesh.position.copy(book.group.position);
  leaf.bend(fwd ? 0 : Math.PI, fwd ? top(1 - fa) : top(fa));
  leaf.mesh.visible = true;
  // underneath, the page it uncovers is already in place
  if (fwd) book.rightPage.material.map = book.tex(book.pageOf('right', to));
  else book.leftPage.material.map = book.tex(book.pageOf('left', to));
  if (single) { viewSide = fwd ? 'left' : 'right'; glide(0.7); }
  const speed = queued ? 0.34 : 0.72;
  await tween(speed, (e) => {
    const th = fwd ? e * Math.PI : (1 - e) * Math.PI;
    const k = th / Math.PI;                                  // 0 on the right-hand pile, 1 on the left
    leaf.bend(th, lerp(top(1 - (fwd ? fa : fb)), top(fwd ? fb : fa), k));
  });
  book.s = to; book.show();
  leaf.mesh.visible = false;
  flipping = false; updateFolio();
  if (queued) { const d = Math.sign(queued); queued -= d; turn(d); }
}
function glide(seconds = 0.45) {
  const v = readView(), c0 = camPos.clone(), l0 = camLook.clone();
  return tween(seconds, (e) => { camPos.lerpVectors(c0, v.pos, e); camLook.lerpVectors(l0, v.look, e); });
}

// ------------------------------------------------------------------ the reader's buttons
function fillReaderChrome(book) {
  const p = book.part;
  $('heading').innerHTML = `<i>Part ${p.roman}</i>${p.title}`;
  $('dl-pdf').href = p.pdf || '#'; $('dl-pdf').hidden = !p.pdf;
  $('dl-epub').href = p.epub || '#'; $('dl-epub').hidden = !p.epub;
  // phones and in-app browsers often ignore a forced download, and a new tab can come up blank:
  // there, go straight to the file in this tab and let the phone show or save it
  if (matchMedia('(pointer: coarse)').matches) for (const id of ['dl-pdf', 'dl-epub']) $(id).removeAttribute('download');
  const ol = $('contents'); ol.replaceChildren();
  for (const c of p.chapters || []) {
    if (!c.page) continue;
    const li = document.createElement('li'), b = document.createElement('button');
    b.type = 'button'; b.innerHTML = `<span class="num">${c.n}</span><span>${c.title}</span>`;
    b.addEventListener('click', () => { ol.hidden = true; $('contents-btn').setAttribute('aria-expanded', 'false'); viewSide = c.page % 2 ? 'left' : 'right'; turn(0, Math.floor((c.page - 1) / 2)); if (single) glide(); });
    li.append(b); ol.append(li);
  }
}
function updateFolio() {
  const b = current; if (!b) return;
  const l = b.pageOf('left'), r = b.pageOf('right');
  const shown = single ? (viewSide === 'left' ? l || r : r || l) : [l, r].filter(Boolean).join('–');
  $('folio').textContent = shown ? `${shown} of ${b.pages}` : '';
  $('prev').disabled = b.s <= 0; $('next').disabled = b.s >= b.spreads;
  history.replaceState(null, '', `#part-${b.part.n}/${single ? shown || 1 : Math.max(l, r, 1)}`);
}
$('back').addEventListener('click', closeBook);
$('prev').addEventListener('click', () => turn(-1));
$('next').addEventListener('click', () => turn(1));
$('contents-btn').addEventListener('click', () => {
  const ol = $('contents'); ol.hidden = !ol.hidden; $('contents-btn').setAttribute('aria-expanded', String(!ol.hidden));
});
$('parts').addEventListener('click', (ev) => {
  const n = ev.target.dataset && ev.target.dataset.part;
  if (n) { ev.target.blur(); openBook(books.find((b) => b.part.n === Number(n))); }
});
addEventListener('keydown', (ev) => {
  if (mode !== 'reading') return;
  if (ev.key === 'ArrowRight' || ev.key === 'PageDown' || ev.key === ' ') { ev.preventDefault(); turn(1); }
  else if (ev.key === 'ArrowLeft' || ev.key === 'PageUp') { ev.preventDefault(); turn(-1); }
  else if (ev.key === 'Home') turn(0, 0);
  else if (ev.key === 'End') turn(0, current.spreads);
  else if (ev.key === 'Escape') { if (!$('contents').hidden) $('contents').hidden = true; else closeBook(); }
});

// ------------------------------------------------------------------ every frame
function frame(now) {
  runTweens(now);
  // books on the desk lift a little under the pointer
  if (mode === 'desk') for (const b of books) {
    if (b.busy) continue;
    const want = b === hovered ? 1 : 0;
    b.hover = lerp(b.hover || 0, want, 0.14);
    b.lift.position.y = b.hover * 0.22;
    b.lift.rotation.z = b.hover * -0.05;
  }
  camera.position.lerp(camPos, mode === 'moving' ? 1 : 0.18);
  camera.lookAt(camLook);
  renderer.render(scene, camera);
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);

// a link such as #part-1/40 opens that part at that page
{
  const m = location.hash.match(/^#part-(\d+)(?:\/(\d+))?/);
  const b = m && books.find((x) => x.part.n === Number(m[1]) && x.part.released);
  if (b) openBook(b, m[2] ? Number(m[2]) : undefined);
}
