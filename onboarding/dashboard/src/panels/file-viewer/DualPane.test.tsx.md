# dashboard/src/panels/file-viewer/DualPane.test.tsx

| Field | Value |
| ---------------------- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/file-viewer/DualPane.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-06-30 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The component under test — the `empty` backdrop branch, the partnerless-overview branch, and `SidecarSide`. | `DualPane`; `SidecarSide` | dashboard/src/panels/file-viewer/DualPane.tsx:73-88; dashboard/src/panels/file-viewer/DualPane.tsx:90-134 |
| The effects-gated boomerang backdrop whose `video` `src`/`opacity` are asserted. | `EmptyStateBackdrop` | dashboard/src/panels/EmptyStateBackdrop.tsx:52-97 |
| The route overview that governs this test. | `## Route Model` | onboarding/dashboard/src/panels/file-viewer/overview.md:26-58 |

## Update History
- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 6 citation finding(s); scoped recheck clean.

- 2026-06-30T00:00:00+02:00 — Created for operations-integration L5: the vitest/RTL test for `DualPane` covering the siege-tank empty-state backdrop (src `/assets/sc2-siege-tank-boomerang.mp4`, opacity `0.18`, no per-side placeholders), the partnerless-overview markdown full-pane in single and split mode, and the overview placeholder fallback when the body is unavailable. Verification metadata pinned to the task base until closeout stamps the L5 code commit.
