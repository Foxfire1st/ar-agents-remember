# mcp/src/agents_remember/models/structural/agent.py

## Governing Overview

[Structural wire models](overview.md)

## Purpose

Declare canonical structural dispatch models and the native receipt-tracked retirement request/response.

## Code Commentary

StructuralRole retains canonical roles and the earlier system-specialist spelling; the
response role validator delegates canonicalization. DispatchAgentRequest is a frozen
record of task_document_ref, role, brief and optional label. StructuralTargetResponse names
work/role/status/detail, not a runtime occupant, and declares optional deliveryState and
adapterDeliveryState; DispatchAgentResponse retains those fields and its operation label.
Parent/child messaging, rename DTOs and AgentMessageKind remain removed. RetireChildRequest and RetireChildResponse are restored for native retirement only: the request carries agent_id and explicit interrupt_turn, and the native owner verifies the original starter and unique recorded target before effects. This is not restoration of the former plane-hosting API. The old
six-consumer/three-producer inventory is history. Untouched internal gate/activation models
remain separate owners; retirement here does not erase their state or authority.

## Current model evidence

- Current source section contains excerpt `StructuralRole = Literal[`; DTO/control ownership is not execution acceptance. [3]

## Historical superseded account (non-operative)

Prior removed-tool/current-roster claims below are preserved provenance, not current
registration, runtime capability or execution evidence.



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

## Evidence

### Docs References


### Repo-Internal References

- The request family uses structural fields only. [1]
- The response family returns structural targets without runtime ids. [2]

### Cross-Repo References


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
