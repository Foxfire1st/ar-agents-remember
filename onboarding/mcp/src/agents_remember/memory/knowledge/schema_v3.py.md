# mcp/src/agents_remember/memory/knowledge/schema_v3.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/schema_v3.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T00:25+02:00 |
| lastVerifiedCommitHash | `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be`|
| lastVerifiedCommitDate | 2026-09-18T08:36:40+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Generation 3's appended tables, as pinned data.** Four tables — `facet_attachment`,
`facet_decision_supersession`, `explanation` and `explanation_revision` — with their column orders, key
tuples, typed-JSON column sets, DDL, eleven indexes and seven immutability triggers.

This module owns **only what generation 3 appends**. Generation 1's ten tables stay declared verbatim in
`schema.py` and generation 2's six in `schema_v2.py`; nothing here redeclares, reorders, renames, retypes
or drops one of them, and no `ALTER TABLE` against an earlier generation's table appears anywhere in the
package. That is why the leaf's whole contribution to the record envelope is **four appended tables**
rather than a column added to `knowledge_record`: appending a column would change a table generation 2's
record must keep declaring, and the additive rule is a property of the generation record rather than a
convention.

## Code Commentary

### Logic

The module is pure data: it defines **no functions and no classes**. Its whole surface is seven module
constants, and each is a member of the generation record `schema_generations.GENERATION_3` composes:

- `APPENDED_TABLES` — the ordered tuple `("facet_attachment", "facet_decision_supersession",
  "explanation", "explanation_revision")`. The order is load-bearing: it is the order the encoder
  serializes them in, and it is appended after generation 2's sixteen so generation 3's manifest **begins
  with** generation 2's, unchanged.
- `APPENDED_COLUMNS`, `APPENDED_PRIMARY_KEYS`, `APPENDED_JSON_COLUMNS` — the per-table declared column
  order, key tuple and typed-JSON set the encoder orders and decodes rows through. Every new
  `provenance` column is a typed-JSON column; `body` and `payload_digest` are not, because an explanation
  body is authored prose rather than structured data and its digest is a single hex string.
- `APPENDED_TABLE_DDL` — one `CREATE TABLE` per appended table.
- `APPENDED_INDEX_DDL` — eleven indexes, each covering the reverse direction of a declared lookup.
- `APPENDED_TRIGGERS` — seven immutability triggers.
- `APPENDED_FEATURES` — the **empty** tuple, declared rather than omitted so the composition states the
  same fact generation 2's does: generation 3 needs no SQLite feature generation 2 does not already
  require, and a reader should not have to infer "no new feature" from an absence.

Why the tables are shaped this way:

- **`facet_attachment` is one row per authored attachment naming one *exact* endpoint.** Endpoint-kind
  compatibility is structural rather than polymorphic: there is one foreign-key column per endpoint kind
  (`invariant_revision_id`, `family_revision_id`, `anchor_id`, `claim_id`), a `CHECK` that the populated
  group matches the stored `endpoint_kind` and that the other groups are `NULL`, and a real foreign key per
  group. The forbidden shape — `(facet_revision_id, endpoint_kind, endpoint_id)`, where a misspelled kind,
  a dangling id and a wrong-kind target all store successfully — **is not expressible here**, because
  there is no `endpoint_id` column for an unchecked identity to land in. The module has **no delete
  trigger** on this table, and that absence is deliberate: removal is an explicit deletion of that
  attachment row and nothing else, so the trigger refuses an in-place repoint instead.
- **`facet_decision_supersession` is the shipped predecessor idiom over the decision record kind**:
  composite foreign keys to both exact revision endpoints, `CHECK (superseding_revision_id <>
  superseded_revision_id)`, and the superseding revision as the key's leading column. There is **no
  update trigger and no delete trigger exception** — both refuse, because a recorded edge is a fact:
  superseding a decision adds an edge row and changes nothing about the superseded revision.
- **`explanation` is the separable record, and its subject is expressed the same structural way the
  attachment's endpoint is, with one addition.** The subject's *identity* is part of the checked group
  too, so the foreign key is the three-column `(repository_id, identity, revision_id)` reference both
  revision tables already declare a `UNIQUE` key for. That makes "this revision really is a revision of
  the statement identity it claims" a constraint of the table rather than a check the write path
  remembers, and it means the stored row reproduces the whole subject without a denormalised copy that
  could disagree with the revision table. `current_revision_id` is the **recorded designation**, and it is
  the one mutable field of this row — which is why there is **no whole-row update trigger** here: the
  `explanation_no_rebind` trigger names every other column, so the guard is authored rather than inferred.
