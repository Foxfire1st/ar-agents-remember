# mcp/tests/test_review_assessment_history.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_assessment_history.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:05:09+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Exercise normal owner assessment capture, cleanup/restart reading and explicit exact-parent recovery through production entry points.

## Code Commentary

### Logic

Fixtures publish two different exact-subject judgments through the guarded curator operation, invoke the public comparison command, remove disposable worktree state and read history through a fresh process. Later source or canonical-pointer movement must not replace the pinned objects or provenance.

The cases keep other channels available when a bound artifact is corrupted, distinguish measured-empty from uncaptured history, and prove explicit generation 2-to-3 recovery with unchanged parents and exact retry. Invalid parent/digest/source selection and reserved-owner impersonation refuse.

**The many-missing-artifacts case (MIK-L25 Q8, fixed in MIK-L31).** `_curator_channel` stubs `_historical_records` to raise the owner's own "Bound curator artifacts are unavailable: <paths>" error over a resolved leaf whose reserved owner evidence is missing, and returns the assessments channel. With 100 artifacts the channel is `unavailable`, lists all 100 as `unreadable`, and its detail names "100 bound artifacts" and the first ones, not the last. With 10 artifacts (review F6, strengthened by R2-2 so the two branches write different text) the landed detail fits `PROSE_MAX_LENGTH` and is kept exactly, without the summary phrase; forcing the summarising branch fails the case.

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
| Normal capture survives cleanup and later pointer/source movement. | `test_public_capture_survives_cleanup_restart_and_later_canonical_source_movement` | mcp/tests/test_review_assessment_history.py:162-217 |
| Damaged expected artifacts isolate the affected channel. | `test_corrupt_bound_artifact_is_unavailable_without_erasing_other_channels` | mcp/tests/test_review_assessment_history.py:220-258 |
| Empty and uncaptured history remain different facts. | `test_new_measured_empty_is_distinct_from_legacy_not_captured` | mcp/tests/test_review_assessment_history.py:261-290 |
| An over-length unreadable-owner detail is summarised; one that fits keeps its landed wording exactly; every artifact is listed either way. | `_curator_channel`; `test_a_leaf_binding_many_missing_curator_artifacts_reads_as_unavailable` | mcp/tests/test_review_assessment_history.py:422-434; mcp/tests/test_review_assessment_history.py:437-460 |
| Explicit successor recovery preserves parent bytes and judgments. | `test_explicit_recovery_keeps_two_legacy_generations_and_publishes_exact_successor` | mcp/tests/test_review_assessment_history.py:293-348 |

## Cross-Repo References

No separate repository supplies this contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | — | — |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Logic records the new Q8 case (the carried MIK-L25 Q8 `ValidationError`, fixed here and accepted at 05:36:19) with its two branches pinned apart (review F6 at 06:10:21, R2-2 at 06:47:03); one row added.

- 2026-09-27T05:02:28+00:00 — Created this source-mirrored card for the durable assessment-history boundary. Verification hash/date remain blank until normal closeout records the actual accepted code commit.
