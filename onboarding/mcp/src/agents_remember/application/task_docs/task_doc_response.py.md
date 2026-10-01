# mcp/src/agents_remember/application/task_docs/task_doc_response.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Own shared task-document result and dry-run rendering.

## Code Commentary

### Logic

The helpers render applied task mutations, preview JSON/Markdown diffs, progress counts, graph titles, and optional master-sync effects from the same candidate TaskDocument used by publication.

### Invariants And Boundaries

- Preview and apply expose the same candidate task truth.
- Rendering does not consult queue rows or operation state.
- Graph and master-sync details are response evidence, not publication authority.

### Todos

None recorded.

## Evidence

### Docs References

No configured domain-documentation source applies to this repository-internal route.

### Repo-Internal References

- Applied results and previews share one response shape. [1]
- Graph-title and master-sync helpers render bounded supporting evidence. [2]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
