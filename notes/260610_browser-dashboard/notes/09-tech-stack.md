# 09 — Tech Stack: Each Tool In Detail And How It Fits

| Field | Value |
| --- | --- |
| Topic | The candidate frontend/transport stack, tool by tool (developer request: "present each tool in detail and how it fits into the project") |
| Status | Researched 2026-06-10 against official docs/repos; versions current as of that date; recommendations, not decisions |
| Sources | Web research agent (links inline); raw detail in `raw/recon-workflow-output.json` → `tech` |

## Division Of Labor (the one-line architecture)

**Motion = the living UI. anime.js = the movie prop.** DOM panels + SVG
schematics carry content; canvas only where streaming demands it (charts,
atmosphere); CSS carries the CRT skin globally; shaders only on canvas regions.

---

## Animation

### Motion (motion.dev, formerly Framer Motion) — recommended backbone
- **What/status:** v12.40.0 (2026-05), MIT, ~30M dl/mo. Hybrid engine: WAAPI/
  ScrollTimeline off-main-thread where possible, JS fallback for springs and
  interruptible keyframes. React API: `<motion.div>`, variants + staggerChildren,
  `AnimatePresence` (exit animations), `layout` prop (FLIP layout animation),
  imperative `animate()` with timeline segments, `stagger()`, SVG `pathLength`.
  Recent: `useFollowValue` (spring-following motion values). Tree-shakeable
  (mini 2.3kb / hybrid 18kb). https://motion.dev/docs/react
- **Fit:** the *hard* dashboard problems — panels reflowing when sessions
  spawn/die (`layout`), alarm banners mounting/unmounting (`AnimatePresence`),
  gauges/energy bars tracking telemetry with physical overshoot
  (`useSpring`/`useFollowValue`).
- **Risks:** timeline ergonomics for long cinematic choreography weaker than
  anime/GSAP; some premium components paid (core fully MIT).

### anime.js v4 — recommended choreography/SVG specialist
- **What/status:** v4.4.1 (2026-04), MIT. ESM-first rewrite: `animate()`,
  `createTimeline()` with labels + `.call()`, `createSpring()`, `createScope()`
  (React lifecycle discipline), `svg.createDrawable()` (stroke draw-on),
  `svg.morphTo()`, `createLayout()`, **`scrambleText()`** (v4.4), auto-grid
  stagger. Framework-agnostic. https://animejs.com
- **Fit:** the boot sequence as one labeled timeline ('power-on' → 'systems-check'
  → 'online'); amber schematic draw-on via `createDrawable`; scrambleText on
  critical readout changes (branch names decoding like alien telemetry — a
  one-call signature effect). Practically a checklist of the podracer aesthetic.
- **Risks:** imperative (ref/useEffect discipline in React); single maintainer,
  healthy cadence.

### GSAP — evaluated, third choice
- v3.15; since the Webflow acquisition 100% free incl. DrawSVG/MorphSVG/SplitText.
  Best-in-class nested timelines. **But:** free ≠ OSI open source (custom Webflow
  license, no fork rights), heavier, less React-idiomatic. Choose only on
  existing team familiarity — not our case. https://gsap.com/pricing/

---

## Charts & Graphs

### uPlot — recommended for streaming telemetry
- v1.6.32, MIT, ~50KB canvas micro-library (by a Grafana engineer). Streams 3,600
  pts at 60fps at ~10% CPU / 12MB (Chart.js 40%/77MB, ECharts 70%/85MB); 166k
  points cold-start 25ms. Deliberately unstyled — custom stroke/fill hooks are
  exactly what an amber-on-black CRT theme needs. `setData()` per rAF tick.
  https://github.com/leeoniya/uPlot
- Fit: the event-rate / latency / fuel-gauge time series. Canvas beats SVG
  decisively for streaming (no DOM churn).

### Apache ECharts 6 — selective use only
- v6.1, Apache-2.0; rich built-in gauge/radar types with smooth animation, theme
  JSON dark-mode. Use for one-off cockpit gauges where its gauge type saves
  weeks; never for high-rate streams (7× uPlot CPU). https://echarts.apache.org

### @xyflow/react (React Flow) 12 — recommended for topology
- v12.11, MIT, actively maintained. Custom React nodes/edges, animated edges,
  minimap, elkjs/dagre auto-layout, all default styles CSS variables.
  https://reactflow.dev
- Fit: the worktree/provider topology map — nodes as amber SVG wireframe panels
  with draw-on borders and live status LEDs; animated dashed edges as "energy
  conduits". Alternative: port mc2's hand-rolled canvas renderer (note 07 §4);
  decide by interactivity needs (xyflow wins on selection/zoom/layout for free).

### Rejected: lightweight-charts (trading-desk idiom fights the aesthetic),
visx / Observable Plot (SVG re-render model unfit for streaming; visx viable for
one-shot SVG charts needing glow filters).

