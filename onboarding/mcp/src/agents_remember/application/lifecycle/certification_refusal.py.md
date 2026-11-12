# mcp/src/agents_remember/application/lifecycle/certification_refusal.py

## Governing Overview

[Governing lifecycle overview](overview.md)

## Purpose

Renders the complete typed certification-admission refusal for public lifecycle adapters.

## Code Commentary

### Logic

`certification_admission_refusal` returns the operation, refused state/status, error detail, every typed finding and zero declared gate starts. `_json_value` recursively converts mappings to string-keyed dictionaries, non-string/bytes sequences to lists, and bytes to an explicit hexadecimal representation. It preserves each finding rather than truncating to the first failure.

CCR-R25 adds a route-review promotion after the complete finding list is built. When a
`CertificationContractError` contains a typed `routeReview` finding, the renderer delegates to
`route_review_refusal_projection` and overlays the concrete route status, expected/observed facts,
next action, and bounded next step while retaining `findings` and `gateStarts`. The optional
contract supplies the exact task address for a `task_doc` retry; without it the renderer emits
guidance only and never invents a task or review payload.

### Conventions

Use this renderer at the admission exception boundary after the actual owner refuses; it does not perform admission itself.

### Invariants And Boundaries

- The renderer does not execute gates, inspect their processes or change lifecycle state.
- Its recursive conversion handles mappings, sequences and bytes explicitly; unrelated objects are returned as supplied.
- Route-review promotion preserves the original certification envelope and delegates classification
  to the shared route-review projector; it does not decide whether a review is required.
- A missing contract identity suppresses executable task arguments rather than guessing a destination.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

No configured domain documentation applies.

### Repo-Internal References

- `_json_value` owns the described value or transition boundary. [1]
- `certification_admission_refusal` owns the described value or transition boundary. [2]

### Cross-Repo References

No cross-repository implementation boundary is owned by this file.

No cross-repository reference is required.
