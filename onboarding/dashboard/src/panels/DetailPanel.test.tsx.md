# dashboard/src/panels/DetailPanel.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/DetailPanel.test.tsx`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T10:05+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Vitest + Testing Library coverage for the `DetailPanel` gate surface. Task 11 asserts the durable gate
renders the shared Respond control with its full request packet; the proto-gate/ask-only regression asserts
attention detail no longer renders the obsolete task-local response box. Slice 6g adds master-series
navigation coverage: the master overview + a sub-task index pinned above the description (with an
in-section copy), drill-in into a slice reader + return via the header breadcrumb, GFM markdown (a
table) rendering, and cross-master "→" / parent-breadcrumb lifecycle jumps.
The promoted-leaf regression covers a selected leaf lifecycle whose visible label comes from the
enclosure while the rendered body comes from a real `subTask` task document. Task 17 adds coverage for
folder-keyed `analytics.series` selection, selected root-task lifecycle mapping through enclosure
`taskId`/`taskName`, structured creation-order sorting, and task-specific leaf labels. The corrected
Task 17 assertions expect the child task document `id` in authored leaf labels while keeping creation
time as the row-order source; parent sub-task `number` is fallback data only. The progress-count
regression covers a leaf whose backend projection reports 46/49 while its visible top-level
implementation-step summary is 6/7; both rendered progress surfaces must preserve the projected
counters. A lifecycle
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
value. The doc-reader change-set bar coverage adds rendering a leaf doc reader with `onOpenChangeSet`
shows a single **committed** button whose click opens the leaf target `{repo, master, leaf, mode}`; a
master doc reader shows a **series** button; a leaf whose enclosure is live (seeded `enclosures` +
`activeWorktreeGroups`) shows both **committed** + **working**; and with no `onOpenChangeSet` wired the bar
is omitted entirely. The viewed-leaf reporting coverage adds a `DetailPanel viewed-leaf reporting` describe block that pins the
new `onViewLeaf` prop: a master overview reports `undefined`, drilling into a sub-task reports the leaf's
qualified id (`repo-a/series/1`, not the master), the breadcrumb back clears it again, and a
directly-opened leaf doc reports its own `repo/master/leaf-id`.

## Code Commentary

### 260707-HFX2 On-Demand Task Bodies

The shared fetch doubles used by the detail-panel and notes integrations now recognize
`/api/task-document?path=...` and return the matching projected fixture as a full document before
falling through to change-set or notes responses. This is test-harness plumbing for the reader's new
on-demand body request; it keeps all pre-existing interaction assertions meaningful without making a
real network request.

### 260707-HFX2 R7 Reader Completion

The on-demand reader tests now distinguish the bounded summary from a fetched full body. One async
case first observes the summary, then verifies fetched objective, requirements, decision, and
reference content while the implementation step remains single-rendered. A second case returns 404,
waits for the explicit unavailable-body message, and proves the summary remains visible. Existing
step-label assertions were corrected from two copies to one after removal of the duplicate Progress
section.

### 260712-TRH Body-First Reader Regression

A lifecycle-backed reader test holds `/api/task-document` unresolved while an active enclosure,
change-set handler, and notes-capable reader are present. It proves the summary and loading status are
visible, the body endpoint is the only request started, and neither notes nor any change-set endpoint
runs ahead of it. After resolving the body, the test proves complete content replaces the summary and
both ancillary request classes resume. The complete-body case now covers objective, requirements,
design, code examples, decisions, open questions, references, freeform sections, and exactly one
implementation-step row. A cache case proves unchanged path/revision reuse and refetch on revision
change. Existing change-set cases await hydration before asserting their buttons.

### Logic

