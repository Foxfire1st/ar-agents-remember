# dashboard/src/panels/EngineRoom.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/EngineRoom.test.tsx`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Vitest + `@testing-library/react` render test for slice 5f S5's lifecycle-phase motion: the Engine Room
header flags `data-phase-active` when the selected enclosure is in a human-gated lifecycle phase (sync /
closeout / integration / cleanup, T12–T18), so the room reads as a machine being synced / landed / retired.
Task 11 adds a render assertion that a projected worktree gate surfaces the compact responder in
diagnostics and threads `data-gate-kind` into the canvas. The official-strip coverage now also pins
workspace provider aggregation: same-state CGC providers collapse into one counted chip, mixed CGC states
stay separate, grouped hover titles expose mainline repo labels, and GrepAI remains separately visible. The
leaf-identity regression seeds two browser-dashboard leaves under one parent series so the rail/header must
show the active leaf name first and keep the parent task as context.

## Code Commentary

### Logic

Seeds the real store from a `GALLERY` projection (`applySnapshot`) and renders `<EngineRoom />` with motion
frozen (`data-effects=off`), so the assertion is the structural flag, not the pulse.

- "marks the header phase-active for a human-gated lifecycle phase" — `engine-cleanup-pending` (the
  selected node is `cleanup-pending`) → `engine-room-header[data-phase-active="true"]`.
- "does not mark phase-active for a freshly started worktree" — `engine-bootstrap` (`worktree-started`) →
  `data-phase-active="false"`.
- "renders the projected gate responder..." builds a local cleanup-gate projection, then asserts
  `engine-gate-responder` renders and `enclosure-canvas[data-gate-kind] === "cleanup-approval"`.
- "aggregates same-state official CGC engines..." seeds seven nominal workspace CGCs plus one GrepAI and
  asserts the strip shows one `7 CGC · nominal` aggregate whose title includes the repo labels.
- "keeps official CGC aggregate chips separated by runtime state" seeds nominal, indexing, and down CGCs
  and asserts the strip keeps one chip per state/color while preserving GrepAI as its own chip.
- "renders leaf enclosure identity ahead of the parent series task name" seeds cleanup-pending leaf 15 and
  active leaf 16 under `260610_browser-dashboard`, then asserts the active leaf row/header render before the
  cleanup sibling and the parent task remains secondary context.

### Invariants And Boundaries

Pure render assertion — relies on the shared `test/setup.ts` jsdom stubs. It pins the *which-phases-pulse*
contract (`LIFECYCLE_PHASES`), not the animation; the pulse itself is gated and visual. The official-strip
tests stay inside the top `EngineRoom` strip by seeding `providers` directly on the gallery projection; they
do not assert or reshape the enclosure canvas' workspace-engine rendering.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `EngineRoomHeader` + `LIFECYCLE_PHASES` under test. | `EngineRoomHeader`; `LIFECYCLE_PHASES` | dashboard/src/panels/EngineRoom.tsx:59-66; dashboard/src/panels/EngineRoom.tsx:137-171 |
| `OfficialStrip` groups official workspace providers by label + runtime state and exposes grouped repo labels via hover/title. | `OfficialStrip` | dashboard/src/panels/EngineRoom.tsx:109-132 |
| The local provider fixture helpers and official-strip assertions pin counted same-state CGCs, mixed-state separation, and GrepAI visibility. | `seedOfficialProviders`; "aggregates same-state official CGC engines into one strip chip"; "keeps official CGC aggregate chips separated by runtime state" | dashboard/src/panels/EngineRoom.test.tsx:93-97; dashboard/src/panels/EngineRoom.test.tsx:163-178; dashboard/src/panels/EngineRoom.test.tsx:180-204 |
| The `GALLERY` projection seed + the store `applySnapshot`. | `GALLERY`; `applySnapshot` | dashboard/src/data/store.ts:43-43; dashboard/src/dev/fixtures.ts:146-490 |
| The honest-motion gate the pulse reads. | `useShouldAnimate` | dashboard/src/panels/engine-room/useShouldAnimate.ts:19-37 |

## Current L5I Maintenance

The focused suite now delegates to the real model builder through a spy and proves the performance
boundary: unchanged render inputs and unrelated analytics deltas do not rebuild the room, while a
real `engineProcesses` change does.

## Update History
- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 1 repeated path:start-end Citation objects from 1 same-claim citation group(s) at card line(s) 61; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 4 citation claims; scoped result 0 findings.

- 2026-07-24T13:17:17Z — Curator: recorded the model-memo and narrowed-subscription regression
  coverage; verification fields remain pre-commit.

- 2026-06-24T08:09+02:00 — Engine Room leaf identity: added a two-leaf browser-dashboard render regression proving the rail/header prefer `leafId` while keeping parent `taskName` context and ordering active work before cleanup-pending siblings. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:26+02:00 — Added official-line strip aggregation coverage: same-state workspace CGCs
  collapse into one counted chip, mixed CGC states remain separate, grouped hover titles include repo labels,
  and GrepAI stays separately visible. Verification metadata pinned until closeout stamps the official-strip
  aggregation code commit.
- 2026-06-23T13:45+02:00 — Task 11: added projected gate render coverage for diagnostics
  `GateResponder` and canvas `data-gate-kind`. Verification metadata pinned until closeout stamps the
  task-11 code commit.
- 2026-06-16T03:50 — Created for slice 5f S5: render test pinning the header `data-phase-active` flag for
  the human-gated lifecycle phases (T12–T18). Verification metadata pinned until closeout stamps the S5 commit.
