# mcp/tests/test_codex_native_history.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Bounded native-history paging and typed refusal propagation.

## Code Commentary

### Logic

Opaque continuation consumes each source page once with one-item bounded requests. A two-cursor cycle terminates before re-requesting a page. A recognized bounded-RPC failure does not silently fall back; oversized materialized responses and both IPC clients retain the typed limit outcome.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Materialization ceilings are distinct from transport fuses. The remaining cases do not separately establish expired-cursor or legacy fallback behavior.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Bounded items are probed and opaque cursor consumes each source page once. [1]
- Two cursor cycle terminates typed without re requesting a source page. [2]
- Recognized bounded rpc failure never silently falls back. [3]
- Source response over post transport materialization ceiling is typed. [4]
- Native history limit outcome survives both control ipc clients. [5]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
