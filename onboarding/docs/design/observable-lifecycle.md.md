# docs/design/observable-lifecycle.md

## Current A10 retained-source account

R113 marks the entire observable-lifecycle design as historical: the session lifecycle, raised developer gates and product-owned agent hosting are removed. The earlier R112 session-driven transition account is superseded as present intent. The current tool surface is separately owned by docs/reference/mcp-tools.md; this retained design source grants no restored transition or execution acceptance.

- R113 marks the entire observable-lifecycle design as historical: the session lifecycle, raised developer gates and product-owned agent hosting are removed. The earlier R112 session-driven transition account is superseded as present intent. The current tool surface is separately owned by docs/reference/mcp-tools.md; this retained design source grants no restored transition or execution acceptance. [3]



## Current operative account — MIK-R112

The amended design retains states, phases, gates, event correlation and persistence tiers, but removes the model-facing lifecycle signal surface. Transitions are session-driven/guarded or system-owned; a raised gate records the ask, ending a turn is not a lifecycle_gate call and there is no restored lifecycle_resume/end/switch tool prescription. Design remains pre-implementation authority, not proof every design transition is shipped. Historical retention and inbox recovery accounts retain their original dated custody.

The original prose, exact parameters, references and dated producer accounts below remain intact as history, not present-tense authority for superseded behavior. Current evidence is the source path `docs/design/observable-lifecycle.md` and the source-specific before/after extents preserved in the residual-hunk account. No code edit, proof rerun or new execution acceptance is claimed.

## Historical original card — preserved, not the current operative account

<details>
<summary>Original source account and historical evidence</summary>

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


</details>
