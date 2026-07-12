# mcp/src/agents_remember/controlplane/interaction_retention.py

| Field                  | Value                                                                  |
| ---------------------- | ---------------------------------------------------------------------- |
| repository             | agents-remember                                                        |
| path                   | `mcp/src/agents_remember/controlplane/interaction_retention.py`        |
| doc_type               | `file-level-onboarding`                                                |
| lastUpdated            | 2026-07-10T02:39+02:00                                                 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`|
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview      | `overview.md`                                                          |

## Governing Overview

[controlplane overview](overview.md)

## Purpose

Central retention policy for short-lived gate and operator-inbox interaction data.

## Code Commentary

### 260712-TRH-L5 Confirmed-Gone Secondary Retention

`inbox_keep_ids` remains the final retention boundary after the supervisor's same-lock
confirmed-gone reconciliation. The 48-hour pending TTL and 500-row folded-current cap are
unchanged; `current=` lets the transaction reuse its single authoritative fold rather than
reading the append-only log again. Ladder-resolved snapshots, including the stable
`subject-session-confirmed-gone` reason, are still removed immediately by this policy.

### 260707-HFX2-L20 Monotonic Inbox Compaction

`inbox_keep_ids` uses the same monotonic fold as the live inbox store. Once a consumed or
ladder-resolved snapshot exists, a physically later pending snapshot produced by an in-flight
delivery cannot extend that row's pending retention or return it to the redelivery pool.

Defines the shared timing constants: `gate_response_wait` defaults to a 300-second wait and 5-second
poll cadence, ordinary consumed interaction records have a 24-hour TTL, pending inbox rows have a
separate hard 48-hour TTL, and task-row pickup feedback switches
from `waiting-for-agent` to `check-chat` after 300 seconds. `gate_keep_ids` and `inbox_keep_ids` take
validated records plus a projection clock and return the ids still worth keeping in compacted logs.
`delete_after_wait` distinguishes non-enforcement gates, which can be deleted after the wait tool
returns their decision, from worktree/closeout/integration/cleanup gates that a mutating tool still has
to consume/apply.

**HFX3 health-first supersession (developer ruling 2026-07-09)**: no inbox row outranks system
health. `_keep_inbox_entry` keeps a pending/unacked row only for
`INBOX_PENDING_TTL_SECONDS` (48 hours), drops `ladder-resolved` rows immediately, and applies the
ordinary 24-hour audit window to consumed rows. `inbox_keep_ids` then enforces
`INBOX_MAX_CURRENT_ROWS = 500`, keeping the newest rows when a producer exceeds the cap. If an
expired condition still holds, the supervisor may recreate one fresh coalesced row; the durable
record is the task/report/gate artifact on disk, never the notification row. This supersedes the
HFX2-L1 immortal-pending rule that contributed to the 2026-07-09 escalation storm.

## Invariants And Boundaries

- This module owns policy only: stores perform the filesystem rewrite, tools decide when to call store
  deletion, and projection readers supply the clock for passive TTL cleanup.
- Interaction records are throwaway; durable task docs, contracts, ledgers, and closeout results remain
  outside this policy.
- Pending inbox rows are disposable notification state: they expire after 48 hours and the folded
  inbox is hard-capped at 500 current ids, newest-first.
- A `ladder-resolved` inbox row is neither pending nor acked; compaction drops it immediately.

## Update History

- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: documented the unchanged 48-hour pending TTL
  and 500-row cap as fallback retention and the pre-folded-current transaction seam used after
  confirmed-gone resolution. Verification metadata remains pinned until closeout stamps the
  candidate commit.

- 2026-07-10T22:18+02:00 — 260707-HFX2-L20: made inbox compaction use the shared terminal-dominant
  fold so stale in-flight delivery snapshots cannot resurrect pending retention.

- 2026-07-10T02:39+02:00 — HFX3 retro curation: replaced the superseded immortal-pending account
  with the reviewed health-first contract: 48-hour pending TTL, 500-row hard cap, newest-first
  eviction, immediate ladder-resolved reclamation, and artifact-not-row durability. Added the
  governing-overview backlink. Verification metadata remains pinned until closeout stamps the
  eventual two-parent code commit.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8: `_keep_inbox_entry` now drops `ladder-resolved` terminal
  rows during compaction while continuing to protect pending/unacked rows. Verification metadata
  pinned until closeout stamps the HFX2-L8 commit.
- 2026-07-08T14:10+02:00 — 260707-HFX2-L1: `_keep_inbox_entry` now keeps every `pending` row
  regardless of age (R1: compaction never removes an unacked row); the 24h TTL applies only to
  `consumed` rows. Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-06-25T13:10+02:00 — Created for task 23/24 gate/inbox retention, wait defaults, and pickup TTLs.
