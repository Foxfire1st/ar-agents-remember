# mcp/tests/test_memory_tool_enclosure_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_tool_enclosure_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6-R29: which memory tree the three memory tools act on, proved by acting on it.

## Code Commentary

### Logic

Module-level surface:

- `_Enclosure` (class, lines 65-72) — One workspace holding both trees a memory tool could resolve, and the contract.
- `_tree_snapshot` (function, lines 75-81) — Every file under ``root`` by relative posix path and content -- the untouched proof.
- `_enclosure` (function, lines 84-154)
- `EnclosureScopeTestCase` (class, lines 157-168) — One temporary workspace per test, holding both trees.
- `RouteIndexRefreshWritesTheNamedTreeTests` (class, lines 171-209) — The urgent one: it writes, so where it writes is the whole question.
- `MemoryQualityCheckReadsTheNamedTreeTests` (class, lines 212-232) — The closeout gate, now runnable on the change-set before the manager runs it.
- `DriftCheckReadsTheNamedTreesTests` (class, lines 235-253) — Drift needs BOTH roots right: the leaf's onboarding and the leaf's code.
- `RefusalTests` (class, lines 256-325) — Every way the enclosure cannot be honoured refuses. None of them falls back.
- `_replaced` (function, lines 328-330) — A copy of the contract with cells overridden, written to disk by the caller.
- `_config_without_memory_root` (function, lines 333-336) — The settings shape whose repository scope carries no memory root at all.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `_Enclosure` (lines 65-72) — One workspace holding both trees a memory tool could resolve, and the contract.. | `_Enclosure` | mcp/tests/test_memory_tool_enclosure_scope.py:65-72 |
| Defines the function `_tree_snapshot` (lines 75-81) — Every file under ``root`` by relative posix path and content -- the untouched proof.. | `_tree_snapshot` | mcp/tests/test_memory_tool_enclosure_scope.py:75-81 |
| Defines the function `_enclosure` (lines 84-154). | `_enclosure` | mcp/tests/test_memory_tool_enclosure_scope.py:84-154 |
| Defines the class `EnclosureScopeTestCase` (lines 157-168) — One temporary workspace per test, holding both trees.. | `EnclosureScopeTestCase` | mcp/tests/test_memory_tool_enclosure_scope.py:157-168 |
| Defines the class `RouteIndexRefreshWritesTheNamedTreeTests` (lines 171-209) — The urgent one: it writes, so where it writes is the whole question.. | `RouteIndexRefreshWritesTheNamedTreeTests` | mcp/tests/test_memory_tool_enclosure_scope.py:171-209 |
| Defines the class `MemoryQualityCheckReadsTheNamedTreeTests` (lines 212-232) — The closeout gate, now runnable on the change-set before the manager runs it.. | `MemoryQualityCheckReadsTheNamedTreeTests` | mcp/tests/test_memory_tool_enclosure_scope.py:212-232 |
| Defines the class `DriftCheckReadsTheNamedTreesTests` (lines 235-253) — Drift needs BOTH roots right: the leaf's onboarding and the leaf's code.. | `DriftCheckReadsTheNamedTreesTests` | mcp/tests/test_memory_tool_enclosure_scope.py:235-253 |
| Defines the class `RefusalTests` (lines 256-325) — Every way the enclosure cannot be honoured refuses. None of them falls back.. | `RefusalTests` | mcp/tests/test_memory_tool_enclosure_scope.py:256-325 |
| Defines the function `_replaced` (lines 328-330) — A copy of the contract with cells overridden, written to disk by the caller.. | `_replaced` | mcp/tests/test_memory_tool_enclosure_scope.py:331-333 |
| Defines the function `_config_without_memory_root` (lines 333-336) — The settings shape whose repository scope carries no memory root at all.. | `_config_without_memory_root` | mcp/tests/test_memory_tool_enclosure_scope.py:333-336 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
