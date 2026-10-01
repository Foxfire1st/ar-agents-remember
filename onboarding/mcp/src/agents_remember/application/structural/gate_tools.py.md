# mcp/src/agents_remember/application/structural/gate_tools.py

## Governing Overview

[Structural application services](overview.md)

## Purpose

Provides lifecycle-gate creation, decision, and list operations addressed by structural
document-and-role relationships instead of caller-supplied lifecycle or gate ids. Since
260815-DAG-L16 the caller may be a hosted seat or — when the process has no plane seat — a
request-carried declared caller (L16-R3).

## Code Commentary

### Logic

`_context` resolves the ambient caller through `resolve_ambient_seat`; a hosted seat wins and any
`AmbientSeatError` other than `ambient-seat-unavailable` reraises. On `ambient-seat-unavailable` it
builds a duck-typed `DeclaredGateCaller` (carrying only `binding_role` and
`binding_task_document_ref`) from the request `caller` (missing → `structural-caller-required`), and
`_refuse_declared_conflict` refuses a request-carried caller that contradicts the hosted seat
(`structural-caller-conflict`). Because the structural tools read only
`binding_role`/`binding_task_document_ref` (duck-typed `DeclaredGateCaller` vs
`TerminalCatalogEntry`, both `TaskDocumentRef`-typed, canonicalized — equality checks sound), the
same topology-based authorization validates the declared caller exactly like a hosted seat
(`_authorize_gate_target` → `authorize_child`). The runtime then qualifies the target seat,
authorizes the relationship, and invokes internal gate tools; `_failure` normalizes refusals into
typed payloads and the public response construction removes plane-only correlation ids.

### Conventions

Public gate responses use task-document and role identity. Internal response models remain confined
to the plane-facing call seam. The declared caller is assertion, not plane proof: it grants no
authority beyond the same role/document pair a seat would have (L16 F5 trust model); the residual
risk is deployment-level (who may reach the server).

### Invariants And Boundaries

- Agents do not select lifecycle or gate records by id.
- A caller cannot decide a gate outside its authorized structural relation.
- Only `ambient-seat-unavailable` triggers the declared-caller fallback; a declared caller that
  contradicts the hosted seat refuses (`structural-caller-conflict`); other seat errors reraise.
- List results redact plane-only correlation fields.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.


### Repo-Internal References

- Lifecycle-gate creation resolves a structural target before invoking internal gate creation. [1]
- Gate decisions and listing authorize through the same ambient structural context. [2]

### Cross-Repo References
