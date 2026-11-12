# familyExpressions.ts

## Governing Overview

[overview.md](../overview.md)

## Purpose

Group carried family realization claims into deduplicated expression summaries without changing their recorded identity.

## Code Commentary

### Logic

carriedMembership preserves before and after membership rows. familyExpressionExcerpts first counts changed, resolved and unmeasured realization outcomes, groups changed claims by path plus recorded source identity, then attaches all per-side readings for those keys. Observed identities are readings, never part of the grouping key. Occurrences retain exact revision IDs and sides; deterministic ordering stabilizes the presentation.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.

### Invariants And Boundaries

Different recorded blobs at the same path remain distinct. A path resolved on one side and mismatched on the other remains one expression with both readings. These realization-resolution counts are not the measured source-change inventory and imply no semantic assessment.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

No configured domain source could be checked.

### Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

- `carriedMembership` owns the behavior described above. [1]
- `familyExpressionExcerpts` owns the behavior described above. [2]
- `excerptKey` owns the behavior described above. [3]
- `recordSideReadings` owns the behavior described above. [4]

### Cross-Repo References

No independent cross-repository interface is introduced by this source.

No additional cross-repository evidence is required.
