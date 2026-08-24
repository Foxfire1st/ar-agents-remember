# mcp/tests/test_execution_graph_render.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_execution_graph_render.py`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-24T13:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the deterministic Mermaid execution-graph render (260815-DAG-L12 R1, hardened by
260821-DAGQC-L1): the
`## Execution Graph` section emits a fenced `flowchart TD` diagram — one subgraph per
master box (title-labeled), one node per leaf (truncated title), atomic masters as single
lump nodes, labeled edges — using collision-free ordinal private ids and human-readable
labels, ordered by derived wave then node order, with the compact
machine-readable Nodes / Dependencies / Derived Waves lists staying alongside.

## Code Commentary

### Logic

`ExecutionGraphMermaidRenderTests` renders a sprint `TaskDocument` and slices the
`## Execution Graph` section (`_graph_section`) and the mermaid fence (`_mermaid_block`):
subgraph-per-master with leaf nodes and a lump; ref-key/leaf-id fallbacks when no titles
join; byte-stable determinism and wave ordering across two renders; pipe/quote escaping in
edge reasons (`&#124;`/`&#34;`); ellipsis truncation of long labels; and a bare-ref
endpoint resolving to a single-segment subgraph id. The sanitizer-collision regression proves
labels such as `a/b` and `a?b` receive distinct ordinal Mermaid ids, edges reuse the same
allocated ids, and changing human labels does not change private identity.
`ExecutionGraphTitlesReadTests` forces the disk-backed `read_graph_titles` join. It also proves
that equal local leaf numbers under two masters remain keyed by `(TaskDocumentRef, leaf id)`, the
master's own title wins regardless of map order, and a missing owning master falls back to the raw
leaf id rather than borrowing another master's title. Missing/invalid master documents retain the
existing empty-map fallback without raising.

### Invariants And Boundaries

- Determinism is a contract: identical inputs produce byte-identical markdown.
- Mermaid identity is allocated from graph declaration order; labels never become ids, and all
  declarations and edge endpoints share the same allocation.
- Leaf-title identity is `(owning master TaskDocumentRef, leaf id)`; a same-numbered row under a
  different master is not a title candidate.
- The render reads a validated model; the JSON is never parsed back.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The Mermaid render forcing suite includes ordinal private ids, sanitizer-collision resistance, edge endpoint reuse, and label-independence. | `ExecutionGraphMermaidRenderTests` | mcp/tests/test_execution_graph_render.py:51-298 |
| The title-join suite proves master-qualified same-numbered leaf titles and the no-borrow fallback. | `ExecutionGraphTitlesReadTests` | mcp/tests/test_execution_graph_render.py:300-401 |
| The renderer allocates declaration-order private ids and reads qualified leaf titles. | `_mermaid_identity_map`; `_execution_graph_lines` | mcp/src/agents_remember/tasks/render.py:204-245; mcp/src/agents_remember/tasks/render.py:283-384 |
| The shared title join keys leaf titles by owning ref and local id. | `SprintGraphTitles`; `build_graph_titles`; `read_graph_titles` | mcp/src/agents_remember/tasks/execution_graph_titles.py:15-79 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-24T13:43+02:00 — 260821-DAGQC-L1: documented collision-free ordinal Mermaid identity,
  qualified same-number leaf-title ownership, and the explicit no-borrow fallback proofs.
  Verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1): mermaid flowchart-TD render

forcing — subgraph/lump shape, title fallbacks, determinism, escaping, truncation, and the

disk-backed title join. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1): mermaid flowchart-TD render
  forcing — subgraph/lump shape, title fallbacks, determinism, escaping, truncation, and the
  disk-backed title join. Verified at code commit b7f2c8e2.
