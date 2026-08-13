# docs/design/observable-lifecycle.md

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| repository             | agents-remember                         |
| path                   | `docs/design/observable-lifecycle.md`   |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-07-08T23:59+02:00                      |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`|
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Retention policy implementation follows this design split. | `gate_keep_ids` | mcp/src/agents_remember/controlplane/interaction_retention.py:126-138 |
| Projection readers apply interaction TTL and pickup feedback. | "def read_agent_pickups(" | mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:142-142 |
| MCP `lifecycle_gate` exposes the unified public gate junction. | `lifecycle_gate_tool` | mcp/src/agents_remember/application/gate_tools.py:384-454 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 3 citation entries (6 findings); no Tier-3 findings.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm, R6): added the documented
  non-destructive operator-inbox storm recovery runbook: save live work first, quarantine
  `operator-inbox.jsonl` to `.bak`, resolve only provably dead terminal rows, restart cleanly, verify
  heartbeat/backlog metrics, and compact without deleting transcripts. Verification metadata pinned
  until closeout stamps the 260707-HFX2-L8 commit.
- 2026-06-26T14:16+02:00 — Task 25: design now names `lifecycle_gate` as the public lifecycle-gate junction and removes the split create/block/wait choreography from the documented public path.
- 2026-06-25T13:20+02:00 — Created for task 23/24 after the design doc gained interaction-retention tiers and the five-minute `gate_response_wait` default.
