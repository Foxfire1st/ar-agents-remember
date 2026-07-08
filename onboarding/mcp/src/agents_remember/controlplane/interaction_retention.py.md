# mcp/src/agents_remember/controlplane/interaction_retention.py

| Field                  | Value                                                                  |
| ---------------------- | ---------------------------------------------------------------------- |
| repository             | agents-remember                                                        |
| path                   | `mcp/src/agents_remember/controlplane/interaction_retention.py`        |
| doc_type               | `file-level-onboarding`                                                |
| lastUpdated            | 2026-07-08T14:10+02:00                                                 |
| lastVerifiedCommitHash | `45708bbddf1ddb8a2045faa9fad88fe72603b674`|
| lastVerifiedCommitDate | 2026-07-08T05:51:44+02:00|
| governingOverview      | `overview.md`                                                          |

## Purpose

Central retention policy for short-lived gate and operator-inbox interaction data.

## Code Commentary

Defines the shared timing constants: `gate_response_wait` defaults to a 300-second wait and 5-second
poll cadence, pending interaction records have a 24-hour TTL, and task-row pickup feedback switches
from `waiting-for-agent` to `check-chat` after 300 seconds. `gate_keep_ids` and `inbox_keep_ids` take
validated records plus a projection clock and return the ids still worth keeping in compacted logs.
`delete_after_wait` distinguishes non-enforcement gates, which can be deleted after the wait tool
returns their decision, from worktree/closeout/integration/cleanup gates that a mutating tool still has
to consume/apply.

**260707-HFX2-L1 (R1 ack semantics)**: `_keep_inbox_entry` no longer ages out a `pending` row at
all — a pending/unacked row is now kept by compaction REGARDLESS OF AGE, since consume=ack is the
only terminal delivery outcome and an unacked row must outlive any cleanup until it is acked or
ladder-resolved. The 24h TTL now applies only to `consumed` rows (kept as an audit grace window;
the ordinary consume path already deletes its row explicitly and rarely reaches this TTL branch at
all). This is a behavior change from the prior "pending ages out after 24h" shape — exercised
directly against `operator_inbox_post_payload`'s post-time compaction call in
`test_operator_inbox.py::test_compaction_never_removes_a_pending_unacked_row_regardless_of_age`.

## Invariants And Boundaries

- This module owns policy only: stores perform the filesystem rewrite, tools decide when to call store
  deletion, and projection readers supply the clock for passive TTL cleanup.
- Interaction records are throwaway; durable task docs, contracts, ledgers, and closeout results remain
  outside this policy.
- A `pending` inbox row is NEVER pruned by age (260707-HFX2-L1, R1) — only `consumed` rows are
  TTL-bounded.

## Update History

- 2026-07-08T14:10+02:00 — 260707-HFX2-L1: `_keep_inbox_entry` now keeps every `pending` row
  regardless of age (R1: compaction never removes an unacked row); the 24h TTL applies only to
  `consumed` rows. Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-06-25T13:10+02:00 — Created for task 23/24 gate/inbox retention, wait defaults, and pickup TTLs.
