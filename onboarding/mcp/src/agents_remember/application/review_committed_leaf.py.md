# mcp/src/agents_remember/application/review_committed_leaf.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Resolve a closed leaf's review to the pair it delivered, or reopen an explicitly numbered comparison or generation, without substituting live data.

## Code Commentary

resolve_review_comparison uses ordinary candidate resolution only when number is absent. A supplied number validates the task context, reads its recorded enclosure and reopens that exact tree comparison even while the leaf is live. It never captures open worktrees or substitutes a legacy generation for a missing number; missing records receive candidate_unresolved with the offending number.

`resolve_committed_leaf_review` reads the leaf contract and asks the delivered resolution first: a leaf whose enclosure records a delivery — a completed or checkpointed closeout or integration — opens the comparison those records name. A leaf that records no delivery keeps its previous recorded default, and a delivery the enclosure claims but this read cannot establish is answered by that resolution's own refusal rather than by the default. `generation_id` still addresses one recorded generation.

`resolve_recorded_leaf_review` is the same read with the delivered default switched off: it addresses the leaf's published comparison, which is what an explicitly historical request asks for. Both go through `_committed_read`, so the enclosure read, the no-enclosure refusal and the generation branch are shared.

`_default_read` returns the delivered resolution when the read asks for it, then falls back to reopening the leaf's recorded trees. `_generation_read` keeps the retained generation record and legacy_comparison_resolution behaviour, including ambiguous/unreadable generation refusals and the absent default generation's bare historical source range.

ClosedLeafReview holds the reopened source/evidence availability, generation id/state and limitation sentence. Historical canonical dataset halves stay legacy-unavailable: closed_leaf_limitations and closed_leaf_dataset_refusal name that boundary rather than reading today's memory or recreating retired datasets.

## Invariants And Boundaries

The delivered default, an explicit recorded-comparison read and an explicit legacy-generation read are different selectors with different owners. The module reads one namespace/enclosure; it grants no acceptance and does not replace missing canonical operands with current candidate data.

## Evidence

- A supplied number reopens only its tree record and refuses a missing enclosure/number. [36]
- Committed/default versus explicit legacy-generation reopening keeps retained identities. [37]
- Historical limitations and dataset refusal preserve missing canonical sides. [38]
- The closed-leaf holder exposes the actual reopened generation and state. [39]

- A closed leaf's default read asks the delivered resolution first, and a leaf with no delivery keeps its recorded default. [40]
- The recorded read addresses the leaf's published comparison with the delivered default switched off. [41]
- The shared read keeps the enclosure refusal and the generation branch. [42]
