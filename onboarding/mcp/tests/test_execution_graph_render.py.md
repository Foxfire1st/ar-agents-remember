# mcp/tests/test_execution_graph_render.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_execution_graph_render.py`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-20T10:45+02:00                           |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62`       |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00                        |
| governingOverview      | `overview.md`                                    |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the deterministic mermaid execution-graph render (260815-DAG-L12 R1): the
`## Execution Graph` section emits a fenced `flowchart TD` diagram — one subgraph per
master box (title-labeled), one node per leaf (truncated title), atomic masters as single
lump nodes, labeled edges — ordered by derived wave then node order, with the compact
machine-readable Nodes / Dependencies / Derived Waves lists staying alongside.

## Code Commentary

### Logic

`ExecutionGraphMermaidRenderTests` renders a sprint `TaskDocument` and slices the
`## Execution Graph` section (`_graph_section`) and the mermaid fence (`_mermaid_block`):
subgraph-per-master with leaf nodes and a lump; ref-key/leaf-id fallbacks when no titles
join; byte-stable determinism and wave ordering across two renders; pipe/quote escaping in
edge reasons (`&#124;`/`&#34;`); ellipsis truncation of long labels; and a bare-ref
endpoint resolving to a single-segment subgraph id. `ExecutionGraphTitlesReadTests` forces
the disk-backed `read_graph_titles` join — real master documents produce joined titles,
and missing/invalid masters degrade to fallbacks without raising.

### Invariants And Boundaries

- Determinism is a contract: identical inputs produce byte-identical markdown.
- The render reads a validated model; the JSON is never parsed back.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The mermaid render forcing suite. | `ExecutionGraphMermaidRenderTests` | mcp/tests/test_execution_graph_render.py:50-223 |
| The title-read forcing suite. | `ExecutionGraphTitlesReadTests` | mcp/tests/test_execution_graph_render.py:226-283 |
| The renderer under test. | `_execution_graph_lines` | mcp/src/agents_remember/tasks/render.py:173-213 |
| The shared title join. | `read_graph_titles` | mcp/src/agents_remember/tasks/execution_graph_titles.py:60-75 |

## Cross-Repo References

No cross-repository implementation source governs this file.

## Update History

- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1): mermaid flowchart-TD render

forcing — subgraph/lump shape, title fallbacks, determinism, escaping, truncation, and the

disk-backed title join. Verified at code commit b7f2c8e2.



- 2026-08-20T10:45+02:00 — Created for 260815-DAG-L12 (R1): mermaid flowchart-TD render
  forcing — subgraph/lump shape, title fallbacks, determinism, escaping, truncation, and the
  disk-backed title join. Verified at code commit b7f2c8e2.
