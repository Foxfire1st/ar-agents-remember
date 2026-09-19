# mcp/src/agents_remember/memory/knowledge/facet_read.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/facet_read.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T00:25+02:00 |
| lastVerifiedCommitHash | `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate | 2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l11` uncommitted source; base `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The one entry point: seed dispatch, the bound it raises past, the declared order, the counts and the manifest.** | `select_facet_scope` | mcp/src/agents_remember/memory/knowledge/facet_read.py:109-129 |
| **The bound and the exception that carries both the count and the bound to the caller.** | `ITEM_LIMIT`; `FacetSelectionIncomplete` | mcp/src/agents_remember/memory/knowledge/facet_read.py:63-65; mcp/src/agents_remember/memory/knowledge/facet_read.py:68-82 |
| The query and the selection as frozen values, with `seed_recorded` as the fact the caller's absence answer rests on. | `FacetSelectionQuery`; `FacetSelection` | mcp/src/agents_remember/memory/knowledge/facet_read.py:85-91; mcp/src/agents_remember/memory/knowledge/facet_read.py:93-106 |
| **The facet-record aggregate: the record, every retained revision, every attachment and every touching edge.** | `_facet_record_items` | mcp/src/agents_remember/memory/knowledge/facet_read.py:132-155 |
| **The both-directions edge walk, deduplicated by the edge's own key.** | `_supersessions_of_record` | mcp/src/agents_remember/memory/knowledge/facet_read.py:158-172 |
| The explanation aggregate and the exact-statement-revision check that keeps the two subject kinds apart. | `_explanation_items`; `_subject_revision_recorded` | mcp/src/agents_remember/memory/knowledge/facet_read.py:175-193; mcp/src/agents_remember/memory/knowledge/facet_read.py:196-206 |
| **The counts derived from the item tuple, so a page cannot report a total its items do not add up to.** | `_counts` | mcp/src/agents_remember/memory/knowledge/facet_read.py:209-219 |
| **The manifest that seals the policy, the seed and the exact item identities.** | `_manifest_digest` | mcp/src/agents_remember/memory/knowledge/facet_read.py:222-236 |
| The read-only execution helpers and the ordered statement set that is the only SQL in the module. | `_one`; `_many`; `_RECORD_BY_ID`; `_ATTACHMENTS_OF_RECORD` | mcp/src/agents_remember/memory/knowledge/facet_read.py:239-248; mcp/src/agents_remember/memory/knowledge/facet_read.py:251-294 |
| The declared policy name, item limit and seed union this module executes. | `FACET_SELECTION_POLICY_VERSION`; `FACET_SELECTION_ITEM_LIMIT`; `FacetReadSeed` | mcp/src/agents_remember/models/knowledge/facet_read.py:56-56; mcp/src/agents_remember/models/knowledge/facet_read.py:61-61; mcp/src/agents_remember/models/knowledge/facet_read.py:182-185 |
| The declared item order and identity the manifest and the page both derive from. | `facet_item_sort_key`; `facet_item_id` | mcp/src/agents_remember/models/knowledge/facet_read.py:273-276; mcp/src/agents_remember/models/knowledge/facet_read.py:295-299 |
| The row codecs every item here is decoded through. | `decode_facet_record_row`; `decode_attachment_row`; `decode_supersession_row`; `decode_explanation_row` | mcp/src/agents_remember/memory/knowledge/facet_records.py:157-190; mcp/src/agents_remember/memory/knowledge/facet_records.py:374-396; mcp/src/agents_remember/memory/knowledge/facet_records.py:429-441; mcp/src/agents_remember/memory/knowledge/facet_records.py:567-585 |
| The application seam that converts the bound into the shipped refusal and owns the operation name. | `read_facet_scope` | mcp/src/agents_remember/application/knowledge_facets.py:71-121 |
| **The case that holds the exact page, the empty-but-real selection and the incompleteness refusal.** | "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact" | mcp/tests/test_knowledge_facets.py:1266-1266 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T15:12:32+00:00: Generated citation repair: "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact" repointed to mcp/tests/test_knowledge_facets.py:1266-1266. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact" repointed to mcp/tests/test_knowledge_facets.py:1246-1246. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact" repointed to mcp/tests/test_knowledge_facets.py:1208-1208. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T00:25+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): created this one-to-one card for the facet-specific selection. It records what each seed selects (including the **both-directions** supersession walk deduplicated by the edge's own key), the complete-or-refused bound with the exception carrying both count and bound to the operation that owns the refusal name, the "nothing is derived" rule (order by kind then stable identifiers, every retained revision served, only the stored designation matters), the counts and manifest derived from the same tuple the page is built from, the read-only handle that makes "a refusal leaves the file byte-identical" structural, and the non-overlap with `KS-R07@v1`'s selection that is the reason a shipped page is byte-identical. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
