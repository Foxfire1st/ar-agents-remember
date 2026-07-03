# dashboard/src/panels/EmptyStateBackdrop.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/EmptyStateBackdrop.tsx`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-24T15:16+02:00                           |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`                                        |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The shared **empty-state backdrop** (slice 07b polish): a faint, effects-gated boomerang-video
atmosphere behind centered empty-state text, so a panel with nothing to show reads as a quiet,
intentional canvas rather than a blank box. It lifts the engine-room G6 backdrop treatment
(`engine-room/EnclosureProcessMap` + `engineRoomStyles` `backdrop`/`backdropVideo`) out into a reusable
panel two empty states share: `DetailPanel`'s no-selection state (battle-cruiser clip) and `Chats`'s
no-session state (adjutant clip).

## Code Commentary

### Logic

A single `EmptyStateBackdrop({ src, children, opacity })` component. The `content` children (the empty-state
message) **always** render in a centered, z-above layer. The video backdrop is conditional: it mounts
only when `useShouldAnimate()` is true — the same honest-motion gate the engine room uses — so under
calm-cockpit (`data-effects=off`) or OS `prefers-reduced-motion` the backdrop is absent entirely (not
just hidden) and the message stands alone. When mounted, a `backdrop` div (`data-testid`
`empty-backdrop`, `aria-hidden`) holds an autoplaying, muted, `playsInline`, `loop`ing `<video>` keyed to
the given `src`. The styling (`backdropVideo`) mirrors the engine room: low opacity, a sepia/amber tint
filter, `screen` blend, and a centered radial mask that vignettes the edges into the stage. The
`backdropVideo` css sets the default faint video opacity to `0.14`; the optional `opacity?: number` prop
overrides that per-caller via an inline `style={{ opacity }}` on the `<video>` (applied only when the prop
is non-null), so a clip that reads darker can be given a touch more presence without changing the default.
The File/Diff viewer's siege-tank backdrops and the Operations `DetailPanel`'s battle-cruiser backdrop
pass `0.18`; the `Chats` adjutant backdrop omits the prop and keeps the `0.14` default.

Any slow zoom and playback cadence belong to the MP4 assets themselves. `EmptyStateBackdrop`
intentionally does **not** mount a Motion wrapper, run `requestAnimationFrame`, or apply a runtime
transform to the backdrop video. Keeping the browser layer static avoids scaling a filtered
video/compositing stack while preserving the existing `objectFit:cover` presentation. Because both empty
states share this one component, the static layer contract applies to **both** backdrops.

### Conventions

Co-located Panda `css()` (panels coding-guideline: no global panel CSS), keyed to the same token feel
as the engine-room backdrop. The clip is a **pre-rendered forward+reverse boomerang**, so `loop` is
seamless by construction (first frame == last) — no JS crossfade needed. The SC2 empty-state clips also
bake their slow zoom into the media file and are finalized as 60fps loops (currently 721 frames over
12.016667s). The zoom is baked into those generated frames to peak around scale `1.03`, so this React
component stays static: no Motion import, no wrapper node, no CSS keyframe/transition, and no rAF loop.
The host slot that mounts this component must be a **flex column** so the component's `flex:1` `canvas`
fills the slot (the `DetailPanel` mounts it inside `Panel` `fill`; `Chats` inside its flex-column
`terminalArea`). The battle-cruiser and adjutant backdrop clips were re-rendered into the same
`sc2-*-boomerang.mp4` paths, so callers keep their existing `src` values.

### Invariants And Boundaries

Pure atmosphere, never state: the video is `aria-hidden` + `pointerEvents:none`, so it carries no
meaning and never intercepts interaction — assistive tech and the calm cockpit see only the message.
The component owns no data and reads no store; it is a presentational wrapper that takes a `src`, the
message as `children`, and an optional `opacity` override. Effects-gating is mandatory (it must consult `useShouldAnimate`, not a CSS-only
switch, because an autoplaying video is not frozen by the `data-effects` CSS layer); gating the whole
backdrop subtree off therefore also stops video playback. Keep the browser backdrop layer static: do not
reintroduce a DOM/CSS/Motion zoom wrapper around this filtered video. If the desired media motion or
framerate changes, re-render the MP4 assets instead. The `.mp4` assets live in
`dashboard/public/assets/` and are referenced by path, not imported.

