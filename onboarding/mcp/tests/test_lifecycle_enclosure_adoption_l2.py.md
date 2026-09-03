# mcp/tests/test_lifecycle_enclosure_adoption_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_enclosure_adoption_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces lifecycle enclosure adoption l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_adoption_and_schema_migration_execute_in_either_order`, `test_adoption_binds_exact_preview_and_refuses_changed_bytes_without_publication`, `test_lost_response_and_idempotent_replay_converge_to_one_receipt`, `test_adoption_conflict_refuses_before_locator_or_manifest_publication`. The suite forces locator and immutable root-manifest publication, confinement and digest contradictions, idempotent pre-adoption enclosure adoption, and exact root-journal recovery after task-contract loss.

Since 260831-CCR (commit `99dc249b`) the suite adds
`test_adoption_preserves_exact_missing_intent_generation_archive` (line 163-201): it writes an
exact `closeout-operation.legacy-missing-intent-generation-1.json` archive beside the legacy
source, proves the preview includes it while a near-match `.log` sibling does not, applies the
adoption, and asserts the archive lands byte-identical in the canonical `.lifecycle` root and is
admitted by the terminal archive `_canonical_entries` with the exact SHA-256.

### Conventions

Tests address operations by task/contract plus kind and generation, assert durable evidence and public legal controls, and compare state across failure cuts. Helpers remain test-only and invoke the same public/domain seams as production.

### Invariants And Boundaries

- A passing assertion must prove the advertised action executes or terminates safely; payload shape alone is insufficient.
- Queue projection is never accepted as lifecycle evidence, and private operation identifiers do not cross the public test boundary.
- Failure-path assertions check non-mutation or exact same-generation recovery, not merely an exception string.
- The legacy missing-intent generation archive is adopted byte-exact and terminally archived; a
  near-match file never qualifies.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to these repository-internal forcing tests.

## Repo-Internal References

The test source is the direct evidence for the regression contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The file defines `test_adoption_and_schema_migration_execute_in_either_order`, `test_adoption_binds_exact_preview_and_refuses_changed_bytes_without_publication`, `test_lost_response_and_idempotent_replay_converge_to_one_receipt`, `test_adoption_conflict_refuses_before_locator_or_manifest_publication` as its principal forcing seams. | `test_adoption_and_schema_migration_execute_in_either_order`; `test_adoption_binds_exact_preview_and_refuses_changed_bytes_without_publication`; `test_lost_response_and_idempotent_replay_converge_to_one_receipt`; `test_adoption_conflict_refuses_before_locator_or_manifest_publication` | mcp/tests/test_lifecycle_enclosure_adoption_l2.py:118-156; mcp/tests/test_lifecycle_enclosure_adoption_l2.py:212-229; mcp/tests/test_lifecycle_enclosure_adoption_l2.py:232-261; mcp/tests/test_lifecycle_enclosure_adoption_l2.py:264-279 |
| The missing-intent generation archive preservation regression. | `test_adoption_preserves_exact_missing_intent_generation_archive` | mcp/tests/test_lifecycle_enclosure_adoption_l2.py:163-201 |
| The shared closeout record payload builder used for the archive bytes. | `_closeout_record_payload` | mcp/tests/test_task_intent_consumers_and_legacy.py:1-700 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## CCR-R02@v2 Missing-Intent Archive Adoption

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, a legacy missing-intent
generation is preserved verbatim before its intent-bound successor; this regression proves
enclosure adoption carries that exact archive into the canonical root unchanged and that the
terminal archive admits it. Part of the landed L25 candidate `99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  added the missing-intent generation archive adoption regression to the documented forcing seams;
  verified byte-exact adoption and terminal-archive admission. Verified at code commit
  99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
