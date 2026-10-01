# docs/design/observable-lifecycle.md

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
response/dismiss/clear/consume deletion paths plus a 24-hour passive TTL. HFX2-L8
adds the non-destructive operator-inbox storm recovery runbook: save live work,
quarantine the inbox jsonl to `.bak` rather than deleting it, park/terminate only
provably dead terminal rows, restart cleanly, then verify heartbeat/backlog
metrics and compact normally.

## Invariants And Boundaries

- This is a design document, not shipped runtime code, but it is the durable source
  for dashboard lifecycle semantics.
- Interaction retention applies to prompt/response handshakes only; tasks,
  contracts, closeout commits, and ledger mappings remain durable lifecycle records.
- Recovery guidance never deletes transcripts or unsaved live-agent state; inbox storm handling is
  quarantine plus audited terminal-row resolution.

## Evidence

### Repo-Internal References

- Retention policy implementation follows this design split. [1]
- Projection readers apply interaction TTL and pickup feedback. [2]
- MCP `lifecycle_gate` exposes the unified public gate junction. [3]
