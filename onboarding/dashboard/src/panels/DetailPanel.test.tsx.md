# dashboard/src/panels/DetailPanel.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/DetailPanel.test.tsx`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-26T20:18+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Vitest + Testing Library coverage for the `DetailPanel` gate surface. Task 11 asserts the durable gate
renders the shared Respond control with its full request packet and that a proto-gate-only lifecycle uses
the same surface. Slice 6g adds master-series
navigation coverage: the master overview + a sub-task index pinned above the description (with an
in-section copy), drill-in into a slice reader + return via the header breadcrumb, GFM markdown (a
table) rendering, and cross-master "→" / parent-breadcrumb lifecycle jumps.
The promoted-leaf regression covers a selected leaf lifecycle whose visible label comes from the
enclosure while the rendered body comes from a real `subTask` task document. Task 17 adds coverage for
folder-keyed `analytics.series` selection, selected root-task lifecycle mapping through enclosure
`taskId`/`taskName`, structured creation-order sorting, and task-specific leaf labels. The corrected
Task 17 assertions expect the child task document `id` in authored leaf labels while keeping creation
time as the row-order source; parent sub-task `number` is fallback data only. The progress-count
regression covers a leaf whose backend projection reports
`40/42` nested progress but whose visible top-level implementation-step summary is `6/7`. A lifecycle
identity regression covers both live leaf shapes: a leaf lifecycle that carries parent `taskName`
metadata but no projected task doc must not render the parent master, and a leaf lifecycle with its own
projected `TaskDocNode` must render that leaf body. Task 17 follow-up coverage also proves unbound
planning leaf/master task documents render through `taskdoc:<docPath>` selection, that lifecycle-bound
selected masters can still open authored sibling leaves from the full projected document pool, that a
missing authored sibling stays static, and that rendered step and code-example labels include their
structured ids.
The promoted-leaf fixture now also includes the parent master document and matching series sub-task
metadata so a direct enclosure-opened leaf can prove its sticky parent/root backlink. Task 21 adds a
master-reader aggregate-token regression: the series fixture carries `seriesTokenTotal`, and the panel
must render both the `series tokens` label and formatted token value. Task 33: every `WorkspaceProjection`
fixture seeded here — the inline objects and the `seedProjection` builder — now sets the required
top-level `activeWorktreeGroups: []`, so the seeded snapshots satisfy the current projection contract
(the field is required because the server always serves it); no DetailPanel assertion depends on its
value.

## Code Commentary

### Logic

Seeds a `GALLERY` fixture into `dashboardStore` (`applySnapshot`) and renders `<DetailPanel selectedId=…>`.
Task 11 gate cases: the `gate-review` scene renders `gate-review` + `gate-respond-open`, no old
decision-verb buttons, and the opened dialog contains the Task 19 human-readable request preview
(`Changed paths`) instead of the raw JSON key; the `blocked` scene
(proto-gate `ask`, no durable gate) renders `gate-banner` through the same Respond surface.

The slice-6g cases build a master+slice projection with a local `taskDoc` factory + `seedSeries`
helper (a folder-keyed `SeriesNode` master in `analytics.series`, a `subTasks` index, a cross-master
"→" row with `linkedLifecycleId`, and one authored slice in `analytics.taskDocuments`). They assert:
the index renders pinned above the description (`compareDocumentPosition`) with the in-section copy
kept; clicking a sub-task opens its `TaskReader` and the header breadcrumb returns; a GFM table renders
as a real `<table>` (not raw pipes); the "→" row calls `onOpenLifecycle` with the target lifecycle; and
`seedSeriesOrdering` proves rows sort by `createdAt` while rendering task-specific `01.` / `99.` numbers
instead of generated `1.` / `2.` counters. `seedSeries` can also attach an enclosure whose `taskId` is the root
selected lifecycle id and whose `taskName` is the folder-keyed series id; the regression asserts that
this selection renders master objective/sections instead of the master-less slice list or no-doc
fallback. The paired leaf regressions deliberately use the same parent `taskName` mapping on a non-root
lifecycle: one moves the only slice doc to another lifecycle and expects the no-doc fallback rather
than master content, and one keeps a direct `TaskDocNode` for the selected lifecycle and expects the
leaf body. Together they document that `taskName` is parent/root identity metadata for leaf lifecycles,
not their content selector.
`nestedProgressSteps` simulates the inflated nested-progress case, and the corresponding regression
asserts that the master sub-task row and opened reader progress fill both show `6/7`, never `40/42`.
`seedTaskDocuments` builds document-only projections with no lifecycles/enclosures, proving planning
docs remain readable before worktree creation. `seedProjection` also supports a lifecycle-bound selected
master regression: selected master `docs` may contain only the master itself, so the component must use
the full projected sibling pool to make the authored leaf row a button. The paired missing-leaf test
asserts the same index row remains static when no sibling JSON task document exists. The id-display
regression expects `S11 — ...`, `S11.1 — ...`, and `E4 — ...` labels in rendered task content, and
rejects title-only rows. The aggregate-token regression reads the same `seedSeries` fixture and asserts
the master overview exposes an accessible `1500 aggregate series tokens` node plus the formatted
`1,500 tok` value.
`seedPromotedLeaf` builds the corrected leaf case: the selected lifecycle id is still the promoted
ULID-like id, the enclosure carries `leafId = 16_engine-room-stack-entry-height`, and
`analytics.taskDocuments` contains both an unrelated parent/master-task document and the selected
leaf's real `subTask` document. The test asserts that the detail panel renders the leaf title,
objective, step, and freeform section while rejecting parent-doc text, raw lifecycle id text, and
`series-contract.md` schema strings. The paired backlink test uses the same fixture, clicks
`master-parent-link`, and expects navigation to the parent master document's typed `taskdoc:` key.

