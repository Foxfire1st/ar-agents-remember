# dashboard/src/data/submitClient.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Provides transport-level regression proof for FEUI-L5 reliable submission, especially the boundary
between certified pre-dispatch failure and ambiguous response loss.

## Code Commentary

### Logic

The suite drives exact epoch/id/text requests through success, queued, rejection, unknown,
unsupported, deadline, first-byte loss, safe certificate, and reconciliation paths. It proves that
only the typed server certificate retries, all possible-post-write failures keep one id and perform
status/reconcile without resending, and store updates respect source provenance plus draft revision
CAS. Create-then-ready scenarios verify that UI composition can precede bridge readiness without
allowing premature delivery.

### Invariants And Boundaries

- Assertions count native-facing submit calls so a test cannot pass while silently duplicating a
  prompt.
- Safe retry reuses both id and text; a new user send gets a new id.
- Non-composer sends cannot clear or restore the composer draft.

### 2026-07-24 Curator Delta

Regression coverage now exercises the honest queued receipt, delivering draft-clear path, live-turn
submission gate, and continued lifecycle polling after non-terminal authority states.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository.

No configured live domain-documentation source was available.

### Repo-Internal References

- The system under test owns transport classification and store-driving. [1]
- Shared fixtures name accepted, ambiguous, queued, and withdrawal scenarios. [2]

### Cross-Repo References

No meaningful cross-repo references found.

This is a repository-local unit suite.

## FEUI-L8 Reviewed Candidate Delta

Adds polite receipt-copy coverage and proves only the focused session announces accepted/queued/rejected/unsupported delivery truth.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
