# dashboard/src/App.tsx

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

## Evidence

### Docs References

No domain documentation is configured. This card describes repository source only.

### Repo-Internal References

These constructs establish the behavior described above.

- Development import guard and pathname-based view selection [1]

### Cross-Repo References

No cross-repository behavior is implemented in this file.
