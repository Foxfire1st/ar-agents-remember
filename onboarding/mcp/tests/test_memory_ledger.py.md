# mcp/tests/test_memory_ledger.py

## Governing Overview

[Nearest governing overview](overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Tests the ledger's newest-first data format and verifies that runtime ledger readers derive
mappings from committed attribution while treating cached tables only as observations.

## Code Commentary

### Logic

The serialization case preserves repeated code commits as ordered memory history: `find_mapping`
returns the newest row and `contains_mapping` can still find an older exact pair. These are lookup
semantics of derived data, not permission to perform Git operations.

`_World` now creates real code commits and attributed memory commits. Its projection cases check
unreachable cache rows, ordering and header differences, a byte-identical correct cache, and forged
metadata/pairs whose objects exist but whose claimed attribution does not. Contract and named-ref
reads survive absent or malformed caches; the named-ref case also creates a same-named tag to prove
that the exact local branch is selected. An unreadable Git commit still raises the explicit refusal.

`_AttributedWorld` retains historical cache-checkpoint commits as a fixture alongside actual
attributed content. The reader must produce the attributed rows at each checkpoint, ignore
hand-written table pairs, and emit no mappings from wholly unattributed history. A partially
attributed history contributes only its real trailers. Invalid source and branch code targets are
reported as exclusions instead of retained. Reversed or incomplete cached superseding pairs cannot
change the order supplied by actual memory history.

The remaining cases cover empty history, branch exclusion, last trailer-block parsing, body
lookalikes, mixed trailer blocks, optional code-object filtering, and attributed commits inherited
through a merge. The writer/reader round trip commits a message rendered by the real effective
closeout input, so it checks that the actual writer's key is recognized by the actual Git reader.

### Conventions

The file retains twenty tests. Historical ledger commits are explicit fixture data for testing
cache independence; they do not prescribe current runtime writes or a fallback reader. Literal
trailer spellings in parser tests are independent oracles, while the writer round trip deliberately
uses the production renderer. Temporary repositories and source assertions provide focused
development evidence, not certification or live integration proof.

### Invariants And Boundaries

- Runtime projection cannot union pre-rule cached rows into attributed Git history.
- A valid-looking pair of existing objects is insufficient without matching committed attribution.
- Cache absence/damage remains distinct from a genuine Git lookup failure.
- Invalid code targets remain visible as exclusions; merged-in attributed history remains visible.
- Repeated valid code-to-memory states keep Git-derived newest-first ordering.
- Historical entries below do not require restoring retired table-authority assertions or ledger legs.

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

- Data round-trip and current-versus-historical lookup semantics. [1]
- Actual attributed fixtures, cache forgery, cache misses, and exact local-ref selection. [2]
- Unattributed and partially attributed histories cannot inherit cached pairs. [3]
- Invalid targets are reported and superseding order comes from actual history. [4]
- The real writer/reader round trip and merged-in attribution stay covered. [5]
- Unattributed and partially attributed histories cannot inherit cached pairs. [6]
- The runtime projection under test separates computed mappings from cache observations. [7]

### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.
