# mcp/tests/test_lifecycle_operation_dry_run_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_operation_dry_run_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces lifecycle operation dry run l2 behavior at the public and durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_control_dry_run_projects_dead_sibling_without_publishing_exit`, `test_dry_run_compatibility_uses_pending_successor_as_current_authority`, `test_only_mutating_compatibility_publishes_proven_terminal_worker_exit`, `test_integration_resolution_emits_exact_generation_and_public_controls`. The suite forces task-addressed legal controls, immutable same-generation retry/recovery, evidence-safe cancellation, write-ahead successor revision, door publication, concurrency, and executable refusal paths.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The file defines `test_control_dry_run_projects_dead_sibling_without_publishing_exit`, `test_dry_run_compatibility_uses_pending_successor_as_current_authority`, `test_only_mutating_compatibility_publishes_proven_terminal_worker_exit`, `test_integration_resolution_emits_exact_generation_and_public_controls` as its principal forcing seams. | `_byte_tree`; `test_control_dry_run_projects_dead_sibling_without_publishing_exit` | mcp/tests/test_lifecycle_operation_dry_run_l2.py:51-56; mcp/tests/test_lifecycle_operation_dry_run_l2.py:59-116 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces byte-preserving lifecycle previews while sibling operation and worker-exit evidence is reconciled.

### Current Invariants

- Dry-run does not publish worker exit, journal, contract, door, or task mutations.
- Mutating execution may publish only evidence proven at the authoritative operation boundary.

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the lifecycle worker-state package relocation used by dry-run mocks; non-mutation and live-evidence forcing are unchanged.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
