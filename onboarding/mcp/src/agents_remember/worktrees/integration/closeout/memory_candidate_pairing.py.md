# mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pairing.py

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Defines retained helpers for resolving a contract-addressed memory pair, reading current Curator coherence facts, and formatting a pair identity.

## Code Commentary

`accepted_closeout_memory_pair` can return the current coherence record’s exact pair, no-impact judgments, record digest and delivery attempt. `resolve_closeout_memory_pair` resolves its external-memory leaf pair from the exact contract. `memory_candidate_pair_payload` formats that type for a caller. These helpers have no production callers on the synchronous preview or apply path.

Internal-memory and series closeout return no pair because MCAR-R03 applies only to
worktree-backed external-memory leaves. There is no repo-id re-resolution or alternate filename
reader.

## Invariants And Boundaries

- The ordinary synchronous owner revalidates its exact candidate and knowledge gate. Required structured coherence is validated through the separate curation procedure before apply.
- The retained leaf-pair resolver passes the contract path and configured repository to the canonical pair resolver.
- This adapter does not invent curator judgments or mutate either repository.

## Evidence

### Repo-Internal References

- Accepted coherence and exact pair facts are returned together. [1]
- The retained external-memory helper resolves the paired roots from the exact contract. [2]
- The retained projection helper formats a resolved pair identity when called. [3]

### Cross-Repo References

No cross-repository implementation reference applies.
