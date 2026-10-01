# mcp/tests/lifecycle_enclosure_test_support.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Provides small explicit builders for lifecycle-enclosure addressability forcing.

## Code Commentary

### Logic

Builders produce exact locator, manifest, predecessor, and archive shapes while leaving scenario differences local.

### Conventions

Tests execute production owners and use shared builders only for canonical setup. Scenario-specific
differences remain in the test so fixtures do not become a parallel implementation.

### Invariants And Boundaries

- The suite preserves loud negative cases and exact identity/refusal assertions; it does not obtain
  green through a fallback, allowlist, or weakened production threshold.
- Dagger owns certifying execution. Any direct execution remains bounded diagnostic evidence only.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

- No external domain source is required for this repository-owned test contract. [1]

### Repo-Internal References

The test file is direct evidence for the production boundary named above.

- The selected scenarios and assertions implement this test unit's forcing proof. [2]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings.

- No meaningful cross-repository reference applies. [3]
