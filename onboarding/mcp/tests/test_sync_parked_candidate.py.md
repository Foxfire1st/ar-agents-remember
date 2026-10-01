# mcp/tests/test_sync_parked_candidate.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Exercise the parked worktree candidate inside the existing sync transaction and prove its return, retained conflicts, cancellation, and recovery.

## Code Commentary

### Logic

The six cases reuse SyncFixture's real repositories and contracts. Clean code carry restores modified/untracked WIP and advances the recorded base. The external-memory case now includes staged cache data beside a real onboarding draft: only the draft appears in parked WIP, and the draft returns with no remaining stash.

Other cases preserve a genuine reapply conflict and its wipRestore marker, return the candidate on cancel, resume a crash before restoration, continue a staged source conflict without losing parked content, and refuse a pre-existing genuine unmerged index without creating a stash. The module validates the public resolution projection as well as the dictionary so producer/model drift is visible.

### Conventions

Intentional fault injection stops restoration once; native Git creates the genuine conflict. Assertions cover exact payload state, candidate bytes, stash identity/emptiness, and recorded bases. These are transaction-level scenarios, not a full closeout acceptance claim.

### Invariants And Boundaries

- Real parked content must return; a memory cache is not part of that candidate.
- A genuine reapply conflict retains the stash until resolution or cancellation.
- Resume must return an already-parked candidate without inventing another merge.
- Pre-existing real conflicts still refuse admission.
- Code-domain files keep ordinary semantics.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Code and memory WIP return, with cache excluded from the memory candidate. [1]
- Genuine reapply conflict and cancellation preserve candidate content. [2]
- Crash recovery and retained-source continuation return parked work. [3]
- Pre-existing genuine conflicts remain a refusal. [4]
- Production parked-content boundary and exact restore proof. [5]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
