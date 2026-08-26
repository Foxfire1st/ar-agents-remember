# test_task_document.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_task_document.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[mcp/overview.md](../overview.md)

## Purpose

Tests for the JSON-primary task-document layer (slice 3c): the schema, renderer,
store, the `task_doc` application entry point (master + subTask leaf authoring; `light` is load-compat only),
and tool registration.

## Code Commentary

### Logic

- `SchemaTests` — `model_dump`/`model_validate` round-trip equality, the `schema`
  alias, `extra="forbid"` rejection, the `step_total`/`step_done`/`current_step`
  leaf-counting logic, a master round-trip, and the kind guards (master ⇒ no
  steps/lifecycleId; light/subTask ⇒ no subTasks + freeform-only `sections`, R4), plus the **R3**
  `codeExamplesNote` cases (round-trip + `exclude_none` omission, master-forbids,
  note-requires-empty-`codeExamples`), the **R4** extension round-trip
  (`statusNote`/`headerNotes`/freeform `sections`), and the `orchestrates` cases
  (master round-trip, master-only rejection on a leaf, `[]` default on docs without the field).
- `RenderTests` — a byte-exact golden for a small light doc, determinism, the
  `(Sub-task <id>)` title + `**Master:**` line, checkbox + substep-note rendering, the **R2**
  outcome-on-the-checkbox + bare-step-heading-only case, decision-cell pipe/newline escaping,
  empty-section placeholders, the **R3** `codeExamplesNote`-renders-on-empty case (note in
  place of the "none needed" default), and code-fence blank-line preservation. **R4:** the `statusNote`
  suffix + `headerNotes` lines render, a leaf's freeform `sections` render after References, and a
  real-sub-task fixture round-trips content-complete.
- `MasterRenderTests` — a byte-exact golden master (header + ordered sections, the
  `subTasks` list with ✅/🔨/⬜ markers incl. the `3c` number, and the Shared Decisions
  table), determinism, the status→marker map, the empty-subtasks placeholder,
  verbatim preservation of bespoke multi-paragraph prose (the S4 acceptance), and the
  `**Orchestrates:**` header line (renders backticked names when set; absent field ⇒ no line).
- `StoreTests` — `doc_stem` light-vs-subtask (and master → `task`), and a write→read
  round-trip that leaves no `.tmp` file.
- `ApplicationTests` — `create` (+ duplicate refusal), `set_status`, `set_field`
  (incl. `codeExamplesNote`/`statusNote`, and the `orchestrates` cases: set on a master —
  persisted + rendered — and rejected on a leaf via the schema backstop), `set_step`
  insert-then-update (no duplication),
  `append_decision`, non-mutating
  `get`, contract `lifecycle_id` pickup, `contract_path` resolution, the error
  paths, and the **R5** dry-run cases (`create` renders without writing either file; a mutating
  `dry_run` leaves both files byte-identical; `wouldLose`/`diff` flag on-disk content the render drops).
  It also covers full-document `replace`: structural arrays/decisions are rewritten, dry-run leaves
  both files untouched, and slug/kind path changes are rejected. Task 21 adds leaf-to-master sync
  coverage: leaf creation inserts the parent master row, updates preserve manually-authored master
  `scope`, step status changes derive the master row status, and dry-run returns a master sync preview
  without mutating the parent file. Master/leaf-only authoring is covered too: `create`/`replace`
  refuse an explicit `kind="light"`, and a bare `create` defaults to `master` with no contract and to
  `subTask` under a leaf contract.
  The shared `_config` fixture builds a real `McpRuntimeConfig` with a committed configured
  repository, `refs/remotes/origin/main`, and symbolic `origin/HEAD`. Task-document publication
  therefore exercises the same exact repository/default-branch authority as production rather
  than bypassing it with a partial namespace.
