# mcp/tests/test_cross_master_concurrency.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Verify independent atomic masters sharing one protected source pair, private work, conflicting publication refusal, and ordinary completion after sibling reconciliation.

## Code Commentary

### Logic

QueueFixture builds two atomic masters with the same code/memory source branches and distinct work branches. The nine scenarios verify independent activation records and readiness, absence of A’s code and memory on the shared source refs, absence of A’s code in B’s code worktree and branch, B leaf landing while A remains unfinished, activation release without publication, stale/non-fast-forward publication refusal, explicit checkpoint availability, genuine graph dependencies, and graph-less concurrency.

The full completion scenario lands A's first leaf and completes B through ordinary closeout/integration. A's stopped interval is represented by before/after private-state snapshots; this is not execution coverage of the public pause tool. A then uses the public sync, starts its remaining leaf, and completes through ordinary closeout/integration without a checkpoint substitute.

Leaf helpers author code plus one attributed memory commit and refresh the cache outside Git. Sync reconciles real content; the former cache-union and ledger-only reconciled-pair write are removed. The final assertions prove both masters' code/memory ancestry and read committed attribution through derive_memory_ledger. No cached row order or mapping for an un-attributed merge commit is required.

### Conventions

Scenarios compose the shared queue, checkpoint, and closeout fixtures under a declared test process. Real fixture repositories establish local operation behavior, not a live orchestration run. Release, stopped-work snapshots, checkpoint publication, and final completion stay separate claims.

### Invariants And Boundaries

- A sibling selection, release, or landing cannot replace another master's activation record.
- The privacy case checks both shared source refs and B’s code worktree and branch. The stale-publication case checks that B’s publication survives.
- A reconciled master finishes through ordinary closeout and integration.
- Both masters' real code and memory histories survive; cache bytes are not retention proof.
- Only the authored dependency graph creates predecessor waiting; graph absence does not serialize independent masters.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.




- Separate activation leaves both masters ready. A’s private code and memory are absent from their respective shared source refs. A’s code is also absent from B’s code worktree and code branch. A separate case lands B’s leaf while A remains active. [1]





- Release and conflicting publication preserve sibling state. [2]




- The master completes the synchronous transaction after its sibling lands, retaining the actual histories. [3]


- The stopped interval is represented by snapshots, not a pause-tool call. [4]
- Checkpoint and authored/absent dependency behavior remain distinct. [5]


- Fixture commits are two actual outputs with Git-owned attribution. [6]



### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
