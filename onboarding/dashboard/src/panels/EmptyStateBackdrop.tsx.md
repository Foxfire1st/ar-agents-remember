# dashboard/src/panels/EmptyStateBackdrop.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/EmptyStateBackdrop.tsx`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T16:02+02:00                           |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                                        |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The shared **empty-state backdrop** (slice 07b polish): a faint, effects-gated boomerang-video
atmosphere behind centered empty-state text, so a panel with nothing to show reads as a quiet,
intentional canvas rather than a blank box. It lifts the engine-room G6 backdrop treatment
(`engine-room/EnclosureProcessMap` + `engineRoomStyles` `backdrop`/`backdropVideo`) out into a reusable
panel primitive. Current production consumers are exactly `DetailPanel` (battle-cruiser clip),
file-viewer `DualPane` (siege-tank clip), and change-set `ChangeSetViewer` (siege-tank clip).

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
All three current production consumers pass `opacity={0.18}`. The component's `0.14` default remains
part of its public contract in source, but no current production caller relies on it.

Any slow zoom and playback cadence belong to the MP4 assets themselves. `EmptyStateBackdrop`
intentionally does **not** mount a Motion wrapper, run `requestAnimationFrame`, or apply a runtime
transform to the backdrop video. Keeping the browser layer static avoids scaling a filtered
video/compositing stack while preserving the existing `objectFit:cover` presentation. Because all three
current empty states share this one component, the static layer contract applies to every consumer.

### Conventions

Co-located Panda `css()` (panels coding-guideline: no global panel CSS), keyed to the same token feel
as the engine-room backdrop. The clip is a **pre-rendered forward+reverse boomerang**, so `loop` is
seamless by construction (first frame == last) — no JS crossfade needed. The SC2 empty-state clips also
bake their slow zoom into the media file and are finalized as 60fps loops (currently 721 frames over
12.016667s). The zoom is baked into those generated frames to peak around scale `1.03`, so this React
component stays static: no Motion import, no wrapper node, no CSS keyframe/transition, and no rAF loop.
The host slot that mounts this component must be a **flex column** so the component's `flex:1` `canvas`
fills the slot. `DetailPanel` mounts it inside `Panel` `fill`; `DualPane` and `ChangeSetViewer` provide
their own bounded empty-state slots. The tracked battle-cruiser and siege-tank clips retain their
`sc2-*-boomerang.mp4` paths.

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

### 2026-07-24 Curator Delta

The backdrop wrapper observes its actual layer visibility. Its looping video pauses while an ancestor
kept-mounted cockpit layer is hidden and resumes when the layer returns, avoiding hidden decoding while
preserving the component's visual treatment.

## Docs References

The engine-room visual language (state colours, motion, glow, the atmospheric backdrop) is the design
authority this backdrop borrows from; the backdrop is explicitly faint, off-state atmosphere, never a
state encoding. No backdrop-for-empty-states page exists in the canonical spec beyond the engine-room
backdrop treatment this reuses.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

This component generalizes the engine-room G6 backdrop into a shared panel; its closest evidence is the
engine-room backdrop styles + their usage, the honest-motion gate it shares, and the three current
empty states that mount it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The engine-room G6 backdrop styles (`backdrop`/`backdropVideo`) this component mirrors. | "export const backdrop =" | dashboard/src/panels/engine-room/backdrop.styles.ts:4-4 |
| The engine-room usage of the same backdrop pattern (effects-gated, aria-hidden video). | "export function EnclosureProcessMap" | dashboard/src/panels/engine-room/EnclosureProcessMap.tsx:67-67 |
| The honest-motion gate that decides whether the backdrop mounts at all. | "export function useShouldAnimate" | dashboard/src/panels/engine-room/useShouldAnimate.ts:19-19 |
| `DetailPanel` mounts the battle-cruiser clip inside `Panel` `fill`, passing `opacity={0.18}`. | "export const DetailPanel" | dashboard/src/panels/detail-panel/DetailPanel.tsx:75-75 |
| File-viewer `DualPane` mounts the siege-tank clip and passes `opacity={0.18}`. | `DualPane` | dashboard/src/panels/file-viewer/DualPane.tsx:90-134 |
| Change-set `ChangeSetViewer` mounts the siege-tank clip and passes `opacity={0.18}`. | `ChangeSetViewer` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:416-478 |
| The static direct-video backdrop: baked media motion is owned by the MP4 asset, while the component only gates and styles a direct `<video>` child. | "export function EmptyStateBackdrop" | dashboard/src/panels/EmptyStateBackdrop.tsx:52-52 |
| The render test pinning children-always-show, effects gating, the direct video child, and absence of `empty-backdrop-zoom`. | "always renders the message children" | dashboard/src/panels/EmptyStateBackdrop.test.tsx:32-37 |

## Cross-Repo References

No meaningful cross-repo references found. This is a self-contained presentational dashboard component.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` rows with exact
  anchors (deleting the unresolvable external URL row); exact non-fixing check returns zero
  findings.

- 2026-07-24T13:17:50Z — Added visibility-gated backdrop video behavior. Verification hash/date remain
  pinned to the pre-commit source stamp.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3 / missing FEUI-L8 history repair: replaced the retired
  Chats/adjutant consumer with the exact three landed consumers (`DetailPanel`, `DualPane`, and
  `ChangeSetViewer`), all using `opacity={0.18}`; the `0.14` default remains supported but has no
  production caller. This explicitly repairs the FEUI-L8 body/reference edit that had no matching
  history entry. Verified against code commit `31f58834f86c0d98e26b0896e099a2403a8729ee`.

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
