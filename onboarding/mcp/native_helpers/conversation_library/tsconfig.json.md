# mcp/native_helpers/conversation_library/tsconfig.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/native_helpers/conversation_library/tsconfig.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Locked native conversation-library helper overview](overview.md)

## Purpose

Defines the helper's strict, no-emit TypeScript compilation boundary.

## Code Commentary

### Logic

Targets ES2022/NodeNext, checks only `src/**/*.ts`, emits nothing, and enables strict mode,
unchecked-index safety, and exact optional-property semantics while skipping dependency declaration
rechecking.

### Conventions

The helper remains an ESM Node package and uses compilation as a contract check, not a build step.

### Invariants And Boundaries

- Preserve `strict`, `noUncheckedIndexedAccess`, and `exactOptionalPropertyTypes`.
- `noEmit` prevents generated output from becoming a second source surface.
- Keep the include scope inside this helper's `src/` route.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this internal compiler configuration.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package's `typecheck` script invokes this no-emit configuration. | `typecheck` | mcp/native_helpers/conversation_library/package.json:9-12 |
| Protocol code and tests are the complete included TypeScript source set. | "export const PROTOCOL_VERSION" | mcp/native_helpers/conversation_library/src/protocol.ts:13-13 |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local configuration.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` row with an exact
  anchor and fixer-generated range; exact non-fixing check returns zero findings.

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the strict compiler-config sidecar.
  Verification is blank until closeout commits and stamps the new source.
