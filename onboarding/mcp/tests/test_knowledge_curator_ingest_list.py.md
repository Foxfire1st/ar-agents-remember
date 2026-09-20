# mcp/tests/test_knowledge_curator_ingest_list.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_curator_ingest_list.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T02:26+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l33-ar`, uncommitted; base `7dcec036094768c5f50e571fb45e59a27ae78efc` |
| lastVerifiedCommitHash | `be95a6cd5f43b72d99868ff9999e16105c3f324d` |
| lastVerifiedCommitDate | 2026-09-20T02:30:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

The module is the evidence for `ingest_curator_list`, the operation the leaf's objective names: the
curator receives the orchestrator's whole hand-off list and turns it into one admitted batch and one
auditable report. The single-entry write half already has its own cases
(`mcp/tests/test_knowledge_curator_ingest.py`), so nothing here re-protects a citation round trip. What
this module adds is five operations those cases cannot reach:

- **a producer citing the code its own leaf is producing** — the case the whole operation exists for,
  and the one that was broken: the leaf's own line is the tree citations resolve against, so a file the
  leaf **added** commits and reads back, and a file the leaf **modified** commits too, rather than
  making the run raise before it has a report;
- **the three outcomes in one run**, on one list: an entry whose citation resolved is `committed`, a
  ruling that carries no target is `skipped` with its own verdict carried, and a target that does not
  resolve is `refused` with the reason that distinguishes the ways it can fail;
- **the whole path of a producer's bare symbol name**: the derived language, the stored two-part
  locator, the read surface handing it back typed, and the rail refusing to resolve it;
- **identity derived from the enclosure**, so a re-run mints the same identities and refuses instead of
  duplicating, and a dry run reports the counts the real run would write;
- **the route leg**, the one part of the citation the closed command union cannot carry.

The CYCLE-01 repair added a sixth: **repository knowledge that is continuous across tasks and code
baselines** — one namespace per repository (read from the dataset that already stores it, derived only
as a cold-start fallback), an absent candidate forked from the selected baseline instead of created
empty, an entry that names the invariant and predecessors it revises instead of re-declaring an
invariant the batch refuses to create, and several anchors in one source file rather than one. Those
cases live in `RepositoryIdentityStabilityTests`.

The properties matter because this operation is the boundary between an unlanded leaf's own work and
the recorded knowledge plane. A curator that resolved against the recorded base would refuse the leaf's
own deliverable as *gone*; a run that raised instead of reporting would leave the hand-off unauditable;
and a reason whose words are true of only one failure would tell a producer to search somewhere else
instead of what to fix.

## Code Commentary

### Logic

The fixture is a real pair of Git repositories beside a real contract, because the ingest resolves paths
through a recorded tree and derives each blob identity from the bytes the tree names: a synthetic path
table would measure the fixture instead of the resolver. `pair` builds it once per session — two
commits in the code repository, the base the contract records and then the leaf's own work on top of it
(one file added, one file edited, both left as the line), plus a memory repository carrying its
onboarding card, plus a third root (`notes/…`) under the coordination root that the citation machinery
does not admit. Nothing is left dirty, so the base tree and the line tree differ only by the leaf's
change, which is what makes a case here a measurement about two trees rather than about a working
directory. `SourcePair` carries both tree ids, both blob tables and the leaf line's identity;
`_Layout` names the four directories the contract's cells name; `_write_files`, `_commit` and `_git`
build the repositories under a pinned environment; and `_contract_text` writes exactly the cells the
ingest reads (coordination root and task root, both repo roots and base commits, work branches, the
ledger) with no defaults assumed. `entry(...)` is revision 1's hand-off shape with the curator-side
fields null, `target(...)` one place with the locator and route the producer wrote or their absence,
`symbol(...)` a producer's bare name and `_range(...)` a producer-written line range. `run(...)`
ingests one list into a candidate directory the case owns, building the one `IngestSelection` the
operation now takes — candidate directory, authorization ref, dry-run flag — `by_id(...)` keys one
report's outcomes, and `counts(...)` reads the six written tables' row counts from the database itself.

The cases, grouped by what they establish:

