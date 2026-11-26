# mcp/src/agents_remember/models/structural/agent.py

## Governing Overview

[Structural wire models](overview.md)

## Purpose

Declare the native receipt-tracked seat-retirement request/response DTOs and retry/open-child answer shapes. Dispatch, shared structural-delivery and parent/child messaging DTOs are absent.

## Code Commentary

`RetireChildRequest` (frozen dataclass) carries required `agent_id` and `role: LauncherRole` (all canonical roles including `bootstrap`, plus legacy `system-specialist` normalization), `reason`, `interrupt_turn=False`, and optional `sprint_document_ref`, `master_document_ref`, and `task_document_ref` (taskless seats need none). The native retirement owner (`cli/role_retire.py` and `application/seat_retirement_scope.py`), not this dataclass, enforces caller scope, receipt uniqueness, open-child refusal, and interruption permission.

`RetirementIntent`, `RecordedSeatSelection` (serializing `RoleSelection` by camelCase alias), and `OpenChildSeat` model retry intent and open-child refusal payloads. `RetireChildResponse` inherits `ToolResponse` and declares `operation="retire_child"`, `status`, optional `sprintDocumentRef`, `masterDocumentRef`, `taskDocumentRef`, `role` (validated through `canonical_role`), `detail`, `retireIntent`, and `openChildren`. Internal task gate/activation owners remain separate; this DTO is not a plane-hosting API.

## Evidence

- `RetireChildRequest`, `RetirementIntent`, `RecordedSeatSelection`, `OpenChildSeat`, and `RetireChildResponse` define the native scope-based seat-retirement request/response wire shapes without dispatch/shared-delivery DTOs. [1]
- `RetireChildRequest.role` uses `LauncherRole` (all canonical roles including `bootstrap`) and `RetireChildResponse._canonical_role` normalizes through `canonical_role`. [2]
