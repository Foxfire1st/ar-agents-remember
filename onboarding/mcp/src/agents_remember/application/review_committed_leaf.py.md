# mcp/src/agents_remember/application/review_committed_leaf.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Resolve an explicitly numbered tree comparison or reopen a committed leaf’s exact retained historical operands without substituting live data.

## Code Commentary

resolve_review_comparison uses ordinary candidate resolution only when number is absent. A supplied number validates the task context, reads its recorded enclosure and reopens that exact tree comparison even while the leaf is live. It never captures open worktrees or substitutes a legacy generation for a missing number; missing records receive candidate_unresolved with the offending number.

The separate resolve_committed_leaf_review first tries converted four-tree reopening when no legacy generation id was supplied. Explicit historical generation or the legacy path delegates through the retained generation record to legacy_comparison_resolution. Ambiguous/unreadable generation refusals remain explicit; the absent default generation can preserve its bare historical source range.

ClosedLeafReview holds the reopened source/evidence availability, generation id/state and limitation sentence. Historical canonical dataset halves stay legacy-unavailable: closed_leaf_limitations and closed_leaf_dataset_refusal name that boundary rather than reading today’s memory or recreating retired datasets.

## Invariants And Boundaries

Numbered-record reads and explicit legacy-generation reads are different selectors with different owners. The module reads one namespace/enclosure; it grants no acceptance and does not replace missing canonical operands with current candidate data.

## Evidence

- A supplied number reopens only its tree record and refuses a missing enclosure/number. [36]
- Committed/default versus explicit legacy-generation reopening keeps retained identities. [37]
- Historical limitations and dataset refusal preserve missing canonical sides. [38]
- The closed-leaf holder exposes the actual reopened generation and state. [39]