- `MasterApplicationTests` — master `create` (writes `task.json`, no `lifecycleId`
  even with a contract present), `set_subtask` insert-then-update by number,
  `set_section` upsert by heading, `set_step` rejected on a master,
  `set_subtask` rejected on a non-master, `set_section` now allowed on a leaf (freeform-only, R4),
  the argument-error paths, and the `remove_subtask` CRUD-delete cases (deletes the leaf doc + master
  row, `keep_file` retains the doc, dry-run reports `wouldDeleteFiles` without deleting, absent number
  raises, non-master rejected). The response-conformance regression:
  `test_remove_subtask_response_validates_on_both_paths` validates the `remove_subtask` result against
  `TaskDocResponse` (`extra="forbid"`) on the delete-with-files AND `keep_file` paths (and the dry-run
  preview) — the regression proving the destructive success no longer surfaces a false tool error.
- `RegistrationTests` — `task_doc` is in `PUBLIC_TOOLS` + the registry, and the
  payload builder returns a token-stamped payload that validates against
  `TaskDocResponse` (ambient reset first).

### Invariants And Boundaries

- The golden + determinism tests are the regression line for the renderer's
  byte-stability contract.
- Conformance of the `task_doc` payload also lives in
  `test_tool_response_conformance.py` (its representative-payload net).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The test imports and exercises the task-document APIs used by this suite. | "from agents_remember.application.task_docs.task_doc_tools import (" | mcp/tests/test_task_document.py:24-24 |
| The application entry point under test. | `task_doc_tool` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:191-284 |
| The path-change rejection test invokes the replace operation and expects TaskDocError. | `test_replace_rejects_document_path_change` | mcp/tests/test_task_document_application_1.py:465-479 |
| Leaf creation inserts the parent master row. | "def create(cls" | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:156-156 |
| Master sync preserves manually-authored scope. | "const { webtuiPrefixOptions } = require('./webtui-scope.config.cjs');" | dashboard/postcss.config.cjs:6-6 |
| Master row status is derived from leaf state. | "export const status = css({" | dashboard/src/panels/sessionComposerStyles.ts:116-116 |
| Dry-run returns the parent master sync preview. | "def _create_missing_dirs(paths: list[Path]" | mcp/src/agents_remember/kernel/memory_init.py:14-14 |
| The conformance net that also covers `task_doc`. | `task_doc` | mcp/tests/test_tool_response_conformance.py:779-779 |

## Series-Contract Notes

Task-document tests cover the `seriesContractPath`/`enclosures[]` linkage fields and observer binding from a leaf doc's enclosure path to its lifecycle.

## Parent-master integrity delta

- An **unreadable parent master refuses the leaf edit rather than dropping the row**: a leaf whose
  parent cannot be read must not be silently orphaned.
- A master ref naming a **sibling leaf** is refused **by kind**, not by id shape.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (task_doc_tool now takes
  `call: TaskDocCall`); claim re-read and citation ranges regenerated. Verified at code commit
  a9d50e08.


- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 moved `task_doc_tool` within `task_doc_tools.py`; re-pointed the citation to `task_doc_tools.py:190-275`. Verification metadata unchanged.
- 2026-08-16T02:51+02:00 — L4 topology-publication authority: replaced the partial
  `SimpleNamespace` fixture with a real configured Git repository and exact remote default
  authority so application tests exercise the strengthened publication boundary.
- 2026-08-14T06:40+02:00 — L23 final candidate review: task-document tests pin canonical
  sprint/master/leaf relationships used by lineage and route-review resolution. Verification
  remains closeout-owned.
- 2026-08-13T07:53+02:00 — 260731-EFA-L23 super-line reconciliation: re-reviewed this card and its Repo-Internal citation targets after absorbing the super-integration memory line. Retained claims remain supported by the current tree. Verification is pinned to real code HEAD `1580f92715ff93c988f9a15439ad9bec60ef4c5d`; the new-line memory mapping remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer residual correction: bound the path-change rejection test,
  `replace` operation, and `TaskDocError` expectation to the complete test body.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata remains pinned until closeout.
