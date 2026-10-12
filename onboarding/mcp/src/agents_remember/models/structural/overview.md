# Structural Wire Models Overview

## What This Area Is

This package defines structural request and response vocabulary addressed by canonical task documents and roles. Its agent-operation models describe dispatch and native receipt-tracked retirement; its gate models separate structural outcomes from internal exact-id responses. It also defines the internal durable activation record and corrupt-entry archive evidence for atomic-series work.

Activation identity belongs to the canonical series contract, rather than a protected code/memory source pair. Two atomic masters sharing a source pair therefore have independent activation records. Each record binds the selected master's `TaskDocumentRef` and canonical contract path without making activation identity a public runtime address.

## Hot Path Summary

Read `agent.py` for dispatch/native-retirement requests and structural target responses, `gates.py` for structural gate requests and the separate structural/internal response families, and `atomic_series_activation.py` for activation states, records, and archive evidence. Message and rename DTOs remain absent from `agent.py`. `RetireChildRequest` and `RetireChildResponse` are present for native receipt-tracked retirement; this does not restore the former hosted-seat path.

## Construction And Main Flows

`DispatchAgentRequest` is a frozen dataclass containing `task_document_ref`, `role`, `brief`, and optional `label`. `StructuralTargetResponse` identifies work and role, declares delivery-state fields, and canonicalizes the response role; `DispatchAgentResponse` fixes the operation to `dispatch_agent`. The frozen `RetireChildRequest` carries `task_document_ref`, `role`, `reason`, optional `agent_id` and default-false `interrupt_turn`; `RetireChildResponse` fixes the operation to `retire_child`. The native owner refuses an absent/invalid agent ID, checks the receipt's original starter and requires interruption permission for an active turn. Those are owner checks, not guarantees supplied by the dataclass. These responses inherit the shared strict tool envelope, so the work-domain boundary concerns their operation-specific identity fields rather than every inherited envelope field.

The dispatch registration constructs that request from the four advertised arguments. Its adapter calls the structural application service, which resolves the task document and caller behind the boundary. A hosted caller must pass child authorization; an ambient launcher has no parent seat but still undergoes role validation against document altitude. Invalid hosted identity is refused rather than treated as ambient. The structural outcome projection returns work identity and delivery state without occupant identity.

The gate request dataclasses carry gate content or a task-document decision, with an optional declared caller for processes lacking a hosted seat. The gate application service validates declared identity against hosted identity when both are present. Structural gate responses expose document, role, kind, state, and decision or wait information; internal response models separately retain exact gate and lifecycle correlations. Their presence in this package does not establish public tool availability.

The activation models are frozen and reject extra fields. `AtomicSeriesActivationRecord` contains schema version, contract fingerprint, selected master, contract path, state, positive revision, and selection time. Record states are `vacant`, `reconciling`, and `active`; selection states are `reconciling` and `active`; observations additionally distinguish `unreadable`. Archive evidence records the addressed fingerprint, activation path, snapshot identity and size, error information, replacement master, and archive time.

The activation store hashes the canonical resolved contract path to name the snapshot. Reads validate the record's fingerprint and resolved path against the addressed contract. Selection preserves an unchanged matching record or increments the previous valid record's revision; without a valid previous record it starts at revision one. Thus revision progression belongs to a valid retained snapshot, rather than promising an uninterrupted counter across corruption recovery.

## What Belongs Here

| Path | Role |
|---|---|
| `agent.py` | Agent-facing structural operation DTOs |
| `atomic_series_activation.py` | Internal per-contract activation selector and corrupt-entry archive records |
| `gates.py` | Agent-facing structural gate DTOs and isolated internal gate DTOs |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
|---|---|
| Catalog/runtime correlation models | Existing control-plane and terminal model modules |
| Address resolution behavior | `serving/structural_seats.py` and `application/structural/` |

## Local Invariants And Boundaries

- Dispatch input remains the canonical task-document address, role, brief, and optional label. The public-surface validator requires those exact input fields and the canonical repository/path shape; a runtime occupant address is not an additional dispatch argument.
- Structural response identity stays separate from internal exact-id gate and lifecycle response identity. Retaining internal models or services does not restore deleted agent APIs or establish their public registration. Native receipt-tracked `retire_child` is explicitly registered and rostered with its own agent-ID operand; dispatch still admits no occupant argument. The standing ban on compatibility aliases for the removed exact-id APIs remains separate from this explicit native restoration.
- Activation identity is keyed by the canonical series contract, never by repository/branch identity or a protected source pair. A snapshot whose fingerprint or resolved contract path differs from the addressed contract is treated as unreadable rather than adopted.
- The selected master's identity is checked against its canonical series contract when loading the selected contract. Queue, lifecycle, and task-document authority are not supplied merely by the activation model's fields.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
|---|---|---|---|
| `agent.py` | public schema | Pins dispatch's occupant-id exclusion and native retirement's receipt-tracked request shape | covered |
| `atomic_series_activation.py` | internal structural record | Separates the selected master and canonical contract identity from queue and lifecycle evidence | covered |
| `gates.py` | public/internal split | Prevents gate/lifecycle ids leaking to agents | covered |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
|---|---|---|---|
| `models/structural/__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Package marker |
| `models/structural/agent.py` | [`agent.py.md`](agent.py.md) | covered | Agent structural schemas |
| `models/structural/atomic_series_activation.py` | [`atomic_series_activation.py.md`](atomic_series_activation.py.md) | covered | Contract-scoped selector/archive vocabulary |
| `models/structural/gates.py` | [`gates.py.md`](gates.py.md) | covered | Structural gate schemas and relocated gate model knowledge |

## Child Overviews

No child overview is needed.

## How To Use This Area

Read this overview and the exact file card before modifying public structural or activation identity vocabulary.

## Retained Metadata And Verification Boundary

| Field | Value |
|---|---|
| sourceRoute | `mcp/src/agents_remember/models/structural/` |
| onboardingRoute | `mcp/src/agents_remember/models/structural/overview.md` |
| parentOverview | [`models/overview.md`](../overview.md) |

The retained tables are metadata, not execution or acceptance promises. The inherited verification statement is preserved as metadata:

> Commit-derived verification metadata awaits governed closeout; the activation-model path,
> contract-scoped vocabulary, and citations are reconciled to the frozen candidate.

Current lifecycle and closeout authority for that statement was not established by this source inspection. No test, native-host, whole-build, landing, or memory acceptance is asserted. References are source navigation, not fresh execution evidence.

## Evidence

- Current dispatch caller resolution owns the structural boundary; source inspection is not execution evidence. [1]
- The record carries the fingerprint, canonical path, selected master, record state, positive revision and selection time. [2]
- The store derives the fingerprint from the canonical resolved contract path and refuses any record that is not this exact contract. [3]
