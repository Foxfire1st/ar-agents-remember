# mcp/src/agents_remember/memory_quality/memory_census.py

## Governing Overview

[Memory quality overview](overview.md)

## Purpose

Builds the deterministic governed-memory census from the contract-owned exact Git scope. The census reads exact code and memory trees, classifies file sidecars, inline onboarding, route overviews, and entity rows, and emits a structural worklist without making semantic acceptance or final-certification decisions. Current candidate metadata is authoritative for live mappings; historical metadata is retained only for removal context and cannot veto a valid current mapping.

## Code Commentary

### Logic

`_Tree` reads exact Git members and metadata without silently normalizing paths. `_Census.sidecars` validates current canonical mappings and carries a historical mapping forward only when its path is absent from the candidate tree. `_Census.edited_documents` treats current metadata as authoritative, blocks current missing metadata, and uses a historical-only document to retain an absent row without a removal blocker. `_Census.add` records the expected final presence and preserves pre-existing absent rows for curator accountability. `_Census` records governed identities, presence, source paths, and reasons across sidecars, inline blocks, route overviews, edited documents, and entity rows. `build_memory_census` assembles the ordered result from the route-owned `MemoryCensusScope`.

**Converted memory (L37 fix round P1b).** `_Tree.converted` is true when the tree holds the layout marker. For
such a tree `_Tree` loads each card's kind and source through `_load_converted_metadata`: the sidecars are
read in one batch and `converted_cards.converted_card_metadata` answers in the legacy table's keys, so the
rest of the census reads both formats through one shape. `build_memory_census` builds its "before" tree from
`scope.memory_comparison_tree` (the baseline, or its conversion: MIK-R24 rule 7), so the mechanical conversion
is never an edit. `_Census.edited_paths` decides what the task edited on a converted tree: a memory path the
scope lists, plus the card of every sidecar with a counted change
(`worktrees/modules/onboarding_trace.counted_sidecar_change`); a change of only an anchor's `blob`, line
numbers and `content` (the fixer's mechanical re-recording) is not an edit, exactly as MIK-R30 rule 3 counts
it. Before this, every converted card was a `contradictory-artifact-type` blocker (2,509 on the cutover leaf).

### Invariants And Boundaries

- Exact Git tree membership and UTF-8 relative paths are validated before a row is emitted.
- Current missing or contradictory sidecar metadata remains a structural blocker; a stale historical association alone does not veto a valid current mapping.
- Missing newly required artifacts remain structural blockers; pre-existing artifacts absent from the candidate remain census rows with `expectedFinalPresence=absent` for curator accountability.
- The census is a derived preparation worklist; it does not publish semantic judgments, coherence, or certification.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; the repository source is the governing evidence.

- The census module has no external domain dependency. [1]

### Repo-Internal References

- Exact Git members and metadata are read through the private tree reader. [2]
- Current sidecar mappings are authoritative, while historical mappings survive only for paths removed from the candidate tree. [3]
- Edited current metadata is checked for missing or contradictory artifact type and mapping; historical-only documents retain an absent row without a removal blocker. [4]
- Structural rows are accumulated for inline onboarding, route overviews, and entities. [5]
- The route-owned scope is converted into one ordered census result. [6]

- A converted tree's cards get their kind and source from the converted format, sidecars read in one batch. [7]
- On a converted tree a sidecar's counted change is its card's edit; anchor-only re-recording is not. [8]
- The census compares the candidate with the scope's comparison tree. [9]

### Cross-Repo References

None; this module consumes the resolved local code/memory pair only.
