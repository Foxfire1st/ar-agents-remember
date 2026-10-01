# mcp/src/agents_remember/models/structural/gates.py

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
- `StructuralLifecycleGateRequest`/`StructuralGateDecisionRequest` carry an optional `caller`
  (`DeclaredCaller`) used only when the process has no plane-injected seat; the structural
  authorization validates the declared role/document before any decision is recorded (L16-R3).
- Internal correlation stays available for the application service to complete the transaction.
- Strict response models reject accidental mixed public/internal payloads.

### Todos

None.

## Evidence

### Docs References


### Repo-Internal References

- Structural requests are separated from internal exact-id responses. [1]
- Public list summaries expose structural identity. [2]

### Cross-Repo References
