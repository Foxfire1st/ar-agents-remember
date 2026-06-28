# mcp/src/agents_remember/controlplane/interaction_retention.py

| Field                  | Value                                                                  |
| ---------------------- | ---------------------------------------------------------------------- |
| repository             | agents-remember                                                        |
| path                   | `mcp/src/agents_remember/controlplane/interaction_retention.py`        |
| doc_type               | `file-level-onboarding`                                                |
| lastUpdated            | 2026-06-25T13:10+02:00                                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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

## Invariants And Boundaries

- This module owns policy only: stores perform the filesystem rewrite, tools decide when to call store
  deletion, and projection readers supply the clock for passive TTL cleanup.
- Interaction records are throwaway; durable task docs, contracts, ledgers, and closeout results remain
  outside this policy.

## Update History

- 2026-06-25T13:10+02:00 — Created for task 23/24 gate/inbox retention, wait defaults, and pickup TTLs.
