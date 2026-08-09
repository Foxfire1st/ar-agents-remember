# mcp/src/agents_remember/models/operator_inbox.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/models/operator_inbox.py`      |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-08-09T06:48+02:00 |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`|
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[overview.md](overview.md)

## Purpose

Strict public response models for the `operator_inbox_*` MCP tools, including
agent-to-agent metadata and hosted-delivery status.

## Code Commentary

### Logic

`OperatorInboxPostResponse` returns the queued entry id, state, mailbox keys,
sender/recipient role metadata, message kind, optional artifact path, and
optional hosted-delivery fields. Since 260707-HFX2-L1 (R4) it also carries the routed-owner
address — `ownerRole`/`ownerAgentId`/`ownerLifecycleId`, derived by
`controlplane/signal_routing.py::derive_signal_owner` from catalog spawn provenance and stamped
onto the entry at post time — distinct from the caller-supplied `recipientRole`; all three are
`None` when routing derived nothing. `OperatorInboxPollResponse` returns the mailbox
key, optional recipient role, pending entry count, and serialized entry
dictionaries. `OperatorInboxConsumeResponse`
returns the entry id, final state, whether this call consumed it now, and the
consume timestamp when present. Since 260713-TES-L4 the consume response state is the
unchanged row state (attribution-only, N16), and a fourth response model,
`OperatorInboxSupersedeResponse`, returns the terminal marker after an explicit supersession:
`entryId`, `state`, `supersededNow`, `terminalAt`, `terminalReason`, `supersededBy` (R11).

### Conventions

All four classes inherit `ToolResponse`, so they are strict AR-owned contracts
with the common `ok`, `operation`, and token metadata envelope. State typing
reuses `OperatorInboxState` from the persisted record module.

### Invariants And Boundaries

- These models describe public MCP responses, not persisted inbox records.
- Nullable fields use `= None` so `_tool_payload(... exclude_none=True)` can omit
  absent mailbox/gate/delivery/consumed timestamp fields.
- Register every new public inbox tool here and in
  `TOOL_RESPONSE_MODELS` (`models/tool_registry.py`).

### Todos

None.

## Docs References

No relevant external documentation found after checking the in-repo design docs
listed as Domain Documentation.

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The response models cover post, poll, and consume payloads. | `OperatorInboxPostResponse`; `OperatorInboxPollResponse`; `OperatorInboxConsumeResponse` | mcp/src/agents_remember/models/operator_inbox.py:17-42; mcp/src/agents_remember/models/operator_inbox.py:45-52; mcp/src/agents_remember/models/operator_inbox.py:55-61 |
| The response models reuse the inbox state literal imported from the persisted record module. | "OperatorInboxState," | mcp/src/agents_remember/models/operator_inbox.py:12-12 |
| The registry imports the inbox response models. | "from agents_remember.models.operator_inbox import (" | mcp/src/agents_remember/models/tool_registry.py:59-65 |
| The registry maps the `operator_inbox_*` tools (post/poll/consume/supersede since 260713-TES-L4) to these response models. | "operator_inbox_post": OperatorInboxPostResponse | mcp/src/agents_remember/models/tool_registry.py:175-180 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded `OperatorInboxSupersedeResponse`
  (R11 explicit supersession terminal marker) and the attribution-only consume response state
  (N16 — state unchanged). Verification metadata pinned until closeout stamps the
  260713-TES-L4 commit.
- 2026-08-04T18:17+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 2 citation rows with exact anchors (the three response models + `OperatorInboxState`, and the registry import/mapping) and ledger-verified ranges. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: `OperatorInboxPostResponse` gained `ownerRole`/`ownerAgentId`/`ownerLifecycleId` (R4 routed-owner address) alongside the existing `recipientRole`. Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-07-04T12:31+02:00 - L3: extended inbox response models with role/message
  metadata and hosted-delivery fields. Verification metadata pinned until
  closeout stamps the L3 commit.
- 2026-06-23T13:44+02:00 — Created for task 10 backend inbox: strict response models for post, poll, and consume. Verification metadata pinned until closeout stamps the task-10 code commit.
