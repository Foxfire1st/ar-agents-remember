# dashboard/scripts/check-diff-coverage.test.mjs

## Governing Overview

[dashboard/scripts overview](overview.md)

## Purpose

The contract suite for the executable-statement diff-coverage accounting, added by
the round-8 metric fix. It pins what v8 records as an executable changed line, what
counts as covered, the exclusion set, and `dashboard/` key normalization.

## Code Commentary

### Logic

One subprocess test removes the Dagger attestation and proves the direct changed-lines
CLI refuses before it reads Git or coverage. Five further tests drive the pure helpers
with synthetic v8 entries: statement-range spanning, executed-only spanning,
denominator semantics (a changed line with no statement contributes nothing), no-entry
files, and the test/dev/types exclusions with `dashboard/`-prefixed key normalization.

### Conventions

Vitest collects `scripts/**/*.test.mjs` via `dashboard/vitest.config.ts`; the suite
is logic-only (no DOM).

### Invariants And Boundaries

The suite must stay aligned with the Python gate's accounting intent: a changed
comment/blank/continuation line is never in the denominator. Running these pure
Vitest assertions directly is diagnostic only; it does not turn the refused CLI into
a host acceptance or changed-lines evidence path.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The direct CLI refusal occurs before base-resolution output. [1]
- The pure executable-statement helpers remain directly importable and tested. [2]
- Vitest includes script tests in its declared test population. [3]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