- **`explanation_revision` is the append-only body table.** `predecessor_revision_id` makes an edit a
  successor naming its exact predecessor, and the trigger set refuses an in-place rewrite or a delete of a
  sealed revision.
- **The two tables reference each other** (`explanation.current_revision_id` → `explanation_revision` and
  `explanation_revision.explanation_id` → `explanation`), which is exactly what `NO ACTION … DEFERRABLE
  INITIALLY DEFERRED` is for: one transaction may insert the record, its first revision and its
  designation without depending on statement order.

### Conventions

- Every table is `STRICT`, every primary-key column is declared `NOT NULL` explicitly, and every foreign
  key is composite and `DEFERRABLE INITIALLY DEFERRED`, exactly as the sixteen shipped tables are.
- Trigger messages share the shipped `immutable_revision:` prefix so `map_sqlite_error` steers a
  trigger-originated error to that code. The seven triggers refuse: repointing an attachment
  (`facet_attachment_no_repoint`, covering every column except the key and `attachment_id`), updating or
  deleting a recorded supersession edge (`facet_decision_supersession_no_update`,
  `facet_decision_supersession_no_delete`), rebinding an explanation's subject
  (`explanation_no_rebind`), deleting an explanation record (`explanation_no_delete`), and rewriting or
  deleting a sealed explanation revision (`explanation_revision_no_rewrite`,
  `explanation_revision_no_delete`).
- Index names are a local choice, not contract; each covers the reverse direction of a lookup the package
  performs — one per endpoint kind on the attachment, one for the superseded side of the edge, the two
  subject groups and the designation on `explanation`, and the owning explanation and predecessor on
  `explanation_revision`.

### Invariants And Boundaries

- **No facet record carries a content address, a logical digest or a fingerprint column, and none is added
  here.** A facet's revision digest is `record_revision.content_digest`, on the sealed revision aggregate
  that owns it; the envelope stays free of any identity-valued column.
- **Additive-only, structurally.** `GENERATION_3.tables[: len(GENERATION_2.tables)] == GENERATION_2.tables`
  and generation 3's columns for each of the first sixteen names are generation 2's. That prefix equality
  is the whole of the additive rule.
- **Immutability is enforced by the database, not only by the operation.** These triggers exist so a
  changeset, a repair script or a future code path that forgot the rule still cannot rewrite a sealed
  revision, rebind a subject or delete a recorded edge. The operations' own preconditions exist to return
  a typed refusal; the triggers exist so that forgetting them still cannot corrupt the record.
- **Boundary.** This module declares structure and nothing else: it writes no rows, performs no
  validation, returns no refusal, and owns no behaviour. Authoring a facet is `facets.py`; converting a
  row is `facet_records.py`; deciding which generation a dataset is, is `schema_generations.py`.
- **Not admissible, recorded so it is not re-proposed:** an `endpoint_id` column (it would restore the
  polymorphic shape the per-kind groups exist to make unrepresentable), and a whole-row update trigger on
  `explanation` (it would forbid the one mutable field the designation is).

### Todos

