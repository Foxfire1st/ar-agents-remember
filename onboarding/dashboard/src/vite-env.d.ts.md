# dashboard/src/vite-env.d.ts

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

## Evidence

### Docs References

No relevant documentation was found after checking the configured sources; current claims are
proven by repository source and build configuration.

No relevant external or domain documentation is configured for this ambient declaration.

### Repo-Internal References

- Consumes the declared build constant. [1]
- Supplies the build-time value. [2]

### Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local ambient
declaration.

The reviewed behavior is wholly repository-local.
