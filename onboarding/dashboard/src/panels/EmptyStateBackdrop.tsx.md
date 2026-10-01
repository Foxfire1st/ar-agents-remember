# dashboard/src/panels/EmptyStateBackdrop.tsx

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

## Evidence

### Docs References

The engine-room visual language (state colours, motion, glow, the atmospheric backdrop) is the design
authority this backdrop borrows from; the backdrop is explicitly faint, off-state atmosphere, never a
state encoding. No backdrop-for-empty-states page exists in the canonical spec beyond the engine-room
backdrop treatment this reuses.

### Repo-Internal References

This component generalizes the engine-room G6 backdrop into a shared panel; its closest evidence is the
engine-room backdrop styles + their usage, the honest-motion gate it shares, and the three current
empty states that mount it.

- The engine-room G6 backdrop styles (`backdrop`/`backdropVideo`) this component mirrors. [1]
- The engine-room usage of the same backdrop pattern (effects-gated, aria-hidden video). [2]
- The honest-motion gate that decides whether the backdrop mounts at all. [3]
- `DetailPanel` mounts the battle-cruiser clip inside `Panel` `fill`, passing `opacity={0.18}`. [4]
- File-viewer `DualPane` mounts the siege-tank clip and passes `opacity={0.18}`. [5]
- Change-set `ChangeSetViewer` mounts the siege-tank clip and passes `opacity={0.18}`. [6]
- The static direct-video backdrop: baked media motion is owned by the MP4 asset, while the component only gates and styles a direct `<video>` child. [7]
- The render test pinning children-always-show, effects gating, the direct video child, and absence of `empty-backdrop-zoom`. [8]

### Cross-Repo References

No meaningful cross-repo references found. This is a self-contained presentational dashboard component.
