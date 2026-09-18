# mcp/tests/test_knowledge_facets.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_facets.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T05:15+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b`|
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l14` uncommitted source; base `4264dcc9decf50e64c863e9c6526ea09117be71b` |
| governingOverview | `overview.md` |

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
  schemas are still exactly their declared ones. The same case checks the per-kind model's `extra`/`frozen` config, that
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
- **The union and dispatch case measures the widening**: the command kinds are exactly the twelve shipped
  plus the six facet kinds (18), `_TARGET_CHECKS` covers every kind, `_STEPS` is exactly the six facet
  kinds, and `MutableRecordTable` is the shipped seven plus the facet module's six declared tables.
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
  current pair. `KS-R14@v1`'s worker report measures the unit population at **1315** and the integration
  population at **322** against the declared `unit_case_budget = 1500` / `integration_case_budget = 400`, and
  this leaf added no case here — its two detection suites are separate modules. Adding a case to *this* module
  without removing or consolidating one is still refused by collection rather than by review.
- **No case was skipped, xfailed or deselected**, and the two checks the L11 worker did not run — the
  contract-scoped memory-quality operation and `--certify` — are named in that leaf's worker report rather
  than implied by a green suite. The two re-scoped cases run in the population that is green on this candidate.
- **Boundary.** This module protects behavior; it makes no requirement-acceptance claim on its own, and the
  recorded constants it reads are evidence about the *shipped* selection rather than a claim about the new
  one.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The closure case: the payload union, the schema map, the seam's three kind groups and the derived envelope row — re-scoped by `KS-R14@v1` and the case that carries the `RE-SCOPED` paragraph.** | "test_the_seam_registry_is_exactly_the_eight_declared_subtypes" | mcp/tests/test_knowledge_facets.py:183-247 |
| **The per-subtype walk: a valid shape, an undeclared field, a dropped meaning, three provenance substitutions and the ninth subtype.** | "test_every_subtype_refuses_a_bad_shape_a_missing_meaning_and_its_own_provenance" | mcp/tests/test_knowledge_facets.py:332-332 |
| The ninth subtype refused through the write path with the table counts unchanged. | "test_an_unknown_ninth_subtype_is_refused_and_never_stored_as_a_generic_facet" | mcp/tests/test_knowledge_facets.py:392-392 |
| **The receipt's field set, the seven absent verdict words and the stored authorship-versus-decider split.** | "test_a_facets_authorship_lifecycle_and_receipt_are_stored_data_with_no_verdict" | mcp/tests/test_knowledge_facets.py:415-415 |
| **Accepted origin data refused at both entry points with the shipped code.** | "test_accepted_origin_data_is_refused_at_both_entry_points" | mcp/tests/test_knowledge_facets.py:455-455 |
| **The four endpoint kinds attached and read back, the checked group measured in DDL, and every kind's missing-target refusal.** | "test_every_endpoint_kind_is_a_checked_group_that_refuses_a_missing_target" | mcp/tests/test_knowledge_facets.py:479-479 |
| **The removal that names its row, refuses a stale digest and deletes that row only.** | "test_removing_an_attachment_names_its_row_and_deletes_that_row_only" | mcp/tests/test_knowledge_facets.py:564-564 |
| The ungoverned and unattached states as explicit values, and the envelope's route association. | "test_an_unattached_facet_and_the_envelopes_route_association_are_explicit_states" | mcp/tests/test_knowledge_facets.py:603-603 |
| **The three digests unchanged across a supersession, and the edge visible from the superseded side.** | "test_a_superseding_decision_authors_an_edge_and_the_superseded_one_is_retained" | mcp/tests/test_knowledge_facets.py:648-648 |
| **The cycle rollback, the sealed rows the database refuses to rewrite or delete, and the non-decision target refusal.** | "test_a_supersession_cycle_rolls_back_and_a_sealed_decision_cannot_be_rewritten" | mcp/tests/test_knowledge_facets.py:698-698 |
| **The explanation's separability: the designated first revision, the unchanged statement digests, and the closed subject set.** | "test_an_explanation_is_separable_and_editing_it_never_rewrites_the_statement" | mcp/tests/test_knowledge_facets.py:697-806 |
| **The widened union and the dispatch tables measured against the twelve shipped kinds.** | "test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables" | mcp/tests/test_knowledge_facets.py:901-901 |
| **Both entry points, the batch rollback, the wrong-operation refusal and the facet-row expectation.** | "test_the_two_entry_points_agree_and_a_refused_write_writes_nothing" | mcp/tests/test_knowledge_facets.py:965-965 |
| **The registry, the additive prefix, the `STRICT` idiom and the rebind trigger's named columns — re-scoped by `KS-R14@v1` so the created generation is named as the newest registered one.** | "test_the_registered_generation_appends_only_and_the_preceding_ones_are_unchanged" | mcp/tests/test_knowledge_facets.py:1045-1045 |
| **The dataset that predates the facet tables: refused, unmigrated and still served as its own generation.** | "test_a_dataset_predating_the_facet_tables_refuses_a_facet_write" | mcp/tests/test_knowledge_facets.py:1142-1142 |
| **The byte-identity comparison against the pre-leaf page and result digests, with the shipped constants unchanged.** | "test_the_shipped_seed_page_is_byte_identical_and_the_facet_page_is_its_own_policy" | mcp/tests/test_knowledge_facets.py:1194-1194 |
| **The exact facet page, the empty-but-real selection, the incompleteness refusal and the damaged-seal refusal.** | "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact" | mcp/tests/test_knowledge_facets.py:1246-1246 |
| The harness, the measured constants and the production entry points these cases drive. | `write_facet`; `build_recorded_fixture`; `PRE_LEAF_PAGE_DIGEST` | mcp/tests/facet_test_support.py:362-380; mcp/tests/facet_test_support.py:535-658; mcp/tests/facet_test_support.py:96-96 |
| The lane row this module is registered under. | "unit-regression = [" | mcp/tests/test-evidence-lanes.toml:5-5 |
|**The governed artifact this module imports, by its own artifact id, and the two detection consumer rows `KS-R14@v1` added beneath it.**|"id = \"knowledge-facet-cases\""| mcp/tests/evidence-lifecycle.toml:55-55 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |
| **The governed artifact this module imports, by its own artifact id, and the two detection consumer rows `KS-R14@v1` added beneath it.** | "id = \"knowledge-facet-cases\"" | mcp/tests/evidence-lifecycle.toml:55-55 |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_every_subtype_refuses_a_bad_shape_a_missing_meaning_and_its_own_provenance" repointed to mcp/tests/test_knowledge_facets.py:332-332. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_an_unknown_ninth_subtype_is_refused_and_never_stored_as_a_generic_facet" repointed to mcp/tests/test_knowledge_facets.py:392-392. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_a_facets_authorship_lifecycle_and_receipt_are_stored_data_with_no_verdict" repointed to mcp/tests/test_knowledge_facets.py:415-415. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_accepted_origin_data_is_refused_at_both_entry_points" repointed to mcp/tests/test_knowledge_facets.py:455-455. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_every_endpoint_kind_is_a_checked_group_that_refuses_a_missing_target" repointed to mcp/tests/test_knowledge_facets.py:479-479. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_removing_an_attachment_names_its_row_and_deletes_that_row_only" repointed to mcp/tests/test_knowledge_facets.py:564-564. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_an_unattached_facet_and_the_envelopes_route_association_are_explicit_states" repointed to mcp/tests/test_knowledge_facets.py:603-603. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_a_superseding_decision_authors_an_edge_and_the_superseded_one_is_retained" repointed to mcp/tests/test_knowledge_facets.py:648-648. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_a_supersession_cycle_rolls_back_and_a_sealed_decision_cannot_be_rewritten" repointed to mcp/tests/test_knowledge_facets.py:698-698. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables" repointed to mcp/tests/test_knowledge_facets.py:901-901. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_the_two_entry_points_agree_and_a_refused_write_writes_nothing" repointed to mcp/tests/test_knowledge_facets.py:965-965. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_the_registered_generation_appends_only_and_the_preceding_ones_are_unchanged" repointed to mcp/tests/test_knowledge_facets.py:1045-1045. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_a_dataset_predating_the_facet_tables_refuses_a_facet_write" repointed to mcp/tests/test_knowledge_facets.py:1142-1142. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_the_shipped_seed_page_is_byte_identical_and_the_facet_page_is_its_own_policy" repointed to mcp/tests/test_knowledge_facets.py:1194-1194. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact" repointed to mcp/tests/test_knowledge_facets.py:1246-1246. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-facet-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:55-55. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-facet-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:55-55. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_every_subtype_refuses_a_bad_shape_a_missing_meaning_and_its_own_provenance" repointed to mcp/tests/test_knowledge_facets.py:307-307. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_an_unknown_ninth_subtype_is_refused_and_never_stored_as_a_generic_facet" repointed to mcp/tests/test_knowledge_facets.py:361-361. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_a_facets_authorship_lifecycle_and_receipt_are_stored_data_with_no_verdict" repointed to mcp/tests/test_knowledge_facets.py:384-384. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_accepted_origin_data_is_refused_at_both_entry_points" repointed to mcp/tests/test_knowledge_facets.py:424-424. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_removing_an_attachment_names_its_row_and_deletes_that_row_only" repointed to mcp/tests/test_knowledge_facets.py:533-533. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_an_unattached_facet_and_the_envelopes_route_association_are_explicit_states" repointed to mcp/tests/test_knowledge_facets.py:572-572. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_a_superseding_decision_authors_an_edge_and_the_superseded_one_is_retained" repointed to mcp/tests/test_knowledge_facets.py:617-617. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables" repointed to mcp/tests/test_knowledge_facets.py:866-866. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_the_two_entry_points_agree_and_a_refused_write_writes_nothing" repointed to mcp/tests/test_knowledge_facets.py:930-930. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_the_registered_generation_appends_only_and_the_preceding_ones_are_unchanged" repointed to mcp/tests/test_knowledge_facets.py:1009-1009. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_a_dataset_predating_the_facet_tables_refuses_a_facet_write" repointed to mcp/tests/test_knowledge_facets.py:1106-1106. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_the_shipped_seed_page_is_byte_identical_and_the_facet_page_is_its_own_policy" repointed to mcp/tests/test_knowledge_facets.py:1157-1157. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact" repointed to mcp/tests/test_knowledge_facets.py:1208-1208. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "id = \"knowledge-facet-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1207-1207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "id = \"knowledge-facet-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1207-1207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 4 generated projection bullet(s) by hand while resolving the memory sync** — `id = \`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T05:00:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): **re-read this card for the two assertions this leaf re-scoped and corrected its account of them.** The command-union case no longer spells the union's membership as a closed list: it unions this leaf's published `COMPOSITION_COMMAND_KINDS` and `COMPOSITION_WRITABLE_TABLES` and asserts `len(kinds) == 18 + len(COMPOSITION_COMMAND_KINDS)`, while keeping the stronger half exactly (`set(_TARGET_CHECKS) == kinds` still fails the moment a command is added without a target check). The registry case no longer pins the four versions as a list: it asserts the generations in **order** and the derived schema-name list, with every generation-3-specific assertion unchanged, including the generation-2 fingerprint pin. Both carry a `RE-SCOPED for KS-R17@v1` paragraph in the case docstring. No case was deleted, skipped, deselected, xfailed or weakened, and neither budget moved. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand** — `id = \`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read every citation this card carries against the current source and repaired the ranges this leaf's addition moved.** This entry recorded the three cases this leaf re-scoped, each gaining the replacement fact in its own docstring, with no case deleted, skipped or weakened. Verification metadata is unchanged and the code commit does not exist yet; closeout owns that stamp.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 3 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"test_an_unknown_ninth_subtype_is_refused_and_never_stored_as_a_generic_facet"` → `mcp/tests/test_knowledge_facets.py:302-302`; `"test_accepted_origin_data_is_refused_at_both_entry_points"` → `mcp/tests/test_knowledge_facets.py:365-365`; `"test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables"` → `mcp/tests/test_knowledge_facets.py:807-807`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/evidence-lifecycle.toml:1192-1192` -> `mcp/tests/evidence-lifecycle.toml:1193-1193`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): **re-read the population claim against the measured candidate and moved both numbers.** This leaf's two new test modules raise the unit population 1315 → **1340** and the integration population 322 → **337**, measured on this candidate before any sync onto the moved official line; the card's ceiling paragraph now states both, against the unchanged declared pair `unit_case_budget = 1500` / `integration_case_budget = 400`. The two cases the leaf re-scoped rather than deleted are recorded here because this is the module that owns them: the seam-registry case is re-scoped **additively** so its union names `CITATION_BINDING_RECORD_KINDS` instead of the expectation being trimmed back, and the generation case now asserts the registry sequence as the **structural** fact — one contiguous `1..N` sequence, each generation declaring its own `ar-knowledge-sqlite/vN` name, in register order — which is stronger than the literal list it replaced, since a hand-edited list stays green on an out-of-order or skipped generation and these assertions redden on exactly that. No case was deleted, skipped or xfailed. Verification metadata is **not** advanced over unreviewed content: the body was re-read against the current source, and the code commit does not exist yet — closeout owns that stamp.

- 2026-09-18T03:15:00+00:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): **re-read this card against the current source and recorded the two cases `KS-R14@v1` re-scoped.** Appending generation 4 falsified exactly two assertions in this module — both spelled the *shared* substrate's membership as a closed list the leaf legitimately grew — and the card's Logic now states what each one asserts instead: the seam-registry case states the registry's **three groups** and pins the facet half *more* precisely by asserting each kind's admissible schema set, and the generation case names the created generation as `GENERATIONS[-1]` rather than as a literal the next generation would falsify, with every generation-3-specific assertion unchanged. **One claim this card carried is corrected rather than carried:** its ceiling paragraph said the unit population was 1250 against `unit_case_budget = 1250`; that was the L11 leaf's own measurement, and the current pair is **1315 against 1500** (integration 322 against 400), which is what the paragraph now says. The lane-row pointer moved with the two-line lane insertion (`:71` → `:73`) and the two re-scoped cases' rows were re-cited (`:181-227` → `:182-227`, `:888-932` → `:901-935`). No case was deleted, skipped or xfailed, and no verification stamp is advanced over content that was not re-read: this card's body was re-read against the current source, and the code commit does not exist yet — closeout owns that stamp.

- 2026-09-17T22:25:00+00:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): created this one-to-one card for the new unit-regression suite. It records the two properties the module names before its cases (the payload seam as the only payload decision point, and nothing derived), the **case-ceiling reason** a case carries a loop rather than a parametrization with its stated cost, each of the seventeen nodes and the clause group it protects — the closure assertions, the eight-kind refusal walk, stored authorship and lifecycle, accepted-origin refusal at both entry points, the four endpoint kinds in both directions, the one-row removal, the explicit ungoverned and unattached states, the retained superseded decision with its three unchanged digests, the cycle rollback and the four database refusals, the separable explanation with the designated first revision, the widened union and dispatch tables, the two entry points, the registry and additive prefix, the predating dataset, and the two read cases (byte identity against the pre-leaf digests, and the exact facet page with its incompleteness and damaged-seal refusals) — plus the lane row and the governed artifact it is registered under. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
