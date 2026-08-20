# mcp/src/agents_remember/tasks/store.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/store.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-20T10:45+02:00 |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62` |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00 |
| governingOverview      | `overview.md`                              |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Read and write one or more task documents: the JSON is the source, the markdown a render.

## Code Commentary

### Logic

`write_task_doc(task_root, doc)` delegates through `write_task_docs` to
`write_task_doc_batch([(task_root, doc)])`. The batch form accepts documents under distinct task
roots, creates each root, prepares every JSON payload
(`model_dump_json(by_alias=True, exclude_none=True, indent=2)`) and rendered markdown
string before any write, rejects duplicate JSON/markdown output targets, snapshots every prior
destination byte-for-byte, then publishes through the kernel's atomic-write primitive. If a write
raises, it restores every prior file (including prior absence) before re-raising; this is
exception-failure rollback across roots, not a claim of multi-file crash atomicity.
`read_task_doc(json_path)` loads via
`model_validate_json` — the markdown is never parsed back. `doc_stem(doc)` is `task`
for a `light` **or `master`** document and `<slug>` for a `subTask`; `json_path_for` /
`markdown_path_for` derive the sibling `.json` / `.md` paths in the task folder.

### Invariants And Boundaries

- Each destination replacement is atomic; the JSON is authoritative and the markdown is always a
  fresh render. A multi-document batch adds exact rollback for raised publication failures.
- Batch writes prepare all payloads before replacing any file. The duplicate-target guard is necessary
  because leaf/master coupled writes would otherwise risk overwriting one prepared document with another.
- Reads go through `model_validate_json`; never reconstruct a document from markdown.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The model written/read. | `TaskDocument` | mcp/src/agents_remember/tasks/document.py:602-716 |
| The renderer invoked on every write. | `render_markdown` | mcp/src/agents_remember/tasks/render.py:20-40 |
| The application entry point uses batch writes when a leaf mutation also changes its parent master row. | `task_doc_tool` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:191-284 |


## 260815-DAG-L12 Title Threading

`write_task_docs` and `write_task_doc_batch` gained the optional `graph_titles` keyword (L12-R1/R4): the batch passes it to `render_markdown` for every document that carries an `executionGraph`, so a sprint's `task.md` mermaid boxes are labeled with real master/leaf titles at publish time. `write_task_doc` delegates through unchanged; the atomic prepare/publish/rollback contract is untouched.


## Update History


- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   `write_task_docs`/`write_task_doc_batch` thread the optional `graph_titles` join into the renderer (L12-R1/R4). Verified at code commit b7f2c8e2.

- 2026-08-20T04:52+02:00 — 260815-DAG-L14 curator: re-read the `TaskDocument` claim — the persisted
  model gained sprint `seats` and typed `masterRef` rows; wording retained, citation regenerated to
  the current class lines, stamp advanced to code commit 2f494982.


- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: `write_task_doc_batch` generalizes the existing
  rollback-safe prepared write to documents across multiple task roots, enabling one atomic sprint migration.
- 2026-08-02T21:40:21+02:00 — 260731-EFA-L6 curator W2-B10: repaired 6 citation findings (3 reference rows); scoped recheck clean.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-26T20:18+02:00 — Task 21 task-doc master sync: added `write_task_docs`, a prepare-all-then-write
  batch path used for coupled leaf/master persistence, with a duplicate output-target guard. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: `doc_stem` maps a `master` to `task` (so a master series wrapper is `task.json`/`task.md`, beside the slice `<slug>` docs). Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1: the atomic JSON+markdown task-document store. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
