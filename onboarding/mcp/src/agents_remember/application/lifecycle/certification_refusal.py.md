# mcp/src/agents_remember/application/lifecycle/certification_refusal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/certification_refusal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-08T16:05:21+02:00 |
| lastVerifiedCommitHash | `602143bd1d48226f4d53b83ff7c5002a695dcdff`|
| lastVerifiedCommitDate | 2026-09-09T00:26:24+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `_json_value` owns the described value or transition boundary. | `_json_value` | mcp/src/agents_remember/application/lifecycle/certification_refusal.py:10-17 |
| `certification_admission_refusal` owns the described value or transition boundary. | `certification_admission_refusal` | mcp/src/agents_remember/application/lifecycle/certification_refusal.py:20-32 |

## Cross-Repo References

No cross-repository implementation boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | N/A | N/A |

## Update History

- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: recorded the route-review finding promotion and exact-contract boundary from the frozen L38 source. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.

- 2026-09-06T15:06:50+00:00 — Created from actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented exact selection, refusal and transition ownership. Source verification does not assert runtime execution or CCR acceptance.
