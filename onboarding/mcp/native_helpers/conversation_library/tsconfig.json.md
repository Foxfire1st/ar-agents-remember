# mcp/native_helpers/conversation_library/tsconfig.json

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

## Evidence

### Docs References

No Domain Documentation source is configured for this internal compiler configuration.

No configured domain documentation was available.

### Repo-Internal References

- The package's `typecheck` script invokes this no-emit configuration. [1]
- Protocol code and tests are the complete included TypeScript source set. [2]

### Cross-Repo References

No meaningful cross-repo boundary exists for this local configuration.

No meaningful cross-repo references found.