Since the enclosure-fixture update, the local `enclosure(...)` fixture defaults the REQUIRED `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags to `true` (a live worktree) — DetailPanel itself does not filter on existence, so no assertion changed.

Seeds a `GALLERY` fixture into `dashboardStore` (`applySnapshot`) and renders the selected detail panel.
The gate cases: the `gate-review` scene renders `gate-review` + `gate-respond-open`, no old
decision-verb buttons, and the opened dialog contains the Task 19 human-readable request preview
(`Changed paths`) instead of the raw JSON key; the `blocked` scene (proto-gate `ask`, no durable gate)
renders the task detail but no `gate-review`, no `gate-banner`, and no `gate-respond-open`, proving the
ask-only task-local response box stays removed.

The slice-6g cases build a master+slice projection with a local `taskDoc` factory + `seedSeries`
helper (a folder-keyed `SeriesNode` master in `analytics.series`, a `subTasks` index whose rows carry
`createdAt`, and one authored slice in `analytics.taskDocuments`). They assert:
the index renders pinned above the description (`compareDocumentPosition`) with the in-section copy
kept; clicking a sub-task opens its `TaskReader` and the header breadcrumb returns; a GFM table renders
as a real table (not raw pipes); and
`seedSeriesOrdering` proves rows sort by `createdAt` while rendering task-specific `01.` / `99.` numbers
instead of generated `1.` / `2.` counters. That ordering assertion now exercises `seriesAsMasterDoc`
rather than `SubTaskIndex` — the sort moved to the series adapter, and `seedSeriesOrdering` seeds a
`SeriesNode`, so the test's meaning is intact while its subject changed.

The cross-master "→" jump has its own fixture, on a master **task document**, not on `seedSeries`.
`seedSeries`'s rows are `SeriesSubTaskNode`s and the server never stamps one with
`linkedLifecycleId`, so seeding the cross-link there described a projection the server cannot produce.
The test now builds a `kind: "master"` `taskDoc` whose second `subTasks` row carries
`linkedLifecycleId: "LC-OTHER"`, seeds it with `seedTaskDocuments`, selects it by
`taskdoc:/tasks/repo-a/planning/task.json`, clicks `subtask-open-link-2`, and expects
`onOpenLifecycle("LC-OTHER")`. Relatedly, the three master-doc fixtures in this block dropped the
`createdAt` they used to put on `subTasks` rows: `TaskSubTaskRefNode` has no such field, and the
literals only typechecked while they were cast.

`seedSeries` can also attach an enclosure whose `taskId` is the root
selected lifecycle id and whose `taskName` is the folder-keyed series id; the regression asserts that
this selection renders master objective/sections instead of the master-less slice list or no-doc
fallback. The paired leaf regressions deliberately use the same parent `taskName` mapping on a non-root
lifecycle: one moves the only slice doc to another lifecycle and expects the no-doc fallback rather
than master content, and one keeps a direct `TaskDocNode` for the selected lifecycle and expects the
leaf body. Together they document that `taskName` is parent/root identity metadata for leaf lifecycles,
not their content selector.
`nestedProgressSteps` deliberately gives the visible top-level list a 6/7 summary while the
projection reports 46/49; the corresponding regression asserts that the master sub-task row and
opened reader progress fill both show 46/49 and reject the locally derivable 6/7.
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
The viewed-leaf cases pass a `vi.fn()` as `onViewLeaf` and assert its **last** call: `series` →
`undefined` while the master overview shows, `subtask-open-1` → `repo-a/series/1`, `series-breadcrumb` →
`undefined` again; the directly-opened-leaf case seeds a leaf `taskDoc` (`id: "260628-leaf"`, repo
`agents-remember`, an operations-integration docPath) and asserts the reported key is the doc's
`qualifiedLeafKey`.

The series-notes block (`stubNotes` — a per-URL fetch stub answering `/api/notes/list` and
`/api/notes/read`, everything else a bare ok) proves the DetailPanel wiring: a leaf reader fetches
the notes list for the doc's OWN series (the exact
`/api/notes/list?repo=agents-remember&master=260703_agent-orchestration` URL is asserted, pinning
the repo/master derivation from the doc node), and since the notes-file update a notes-file reference renders as
`note-ref-1` whose click fires the `onOpenNotes` callback with `{repo, master, path}` (the
  notes-reader takeover; no inline `note-view` remains) while a code-path reference gets no link
(`note-ref-2` absent), and a master overview shows the "Series notes" list.

### Invariants And Boundaries

Component-level (jsdom) — no real backend. Reuses the
`GALLERY` bench fixtures so the test data matches the dev bench.
The promoted-leaf case is a component contract only: it proves the panel does not use contract text as
readable task content, but it does not exercise the Python reader that populates `analytics.taskDocuments`.
The planning-doc cases are also component-level; observer reader tests prove projection of unbound and
archived documents.

The body cases stub `fetch` and prove component behavior only; they do not re-test the Python endpoint.
Failure coverage is one request plus honest fallback, not a retry-loop test. The ordering case proves
which requests mount first in jsdom; the separate task evidence records the natural-browser smoke over
the real live backend.

Fixtures must state shapes the server can actually send. `linkedLifecycleId` belongs on a master task
document's rows (`TaskSubTaskRefNode`) and `createdAt` on a series' rows (`SeriesSubTaskNode`); putting
either on the other model describes a projection that cannot arrive, and — because both models are
`extra="forbid"` — one the server would reject outright. Every seeded `WorkspaceProjection` here now
derives its `metrics` from `metricsFor(lifecycles)` instead of hand-listing buckets, so a new lifecycle
state fails these seeds at compile time; no assertion in this file reads `metrics`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The body-first cases pin request ordering, complete-field rendering, unavailable fallback, retained summary content, one step copy, and revision cache invalidation. | "loads the complete task body before mounting reader ancillary requests"; "renders the complete on-demand task-document body while retaining its summary"; "shows the available summary when the on-demand task-document body is absent"; "reuses an unchanged task body and refetches when its revision changes" | dashboard/src/panels/DetailPanel.test.tsx:855-956; dashboard/src/panels/DetailPanel.test.tsx:958-1025; dashboard/src/panels/DetailPanel.test.tsx:1027-1049; dashboard/src/panels/DetailPanel.test.tsx:1051-1095 |
| The hook records body availability and merges absent arrays; the component delays ancillary mounts and renders loading/fallback messages. | `useTaskDocumentBody`; `TaskReader`; `TaskBodyNotice` | dashboard/src/data/useTaskDocumentBody.ts:29-74; dashboard/src/panels/DetailPanel.tsx:350-395; dashboard/src/panels/DetailPanel.tsx:1303-1388; dashboard/src/panels/DetailPanel.tsx:1390-1404 |
| The drawer selects the series for direct or root-task selection. | `selectedSeries` | dashboard/src/panels/DetailPanel.tsx:380-386 |
| `seriesAsMasterDoc` sorts a series' rows before the index renders them in received order. | `seriesAsMasterDoc`; `SubTaskIndex` | dashboard/src/panels/DetailPanel.tsx:961-976; dashboard/src/panels/DetailPanel.tsx:1148-1230 |
| Projected step progress is declared for the drawer. | `taskStepProgress` | dashboard/src/panels/DetailPanel.tsx:939-942 |
| The index forwards projected step progress through its received rows. | `SubTaskIndex` | dashboard/src/panels/DetailPanel.tsx:1148-1230 |
| The reader consumes projected step progress for the opened document. | `TaskReader` | dashboard/src/panels/DetailPanel.tsx:1303-1388 |
| `SubTaskIndex` reads the `linkedLifecycleId` property from each row, so only a task-doc master's rows reach the cross-link branch. | `SubTaskIndex`; `linkedLifecycleId` | dashboard/src/panels/DetailPanel.tsx:1148-1230 |
| The `taskDoc`/`seriesNode`/`enclosure` factories, the `seedSeries` helper, and `nestedProgressSteps` (top-level progress deliberately differing from backend `stepsDone`/`stepsTotal`). | `taskDoc`; `seriesNode`; `enclosure`; `seedSeries`; `nestedProgressSteps`; `stepsDone`; `stepsTotal` | dashboard/src/panels/DetailPanel.test.tsx:22-45; dashboard/src/panels/DetailPanel.test.tsx:47-63; dashboard/src/panels/DetailPanel.test.tsx:65-83; dashboard/src/panels/DetailPanel.test.tsx:86-185; dashboard/src/panels/DetailPanel.test.tsx:187-198 |
| `seedSeriesOrdering` seeds a `SeriesNode` whose rows carry `createdAt`, so the ordering assertion exercises `seriesAsMasterDoc`. | `seedSeriesOrdering` | dashboard/src/panels/DetailPanel.test.tsx:200-248 |
| The ordering assertion pins creation-time placement while expecting child task-document id labels and rejecting generated local counters. | "orders master leaves by creation time and displays task-specific numbers" | dashboard/src/panels/DetailPanel.test.tsx:783-791 |
| The cross-master fixture carries a master task document with the `linkedLifecycleId` metadata. | `linkedLifecycleId` | dashboard/src/panels/DetailPanel.test.tsx:734-751 |
| The cross-master fixture is selected by its `taskdoc` key. | `taskdoc` | dashboard/src/panels/DetailPanel.test.tsx:756-756 |
| The projected-progress regression expects 46/49 in both the master row and opened leaf reader and rejects the locally derivable 6/7. | "summarizes task progress with every declared parent and nested step" | dashboard/src/panels/DetailPanel.test.tsx:793-811 |
| The aggregate-token regression pins the master reader's `series tokens` display from `seriesTokenTotal`. | `seriesTokenTotal`; "renders aggregate series tokens on the master reader" | dashboard/src/panels/DetailPanel.tsx:959-959; dashboard/src/panels/DetailPanel.test.tsx:107-112; dashboard/src/panels/DetailPanel.test.tsx:774-781 |
| The typed taskdoc selection regressions cover unbound planning leaf/master docs, lifecycle-bound master sibling-pool navigation, static missing-leaf rows, and structured step/example id display. | "renders an unbound planning leaf task document by typed taskdoc selection"; "renders an unbound master task document by kind"; "opens authored master leaves from the full projected pool when the master is lifecycle-bound"; "keeps master rows static when the referenced leaf has no authored task document"; "renders structured ids with step and code example titles" | dashboard/src/panels/DetailPanel.test.tsx:460-477; dashboard/src/panels/DetailPanel.test.tsx:479-513; dashboard/src/panels/DetailPanel.test.tsx:515-580; dashboard/src/panels/DetailPanel.test.tsx:582-607; dashboard/src/panels/DetailPanel.test.tsx:609-651 |
| The root-task lifecycle regression proves enclosure `taskId`/`taskName` selects the folder-keyed series master for the master row. | "renders master content when a selected task-id lifecycle maps to the series task name" | dashboard/src/panels/DetailPanel.test.tsx:813-825 |
| The missing-doc leaf lifecycle regression proves parent `taskName` alone does not render the master for leaf rows. | "does not use parent taskName as content for a leaf lifecycle without a projected doc" | dashboard/src/panels/DetailPanel.test.tsx:827-839 |
| The direct leaf lifecycle regression proves a projected leaf `TaskDocNode` wins over parent `taskName` mapping, preventing leaf sidebar rows from rendering the master. | "keeps a direct leaf lifecycle document ahead of the parent series mapping" | dashboard/src/panels/DetailPanel.test.tsx:841-853 |
| `seedPromotedLeaf` carries the parent master/series metadata. | `seedPromotedLeaf` | dashboard/src/panels/DetailPanel.test.tsx:304-399 |
| The backlink regression clicks "master-parent-link" and expects navigation to the parent master task document. | "links an enclosure-opened leaf back to its parent task document" | dashboard/src/panels/DetailPanel.test.tsx:1120-1132 |
| `findParentTaskMatch`/`parentTaskLinkForDoc` resolve the parent link from projected series sub-task refs. | `findParentTaskMatch`; `parentTaskLinkForDoc` | dashboard/src/data/taskHierarchy.ts:43-51; dashboard/src/data/taskHierarchy.ts:68-82 |
| `SeriesSubTaskNode` vs `TaskSubTaskRefNode` — which fixture row may carry `createdAt` and which may carry `linkedLifecycleId`. | `SeriesSubTaskNode`; `TaskSubTaskRefNode` | dashboard/src/types/projection.ts:369-376; dashboard/src/types/projection.ts:494-501 |
| `taskLabel`/`taskDocumentLabel` — the helpers that separate visible lifecycle labels from direct task-doc filtering. | `taskLabel`; `taskDocumentLabel` | dashboard/src/data/taskIdentity.ts:213-230; dashboard/src/data/taskIdentity.ts:239-244 |
| The gate-review test opens the shared responder and expects the rendered preview label `Changed paths`. | "renders the gate respond drawer with the full request packet" | dashboard/src/panels/DetailPanel.test.tsx:439-447 |
| The ask-only attention detail regression asserts the obsolete task-local response box is absent when no durable gate exists. | "does not render the obsolete task-local response box for ask-only attention details" | dashboard/src/panels/DetailPanel.test.tsx:449-456 |
| The blocked fixture is the ask-only scene without a durable gate. | "blocked" | dashboard/src/dev/fixtures.ts:171-206 |
| The gate-review fixture supplies the durable gate scene. | "gate-review" | dashboard/src/dev/fixtures.ts:443-480 |
| The shared responder rendered by the gate cases. | `GateResponder`; "gate-respond-open" | dashboard/src/panels/GateResponder.tsx:217-539 |

## Update History

- 2026-08-04T13:42:02+02:00 — 260731-EFA-L6 S18-B08 curator: audited whole-claim coverage, split selection/progress and fixture owners, and retained the generated seed/backlink ranges at 304-399 and 1120-1132 pending the final scoped fixer gate.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: corrected the progress regression to its
current authority: projected 46/49 wins on both surfaces and locally derivable 6/7 is rejected.
  Row 188's still-true fixture mismatch description is unchanged; the current test binding is
  retained for the final scoped citation fixer.

- 2026-08-01T10:05+02:00 — 260731-EFA curator: corrected a body claim that had become false.
  `seedSeries` no longer carries `linkedLifecycleId` on its `SeriesSubTaskNode` rows — the server never
  stamps one there — so the cross-master `→` test builds its own `kind: "master"` `taskDoc`, seeds it
  with `seedTaskDocuments`, and selects it by `taskdoc:` key. Recorded that the ordering assertion still
  passes but now exercises `seriesAsMasterDoc`'s `orderedByCreation` instead of `SubTaskIndex`'s
  (verified `seedSeriesOrdering` seeds `analytics.series`, so the series adapter is the sort site), and
  that the three master-doc fixtures dropped `subTasks[].createdAt`, which `TaskSubTaskRefNode` does not
  declare. Added the fixture-honesty and `metricsFor` boundaries. Repaired fourteen citations against
  the current sources; the drifted references were mostly wholesale range moves across the ordering,
  progress, lifecycle-identity, backlink, and `GateResponder` claims (the old responder range held only
  styles). The dated entry preserves this historical progress correction without reopening its completed
  gate and fixture citation repair.

- 2026-07-12T12:07+02:00 — 260712-TRH: added the deferred-body request-order regression, expanded
  complete-content coverage to every reader field class, pinned path/revision cache behavior, and made
  affected change-set assertions await body hydration. Verification metadata stays pinned until
  closeout stamps the code commit.

- 2026-07-10T13:41+02:00 — 260707-HFX2 R7: added async full-body merge and 404 summary-fallback
  regressions, and changed step assertions to require exactly one Implementation steps copy.
  Verification metadata stays pinned until closeout stamps the eventual code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2: taught the shared fetch stubs to serve full task
  documents for the on-demand reader path while preserving change-set and notes API behavior.
  Verification metadata remains pinned until closeout stamps the eventual code commit.

- 2026-07-07T14:00+02:00 — agent-orchestration follow-up: the "series notes" test's resolved-reference click now
  asserts the `onOpenNotes` callback fires with `{repo, master, path}` (the reader takeover opens) instead
  of an inline `note-view`; the master-overview list test is unchanged. (Also normalized the malformed
  `lastUpdated` frontmatter value.) Verification metadata pinned until closeout stamps the eventual commit.
- 2026-07-06T10:45+02:00 — Body note: the enclosure fixture carries the required existence flags (default true); no assertion change. Verification metadata pinned until closeout stamps the eventual commit.
- 2026-07-06T03:05+02:00 — Projection-contract fixture update: the local `enclosure(...)` fixture now defaults the new required
  `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags to `true` (a live worktree), matching
  the projection contract; no assertion change — DetailPanel does not filter on existence. Verification
  metadata pinned until closeout stamps the eventual commit.
