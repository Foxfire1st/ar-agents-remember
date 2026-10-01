# mcp/src/agents_remember/memory/knowledge/facet_read.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The facet-specific selection: one seed, one complete aggregate, or one typed refusal.** This module
executes the facet read over one snapshot: it resolves the seed, walks the aggregate it names, counts what
it selected, and seals the result into a manifest digest.

It is a **separate** selection rather than an extension of `KS-R07@v1`'s recorded-scope selection, and that
separation is the module's reason for existing: nothing here calls into the shipped selection, and the
shipped selection calls into nothing here, so a shipped seed's serialized page is byte-identical to what it
was before this leaf **because no code path is shared** rather than because a guard prevents an addition.
Its own declared policy name (`authored-judgment-facets/v1`), its own two seed kinds, its own six item kinds
and its own counts live in `models/knowledge/facet_read.py`; this module executes them.

## Code Commentary

### Logic

- **What a seed selects.** A `FacetRecordSeed` selects that record, every retained revision of it, every
  attachment row of those revisions, and every recorded supersession edge that touches any of them — **in
  both directions**, so a decision's page reports what it supersedes and what supersedes it. An
  `ExplanationSubjectSeed` selects every explanation whose subject is that exact statement revision, plus
  every retained revision of those explanations. `_facet_record_items` and `_explanation_items` each return
  `(recorded, items)`, so the caller can tell "this seed names something" from "here are the rows".
- **Complete or refused.** `select_facet_scope` raises `FacetSelectionIncomplete` when the enumerated
  aggregate exceeds `ITEM_LIMIT` (the declared `FACET_SELECTION_ITEM_LIMIT`), rather than emitting a partial
  page with a total that was never computed. The exception carries both the count and the bound, and the
  caller — the read operation, which owns the operation name a refusal is reported under — converts it into
  the shipped `selection_incomplete` refusal. There is no cursor, so there is no continuation contract to
  bind and no position that could be read as a different selection.
- **Nothing is derived.** An item's order is fixed by its kind and then by stable identifiers
  (`facet_item_sort_key`), never by an authored label, an insertion order or a timestamp; every retained
  revision is served as its own item; and the only statement about which explanation revision matters is
  the designation the explanation record stores. No field here could be read as "newest", and no
  endorsement, confidence, severity or score is computed or served.
- **The counts and the manifest come from the same tuple the page is built from.** `_counts` counts the
  ordered items by kind, and `_manifest_digest` seals the declared policy version, the seed's own JSON
  rendering and each item's `(kind, item_id)` pair — so a manifest that does not describe the items cannot
  be produced here, and "a position in one selection" stays a checkable fact.
- **The two absences a caller can tell apart are the shipped ones.** A seed naming nothing recorded reports
  `recorded=False` and the caller answers `selector_absent`, while a recorded facet record with no
  attachments or no supersession edges is a real page reporting zero counts for those kinds. The subject
  side checks the exact statement revision against its own canonical table
  (`_subject_revision_recorded`), so a family subject is never satisfied by an invariant revision.
- **Every statement is a `SELECT` on the caller's read-only handle.** `_one` and `_many` are the only two
  execution helpers, each statement below them is a module constant, and each is ordered by the item's own
  stable identifier rather than left to the storage engine — because the page's declared order is a property
  of this selection and not of how SQLite happened to answer. Supersession rows are deduplicated by the
  edge's own key (`_supersessions_of_record`), because one edge can touch a record from both sides.

### Conventions

- **The query and the selection are frozen dataclasses.** `FacetSelectionQuery` carries the namespace and
  the seed; `FacetSelection` carries the ordered items, the counts, the manifest digest and the
  `seed_recorded` fact, plus an `empty` property. The caller builds the result from the selection rather
  than re-deriving any part of it.
- **The bound is named beside the reason** (`ITEM_LIMIT = FACET_SELECTION_ITEM_LIMIT`), so a refusal can
  say which bound it reached without restating the number.
- **The module returns values, not refusals, except for the bound.** `select_facet_scope` has exactly one
  failure mode and it is raised rather than returned, because the operation name belongs to the caller.
- **The public surface is five names** (`ITEM_LIMIT`, `FacetSelection`, `FacetSelectionIncomplete`,
  `FacetSelectionQuery`, `select_facet_scope`).

### Invariants And Boundaries

- **A refusal leaves the file byte-identical, structurally.** The connection is the caller's read-only
  handle and every statement here is a `SELECT`, so there is no statement that could change the file.
- **The shipped selection is untouched.** This module does not import the recorded-scope read, does not
  reuse its policy name, and adds no item to its item union; the byte identity of a shipped page is a
  consequence of that non-overlap.
- **The page is not paged.** There is no limit/offset, no cursor and no `has_more`; a selection that does
  not fit whole is refused, which is why the aggregate limit is described as an execution bound rather than
  a page size.
- **Boundary.** This module does not declare the item, seed, count or policy shapes
  (`models/knowledge/facet_read.py` does), does not convert a row into a value (`facet_records.py` does),
  does not verify the snapshot it is handed (the application seam does), and writes nothing at all — the
  write path is `facets.py`.

### Todos

None recorded. A cursor for a selection that does not fit is deliberately not planned: the declared
contract is complete-or-refused, and a continuation surface would be a second declared policy.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The one entry point: seed dispatch, the bound it raises past, the declared order, the counts and the manifest.** [1]
- **The bound and the exception that carries both the count and the bound to the caller.** [2]
- The query and the selection as frozen values, with `seed_recorded` as the fact the caller's absence answer rests on. [3]
- **The facet-record aggregate: the record, every retained revision, every attachment and every touching edge.** [4]
- **The both-directions edge walk, deduplicated by the edge's own key.** [5]
- The explanation aggregate and the exact-statement-revision check that keeps the two subject kinds apart. [6]
- **The counts derived from the item tuple, so a page cannot report a total its items do not add up to.** [7]
- **The manifest that seals the policy, the seed and the exact item identities.** [8]
- The read-only execution helpers and the ordered statement set that is the only SQL in the module. [9]
- The declared policy name, item limit and seed union this module executes. [10]
- The declared item order and identity the manifest and the page both derive from. [11]
- The row codecs every item here is decoded through. [12]
- The application seam that converts the bound into the shipped refusal and owns the operation name. [13]
- **The case that holds the exact page, the empty-but-real selection and the incompleteness refusal.** [14]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
