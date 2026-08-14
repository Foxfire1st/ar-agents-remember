# mcp/src/agents_remember/tasks/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `aeca9a2839c965218a61a3040e15cb84367ebeca` |
| lastVerifiedCommitDate | 2026-08-14T13:35:55+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Public import surface for the JSON-primary task-document package: the schema, the
renderer, and the single/batch store helpers.

## Code Commentary

### Logic

Re-exports `document` (`TaskDocument` + the node models incl. `SubTaskRef`/`Section`/`HeaderNote`,
the `DocKind`/`DocStatus`/`StepStatus` Literals, `TASK_DOCUMENT_SCHEMA`, and the
`step_total`/`step_done`/`current_step` + R1 `series_total`/`series_done` helpers), `render`
(`render_markdown`), and
`store` (`read_task_doc`/`write_task_doc`/`write_task_docs`/`json_path_for`/`markdown_path_for`/
`doc_stem`). `__all__` lists the full public set.

### Invariants And Boundaries

- Consumers (the `task_doc` application entry point, the observer S7 reader) import from
  `agents_remember.tasks`; keep the facade re-exporting the full set.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The schema, renderer, and store owned by this package. | "class TaskDocument(_Doc):"; "def render_markdown(doc: TaskDocument) -> str:"; "def write_task_docs(task_root: Path" | mcp/src/agents_remember/tasks/document.py:182-182; mcp/src/agents_remember/tasks/render.py:29-29; mcp/src/agents_remember/tasks/store.py:40-40 |

## Series-Contract Notes

The package facade exports `TaskEnclosureRef` so task-document callers can construct `enclosures[]` references without importing the model internals directly.

## Update History
- 2026-08-14T06:34+02:00 — L23 final candidate review: task exports expose the canonical document
  and reopen-planning helpers used by lineage/start admission; no second task identity is added.

- 2026-08-04T18:31+02:00 — 260731-EFA-L6 S18-B14 curator: re-derived 2 stale citation ranges (`class TaskDocument` document.py:141, `def render_markdown` render.py:28); scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 1 citation row with exact anchors and current source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-26T20:18+02:00 — Task 21 task-doc master sync: facade now exports `write_task_docs` so the
  controller can persist coupled leaf/master task-document updates through the package surface. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the task package now exports `TaskEnclosureRef`, the JSON task-doc reference that binds leaf documents to enclosure `series-contract.md` paths. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:03 — Slice 3c reopened (R4): facade now also re-exports `HeaderNote` (the extra-header-line model). Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T03:17 — Slice 3c reopened (R1): facade now also re-exports `series_total`/`series_done` (the master series-progress helpers). Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: facade now also re-exports `SubTaskRef` and `Section` (the master series-index + section models). Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1 as the task-document package facade. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
