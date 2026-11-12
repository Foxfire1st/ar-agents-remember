# mcp/src/agents_remember/application/memory_quality/census.py

## Governing Overview

[Application overview](../overview.md)

## Purpose

Builds the complete memory-candidate census used before certification admission and adapts every
governed onboarding identity into the curator's one-to-one coherence candidate list. The module
keeps this structural inventory non-certifying: it reports exact rows and blockers without granting
semantic acceptance or a code/memory commit.

## Code Commentary

### Logic

`prepare_memory_census` captures the contract-scoped code and memory candidate pair and builds the
full `MemoryCensusResult`; prepared code recovery supplies the selected code tree as provenance
while retaining the logical pair identity. `publish_memory_census` rereads the scope before
atomically writing the enclosure report, returns bounded diagnostics, and marks any census blockers
without calling the result certified.

`census_curator_candidates` converts every governed census row exactly once to a
`CuratorSourceCandidate`, requiring an onboarding-relative path, canonical source identity, and
unique candidate identity. `_curator_source` takes a file or route artifact's source from
`_governed_metadata`, while entity rows and inline onboarding use their own canonical
identity rules. Missing or ambiguous identity fails closed.

**Converted memory (L37 fix round P1b).** `_governed_metadata` reads the governed card in its own format,
from the tree that holds it: the candidate for a present card, and for an absent one the tree the census
compared with (`scope.memory_comparison_tree`: the baseline, or its conversion). A tree without the layout
marker is read through the legacy metadata table. A converted card keeps no such table, so its kind and
source come from `converted_cards.converted_card_metadata`: the sidecar's `path`, or the card's place in the
tree. Before this, the first converted card raised `governed artifact lacks its canonical source identity`
and the full contract-scoped run failed. `prepare_memory_census` and `publish_memory_census` also pass
`census_base.census_comparison(contract)`, so a converted candidate is compared with K_B's conversion
(MIK-R24 rule 7) and the mechanical conversion counts for nothing.

### Conventions

Candidate reports are JSON with a schema version, exact scope, complete census, bounded response
rows, and a SHA-256 of the written bytes. The report is operational evidence only; the lifecycle
coherence authority owns semantic dispositions and publication.

### Invariants And Boundaries

- The captured scope must remain unchanged between preparation and report publication.
- Every governed onboarding artifact must map to one canonical source or entity identity; duplicate
  normalized identities are refused.
- Prepared code-tree input is provenance for recovery comparison and does not fabricate a commit.
- This module does not edit onboarding, decide curator judgments, certify tests, or publish protected
  source changes.

### Todos

None recorded.

## Evidence

### Docs References

The resolved Domain Documentation registry has no entries, so no external documentation claim is
made for this repository-owned census boundary.

No configured external source applies.

### Repo-Internal References

The source file is the direct implementation evidence; the application and closeout overviews
describe adjacent preparation and certification ownership.

- Contract-scoped census preparation and selected-tree provenance. [1]
- Exact report publication and non-certifying diagnostics. [2]
- One-to-one curator candidate mapping and canonical identity refusal. [3]
- Census publication is diagnostic and non-certifying. [4]

- The governed card's kind and source, read in its own format from the tree that holds it. [5]
- The census scope is captured with the converted-base comparison. [6]

### Cross-Repo References

No cross-repository implementation or external-system boundary is owned here.

No meaningful cross-repo reference applies.

## Source File Binding

The current uncommitted source bytes are SHA-256
`e34ba2fde7498ce60c0bbf5cd2a195e410f9190cd836c0dbb96c5f3ddc6422cd` (`6229` bytes, `153` lines).
Verification metadata remains blank until closeout creates a genuine code commit.
