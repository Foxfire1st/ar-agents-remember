# mcp/tests/test_quality_report_publication_security.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_report_publication_security.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Proves immutable quality-report publication refuses dangling result references and symlink
substitution at nested legacy and generation boundaries.


CCR-R22@v1 (L22, commit `685f83c44055`) re-bases publication-security tests on profile-bound
publication: helpers `_profile_execution` and `_publish_reports` publish a profile-admitted
generation, inventory and size enforcement now follow `PublishedArtifactDefinition` limits, and
assertions cover the schema-v3 profile identity fields.

## Code Commentary

### Logic

The suite builds minimal report exports, invokes publication, and asserts that an out-of-inventory
reference, a nested legacy-directory symlink, an exact candidate-generation symlink, or an unrelated
historical-generation symlink refuses without modifying external bytes or advancing the live pointer.
It also forces malformed authoritative results, inconsistent step-owned artifact claims,
no-follow inspection failures, irregular report-tree nodes, non-empty legacy cleanup preservation,
and undeclared generation contents.

### Conventions

Security tests exercise the publication boundary with real filesystem nodes and candidate-bound
results.

### Invariants And Boundaries

- Authoritative results cannot name unpublished artifacts.
- Cleanup never follows a nested legacy symlink.
- Existing generation links cannot substitute external evidence.
- An irregular unrelated 64-hex historical generation is rejected before the live pointer moves.
- External sentinel bytes remain unchanged after refusal.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Dangling result references refuse publication. | `test_result_cannot_reference_an_artifact_outside_the_export_inventory` | mcp/tests/test_quality_report_publication_security.py:24-49 |
| Nested and generation symlinks cannot escape publication ownership. | `test_nested_legacy_directory_symlink_cannot_delete_external_reports`; `test_generation_symlink_cannot_substitute_external_evidence` | mcp/tests/test_quality_report_publication_security.py:51-120 |
| An unrelated historical-generation symlink preserves both the external sentinel and prior live pointer. | `test_historical_generation_symlink_refuses_before_pointer_moves` | mcp/tests/test_quality_report_publication_security.py:118-151 |

## Cross-Repo References

No cross-repository implementation dependency governs this suite.

## Update History
- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile-bound publication security test re-base.


- 2026-08-31T13:42+02:00 — A005 closeout repair completed the quality-result parser and immutable
  publication boundary matrix, including the branch set that had raised CRAP above threshold.

- 2026-08-31T08:05+02:00 — Added the A004 prior-pointer forcing case for an unrelated historical
  64-hex generation symlink.

- 2026-08-31T07:35+02:00 — Created for 260821-ARSPAWN-L5 independent-review repair. Verification remains closeout-owned.
