# docs/design/observable-lifecycle.md

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| repository             | agents-remember                         |
| path                   | `docs/design/observable-lifecycle.md`   |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-06-26T14:16+02:00                      |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                           |

## Governing Overview

[docs/design overview](overview.md)

## Purpose

Design authority for the observable lifecycle and dashboard state model.

## Code Commentary

The document describes the lifecycle substrate, projection read side, dashboard
state surfaces, and persistence tiers that guide implementation. Task 25 updates
the public gate design around `lifecycle_gate`: one agent-facing junction opens
the durable gate, blocks the lifecycle with the ask, and initializes wait/response
state while keeping durable gate kind (`plan-approval`, `worktree-intent`,
`closeout-approval`, etc.) separate from answer-shape kind (`question`,
`decision`, `conflict`). Task 23/24 retention still applies: durable work records
stay, while gate/operator-inbox interaction records are throwaway data with
response/dismiss/clear/consume deletion paths plus a 24-hour passive TTL.

## Invariants And Boundaries

- This is a design document, not shipped runtime code, but it is the durable source
  for dashboard lifecycle semantics.
- Interaction retention applies to prompt/response handshakes only; tasks,
  contracts, closeout commits, and ledger mappings remain durable lifecycle records.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Retention policy implementation follows this design split. | [controlplane/interaction_retention.py](../../mcp/src/agents_remember/controlplane/interaction_retention.py) |
| Projection readers apply interaction TTL and pickup feedback. | [observer/snapshots.py](../../mcp/src/agents_remember/observer/snapshots.py) |
| MCP `lifecycle_gate` exposes the unified public gate junction. | [mcp/server.py](../../mcp/src/agents_remember/mcp/server.py) |

## Update History

- 2026-06-26T14:16+02:00 — Task 25: design now names `lifecycle_gate` as the public lifecycle-gate junction and removes the split create/block/wait choreography from the documented public path.
- 2026-06-25T13:20+02:00 — Created for task 23/24 after the design doc gained interaction-retention tiers and the five-minute `gate_response_wait` default.
