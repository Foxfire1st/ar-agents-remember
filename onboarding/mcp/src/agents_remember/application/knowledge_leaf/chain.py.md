# mcp/src/agents_remember/application/knowledge_leaf/chain.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The route chain of a seed path, appended to its leaf read (MIK-R05@v2).** A path sees every family whose territory it lies in, even when it realizes none of the family's members: a new or unattributed file is the typical case. Families are listed only at their own routes (MIK-R04, D20), so the read walks upward from the path's directory. The module also owns the `served_earlier` rendering that only `read_ar_files` applies to chain entries.

## Code Commentary

### Logic

- **The chain (rule 1).** `chain_directory(path)` is the path's directory (`.` at the repository root). `_links(directory)` is that directory, then every ancestor, ending with `ROOT_ROUTE_PATH` (`.`). It is computed at read time from the path alone and labelled `CHAIN_DERIVATION` = `mechanical`. Nothing walks down into a child or a sibling directory, and no ownership is inferred (MIK-R05 Exclusions).
- **The lookup (`select_chain(index, path, seed)`).** It asks L23's `KnowledgeIndex.families_governing(directory)`, which already walks self-and-ancestors to `.`, so the index is not edited and `INDEX_FORMAT` is unchanged. For each family found:
  - it reads the family through `index.family`, and skips a missing record, a non-`family` record or a `retired` one (so L13's decision records, which are other `ix_record` kinds, never appear);
  - `members` are the family's live invariants only (`_live_invariant`);
  - `via` are the family's routes that lie on the chain, nearest first;
  - `member_at_seed` is true when one of its live members is a seed invariant, that is, has an entry at the seed path.
  - The result is sorted by the distance of the nearest matching route, then by family ID (ruling Q3, 2026-09-30 03:32:18). A family with several routes on the chain is one entry, placed at its nearest route, with all of them in `via`.
- **The compact entry (`chain_row`, rule 2).** `kind: "chain_family"`, `id`, `revision`, `title`, `guarantee`, `routes`, `memberCount` (live members), `via`, `memberAtSeed`, and `expand`: `{"operation": "knowledge_read", "view": "source_context", "familyRevisionId": <ID>}`, the family seed that returns the full MIK-R01 content (rule 3). The row holds no member list and no statements. `expand` names the bare ID, so it survives revision bumps (review R1 F6, accepted as designed).
- **`memberAtSeed` families keep their row** (ruling Q2, 2026-09-30 03:32:18). Rule 4 says the selection always includes all chain entries, so a family the MIK-R01 content already expanded above still gets its compact row, with `memberAtSeed: true`; its R01 content is not repeated.
- **The statement of the chain (`route_chain_block`).** `directory`, `links` (the chain's length), `derivation: "mechanical"`, `state` (`governed`, or `NO_GOVERNING_FAMILY` = `no_governing_family` when no route covers the path; a state, not an error) and `families`. It names the directory and the link count rather than listing each ancestor, because a list would grow with the square of the path's depth (ruling Q3).
- **The `read_ar_files` rendering (rule 4).** `shorten_served(block, should_serve)` walks each seed's `rows` in a published-intent block and replaces each `chain_family` row whose family was already served (per `should_serve(family_id, content_hash)`) with a `served_earlier` row: `kind`, `servedKind: "chain_family"`, `id`, `revision`, `title`, `via` and `memberAtSeed`. The row keeps its position, so the page's counts, manifest and continuation are those of the full selection. `served_hash` digests the row without the seed-dependent `via` and `memberAtSeed` (`_SEED_FIELDS`), so the same family reached from another path is recognised as served too.

### Conventions

- Row kind constants: `CHAIN_ROW` = `chain_family`, `SERVED_EARLIER` = `served_earlier`; the state constants `GOVERNED` and `NO_GOVERNING_FAMILY`.
- The module is pure: `select_chain` reads the index, and `shorten_served` takes the ledger decision as a callable, so the served ledger stays in `read_files.py`.

### Invariants And Boundaries

- **A leaf read returns the governing route chain after the leaf content, each chain row exactly once, within the bound** (candidate invariant; see the `application` overview). The rows are ordered last by `selection._order` and paged by L02's `cut_page` under the same threshold and token.
- **Upward only.** The chain is the directory and its ancestors; children and siblings are never walked (MIK-R05 Exclusions).
- **Only `read_ar_files` shortens.** `knowledge_read` never calls `shorten_served`; its rows are always full (rule 4).
- **Retired families and members are never counted or listed.**

### Todos

- **Real routes are unassigned today.** Every real family has `routes: []`, so every real read states `no_governing_family` until routes are assigned (MIK-R06 and curation). The L05 worker assigned routes in scratch only to show the chain on real data.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R05@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`05_route-chain-family-retrieval.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module statement: the chain, compact entries, the order, `no_governing_family`, and the rendering only `read_ar_files` applies. [1]
- The derivation label, the row kinds and the chain states. [2]
- The seed-dependent fields left out of the served hash. [3]
- One live family on the chain, with its live members, routes, the routes on the chain and whether a member is at the seed. [4]
- The chain's first link: the path's directory. [5]
- The lookup through the index's governing families, skipping retired and non-family records, ordered by nearest route then ID. [6]
- The chain: the directory, then every ancestor, ending at the root. [7]
- Only live invariants count as members. [8]
- The compact entry, with the family seed in `expand`. [9]
- The page's statement of the chain: the directory, the link count and the state. [10]
- The rendering only `read_ar_files` applies: a served entry keeps its place as a reference row. [11]

### Cross-Repo References

No meaningful cross-repo references found: the chain reads one memory tree's derived index.

No cross-repo boundary is crossed by this file.
