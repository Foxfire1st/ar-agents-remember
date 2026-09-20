# mcp/src/agents_remember/models/structural/agent.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/structural/agent.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:02+02:00 |
| lastVerifiedCommitHash |  `f05ba167cd6dfb56b48a775f3da5d45528c09c82`|
| lastVerifiedCommitDate |  2026-09-18T17:19:31+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l4-ar` uncommitted source; base `0dd04d6adbca3e8ba61849b605ece3137005829e` |
| governingOverview | `overview.md` |

## Governing Overview

[Structural wire models](overview.md)

## Purpose

Defines strict agent-facing DTOs for dispatch, parent/child messaging, retirement, and rename. The
wire contains stable work-domain identity and intentionally has no runtime addressing fields.

## Code Commentary

### Logic

Request dataclasses accept only task-document, role, content, label, and reason fields. Response
models share `StructuralTargetResponse`, exposing the resolved task document and role plus status.

### Conventions

Every operation has a distinct response model so the registry remains self-describing while the
structural target shape stays common.

### Invariants And Boundaries

- Public request dataclasses define only the listed structural fields; registration and wire tests
  guard the absence of plane-only address vocabulary.
- Session, lifecycle, terminal, inbox-row, and gate ids are forbidden on public schemas.
- Do not add legacy aliases for removed exact-id requests.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The request family uses structural fields only. | `DispatchAgentRequest` | mcp/src/agents_remember/models/structural/agent.py:39-69 |
| The response family returns structural targets without runtime ids. | `StructuralTargetResponse` | mcp/src/agents_remember/models/structural/agent.py:71-117 |

## Cross-Repo References


## 260918-TSIP-L4 — The Delivery Projection Declared On The Shared Base (`T4`)

`StructuralTargetResponse` now declares `deliveryState: InboxDeliveryState | None = None`
and `adapterDeliveryState: AdapterDeliveryState | None = None` (**`:86-87`**), which moved every
line at or below the old `:78` down by `+10` (`RetireChildResponse` `98 → 108`,
`RenameChildResponse` `102 → 112`, `RenameSelfResponse` `106 → 116`; file **107 → 117 lines**).

The producer is the shared `structural_payload` (`application/structural/outcomes.py:36-39`): it
adds both keys whenever the outcome carries a delivery state. **Declaring them on the base repairs
the class rather than the three instances** — all six consumers inherit them, and
`dispatch_agent`, `message_parent` and `message_child` are the three call sites that populate them
today while `retire_child`, `rename_child` and `rename_self` pass no delivery state and leave both
`None` (excluded by `exclude_none`). A strict consumer that omits a key its own producer can emit
is exactly the `D53` shape, and there is no fourth consumer to fall through.

Pinned by `mcp/tests/test_tool_response_conformance.py::test_the_structural_delivery_projection_is_declared_on_every_consumer`,
which fails against the base model with `Items in the second set but not the first: {'deliveryState',
'adapterDeliveryState'}`.

## Update History
- 2026-09-18T17:02+02:00 — 260918-TSIP-L4 curator (uncommitted change set on `ar/260918-tsip-l4-ar`, base `0dd04d6a`): the delivery projection declared on the shared base (`:86-87`, `T4`) — the class repaired, not the three instances. Verification metadata stays at the recorded verification because the candidate is uncommitted and the governed closeout owns the real code commit; `lastUpdated` advances with this body edit.

- 2026-08-11T14:29+02:00 — Re-read `DispatchAgentRequest` and widened its citation to include
  the dataclass declaration; verification metadata remains pending for governed closeout.
- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for the public structural agent DTO family.
