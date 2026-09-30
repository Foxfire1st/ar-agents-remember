# mcp/src/agents_remember/application/knowledge_leaf/selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_leaf/selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T02:10:00+02:00 |
| lastVerifiedCommitHash | `3772cdcd008fcacdc5a86e264a3ef63e879ea544`|
| lastVerifiedCommitDate | 2026-09-30T02:36:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**What one seed path selects, in which order, and the rows at a code tree (MIK-R01 rules 1 to 5, 7 and 8).** From the derived index of one memory tree (MIK-R23) it selects the entries at the path (realization *and* proof entries), their invariants, every family containing those invariants with its guarantee, routes and members, and every member's entries. Traversal is one family hop; a member's other families are advertised, never expanded.

## Code Commentary

### Logic

- **Two steps, so the manifest never depends on a code tree.**
  - `select_leaf(index, path)` reads the structure, a `LeafStructure`: the seed invariants, the families, the members, the advertised frontier, the family titles and `order`, the row identities as `(kind, subject, group)` triples. It returns `None` when no live entry is recorded at the path.
  - `leaf_rows(structure, currentness)` renders that structure as `PageRow` values, each entry and invariant stated at the walk's code tree (MIK-R03).
  - `LeafStructure.manifest_digest` is the `sha256_digest` of the policy label, the seed path and the ordered row identities only. That is why both surfaces agree on it even when their code trees differ (ruling Q4, 2026-09-29 23:21:57: conformance is the equal manifest digest, and entry states follow each surface's code tree).
- **The seed (`_seed_invariants`).** The live invariants of every realization and proof entry at the path, by ID. Proof entries seed the read (ruling Q3); the older scope read seeded on realizations only.
- **The families (`_families_of`).** The live families containing a seed invariant, each keeping only its live members. `_member` reads each invariant once per selection and keeps only live families; `_family` and `_live` reject a retired record, so a retired invariant or family is never selected, listed or counted (MIK-R23 ruling Q4).
- **The frontier (`_advertised`).** Each family a selected member belongs to outside the selection, **once**, with every selected member that reaches it, sorted (ruling N4, 2026-09-30 00:08:39). Its manifest identity is `("advertised_family", family, None)`.
- **The declared order (`_order`, rule 4).**
  1. The seed's own invariants, by ID: each a `member` row followed by its entry rows (`_ordered`: realizations, then proofs, each by path then entry ID).
  2. Each family, by ID: a `family_header` row, then its remaining members by ID. A seed invariant is listed in the header's `members` and **not repeated** (ruling Q2). A member already returned under an earlier family becomes a `member_reference` row (rule 5).
  3. One `advertised_family` row per frontier family.
- **Rendering (`_Rendering`, `_RENDERERS`).** One renderer per row kind: `_render_member`, `_render_entry` (realizations and proofs), `_render_header`, `_render_reference` and `_render_advertised`. The dispatch table and the helper extractions keep every function at or below 10 under radon (ruling N1).
  - **`member`** (`_member_row`): `id`, `revision`, `status`, `admission`, `statement`, `applicability`, `conditions`, `exclusions`, `state` and `families`, every live family containing it, selected or advertised (rule 7).
  - **`realization` / `proof`** (`_entry_row`): `id`, `invariant`, `path`, `locator`, `role` or `facet`, `state`, and `reason` when the entry is not current. `_observed` drops a read-wide reason (no code tree was requested), which the `currentness` block states once.
  - **`family_header`** (`_header_row`): `id`, `revision`, `status`, `admission`, `title`, `guarantee`, `routes`, `memberCount`, `members` and `staleMembers`. It also returns the `family_header_reference` body (`id`, `revision`, `title`) as the row's paging `reference`; every row of a family carries the family as its paging `group`.
  - **`member_reference`**: `id`, `revision`, `returnedUnder` (the family, or `seed`, it was first returned under), and `title` with `titleDerivedFrom: "statement"`.
  - **`advertised_family`**: `id`, `title` and `via`.
- **The derived title (`derived_title`, ruling Q1).** An invariant record has no title field, and none is added. The reference title is the statement's first sentence: text up to a `.`, `!` or `?` followed by whitespace or the end (so "2.1" does not end it), whitespace collapsed, at most `DERIVED_TITLE_LENGTH` = 80 characters, and a cut title ends in `…`.
- **Counts (`leaf_counts`, rule 8).** `families`, `members`, `entries`, `realizations`, `proofs`, `distinctPaths`, `invariantsByState` (`_by_state`), `advertisedFamilies` and `rowsTotal`. The walk's `rowsReturned` and `rowsRemaining` are added per page by `pages.py`.
- **`family_names(index, invariant)`.** The live families containing an invariant, each by ID and title. The `invariant` view of `knowledge_read` uses it (rule 7).

### Conventions

- Ties are broken by stable ID everywhere: seeds, families, members, entries and frontier families.
- `LEAF_POLICY` = `family-complete-leaf`, `LEAF_POLICY_VERSION` = `v1`.

### Invariants And Boundaries

- **One family hop.** A member's other families are advertised, never expanded (MIK-R01 Exclusions).
- **A member already returned appears later only as a reference row** (candidate invariant; see the `application` overview).
- **The manifest depends on the selection and its order only**, never on a code tree or a surface.
- **Retired records are never selected**, listed, counted or placed in `currentness`.
- **No ranking and no writes.** The module only reads `ix_*` answers through `KnowledgeIndex` (`entries_at_path`, `invariant`, `family`, `record`); it does not change `INDEX_FORMAT`.

### Todos

- **Real data has no shared member and no frontier family.** On the converted real tree, no path's page has a `member_reference` or an `advertised_family` row, so the Q1 title and the N4 merge are exercised by fixtures only.
- **Real families have `routes: []`.** The conversion did not populate routes; the header carries whatever the record holds (MIK-R04 and MIK-R06 territory).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R01@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`01_family-complete-leaf-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module statement: the selection, the declared row order, and the two steps that keep the manifest free of a code tree. | "The family-complete leaf read's selection and its ordered rows" | mcp/src/agents_remember/application/knowledge_leaf/selection.py:1-31 |
| The policy name and version, and the derived-title length. | `LEAF_POLICY`; `LEAF_POLICY_VERSION`; `DERIVED_TITLE_LENGTH` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:62-68 |
| The structure and its manifest digest over the ordered row identities only. | `LeafStructure`; `manifest_digest` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:89-119 |
| The selection: `None` for a path with no live entry, otherwise the seed, its families, the frontier and the order. | `select_leaf` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:122-143 |
| Realization and proof entries at the path both seed the read (ruling Q3). | `_seed_invariants` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:146-153 |
| The live families of the seed, each with its live members only. | `_families_of` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:156-170 |
| One frontier entry per family, with every member that reaches it (ruling N4). | `_advertised` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:173-183 |
| Retired invariants and families are never selected. | `_member`; `_family`; `_live` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:186-211 |
| The declared order: seed invariants, then each family header and its remaining members (seed invariants not repeated, earlier members as references), then the frontier. | `_order`; `_ordered` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:220-252 |
| The rendering at one code tree, and a read-wide reason stated once. | `leaf_rows`; `_observed` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:271-293 |
| The reference row with its derived title and the section it was first returned under. | `_render_reference` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:310-322 |
| One renderer per row kind. | `_RENDERERS` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:336-343 |
| The derived title: the first sentence, at most 80 characters (ruling Q1). | `derived_title` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:346-355 |
| The member, entry and header rows with their fields. | `_member_row`; `_entry_row`; `_header_row` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:358-426 |
| The counts of rule 8. | `leaf_counts`; `_by_state` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:429-451 |
| The family names of rule 7. | `family_names` | mcp/src/agents_remember/application/knowledge_leaf/selection.py:454-460 |

## Cross-Repo References

No meaningful cross-repo references found: the selection reads one memory tree's derived index.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): created this card for the new file MIK-R01 adds. It records the architect rulings of 2026-09-29 23:21:57 (Q1 the derived reference title, Q2 seed invariants not repeated, Q3 proof entries seed the read, Q4 conformance by the manifest digest) and 2026-09-30 00:08:39 (N1 radon at or below 10, N4 one advertised row per family with `via`). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