### Invariants And Boundaries

Component-level (jsdom) — no real backend. Reuses the
`GALLERY` bench fixtures (`gate-review`/`blocked`) so the test data matches the dev bench.
The promoted-leaf case is a component contract only: it proves the panel does not use contract text as
readable task content, but it does not exercise the Python reader that populates `analytics.taskDocuments`.
The planning-doc cases are also component-level; observer reader tests prove projection of unbound and
archived documents.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The drawer under test renders selected series from `analytics.series`, maps only selected root-task lifecycles through enclosure `taskId`/`taskName`, displays child task-document id labels in creation order, and shows top-level task-doc progress. | L305-L452; L496-L508; L553-L556; L717-L785 | [DetailPanel.tsx](DetailPanel.tsx) |
| The task/series fixture factories include `TaskDocNode.createdAt`, `SeriesNode`, optional task-id/name enclosure mapping, and a nested-progress fixture where top-level progress intentionally differs from backend `stepsDone/stepsTotal`. | L21-L57; L77-L190 | [DetailPanel.test.tsx](DetailPanel.test.tsx) |
| The ordering assertion pins creation-time placement while expecting child task-document id labels and rejecting generated local counters. | L671-L678 | [DetailPanel.test.tsx](DetailPanel.test.tsx) |
| The top-level progress regression rejects a `40/42` nested count in both the master row and opened leaf reader, expecting `6/7`. | L660-L676 | [DetailPanel.test.tsx](DetailPanel.test.tsx) |
| The aggregate-token regression pins the master reader's `series tokens` display from `seriesTokenTotal`. | L676-L683 | [DetailPanel.test.tsx](DetailPanel.test.tsx) |
| The typed taskdoc selection regressions cover unbound planning leaf/master docs, lifecycle-bound master sibling-pool navigation, static missing-leaf rows, and structured step/example id display. | L405-L458; L460-L550; L552-L592 | [DetailPanel.test.tsx](DetailPanel.test.tsx) |
| The root-task lifecycle regression proves enclosure `taskId`/`taskName` selects the folder-keyed series master for the master row. | L678-L690 | [DetailPanel.test.tsx](DetailPanel.test.tsx) |
| The missing-doc leaf lifecycle regression proves parent `taskName` alone does not render the master for leaf rows. | L692-L704 | [DetailPanel.test.tsx](DetailPanel.test.tsx) |
| The direct leaf lifecycle regression proves a projected leaf `TaskDocNode` wins over parent `taskName` mapping, preventing leaf sidebar rows from rendering the master. | L706-L718 | [DetailPanel.test.tsx](DetailPanel.test.tsx) |
| The promoted-leaf fixture now carries parent master/series metadata, and the backlink regression proves `master-parent-link` targets the parent master task document. | L301-L399; L766-L778 | [DetailPanel.test.tsx](DetailPanel.test.tsx) |
| The shared hierarchy helper resolves the parent link from projected series sub-task refs. | L45-L58; L85-L88 | [taskHierarchy.ts](../data/taskHierarchy.ts) |
| The helper that separates visible lifecycle labels from direct task-doc filtering. | L1-L63 | [taskIdentity.ts](../data/taskIdentity.ts) |
| The gate-review test opens the shared responder and expects the rendered preview label `Changed paths`. | L408-L417 | [DetailPanel.test.tsx](DetailPanel.test.tsx) |
| The shared responder rendered by the gate cases. | L1-L124 | [GateResponder.tsx](GateResponder.tsx) |
| The `gate-review` / `blocked` fixtures seeded. | L151-L290 | [dev/fixtures.ts](../dev/fixtures.ts) |