---

## Sci-Fi / FUI Techniques

### Arwes — a quarry, not a dependency
- https://github.com/arwes/arwes (7.5k★): frames (SVG corner-bracket panel
  borders), Animator cascades (parent→child enter/exit flows), text effects,
  bleeps (sound manager). **Still 1.0.0-alpha, npm build 16 months stale, not
  React-strict/RSC compatible.** Copy its frame geometry + animator/bleeps
  architecture into ~200-line own equivalents; `@arwes/frames`/`@arwes/bleeps`
  (vanilla) are the only importable candidates.

### CRT layering strategy (the fidelity/effort sweet spot)
- **Global, DOM-safe (pure CSS, zero JS):** fixed pointer-events:none overlay —
  repeating-linear-gradient scanlines, radial vignette, slow compositor-only
  flicker keyframe; chromatic aberration via offset red/cyan text-shadows on
  headings only.
- **Canvas regions only:** real barrel distortion/bloom/phosphor masks via WebGL
  postprocessing (crt-fx: https://github.com/stefanlegg/crt-fx) — wrap the uPlot
  canvas or a background layer. WebGL cannot sample live DOM; keep text in DOM,
  crisp and accessible.
- **Glow:** SVG feGaussianBlur + feMerge stacks for strokes; layered text-shadows
  for type. **Rule: never animate blur radius per frame** — pre-render the glow
  layer and animate opacity, or pulse a CSS `@property` registered variable.

### Boot sequence pattern
One anime.js master timeline: power-on flash → scanline overlay fades in →
schematic draw-on staggered per subsystem → panel frames stagger-reveal →
scrambleText boot readout (+ WebAudio chirps) → live data fades in, SSE
subscribes. Gate on `document.fonts.ready` + first status snapshot (never reveal
empty panels). Play once per session, click-to-skip, instant variant under
`prefers-reduced-motion`.

---

## Supporting Acts

- **WebAudio** — synthesized cockpit audio, zero assets: OscillatorNode + gain
  envelopes for chirps/klaxons (~40 lines). Autoplay policy requires a user
  gesture: make the boot start from a diegetic **IGNITION** button, which
  legitimizes audio for the session. Arwes bleeps as reference.
- **View Transitions API** — now cross-browser (Chrome 111+/Safari 18+/
  Firefox 144+): cockpit mode-switches as `document.startViewTransition` with a
  scanline-mask CRT wipe, ~20 lines, no router dependency.
- **CSS `@property`** — register `--glow-strength`/`--scan-pos` as typed,
  animatable properties: compositor-interpolated alarm pulses and roaming
  scanner lines without per-frame JS.
- **PixiJS v8** — optional single full-viewport background canvas running a cheap
  fragment shader (heat-haze, drifting dust, phosphor noise) *behind* DOM panels.
  Pure atmosphere; pausable under reduced-motion.
- **OffscreenCanvas + Worker** — escape hatch if uPlot must keep scrolling at
  60fps through React render bursts.
- **prefers-reduced-motion as a feature** — ship the "CALM COCKPIT" toggle
  (instant boot, static glows, no audio): accessibility story = long-day
  ergonomics story.

## HyperFrames — adjacent, not core
HeyGen's open-source (Apache-2.0, very active, v0.6.88) **HTML-to-video
renderer**: deterministic frame-seeking headless Chrome + FFmpeg. NOT a UI
framework, no live data — wrong for the dashboard itself. Right for one bonus
feature: **mission replays** — pipe a finished lifecycle's event log through the
same components and render a cinematic MP4 of the run. Shareable agent-session
replays. https://github.com/heygen-com/hyperframes

## Transport — SSE, one multiplexed stream
For a local Python server streaming JSONL tails + status JSON:
- **SSE over WebSocket/polling**: traffic is server→client; the few upstream
  actions are plain POSTs (note 04). `EventSource` auto-reconnects and sends
  `Last-Event-ID` — built-in backfill.
- **FastAPI ≥0.135 ships `fastapi.sse`** (`EventSourceResponse`,
  `ServerSentEvent`, auto keep-alive pings); older: sse-starlette.
- **Design:** snapshot-then-deltas (GET /api/status, then /api/events; or first
  SSE event = full snapshot per connection); event id = JSONL byte offset
  (`events.jsonl:48213`) so reconnect resumes exactly; **one** EventSource with
  named event types fanned out client-side (browsers cap ~6 connections/origin
  on HTTP/1.1 — per-panel streams would starve the tab); `retry: 2000`.
- **Diegetic failure mode:** render `CONNECTING` as a SIGNAL LOST flicker — the
  reconnect story joins the cockpit fiction.
- Open (note 11): where this server lives — standalone sidecar vs shipped as part
  of the package (`agents-remember dashboard` command). Interacts with the 3.0
  posture (note 04).
