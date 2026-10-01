# mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py

## Governing Overview

[task-doc application overview](overview.md)

## Purpose

Own the current graph-bearing publication-batch cardinality and the one in-memory title-context
builder shared by execution-topology authoring and sprint linkage. This is the fail-fast boundary
that prevents an unsupported multi-graph batch from acquiring accidental first-document semantics.

## Code Commentary

### Logic

- `require_single_graph_document(documents)` inspects the complete submitted batch, returns its
  sole graph-bearing document or `None`, and raises typed `TaskDocError` when the count exceeds one.
- `build_publication_batch_graph_titles(documents)` delegates to that same assertion, builds the
  master map from the exact in-memory batch, and calls the tasks-layer `build_graph_titles` only
  after zero/one cardinality is established.
- `GraphPublicationDocument` keeps the application tuple shape explicit:
  `(TaskDocumentRef, task root, TaskDocument)`.

The shared title join qualifies leaf titles by `(master ref, leaf id)`, using each master
subtask row’s number. Missing in-memory master documents contribute no titles; another master’s
same-numbered leaf cannot fill the gap.

cit:([`build_graph_titles`], mcp/src/agents_remember/tasks/execution_graph_titles.py:37-59)

### Conventions

Cardinality is checked from pure submitted data before any publisher, projection refresh, queue
invalidation, or disk write. Callers do not catch the refusal and retry documents separately.

### Invariants And Boundaries

- One publication batch currently contains at most one graph-bearing document.
- The module owns no disk read and no mutation. Ordinary disk-backed title reads stay inside the
  task publisher's protected callback; this owner handles only pure batch shape and in-memory joins.
- There is no first-graph fallback, per-document compatibility reader, or speculative multi-graph
  map. A future demonstrated multi-graph transaction must replace this single-context contract.

### Todos

Re-evaluate the zero/one invariant only if a real atomic task-publication transaction demonstrates
more than one graph-bearing document.

## Evidence

### Docs References

No Domain Documentation sources are configured for this repository-internal application seam.

No relevant external documentation was available after checking the configured source registry.

### Repo-Internal References

The source, its ordinary-publication consumer, and focused forcing suite define the contract.

- The central owner refuses more than one graph document and builds the one in-memory title context. [1]
- Ordinary publication checks the same cardinality before it constructs the task transaction. [2]
- Focused proof covers zero/one support, two-graph no-write refusal, and order-independent errors. [3]

### Cross-Repo References

No cross-repository boundary is owned by this file.

No meaningful cross-repository references were found.
