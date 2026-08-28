# mcp/tests/_evidence_catalog_fixture.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_evidence_catalog_fixture.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

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

## Docs References

No external documentation governs this synthetic helper.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One function writes complete current lifecycle metadata. | `write_synthetic_evidence_catalog` | mcp/tests/_evidence_catalog_fixture.py:1-50 |
| Production validation owns the accepted schema. | `load_evidence_inventory` | mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:140-236 |

## Cross-Repo References

No cross-repository boundary is involved.

## Update History

- 2026-08-25T01:56+02:00 — Created to stop synthetic tests from duplicating lifecycle metadata.
