# mcp/tests/test_knowledge_curator_ingest_list.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

**`260921-ICR-L18` extracted one case out of this module and this card records that, not a re-reading.**
The write site's own byte precondition moved to
[`test_knowledge_ingest_failure_windows.py`](test_knowledge_ingest_failure_windows.py.md) with the
placement owner it measures, and this file's own note where it stood (`:2404-2409`) says so — except
that the note names `test_knowledge_ingest_comparison_generation.py` as the destination, which is where
the case first landed before the failure surface was extracted again; the case lives in the
failure-window module, and that discrepancy is recorded here rather than silently reconciled. The file
is **3162 lines** where this card last measured 3192, a net **−30** that is extraction, never growth.
Because that is the only change, **every range in this card was re-derived against the moved file**
(everything above the removal moved by −1, everything below it by −30) rather than carried.

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
- **identity measured rather than assumed**, so a repeat of one creation operation resolves to the
  identities that operation already holds and files no second record, while a dry run reports the
  counts the real run would write;
- **the route leg**, the one part of the citation the closed command union cannot carry.

This leaf (`260921-ICR-L5`) adds a seventh: **the before half a cold-start run has to leave behind.**
The defect these cases seal is the packet's own: a fresh CLI ingest with no `--baseline` committed its
candidate and left the review's before half absent, and the review then refused the missing half — so
the first invariant a repository ever recorded could not be displayed as an addition at all. The
tempting repair is the wrong one the requirement names, and these cases measure the difference: the
half is *established* and *identified* (an empty dataset in the candidate's own namespace plus an origin
record that says which generation it is and that pre-feature history was not recorded), while a fork
point the caller *named* that is missing or corrupt is refused by name and establishes nothing. Eight
cases carry it, each a distinct user operation rather than a variation: the cold-start run itself, the
pair that run then reviews, the non-conforming selected-baseline case (both ways an input can be
unavailable), the initialization failure that must claim nothing, the resume run that names an
unreadable baseline, the damaged half, the later selected baseline that must not replace an identified
generation, and the write site's own byte precondition (driven directly, because the operation refuses
an unreadable selected baseline earlier — the right order, and also why a CLI-level case cannot reach
that rule).

