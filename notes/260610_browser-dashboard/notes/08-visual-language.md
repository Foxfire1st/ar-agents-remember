# 08 — Visual Language: The Podracer Cockpit Grammar

| Field | Value |
| --- | --- |
| Topic | The diegetic visual grammar extracted from the podracer clip, and its semantic mapping onto Agents Remember |
| Status | Direction aligned ("visually we are much more on a wavelength already") |
| Sources | Frame-by-frame scan of `C:/Users/reado/Videos/Inspirations/podracer-clip/` (2,454 frames, 109 sampled by agents + 19 first-hand); `ui-animations.mp4` (secondary); full sequence detail in `raw/recon-workflow-output.json` → `frames` |

## The Core Principle (what makes this better than generic FUI)

**State is carried by color and silhouette, never by chrome.** The same gauge
geometry renders amber when healthy, crimson when failing, skeletal dark-red when
dormant, mint-green when freshly online. No badges, no toasts. Glyph captions
appear only when something needs explaining — progressive disclosure on anomaly.

## The State Grammar (frame-verified)

| State | Visual | Color anchors |
| --- | --- | --- |
| Dormant / off | thin skeletal outlines only, screen face black | brick red `#7A1010` on brown-black |
| Healthy / nominal | 1–3px wireframe schematic + faint polar-grid web | amber/gold `#E8A020` |
| Progress / charge | striped bar filling bottom-up *inside* the engine outline | cyan-blue `#5FA8FF`–`#6EC1F0`, fine horizontal scanline hatching |
| Alarm / failure | **whole-silhouette pulsing red outline** on the affected unit + alarm wedge + caption box lights | red `#FF2A18`–`#FF3322`, pulse ~2–3/s (cap ours at ≤3 flashes/s, WCAG 2.3.1; 1Hz breathe reads more cinematic) |
| Power transfer / recovery | orange glowing capsule-dots streaming behind a yellow C-bracket arrow; bars rebalance; capsules fade one-by-one (~one per 8–10 frames) | orange `#FF8C2A`, yellow bracket |
| Boot / online | dormant → ignition sigil fades up (~1s) → repaint to mint-green in **~0.4s** → peripheral segmented arc tiles light one-by-one at **~0.5s cadence** like a circular loading bar | green `#7CFA9C` over `#DFFFE8`, arc tiles `#FFD23F` |
| Failure power-down | staged fade: content vanishes → chrome thins → black, over ~3s | all-red recolor of the same geometry first |

Plus the **physical layer** (the cockpit's second voice): jewel-tone backlit
square buttons (cyan `#2FB8C8` / amber `#FFA62E` / orange-red `#FF5A22`), red
dome lamps with bloom, chrome toggles, the striped emergency lever — and the
key diegetic trick: a **dimmed jewel = de-energized channel** (the cyan button
visibly dims between the two ignition-panel visits). Gate/approval controls
should borrow this: deliberate, guarded, mechanical.

Texture: CRT bloom/halation, convex-glass specular, slight barrel distortion,
weathered bezels, visible cabling. Lived-in, not clean.

## Key Reference Sequences (frame numbers in the clip)

- `216112–216248` red alert wedge gauge + overheat blotches (alarm vocabulary)
- `216460–216618` boot: dead gauge → sigil ignition → green/blue arcs accrete
- `216895–216978` failure power-down beside a burning-engine schematic
- `217014–217126` **anchor**: dual-engine screen — fire flicker left, blue bar
  fills right, red silhouette alarm peaks as remedy completes (best: 217026/217044/217098/217116)
- `217470–217578` fault clears + orange capsule power-transfer animation
- `218160–218260` **hero boot**: amber → green repaint + sequential gold arc ring
  (best: 218193/218211/218229/218256)

## Semantic Mapping (the design thesis)

| Podracer | Agents Remember |
| --- | --- |
| The pod, twin engines + energy binder | A worktree's provider stack: **CGC engine + GrepAI engine** (exactly two!), bound by the coordination runtime |
| Blue fill inside engine outline | Indexing/seed progress per provider |
| Engine fire + red silhouette | `empty` / `backend-unreachable` / crash-loop — the *invisible* fire of the 2026-06-09 incident (green over a 0-node graph for 3 days) made visible |
| Orange capsule transfer | Recovery actions: seed import, refresh-all fallback, memory carryover, ledger fast-forward |
| Boot sequence + arc tiles | `worktree_start` async setup — **`setup-progress.json` already provides the exact data**: `completedPhases[]` light the tiles, `currentPhase` pulses, `seedFallback` = the visibly-slow boot, heartbeat age = freshness flicker |
| Master caution lamps / hand on levers | Attention queue / gate approvals (notes 04, 06) |
| The race course | l-01 lifecycle phases; a gate = the race pauses on your input |

Narrative frame (Territory Studio's transferable lesson: every graphic answers a
real operator question; motion designed before static comps; one grid, one glow
language so the cockpit feels like one machine): **each agent session is a
podrace; a provider fire mid-build is Anakin fixing the pod in prod** — which is
the clip that started this. The honest version *is* the quirky version.

## Secondary Inspiration: `ui-animations.mp4`

Modern dark-dashboard craft to keep alongside the diegetic layer: glowing dashed
line-traces, neon bars with bloom, dotted line charts, "Copilot Analysis" alert
cards. Take from it the *smoothness standard* (buttery 60fps chart motion) and
the restraint of dark surfaces — not its corporate styling.
