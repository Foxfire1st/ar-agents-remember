# mcp/src/agents_remember/models/gates.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/models/gates.py`   |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-07-04T12:32+02:00                      |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`  |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                               |

## Purpose

Response models for lifecycle gate control-plane payloads — AR-owned strict
`ToolResponse`s, not the persisted `GateRecord`.

## Code Commentary

`LifecycleGateResponse` is the public unified junction response: it carries separate
`gate`, `lifecycle`, and `wait` objects plus the optional structured `ask`.
`GateCreateResponse`, `GateWaitResponse`, and `GateResponseWaitResponse` remain
internal compatibility response models for lower-level payload builders.
`GateDecideResponse` (gateId / state / decidedBy / decidedVia, plus L4
`decidingRole` and `evidenceRefs`) and
`GateListResponse` (lifecycleId / gates) remain public gate response models. All subclass `ToolResponse` (strict,
`extra="forbid"`). `GateKind` / `GateState` reuse the record's Literals so the response contract is as
drift-proof as the record.

## Invariants And Boundaries

- STRICT models (AR-owned shape): `extra="forbid"`. Registered in
  `tool_registry.TOOL_RESPONSE_MODELS` and exercised by the conformance suite,
  which requires a representative payload per modeled builder.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The Literals reused here (`GateKind` kernel-owned since L9). | "GateKind = Literal["; `GateState` | mcp/src/agents_remember/kernel/primitives/gate_vocab.py:12-12; mcp/src/agents_remember/kernel/primitives/gate_vocab.py:32-38 |
| The strict response base. | `ToolResponse` | mcp/src/agents_remember/models/base.py:63-66 |
| The registry that maps the gate tools to these models. | `TOOL_RESPONSE_MODELS`; `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:116-179; mcp/src/agents_remember/models/tool_registry.py:181-185 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the scoped gate-model citation claims; final exact frozen-snapshot check is clean.
- 2026-07-04T12:32+02:00 — 260703-L4: `GateDecideResponse` now exposes
  delegated-decision attribution (`decidingRole`) and reviewer/evidence refs
  carried on the gate record. Verification metadata pinned until closeout stamps
  the L4 commit.
- 2026-06-26T14:16+02:00 — Task 25: added `LifecycleGateResponse` for the unified public junction and classified create/wait/response-wait models as internal compatibility contracts.
- 2026-06-25T07:17+02:00 — Task 19: `GateWaitResponse` now carries optional decision metadata and `GateResponseWaitResponse` models the combined gate/inbox bounded wait helper. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-18T01:05+02:00 — Created for task 6 slice 6a: the four `gate_*` response models. Verification metadata pinned until closeout stamps the 6a code commit.
