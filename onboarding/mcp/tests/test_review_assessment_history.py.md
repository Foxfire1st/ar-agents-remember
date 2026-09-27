# mcp/tests/test_review_assessment_history.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_assessment_history.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:02:28+00:00 |
| lastVerifiedCommitHash | `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`|
| lastVerifiedCommitDate | 2026-09-27T07:57:14+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Exercise normal owner assessment capture, cleanup/restart reading and explicit exact-parent recovery through production entry points.

## Code Commentary

### Logic

Fixtures publish two different exact-subject judgments through the guarded curator operation, invoke the public comparison command, remove disposable worktree state and read history through a fresh process. Later source or canonical-pointer movement must not replace the pinned objects or provenance.

The cases keep other channels available when a bound artifact is corrupted, distinguish measured-empty from uncaptured history, and prove explicit generation 2-to-3 recovery with unchanged parents and exact retry. Invalid parent/digest/source selection and reserved-owner impersonation refuse.

### Conventions

Use the existing typed owners and exact recorded identities. Keep operation evidence and candidate provenance in task notes.

### Invariants And Boundaries

These are disposable production-composition regressions. They do not mutate original L38/L40 records or establish installed-runtime/product acceptance.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured. The repository declarations below support this contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The cited owners carry the behavior and failure boundaries described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| Normal capture survives cleanup and later pointer/source movement. | `test_public_capture_survives_cleanup_restart_and_later_canonical_source_movement` | mcp/tests/test_review_assessment_history.py:159-214 |
| Damaged expected artifacts isolate the affected channel. | `test_corrupt_bound_artifact_is_unavailable_without_erasing_other_channels` | mcp/tests/test_review_assessment_history.py:218-255 |
| Empty and uncaptured history remain different facts. | `test_new_measured_empty_is_distinct_from_legacy_not_captured` | mcp/tests/test_review_assessment_history.py:258-287 |
| Explicit successor recovery preserves parent bytes and judgments. | `test_explicit_recovery_keeps_two_legacy_generations_and_publishes_exact_successor` | mcp/tests/test_review_assessment_history.py:290-345 |

## Cross-Repo References

No separate repository supplies this contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | — | — |

## Update History

- 2026-09-27T05:02:28+00:00 — Created this source-mirrored card for the durable assessment-history boundary. Verification hash/date remain blank until normal closeout records the actual accepted code commit.
