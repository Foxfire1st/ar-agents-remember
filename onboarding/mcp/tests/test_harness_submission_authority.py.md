# mcp/tests/test_harness_submission_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_submission_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Provides the focused concurrency and lifecycle proof for `HarnessSubmissionAuthority`, including
the pop-back linearization point that end-to-end FEUI-L5 required.

## Code Commentary

### Logic

The suite races withdrawal against dispatch, keeps status/withdraw responsive during slow adapter
work, and proves completion-before-receipt dominance for prompts and setters. It exercises full-ref
dedupe under id reuse, strict timeline ordering, payload/source conflicts, bounded duplicate tables,
certified preflight busy versus impossible safe retry after a possible first byte, epoch mismatch,
raw-free disclosure, and invalid operation references. These tests are the regression pins for the
architectural gap surfaced when Alt+Up first put queue, adapter, and UI behavior under one end-to-end
interaction.

### Invariants And Boundaries

- Concurrency tests synchronize at authority/adapter seams rather than relying on sleeps alone.
- A successful withdraw proves the operation never claimed adapter dispatch; losing the race keeps
  truthful non-withdrawable state.
- Early exact terminal evidence may dominate unknown, but stale/partial/id-only completion cannot.
- Bounds never evict live, active, or unknown rows.

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Slow-adapter responsiveness and dispatch/withdraw races. | L214-L292 | [test_harness_submission_authority.py](test_harness_submission_authority.py) |
| Early completion, full-ref reuse, ordering, conflicts, bounds, epoch, and privacy. | L293-L636 | [test_harness_submission_authority.py](test_harness_submission_authority.py) |
| The system under test defines the sole timeline and lifecycle lock. | — | [../src/agents_remember/serving/harness_submission_authority.py](../src/agents_remember/serving/harness_submission_authority.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This is a repository-local authority suite. | — | — |

## Update History

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; captured authoritative pop-back races,
  completion-before-receipt, exact-ref id reuse, ordering, idempotency/conflict, retry safety,
  retention, epoch, and privacy proofs. Verification metadata remains pinned to the leaf base.
