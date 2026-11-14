# dashboard/src/panels/file-viewer/DualPane.test.tsx

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

The vitest + Testing-Library test for the File Viewer's reusable `DualPane`. It pins the two whole-pane
branches L5 added ahead of the split: the **siege-tank empty-state backdrop** shown before anything is
opened, and the **partnerless-overview** rendering that puts a code-less markdown doc's prose full-pane
(in both single and split mode) instead of an empty code split — with a fallback to the no-code-partner
placeholder when an overview's body is unavailable.

## Code Commentary

### Logic

`afterEach(cleanup)` follows each direct render with explicit props. These fixtures contain no linked document requiring resolution; shared document and media children can load supplied addresses. Suite 1 (`empty-state backdrop`) renders
`code={null} sidecar={{ state: "empty" }} split={true}` and asserts: the prompt text "Select a code file"
is present; the `empty-backdrop` testid's `<video>` has `src` `/assets/sc2-siege-tank-boomerang.mp4`; its
inline `style.opacity` is `"0.18"` (the brighter wash over the shared 0.14 default); and **no**
`pane-placeholder` node exists (the backdrop replaces the per-side placeholders). Suite 2
(`partnerless overview rendering`) has three cases: `{ state: "markdown", body }` with `split={false}`
renders the `sidecar-pane` markdown full-pane (body prose present, no `pane-placeholder`); the same with
`split={true}` still renders the markdown full-pane (not an empty code split); and `{ state: "overview" }`
with `split={true}` falls back to a `pane-placeholder` whose text includes "Overview".

### Invariants And Boundaries

The source renders DualPane directly with explicit props and makes no direct file API request; this does not establish a no-network boundary for its shared children. It
encodes the L5 branch order: an `empty` sidecar shows the effects-gated `EmptyStateBackdrop` (the
`empty-backdrop` testid only exists when `useShouldAnimate` is true, the jsdom default), and a partnerless
`markdown` sidecar (`code === null`) renders `SidecarSide` full-pane regardless of `split`. Assertions inspect `empty-backdrop`, `sidecar-pane`, `pane-placeholder`, the video source and the `0.18` opacity.

## Evidence

### Repo-Internal References




- The component under test — the `empty` backdrop branch, the partnerless-overview branch, and `SidecarSide`. Anchor: `DualPane` `SidecarSide` [1]


- The effects-gated boomerang backdrop whose `video` `src`/`opacity` are asserted. [2]
