# mcp/src/agents_remember/models/structural/gates.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/structural/gates.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T14:29+02:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structural wire models](overview.md)

## Purpose

Holds structural delegated-gate request/response models and the isolated internal exact-correlation
gate response models. This is the behavior-preserving destination of the former flat
`models/gates.py` card, with the public/internal identity boundary made explicit.

## Code Commentary

### Logic

Structural requests name a target role/document relation and decision content. Internal response
models retain lifecycle/gate ids only for application-to-plane calls. Public summaries and responses
replace those ids with task-document and role identity.

### Conventions

The `Internal*` prefix is a boundary marker: those models must never be registered as public agent
MCP results.

### Invariants And Boundaries

- Agent-facing schemas never expose lifecycle or gate ids.
- Internal correlation stays available for the application service to complete the transaction.
- Strict response models reject accidental mixed public/internal payloads.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Structural requests are separated from internal exact-id responses. | `StructuralLifecycleGateRequest` | mcp/src/agents_remember/models/structural/gates.py:25-118 |
| Public list summaries expose structural identity. | `StructuralGateSummary` | mcp/src/agents_remember/models/structural/gates.py:119-164 |

## Cross-Repo References


## Update History

- 2026-08-11T14:29+02:00 — Re-read `StructuralLifecycleGateRequest` and widened its citation to
  include the dataclass declaration; verification metadata remains pending for governed closeout.
- 2026-08-11T06:47+02:00 — 260731-EFA-L19: relocated and rewrote the former flat gate-model onboarding around the public structural/internal correlation split.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the scoped gate-model citation claims; final exact frozen-snapshot check is clean.
- 2026-07-04T12:32+02:00 — 260703-L4: `GateDecideResponse` exposed delegated-decision attribution (`decidingRole`) and reviewer/evidence refs carried on the gate record. Verification metadata remained pinned until closeout.
- 2026-06-26T14:16+02:00 — Task 25: added `LifecycleGateResponse` for the unified public junction and classified create/wait/response-wait models as internal compatibility contracts.
- 2026-06-25T07:17+02:00 — Task 19: `GateWaitResponse` gained optional decision metadata and `GateResponseWaitResponse` modeled the combined gate/inbox bounded wait helper.
- 2026-06-18T01:05+02:00 — Created for task 6 slice 6a as the original flat gate response-model card.
