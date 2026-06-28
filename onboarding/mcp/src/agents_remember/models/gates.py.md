# mcp/src/agents_remember/models/gates.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/models/gates.py`   |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-06-26T14:16+02:00                      |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`  |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                               |

## Purpose

Response models for lifecycle gate control-plane payloads — AR-owned strict
`ToolResponse`s, not the persisted `GateRecord`.

## Code Commentary

`LifecycleGateResponse` is the public unified junction response: it carries separate
`gate`, `lifecycle`, and `wait` objects plus the optional structured `ask`.
`GateCreateResponse`, `GateWaitResponse`, and `GateResponseWaitResponse` remain
internal compatibility response models for lower-level payload builders.
`GateDecideResponse` (gateId / state / decidedBy / decidedVia) and
`GateListResponse` (lifecycleId / gates) remain public gate response models. All subclass `ToolResponse` (strict,
`extra="forbid"`). `GateKind` / `GateState` reuse the record's Literals so the response contract is as
drift-proof as the record.

## Invariants And Boundaries

- STRICT models (AR-owned shape): `extra="forbid"`. Registered in
  `tool_registry.TOOL_RESPONSE_MODELS` and exercised by the conformance suite,
  which requires a representative payload per modeled builder.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The Literals reused here. | [controlplane/records.py](agents-remember/mcp/src/agents_remember/controlplane/records.py) |
| The strict response base. | [models/base.py](agents-remember/mcp/src/agents_remember/models/base.py) |
| The registry that maps the gate tools to these models. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |

## Update History

- 2026-06-26T14:16+02:00 — Task 25: added `LifecycleGateResponse` for the unified public junction and classified create/wait/response-wait models as internal compatibility contracts.
- 2026-06-25T07:17+02:00 — Task 19: `GateWaitResponse` now carries optional decision metadata and `GateResponseWaitResponse` models the combined gate/inbox bounded wait helper. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-18T01:05+02:00 — Created for task 6 slice 6a: the four `gate_*` response models. Verification metadata pinned until closeout stamps the 6a code commit.
