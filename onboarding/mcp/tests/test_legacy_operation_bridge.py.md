# mcp/tests/test_legacy_operation_bridge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_legacy_operation_bridge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces legacy operation bridge behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_normal_reader_refuses_legacy_and_inspect_preserves_exact_bytes`, `test_operation_key_mismatch_is_publicly_digest_bounded`, `test_migration_dry_run_is_byte_exact_and_leaves_no_lock_or_receipt`, `test_migration_preserves_proof_and_only_advertises_recover`. The suite bounds schema-1 inspect/migrate/archive and proves confinement, original-byte evidence, dedicated serialization, idempotence, removal guards, and separation from normal current-schema admission.

### Conventions

Tests address operations by task/contract plus kind and generation, assert durable evidence and public legal controls, and compare state across failure cuts. Helpers remain test-only and invoke the same public/domain seams as production.

### Invariants And Boundaries

- A passing assertion must prove the advertised action executes or terminates safely; payload shape alone is insufficient.
- Queue projection is never accepted as lifecycle evidence, and private operation identifiers do not cross the public test boundary.
- Failure-path assertions check non-mutation or exact same-generation recovery, not merely an exception string.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to these repository-internal forcing tests.

## Repo-Internal References

The test source is the direct evidence for the regression contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The file defines `test_normal_reader_refuses_legacy_and_inspect_preserves_exact_bytes`, `test_operation_key_mismatch_is_publicly_digest_bounded`, `test_migration_dry_run_is_byte_exact_and_leaves_no_lock_or_receipt`, `test_migration_preserves_proof_and_only_advertises_recover` as its principal forcing seams. | L240-L257; L259-L281; L283-L334; L336-L365 | `mcp/tests/test_legacy_operation_bridge.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces the isolated schema-1 lifecycle inspection, migration, and terminal archival bridge across malformed, partial, conflicting, and already-migrated records.

### Current Invariants

- The bridge preserves original bytes, digest, and Git evidence and writes one canonical current journal or terminal archive.
- Normal current readers never fall back to schema 1; the bridge is explicit, audited, bounded, and removable.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
