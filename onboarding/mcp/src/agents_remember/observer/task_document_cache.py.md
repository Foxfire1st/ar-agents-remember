# mcp/src/agents_remember/observer/task_document_cache.py

## Governing Overview

[Observer overview](overview.md)

## Purpose

Avoids reparsing unchanged task-document JSON while retaining only live files under a bounded
number of task roots.

## Code Commentary

### Logic

`TaskDocumentPayloadCache.payloads` keys entries by root and source path, validates a cached parse
against `mtime_ns`, size, and `ctime_ns`, parses only misses, and deletes entries absent from the
current path enumeration. Roots form an eight-entry LRU by default, covering standalone
diagnostics without turning temporary coordination roots into unbounded process state.

### Conventions

The caller supplies the JSON reader and path enumeration. The serialized projection worker is the
single owner, so no lock is needed.

### Invariants And Boundaries

- A changed stat identity forces a reparse.
- Deleted or unreadable files leave no retained payload.
- Root count is explicitly bounded and configurable for tests.
- Cached payloads are reused only within the exact tasks root.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Task-document enumeration and parsing consumer. [1]

### Cross-Repo References

No meaningful cross-repository references found.
