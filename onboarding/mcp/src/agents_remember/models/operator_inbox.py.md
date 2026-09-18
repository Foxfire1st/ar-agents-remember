# mcp/src/agents_remember/models/operator_inbox.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/models/operator_inbox.py`      |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated | 2026-09-18T17:02+02:00 |
| lastVerifiedCommitHash | `f05ba167cd6dfb56b48a775f3da5d45528c09c82` |
| lastVerifiedCommitDate | 2026-09-18T17:19:31+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l4-ar` uncommitted source; base `0dd04d6adbca3e8ba61849b605ece3137005829e` |
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
| The response models cover post, poll, and consume payloads and reuse the inbox state literal. | "class OperatorInboxPostResponse(ToolResponse):"; "class OperatorInboxPollResponse(ToolResponse):"; "class OperatorInboxConsumeResponse(ToolResponse):"; "OperatorInboxState = Literal[" | mcp/src/agents_remember/models/operator_inbox.py:12-12; mcp/src/agents_remember/models/operator_inbox.py:62-62; mcp/src/agents_remember/models/operator_inbox.py:119-119; mcp/src/agents_remember/models/operator_inbox.py:129-129 |
| The registry maps operator inbox post, poll, consume, and supersede tools to their response models. | "\"operator_inbox_post\": OperatorInboxPostResponse," | mcp/src/agents_remember/models/tools/tool_registry.py:231-231 |

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

## 260918-TSIP-L4 — The Refusal Half Of `operator_inbox_post` (`T15`)

`OperatorInboxPostResponse` now carries a typed refusal as well as the queued projection
(file **109 → 146 lines**; the class **`:62-116`**, with `OperatorInboxPollResponse` following at
`:119`).

- **`OperatorInboxPostStatus = Literal["queued", "sprint-owner-required"]`** is new at
  **`:59`**, and `status: OperatorInboxPostStatus` is declared at **`:75`**. It names which of
  the two outcomes the response is: `serving/operator_inbox_posts.py:304-310` returns
  `{"ok": False, "operation": "operator_inbox_post", "status": "sprint-owner-required"}` — a typed
  outcome of this operation, which previously surfaced as a bare tool error with no envelope.
- **`detail: str | None`** (**`:101`**, `max_length=8192`) carries the refusal's prose, as on
  `SessionRetireResponse`.
- **The four queued-projection fields are conditional on `ok`.** `entryId`, `state`,
  `messageKind` and `deliveryState` are now `| None = None`, and a
  `@model_validator(mode="after")` (**`:103-116`**) refuses a success that omits any of them:
  *"a queued operator post must report entryId, state, messageKind, deliveryState"*. The refusal
  fires **before the first write**, so it has no entry id and must not invent one; making the four
  optionally-absent without the validator would have hollowed out the success contract instead.

**The JSON schema cannot carry the rule** — `required` is only ever unconditional — so the model
docstring states it and the validator enforces it; a caller reading the schema alone must read the
docstring with it. Pinned by
`mcp/tests/test_tool_response_conformance.py::test_a_queued_operator_inbox_post_still_must_report_its_entry`
and `::test_operator_inbox_post_sprint_owner_refusal_is_a_typed_payload`.

**Correction to the register's carried figure:** the `sprint-owner-required` branch omits
**four** required fields (`entryId`, `state`, `messageKind`, `deliveryState`), not two; Addendum C
said two and the row that first recorded the defect said four. Executed against the base model the
run reports `4 validation errors … Field required` plus `1 … status Extra inputs are not
permitted`.

## Update History
- 2026-09-18T17:02+02:00 — 260918-TSIP-L4 curator (uncommitted change set on `ar/260918-tsip-l4-ar`, base `0dd04d6a`): the typed refusal half of `operator_inbox_post` (`:59-60`, `:75`, `:101`, `:103-119`; `T15`), and the register's two-field figure corrected to four. Verification metadata stays at the recorded verification because the candidate is uncommitted and the governed closeout owns the real code commit; `lastUpdated` advances with this body edit.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "\"operator_inbox_post\": OperatorInboxPostResponse," repointed to mcp/src/agents_remember/models/tools/tool_registry.py:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "\"operator_inbox_post\": OperatorInboxPostResponse," repointed to mcp/src/agents_remember/models/tools/tool_registry.py:224-224. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:06:15+00:00: Generated citation repair: "\"operator_inbox_post\": OperatorInboxPostResponse," repointed to mcp/src/agents_remember/models/tools/tool_registry.py:222-222. No content impact: mechanical anchor-range projection bound to citation source snapshot 1740540b8733028dd833a3538d739271e8925ea5f51911a0f8dcd8c49e7e1c13; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T23:44:56+00:00: Generated citation repair: "\"operator_inbox_post\": OperatorInboxPostResponse," repointed to mcp/src/agents_remember/models/tools/tool_registry.py:220-220. No content impact: mechanical anchor-range projection bound to citation source snapshot fc36bf81fd36002f552f72a34a44e9713fa47fc86ced6632de3215e5011793d3; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "\"operator_inbox_post\": OperatorInboxPostResponse," repointed to mcp/src/agents_remember/models/tools/tool_registry.py:218-218. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 1 declined citation claim against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Selected the complete actual operator-inbox mapping rather than its import block and a gate-list line. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.

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
