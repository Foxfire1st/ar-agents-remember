# mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pairing.py

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Provides the small closeout adapter that makes preview, apply, and recovery consume one pair
validator and one current curator-coherence authority.

## Code Commentary

`accepted_closeout_memory_pair` obtains the current coherence record, its exact pair, no-impact
judgments, record digest, and delivery attempt as one value. `resolve_closeout_memory_pair`
re-proves the contract-addressed pair for initial apply acknowledgement and post-commit recovery
without requiring stale pre-commit candidate-tree evidence. `memory_candidate_pair_payload`
renders the same typed identity into public closeout results.

Internal-memory and series closeout return no pair because MCAR-R03 applies only to
worktree-backed external-memory leaves. There is no repo-id re-resolution or alternate filename
reader.

## Invariants And Boundaries

- Preview and normal closeout consume the pair from the validated coherence authority.
- Apply admission and recovery invoke the same canonical resolver against the exact contract.
- Recovery does not depend on a pre-commit report that must become stale after commits.
- This adapter does not invent curator judgments or mutate either repository.

## Evidence

### Repo-Internal References

- Accepted coherence and exact pair facts are returned together. [1]
- Apply/recovery re-prove the exact contract pair. [2]
- Public closeout projection uses one pair payload writer. [3]

### Cross-Repo References

No cross-repository implementation reference applies.
