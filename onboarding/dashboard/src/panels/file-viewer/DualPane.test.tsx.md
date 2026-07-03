# dashboard/src/panels/file-viewer/DualPane.test.tsx

| Field | Value |
| ---------------------- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/file-viewer/DualPane.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-30 |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a` |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview | `overview.md` |

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

`afterEach(cleanup)`; no `fetch` stub is needed because `DualPane` is presentational — every test renders
it directly with explicit `code` / `sidecar` / `split` props. Suite 1 (`empty-state backdrop`) renders
`code={null} sidecar={{ state: "empty" }} split={true}` and asserts: the prompt text "Select a code file"
is present; the `empty-backdrop` testid's `<video>` has `src` `/assets/sc2-siege-tank-boomerang.mp4`; its
inline `style.opacity` is `"0.18"` (the brighter wash over the shared 0.14 default); and **no**
`pane-placeholder` node exists (the backdrop replaces the per-side placeholders). Suite 2
(`partnerless overview rendering`) has three cases: `{ state: "markdown", body }` with `split={false}`
renders the `sidecar-pane` markdown full-pane (body prose present, no `pane-placeholder`); the same with
`split={true}` still renders the markdown full-pane (not an empty code split); and `{ state: "overview" }`
with `split={true}` falls back to a `pane-placeholder` whose text includes "Overview".

### Invariants And Boundaries

The test is pure-render — no network, no store — so it depends only on `DualPane`'s prop contract. It
encodes the L5 branch order: an `empty` sidecar shows the effects-gated `EmptyStateBackdrop` (the
`empty-backdrop` testid only exists when `useShouldAnimate` is true, the jsdom default), and a partnerless
`markdown` sidecar (`code === null`) renders `SidecarSide` full-pane regardless of `split`. Assertions key
off stable hooks (`data-testid` `empty-backdrop` / `sidecar-pane` / `pane-placeholder`, the video `src`
path, and the `0.18` opacity), so renaming those or changing the clip/opacity is a breaking change.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test — the `empty` backdrop branch, the partnerless-overview branch, and `SidecarSide`. | L73-L134 | [DualPane.tsx](DualPane.tsx) |
| The effects-gated boomerang backdrop whose `video` `src`/`opacity` are asserted. | L51-L83 | [EmptyStateBackdrop.tsx](agents-remember/dashboard/src/panels/EmptyStateBackdrop.tsx) |
| The route overview that governs this test. | — | [overview.md](overview.md) |

## Update History

- 2026-06-30T00:00:00+02:00 — Created for operations-integration L5: the vitest/RTL test for `DualPane` covering the siege-tank empty-state backdrop (src `/assets/sc2-siege-tank-boomerang.mp4`, opacity `0.18`, no per-side placeholders), the partnerless-overview markdown full-pane in single and split mode, and the overview placeholder fallback when the body is unavailable. Verification metadata pinned to the task base until closeout stamps the L5 code commit.
