# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:06 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Nearest governing overview](../overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Classifies live evidence for a retained direct-landing generation without mutating its journal.
The outcomes distinguish recoverable work, terminalizable output, and contradictions requiring a
developer decision.

## Code Commentary

### Logic

`classify_direct_landing_recovery` requires the typed direct input, the configured memory
repository and branch/ref, and the accepted code commit and candidate tree. It reads a disposable
memory snapshot with `memory_cache=True`; no cached ledger table participates in classification.

`_direct_recovery_outputs` uses durable memory cells or a proven commit, recognizes an accepted
clean-memory reuse, and can infer an unpublished receipt from the exact mutation lineage.
`_memory_commit_matches_intent` checks the parent and expected tree of the actual memory commit.
The output must still be at the accepted ref and satisfy the shared clean-snapshot predicate.

Before a commit, convergence requires either the exact accepted snapshot or an allowed prepared
state on the same ref, HEAD/tree, and reflog base with the bound candidate/index tree. After a
commit, parent, ref, tree, and clean state must match the intent. Changed code, memory ref, or
unaccepted content produces a decision surface. An absent or malformed cache does not.

The former ledger mapping states, accepted/intended cache-byte digests, and ledger-only output
reconstruction are removed. The classifier reports a memory commit when one is proven; it never
creates a dummy mapping to fill missing attribution.

### Conventions

This is a read-only classifier over typed snapshots. The integration mutation-evidence owner
defines cleanliness; `contentHeadTree` permits cache-excluded comparison while actual `head` and
`headTree` remain available for ref and object proof.

### Invariants And Boundaries

- A matching cache row or the shape of HEAD alone cannot establish a memory output.
- Source code, exact memory repository/ref, and actual parent/tree lineage remain checked.
- Recovery does not consult cache bytes, cached row order, or historical ledger commits.
- Decision payloads preserve expected/observed evidence and never silently choose a different generation.

### Todos

No new file-local follow-up is established by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

| Finding | Anchor | Source |
| --- | --- | --- |
| Typed classification checks actual code, memory repository/ref, and candidate evidence. | `DirectLandingRecoveryClassification`; `_memory_output_matches_evidence` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py:30-53; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py:226-252 |
| Memory receipt inference and output matching are based on actual Git lineage. | `_direct_recovery_outputs`; `_memory_output_matches_evidence` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py:185-204; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py:226-252 |
| Prepared and committed intent convergence retain exact ref/tree checks. | `_mutation_intent_converges`; `_committed_intent_converges` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py:300-319 |
| Shared snapshots exclude cache data while retaining actual objects. | `snapshot_is_clean_at_head`; `_exclude_cache_from_index` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:42-57; mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:476-479 |
| Recovery tests reject code/ref/content drift and accept cache absence or damage. | `_recover_after_interrupted_receipt`; `test_direct_landing_publishes_memory_and_recovers_independently_of_cache` | mcp/tests/test_direct_landing.py:171-272 |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History

- 2026-09-15T01:06 UTC — Rebound source citation ranges after final shared-helper updates and formatting; current body contracts rechecked against the working candidate. No committed-source hash or execution claim was advanced.


- 2026-09-15T00:51 UTC — Replaced ledger mapping/byte-state reconstruction with code and memory Git evidence; documented cache-excluded snapshots, preserved parent/ref/tree checks, and no dummy attribution for clean reuse. Working candidate verified by source inspection; real last-touch commit metadata retained, with no future commit hash or certification claim.


- 2026-08-27T18:33+02:00 — Removed the private clean-snapshot duplicate and consumed the shared
  mutation-evidence predicate; recovery semantics are unchanged.
- 2026-08-26T17:49+02:00 — Replaced single-prepend byte equality with the complete newest-first
  recovery proof: the current operation mapping must be first, accepted history must remain an exact
  suffix, canonical metadata and rendering must hold, and commit lineage/path evidence remains
  exact. This admits legitimate intervening history without weakening corruption detection.

- 2026-08-26T14:32+02:00 — Added the explicit `historical` ledger state so valid same-code memory
  history remains recoverable while unreadable or intent-conflicting evidence still fails closed.
  Verification remains closeout-owned.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: documented the exact lineage and byte predicates for direct-landing recovery. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
