# mcp/src/agents_remember/models/operator_inbox.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/models/operator_inbox.py`      |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
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

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The response models cover post, poll, and consume payloads and reuse the inbox state literal. | "class OperatorInboxPostResponse(ToolResponse):"; "class OperatorInboxPollResponse(ToolResponse):"; "class OperatorInboxConsumeResponse(ToolResponse):"; "OperatorInboxState = Literal[" | mcp/src/agents_remember/models/operator_inbox.py:10-10; mcp/src/agents_remember/models/operator_inbox.py:54-54; mcp/src/agents_remember/models/operator_inbox.py:82-82; mcp/src/agents_remember/models/operator_inbox.py:92-92 |
| The registry maps the three `operator_inbox_*` tools to these response models. | "from agents_remember.models.operator_inbox import ("; "\"operator_inbox_post\": OperatorInboxPostResponse," | mcp/src/agents_remember/models/tools/tool_registry.py:53-53; mcp/src/agents_remember/models/tools/tool_registry.py:216-216 |

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

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 curator: re-anchored citation range(s) to current source after the L16 line movement (cited files changed, card source unchanged); verification metadata unchanged.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:17+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 2 citation rows with exact anchors (the three response models + `OperatorInboxState`, and the registry import/mapping) and ledger-verified ranges. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: `OperatorInboxPostResponse` gained `ownerRole`/`ownerAgentId`/`ownerLifecycleId` (R4 routed-owner address) alongside the existing `recipientRole`. Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-07-04T12:31+02:00 - L3: extended inbox response models with role/message
  metadata and hosted-delivery fields. Verification metadata pinned until
  closeout stamps the L3 commit.
- 2026-06-23T13:44+02:00 — Created for task 10 backend inbox: strict response models for post, poll, and consume. Verification metadata pinned until closeout stamps the task-10 code commit.
