# test_task_document.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_task_document.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-06-29T22:57+02:00 |
| lastVerifiedCommitHash | `026b2468a8d456e35a4f80a86e66a574b1e81f4b` |
| lastVerifiedCommitDate | 2026-06-30T00:57:11+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[mcp/overview.md](../overview.md)

## Purpose

Tests for the JSON-primary task-document layer (slice 3c): the schema, renderer,
store, the `task_doc` controller (master + subTask leaf authoring; `light` is load-compat only),
and tool registration.

## Code Commentary

### Logic

- `SchemaTests` — `model_dump`/`model_validate` round-trip equality, the `schema`
  alias, `extra="forbid"` rejection, the `step_total`/`step_done`/`current_step`
  leaf-counting logic, a master round-trip, and the kind guards (master ⇒ no
  steps/lifecycleId; light/subTask ⇒ no subTasks + freeform-only `sections`, R4), plus the **R3**
  `codeExamplesNote` cases (round-trip + `exclude_none` omission, master-forbids,
  note-requires-empty-`codeExamples`) and the **R4** extension round-trip
  (`statusNote`/`headerNotes`/freeform `sections`).
- `RenderTests` — a byte-exact golden for a small light doc, determinism, the
  `(Sub-task <id>)` title + `**Master:**` line, checkbox + substep-note rendering, the **R2**
  outcome-on-the-checkbox + bare-step-heading-only case, decision-cell pipe/newline escaping,
  empty-section placeholders, the **R3** `codeExamplesNote`-renders-on-empty case (note in
  place of the "none needed" default), and code-fence blank-line preservation. **R4:** the `statusNote`
  suffix + `headerNotes` lines render, a leaf's freeform `sections` render after References, and a
  real-sub-task fixture round-trips content-complete.
- `MasterRenderTests` — a byte-exact golden master (header + ordered sections, the
  `subTasks` list with ✅/🔨/⬜ markers incl. the `3c` number, and the Shared Decisions
  table), determinism, the status→marker map, the empty-subtasks placeholder, and
  verbatim preservation of bespoke multi-paragraph prose (the S4 acceptance).
- `StoreTests` — `doc_stem` light-vs-subtask (and master → `task`), and a write→read
  round-trip that leaves no `.tmp` file.
- `ControllerTests` — `create` (+ duplicate refusal), `set_status`, `set_field`
  (incl. `codeExamplesNote`/`statusNote`), `set_step` insert-then-update (no duplication),
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
  A `cast`-typed `SimpleNamespace` stands in for `McpRuntimeConfig` (only
  `coordination_root` is read).
- `MasterControllerTests` — master `create` (writes `task.json`, no `lifecycleId`
  even with a contract present), `set_subtask` insert-then-update by number,
  `set_section` upsert by heading, `set_step` rejected on a master,
  `set_subtask` rejected on a non-master, `set_section` now allowed on a leaf (freeform-only, R4),
  the argument-error paths, and the `remove_subtask` CRUD-delete cases (deletes the leaf doc + master
  row, `keep_file` retains the doc, dry-run reports `wouldDeleteFiles` without deleting, absent number
  raises, non-master rejected).
- `RegistrationTests` — `task_doc` is in `PUBLIC_TOOLS` + the registry, and the
  payload builder returns a token-stamped payload that validates against
  `TaskDocResponse` (ambient reset first).

### Invariants And Boundaries

- The golden + determinism tests are the regression line for the renderer's
  byte-stability contract.
- Conformance of the `task_doc` payload also lives in
  `test_tool_response_conformance.py` (its representative-payload net).

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The package under test. | [tasks/](agents-remember/mcp/src/agents_remember/tasks/) |
| The controller under test. | [task_doc_tools.py](agents-remember/mcp/src/agents_remember/controllers/task_doc_tools.py) |
| The replace controller cases cover structural rewrites, dry-run no-mutation, and path-change rejection. | [test_task_document.py](agents-remember/mcp/tests/test_task_document.py) |
| The master-sync controller cases cover row creation, manual scope preservation, derived status, and dry-run parent preview. | [test_task_document.py](agents-remember/mcp/tests/test_task_document.py) |
| The conformance net that also covers `task_doc`. | [test_tool_response_conformance.py](agents-remember/mcp/tests/test_tool_response_conformance.py) |

## Series-Contract Notes

Task-document tests cover the `seriesContractPath`/`enclosures[]` linkage fields and observer binding from a leaf doc's enclosure path to its lifecycle.

## Update History

- 2026-06-29T22:57+02:00 — CRUD completion (L2): added `MasterControllerTests` cases for `remove_subtask`
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
