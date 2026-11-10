# mcp/src/agents_remember/models/structural/agent.py

## Governing Overview

[Structural wire models](overview.md)

## Purpose

Declare the native receipt-tracked seat-retirement request/response and canonical role vocabulary.
Dispatch, shared structural-delivery and parent/child messaging DTOs are absent.

## Code Commentary

`StructuralRole` names the task-seat roles (architect, orchestrator, investigator, manager, worker,
reviewer, curator) and the earlier system-specialist spelling.
The frozen `RetireChildRequest` carries task_document_ref, role, reason, optional agent_id and
interrupt_turn; the native owner, not this dataclass, enforces starter/receipt identity and
refuses an empty target or an unadmitted interruption.

`RetireChildResponse` declares retire_child, status, optional taskDocumentRef, role and detail;
its role validator calls canonical_role. It inherits the retained ToolResponse envelope and
does not expose a runtime-occupant response field. Internal task gate/activation owners remain
separate; this DTO is not a plane-hosting API.

## Current model evidence

The complete current source has only the role Literal, RetireChildRequest and
RetireChildResponse.

## Evidence

- The retained role Literal and native retirement request/response have no dispatch/shared-delivery DTO. [1]

- The task-seat role literal holds seven canonical roles plus the system-specialist spelling. [2]
