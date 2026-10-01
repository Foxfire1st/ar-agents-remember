# mcp/tests/test_knowledge_facets.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

**The authored-judgment vocabulary's 17 cases, in the order the requirement states its clauses.** Every case
protects one clause group: the closed subtype vocabulary and its payload seam, authorship and lifecycle as
stored data, the typed attachment contract, the decision's supersession edge, the independently editable
explanation, the candidate write path, the registered generation, and the read projection beside the shipped
selection. The module is `unit-regression` (row `mcp/tests/test-evidence-lanes.toml:73`) and is hermetic:
temporary directories, in-process APSW databases built through the production application seam, and one
recorded generation-2 fixture.

**Two of its cases were re-scoped by `KS-R14@v1`, and both keep their protected property.** Appending
generation 4 falsified exactly two assertions here — the two that spelled the *shared* substrate's membership
as a closed list this leaf legitimately grew — and each gained the replacement fact rather than being deleted,
skipped or xfailed. Both carry a `RE-SCOPED for KS-R14@v1` paragraph in the case docstring, and the Logic
section below states what each one now asserts.

Two properties are load-bearing enough that the module docstring names them before the cases:

- **The payload seam is the only payload decision point.** An unknown subtype, an undeclared field, a
  missing meaning and a payload that carries its own provenance are all the same shipped `invalid_payload`
  refusal, and every one of them leaves the dataset byte-identical (the cases assert the table counts).
- **Nothing here is derived.** An attachment's endpoint, a record's governing route, a supersession edge and
  an explanation's designation are stored facts with an operation behind them, and the cases assert that the
  absent state is reported as absent rather than defaulted.

**The case ceiling is why a case carries a loop rather than a parametrization.** The unit population's
declared budget had twenty slots left when this leaf landed and the repository's own record forbids a KS leaf
from raising it, so the per-subtype and per-endpoint-kind variants are driven *inside* the case that owns
their property, with every assertion naming the subtype or kind it is about. The module states the cost — no
independent failure attribution between variants of one property — and what it preserves: every clause, and a
population that runs at all, since an over-budget population raises `UsageError` and executes zero tests.

## Code Commentary

### Logic

- **The vocabulary's closure is asserted three ways** in `test_the_seam_registry_is_exactly_the_eight_declared_subtypes`:
  the payload union's member literals equal `FACET_KINDS`; `FACET_RECORD_SCHEMAS` and the seam's
  `FACET_RECORD_KINDS` have the same key set; and `KIND_SCHEMAS` is exactly the eight kinds plus the
  marked-internal conformance kind. **RE-SCOPED for `KS-R14@v1`:** the registry this asserts against is the
  *shared* envelope seam, and `KS-R10@v1`'s own docstring named the concrete non-facet categories as later
  leaves; `KS-R14@v1` registers the mechanical-detection pair through it. The case therefore states the
  three groups the registry now declares — the internal conformance kind, the eight facet kinds and
  `DETECTION_RECORD_KINDS` — and states the facet half **more precisely than before** by asserting
  `KIND_SCHEMAS[kind] == {FACET_RECORD_SCHEMAS[kind]}` for each of the eight, so the facet kinds' admissible
  schemas are still exactly their declared ones. **`260915-KS-L21` re-scoped it once more:** the tuple of
  groups the case unions gained the census group's own derived set `CENSUS_RECORD_KINDS`
  (`mcp/tests/test_knowledge_facets.py:291`), imported from `agents_remember.models.knowledge.census`
  (`:80-83`), so the subset, pairwise-disjointness and partition assertions the case already made now cover
  the census group without an edit here — a fourth census kind is answered by the census's own vocabulary
  rather than by a literal. The facet half is untouched: `len(FACET_KINDS) == 8` and the per-kind schema pin
  are asserted before the membership line. The same case checks the per-kind model's `extra`/`frozen` config, that
  `PAYLOAD_MODELS[(kind, schema)]` is that model, the derived envelope row's `record_schema`
  (`facet-decision/v1`), the two subject kinds, the two seed models, and the six writable tables.
- **The per-subtype walk** in `test_every_subtype_refuses_a_bad_shape_a_missing_meaning_and_its_own_provenance`
  drives all eight kinds through the seam: a valid payload validates and reports its own `facet_kind`; an
  undeclared field, a dropped required meaning (naming which field was dropped), each of the three
  provenance-shaped substitutions (`actor_ref`, `authorization_ref`, `recorded_at`) and an over-length prose
  field are all `invalid_payload`; no subtype carries an assessment, verdict, endorsement, confidence,
  severity or score field; and the ninth subtype is refused with its observed value and the joined expected
  kind list.
