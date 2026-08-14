# mcp/src/agents_remember/serving/codex_app_server_threads.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_threads.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Multiplexed thread demux for one Codex app-server connection.

## Code Commentary

### Logic

Module-level surface:

- `CodexThreadState` (class, lines 32-66) — Per-thread demux state on one multiplexed app-server connection.
- `CodexThreadRegistry` (class, lines 69-300) — The threads on one connection, their agent identities, and the item->thread index.

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
| Defines the class `CodexThreadState` (lines 32-66) — Per-thread demux state on one multiplexed app-server connection.. | `CodexThreadState` | mcp/src/agents_remember/serving/codex_app_server_threads.py:31-66 |
| Defines the class `CodexThreadRegistry` (lines 69-300) — The threads on one connection, their agent identities, and the item->thread index.. | `CodexThreadRegistry` | mcp/src/agents_remember/serving/codex_app_server_threads.py:69-300 |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
