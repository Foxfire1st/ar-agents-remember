# mcp/src/agents_remember/application/lifecycle/certification_refusal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/certification_refusal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:06:50+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing lifecycle overview](overview.md)

## Purpose

Renders the complete typed certification-admission refusal for public lifecycle adapters.

## Code Commentary

### Logic

`certification_admission_refusal` returns the operation, refused state/status, error detail, every typed finding and zero declared gate starts. `_json_value` recursively converts mappings to string-keyed dictionaries, non-string/bytes sequences to lists, and bytes to an explicit hexadecimal representation. It preserves each finding rather than truncating to the first failure.

### Conventions

Use this renderer at the admission exception boundary after the actual owner refuses; it does not perform admission itself.

### Invariants And Boundaries

- The renderer does not execute gates, inspect their processes or change lifecycle state.
- Its recursive conversion handles mappings, sequences and bytes explicitly; unrelated objects are returned as supplied.

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

- 2026-09-06T15:06:50+00:00 — Created from actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented exact selection, refusal and transition ownership. Source verification does not assert runtime execution or CCR acceptance.