## Update History

- 2026-06-28T07:30+02:00 — Task 33: the inline/`seedProjection` `WorkspaceProjection` fixtures gained
  `activeWorktreeGroups: []` for the new required projection field; no behavioural assertion change.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 series token rollup: `seedSeries` now carries
  `seriesTokenTotal`, and a regression asserts the master reader renders the aggregate label, formatted
  value, and accessible label. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-25T07:39+02:00 — Task 19 gate preview assertion: the gate-review test now expects the
  human-readable `Changed paths` label in `gate-request`, pinning the rendered preview over raw JSON
  field names. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-24T18:11+02:00 — Corrected Task 17 live-data numbering tests: fixtures now give authored leaf
  task docs explicit `id` values and assertions pin child-id display, with parent refs left as fallback
  data. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:02+02:00 — Corrected Task 17 numbering regressions: master and unbound-master leaf
  assertions now expect structured numeric labels (`99.`, `01.`) while rejecting generated `1.`/`2.`
  counters. The later 18:11 entry pins the child task-id source. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-24T17:51+02:00 — Task 17 parent-link regression: the promoted-leaf fixture now includes the
  parent master document and structured series metadata, and a new assertion proves an enclosure-opened
  leaf links back to the parent master task document via a typed `taskdoc:` key. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T17:20+02:00 — Task 17 master-navigation/sidebar-scope tests: added coverage that a
  lifecycle-bound selected master opens an authored sibling leaf from the full projected pool, while a
  missing sibling remains static. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:33+02:00 — Task 17 task-document-first reader tests: added document-only projections for
  unbound planning leaf/master docs selected by `taskdoc:<docPath>`, and coverage that rendered
  steps/examples show structured ids with titles. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-24T15:37+02:00 — Task 17 live-projection regression update: test fixtures now mirror the
  browser stream by distinguishing the root task lifecycle (`lifecycle.id === taskId`) from leaf
  lifecycle rows (`taskId` still names the parent), and coverage includes the missing-projected-doc leaf
  case that must not render the parent master. Verification metadata pinned until closeout stamps the
  follow-up code commit.
- 2026-06-24T15:23+02:00 — Task 17 lifecycle-leaf regression: added coverage for the parent
  `taskName` metadata case on a selected leaf lifecycle with its own direct task doc, proving the leaf
  body renders and the master body does not. Verification metadata pinned until closeout stamps the
  follow-up code commit.
- 2026-06-24T13:59+02:00 — Task 17 progress-count regression: `seedSeries` can override the slice doc,
  `nestedProgressSteps` models `40/42` nested backend progress over seven top-level steps, and the test
  now proves the master row plus reader progress fill show `6/7`. Verification metadata pinned until
  closeout stamps the follow-up code commit.
- 2026-06-24T12:53+02:00 — Master selection follow-up: `seedSeries` can attach a selected task-id
  enclosure, and a regression now proves that `DetailPanel` maps through enclosure `taskName` to render
  master content instead of the no-doc fallback. Verification metadata pinned until closeout stamps the
  follow-up code commit.
- 2026-06-24T12:21+02:00 — Task 17 detail-panel regression: tests now seed masters through
  `analytics.series`, include `createdAt` on task/series rows, assert oldest-first ordering with local
  ordinals, and account for the new top Progress copy of task steps. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Promoted leaf task-document regression: added/updated the selected leaf
  scenario so DetailPanel renders the real `subTask` JSON document for
  `16_engine-room-stack-entry-height`, rejects parent-task content, and rejects `series-contract.md`
  strings. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T13:45+02:00 — Task 11: replaced the old `/api/actions` gate-decision assertions with
  Respond-surface assertions (full request packet, no decision verb buttons, proto ask uses same
  surface). Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-21T02:44+02:00 — Slice 6g: added master-series navigation tests (pinned + in-section sub-task index, drill-in + header-breadcrumb return, GFM table rendering, cross-master "→" / parent-breadcrumb `onOpenLifecycle` jumps) + a `taskDoc` factory and `seedSeries` helper. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-18T15:00 — Created for task 6 slice 6c Part B: the Gate Review drawer tests (render / POST-recorded / 409-no-open-gate / proto-gate fallback). Verification metadata pinned to the task base until closeout stamps the 6c Part B code commit.