- **The mixture.** `test_one_run_reports_committed_skipped_and_each_refusal_reason` drives five entries
  in one report — one committed, one ruling, and three path refusals — and asserts the ruling is
  `skipped` **with its own verdict carried** (`disposition`, `kind`) and that the three path reasons
  (`top_level_entry_file_gone`, `third_root_out_of_scope`, `dependency_source_not_ours`) are three
  distinct words rather than three spellings of one. `test_a_ruling_is_never_committed_as_an_obligation_with_no_realization`
  pins the empty-target rule to the target and not to the kind: an entry with no target is skipped,
  nothing is written (zero `invariant` rows, because `CuratorEntry.citations` permits an empty list and
  that path is deliberately not taken here), and a `clause` and a `finding` ruling are skipped too,
  their dispositions intact. The two were merged because both measure one reading of `target: []`.
- **The leaf's own line.** `test_a_producer_citing_a_file_its_own_leaf_created_commits_and_reads_back`
  commits the leaf's new file, asserts the report's `code_tree_id` is the line's tree, that the recorded
  `source_identity` is that tree's blob, and that the base tree holds no member at that path at all —
  which is the whole difference between the two trees — then reads the stored row back as the derived
  two-part symbol locator. `test_a_producer_citing_a_file_its_own_leaf_modified_gets_a_report_not_an_exception`
  is the ordinary state of a leaf: a changed file on its line commits with the line's blob as its
  identity, and the case states that the two trees genuinely disagree about that file, which is what
  made the old base binding raise.
- **The reason vocabulary.** `test_each_locator_failure_carries_the_reason_that_is_true_of_it`
  distinguishes five failures — non-integer bounds, a reversed pair, a zero-based range, a range past
  the last line, an unsupported locator kind — and then shows the distinction is neither a blanket
  refusal of ranges (a one-based range inside the file is accepted) nor a single measurement:
  `targets_completed` counts every place whose path the read really measured while `locators_resolved`
  counts only the places that reached the batch, so on an entry refused at its second target the two
  differ by exactly that first place. `test_a_path_reason_is_read_from_the_trees_and_not_from_the_live_directories`
  builds its own enclosure, asserts six reason codes across repeated runs, then deletes the cited report
  and finally the third root's own directory, showing every reason comes from the recorded trees and the
  path's own spelling — and states the one limit rather than hiding it, that the first-segment test does
  read which top-level directories the coordination root holds.
- **The symbol path.** `test_a_symbol_locator_resolves_a_qualified_name_and_refuses_an_invented_prefix`
  accepts `Holder.<method>` by checking both real halves of the name and refuses `Nowhere.<method>`.
  `test_a_producer_symbol_name_is_resolved_stored_and_read_back_typed` follows a bare name through
  every step: the stored row, the mounted view handing back a `SymbolLocator` rather than the stored
  text, and the rail answering `unsupported_locator`. `test_the_definition_check_refuses_a_mention_and_every_kind_of_non_definition`
  refuses seven shapes with the reason true of each — a name in a docstring, in a comment, a name that
  is a substring of another definition, a name defined in a different file, a target carrying no
  locator, a memory card (`symbol_target_is_prose`) and a structured data file's key
  (`symbol_target_is_prose`). The first two are what a check reading raw bytes would have accepted,
  which is the fabrication the case exists to refuse.
- **Identity measured, not assumed.** `test_the_recorded_blob_identity_is_measured_and_a_working_edit_is_a_typed_refusal`
  shows the identity is read from the working bytes so the mismatch state is reachable at all: the
  ordinary case records the committed blob and observes the symbol as unsupported, and an uncommitted
  edit to the cited file refuses with `recorded_blob_mismatch` and zero rows written.
  `test_a_path_in_the_memory_root_carries_the_memory_tree_identity` resolves a memory card through the
  declared `memory-onboarding` step and records the memory tree's blob, which is not the code tree's.
- **Identity derived, dry runs, authorization.** `test_identity_is_derived_from_the_enclosure_so_a_second_run_is_diagnosable`
  runs the same list twice: the first commits with the anchor identity equal to the file's own blob,
  the second refuses with `batch_stale_precondition` (the batch is all-or-nothing, so a re-run that
  would re-assert the same rows refuses instead of duplicating) and leaves every count unchanged.
  `test_dry_and_real_runs_report_the_same_written_rows_and_a_refused_run_reports_none` asserts the dry
  report names both trees it read, reports four commands and six rows — four batch rows plus the
  scope's route row and its association — while creating no candidate directory at all, and that the
  real run's counts equal the dry one's and the database's own row sum; a refused re-run reports zero
  rows written and zero routes authored. `test_an_empty_authorization_is_refused_by_name_before_anything_is_read`
  expects a `ValueError` naming `authorization_ref` and no candidate directory, so a caller that
  omitted the authorization gets a sentence rather than a model error from deep inside the envelope.
