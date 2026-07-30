# mcp/src/agents_remember/observer/task_document_cache.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/observer/task_document_cache.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Task-document enumeration and parsing consumer. | [snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |
| Cache scaling regressions. | [test_task_document_payload_cache.py](agents-remember/mcp/tests/test_task_document_payload_cache.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created onboarding for the
  task-document stat-identity cache and its root/live-path bounds. Verification metadata remains
  blank until commit.