- **Authorship and lifecycle are stored data.** The receipt case asserts the model's own field set
  (`state`, `repository_id`, `written`, `refusal`) and the absence of seven verdict-shaped names, then reads
  the stored record back: `lifecycle == "proposed"`, the namespace's `authority_home`, the payload's
  `decider` **different from** the revision's `provenance.actor_ref`, the same `operation_id` the admission
  assigned, and a serialized page in which none of the words approval, endorsement, confidence, severity,
  score or latest appears.
- **Both entry points refuse accepted origin data** in
  `test_accepted_origin_data_is_refused_at_both_entry_points`, each with `promotion_not_supported`, and the
  batch reports `before == after` beside the unchanged table counts.
- **The attachment contract is walked in both directions.** The endpoint case attaches all four kinds and
  reads each endpoint back identically, then asserts the generation-3 column set (`endpoint_id` absent, the
  four identity columns present), that the DDL spells a checked group per kind, that it carries exactly six
  deferred foreign keys, and that an inconsistent two-column insert is refused by the database. The same case
  then refuses a missing target of each kind with `invalid_reference`, the orphan's id as `record_id` and the
  per-kind noun as `expected`, with the table counts unchanged.
- **The removal case names its row and proves the blast radius is one row**: a stale digest is
  `stale_precondition` with the stored digest still readable, and the successful removal reports
  `state="removed"` while the named invariant revision, the facet revision and the record envelope all
  remain.
- **The ungoverned and unattached states are explicit.** The route case reads a facet with no attachments as
  a two-item page with `governing_route_id is None`, authors a real route, reads a governed facet back with
  the route id, refuses a dangling route id with `missing_expected_row`, and asserts no `facet_route` table
  exists while `governing_route_id` stays a generation-2 column.
- **The supersession pair.** The forwarding case asserts `DecisionPayload`'s exact four fields, takes the
  three digests (record, revision, attachment) before superseding, and asserts all three are unchanged
  afterwards while the superseded record's page reports the edge and the superseding record's page reports
  three items. The cycle case drives a three-command batch around a cycle, asserts `lineage_cycle` with the
  edge table named and all three revisions in `observed`, asserts the table counts are unchanged, and then
  refuses a non-decision target with `invalid_reference` / `decision revision`. It also asserts the database
  refuses a rewrite of the sealed revision, a delete of it, a delete of the edge and a delete of the
  envelope — all four `apsw.Error`, three of them matching `immutable_revision`.
- **The explanation case is the leaf's strongest single act.** It takes the explained statement's
  `payload_digest` and the invariant's `row_digest` before authoring, authors an explanation, adds a
  successor, refuses a stale designation with `stale_precondition` and a foreign revision with
  `invalid_reference`, then designates the **first** revision even though a successor exists and asserts the
  page reports that stored designation. The statement's `payload_digest`, `statement` and `conditions` and
  the invariant's `row_digest` are all identical afterwards; the page carries both explanation revisions and
  the words latest/newest appear nowhere in its serialization; a family subject of another identity is
  refused with `invalid_reference` and the family revision as `record_id`; and `explanation` is not a column
  of generation 1's `invariant_revision`.
- **The union and dispatch case measures the widening**: the command kinds are exactly the declared groups
  and no count — `SHIPPED_COMMAND_KINDS` unioned with each record group's own derived set, which
  `260915-KS-L21` extended with the census group's `CENSUS_COMMAND_KINDS`
  (`mcp/tests/test_knowledge_facets.py:953`), `_TARGET_CHECKS` covers every kind, `_STEPS` is exactly the
  six facet kinds, and `MutableRecordTable`'s literal is the shipped seven unioned with every group's
  declared table set, the census group's `CENSUS_WRITABLE_TABLES` (`:981`) included. The exact-total form
  this case carried before `KS-R17@v1` ("the twelve shipped plus the six facet kinds (18)") is
  **superseded and retained as history**: an exact count cannot catch a kind added to one group but not to
  the dispatch table, and the set equality still does — a census command missing from the union, from
  `_TARGET_CHECKS` or from its own step table fails this case.
- **The two-entry-points case** drives a standalone write and a batch write, asserts the batch receipt's two
  touched tables in order, refuses a batch whose second command is inadmissible with `before == after` and
  unchanged counts, refuses a command presented to another operation's entry point with
  `expected`/`observed` `("add_facet", "attach_facet")`, and refuses a stale batch expectation over a stored
  facet revision with `stale_precondition`.