- **The route leg.** `test_the_governing_route_is_recorded_once_per_scope_and_attached_to_each_anchor`
  drives three targets, two of which name one scope, and produces one `route` row, two associations,
  and one anchor left explicitly `ungoverned` rather than inheriting a route.
  `test_re_authoring_an_existing_route_reuses_its_row_rather_than_writing_a_second` shows the second
  run authors nothing and reuses the row, which is what keeps one scope one route, and that the report
  says which leg answered.
- **What the report names.** `test_the_report_names_the_candidate_its_receipt_the_lane_and_the_exact_inputs`
  pins the candidate directory, the receipt path (narrowed to `str` before it is used as a path, so a
  missing receipt fails the equality instead of reaching `Path` as `None`), the `draft-candidate` lane,
  the leaf-line tree id beside the recorded base commit and the `work-line:` source that says where
  that tree came from, the memory tree, the repository and the entries read.
- **CYCLE-01: continuity across tasks and baselines.**
  `test_repository_knowledge_continues_across_baselines_and_tasks` is five assertions kept as one
  case because the unit lane's ceiling is a hard 2300 that this change set had already breached, and
  every original assertion survives: (a) one `_repository_identity` for one repository read at two
  code baselines, where the old derivation keyed the namespace on the enclosure's recorded base commit
  and so gave one repository two namespaces *and* two repositories sharing a base the same one; (b)
  the **stored** namespace wins — a real `build_case`/`create` database carrying a `uuid4` namespace
  unrelated to anything derivable from the contract is handed in as the baseline and its value comes
  back, and a baseline that is not a database falls back to the same value an absent one gives rather
  than raising; (c) an absent candidate **forks** the selected baseline through
  `_admitted_candidate(..., baseline=...)`, and the forked database really carries the prior
  invariant and a revision; (d) `_EntryFields.read` makes an entry naming `predecessor_revision_ids`
  a successor (`declares_invariant is False`, the predecessors kept, `invariant_id` read as the named
  one) and `curator_entry_commands` then emits no `AddInvariant` at all — the
  `batch_stale_precondition` refusal the review reproduced — while a declaring entry still emits both
  commands; and (e) two symbols in one file produce two different `_observation_id` anchors while the
  same symbol named twice still produces one, which is the duplicate guard's own purpose asserted
  intact rather than weakened away.

### Conventions

- **The fixture is built in-file, and the one governed artifact it consumes is the snapshot
  lifecycle's support module.** The module imports the standard library, `pytest` and production code,
  and — since CYCLE-01 — `build_case`, `create` and `write_record` from
  `snapshot_lifecycle_test_support`, which is what gives the continuity case a real candidate
  database to fork. The two repositories, the contract and the Git calls are still local to this
  file, and because that import makes this module a consumer of a governed artifact it carries a
  `consumers` row in `mcp/tests/evidence-lifecycle.toml` for the `snapshot_lifecycle_test_support.py`
  artifact and its `knowledge-snapshot-lifecycle-cases` contract.
- **The fixture is session-scoped and never mutated by a case.** Every case writes into its own
  candidate directory under its own `tmp_path`, and the cases that need to change a cited file build
  their own enclosure instead of touching the shared one.
