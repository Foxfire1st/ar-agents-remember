# mcp/src/agents_remember/mcp/registration/tasks.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/mcp/registration/tasks.py`       |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-07-31T15:31+02:00                                    |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                             |

## Governing Overview

[registration route overview](overview.md)

## Purpose

`register_task_tools(server, config)` declares the task-document authoring tool plus the two
task-state transitions: `task_reopen`, `lifecycle_finalize_task`, `task_doc`.

## Code Commentary

### Logic

`task_doc` is the JSON-primary authoring tool and carries the longest docstring on the surface,
because the operation vocabulary is not in the types: `create` | `replace` | `set_status` |
`set_step` | `set_subtask` | `remove_subtask` | `set_section` | `append_decision` | `set_field` |
`get`. The JSON document is the source of truth; `task.md` / `<slug>.md` is a generated render that
is never parsed back. Everything mutates except `operation='get'`, and `dry_run=true` builds and
validates and returns `rendered`/`diff`/`wouldLose` **without** writing — the preview before
adopting a hand-written `.md`. Master (`kind:"master"`) documents use `set_subtask` /
`remove_subtask` / `set_section`; `remove_subtask` also deletes the leaf doc (json+md) unless
`subtask.keep_file`; `set_step` is leaf-only.

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
  `controllers/task_doc_tools.py` and `controllers/worktree_tools.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The `task_doc` / `task_reopen` payload builders. | [tools/task_doc.py](agents-remember/mcp/src/agents_remember/mcp/tools/task_doc.py) |
| The finalize builder. | [tools/lifecycle_finalize.py](agents-remember/mcp/src/agents_remember/mcp/tools/lifecycle_finalize.py) |
| `TaskDocTarget`, `TaskDocEdit`. | [controllers/task_doc_tools.py](agents-remember/mcp/src/agents_remember/controllers/task_doc_tools.py) |
| `FinalizeTaskDocs`. | [controllers/worktree_tools.py](agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py) |
| Target/edit splitting and the unset-edit read proved through a live server. | [test_mcp_registration_wiring.py](agents-remember/mcp/tests/test_mcp_registration_wiring.py) |

## Update History

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The three task
  declarations moved out of `server.py`; `task_doc` now packs `TaskDocTarget`/`TaskDocEdit` and
  `lifecycle_finalize_task` packs `FinalizeTaskDocs`. Verification metadata pinned to the pre-change
  commit until closeout stamps the L2 code commit.