## Docs References

The engine-room visual language (state colours, motion, glow, the atmospheric backdrop) is the design
authority this backdrop borrows from; the backdrop is explicitly faint, off-state atmosphere, never a
state encoding. No backdrop-for-empty-states page exists in the canonical spec beyond the engine-room
backdrop treatment this reuses.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The engine-room visual-language spec the G6 atmospheric backdrop (reused here) is drawn from. | — | [engine-room-visual-language.html](https://github.com/readeas/agents-remember/blob/main/docs/design/engine-room/engine-room-visual-language.html) |

## Repo-Internal References

This component generalizes the engine-room G6 backdrop into a shared panel; its closest evidence is the
engine-room backdrop styles + their usage, the honest-motion gate it shares, and the two empty states
that now mount it.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The engine-room G6 backdrop styles (`backdrop`/`backdropVideo`) this component mirrors. | L1230-L1247 | [engine-room/engineRoomStyles.ts](engine-room/engineRoomStyles.ts) |
| The engine-room usage of the same backdrop pattern (effects-gated, aria-hidden video). | L82-L88 | [engine-room/EnclosureProcessMap.tsx](engine-room/EnclosureProcessMap.tsx) |
| The honest-motion gate that decides whether the backdrop mounts at all. | L19-L37 | [engine-room/useShouldAnimate.ts](engine-room/useShouldAnimate.ts) |
| The no-selection empty state that mounts this with the battle-cruiser clip (inside `Panel` `fill`), passing `opacity={0.18}`. | L446-L449 | [DetailPanel.tsx](DetailPanel.tsx) |
| The no-session empty state that mounts this with the adjutant clip (inside `terminalArea`); no `opacity` prop, so it keeps the `0.14` default. | L435-L438 | [Chats.tsx](Chats.tsx) |
| The File-viewer no-selection empty state that mounts this with the siege-tank clip, passing `opacity={0.18}` (the clip reads darker). | L105-L109 | [file-viewer/DualPane.tsx](file-viewer/DualPane.tsx) |
| The Diff (change-set) viewer empty state that mounts this with the siege-tank clip, passing `opacity={0.18}`. | L337-L339 | [changeset/ChangeSetViewer.tsx](changeset/ChangeSetViewer.tsx) |
| The static direct-video backdrop: baked media motion is owned by the MP4 asset, while the component only gates and styles a direct `<video>` child. | L6-L12; L31-L40; L51-L59 | [EmptyStateBackdrop.tsx](EmptyStateBackdrop.tsx) |
| The render test pinning children-always-show, effects gating, the direct video child, and absence of `empty-backdrop-zoom`. | L39-L55 | [EmptyStateBackdrop.test.tsx](EmptyStateBackdrop.test.tsx) |

## Cross-Repo References

No meaningful cross-repo references found. This is a self-contained presentational dashboard component.

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-30T00:00:00+02:00 — Operations Integration L5: added an optional `opacity?: number` prop. When supplied it
  overrides the `backdropVideo` css default (`0.14`) via an inline `style={{ opacity }}` on the `<video>`
  (applied only when non-null); default behaviour with no prop is unchanged. Callers whose clip reads
  darker pass a brighter value — the File viewer (`DualPane`) and Diff viewer (`ChangeSetViewer`)
  siege-tank backdrops and the Operations `DetailPanel` battle-cruiser backdrop all pass `0.18`; the
  `Chats` adjutant backdrop keeps the default. Verification metadata pinned until closeout stamps the L5
  commit.
- 2026-06-24T15:16+02:00 — Developer finalized the two SC2 boomerang assets in a video editor after the
  ffmpeg rebuild experiments. Current tracked assets are 1280x720, 60fps, 721 frames, and 12.016667s;
  the slow zoom remains baked into the media and the component remains a static direct-video layer. This
  supersedes the exact 725-frame ffmpeg recipe below as an implementation attempt, not the current asset
  fact. Verification metadata remains pinned until closeout stamps the code commit.
- 2026-06-24T13:48+02:00 — Regenerated both tracked SC2 boomerang assets from the restored original
  24fps clips instead of reprocessing the already-boomeranged output. The new files synthesize the
  60fps forward segment first, bake the slow zoom from `1.0` to `1.03`, then append the reversed frames
  without duplicating the peak frame: 363 forward frames + 362 reverse frames = 725 frames over
  12.083333s, with the loop returning to the first frame. Verification metadata remains pinned until
  closeout stamps the code commit.
- 2026-06-24T13:22+02:00 — Rerendered both tracked SC2 empty-state backdrop assets to exact 60fps loops:
  `sc2-battlecruiser-boomerang.mp4` and `sc2-adjutant-boomerang.mp4` are 1280x720, 725 frames, and
  12.083333s. The component still keeps a direct static `<video>` layer; if cadence needs to change,
  update the media assets rather than adding runtime transforms. Verification metadata remains pinned
  until closeout stamps the code commit.
- 2026-06-24T13:04+02:00 — Baked the empty-state slow zoom into both tracked SC2 MP4 assets and removed
  the runtime Motion/rAF zoom path from `EmptyStateBackdrop`. The component now renders a direct static
  `<video>` inside `empty-backdrop`; there is no `empty-backdrop-zoom` wrapper, no Motion import, and no
  transform/compositor workaround in the component. Verification metadata remains pinned until closeout
  stamps the code commit.
- 2026-06-24T12:28+02:00 — Added compositor/sub-pixel stabilization to the current media-clock zoom
  experiment. The wrapper transform now uses `translate3d(0, 0, 0) scale(...)`; the wrapper has
  `backfaceVisibility` and a `-1px` overscan under the clipping backdrop; the video keeps its
  animation-free role but carries a static `translate3d(0, 0, 0)` plus backface-hidden hints.
  Verification metadata remains pinned until closeout stamps the code commit.
- 2026-06-24T11:47+02:00 — Phase-locked the empty-state backdrop zoom to the video media clock. The
  wrapper still owns the transform and the `<video>` remains static, but the transform is now a Motion
  `MotionValue` updated from `video.currentTime / video.duration` through a `requestAnimationFrame` loop,
  using a cosine yoyo from `scale(1)` to `scale(1.03)` and back. This replaces the free-running 12.000s
  Motion repeat so the zoom reversal tracks the actual boomerang clip duration. Verification metadata
  remains pinned until closeout stamps the code commit.
- 2026-06-24T11:24+02:00 — Moved the slow empty-state backdrop zoom off the `<video>` itself and onto a
  Motion wrapper layer (`empty-backdrop-zoom`). The wrapper now animates a full transform
  `translateZ(0) scale(1)`→`translateZ(0) scale(1.03)` with the same 6s reverse-repeat timing, while
  the video element remains static and continues to own the `objectFit`, tint/filter, blend, and radial
  mask treatment. This preserves the slow zoom but avoids coupling video playback/effects work to the
  animated transform layer. Verification metadata remains pinned until closeout stamps the code commit.
- 2026-06-23T07:39+02:00 — The backdrop `<video>` became a **`motion.video`** (`motion/react`) with a
  slow **12s back-and-forth zoom**: a scale yoyo `1`→`1.03`, 6s each way (`ease: "easeInOut"`, `repeat:
  Infinity`, `repeatType: "reverse"`), declared on the Motion component — **no CSS** per the dashboard
  animation doctrine. The zoom is shared by both empty-state backdrops; scale stays `≥1` so
  `objectFit:cover` never reveals an edge; it rides the same `useShouldAnimate` effects gate (off →
  whole backdrop, and its zoom, absent). Also noted: the battle-cruiser clip was re-sourced (new source
  boomeranged into the same `sc2-battlecruiser-boomerang.mp4` path, so no `src` change). Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-23T04:20+02:00 — Created for slice 07b polish: the shared `EmptyStateBackdrop` — a faint,
  effects-gated boomerang-video atmosphere behind centered empty-state text, lifted from the engine-room
  G6 backdrop (`engineRoomStyles` `backdrop`/`backdropVideo`). Children always render; the `<video>` is
  `aria-hidden` + `pointer-events:none` (pure atmosphere) and mounts only when `useShouldAnimate()` is
  true (absent under calm-cockpit / reduced-motion). The clip is a pre-rendered forward+reverse boomerang
  so `loop` is seamless. Now mounted by `DetailPanel` (battle cruiser) and `Chats` (adjutant).
  Verification metadata pinned until closeout stamps the slice-07b code commit.
