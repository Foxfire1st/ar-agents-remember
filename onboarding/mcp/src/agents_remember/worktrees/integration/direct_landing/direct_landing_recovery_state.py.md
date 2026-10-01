# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

- Typed classification checks actual code, memory repository/ref, and candidate evidence. [1]
- Memory receipt inference and output matching are based on actual Git lineage. [2]
- Prepared and committed intent convergence retain exact ref/tree checks. [3]
- Shared snapshots exclude cache data while retaining actual objects. [4]
- Recovery tests reject code/ref/content drift and accept cache absence or damage. [5]

### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.
