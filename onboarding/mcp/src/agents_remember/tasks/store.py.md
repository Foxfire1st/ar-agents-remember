# mcp/src/agents_remember/tasks/store.py

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

Since 260831-CCR (commit `99dc249b`) the batch writer refuses to publish a document whose route
review carries a missing or stale task intent: `_require_publishable_task_document` (line 221)
runs on every document before the batch prepares target paths and calls
`require_task_intent_identity(review.taskIntent, owner="route-review",
next_action="record_route_review")` (line 225-227). A legacy review with no canonical identity can
therefore no longer be written back to disk as current task truth.

### Invariants And Boundaries

- Each destination replacement is atomic; the JSON is authoritative and the markdown is always a
  fresh render. A multi-document batch adds exact rollback for raised publication failures.
- Batch writes prepare all payloads before replacing any file. The duplicate-target guard is necessary
  because leaf/master coupled writes would otherwise risk overwriting one prepared document with another.
- Reads go through `model_validate_json`; never reconstruct a document from markdown.
- A document carrying a route review without canonical task intent is not publishable; the store
  refuses before any file is touched.

## Evidence

### Repo-Internal References

- The task-document model the store writes, and reads back through `model_validate_json`. [1]
- The renderer invoked on every write. [2]
- The application entry point uses batch writes when a leaf mutation also changes its parent master row. [3]
- Publishability gate refusing legacy review intent. [4]
- The shared identity rejection seam it calls. [5]


## 260815-DAG-L12 Title Threading

`write_task_docs` and `write_task_doc_batch` gained the optional `graph_titles` keyword (L12-R1/R4): the batch passes it to `render_markdown` for every document that carries an `executionGraph`, so a sprint's `task.md` mermaid boxes are labeled with real master/leaf titles at publish time. `write_task_doc` delegates through unchanged; the atomic prepare/publish/rollback contract is untouched.


## 260821-CLIVE Final Store Contract

The current source seams include `TaskDocSourceSnapshot`, `TaskDocSourceReadError`, and `doc_stem`.
Exact task-document bytes and absence are explicit publication inputs so stale before-state fails
precisely. The store now also owns rollback-safe write-plus-remove mechanics, but it still does not
compute projection blast radius or publish refresh effects; those remain application concerns after
canonical task publication.

### Reconciled Source Evidence

- The current module exposes `TaskDocSourceSnapshot`, `TaskDocSourceReadError`, `doc_stem` at this ownership boundary. [6]

## 260821-CLIVE Atomic Parent-Write And Child-Removal

`write_task_docs_and_remove` publishes prepared task documents and removes exact sibling source
paths as one rollback-safe file set. It forbids write/removal overlap, snapshots every touched path,
and restores exact prior bytes if any replacement or unlink fails; a rollback failure is loud.
The surrounding task-publication CAS provides serialization. This prevents discard-unstarted from
exposing a parent audit without removal or deleting the child without the audit.

## CCR-R02@v2 Publishability Boundary

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, newly published containers must
carry the exact canonical intent identity and writers may not emit the sentinel. The batch writer
enforces this for route-review-bearing documents, so a legacy review cannot be persisted as current.
