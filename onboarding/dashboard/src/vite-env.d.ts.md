# dashboard/src/vite-env.d.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/vite-env.d.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T12:43+02:00 |
| lastVerifiedCommitHash | `82f2de40a666ea00754f364cfe764cea9294235f`|
| lastVerifiedCommitDate | 2026-07-18T13:07:00+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[dashboard/src overview](overview.md)

## Purpose

This ambient declaration connects Vite's client types with the dashboard-build fingerprint constant
injected by the build configuration.

## Code Commentary

### Logic

The file preserves the Vite client type reference and declares `__AR_DASHBOARD_BUILD__` as a string.
That declaration is the compile-time type seam consumed by `data/buildIdentity.ts`; it does not
provide a runtime default or infer a fingerprint.

### Conventions

The ambient identifier and string type must match the Vite and Vitest `define` keys exactly.

### Invariants And Boundaries

- Runtime value ownership remains in the Vite `define` configuration.
- The declared symbol is a string and is not optional at client compile time.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Docs References

No relevant documentation was found after checking the configured sources; current claims are
proven by repository source and build configuration.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external or domain documentation is configured for this ambient declaration. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Consumes the declared build constant. | L1-L10 | [data/buildIdentity.ts](data/buildIdentity.ts) |
| Supplies the build-time value. | L65 | [vite.config.ts](../vite.config.ts) |

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local ambient
declaration.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | Import and task-boundary review | — |

## Update History

- 2026-07-18T12:43+02:00 — FEUI-L9R: created the missing one-to-one card for the modified ambient
  declaration; verification metadata stays blank until the code candidate is committed and closeout
  can stamp it.