- 2026-07-06T02:40+02:00 — agent-orchestration follow-up: added the `DetailPanel series notes` describe
  block (per-URL `stubNotes` fetch stub) pinning the notes-list wiring on a leaf reader (exact
  list URL → the doc's own repo/master), reference-link resolution (notes file → openable
  `note-ref-1`; code path → plain text), and the master-overview "Series notes" section.
  Verification metadata pinned until closeout stamps the eventual commit.
- 2026-07-02T16:18+02:00 — Ask-only attention-detail follow-up: changed the ask-only attention detail regression to assert no
  `GateResponder`/`gate-banner`/`gate-respond-open` is rendered when only `activeLifecycle.ask` exists,
  while durable gate coverage remains intact. Verification metadata pinned until closeout stamps the
  commit.
- 2026-06-30T00:00:00+02:00 — Viewed-leaf follow-up: added a `DetailPanel viewed-leaf reporting` describe block pinning the new
  `onViewLeaf` prop — a master overview reports `undefined`, drilling a sub-task reports the leaf's
  qualified id (not the master), the breadcrumb clears it, and a directly-opened leaf doc reports its own
  `repo/master/leaf-id`. Verification metadata pinned until closeout stamps the eventual commit.
- 2026-06-29T23:00+02:00 — Doc-reader change-set-bar follow-up: added a `DetailPanel doc-reader change-set bar` describe block (a
  `stubCounters` fetch stub; `afterEach` now also `vi.unstubAllGlobals()`) — committed button + leaf target
  on a leaf reader, series button on a master reader, working button only when the leaf's enclosure is
  live, and the bar omitted with no `onOpenChangeSet`. Verification metadata pinned until closeout stamps
  the eventual commit.
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
- 2026-06-24T13:59+02:00 — Task 17 progress-count regression: the then-current `seedSeries` fixture
  modeled 40/42 nested backend progress over seven top-level steps and asserted 6/7 on both surfaces.
  The later S18-T3 correction supersedes those expected values with the projected 46/49 behavior;
  this entry remains historical provenance. Verification metadata pinned until closeout stamps the
  follow-up code commit.
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
