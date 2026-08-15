# mcp/src/agents_remember/mcp/registration/tasks.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/mcp/registration/tasks.py`       |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-08-02T01:05+02:00                                    |
| lastVerifiedCommitHash | `28a66feae742bf02fe4b647388b220f921cc7007`                |
| lastVerifiedCommitDate | 2026-08-15T03:44:49+02:00|
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
`set_step` | `skip_step` | `set_subtask` | `remove_subtask` | `set_section` | `append_decision` | `set_field` |
`get`. The JSON document is the source of truth; `task.md` / `<slug>.md` is a generated render that
is never parsed back. Everything mutates except `operation='get'`, and `dry_run=true` builds and
validates and returns `rendered`/`diff`/`wouldLose` **without** writing — the preview before
adopting a hand-written `.md`. Master (`kind:"master"`) documents use `set_subtask` /
`remove_subtask` / `set_section`; `remove_subtask` also deletes the leaf doc (json+md) unless
`subtask.keep_file`; `set_step` is leaf-only. `skip_step` takes an exact existing step and a nonblank
reason, marks only that unit done, records intentional-skip provenance, and does not cascade; an
        explicit status clears an earlier skip disposition cit:(["operation: 'create'", "exact existing step", "sets only that unit done", "records intentional-skip provenance without cascading", "A nonblank reason is required.", "explicit status clears an earlier skip disposition"], mcp/src/agents_remember/mcp/registration/tasks.py:91-91; mcp/src/agents_remember/mcp/registration/tasks.py:100-102).

The body splits that into two objects: `TaskDocTarget(repo_id, task_name, contract_path, slug)` —
which document to edit — and `TaskDocEdit(fields, step, decision, subtask, section)` — what the edit
is. `operation` and `dry_run` stay separate arguments. A read (`operation='get'`) leaves every edit
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
| `FinalizeTaskDocs`. | `FinalizeTaskDocs` | mcp/src/agents_remember/application/worktree_tools.py:522-529 |
| Target/edit splitting and the unset-edit read proved through a live server. | `test_task_doc_splits_the_document_target_from_the_edit`, `test_task_doc_leaves_every_edit_slot_unset_for_a_read` | mcp/tests/test_mcp_registration_wiring_tests_2.py:182-217; mcp/tests/test_mcp_registration_wiring_tests_2.py:219-230 |

## Update History

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
