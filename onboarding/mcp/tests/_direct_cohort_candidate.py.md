# mcp/tests/_direct_cohort_candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_direct_cohort_candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Builds minimal content-sealed manifests for isolated direct-cohort forcing tests.

## Code Commentary

### Logic

`SyntheticCohortOptions` carries optional local-import, effect, known-effect, and closure facts.
`write_synthetic_direct_cohort` hashes exact synthetic files/configurations and emits current v2
file/node tables.

### Conventions

The helper uses production schema constants so tests do not reproduce version strings or bounds.

### Invariants And Boundaries

- The helper cannot alter the real checked-in cohort.
- Synthetic hashes come from the exact temporary bytes under test.
- It supplies declared facts; the production classifier still performs all validation/refusal.

### Todos

None.

## Docs References

No external documentation governs this synthetic helper.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Options and writer emit the complete current cohort schema. | `write_synthetic_direct_cohort` | mcp/tests/_direct_cohort_candidate.py:22-96 |
| The production parser remains the sole schema authority. | `load_direct_cohort_manifest` | mcp/src/agents_remember/testing/cohort_manifest.py:17-248 |

## Cross-Repo References

No cross-repository boundary is involved.

## Update History

- 2026-08-25T01:56+02:00 — Created after replacing generic analyzer fixtures with one sealed-cohort
  candidate builder.
