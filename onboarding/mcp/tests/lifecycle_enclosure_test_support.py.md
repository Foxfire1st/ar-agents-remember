# mcp/tests/lifecycle_enclosure_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/lifecycle_enclosure_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Provides shared test builders for the public lifecycle-control and enclosure-addressability forcing suites.

## Code Commentary

### Logic

The principal forcing seams are `enclosure_contract`, `publish_test_enclosure`, `byte_tree`. The suite forces locator and immutable root-manifest publication, confinement and digest contradictions, idempotent pre-adoption enclosure adoption, and exact root-journal recovery after task-contract loss.

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
| The file defines `enclosure_contract`, `publish_test_enclosure`, `byte_tree` as its principal forcing seams. | L23-L52; L55-L56; L59-L64 | `mcp/tests/lifecycle_enclosure_test_support.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Provides small explicit builders for immutable enclosure manifest, locator, journal, contract, and byte-tree forcing.

### Current Invariants

- Published test enclosures use the canonical address chain.
- Byte-tree snapshots make crash and refusal purity assertions exact.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
