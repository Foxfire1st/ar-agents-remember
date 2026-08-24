# mcp/src/agents_remember/testing/selection_contract.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/selection_contract.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns the closed typed vocabulary passed between exact-selector resolution, static closure,
eligibility, bootstrap, and the direct runner.

## Code Commentary

`UnsafeEffectFamily` and `DirectRefusalCode` make every policy outcome explicit.
`EligibleDirectSelection` contains candidate root, exact nodes, complete closure, and immutable
binding. `RefusedDirectSelection` carries one stable reason and the whole refused selection.

## Invariants And Boundaries

- A decision is eligible or refused; there is no unknown/fallback result.
- Unsafe families and refusal codes are closed enums. Adding a member is a policy change.
- `DependencyObservation` is source-backed and may name one unsafe family; prose alone is not a
  classifier result.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closed unsafe and refusal vocabularies. | `UnsafeEffectFamily`; `DirectRefusalCode` | mcp/src/agents_remember/testing/selection_contract.py:13-44 |
| Atomic eligible/refused result shapes. | `EligibleDirectSelection`; `RefusedDirectSelection` | mcp/src/agents_remember/testing/selection_contract.py:66-85 |

## Update History

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
