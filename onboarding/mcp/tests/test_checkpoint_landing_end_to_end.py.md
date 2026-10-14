# mcp/tests/test_checkpoint_landing_end_to_end.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the current working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Exercise composed checkpoint and ordinary integration behavior against real temporary code/memory repositories.

## Code Commentary

### Current Contract

The module defines 18 scenario methods. Its retained Git/ref/cache/approval checks now also assert answered closeout-incomplete, atomic-series-closeout-master-incomplete and checkpoint-master-complete outcomes, children-not-retired cleanup, and abandoned-master preview/apply refusal with worktree_abandon guidance. The repeated-checkpoint assertion remains in a genuinely still-unclosed frame. These are source assertions, not a newly run landing or a sync-behavior finding.

### Logic

> **Retained historical source account — superseded by the current contract:**
> The sixteen scenario definitions start from QueueFixture's unfinished atomic master and its exact series/leaf contracts. `_unclosed_contract` asserts empty closeout code/memory outputs rather than fabricating completion. Most checkpoint scenarios use the shared public-tool helper; targeted ordinary-entry and approval tests also call their operation seam directly.

> **Retained historical source account — superseded by the current contract:**
> The cases verify live-pair preview/apply publication, a real merged memory source, source divergence refusal, idempotent retry and continued work, ordinary final-route completion requirements, closeout preview/apply parity, unchanged leaf preview admission, and ordinary leaf integration with no cache file. They preserve the distinction between checkpoint publication and a stop-only pause.

> **Retained historical source account — superseded by the current contract:**
> A bare code advance that no leaf landed is refused by both checkpoint preview and apply with `knowledge-gate-refused` and `atomic-series-leaf-chain-invalid`, naming the foreign commit, preserving both work-branch tips, and fabricating no ledger row. Missing, stale, or malformed cache data on an owned source checkout cannot block checkpoint publication. Actual master-complete, approval, and ref-race guards remain, including a race response that names the checkpoint tool. Successful assertions read both destination refs and persisted contract cells; refusals verify the relevant refs did not move.

### Conventions

Each test owns a temporary world registered for cleanup during setup, including setup failure. Cached-table corruption/refusal matrices and their old flake note are superseded by current Git-fact scenarios; their prior history remains historical evidence.

### Invariants And Boundaries

- An unfinished checkpoint does not require closeout outputs or claim completed task state.
- The accepted pair is the live code and actual memory ref, not a cache-selected pair.
- Preview and apply preserve completion/source/approval boundaries.
- Cache damage does not become a publication gate; a bare code advance outside the admitted leaf chain is refused.
- Substantive divergence and CAS races remain visible.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.


### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

### Current Source-Inspection References

- **Retained historical source account — superseded by the current contract:** Initial live-pair capture, source merge, and source divergence. [1]
- **Retained historical source account — superseded by the current contract:** Retry, continued work, and final-route completion semantics. [2]
- **Retained historical source account — superseded by the current contract:** Ordinary leaf cache absence and bare code-advance leaf-chain refusal are asserted. [3]
- **Retained historical source account — superseded by the current contract:** Source-cache damage does not block; real approval/master/race guards survive. [4]
- **Retained historical source account — superseded by the current contract:** Checkpoint publication remains distinct from pause. [5]

- The module defines 18 scenario methods. Its retained Git/ref/cache/approval checks now also assert answered closeout-incomplete, atomic-series-closeout-master-incomplete and checkpoint-master-complete outcomes, children-not-retired cleanup, and abandoned-master preview/apply refusal with worktree_abandon guidance. The repeated-checkpoint assertion remains in a genuinely still-unclosed frame. These are source assertions, not a newly run landing or a sync-behavior finding. [6]