- **The generation case measures the registry rather than asserting it**, and **`KS-R14@v1` re-scoped it**:
  the two assertions that spelled the registry's membership as a closed list of three are replaced by the fact
  they were standing in for, so the case now asserts versions `[1, 2, 3, 4]` with the four schema names,
  `GENERATION_3` still a member at `user_version == 3`, and `CURRENT_GENERATION is GENERATIONS[-1]` — i.e. the
  created generation is named as "the newest registered one" rather than pinned to a literal the next
  generation would falsify. Generation 1's fingerprint is still asserted equal to its constant, generation 2's
  to the **pre-leaf** constant, generation 2 at sixteen tables, generation 3's table prefix equal to
  generation 2's with equal columns and keys per name, the appended four in order, no `ALTER TABLE` in any
  generation's statements, every appended DDL `STRICT` and without `ON DELETE CASCADE` and with its key
  columns `NOT NULL`, and `explanation_no_rebind` naming everything except `current_revision_id` — every
  generation-3-specific assertion is unchanged.
- **The predating-dataset case** builds a genuine version-2 dataset, refuses a facet write with
  `unsupported_schema` and expected/observed `"3"`/`"2"`, asserts the same facts through
  `require_facet_generation`, asserts a shipped generation-1-table write still works in that dataset, and
  asserts the file still reports generation 2.
- **The two read cases measure both directions.** The byte-identity case builds the recorded fixture, asserts
  its logical digest equals the pre-leaf constant, drives the shipped read and compares the serialized page
  and the whole result against the pre-leaf digests with the item count, `MAX_PAGE_ITEMS`,
  `SELECTION_ITEM_LIMIT` and the shipped item-kind tuple all unchanged, then asserts the facet policy name
  differs and an absent facet seed refuses with `selector_absent` under the facet policy. The second case
  asserts the facet page's counts, order, revision digest and endpoint, that no facet kind appears in a
  shipped seed's page, that a recorded statement revision with no explanation is a real empty page, that the
  selection past its bound raises `FacetSelectionIncomplete` with `(3, 1)` and refuses with
  `selection_incomplete`, and that a directly inserted revision whose seal does not hold is refused with
  `snapshot_unavailable` rather than served.

**Three cases were re-scoped by this leaf, and none was deleted, skipped or weakened.** Appending generation 5 and registering two more record kinds falsified exactly three assertions here — each one spelled the *shared* substrate's membership as a closed list this leaf legitimately grew — and each gained the replacement fact in its own docstring. `test_the_seam_registry_is_exactly_the_eight_declared_subtypes` now unions four groups, each named by the record group's own derived constant (`EVIDENCE_RECORD_KINDS` beside `DETECTION_RECORD_KINDS`), so a later group's registration is answered by that group's constant instead of by an edit here; the case's protected property — this vocabulary's eight kinds, their schemas, and no ninth facet subtype having an admissible shape — is unchanged and is asserted *before* the membership line. `test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables` now asserts the containment the facet group owns (`set(FACET_COMMAND_KINDS) <= kinds`), that every union member has a target check, and that the facet tables are a subset of the mutable set: the exact union size is another leaf's business now, while a facet command missing from the union, from the target checks or from its own step table still fails. `test_the_registered_generation_appends_only_and_the_preceding_ones_are_unchanged` derives its version and schema-name lists from the registry's own order, so a later generation's registration no longer edits it, while a gap, a repeat, a reordering or a renamed earlier generation still fails it. **The module's own count is unchanged and every shipped case is still present.**

**`260915-KS-L21` re-scoped two of those same cases again, for the census record group, and added no case
here.** The truth-coverage census registers three record kinds — the inventory row, the assessable claim and
the migration disposition — plus the three relations they resolve through, so the seam registry and the
command union each gained one group. The change is additive and stated as vocabulary rather than as
literals: `set(CENSUS_RECORD_KINDS)` joins the group tuple in
`test_the_seam_registry_is_exactly_the_eight_declared_subtypes`, and `set(CENSUS_COMMAND_KINDS)` and
`set(CENSUS_WRITABLE_TABLES)` join the two equalities in
`test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables`, all three imported from
`agents_remember.models.knowledge.census` (`mcp/tests/test_knowledge_facets.py:80-83`). Both case docstrings
carry a `RE-SCOPED once more for KS-R21@v1` paragraph (`:248-252`) saying the same thing the code does: the
group answers for its own membership, so the next kind in either group is an edit in the census's vocabulary
rather than in this module. The module's 17 cases, its lane row and its hermetic shape are unchanged, and no
assertion was deleted, skipped, deselected or weakened — the two cases still hold their own protected
properties exactly as before, and each re-scope is stated *before* the membership line rather than after it.

### Conventions

- **Assertions name the variant they are about.** Every loop over subtypes or endpoint kinds passes the kind
  into the assertion message, which is what makes one case carrying eight variants readable when it fails.
- **Refusal cases assert the write's absence**, not only the refusal code: table counts before/after, and
  `before == after` for a batch.
- **Counting and introspection are done through the harness** (`member_models`, `payload_kinds`,
  `command_kinds`, `declared_subject_kinds`, `table_counts`) rather than by restating a list in the case.
