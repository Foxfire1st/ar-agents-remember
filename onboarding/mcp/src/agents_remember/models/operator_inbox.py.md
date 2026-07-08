# mcp/src/agents_remember/models/operator_inbox.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/models/operator_inbox.py`      |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-08T14:35+02:00 |
| lastVerifiedCommitHash |                                                         `45708bbddf1ddb8a2045faa9fad88fe72603b674`|
| lastVerifiedCommitDate |                                                         2026-07-08T05:51:44+02:00|
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
consume timestamp when present.

### Conventions

All three classes inherit `ToolResponse`, so they are strict AR-owned contracts
with the common `ok`, `operation`, and token metadata envelope. State typing
reuses `OperatorInboxState` from the persisted record module.

### Invariants And Boundaries

- These models describe public MCP responses, not persisted inbox records.
- Nullable fields use `= None` so `_tool_payload(... exclude_none=True)` can omit
  absent mailbox/gate/delivery/consumed timestamp fields.
- Register every new public inbox tool here and in
  `PUBLIC_TOOL_RESPONSE_MODELS`.

### Todos

None.

## Docs References

No relevant external documentation found after checking the in-repo design docs
listed as Domain Documentation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The response models cover post, poll, and consume payloads and reuse the inbox state literal. | L7-L36 | [operator_inbox.py](agents-remember/mcp/src/agents_remember/models/operator_inbox.py) |
| The registry maps the three `operator_inbox_*` tools to these response models. | L56-L60; L139-L141 | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: `OperatorInboxPostResponse` gained `ownerRole`/`ownerAgentId`/`ownerLifecycleId` (R4 routed-owner address) alongside the existing `recipientRole`. Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-07-04T12:31+02:00 - L3: extended inbox response models with role/message
  metadata and hosted-delivery fields. Verification metadata pinned until
  closeout stamps the L3 commit.
- 2026-06-23T13:44+02:00 — Created for task 10 backend inbox: strict response models for post, poll, and consume. Verification metadata pinned until closeout stamps the task-10 code commit.