None recorded. The generation's own fingerprint is computed by composition in `schema_generations.py`
rather than recorded here, and the recorded detail that this leaf measured is the composed generation-3
fingerprint `01161417a87618c824dba9e6f2add26b2ba8f84797cfc35b7cc9c841177a1f20`, read from the registry —
durable in `facet_test_support.py` and the leaf's worker report rather than in a constant here.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The ordered appended-table tuple whose prefix rule makes generation 3's manifest begin with generation 2's sixteen tables. | `APPENDED_TABLES` | mcp/src/agents_remember/memory/knowledge/schema_v3.py:53-58 |
| The declared column order, key tuple and typed-JSON set per appended table — the encoder's ordering and decoding inputs. | `APPENDED_COLUMNS`; `APPENDED_PRIMARY_KEYS`; `APPENDED_JSON_COLUMNS` | mcp/src/agents_remember/memory/knowledge/schema_v3.py:60-101; mcp/src/agents_remember/memory/knowledge/schema_v3.py:103-112; mcp/src/agents_remember/memory/knowledge/schema_v3.py:118-123 |
| **The four `STRICT` `CREATE TABLE` statements: the per-kind endpoint groups and their `CHECK`, the supersession edge and its `CHECK`, and the explanation pair's checked subject group and recorded designation.** | `APPENDED_TABLE_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v3.py:125-239 |
| The eleven reverse-direction indexes, one per declared lookup direction. | `APPENDED_INDEX_DDL` | mcp/src/agents_remember/memory/knowledge/schema_v3.py:243-263 |
| **The seven immutability triggers, with the two deliberate absences stated in the comment above them.** | `APPENDED_TRIGGERS`; "immutable_revision: an attachment cannot be repointed in place" | mcp/src/agents_remember/memory/knowledge/schema_v3.py:265-312 |
| **The declared-but-empty feature tuple, so "no new SQLite feature" is stated rather than inferred.** | `APPENDED_FEATURES` | mcp/src/agents_remember/memory/knowledge/schema_v3.py:314-319 |
| The generation record this module's data is composed into, and the append that keeps generation 2's prefix intact. | `GENERATION_3`; `_compose_generation_3` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:287-295; mcp/src/agents_remember/memory/knowledge/schema_generations.py:298-298 |
| **The registry, ordered oldest first and now holding five generations — re-read by hand after `KS-R18@v1` appended generation 5, so "the newest supported generation" is generation 5 rather than generation 4.** | `GENERATIONS` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:365-372 |
| The generation-2 tables this module appends after and never touches. | `APPENDED_TABLES` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:42-49 |
| The write path that inserts these rows, and the row codecs that populate the checked groups. | `apply_add_facet`; `attachment_endpoint_columns` | mcp/src/agents_remember/memory/knowledge/facets.py:218-272; mcp/src/agents_remember/memory/knowledge/facet_records.py:277-301 |
| **The case that measures the additive rule, the append order, the `STRICT` shape and the two deliberate trigger absences.** | "test_the_registered_generation_appends_only_and_the_preceding_ones_are_unchanged" | mcp/tests/test_knowledge_facets.py:888-932 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T08:30+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 2 generated projection bullet(s) by hand** — `GENERATIONS`, `_compose_generation_3`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): **re-read the registry claim against the construct as it now stands, and corrected the number it states as a fact.** `GENERATIONS` held four members when this card was last verified and holds **five** now, because `KS-R18@v1` appends generation 5 (`ar-knowledge-sqlite/v5`); `CURRENT_GENERATION = GENERATIONS[-1]` is what makes a *created* store declare version 5 while an existing generation-4 dataset keeps declaring 4. The wording was corrected rather than softened — the row now names generation 5 as "the newest supported generation" — and its range is an agent's read of the declaration's own lines (`:299-305`) rather than a projected one. No other row of this card was changed. Verification metadata advances to the leaf's base commit `e963a01c` because the claim was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T05:15+02:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): **re-read the registry claim, corrected its wording, and re-cited it by hand — replacing a generated projection whose range had been rewritten mechanically.** The construct genuinely changed: `GENERATIONS` held three members when this card was verified and holds **four** now, because `KS-R14@v1` appended generation 4 (`ar-knowledge-sqlite/v4`), and `CURRENT_GENERATION = GENERATIONS[-1]` is what makes a *created* store declare version 4 while a generation-3 dataset keeps declaring 3. The row's words are retained and sharpened rather than softened — "the newest supported generation" is now named as generation 4 — and its range (`:264-269`) is an agent's read of the declaration, not a projected one. **The generated bullet that produced the previous range was removed**, because a mechanically projected range is unverified evidence. No other row of this card was re-read in this pass, and no other row of it was changed. Verification metadata is **not** advanced over unreviewed content: this card's stamp stays where the L11 curator left it.
- 2026-09-18T00:25+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): created this one-to-one card for generation 3's appended tables. It records the four-table append order that makes generation 3's manifest begin with generation 2's sixteen, the **per-kind foreign-key groups plus their `CHECK`** that make the forbidden polymorphic endpoint shape unrepresentable (there is no `endpoint_id` column for an unchecked identity to land in), the three-column subject reference that makes "this revision is a revision of the identity it claims" a table constraint, `current_revision_id` as the one mutable field with the rebind trigger naming every other column, the mutual reference between the explanation pair that `DEFERRABLE INITIALLY DEFERRED` exists for, and the two **deliberate trigger absences** (no delete trigger on the attachment, no whole-row update trigger on the explanation) recorded with their reasons so neither is re-proposed. It also records the declared-but-empty feature tuple, the eleven indexes, the seven triggers with their shared `immutable_revision:` prefix, and the composed generation-3 fingerprint as a measured value carried in the leaf's test support rather than as a constant here. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
