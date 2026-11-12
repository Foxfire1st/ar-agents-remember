# mcp/tests/test_static.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Serves controlled built-bundle and missing-bundle worlds. Entry HTML revalidates while assets retain their own cache policy; missing output returns 503 with the actual build command and no-store, while the API remains usable. A source checkout without a built bundle is an explicit supported state, not evidence of an installed UI.

## Current source account

New cases reserve unknown /api paths from static fallback for GET/HEAD/POST/PUT/DELETE both with and without a bundle. Registered API routes retain success or wrong-method 405; API-prefixed lookalikes and assets keep static behavior. A companion case keeps index/assets served and missing-bundle 503 notice intact; OPTIONS is not part of the matrix.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Built bundle is served with revalidated html [1]
- Missing bundle answers 503 with the build command [2]
- Missing bundle leaves the api alone [3]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