The CYCLE-01 repair added a sixth: **repository knowledge that is continuous across tasks and code
baselines** — one namespace per repository (read from the dataset that already stores it, derived only
as a cold-start fallback), an absent candidate forked from the selected baseline instead of created
empty, an entry that names the invariant and predecessors it revises instead of re-declaring an
invariant the batch refuses to create, and several anchors in one source file rather than one. Those
cases live in `RepositoryIdentityStabilityTests`. **CYCLE-01's close-out then changed what continuity
is**: the continuity those cases measure is the *baseline fork* plus **explicitly naming the stored
identity**, not a reused local label resolving to one record. `R-LOCAL` is a local hand-off label; two
independent tasks numbering an entry that way are two creation operations, they mint two distinct
truths, and the next task continues one of them by naming its stored `invariant_id` (or reusing a
stored anchor through a target's `anchor_id`).

This leaf closes the three points the follow-up review kept open, and it adds no collected case to do
it. (f) The identities the **write path** stores now distinguish two constructs of one file:
`_target_identities` mints the anchor from the **allocated revision id** with the locator's qualified
name as the in-creation disambiguator, and the claim from its own revision-plus-anchor edge, while the
route stays one scope per path. (g) The **public operation** commits, forks and publishes for real: the
journey drives `ingest_curator_list` with a selected `baseline` against a real SQLite store and reads
back the rows the next task's candidate and the published dataset actually hold. (h) **A reused local
hand-off label is not an identity input, and naming the stored identity is what continuity is.**
`_cycle01_reused_label_identity` used to assert the opposite — that one reused label at two baselines
mints ONE record, "which is what lets the next task find what the previous one recorded" — and the
developer's 2026-09-20 ruling measured that reading and rejected it. The case now publishes one
baseline, cuts **two sibling enclosures that differ in nothing but their leaf id**, ingests an entry
labelled `R-LOCAL` with a different statement in each, and asserts the two stored invariant ids and
the two stored revision ids **differ**; a third enclosure then names the first side's stored
`invariant_id` and must evolve *that* record, keeping its identity and filing a distinct revision with
its own predecessor edge. The old assertion's legitimate concern — the next task must be able to find
what the previous one recorded — is still proved, by the route that actually provides it. The new
statements are plain functions called from inside the existing case — `_cycle01_public_identities` at
its end — because both lanes sit at exactly their budget (2300 / 2300 unit and 400 / 400 integration)
and one added collected case makes the lane execute zero tests.

The properties matter because this operation is the boundary between an unlanded leaf's own work and
the recorded knowledge plane. A curator that resolved against the recorded base would refuse the leaf's
own deliverable as *gone*; a run that raised instead of reporting would leave the hand-off unauditable;
and a reason whose words are true of only one failure would tell a producer to search somewhere else
instead of what to fix.

## Code Commentary

### Logic

The shared handoff builder now supplies explicit semantic applicability, conditions and exclusions. Existing tests continue to exercise their original publication, retry, lineage and refusal behavior under the current scope-required admission; the fixture does not authorize inferred or migrated scope.

Since leaf `260921-ICR-L45` the shared `entry` builder also states an **explicit entry-level
`realization_rationale` default** (`rationale=`, default "The cited place carries this obligation in the
fixture."; passing `None` omits the key). The writer refuses a new realization with no authored
rationale at either level (`realization_rationale_absent`) and no longer generates one, so the builder
supplies the default explicitly rather than relying on a writer fallback; the per-target cases live in
`test_curator_realization_authoring.py`, which reuses these builders.

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

**The first-generation group brings five helpers, and each exists because the review's before half is
derived from a contract's own recorded worktree group.** `_review_before_half(contract)` derives the
half exactly as the review derives it, so a case that read the half from anywhere else could pass while
the review still refused the pair. `_cold_start_argv(contract, listed, candidate)` is the shipped
invocation a repository's first task issues — no `--baseline` to name. `_one_entry_list(directory, name,
entry_id, symbol_name)` writes a one-entry hand-off list, and it exists because the ingest's idempotency
key is the entry's own id: a case that needs a run to **commit** writes the next id rather than
repeating one, since a repeated id replays and a replayed batch places nothing in the before half —
which would make a case about the half pass without ever reaching it. `_private_pair(root)` and
`_relocated_contract(pair, root)` give a case its **own** enclosure: the session fixture's contract is
shared by every case in the file, and the two halves are derived from the contract's recorded worktree
group, so a case that established or read a half through the shared contract would be measuring another
case's state. `_relocated_contract` moves only the four coordination cells and keeps the code and memory
lines naming the fixture's real repositories, because the case it serves is about *where* the before
half lives and not about new sources.

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
- **Identity allocated, replayed, dry runs, authorization.** `test_a_second_run_resolves_to_the_identities_the_operation_was_allocated`
  (renamed from `test_identity_is_derived_from_the_enclosure_so_a_second_run_is_diagnosable`, which
  named the rule the ruling replaced) runs the same list twice: the first commits with the anchor
  identity equal to the file's own blob, and the second is a **replay** — `batch_state == "replayed"`,
  `commands_sent == 0`, `records_written == 0`, the entry reported committed with the identities it
  already holds, and the candidate's stored row sets byte-identical — because the batch's
  insert-absence precondition would refuse the same rows, and a refusal is not what repeating an
  operation that already succeeded means.
  `test_dry_and_real_runs_report_the_same_written_rows_and_a_repeat_writes_none` (renamed from `…_and_a_refused_run_reports_none`, because the re-run it measures is now a replay rather than a refusal) asserts the dry
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
  **The same case also holds the report's description of its own identity rule to the rule**, which
  is the public half of this leaf's change: `report.code_base_commit` must not appear in
  `derived_identities`, the field must name the repository's own namespace, and the field must state
  the **split** — an allocated invariant/revision pair against derived citation identities — because
  that split is the ruling this leaf implements. The assertion exists because the field described
  uuid5 over the enclosure's recorded code base commit long after `_identity` stopped deriving from
  any commit, and a public field naming the wrong input is what misled a verification round into
  reading a minted identity as baseline-scoped; a phrase check would have passed on the old text, so
  the case checks the rule against the field's own statement of it.
- **The review's before half, five ways it can be reached, and one case that predates this leaf.**
  `test_a_refused_rerun_leaves_the_reviews_before_half_at_the_fork_point` already measured the refusal
  path at the CLI; this leaf's eight cases measure the *filling* path. The cold-start case commits a
  first obligation with no `--baseline` and asserts five things: the planning run claims nothing (a
  `not-placed` line, no candidate directory, no half); the committed run reports `established:` and the
  half exists; the half is **empty** (`_cycle01_candidate_rows` returns two empty sets, so the populated
  candidate was not copied backward as its own origin) while the candidate holds exactly one invariant
  and one revision; the half is bound to the **candidate's own namespace** and its digest differs from
  the candidate's; and the origin record names the identity actually on disk, the one state, `none` for
  the baseline this run was handed, `not-recorded` for pre-feature history, and the run's own leaf,
  contract, authorization and observed code base. It then commits a **second** obligation and asserts
  the half and the record are byte-for-byte what they were. The pair case drives the shipped
  `compose_review` over the two paths the ingest wrote — built from real namespace and tree ids, not a
  fixture payload — and measures which side the subject is on: `present` after and `absent` **before**,
  because "an empty before *side* is not an empty history". The refused-input case exercises both ways a
  *selected* fork point can be unavailable (a path that is gone, and a path holding something that is
  not a dataset) and requires `selected_input_unavailable` naming the path for both, with no candidate,
  no half and no origin, and every handed-over entry naming the same refusal. The expose-failure case
  occupies the half's own directory with foreign content, so the promote cannot replace it: the run
  commits the entry it was asked for, reports `not-established:` with the path and the reason, leaves no
  dataset and no record, leaves the foreign content exactly as it was, and leaves nothing else in the
  directory — the private stage did not survive the attempt. The resume case establishes a half, then
  re-runs with `--baseline` naming a lost or corrupt dataset and requires the half, the origin record and
  the candidate's rows all to be unchanged; before this leaf the run committed and reported
  `placed: … (captured from …/corrupt.sqlite before this run)`, leaving a damaged dataset beside an
  origin record that no longer matched it. The damaged-half case damps the half twice on one leaf — first
  with bytes that are not a dataset, then with a **readable** dataset that is simply not the one the
  record was written for — and requires `not-established` naming the path and the reason both times,
  with each damage named by its own expected phrase (`could not be read as a dataset`, then
  `logical_digest`), the half's bytes and the record untouched, and the candidate write the run *was*
  asked for still landed. The later-baseline case publishes a real dataset after the half exists,
  commits a second entry naming it, and requires the run to report `not-placed:` with "already records
  its first generation" while the half and the record stay byte-identical. The last case drives
  `_place_fork_point` directly, because the operation refuses an unreadable selected baseline before the
  write site is reached: corrupt bytes are refused by name with nothing created, a real dataset is
  written, and the retry that follows reports `present:` and restates nothing.
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
- **CYCLE-01, closed at the public boundary (this leaf).** The three points the follow-up review kept
  open are pinned from inside the same case, as calls to plain functions rather than as new collected
  cases. **(f)** `_cycle01_public_identities` asserts the identities the *write path* stores: two
  constructs of one `pkg/module.py` get two different anchor ids and two different claim ids from
  `_target_identities`, while both keep the *same* route id, because a route governs a path. The two
  ids are now keyed differently from each other and from the label: the anchor on the **allocated
  revision id** with the symbol's qualified name as the in-creation disambiguator, and the claim on its
  own revision-plus-anchor edge — which is what makes a claim a distinct realization rather than the
  same claim re-declared. **(g)**
  `_cycle01_cli_baseline_journey` drives the public operation with a selected `baseline` against a real
  SQLite store: task A commits two constructs of one file and publishes, task B forks A's dataset and
  keeps A's invariant and revisions by exact id, stores an explicit successor under the invariant it
  names with a recorded `invariant_predecessor` edge, adds an unrelated record, and republishes over the
  dataset it forked from (`previous_identity` equal to A's); afterwards the published `knowledge.sqlite`
  holds exactly the candidate's invariants and revisions, and the candidate holds four distinct anchors,
  three of them for the one file. **(h)** `_cycle01_reused_label_identity` asserts the **ruled**
  semantics and no longer the pre-ruling one: it publishes a baseline, cuts two sibling enclosures
  differing in nothing but their leaf id, ingests one entry labelled `R-LOCAL` with a different
  statement in each, and requires the two stored invariant ids and the two stored revision ids to
  **differ** — two independent tasks are two creation operations, and a label says nothing about
  whether two entries represent the same truth. It then proves the continuity the old assertion was
  reaching for, by the route that provides it: a third enclosure names the first side's stored
  `invariant_id` (and its revision as predecessor) and must evolve *that* record, keeping its identity
  and filing a distinct revision with a recorded predecessor edge. The statement that used to stand
  here — the same invariant and revision for one reused label, "which is what makes the obligation
  recorded at the first baseline findable at the second" — was true of the fixture it measured and is
  the reading the developer's ruling replaced; continuity across a task boundary is naming the stored
  identity, not reusing the label. The
  journey publishes into a private pair's memory root, so it builds its own repositories through the
  fixture's own builder (`pair.__wrapped__`) under a small private tmp factory instead of reusing the
  session pair, whose memory root the other cases read but never write.

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
- **The first-generation cases read the half through the module's own helpers and drive the shipped CLI**
  (`main`), importing only the two CLI-private callables the write-site case needs
  (`_CapturedBaseline`, `_place_fork_point`) and the before-half names the assertions compare against
  (`BASELINE_ORIGIN_NAME`, `baseline_origin_path`, plus `dataset_identity`,
  `ReviewCandidateResolution`, `ReviewSurfaceRequest` and `compose_review` for the pair case). No case
  re-implements the establishment, the placement rules or the comparison it measures.
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
- Identity is derived from the **repository** and the entry's own id rather than drawn, and the
  *resolution* tree (the leaf's own line) is kept apart from the identity: a target adds what inside
  the file the citation is about — the written path for its route, the locator's qualified name for its
  anchor and its claim — which is what makes two constructs of one file two stored records rather than
  one `source_anchor` the batch refuses. The **repository namespace** is the one identity that is not
  derived first: a run READS it from the dataset it was handed as the baseline, and derives under
  `_INGEST_NAMESPACE` from `repo_name` only when that dataset records none or cannot be read, because a
  namespace keyed on the code base commit moves with the baseline while the knowledge it scopes does not.
- **Boundary.** The route leg does not travel through the command batch — its only route member names a
  family revision — so the two legs are reported separately, and a route that cannot be recorded
  refuses the list before anything is committed. This module starts no publication and makes no
  requirement-acceptance claim of its own.

### Todos

No file-local implementation change is requested by this card. Two registration facts are recorded
rather than assumed here, and one of them corrects an earlier claim on this card:

1. The module **is** placed: `mcp/tests/test-evidence-lanes.toml:86` lists it under the
   `unit-regression` lane's `[files]` block. The earlier statement that it "still carries no placement
   in `mcp/tests/test-evidence-lanes.toml`" was false as written and is corrected here.
2. It carries **two** `consumers` rows in `mcp/tests/evidence-lifecycle.toml` — `:730` and `:1265` —
   not one; the second is the `knowledge-snapshot-lifecycle-cases` contract the Conventions section
   below describes.

The budget this leaf's eight added cases are collected under is the current declaration in
`pyproject.toml`: `unit_case_budget = 4000` (`:278`) and `integration_case_budget = 1000` (`:279`).
The "unit lane's ceiling is a hard 2300" the Purpose and case list quote is a historical figure from
an earlier series line, retained there because it is what those decisions were taken under, not the
current ceiling. No test run was executed for this card, so the eight added cases are counted from
source rather than from a collection report; that count is the owning seat's to measure.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The rows below cite the module's own constructs, the operations they drive and the vocabulary those
operations report, with each anchor resolving inside the range cited for it. Ranges are the exact
construct extents at the verification commit.

- The session fixture: a real code repository committed twice (the recorded base and the leaf's own line), a real memory repository, and the contract that names both. [1]
- The fixture's own machinery: write files, commit under a pinned identity, call Git with a hermetic environment, and write a contract carrying exactly the cells the ingest reads. [2]
- The shared handoff builders create the entry, target, symbol and line-range test inputs; the entry builder states an explicit entry-level `realization_rationale` default. [3]
- The drive and measurement helpers: ingest one list into a candidate directory the case owns — building the one `IngestSelection` the operation now takes — key one report's outcomes, and count the six written tables from the database. [4]
- **This leaf's five first-generation helpers, each existing because the review's before half is derived from an enclosure's own recorded worktree group**: the half derived as the review derives it; the shipped cold-start invocation; a one-entry list whose **id** the case chooses (a repeated id replays, and a replayed batch places nothing, so a case about the half would pass without reaching it); a private pair; and a relocated enclosure that moves only the four coordination cells. [5]
- **The cold-start user operation, five facts in one case, and the second run that must not restate what the first established.** The half is empty (the candidate's rows are not copied backward), bound to the candidate's own namespace, and identified by a record naming the identity actually on disk, `none` for the baseline this run was handed, and `not-recorded` for pre-feature history; a later committing run reports `present:` and leaves both files byte-identical. [6]
- **The half of the same operation that makes it worth anything: the shipped comparison opens the pair the ingest wrote, and the first invariant is `present` after and `absent` before.** [7]
- **The non-conforming case the requirement names, both ways an input can be unavailable**: a *selected* fork point that is gone and one that holds bytes which are not a dataset are each refused `selected_input_unavailable` naming the path, with no candidate, no before half and no origin record — the regression for a run that used to end in a traceback where a report belongs. [8]
- **Initialization failure claims nothing**: with the half's own directory occupied by foreign content the promote cannot replace, the run still commits the entry it was asked for, reports `not-established:` with the path and reason, leaves no dataset and no record, leaves the foreign content exactly as it was, and leaves nothing else behind — the private stage did not survive the attempt. [9]
- **The resume path's regression**: with a half already established, a second run naming a lost or corrupt `--baseline` refuses the selected input, commits nothing, adds no row, and leaves the half and its record byte-for-byte unchanged — where before the run committed and reported `placed: … (captured from …/corrupt.sqlite before this run)`. [10]
- **Damage named in both of its forms**: bytes that are not a dataset, and a *readable* dataset that is not the one the record names, each answer `not-established` with the path and their own phrase, leave the half and the record exactly as they are, and do not stop the candidate write the run was asked for. [11]
- **An identified first generation is never replaced by a later selected baseline**, even when the caller names a real published dataset: the entry commits, the half reports `not-placed:` with "already records its first generation", and both files stay byte-identical. [12]
- **The write site's own precondition, which this leaf MOVED OUT to `test_knowledge_ingest_failure_windows.py` with the placement owner it measures** (ICR-R18) — the right order, and also why a CLI-level case cannot reach this rule: corrupt bytes are refused by name with nothing created, a real dataset is published with the record that names its generation, and the run that follows reports `present:` and restates nothing. What stands here in its place is the note that names the move and the reason (`:2404-2409`). [13]
- The three outcomes in one report, with the ruling skipped while carrying its own verdict and the three path reasons asserted to be three distinct words. [14]
- The leaf's own line as the resolution tree: a file the leaf added commits and reads back, and a file the leaf modified produces a report rather than an exception. [15]
- The refusal vocabulary: five distinct locator failures and their distinct reasons, and every path reason read from the recorded trees rather than from the live directories. [16]
- The producer's bare symbol name end to end: a qualified name resolved by both halves with an invented prefix refused, a bare name stored and read back typed, and a definition check that refuses a mention or any other non-definition. [17]
- Working code citations bind the captured blob, while memory-path citations retain the admitted memory tree identity. [18]
- Allocation and the modes around it: a repeat of one creation operation resolves to the identities it already holds and writes nothing, a dry run's counts are the counts the real run writes, and a blank authorization is refused by name before anything is read. [19]
- The route leg and the report's own names: one row per scope with one association per governed anchor and an ungoverned anchor left ungoverned, a re-authored route reused rather than written twice, and the candidate, receipt, lane and trees the report names. [20]
- The operation under test and the report it returns: one admitted batch or a typed refusal per entry, with the three outcomes and the counts that make a run auditable kept apart — and the selection value the operation is handed, including the `baseline` it forks from. [21]
- The vocabulary this module asserts by name: the six path reasons and the nine locator-or-symbol codes its cases name, each standing for one distinct fact rather than one shared word for "did not resolve". [22]
- The internals that produce the pinned behaviour: the reason classifier read from the recorded trees, the symbol resolution, its language gate and its definition check, the occurrence test that separates a definition from a mention, the observation gate that accepts a symbol only on the rail's own answer, and the route leg that runs before the batch. [23]
- The internals that produce the pinned behaviour: the reason classifier read from the recorded trees, the symbol resolution and its definition check — which is the shipped `bound_definitions`, because this module no longer carries its own blanking pass or `_defines`/`_code_only`, with `_occurs` the mention test that separates a non-definition from an absent construct — the observation gate that accepts a symbol only on the rail's own answer, and the route leg that runs before the batch. [24]
- **The CYCLE-01 continuity cases, merged into one class because the unit ceiling is a hard 2300**: one namespace per repository read at two code baselines, a namespace READ from the dataset before one is derived (with an unreadable baseline falling back rather than raising), an absent candidate FORKED from the selected baseline so the prior invariant survives, an entry that declares its invariant versus one that names the predecessors it revises, two symbols in one file as two anchors with the duplicate guard still refusing a genuine duplicate, and — this leaf — the identities the write path stores, the public journey its own call now runs, and the sibling-identity check that proves a reused label is not an identity input. [25]
- The CYCLE-01 fixture helpers: one contract that differs from its siblings only in the recorded baseline, the command names one curator entry contributes declared or revised, the fork of a selected baseline into an absent candidate, and the invariant and revision identities a candidate database actually holds. [26]
- **The public-operation journey this leaf added, and the ruled semantics this leaf re-pointed it at (no collected case was created for either — both lanes sit at exactly their budget).** `_cycle01_public_identities` is the entry point the existing case calls: it asserts the three write-path identities of two constructs in one file, then runs the CLI journey and the reused-label check. `_cycle01_cli_baseline_journey` builds a private pair, publishes task A, forks task B from that dataset and measures the consequences from the databases themselves. `_cycle01_reused_label_identity` is the re-pointed one: with the three helpers this leaf wrote for it — `_cycle01_sibling_contract` (a second enclosure differing from the fixture's only in its recorded `leaf_id`, which is the retry key's scope), `_cycle01_publish_baseline` (one baseline truth published through the public operation) and `_cycle01_revisions_of` (every revision one invariant holds, read from the database) — it measures two sibling enclosures, one reused label, two different statements, distinct stored identity pairs, and continuity proved by a third enclosure **naming** the first side's stored invariant. Those three helpers are **this leaf's own work, and they do exist at the commit this card is verified against** — `4ef4dddc`, which contains this leaf's whole change set — so a reader can resolve them there; they are named in this sentence rather than in the Anchor cell because they are part of what the claim describes measuring rather than further evidence for it, and because a reader working from an earlier revision will not find them at all. [27]
- **The journey's two tasks, and what each one is allowed to prove.** Task A commits two constructs of one file and publishes; task B names the baseline it forks from, keeps the prior invariant and revisions by exact id, stores an explicit successor under that invariant, adds an unrelated record, and republishes over the dataset it forked from. [28]
- **The journey's measurements, read from the candidate and the published dataset rather than from the report.** `_cycle01_baseline_consequences` asserts the baseline containment, the successor revision, the four distinct anchors and the predecessor edge; the three readers below it read revisions-by-label, anchors and predecessor edges out of SQLite. [29]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

| **A refused re-run leaves the review's before half at the fork point.** The user operation: author the entry, publish over the dataset the leaf forked from, then re-run the SAME hand-off entry with a changed statement. The write plane correctly refuses that second run, and the case measures three facts — the publishing run still places the fork point, the refused run reports `not-placed` and leaves the half byte-identical to the fork point, and the review still reads the addition `absent` before and `present` after over two different digests. It seals the refusal-path defect: placement gated on batch state alone re-placed the before half, once the leaf had published over its own fork point, from the captured bytes — which by then are the PUBLISHED dataset. | `test_a_refused_rerun_leaves_the_reviews_before_half_at_the_fork_point` | mcp/tests/test_knowledge_curator_ingest_list.py:1789-1880 |
