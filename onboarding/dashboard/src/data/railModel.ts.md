# dashboard/src/data/railModel.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/railModel.ts`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T23:40+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Builds the canonical Chats hierarchy from real sprint, master, and leaf task documents, then places
each live hosted occupant at its task-document-and-role seat. Runtime spawn ancestry is retained only
as a separate diagnostic tree.

## Code Commentary

### Logic

`buildRailModel` indexes task documents by canonical reference, derives sprint/master/leaf sections,
and joins catalog sessions through `session.taskDocumentRef`. Role-altitude rows remain stable across
occupant replacement. `buildSpawnTree` deliberately projects runtime provenance outside the default
Chats hierarchy. Row layout exposes a fixed segment contract so long labels are clipped in one line.

### Conventions

Task containment supplies hierarchy; role supplies seat altitude and ordering. Runtime ids identify
the focused occupant only.

### Invariants And Boundaries

- Default Chats nesting is task-document hierarchy, not spawn ancestry.
- A row's structural address survives replacement.
- Missing task bindings do not get guessed into a task branch.
- Row titles remain single-line; status is the only declared elidable segment.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Structural rail nodes carry canonical task-document references. | `RailLeafCluster` | dashboard/src/data/railModel.ts:83-119 |
| The default rail joins sessions to real task topology. | `buildRailModel` | dashboard/src/data/railModel.ts:361-387 |
| Runtime provenance is a separate diagnostic projection. | `buildSpawnTree` | dashboard/src/data/railModel.ts:414-436 |
| The row segment contract keeps status as the only elidable segment. | `ROW_SEGMENTS` | dashboard/src/data/railModel.ts:442-443 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T23:40+02:00 — No content impact: the lint-only split of `buildRailModel` into
  document initialization, altitude-specific session classifiers, and section materialization
  preserves the task-document hierarchy, role-altitude placement, unattached refusal, and separate
  spawn-provenance contracts already stated above. Verification metadata remains pinned until
  governed closeout.

- 2026-08-11T19:58+02:00 — Aligned the current data-contract card for `railModel.ts` with task-document identity, qualified seat state, and terminal projections represented by this source.
- 2026-08-10T09:45+02:00 — 260731-EFA-L9 curator repair: updated rail-model test and build citations.


- 2026-08-10T04:39+02:00 — 260713-TES-L6: documented sprint-qualified command groups and the
  migration-only legacy command-seat bucket. Verification metadata remains pinned until closeout
  stamps the code commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T02:35:41+02:00 — W3-B04 curator: curated 8 table citations and 10 prose citations (18 total), supplying exact anchors and paths; the scoped fixer generated all final extents.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the fix-round review-N1 triage change.
  `waitingSeats` (the palette's question-triage list) now filters with
  `sessions.ts`'s `sessionHasPendingInteraction` — the singular parent slot OR a non-empty
  multiplexed sub-agent list — so a seat blocked SOLELY on a sub-agent approval is listed instead of
  going dark; newest-first ordering is unchanged. Source is uncommitted; closeout re-stamps
  verification.

- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3: moved the `SessionList` comparison into explicit
  historical provenance and recorded the landed `buildRailModel` → `SessionsView` → `SessionRail`
  ownership chain. Verified against code commit `31f58834f86c0d98e26b0896e099a2403a8729ee`.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S4 (R5/R6/R8/R9/R12/R13/R16/R17, incl. the
  review finding-4 fix making the longest-waiting tiebreak hold in every attention class): the
  pure ruled-hierarchy rail model — flat command spine, per-leaf clusters with deterministic
  active-first sort, completed folders, spawn-edge provenance tree, row-anatomy invariants +
  tooltip truth, fleet-attention rollup with zero-state suppression and jump priority, held-gate /
  two-state-brief / critical-bus projection joins, smart-default focus, and question triage.
  Verification metadata pinned to the leaf base until closeout stamps the L2 code commit.
