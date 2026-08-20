# mcp/src/agents_remember/mcp/registration/tasks.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/mcp/registration/tasks.py`       |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview      | `overview.md`                                             |

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_task_tools(server, config)` declares the task-document authoring tool plus the two
task-state transitions: `task_reopen`, `lifecycle_finalize_task`, `task_doc`.

## Code Commentary

### Logic

`task_doc` is the JSON-primary authoring tool and carries the longest docstring on the surface,
because the operation vocabulary is not in the types: `create` | `replace` | `set_status` |
`set_step` | `skip_step` | `set_subtask` | `remove_subtask` | `set_section` | `append_decision` |
`record_route_review` | `author_execution_graph` | `attach_master` | `detach_master` |
`linkage_report` | `set_field` |
`get` (`migrate_execution_topology` was removed in 260815-DAG-L13). The JSON document is the source of truth; `task.md` / `<slug>.md` is a generated render that
is never parsed back. Everything mutates except `operation='get'`, and `dry_run=true` builds and
validates and returns `rendered`/`diff`/`wouldLose` **without** writing — the preview before
adopting a hand-written `.md`. Master (`kind:"master"`) documents use `set_subtask` /
`remove_subtask` / `set_section`; `remove_subtask` also deletes the leaf doc (json+md) unless
`subtask.keep_file`; `set_step` is leaf-only. `skip_step` takes an exact existing step and a nonblank
reason, marks only that unit done, records intentional-skip provenance, and does not cascade; an
        explicit status clears an earlier skip disposition cit:(["operation: 'create'", "exact existing step", "sets only that unit done", "records intentional-skip provenance without cascading", "A nonblank reason is required.", "explicit status clears an earlier skip disposition"], mcp/src/agents_remember/mcp/registration/tasks.py:111-111; mcp/src/agents_remember/mcp/registration/tasks.py:123-125).

Since 260815-DAG-L11 the docstring also spells out the graph operation:
`author_execution_graph` applies one
validated atomic batch of typed mutations (`add_node`/`remove_node`/`add_edge`/`remove_edge`/
`move_leaf`/`set_nature`) to a sprint's `executionGraph` — segment-addressed by sampling
leaf ids, with judgment-bearing mutations requiring a `judgmentId` row in the sprint's Judgment
Register (the mechanism never invents one), typed refusals for segment-on-atomic and incomplete
partitions, and unplaced-leaf placements plus numbering inversions reported as facts. Since
260815-DAG-L13 the first `add_node` batch on a graph-less sprint bootstraps the graph (the result
reports `bootstrapped: true`), sprint creation scaffolds the empty canonical Judgment and Priority
Register sections, and a `set_section` carrying a canonical register heading must keep the exact
register table shape (write-time validation). Since 260815-DAG-L14 the docstring also spells
out the sprint linkage operations: `attach_master` writes the typed `masterRef` row, the
`orchestrates` slug, and — only on a graphed sprint — the lump graph node as one validated atomic
batch (a nature-less master requires `executionNature` + a `judgmentId` from the sprint Judgment
Register; graph-less sprints report `graphNode: deferred-no-graph-default`); `detach_master`
removes the typed row, membership slug, and graph node, refusing while any edge touches the node
and never deleting files; `linkage_report` surfaces seat-doc rows, slug-only membership,
row/membership mismatches, and uncommanded masters as facts, and `get` on a sprint carries the
same `linkageFacts`.

The body splits that into two objects: `TaskDocTarget(repo_id, task_name, contract_path, slug)` —
which document to edit — and `TaskDocEdit(fields, step, decision, subtask, section)` — what the edit
is. `operation` and `dry_run` stay separate arguments; since 260815-DAG-L16 the registered `task_doc`
also exposes `branch_addressed` (policy-gated direct-execution opt-in for `record_route_review`,
bound to the task-root series contract — L16-R6). A read (`operation='get'`) leaves every edit
slot unset.

`lifecycle_finalize_task` packs its three document arguments into `FinalizeTaskDocs(task_doc_path,
master_doc_path, subtask_number)` and keeps `dry_run` and `teardown_providers` separate. Its
docstring states the terminal semantics: the task's landed commit must be reachable from the
contract's local target/source branch — a PR-gated flow must complete the merge and pull first, so
the proof is structurally identical to a non-PR edge — and no squash-merge equivalence is attempted.

`task_reopen(contract_path, dry_run)` is a state reset, not a worktree creator: it returns the
enclosure contract's review/closeout/integration state to virgin and the leaf's task document to
planning, under the **exact same leaf id** (no `-rN` suffix). It refuses masters, in-flight leaves,
and leaves whose worktrees still exist; afterwards the normal `worktree_start` with the same leaf id
recreates everything.

### Invariants And Boundaries

- Flat signature; `TaskDocTarget` / `TaskDocEdit` / `FinalizeTaskDocs` are built in the body.
- `task_doc` is mutating except `get`, and registers `dry_run=False`.
- Document schema validation, master/leaf rules, and the reopen refusals live in
  `application/task_doc_tools.py` and `application/worktree_tools.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `task_doc` / `task_reopen` payload builders. | `task_doc_payload`, `task_reopen_payload` | mcp/src/agents_remember/mcp/tools/task_doc.py:19-30; mcp/src/agents_remember/mcp/tools/task_doc.py:33-46 |
