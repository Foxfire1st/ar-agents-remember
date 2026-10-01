# mcp/src/agents_remember/application/knowledge_leaf/pages.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Pages of the family-complete leaf read, cut by the shared threshold (MIK-R01 with MIK-R02).** The same `PreparedLeaf` builds page 1 inside a `read_ar_files` block and every page of `knowledge_read`'s `source_context` view, so both surfaces return one selection under one manifest (rule 6). **Since MIK-R05** a path seed's page also states its route chain (`routeChain`), an entry-less path with a governing family is a page, and a *family seed* pages one family's full content under the same policy.

## Code Commentary

### Logic

- **`LeafRequest`.** The index path, the memory tree ID, the index state, the seed (a `path`, or since MIK-R05 a `family` ID; `path` is optional and `seed_json` gives `{"kind": "path", "path"}` or `{"kind": "family", "id"}`, which `PreparedLeaf.seed_json` now delegates to), the code tree entries are observed at (MIK-R03; its ID is what the walk binds) and an optional continuation to resume.
- **`prepare_leaf(request)`** opens the index with `expected_key` set to the memory tree, then:
  - the seed is selected through `_select` (a path's `select_leaf`, or a family's `select_family`);
  - a path with no live entry **and no governing family** returns `registration_absent_refusal(path=…, with_proofs=True)`, whose wording names "realization or proof claim" (ruling N6, 2026-09-30 00:08:39); a family seed the tree holds no live family for returns `selector_absent_refusal(record_id=…, kind="live family")`;
  - otherwise it computes the selection's currentness once (`_currentness`), the rows (`leaf_rows`) and the counts (`leaf_counts`);
  - it binds the page with a `PageBinding`: the memory tree, policy `family-complete-leaf` / `v2` (bumped by MIK-R05, ruling Q4 of 2026-09-30 03:32:18), the structure's manifest digest and the code tree ID;
  - a resumed read is checked with L02's `position_refusal` against the manifest and the row total;
  - queued seeds (`rest`) have the first one's manifest computed (`_next_manifest`, which selects through `_select`, so a queued seed may be a path or a family), and a queued seed that selects nothing is refused `continuation_binding_mismatch` rather than skipped.
- **`_currentness`.** `invariant_currentness` at the code tree, with each family header's `FamilyCurrentness` counting live members only. A failure in `CURRENTNESS_FAILURES` returns the rows with states unset and the reason in `problem`: currentness is advisory beside the answer (L03 ruling N2).
- **`PreparedLeaf`.** It has the shape of L02's `PreparedScope`, so `block_pages` cuts either:
  - `render(cut)` is the seed's page (`_page`);
  - `deferred()` is the seed's counts and a position-0 continuation when the block is already full;
  - `collapsed(queued)` is this seed and the queued seeds as one deferred entry, whose single continuation walks them all.
  - Every token is minted with `response="leaf"` and `view=LEAF_VIEW` (`source_context`).
- **The page (`_page`).**
  - `seed`, `state: "page"` and `memoryTreeId` (rule 9); `manifestDigest`; `rows`; `counts` with the walk's `rowsReturned` and `rowsRemaining`; `hasMore`, `enumerationComplete` and `indexState`; `continuation`, `continuationOperation: "knowledge_read"` and `continuationView: "source_context"`; and `page`, L02's page block.
  - **The header reference is a literal first row** (carried obligation 1, L02 ruling Q3 of 2026-09-29 19:56:40): `_page` pops `headerReference` out of `page` and places the `family_header_reference` row at `rows[0]`. It repeats an identity already returned and is not counted as a returned row.
  - `enumerationComplete` is true only when the cut is complete *and* the index is `complete`: a page from a partial index is never presented as complete.
  - **The route chain (MIK-R05).** A path seed's page (not a family seed's) carries `routeChain` from `chain.route_chain_block`: `directory`, `links`, `derivation: "mechanical"`, `state` (`governed` or `no_governing_family`) and `families`. When the path has no seed invariant, the page also states `registration: {"state": "registration_absent", "detail"}`, with the N6 wording (MIK-R01 Failure: route-chain families are still returned). Every path page carries `routeChain`, even when it states `no_governing_family`, so the block's tokens can move the page-1 cut by one row on paged walks; the selection and the row sequence do not change (review R1 F3, accepted as designed on 2026-09-30 04:12:49).
  - When this seed is done and a queued seed follows, the token moves on to it with that seed's manifest, and the page names it as `continuationSeed`.
- **`absent_chain(path)`** is what a `registration_absent` refusal of a path adds: `{"routeChain": …}` stating `no_governing_family`. `tree_read._leaf_response` and `published_intent._tree_page_block` merge it into their refusals, so both surfaces state the same chain.
- **No local path in the token** (carried obligation 4, 2026-09-29 21:17:07). The continuation carries the seed path, the tree, the manifest and the code tree ID, never a repository root; `tree_read` resolves the repository from `repositoryRoot` or the mount workspace.

### Conventions

- `LEAF_VIEW` = `source_context` is the one view a leaf walk resumes on.
- A leaf has one declared row order; an ordering is not part of its binding (ruling Q7).

### Invariants And Boundaries

- **Every page continuing a family starts with a header reference row** (candidate invariant).
- **Both surfaces return one selection:** page 1 of the block and every `source_context` page come from one `PreparedLeaf`, under one manifest digest. Page-1 cuts may differ between surfaces, because the envelopes differ; the selection does not.
- **A queued seed is never silently dropped.**
- **An entry-less path is refused only when no family route covers it** (MIK-R05 Failure; ruling Q3 of 2026-09-30 03:32:18 kept the refusal for that case). `no_governing_family` itself is a state, not an error.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R01@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`01_family-complete-leaf-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module statement: one prepared leaf for both surfaces, and the header reference as a literal first row. [1]
- The view a leaf walk resumes on, and the request with its path or family seed. [2]
- The prepared leaf with its page, deferred and collapsed forms, each minting a `leaf` token. [3]
- The preparation: `selector_absent` for an unknown family seed, `registration_absent` (naming proof claims too) for a path with no entry and no governing family, the binding, and the position check of a resumed walk. [4]
- Currentness computed once per selection, advisory on failure, family headers counting live members. [5]
- The first queued seed's manifest, selected through the path-or-family step, and the refusal of a queued seed that selects nothing. [6]
- What a path's `registration_absent` refusal adds on both surfaces: its route chain, which found no family. [7]
- The token after a page: within the seed, or moving on to the next queued seed. [8]
- The page: the reference row first, the counts with the walk's position, a partial index never complete, and a path seed's `routeChain` with `registration` when it has no entry. [9]

### Cross-Repo References

No meaningful cross-repo references found: the pages read one memory tree's derived index.

No cross-repo boundary is crossed by this file.
