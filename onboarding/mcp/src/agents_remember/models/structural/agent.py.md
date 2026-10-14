# mcp/src/agents_remember/models/structural/agent.py

## Governing Overview

[Structural wire models](overview.md)

## Purpose

Declare the native receipt-tracked seat-retirement request/response and canonical role vocabulary.
Dispatch, shared structural-delivery and parent/child messaging DTOs are absent.

## Code Commentary

`StructuralRole` includes canonical role names and the earlier system-specialist spelling.
The frozen `RetireChildRequest` carries task_document_ref, role, reason, optional agent_id and
interrupt_turn; the native owner, not this dataclass, enforces starter/receipt identity and
refuses an empty target or an unadmitted interruption.

`RetireChildResponse` declares retire_child, status, optional taskDocumentRef, role and detail;
its role validator calls canonical_role. It inherits the retained ToolResponse envelope and
does not expose a runtime-occupant response field. Internal task gate/activation owners remain
separate; this DTO does not revive the old plane-hosting API.

## Current model evidence

The complete current source has only the role Literal, RetireChildRequest and
RetireChildResponse; historical shared-delivery claims below are non-operative.

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

- The retained role Literal and native retirement request/response have no dispatch/shared-delivery DTO. [1]

## Historical 260918-TSIP-L4 delivery projection (non-operative)

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
