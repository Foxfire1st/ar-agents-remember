# mcp/src/agents_remember/serving/operator_inbox_posts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/operator_inbox_posts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Persist and optionally deliver one operator-inbox post.

## Code Commentary

### Logic

Module-level surface:

- `OperatorInboxPostContext` (class, lines 62-67) — Persistence and delivery collaborators for one operator-inbox post.
- `_redelivery_floor_seconds` (function, lines 70-73)
- `_delivery_catalog` (function, lines 76-83)
- `_signal_route` (function, lines 86-101)
- `_post_address` (function, lines 104-119)
- `_post_catalog` (function, lines 122-130)
- `_dispatch_entry_fields` (function, lines 133-141)
- `_persist_post` (function, lines 144-175)
- `_deliver_post` (function, lines 178-199)
- `post_operator_inbox_entry` (function, lines 202-288) — Create, persist, deliver, and describe one post through the shared real owner.

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
| Defines the class `OperatorInboxPostContext` (lines 62-67) — Persistence and delivery collaborators for one operator-inbox post.. | `OperatorInboxPostContext` | mcp/src/agents_remember/serving/operator_inbox_posts.py:59-65 |
| Defines the function `_redelivery_floor_seconds` (lines 70-73). | `_redelivery_floor_seconds` | mcp/src/agents_remember/serving/operator_inbox_posts.py:68-73 |
| Defines the function `_delivery_catalog` (lines 76-83). | `_delivery_catalog` | mcp/src/agents_remember/serving/operator_inbox_posts.py:76-83 |
| Defines the function `_signal_route` (lines 86-101). | `_signal_route` | mcp/src/agents_remember/serving/operator_inbox_posts.py:86-101 |
| Defines the function `_post_address` (lines 104-119). | `_post_address` | mcp/src/agents_remember/serving/operator_inbox_posts.py:104-119 |
| Defines the function `_post_catalog` (lines 122-130). | `_post_catalog` | mcp/src/agents_remember/serving/operator_inbox_posts.py:171-179 |
| Defines the function `_dispatch_entry_fields` (lines 133-141). | `_dispatch_entry_fields` | mcp/src/agents_remember/serving/operator_inbox_posts.py:182-190 |
| Defines the function `_persist_post` (lines 144-175). | `_persist_post` | mcp/src/agents_remember/serving/operator_inbox_posts.py:193-202 |
| Defines the function `_deliver_post` (lines 178-199). | `_deliver_post` | mcp/src/agents_remember/serving/operator_inbox_posts.py:205-226 |
| Defines the function `post_operator_inbox_entry` (lines 202-288) — Create, persist, deliver, and describe one post through the shared real owner.. | `post_operator_inbox_entry` | mcp/src/agents_remember/serving/operator_inbox_posts.py:202-288 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
