# mcp/tests/_quality_evidence_fixture.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_quality_evidence_fixture.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:27+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Provides one canonical fixture for tests that need a successfully published immutable quality
generation. It replaces repeated mocks that returned a green dictionary without publishing the
evidence the lifecycle consumer actually verifies.

## Code Commentary

### Logic

`publish_passing_quality_gate` records the current index tree, writes the canonical passed result
into a temporary export, invokes the clean-executor publication primitive, and returns the public
gate summary bound to the same candidate tree and diff base.

### Conventions

The fixture publishes the production evidence shape but remains explicit test support. Callers may
vary attestation and diff base; ignored plan/invocation parameters preserve the gate-double call
shape without inventing alternate behavior.

### Invariants And Boundaries

- A mocked successful gate must publish immutable evidence; a return dictionary alone is
  insufficient for lifecycle consumers.
- The candidate tree comes from the target index and must match the published generation.
- This helper cannot create acceptance evidence outside tests or bypass clean-executor validation.
- Private publication access is isolated here so individual tests do not duplicate it.

### Todos

None recorded.

## Docs References

No external Domain Documentation source governs this internal fixture.

## Repo-Internal References

The source file is the direct evidence for the canonical test publication seam.

| Finding | Anchor | Source |
| --- | --- | --- |
| The helper binds a passed published result to the current candidate tree and optional attestation. | `publish_passing_quality_gate` | mcp/tests/_quality_evidence_fixture.py:15-45 |
| Publication uses the clean-executor report owner rather than a dictionary-only mock. | `_publish_reports` | mcp/tests/_quality_evidence_fixture.py:26-38 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test helper.

## Update History

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: created for the canonical published-quality fixture and verified against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this provenance does not certify the red Dagger gate.
