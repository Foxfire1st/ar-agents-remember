# mcp/src/agents_remember/models/certification/corrective.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/certification/corrective.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:03:08+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Package overview](overview.md)

## Purpose

Owns typed corrective dispositions carried across lifecycle admission boundaries.

## Code Commentary

### Logic

`CorrectiveInputChange` names one semantic input and requires distinct before/after digests. `RedCatalogDisposition` binds one failed or blocked rail, its exact prior result digest and corrective owner. Direct repair requires changed inputs without a repaired root; repaired-root disposition requires its root and no changed inputs. Changed inputs must be uniquely keyed and canonically sorted.

### Conventions

Input digests accept Git-width SHA-1 or SHA-256 values; the prior-result digest is SHA-256. Identifiers and rationale retain the shared unpadded semantic-text contract.

### Invariants And Boundaries

- Constructor validity does not prove that an input changed in the repository or that the named root repairs a failed rail. Admission compares dispositions with owner-produced observations and the complete prior-red catalog.
- Admission decides whether corrective evidence clears a prior failure. The wire shape separately rejects a second representation of the same input key.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry has no entries. This repository-owned contract is established by the source below.

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The disposition kinds are a closed vocabulary. | `CorrectiveDispositionKind` | mcp/src/agents_remember/models/certification/corrective.py:19-19 |
| Each corrective input must move an exact semantic identity. | `CorrectiveInputChange` | mcp/src/agents_remember/models/certification/corrective.py:22-38 |
| Direct/root shape, unique keys and canonical ordering are enforced together. | `RedCatalogDisposition` | mcp/src/agents_remember/models/certification/corrective.py:41-70 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |
## Update History

- 2026-09-06T15:03:08+00:00 — Added explicit not-applicable Docs/Cross-Repo reference rows required by the file-card template; source claims, verification stamps and all earlier history are unchanged.


- 2026-09-06T14:48:58+00:00 — Created from source at `c69d5171187fa1957025e393270db9f5a864ab14` for the shared wire/generation ownership split. Verification records source review, not gate execution or acceptance.
