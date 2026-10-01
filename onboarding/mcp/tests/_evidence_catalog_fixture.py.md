# mcp/tests/_evidence_catalog_fixture.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Provides one lifecycle-valid synthetic catalog builder for isolated ownership, retry, and metadata
contract tests.

## Code Commentary

### Logic

`write_synthetic_evidence_catalog` requires at least one artifact and one consumer per artifact,
then writes the complete current schema with internal-canonical unit-regression defaults.

### Conventions

Tests vary only the facts relevant to their case instead of hand-copying the full metadata schema.

### Invariants And Boundaries

- This helper is test support, not the production catalog authority.
- It emits every required field and cannot create an empty catalog or consumerless artifact.
- Schema changes have one synthetic builder to update.

### Todos

None.

## Evidence

### Docs References

No external documentation governs this synthetic helper.

### Repo-Internal References

- One function writes complete current lifecycle metadata. [1]
- Production validation owns the accepted schema. [2]

### Cross-Repo References

No cross-repository boundary is involved.
