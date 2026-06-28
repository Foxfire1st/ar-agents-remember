# mcp/src/agents_remember/tasks/store.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/store.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-26T20:18+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Read and write one or more task documents: the JSON is the source, the markdown a render.

## Code Commentary

### Logic

`write_task_doc(task_root, doc)` delegates to `write_task_docs(task_root, [doc])`.
`write_task_docs` creates the task root, prepares every JSON payload
(`model_dump_json(by_alias=True, exclude_none=True, indent=2)`) and rendered markdown
string before any write, rejects duplicate JSON/markdown output targets, then writes
each prepared path through `_atomic_write` (temp file + `os.replace`, the same idiom
the observer drift snapshot uses). `read_task_doc(json_path)` loads via
`model_validate_json` — the markdown is never parsed back. `doc_stem(doc)` is `task`
for a `light` **or `master`** document and `<slug>` for a `subTask`; `json_path_for` /
`markdown_path_for` derive the sibling `.json` / `.md` paths in the task folder.

### Invariants And Boundaries

- Both files are written atomically; the JSON is authoritative and the markdown is
  always a fresh render of it.
- Batch writes prepare all payloads before replacing any file. The duplicate-target guard is necessary
  because leaf/master coupled writes would otherwise risk overwriting one prepared document with another.
- Reads go through `model_validate_json`; never reconstruct a document from markdown.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The model written/read. | [document.py](agents-remember/mcp/src/agents_remember/tasks/document.py) |
| The renderer invoked on every write. | [render.py](agents-remember/mcp/src/agents_remember/tasks/render.py) |
| The controller uses batch writes when a leaf mutation also changes its parent master row. | [task_doc_tools.py](agents-remember/mcp/src/agents_remember/controllers/task_doc_tools.py) |

## Update History

- 2026-06-26T20:18+02:00 — Task 21 task-doc master sync: added `write_task_docs`, a prepare-all-then-write
  batch path used for coupled leaf/master persistence, with a duplicate output-target guard. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: `doc_stem` maps a `master` to `task` (so a master series wrapper is `task.json`/`task.md`, beside the slice `<slug>` docs). Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1: the atomic JSON+markdown task-document store. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