- 2026-08-02T00:17+02:00 — No content impact: the controllers package was renamed to `application/` and `worktrees/status.py` moved to `application/worktree_status.py`. Updated the references and vocabulary here; the behavior this document describes is unchanged. Verification metadata remains pinned until closeout.
- 2026-07-31T15:32+02:00 — Recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata remains pinned until closeout.

- 2026-07-07T18:40+02:00 — Review fix batch (finding 1 / friction F-N): added
  `MasterControllerTests.test_remove_subtask_response_validates_on_both_paths` — validates the
  `remove_subtask` payload against `TaskDocResponse` on the delete-with-files, `keep_file`, and dry-run
  paths, locking the response contract for the destructive success. Verification metadata pinned until
  closeout stamps the review commit.
- 2026-07-06T23:58:36+02:00 — Visual hierarchy + chat grouping: added the `orchestrates`
  coverage — `SchemaTests` round-trip on a master + master-only rejection + `[]` default,
  `MasterRenderTests` `**Orchestrates:**` header line (present when set, absent otherwise), and
  `ControllerTests` `set_field` on a master (persisted + rendered) with the leaf rejection.
  Verification metadata remains pinned until closeout.
- 2026-06-29T22:57+02:00 — CRUD completion: added `MasterControllerTests` cases for `remove_subtask`
  — deletes the leaf doc + master row, `keep_file` retains the doc, dry-run previews `wouldDeleteFiles`
  without deleting, absent number raises, non-master rejected. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-29T21:24+02:00 — Post-landing cleanup (master/leaf-only authoring): added `ControllerTests`
  cases that `create`/`replace` refuse an explicit `kind="light"` and that a bare `create` defaults to
  `master` (no contract) or `subTask` (leaf contract); repaired the `MasterControllerTests` non-master
  fixture and the `RegistrationTests` payload-builder fixture, which previously authored `light` through
  the controller. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 task-doc master sync: controller coverage now proves automatic
  same-root master row create/update, manual `scope` preservation, derived row status, and dry-run master
  preview without parent mutation. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T12:41+02:00 — Task-doc replacement repair: fixed the stale governing overview link
  to the existing MCP route overview and documented the new `replace` controller tests for structural
  rewrites, dry-run no-mutation, and path-change rejection. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: task-document tests now validate `seriesContractPath`, `enclosures[]`, leaf lifecycle binding through enclosure paths, and task-name resolution without requiring users to pass task filesystem paths. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T07:23 — Slice 3c reopened (R5, dry-run/preview): added the `ControllerTests` dry-run cases — `create` renders without writing either file; a mutating `dry_run` leaves both files byte-identical; `wouldLose`/`diff` against unmodeled on-disk content. Verification metadata pinned until closeout stamps the R5 code commit.
- 2026-06-19T06:03 — Slice 3c reopened (R4, leaf-doc fidelity): split the leaf-forbids test (a freeform leaf section is now legal; `subTasks` + non-freeform sections still forbidden), added render tests for `statusNote`/`headerNotes`/leaf freeform sections + a content-complete real-sub-task round-trip fixture, and a controller `set_section`-on-leaf + `set_field statusNote` test. Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T05:15 — Slice 3c reopened (R3, deferred-examples honesty): added the `codeExamplesNote` cases — `RenderTests` (note renders for an empty `codeExamples` instead of the "none needed" default), `SchemaTests` (round-trip + `exclude_none` omission, master-forbids, note-requires-empty-examples), and `ControllerTests` (`set_field` of `codeExamplesNote`). Verification metadata pinned until closeout stamps the R3 code commit.
- 2026-06-19T04:18 — Slice 3c reopened (R2, heading-vs-outcome): added the outcome/bare-step render case to `RenderTests` (outcome on the checkbox distinct from the heading; a bare step is heading-only) and updated the bare-step golden (the redundant `- [ ]` echo dropped). Verification metadata pinned until closeout stamps the R2 code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: added `MasterRenderTests` and `MasterControllerTests`, master cases in `SchemaTests`/`StoreTests`, and the S4 verbatim-prose acceptance. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1: tests for the task-document schema, renderer, store, controller, and registration. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