- **The module's imports are deliberately explicit**, including private dispatch tables
  (`_INSERTING_KINDS`, `_TARGET_CHECKS`, `_STEPS`), because the case's claim is about those tables agreeing
  with each other rather than about the public surface alone.

### Invariants And Boundaries

- **The suite is still 17 cases, and the ceiling claim this card used to carry is corrected rather than
  carried.** The card said the module sat "at the declared ceiling with the rest of the unit population …
  1250 against `unit_case_budget = 1250`"; that was true when the L11 leaf measured it and is **not** the
  current pair. `KS-R14@v1`'s worker report measured the unit population at **1315** and the integration
  population at **322** against the declared `unit_case_budget = 1500` / `integration_case_budget = 400`;
  that reading is retained here as the state it measured, and `260915-KS-L21` re-read it against the file.
  **The pair the file declares now is `unit_case_budget = 4000` (`pyproject.toml:278`) and
  `integration_case_budget = 1000` (`pyproject.toml:279`)** — re-read 2026-09-20 by `260918-TSIP-L13` on the raised pair; the reading measured on this candidate was **2206** unit
  collected and **394** integration collected — the census leaf's 48 unit cases took the merged population
  six past the then-declared 2200, and its unit ceiling was raised to 2300 with the measured entry recorded
  above the value, because an over-budget population makes `pytest_collection_finish` raise `UsageError` and
  execute **zero** tests. Integration is unchanged at 400 and this leaf adds no integration case. This module
  added no case in either change — the census cases are a separate module — so adding a case to *this* module
  without removing or consolidating one is still refused by collection rather than by review.
- **No case was skipped, xfailed or deselected**, and the two checks the L11 worker did not run — the
  contract-scoped memory-quality operation and `--certify` — are named in that leaf's worker report rather
  than implied by a green suite. The two re-scoped cases run in the population that is green on this candidate.
- **Boundary.** This module protects behavior; it makes no requirement-acceptance claim on its own, and the
  recorded constants it reads are evidence about the *shipped* selection rather than a claim about the new
  one.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The closure case: the payload union, the schema map, the seam's kind groups and the derived envelope row — re-scoped by `KS-R14@v1`, again for the census group by `260915-KS-L21` (`set(CENSUS_RECORD_KINDS)` at `:291`, inside the range below), and the case that carries the `RE-SCOPED` paragraph.** [1]
- **The three census vocabulary constants this leaf's two re-scoped cases import — the group's record kinds, command kinds and writable tables — added to the explicit import block at the top of the module.** [2]
- **The per-subtype walk: a valid shape, an undeclared field, a dropped meaning, three provenance substitutions and the ninth subtype.** [3]
- The ninth subtype refused through the write path with the table counts unchanged. [4]
- **The receipt's field set, the seven absent verdict words and the stored authorship-versus-decider split.** [5]
- **Accepted origin data refused at both entry points with the shipped code.** [6]
- **The four endpoint kinds attached and read back, the checked group measured in DDL, and every kind's missing-target refusal.** [7]
- **The removal that names its row, refuses a stale digest and deletes that row only.** [8]
- The ungoverned and unattached states as explicit values, and the envelope's route association. [9]
- **The three digests unchanged across a supersession, and the edge visible from the superseded side.** [10]
- **The cycle rollback, the sealed rows the database refuses to rewrite or delete, and the non-decision target refusal.** [11]
- **The explanation's separability: the designated first revision, the unchanged statement digests, and the closed subject set.** [12]
- **The widened union and the dispatch tables, now closed over every declared record group rather than over a count — `set(CENSUS_COMMAND_KINDS)` at `:953` and `set(CENSUS_WRITABLE_TABLES)` at `:981` are this leaf's two additions inside the range below, which is why the exact-total wording this row used to carry is superseded.** [13]
- **Both entry points, the batch rollback, the wrong-operation refusal and the facet-row expectation.** [14]
- **The registry, the additive prefix, the `STRICT` idiom and the rebind trigger's named columns — re-scoped by `KS-R14@v1` so the created generation is named as the newest registered one.** [15]
- **The dataset that predates the facet tables: refused, unmigrated and still served as its own generation.** [16]
- **The byte-identity comparison against the pre-leaf page and result digests. The other shipped constants are unchanged; the two digests were re-measured once, by `260921-ICR-L57`, for L44's additive `resolved_ranges` field (see `facet_test_support.py.md`).** [17]
- **The exact facet page, the empty-but-real selection, the incompleteness refusal and the damaged-seal refusal.** [18]
- The harness, the measured constants and the production entry points these cases drive. [19]
- The lane row this module is registered under. [20]
- **The governed artifact this module imports, by its own artifact id, and the two detection consumer rows `KS-R14@v1` added beneath it.** [21]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
- **The governed artifact this module imports, by its own artifact id, and the two detection consumer rows `KS-R14@v1` added beneath it.** [22]