| The finalize builder. | `lifecycle_finalize_task_payload` | mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py:15-32 |
| `FinalizeTaskDocs`. | `FinalizeTaskDocs` | mcp/src/agents_remember/application/worktree_tools.py:538-545 |
| Target/edit splitting and the unset-edit read proved through a live server. | `test_task_doc_splits_the_document_target_from_the_edit`, `test_task_doc_leaves_every_edit_slot_unset_for_a_read` | mcp/tests/test_mcp_registration_wiring_tests_2.py:203-238; mcp/tests/test_mcp_registration_wiring_tests_2.py:240-251 |

## 260815-DAG-L3 `closeout_queue` Registration

This registration surface now exposes `closeout_queue` with the strict request model and describes
the manager/orchestrator authority split, revision/idempotency protocol, exact curator and planning
evidence, deterministic ordering, atomic blocker semantics, bounded durable artifact, and
task-addressed lifecycle ownership. Since 260815-DAG-L13 the docstring also states the degraded
read contract: `status` never fails on a missing executionGraph or malformed registers (it reports
mode, registers, laneOwner, and legalNextOperations), stale-base closeout/integration refusals name
`worktree_sync` as the recovery, a completed landing reports stale-by-evidence siblings, an
in-flight atomic block owns the landing lane for its lifetime, acquisition reports in-flight
organizational leafs as facts, and a certified candidate no longer occupies the lane. Since
260815-DAG-L16 the docstring states the caller rule exactly: the caller is the plane-injected
hosted seat when one exists; an ambient caller with no plane seat declares `caller` (role +
task_document_ref) instead, and the same queue authorization validates it identically.

## 260815-DAG Master Full-Gate Repair

The `task_doc` tool's long docstring moved to the module-level `_TASK_DOC_TOOL_DESCRIPTION` constant, passed through `@server.tool(description=...)` (wire-contract conformance); the import of `task_doc_tools` follows the move to `application/task_docs/`. The registered tool surface is unchanged.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: `task_doc` description extracted to a module constant; imports updated to `application/task_docs/task_doc_tools`. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: the `task_doc` declaration gains `branch_addressed`
  (policy-gated direct-execution opt-in for `record_route_review`), and the `closeout_queue`
  docstring caller rule is updated to the declared-caller reality (L16-R2). Verified at code
  commit a9d50e08.


- 2026-08-20T04:28+02:00 — 260815-DAG-L14: the `task_doc` docstring and operation vocabulary add
  `attach_master`/`detach_master`/`linkage_report` (typed masterRef batch, symmetric detach,
  read-only linkage facts); a sprint `get` carries `linkageFacts`. Verified at code commit 2f494982.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: `task_doc` docstring drops the removed
  `migrate_execution_topology` operation, documents the graph-less `author_execution_graph`
  bootstrap, the scaffolded planning registers, and the register write-time shape validation; the
  `closeout_queue` docstring documents the degraded status readout and the sync-first recovery
  naming. Verification remains closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: the `task_doc` docstring gains the
  `author_execution_graph` operation (typed mutation batch, segment-sampling endpoints,
  Judgment-Register provenance, partition refusals, fact-only placement/numbering reporting) and
  now scopes `migrate_execution_topology` as the lump-only bootstrap. Verification remains
  closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: registered and documented the public closeout-queue
  tool contract; verification remains closeout-owned.

- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: the public migration description
  now spells out the nested master reference/nature cells, graph node and reasoned-edge cells,
  and the classification plus wave surfaces returned by preview.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: the public task-doc tool contract documents the
  previewable multi-document execution-topology migration payload and derived-wave response.
- 2026-08-14T06:32+02:00 — No public schema impact: L23 keeps task registrations task-addressed
  while the application layer owns reopen planning, lineage, and route-review admission.
  Verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.
- 2026-08-04T16:28:49+02:00 — 260731-EFA-L6 S18-B11 same-reviewer residual correction: rebound the complete `skip_step` vocabulary and semantics to the registration docstring span, with explicit anchors for the operation member, exact-step shape, one-unit completion, intentional-skip provenance, non-cascade, nonblank-reason, and status-clearing predicates. Verification metadata unchanged.

- 2026-08-02T21:07:18+02:00 — 260731-EFA-L6 curator W2-B10: repaired 8 citation findings (4 reference rows); scoped recheck clean.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The three task
  declarations moved out of `server.py`; `task_doc` now packs `TaskDocTarget`/`TaskDocEdit` and
  `lifecycle_finalize_task` packs `FinalizeTaskDocs`. Verification metadata pinned to the pre-change
  commit until closeout stamps the L2 code commit.
