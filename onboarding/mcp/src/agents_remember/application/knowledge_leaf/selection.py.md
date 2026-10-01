# mcp/src/agents_remember/application/knowledge_leaf/selection.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**What one seed path selects, in which order, and the rows at a code tree (MIK-R01 rules 1 to 5, 7 and 8).** From the derived index of one memory tree (MIK-R23) it selects the entries at the path (realization *and* proof entries), their invariants, every family containing those invariants with its guarantee, routes and members, and every member's entries. Traversal is one family hop; a member's other families are advertised, never expanded. **MIK-R05 appends the route chain** (one compact `chain_family` row per live family routed at the path's directory or an ancestor, from `chain.py`) and adds the *family seed*, which selects one family's full content.

## Code Commentary

### Logic

- **Two steps, so the manifest never depends on a code tree.**
  - `select_leaf(index, path)` reads the structure, a `LeafStructure`: the seed invariants, the families, the members, the advertised frontier, the family titles and `order`, the row identities as `(kind, subject, group)` triples. Since MIK-R05 it also calls `select_chain` and keeps the result as `chain`; it returns `None` only when the path has **no live entry and no governing family** (a path with chain families but no entry is a page of chain rows).
  - `leaf_rows(structure, currentness)` renders that structure as `PageRow` values, each entry and invariant stated at the walk's code tree (MIK-R03).
  - **The family seed (`select_family`, MIK-R05 rule 3).** `_family` reads one live family; every live member is kept (`_member`), and `_structure` builds a `LeafStructure` with an empty `path`, no seed invariants and `family_seed` set, so `_order` gives the family's header, every member with its entries, then its advertised frontier. `None` when the tree holds no live family by that ID. `select_leaf` and `select_family` share `_structure` (the frontier, the titles and the order).
  - `LeafStructure.manifest_digest` is the `sha256_digest` of the policy label, the seed (the path, or `{"kind": "family", "id"}` for a family seed) and the ordered row identities only. That is why both surfaces agree on it even when their code trees differ (ruling Q4, 2026-09-29 23:21:57: conformance is the equal manifest digest, and entry states follow each surface's code tree).
- **The seed (`_seed_invariants`).** The live invariants of every realization and proof entry at the path, by ID. Proof entries seed the read (ruling Q3); the older scope read seeded on realizations only.
- **The families (`_families_of`).** The live families containing a seed invariant, each keeping only its live members. `_member` reads each invariant once per selection and keeps only live families; `_family` and `_live` reject a retired record, so a retired invariant or family is never selected, listed or counted (MIK-R23 ruling Q4).
- **The frontier (`_advertised`).** Each family a selected member belongs to outside the selection, **once**, with every selected member that reaches it, sorted (ruling N4, 2026-09-30 00:08:39). Its manifest identity is `("advertised_family", family, None)`.
- **The declared order (`_order`, rule 4).**
  1. The seed's own invariants, by ID: each a `member` row followed by its entry rows (`_ordered`: realizations, then proofs, each by path then entry ID).
  2. Each family, by ID: a `family_header` row, then its remaining members by ID. A seed invariant is listed in the header's `members` and **not repeated** (ruling Q2). A member already returned under an earlier family becomes a `member_reference` row (rule 5).
  3. One `advertised_family` row per frontier family.
  4. **The route chain (MIK-R05 rule 5):** one `chain_family` row per `structure.chain` entry, in `select_chain`'s order (nearest route, then family ID). It comes after all MIK-R01 content and has no paging group. A family expanded above still gets its chain row, flagged `memberAtSeed: true` (ruling Q2, 2026-09-30 03:32:18: the chain includes every entry).
- **Rendering (`_Rendering`, `_RENDERERS`).** One renderer per row kind: `_render_member`, `_render_entry` (realizations and proofs), `_render_header`, `_render_reference`, `_render_advertised` and, since MIK-R05, `_render_chain` (the compact row from `chain.chain_row`). The dispatch table and the helper extractions keep every function at or below 10 under radon (ruling N1).
  - **`member`** (`_member_row`): `id`, `revision`, `status`, `admission`, `statement`, `applicability`, `conditions`, `exclusions`, `state` and `families`, every live family containing it, selected or advertised (rule 7).
  - **`realization` / `proof`** (`_entry_row`): `id`, `invariant`, `path`, `locator`, `role` or `facet`, `state`, and `reason` when the entry is not current. `_observed` drops a read-wide reason (no code tree was requested), which the `currentness` block states once.
  - **`family_header`** (`_header_row`): `id`, `revision`, `status`, `admission`, `title`, `guarantee`, `routes`, `memberCount`, `members` and `staleMembers`. It also returns the `family_header_reference` body (`id`, `revision`, `title`) as the row's paging `reference`; every row of a family carries the family as its paging `group`.
  - **`member_reference`**: `id`, `revision`, `returnedUnder` (the family, or `seed`, it was first returned under), and `title` with `titleDerivedFrom: "statement"`.
  - **`advertised_family`**: `id`, `title` and `via`.
- **The derived title (`derived_title`, ruling Q1).** An invariant record has no title field, and none is added. The reference title is the statement's first sentence: text up to a `.`, `!` or `?` followed by whitespace or the end (so "2.1" does not end it), whitespace collapsed, at most `DERIVED_TITLE_LENGTH` = 80 characters, and a cut title ends in `…`.
- **Counts (`leaf_counts`, rule 8).** `families`, `members`, `entries`, `realizations`, `proofs`, `distinctPaths`, `invariantsByState` (`_by_state`), `advertisedFamilies`, `chainFamilies` (MIK-R05; present even when 0) and `rowsTotal`. The walk's `rowsReturned` and `rowsRemaining` are added per page by `pages.py`.
- **`family_names(index, invariant)`.** The live families containing an invariant, each by ID and title. The `invariant` view of `knowledge_read` uses it (rule 7).

### Conventions

- Ties are broken by stable ID everywhere: seeds, families, members, entries and frontier families.
- `LEAF_POLICY` = `family-complete-leaf`, `LEAF_POLICY_VERSION` = `v2`. **The version was bumped from `v1` by MIK-R05** (ruling Q4, 2026-09-30 03:32:18): the selection now includes chain rows, and a continuation binds the policy version, so a token minted under `v1` is refused `continuation_binding_mismatch` (review F2, 2026-09-30 04:12:49). The digest includes the policy, so every leaf manifest changed with the bump.

### Invariants And Boundaries

- **One family hop.** A member's other families are advertised, never expanded (MIK-R01 Exclusions).
- **A member already returned appears later only as a reference row** (candidate invariant; see the `application` overview).
- **The manifest depends on the selection and its order only**, never on a code tree or a surface.
- **Chain rows come after the MIK-R01 content, each family once** (MIK-R05 rules 4 and 5; candidate invariant, see the `application` overview).
- **Retired records are never selected**, listed, counted or placed in `currentness`.
- **No ranking and no writes.** The module only reads `ix_*` answers through `KnowledgeIndex` (`entries_at_path`, `invariant`, `family`, `record`); it does not change `INDEX_FORMAT`.

### Todos

- **Real data has no shared member and no frontier family.** On the converted real tree, no path's page has a `member_reference` or an `advertised_family` row, so the Q1 title and the N4 merge are exercised by fixtures only.
- **Real families have `routes: []`.** The conversion did not populate routes; the header carries whatever the record holds (MIK-R04 and MIK-R06 territory). Until routes are assigned, every real read's chain states `no_governing_family`; the MIK-R05 real-data evidence assigned routes in scratch only.

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

- The module statement: the selection, the declared row order, and the two steps that keep the manifest free of a code tree. [1]
- The policy name and its version `v2` (bumped by MIK-R05 for the chain rows), and the derived-title length. [2]
- The structure, with the chain and the family seed, and its manifest digest over the seed (a path or a family) and the ordered row identities only. [3]
- The selection with its route chain: `None` only for a path with no live entry and no governing family. [4]
- The family seed (MIK-R05 rule 3): one live family's full content, `None` when the tree holds no live family by that ID, built through the shared structure step. [5]
- Realization and proof entries at the path both seed the read (ruling Q3). [6]
- The live families of the seed, each with its live members only. [7]
- One frontier entry per family, with every member that reaches it (ruling N4). [8]
- Retired invariants and families are never selected. [9]
- The declared order: seed invariants, then each family header and its remaining members (seed invariants not repeated, earlier members as references), then the frontier, then the chain rows last. [10]
- The rendering at one code tree, and a read-wide reason stated once. [11]
- The reference row with its derived title and the section it was first returned under. [12]
- One renderer per row kind, the chain row's included. [13]
- The chain row's renderer (MIK-R05): the compact entry of the family the row names. [14]
- The derived title: the first sentence, at most 80 characters (ruling Q1). [15]
- The member, entry and header rows with their fields. [16]
- The counts of rule 8, with the chain families. [17]
- The family names of rule 7. [18]

### Cross-Repo References

No meaningful cross-repo references found: the selection reads one memory tree's derived index.

No cross-repo boundary is crossed by this file.
