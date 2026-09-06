# mcp/tests/test_quality_report_publication_security.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_report_publication_security.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `cfd0938103b1392e471144b6997c51a41591ad2b` |
| lastVerifiedCommitDate | 2026-09-04T08:34:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises report-publication confinement: an exported artifact outside the declared profile inventory refuses, nested legacy-directory symlinks cannot remove external reports, and generation symlinks cannot substitute external evidence. Profile-bound fixtures establish the artifact authority; this file no longer proves the old runtime-digest mutation matrix.

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

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Export cannot publish an artifact outside the profile inventory | `test_export_cannot_publish_an_artifact_outside_the_profile_inventory` | mcp/tests/test_quality_report_publication_security.py:44-64 |
| Nested legacy directory symlink cannot delete external reports | `test_nested_legacy_directory_symlink_cannot_delete_external_reports` | mcp/tests/test_quality_report_publication_security.py:66-89 |
| Generation symlink cannot substitute external evidence | `test_generation_symlink_cannot_substitute_external_evidence` | mcp/tests/test_quality_report_publication_security.py:91-128 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the new invalid-`runtimeAuthorityDigest` refusal case and the schema-v3.1 model field in the publication-security suite.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile-bound publication security test re-base.


- 2026-08-31T13:42+02:00 — A005 closeout repair completed the quality-result parser and immutable
  publication boundary matrix, including the branch set that had raised CRAP above threshold.

- 2026-08-31T08:05+02:00 — Added the A004 prior-pointer forcing case for an unrelated historical
  64-hex generation symlink.

- 2026-08-31T07:35+02:00 — Created for 260821-ARSPAWN-L5 independent-review repair. Verification remains closeout-owned.
