# mcp/src/agents_remember/tasks/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-26T20:18+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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

- Consumers (the `task_doc` controller, the observer S7 reader) import from
  `agents_remember.tasks`; keep the facade re-exporting the full set.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The schema, renderer, and store owned by this package. | [document.py](agents-remember/mcp/src/agents_remember/tasks/document.py); [render.py](agents-remember/mcp/src/agents_remember/tasks/render.py); [store.py](agents-remember/mcp/src/agents_remember/tasks/store.py) |

## Series-Contract Notes

The package facade exports `TaskEnclosureRef` so task-document callers can construct `enclosures[]` references without importing the model internals directly.

## Update History

- 2026-06-26T20:18+02:00 — Task 21 task-doc master sync: facade now exports `write_task_docs` so the
  controller can persist coupled leaf/master task-document updates through the package surface. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the task package now exports `TaskEnclosureRef`, the JSON task-doc reference that binds leaf documents to enclosure `series-contract.md` paths. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:03 — Slice 3c reopened (R4): facade now also re-exports `HeaderNote` (the extra-header-line model). Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T03:17 — Slice 3c reopened (R1): facade now also re-exports `series_total`/`series_done` (the master series-progress helpers). Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: facade now also re-exports `SubTaskRef` and `Section` (the master series-index + section models). Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1 as the task-document package facade. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
