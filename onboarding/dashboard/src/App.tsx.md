# dashboard/src/App.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/App.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:47:44+00:00 |
| lastVerifiedCommitHash | `c041ff5fade16d9e4de73a4d2404574effb98cab` |
| lastVerifiedCommitDate | 2026-06-14T17:36:44+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Selects the cockpit or the development harness at the application's top level.

## Code Commentary

### Logic

The development flag controls creation of the lazy DevApp import. When that component exists and the pathname begins with /dev/, App renders it under Suspense with a null loading view. Every other case renders Cockpit.

### Conventions

The pathname switch is local to this component. Development-only loading stays inside the environment guard.

### Invariants And Boundaries

When the development flag is false, this component always selects Cockpit. The source guard expresses the production bundle boundary; this card does not claim a bundle build was run.

### Todos

None recorded.

## Docs References

No domain documentation is configured. This card describes repository source only.

## Repo-Internal References

These constructs establish the behavior described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| Development import guard and pathname-based view selection | `DevApp`; `App`; `Cockpit`; `Suspense` | dashboard/src/App.tsx:1-19 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

## Update History

- 2026-09-05T06:47:44+00:00 — Created during L31 full-population memory recovery from frozen ea359649; verification records the actual source-touching commit. Documentation evidence only.