- **Fixed inputs live in module constants** (the paths, the symbol names, the mentions file's text, the
  structured data file's text), so a case varies a fact rather than a string.
- **Refusals are asserted by their own code**, and the path reasons are read past the step prefix, so a
  case cannot pass on a neighbouring refusal.
- **Row counts are read from the database through `counts(...)`** rather than from the report, so the
  report's arithmetic is measured against the rows that exist.
- The card records source behaviour. Source inspection is memory preparation: no test run was executed
  in this pass, and the verification stamps above are closeout-owned.

### Invariants And Boundaries

- One list, one batch, one report, and the batch is all-or-nothing: a re-run that would re-assert the
  same rows refuses rather than duplicating them, and a refusal writes nothing.
- The three outcomes never merge: `committed`, `skipped` (a ruling with no target, its verdict carried)
  and `refused` (a named target that did not resolve). An entry appears in exactly one of them.
- A citation's reason is a fact about the recorded trees and the path's own spelling, never about
  `is_file()` on a live directory, so the enclosure's cleanup cannot change it. The one live fact the
  classification reads is which top-level directories the coordination root holds.
- A symbol citation is verified at ingest time — the rail cannot re-verify a symbol kind — so only a
  definition becomes a symbol locator; a mention, a prose document and a structured data file's key are
  each refused with the reason true of that form.
- Identity is derived from the enclosure and the entry's own id rather than drawn, and the resolution
  tree (the leaf's own line) is kept apart from the identity anchor (the recorded base commit). The
  **repository namespace** is the one identity that is not derived first: a run READS it from the
  dataset it was handed as the baseline, and derives under `_INGEST_NAMESPACE` from `repo_name` only
  when that dataset records none or cannot be read, because a namespace keyed on the code base commit
  moves with the baseline while the knowledge it scopes does not.
- **Boundary.** The route leg does not travel through the command batch — its only route member names a
  family revision — so the two legs are reported separately, and a route that cannot be recorded
  refuses the list before anything is committed. This module starts no publication and makes no
  requirement-acceptance claim of its own.

### Todos

No file-local implementation change is requested by this card. One registration fact changed at
CYCLE-01 and is recorded rather than assumed: the module now imports
`snapshot_lifecycle_test_support`, so it carries a `consumers` row in
`mcp/tests/evidence-lifecycle.toml` for that artifact and its
`knowledge-snapshot-lifecycle-cases` contract — the row this leaf appended, which is what the catalog's
own consumer proof requires of every importer. It still carries no placement in
`mcp/tests/test-evidence-lanes.toml`, so no lane placement is asserted here and no test run was
executed to produce one.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows below cite the module's own constructs, the operations they drive and the vocabulary those
operations report, with each anchor resolving inside the range cited for it. Ranges are the exact
construct extents at the verification commit.

| Finding | Anchor | Source |
| --- | --- | --- |
| The session fixture: a real code repository committed twice (the recorded base and the leaf's own line), a real memory repository, and the contract that names both. | `pair`; `SourcePair` | mcp/tests/test_knowledge_curator_ingest_list.py:154-233; mcp/tests/test_knowledge_curator_ingest_list.py:137-153 |
| The fixture's own machinery: write files, commit under a pinned identity, call Git with a hermetic environment, and write a contract carrying exactly the cells the ingest reads. | `_write_files`; `_commit`; `_git`; `_contract_text` | mcp/tests/test_knowledge_curator_ingest_list.py:236-240; mcp/tests/test_knowledge_curator_ingest_list.py:243-248; mcp/tests/test_knowledge_curator_ingest_list.py:251-262; mcp/tests/test_knowledge_curator_ingest_list.py:265-309 |
| The hand-off builders: one entry in revision 1's shape, one target place, the producer's bare symbol spelling, and a producer-written line range. | `entry`; `target`; `symbol`; `_range` | mcp/tests/test_knowledge_curator_ingest_list.py:317-340; mcp/tests/test_knowledge_curator_ingest_list.py:343-346; mcp/tests/test_knowledge_curator_ingest_list.py:355-358; mcp/tests/test_knowledge_curator_ingest_list.py:349-352 |
| The drive and measurement helpers: ingest one list into a candidate directory the case owns — building the one `IngestSelection` the operation now takes — key one report's outcomes, and count the six written tables from the database. | `run`; `by_id`; `counts` | mcp/tests/test_knowledge_curator_ingest_list.py:361-374; mcp/tests/test_knowledge_curator_ingest_list.py:377-380; mcp/tests/test_knowledge_curator_ingest_list.py:383-400 |
| The three outcomes in one report, with the ruling skipped while carrying its own verdict and the three path reasons asserted to be three distinct words. | "test_one_run_reports_committed_skipped_and_each_refusal_reason"; "test_a_ruling_is_never_committed_as_an_obligation_with_no_realization" | mcp/tests/test_knowledge_curator_ingest_list.py:408-463; mcp/tests/test_knowledge_curator_ingest_list.py:466-505 |
| The leaf's own line as the resolution tree: a file the leaf added commits and reads back, and a file the leaf modified produces a report rather than an exception. | "test_a_producer_citing_a_file_its_own_leaf_created_commits_and_reads_back"; "test_a_producer_citing_a_file_its_own_leaf_modified_gets_a_report_not_an_exception" | mcp/tests/test_knowledge_curator_ingest_list.py:513-566; mcp/tests/test_knowledge_curator_ingest_list.py:569-596 |
| The refusal vocabulary: five distinct locator failures and their distinct reasons, and every path reason read from the recorded trees rather than from the live directories. | "test_each_locator_failure_carries_the_reason_that_is_true_of_it"; "test_a_path_reason_is_read_from_the_trees_and_not_from_the_live_directories" | mcp/tests/test_knowledge_curator_ingest_list.py:604-699; mcp/tests/test_knowledge_curator_ingest_list.py:702-799 |
| The producer's bare symbol name end to end: a qualified name resolved by both halves with an invented prefix refused, a bare name stored and read back typed, and a definition check that refuses a mention or any other non-definition. | "test_a_symbol_locator_resolves_a_qualified_name_and_refuses_an_invented_prefix"; "test_a_producer_symbol_name_is_resolved_stored_and_read_back_typed"; "test_the_definition_check_refuses_a_mention_and_every_kind_of_non_definition" | mcp/tests/test_knowledge_curator_ingest_list.py:802-849; mcp/tests/test_knowledge_curator_ingest_list.py:929-988; mcp/tests/test_knowledge_curator_ingest_list.py:991-1066 |
| The recorded identity measured against the working bytes, and a memory path carrying the memory tree's identity rather than the code tree's. | "test_the_recorded_blob_identity_is_measured_and_a_working_edit_is_a_typed_refusal"; "test_a_path_in_the_memory_root_carries_the_memory_tree_identity" | mcp/tests/test_knowledge_curator_ingest_list.py:852-921; mcp/tests/test_knowledge_curator_ingest_list.py:1069-1069 |
| Derived identity and the modes around it: a second run refuses rather than duplicating, a dry run's counts are the counts the real run writes, and a blank authorization is refused by name before anything is read. | "test_identity_is_derived_from_the_enclosure_so_a_second_run_is_diagnosable"; "test_dry_and_real_runs_report_the_same_written_rows_and_a_refused_run_reports_none"; "test_an_empty_authorization_is_refused_by_name_before_anything_is_read" | mcp/tests/test_knowledge_curator_ingest_list.py:1103-1103; mcp/tests/test_knowledge_curator_ingest_list.py:1139-1221; mcp/tests/test_knowledge_curator_ingest_list.py:1224-1224 |
| The route leg and the report's own names: one row per scope with one association per governed anchor and an ungoverned anchor left ungoverned, a re-authored route reused rather than written twice, and the candidate, receipt, lane and trees the report names. | "test_the_governing_route_is_recorded_once_per_scope_and_attached_to_each_anchor"; "test_re_authoring_an_existing_route_reuses_its_row_rather_than_writing_a_second"; "test_the_report_names_the_candidate_its_receipt_the_lane_and_the_exact_inputs" | mcp/tests/test_knowledge_curator_ingest_list.py:1252-1308; mcp/tests/test_knowledge_curator_ingest_list.py:1311-1344; mcp/tests/test_knowledge_curator_ingest_list.py:1352-1352 |
| The operation under test and the report it returns: one admitted batch or a typed refusal per entry, with the three outcomes and the counts that make a run auditable kept apart. | `ingest_curator_list`; `IngestReport`; `IngestCounts`; `TargetOutcome`; `EntryOutcome` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:700-795; mcp/src/agents_remember/application/knowledge_curator_ingest.py:364-397; mcp/src/agents_remember/application/knowledge_curator_ingest.py:304-316; mcp/src/agents_remember/application/knowledge_curator_ingest.py:330-340; mcp/src/agents_remember/application/knowledge_curator_ingest.py:681-780 |
| The vocabulary this module asserts by name: the six path reasons and the nine locator-or-symbol codes its cases name, each standing for one distinct fact rather than one shared word for "did not resolve". | `_REASON_THIRD_ROOT`; `_REASON_GONE`; `_REASON_DEPENDENCY`; `_REASON_OUTSIDE_BY_SPELLING`; `_REASON_NOT_CONFINED`; `_REASON_INSIDE_BY_SPELLING`; `_CODE_LINE_RANGE_MALFORMED`; `_CODE_LINE_RANGE_ORDER`; `_CODE_LINE_RANGE_ZERO_BASED`; `_CODE_LINE_RANGE_PAST_END`; `_CODE_LOCATOR_MISSING`; `_CODE_LOCATOR_KIND`; `_CODE_CONSTRUCT_ABSENT`; `_CODE_NOT_A_DEFINITION`; `_CODE_NO_DEFINITIONS_IN_PROSE` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:186-186; mcp/src/agents_remember/application/knowledge_curator_ingest.py:188-188; mcp/src/agents_remember/application/knowledge_curator_ingest.py:187-187; mcp/src/agents_remember/application/knowledge_curator_ingest.py:189-189; mcp/src/agents_remember/application/knowledge_curator_ingest.py:190-190; mcp/src/agents_remember/application/knowledge_curator_ingest.py:191-191; mcp/src/agents_remember/application/knowledge_curator_ingest.py:205-205; mcp/src/agents_remember/application/knowledge_curator_ingest.py:206-206; mcp/src/agents_remember/application/knowledge_curator_ingest.py:207-207; mcp/src/agents_remember/application/knowledge_curator_ingest.py:208-208; mcp/src/agents_remember/application/knowledge_curator_ingest.py:211-211; mcp/src/agents_remember/application/knowledge_curator_ingest.py:212-212; mcp/src/agents_remember/application/knowledge_curator_ingest.py:213-213; mcp/src/agents_remember/application/knowledge_curator_ingest.py:214-214; mcp/src/agents_remember/application/knowledge_curator_ingest.py:215-215 |
| The internals that produce the pinned behaviour: the reason classifier read from the recorded trees, the symbol resolution, its language gate and its definition check, the occurrence test that separates a definition from a mention, the observation gate that accepts a symbol only on the rail's own answer, and the route leg that runs before the batch. | `_unresolved_reason`; `_symbol_locator`; `_symbol_language`; `_occurs`; `_observe`; `_author_routes` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1405-1445; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1636-1679; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1682-1723; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1738-1748; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1757-1801; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1815-1843 |
| The operation under test and the report it returns: one admitted batch or a typed refusal per entry, with the three outcomes and the counts that make a run auditable kept apart — and the selection value the operation is handed. | `ingest_curator_list`; `IngestSelection`; `IngestReport`; `IngestCounts`; `TargetOutcome`; `EntryOutcome` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:741-843; mcp/src/agents_remember/application/knowledge_curator_ingest.py:725-738; mcp/src/agents_remember/application/knowledge_curator_ingest.py:344-377; mcp/src/agents_remember/application/knowledge_curator_ingest.py:320-340; mcp/src/agents_remember/application/knowledge_curator_ingest.py:280-292; mcp/src/agents_remember/application/knowledge_curator_ingest.py:306-316 |
| The internals that produce the pinned behaviour: the reason classifier read from the recorded trees, the symbol resolution and its definition check — which is the shipped `bound_definitions`, because this module no longer carries its own blanking pass or `_defines`/`_code_only`, with `_occurs` the mention test that separates a non-definition from an absent construct — the observation gate that accepts a symbol only on the rail's own answer, and the route leg that runs before the batch. | `_unresolved_reason`; `_symbol_locator`; `bound_definitions`; `_occurs`; `_observe`; `_author_routes` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1637-1677; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1868-1911; mcp/src/agents_remember/memory_quality/style/citations/extents.py:107-131; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1970-1980; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1989-2033; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2097-2125 |
| **The CYCLE-01 continuity cases, merged into one class because the unit ceiling is a hard 2300**: one namespace per repository read at two code baselines, a namespace READ from the dataset before one is derived (with an unreadable baseline falling back rather than raising), an absent candidate FORKED from the selected baseline so the prior invariant survives, an entry that declares its invariant versus one that names the predecessors it revises, and two symbols in one file as two anchors with the duplicate guard still refusing a genuine duplicate. | `RepositoryIdentityStabilityTests`; `test_repository_knowledge_continues_across_baselines_and_tasks` | mcp/tests/test_knowledge_curator_ingest_list.py:1605-1729; mcp/tests/test_knowledge_curator_ingest_list.py:1615-1729 |
| The CYCLE-01 fixture helpers: one contract that differs from its siblings only in the recorded baseline, the command names one curator entry contributes declared or revised, the fork of a selected baseline into an absent candidate, and the invariant and revision identities a candidate database actually holds. | `_cycle01_contract`; `_cycle01_command_kinds`; `_cycle01_forked_candidate`; `_cycle01_candidate_rows` | mcp/tests/test_knowledge_curator_ingest_list.py:1556-1585; mcp/tests/test_knowledge_curator_ingest_list.py:1588-1606; mcp/tests/test_knowledge_curator_ingest_list.py:1609-1620; mcp/tests/test_knowledge_curator_ingest_list.py:1623-1636 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `test_knowledge_curator_ingest_list.py.md:209` (_unresolved_reason, _symbol_locator, _symbol_language, _occurs, _observe, _author_routes) — re-read the claim against the current module: the named case was renamed or consolidated, and the successor's own docstring names the consolidation.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 4 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `test_knowledge_curator_ingest_list.py.md:198` (`entry`, `target`, `symbol`, `_range`); `test_knowledge_curator_ingest_list.py.md:205` ("test_identity_is_derived_from_the_enclosure_so_a_second_run_is_diagnosable", "test_dry_and_real_runs_report_the_same_written_rows_and_a_refused_run_reports_none", "test_an_empty_authorization_is_refused_by_name_before_anything_is_read"); `test_knowledge_curator_ingest_list.py.md:207` (`ingest_curator_list`, `IngestReport`, `IngestCounts`, `TargetOutcome`, `EntryOutcome`); `test_knowledge_curator_ingest_list.py.md:208` (`_REASON_THIRD_ROOT`, `_REASON_GONE`, `_REASON_DEPENDENCY`, `_REASON_OUTSIDE_BY_SPELLING`, `_REASON_NOT_CONFINED`, `_REASON_INSIDE_BY_SPELLING`, `_CODE_LINE_RANGE_MALFORMED`, `_CODE_LINE_RANGE_ORDER`, `_CODE_LINE_RANGE_ZERO_BASED`, `_CODE_LINE_RANGE_PAST_END`, `_CODE_LOCATOR_MISSING`, `_CODE_LOCATOR_KIND`, `_CODE_CONSTRUCT_ABSENT`, `_CODE_NOT_A_DEFINITION`, `_CODE_NO_DEFINITIONS_IN_PROSE`).

- 2026-09-20T02:26+02:00 — 260915-KS-L33 curator, post-sync citation pass (uncommitted change set on `ar/260915-ks-l33-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **repointed one range in the "internals that produce the pinned behaviour" row (line 247) to its construct's current extent.** This leaf's own change to `application/knowledge_curator_ingest.py` — the realization role is authored by the entry rather than inferred from the locator — moved `_author_routes` to `:2097-2125`, and the row's last range `:2062-2090` therefore no longer held the anchor it names. The range was repointed to the declaration's current extent; the Finding text, all six anchors and the row's other five ranges are unchanged. No anchor was renamed, no citation was dropped and no range was deleted. `reviewedWorkingCandidate` was moved onto this leaf's candidate `ar/260915-ks-l33-ar` on the same base, because that is the candidate this reading was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded. No commit, no verification stamp advanced, no acceptance claim made.
- 2026-09-20T01:23+02:00 — 260915-KS-L30 curator, final citation pass (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared the 17 enforced `citation_anchor_absent_from_range` rows and this card's one `citation_claim_reopened` row, by RANGE REPAIR plus STAMP ACCOUNTING.** Every flagged range was hand-read against this candidate and repointed to the declaration extent of the anchor it was written for; the pairing of a range to its anchor was fixed by the construct the range held at the revision its numbers were true at, so no citation changed which anchor it belongs to and none was dropped. What moved: (1) the leaf's-own-line row — `test_a_producer_citing_a_file_its_own_leaf_modified_gets_a_report_not_an_exception` had been given the `_commit` range it does not own (`:243-248`, still cited by the fixture-machinery row), repointed to `:569-596`, the case's own `def` through its last assertion; (2) the fifteen-constant row — `:169/:171/:170/:172/:173/:174` → `:186/:188/:187/:189/:190/:191` (the six path reasons) and `:188/:189/:190/:191/:194/:195/:196/:197/:198` → `:205/:206/:207/:208/:211/:212/:213/:214/:215` (the nine locator-or-symbol codes), the whole block sitting 24 lines below its cited values; (3) the internals row — `:1551-1591; :1782-1825; :1884-1894; :1903-1947; :1976-2004` → `:1637-1677; :1868-1911; :1970-1980; :1989-2033; :2062-2090` (a uniform 86-line move; the cross-file `bound_definitions` citation at `extents.py:107-131` already resolved and was left standing); (4) the CYCLE-01 helper row — `:1522-1551; :1554-1572; :1575-1586; :1589-1602` → `:1556-1585; :1588-1606; :1609-1620; :1623-1636` (a uniform 34-line move). The reopened claim (`_cycle01_command_kinds`, `_cycle01_forked_candidate`, `_cycle01_candidate_rows` did not exist at the recorded verification commit) was re-read at each helper and its wording is **retained**: `_cycle01_contract` still differs from its siblings in nothing but the recorded baseline, `_cycle01_command_kinds` still names the commands one entry contributes declared or revised, `_cycle01_forked_candidate` still forks a baseline into an absent candidate, and `_cycle01_candidate_rows` still reads the identities a candidate database holds. **Stamp position:** the reopened claim's evidence changed after the recorded verification and this card's body was rewritten after it (2026-09-20T00:31), so the stale `lastVerifiedCommitHash`/`lastVerifiedCommitDate` metadata rows were replaced by one `reviewedWorkingCandidate` row naming this candidate and its base; no commit hash was invented and no stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 5 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `_commit`; `test_a_path_in_the_memory_root_carries_the_memory_tree_identity`; `test_an_empty_authorization_is_refused_by_name_before_anything_is_read`; `test_identity_is_derived_from_the_enclosure_so_a_second_run_is_diagnosable`; `test_the_report_names_the_candidate_its_receipt_the_lane_and_the_exact_inputs`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): re-read this card against the CYCLE-01 repair and recorded the new cases, which **merged into one class rather than seven functions** because the unit lane's ceiling is a hard 2300 this change set had already breached: `RepositoryIdentityStabilityTests.test_repository_knowledge_continues_across_baselines_and_tasks` (lines 1615-1729) now pins one namespace per repository across two code baselines, the namespace being READ from the dataset before one is derived (with an unreadable baseline falling back instead of raising), an absent candidate FORKED from the selected baseline so the prior invariant survives in it, an entry that names its predecessors and invariant as a successor (`declares_invariant is False`, and `curator_entry_commands` then emits no `AddInvariant`) against one that declares it, and two symbols in one file as two anchors with the duplicate guard still refusing a genuine duplicate. Four helper functions carry that case (`_cycle01_contract`, `_cycle01_command_kinds`, `_cycle01_forked_candidate`, `_cycle01_candidate_rows`, lines 1522-1602). Four claims the change invalidated were corrected rather than left standing: the drive helper paragraph now says `run(...)` builds the one `IngestSelection`; the Conventions claim that the module "imports no test-support module" is false — it imports `snapshot_lifecycle_test_support` for the real candidate database — and that import is exactly why this module now carries a `consumers` row in `mcp/tests/evidence-lifecycle.toml`, which the Todos paragraph previously denied; and the identity invariant now says the repository namespace is **read** first and derived only as a cold-start fallback. The reopened `_defines`/`_code_only` claim was re-read: those helpers no longer exist anywhere in the code tree (this leaf's `_symbol_locator` calls the shipped `bound_definitions`, with `_occurs` the mention test), so the row now names the constructs that are actually there. Every other reference row was re-cited to its construct's current extent, which this leaf's 292 inserted lines moved. No verification stamp was advanced.
- 2026-09-19T17:14+02:00 — 260915-KS-L28 curator (sealed finding M1-5 repair): created this
  one-to-one card for `mcp/tests/test_knowledge_curator_ingest_list.py`. It records the list-level
  operation — the session fixture that builds two real repositories and the leaf's own line on top of
  the recorded base, the hand-off builders and the drive and measurement helpers, and the seventeen
  cases that pin the three outcomes in one report, the empty-target ruling that is skipped rather than
  filed, the leaf's added and modified files resolving against its own line, the distinct locator and
  path refusal vocabulary, the bare-symbol path from language derivation through the typed read-back to
  the rail's refusal, the definition check that refuses a mention, derived identity and the dry-run
  accounting that matches the real run, the route leg, and the report's own names. Every range is the
  construct extent at the committed revision this card names (`7e6936c0`, 2026-09-19T13:56:32+02:00),
  which is byte-identical at the code worktree HEAD `e7998504`; closeout owns the final stamps.
