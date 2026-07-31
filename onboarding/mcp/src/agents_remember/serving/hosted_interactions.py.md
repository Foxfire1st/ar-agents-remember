# hosted_interactions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/hosted_interactions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T17:18:47+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Synchronizes adapter-owned pending questions and terminal completion evidence with durable gates
and durable inbox rows.

## Code Commentary
### Logic
Pending interactions create `agent-question` gates containing exact session/interaction identity,
prompt, choices, and raw detail. A decided gate responds through the same adapter interaction id;
disappearance expires only the matching open gate. For a Codex terminal result whose protocol
`requestId` is null, completion uses the protocol-owned vendor correlation field and the same
hosted session to select exactly one accepted inbox row, then projects completion onto that row.
The correlation must be present, text, matched, and unambiguous; otherwise the operation fails
loudly. Production consumes structured messages and fields, not the exact 2.1.207, 0.144.3, or
0.80.6 fixture/smoke values.
### Invariants And Boundaries
Completion never calls `consume`; `record_adapter_completion` writes `adapterDeliveryState` and
`adapterCompletedAt` on the same row while its explicit inbox `state` remains `pending` and
unconsumed. Explicit recipient consumption remains the sole inbox acknowledgement. Missing,
non-text, unmatched, or ambiguous correlation fails loudly and cannot degrade to a parser or
fallback. Adapter failures leave durable state truthful and retryable.

## Docs References
No relevant external/domain documentation was configured; gate, inbox, and interaction tests are authoritative.

## Repo-Internal References
- [operator_inbox_store.py](../controlplane/operator_inbox_store.py) persists delivery evidence.
- [GateResponder.tsx](agents-remember/dashboard/src/panels/GateResponder.tsx) renders interaction context.
- [harness_control_client.py](harness_control_client.py) sends interaction responses.

## Cross-Repo References
No meaningful cross-repo references.

## 260718-CHATS-L5I Current Delta

Hosted interactions now serialize structured answers for harness adapters and reopen a failed decision with `adapterDecisionFailure` evidence. A delivery fault is visible and answerable again; it is not silently swallowed or represented as a completed approval.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

Gate creation now uses the control-plane gate parameter objects: the `agent-question` gate is opened
with a positional kind plus `anchor=GateAnchor(lifecycle_id=…)` and
`request=GateRequest(packet=…, required_decision=…)` instead of flat keywords. The gate contents are
unchanged — the same exact session/interaction identity, prompt, choices, raw detail and question
list ride the `adapterInteraction` packet, and the required decision is still the interaction's own
choices, falling back to `["approve", "reject"]`.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `GateAnchor` / `GateRequest` call shape for the agent-question gate; gate contents unchanged.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: documented protocol-owned null-requestId/vendor-correlation
  completion projection, explicit pending/unconsumed inbox semantics, and loud correlation failures.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented durable interaction gates and completion-without-consumption.
