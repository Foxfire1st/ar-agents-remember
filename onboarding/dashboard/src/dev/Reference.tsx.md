# dashboard/src/dev/Reference.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/dev/Reference.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T07:08:26+00:00 |
| lastVerifiedCommitHash | `c041ff5fade16d9e4de73a4d2404574effb98cab` |
| lastVerifiedCommitDate | 2026-06-14T17:36:44+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Displays the imported mc2 design reference beside development views.

## Code Commentary

### Logic

Imports the HTML as raw text and passes it to an iframe through srcDoc. A surrounding bar labels the canonical design endpoint.

### Conventions

The component owns presentation of the reference; DevApp selects it for /dev/reference.

### Invariants And Boundaries

The iframe content comes from the imported snapshot. This component provides no source-editing control; its read-only label is not a sandbox declaration.

### Todos

None recorded.

## Docs References

No domain documentation is configured. This card describes repository source only.

## Repo-Internal References

These constructs establish the behavior described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| Raw reference import and iframe presentation | `Reference`; `mc2`; `srcDoc` | dashboard/src/dev/Reference.tsx:1-13 |
| Development route selects this reference component | "if (path.startsWith(\"/dev/reference\")) return <Reference />;" | dashboard/src/dev/DevApp.tsx:15-15 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

## Update History

- 2026-09-05T07:08:26+00:00 — L31 final residual curation against frozen code `ea35964985f30080488270e71ac81657ac40682b`: Replaced ambiguous imported/called component names with the unique route-selection statement; component and route behavior unchanged. This scoped repair does not promote the card's verification stamp or certify a gate.

- 2026-09-05T06:47:44+00:00 — Created during L31 full-population memory recovery from frozen ea359649; verification records the actual source-touching commit. Documentation evidence only.
