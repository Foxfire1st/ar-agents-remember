# mcp/src/agents_remember/observer/task_document_cache.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/observer/task_document_cache.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-31T00:00+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Task-document enumeration and parsing consumer. | `_iter_task_document_payloads` | mcp/src/agents_remember/observer/snapshots.py:147-165 |
| Cache scaling regressions. | `TaskDocumentPayloadCacheTests` | mcp/tests/test_task_document_payload_cache.py:18-96 |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 4 citation finding(s); scoped recheck clean.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/observer/task_document_cache.py` since the L2 base commit is the whole-
  tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created onboarding for the
  task-document stat-identity cache and its root/live-path bounds. Verification metadata remains
  blank until commit.
