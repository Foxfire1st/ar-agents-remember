# mcp/src/agents_remember/serving/operator_inbox_posts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/operator_inbox_posts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T06:48+02:00 |
| lastVerifiedCommitHash | `a84add4c9422b18a26f1748dedaed16194994ded` |
| lastVerifiedCommitDate | 2026-08-10T05:11:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Persist and optionally deliver one operator-inbox post.

## Code Commentary

### Logic

Inbox addressing now consumes sprint-qualified catalog ownership for named command seats. Posts
that target architect custody resolve inside the row's repository+sprint scope; missing or legacy
global identity does not authorize cross-sprint delivery. Existing exact-agent delivery remains
unchanged.

Module-level surface:

- `OperatorInboxPostContext` (class, lines 62-67) — Persistence and delivery collaborators for one operator-inbox post.
- `_redelivery_floor_seconds` (function, lines 70-73)
- `_delivery_catalog` (function, lines 76-83)
- `_signal_route` (function, lines 86-101)
- `_post_address` (function, lines 104-119)
- `_is_owner_addressed` (function, lines 128-157) — whether an address names an owner mailbox
  (`manager`/`orchestrator`/`architect` role, or a catalog seat/lifecycle bound to the derived
  owner's role); peer-seat addresses are preserved verbatim.
- `_post_catalog` (function, lines 122-130)
- `_dispatch_entry_fields` (function, lines 133-141)
- `_persist_post` (function, lines 145-160) — appends the entry, compacts, and starts
  dispatch expectations; it no longer writes `ack-by` expectation rows (N16 — ack-by retires
  with the consume demotion, and ordinary posts write no expectation row at all).
- `_deliver_post` (function, lines 178-199)
- `post_operator_inbox_entry` (function, lines 202-288) — Create, persist, deliver, and describe one post through the shared real owner.

**260713-TES-L4 (N14) post-time owner re-resolution.** `_post_address` now takes the catalog and
re-derives the CURRENT qualified owner for every owner-addressed post before persisting — not
just the legacy `turn-report`/`master-handover` kinds — so a worker whose manager was replaced
never addresses the corpse at post time (the same-leaf+role replacement gets the row directly).
`dispatch-brief` rows stay exact-pinned (never rebind; a replacement receives a fresh brief from
its owner). Cross-agent messages are never hijacked: a caller-addressed recipient that is not an
owner mailbox — or cannot be proven to be one — is kept verbatim via `_is_owner_addressed`.

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
| Defines the class `OperatorInboxPostContext` (lines 62-67) — Persistence and delivery collaborators for one operator-inbox post.. | `OperatorInboxPostContext` | mcp/src/agents_remember/serving/operator_inbox_posts.py:54-60 |
| Defines the function `_redelivery_floor_seconds` (lines 70-73). | `_redelivery_floor_seconds` | mcp/src/agents_remember/serving/operator_inbox_posts.py:63-68 |
| Defines the function `_delivery_catalog` (lines 76-83). | `_delivery_catalog` | mcp/src/agents_remember/serving/operator_inbox_posts.py:71-78 |
| Defines the function `_signal_route` (lines 86-101). | `_signal_route` | mcp/src/agents_remember/serving/operator_inbox_posts.py:81-96 |
| Defines the function `_post_address` (lines 104-119). | `_post_address` | mcp/src/agents_remember/serving/operator_inbox_posts.py:99-125 |
| Defines the function `_post_catalog` (lines 122-130). | `_post_catalog` | mcp/src/agents_remember/serving/operator_inbox_posts.py:158-166 |
| Defines the function `_dispatch_entry_fields` (lines 133-141). | `_dispatch_entry_fields` | mcp/src/agents_remember/serving/operator_inbox_posts.py:169-177 |
| Defines the function `_persist_post` (lines 144-175). | `_persist_post` | mcp/src/agents_remember/serving/operator_inbox_posts.py:180-189 |
| Defines the function `_deliver_post` (lines 178-199). | `_deliver_post` | mcp/src/agents_remember/serving/operator_inbox_posts.py:200-221 |
| Defines the function `post_operator_inbox_entry` (lines 202-288) — Create, persist, deliver, and describe one post through the shared real owner.. | `post_operator_inbox_entry` | mcp/src/agents_remember/serving/operator_inbox_posts.py:202-288 |

## Update History

- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded sprint-local architect custody for inbox post
  routing. Verification metadata remains pinned until closeout stamps the code commit.

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the N14 post-time owner
  re-resolution (`_post_address` generalized to every owner-addressed post with the
  `_is_owner_addressed` owner-mailbox gate; dispatch-brief exact-pinned; peer addresses
  preserved verbatim) and the ack-by retirement in `_persist_post` (no expectation rows written
  for ordinary posts; N16). Verification metadata pinned until closeout stamps the
  260713-TES-L4 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
