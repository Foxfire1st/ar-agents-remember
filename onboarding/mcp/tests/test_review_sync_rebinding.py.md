# mcp/tests/test_review_sync_rebinding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_sync_rebinding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T17:15:00+02:00 |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d` |
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

**ICR-R22@v1's sync-side case evidence: what a managed sync measures about the review it moved.** The
leaf `260921-ICR-L22` makes a completed `worktree_sync` measure the source/knowledge pair it resolved
against the comparison generation the leaf published, publish one durable
`ar-review-sync-rebinding/v1` record, and render that measurement on the live review read. This module
owns the sync half and the read half's sibling (`test_review_sync_movement_read.py`) owns what the read
renders. Every case here drives the production path — `worktree_tools.worktree_sync_tool`, the real
transaction, the real binary-stage knowledge merge, the real publication owner and the real
comparison-generation owner — and then compares the record against the store's own reopened truth
(`read_manifest`, `read_review_sync_rebinding`, `git rev-list --parents`, `dataset_identity`) rather than
against the response that carried it. **Nothing here injects a resolution, a payload or a prebuilt
record.**

`ReviewSyncFixture` (`:102-112`) is the enclosure: the shipped endpoint fixture's own pair, plus the
three things a managed sync needs on top of it — an MCP configuration bound to the enclosure's
coordination root, one published lifecycle-operation location, and two review datasets created through
the store's own API in the leaf's disposable knowledge root.

The module holds **seven** case methods. Its docstring frames **four**, and the four later cases carry
their own `F1`–`F4` labels in their docstrings, so the two counts are both in the bytes:

| Property | Case |
| --- | --- |
| the moved official line is measured against the reviewed generation, and the judged generation keeps every byte | `test_official_source_movement_is_measured_against_the_reviewed_generation` (`:391`) |
| the conforming example — a real knowledge union, the parked WIP handed back, the union measured | `test_clean_knowledge_union_is_measured_and_the_parked_wip_returns` (`:466`) |
| the record refuses eight forged verdict shapes, and identity forgery is caught against the manifest instead | `test_a_forged_rebinding_verdict_is_refused_by_the_record_itself` (`:514`) |
| `F1` — the four states that carried nothing each name the store fact they observed, and none writes a durable record | `test_every_state_that_carried_nothing_says_which_one_it_is` (`:635`) |
| `F2` — the source clause locates the capture at the head instead of claiming the head carries it | `test_the_source_clause_names_a_locator_not_a_carrier` (`:695`) |
| `F3` — no generation and an unreadable generation store are two states, neither the reader's `unreadable` | `test_a_carrying_sync_without_a_measurable_generation_says_which` (`:735`) |
| `F4` — after its own reclamation the reader reports an empty location, not a history claim | `test_the_reader_observes_the_location_after_its_own_reclamation` (`:779`) |

## Code Commentary

### Logic

**The fixture is authority and store, and the datasets it creates are the product path.** The enclosure
is `build_endpoint_fixture(root / "endpoint", memory_mode="external")` (`:115`), and the fixture adds a
symlink from the coordination root to the code repository (`:118-120`), the MCP settings file the tool's
own contract admission reloads (`_bind_authority`, `:147-163`) and one published lifecycle-operation
location (`:126-129`). `_seed_review_datasets` (`:165-222`) deliberately does **not** use the endpoint
fixture's own datasets: it creates the leaf's two halves through the store's API inside the leaf's
disposable knowledge root, because a dataset bound to another repository's authority home is another
repository's publication and the publication route rightly refuses it. The two halves differ by
`CANDIDATE_ONLY_INVARIANT_ID` (`:92`) on purpose, "so the two review halves are different datasets rather
than two spellings of one".

**Everything downstream of the fixture is a shipped owner.** `build_knowledge_base` (`:224-270`) authors
a real common ancestor for the three-way knowledge merge; `commit_leaf_candidate` (`:283-295`) puts the
leaf's candidate on the record the way a real leaf reaches a sync; `on_official_line` (`:297-315`)
checks one repository out on its **recorded** source branch, runs the action and restores the previous
checkout, so no case depends on which branch happened to be checked out. `freeze_review` (`:325-331`)
calls the real `freeze_review_comparison` and requires `published`; `publish_reviewed_candidate`
(`:333-358`) installs the compared dataset at `declared_publication_location` through
`freeze_closed_snapshot` + `publish_prepared_snapshot`; `sync` (`:360-365`) is the production tool;
`capture_tree` (`:370-373`) is the capture owner; `generation_directory` (`:375-378`) is the
generation store's own layout owner. The helpers only *address* the operation.

**Movement is measured, and the record is read back rather than believed.** Case `:391-465` asserts the
wire block's every identity — `state == "moved"`, `covers_resolved_pair is False`, the two channel
matches, both reviewed identities, the generation id and binding digest, `resolved_code_head` against the
worktree's own `HEAD`, `resolved_candidate_code_tree_id` against `fixture.capture_tree()` and
`read_back == "matched"` — and then proves the resolved pair is a real merge: `git rev-list --parents -n 1
HEAD` has exactly the recorded pre-sync head and the moved official tip as parents. The judged generation
is then read off disk and compared byte-for-byte with the manifest the freeze returned, and the durable
record is re-read through `read_review_sync_rebinding` (`:455-465`). **Recording movement is not the act
of publishing a successor.**

**The conforming example is a real union with the curator's WIP handed back.** `stage_knowledge_divergence`
(`:870-921`) authors the base, commits it onto the official memory line, bootstraps it into the leaf's own
memory line through an ordinary sync, records the store's own derived lock file in `.gitignore` so the
park/restore path never has to reapply a file it must not overwrite, freezes and publishes the review
while the base is still the compared dataset, and only then diverges left (a label) and right (an anchor).
The case parks one file, and asserts both sides' changes survived the union, the parked bytes came back
exactly, `git stash list` is empty, the record measures the dataset now standing at the declared location
(`assert_rebinding_measures_the_location`, `:853-867`), and the judged generation is untouched.

**The forgery case has two halves, and the second one is the validator's blind spot.** Eight mutations of
a real published record are refused by the record's own validator — the verdict, each channel, both
channels plus the verdict together, the reviewed knowledge state, both knowledge fields, the dropped
dependency, and an identity beside a location reported as holding nothing — and the case asserts the
label list it checked in order, so a clause that stops refusing fails by name (`:544-614`). Then it pins
the half a self-consistent forgery defeats: a record whose reviewed identity is replaced by `"0" * 40`
still validates, and only `rebinding_names_the_generation` against the sealed manifest refuses it
(`:620-633`).

**The four later cases each pin one sentence.** `F1` (`:635-693`) drives the four states that carried
nothing — `already-current`, a genuine dry-run preview, a retained source conflict and its supported
cancellation — and requires each block to name its own store fact while the durable destination
(`durable_reports_root(...) / rebinding_file_name(...)`, `:649-651`) stays absent for all four. `F2`
(`:695-733`) reproduces the state where the add-all capture does **not** equal the head's tree and asserts
the sentence locates the capture at the head instead of claiming the head carries it. `F3` (`:735-777`)
separates "never reviewed" from "an unreadable generation store", keeping the selection owner's own
sentence under its own key. `F4` (`:779-818`) discards the record through its named reclamation owner and
requires the reader to report an empty location that says so.

### Conventions

The module docstring (`:1-14`) states the file-size seam: these cases live beside
`test_worktree_sync.py` rather than inside it because that module was already in the 900-line soft band
and the sibling keeps every pre-existing managed-sync case, so each module is one intent. Imports are
absolute through the `MCP_SRC` path insert (`:28-29`); the owner under test is imported from
`agents_remember.application.review_sync_rebinding` (`:51-56`) and support comes from sibling modules —
`merge_case_test_support` (`:82`), `read_scope_test_support` (`:84`) and the endpoint fixture's own module
(`:85`). Fixtures are plain classes and module-level helpers rather than pytest fixtures, because they
build one enclosure value the cases address. The module is registered as one `integration` lane row
(`mcp/tests/test-evidence-lanes.toml:299-302`) and as four `consumer_scope = "exact"` consumer rows in
`mcp/tests/evidence-lifecycle.toml` (`:801-803`, `:1305-1309`, `:1431-1435`, `:1477-1481`), whose added
rows move the catalog digest pinned in `test_dependency_ownership_ast_helpers.py:46`. It measures **942
lines**, inside the 1200-line hard rail, and adds no `# noqa` and no timers.

### Invariants And Boundaries

- **No case asserts a prebuilt payload.** Every identity is checked against the store's own answer: the
  sealed manifest re-read from disk, the reader's own state and sentence, `git rev-list --parents`, the
  dataset's identity, and the labels and anchors read out of the database itself.
- **Recording movement is not publishing a successor.** Cases `:391` and `:466` both assert the judged
  generation's manifest still dumps byte-identically after the sync; the successor is named as an action,
  never performed here.
- **The rebinding is not a gate.** Every state these cases measure reports `ok is True` on the sync
  payload — `moved` in cases `:391` and `:466`, `already-current` and a dry-run preview in `F1`, and
  `no-generation` and `generation-unreadable` in `F3` — because the owner's never-raising entry point is
  what the tool calls, after the Git transaction and the contract write. The one `ok is False` payload here
  is `F1`'s retained conflict, which the block reports as `not-resolved` instead of measuring anything.
- **Boundary: `F3`'s docstring names three generation-store states and the case drives two.** No
  generation and an unreadable store are driven; the third, an ambiguous tie, is covered by the owner's
  own table (`"generation-selection-ambiguous"`, `application/review_sync_rebinding.py:597-638`) and is
  **not** driven by any case in this module.
- **Boundary: the record's validator cannot refuse a forged identity carried beside a matching verdict.**
  That is by design — comparing two fabricated identities is still a comparison — and the case pins
  `rebinding_names_the_generation` as the half that compares against the sealed manifest instead.
- **Boundary: one durable file per (leaf, generation).** The record's location is
  `rebinding_file_name(leaf_id, generation_id)` under the shipped durable reports root, so the four
  not-carried states assert an absent file rather than an absent directory.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository — the memory layer's `system/sources.md`
records no entries at all. The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The claims on this card are checkable in the module's own docstrings, its fixture and its cases, and in
the owners those cases drive. What a reader should carry: the fixture is the product path (the endpoint
fixture's own datasets are refused by the publication route, so the leaf's halves are created through the
store); the assertions compare against the store's own reopened truth; and the four `F` cases exist
because each of them pins one sentence a verifier could otherwise reproduce as false.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own frame: the file-size seam, and that the four cases drive the real managed path with nothing injected.** | `worktree_sync` | mcp/tests/test_review_sync_rebinding.py:1-14 |
| The sibling that keeps every pre-existing managed-sync case, which is why the seam falls here. | `WorktreeSyncTests` | mcp/tests/test_worktree_sync.py:493-900 |
| The two review identities, the candidate-only invariant that makes the halves different datasets, and the two fixed row identities the union case uses. | `CANDIDATE_ONLY_INVARIANT_ID`; `CONFLICT_ANCHOR_ID`; `CASE_ANCHOR_ID`; `NEWLINE` | mcp/tests/test_review_sync_rebinding.py:92-92; mcp/tests/test_review_sync_rebinding.py:95-95; mcp/tests/test_review_sync_rebinding.py:98-99 |
| **The enclosure itself: the shipped endpoint fixture's pair, the authority binding, the store-created review datasets.** | `ReviewSyncFixture`; `_seed_review_datasets` | mcp/tests/test_review_sync_rebinding.py:102-378; mcp/tests/test_review_sync_rebinding.py:165-222 |
| The MCP authority the tool's own contract admission reloads, written and loaded by the fixture. | `_bind_authority`; `load_config`; `publish_new_lifecycle_operation_location` | mcp/tests/test_review_sync_rebinding.py:126-126; mcp/tests/test_review_sync_rebinding.py:147-163 |
| The authored common ancestor a three-way knowledge merge needs, and its adoption as review candidate and published line. | `build_knowledge_base`; `adopt_base_dataset` | mcp/tests/test_review_sync_rebinding.py:224-270; mcp/tests/test_review_sync_rebinding.py:272-281 |
| The two ways the official line is advanced here: a committed leaf candidate, and a source-branch action that restores the previous checkout. | `commit_leaf_candidate`; `on_official_line` | mcp/tests/test_review_sync_rebinding.py:283-295; mcp/tests/test_review_sync_rebinding.py:297-315 |
| **The real freeze and the real publication owners at the read route's own declared location.** | `freeze_review`; `publish_reviewed_candidate`; `declared_publication_location`; `publish_prepared_snapshot` | mcp/tests/test_review_sync_rebinding.py:325-331; mcp/tests/test_review_sync_rebinding.py:333-358 |
| The production sync tool, and the owners the cases read the store back with. | `worktree_sync_tool`; `capture_tree`; `generation_directory` | mcp/tests/test_review_sync_rebinding.py:363-363; mcp/tests/test_review_sync_rebinding.py:370-373; mcp/tests/test_review_sync_rebinding.py:375-378 |
| **Case 1: the moved official line measured against the reviewed generation, the real merge parents, the byte-identical judged manifest, and the durable read-back.** | `test_official_source_movement_is_measured_against_the_reviewed_generation`; `read_review_sync_rebinding` | mcp/tests/test_review_sync_rebinding.py:391-464 |
| **Case 2: the conforming example — a real union, both sides' changes surviving, the parked WIP returned with no stash entry left.** | `test_clean_knowledge_union_is_measured_and_the_parked_wip_returns`; `assert_rebinding_measures_the_location` | mcp/tests/test_review_sync_rebinding.py:466-512; mcp/tests/test_review_sync_rebinding.py:853-867 |
| **The two-sided divergence stage, including the store's own derived lock kept out of the park/restore path.** | `stage_knowledge_divergence`; `.knowledge.sqlite.lock` | mcp/tests/test_review_sync_rebinding.py:870-921 |
| **Case 3: the eight forged verdict shapes the record's own validator refuses, in the order the case checked them.** | `test_a_forged_rebinding_verdict_is_refused_by_the_record_itself`; `"dependency_dropped"` | mcp/tests/test_review_sync_rebinding.py:514-633 |
| **The validator's blind spot, pinned against the sealed manifest instead: a forged reviewed identity stops describing the generation.** | `rebinding_names_the_generation` | mcp/tests/test_review_sync_rebinding.py:620-633 |
| `F1`: the four states that carried nothing each name their own store fact, and the durable location stays empty. | `test_every_state_that_carried_nothing_says_which_one_it_is`; `rebinding_file_name` | mcp/tests/test_review_sync_rebinding.py:635-693 |
| `F2`: the state where the head does not carry the add-all capture, and the wording that locates it instead. | `test_the_source_clause_names_a_locator_not_a_carrier` | mcp/tests/test_review_sync_rebinding.py:695-733 |
| `F3`: no generation and an unreadable generation store are two states, with the selection owner's sentence kept under its own key. | `test_a_carrying_sync_without_a_measurable_generation_says_which`; `"none holds a readable manifest"` | mcp/tests/test_review_sync_rebinding.py:735-777 |
| `F4`: the named reclamation owner removes the record, and the reader reports an empty location that says which fact it observed. | `test_the_reader_observes_the_location_after_its_own_reclamation`; `discard_review_sync_rebindings` | mcp/tests/test_review_sync_rebinding.py:779-818 |
| The helpers the cases read the dataset, the publication admission and Git with. | `anchor_paths_of`; `admitted_destination_identity`; `git` | mcp/tests/test_review_sync_rebinding.py:821-837; mcp/tests/test_review_sync_rebinding.py:840-850; mcp/tests/test_review_sync_rebinding.py:934-938 |
| **The sync-side owner's own statement of what it measures, that it re-implements no owner, and that nothing there can refuse a sync.** | `discard_review_sync_rebindings` | mcp/src/agents_remember/application/review_sync_rebinding.py:505-528 |
| **The three carrying states, and the table of every state that carried nothing with the reason no pair was resolved.** | `_CARRYING_SYNC_STATES`; `_CARRIED_NOTHING` | mcp/src/agents_remember/application/review_sync_rebinding.py:155-161; mcp/src/agents_remember/application/review_sync_rebinding.py:167-193 |
| **The success conjunct and its own stated reason for existing, which `G2` on the sibling module pins.** | `resolved_pair_completed` | mcp/src/agents_remember/application/review_sync_rebinding.py:196-220 |
| One durable file per leaf and judged generation, under the shipped reports root. | `rebinding_file_name` | mcp/src/agents_remember/application/review_sync_rebinding.py:265-268 |
| **The recorder: the store's own selection, the resolved capture, the sealed manifest, and the published record with its read-back.** | `record_review_sync_rebinding`; `select_review_generation` | mcp/src/agents_remember/application/review_sync_rebinding.py:271-313 |
| **The never-raising entry point the sync tool calls, with each state it can report instead of raising.** | `rebinding_result_block` | mcp/src/agents_remember/application/review_sync_rebinding.py:316-373 |
| The reader's three states, its sentence, and its own statement that a discarded record and one never written read the same. | `read_review_sync_rebinding` | mcp/src/agents_remember/application/review_sync_rebinding.py:376-438 |
| **The half that compares a record against the generation store rather than against itself.** | `rebinding_names_the_generation` | mcp/src/agents_remember/application/review_sync_rebinding.py:441-476 |
| The named reclamation owner, and its own statement that no mounted tool calls it yet. | `discard_review_sync_rebindings` | mcp/src/agents_remember/application/review_sync_rebinding.py:505-528 |
| **R22's own words for a carried pair with no measurable generation, and the selection owner's answer carried under its own keys.** | `_no_generation_block`; `"generation-selection-ambiguous"` | mcp/src/agents_remember/application/review_sync_rebinding.py:597-638 |
| Assembly that selects nothing and re-derives no reviewed value, asking the vocabulary for the channel matches and the verdict. | `_assemble`; `code_channel_match`; `review_sync_verdict` | mcp/src/agents_remember/application/review_sync_rebinding.py:641-678 |
| The resolved knowledge channel read through the route a later reader selects its knowledge with. | `_resolved_knowledge`; `resolve_published_intent` | mcp/src/agents_remember/application/review_sync_rebinding.py:703-727 |
| The record's own version, selection rule, channel-match vocabulary and three-valued verdict. | `REVIEW_SYNC_REBINDING_VERSION`; `ReviewSyncRebindingVerdict` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:76-78; mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:97-97 |
| The one verdict rule, stated once so a writer and the record's validator cannot disagree. | `review_sync_verdict`; `knowledge_channel_match` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:120-139; mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:142-161 |
| **The validator the eight forgeries are aimed at: every verdict re-derived from the identities the record carries.** | `_the_rebinding_agrees_with_itself` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:242-300 |
| **The clause `F2` pins: the head locates the capture, it does not carry it.** | `_code_clause` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:342-363 |
| **The production call site: the rebinding is attached to the tool result after the transaction has finished and the contract is written.** | `rebinding_result_block` | mcp/src/agents_remember/application/worktree_tools.py:378-378 |
| The shipped capture owner that derives the resolved source side after the sync. | `capture_future_code_candidate` | mcp/src/agents_remember/worktrees/modules/future_code_candidate.py:25-52 |
| The freeze owner whose options name the predecessor — the operation the record's remedy names. | `ComparisonFreezeOptions`; `freeze_review_comparison` | mcp/src/agents_remember/application/review_comparison_freeze.py:147-160; mcp/src/agents_remember/application/review_comparison_freeze.py:233-252 |
| The generation store's own layout and manifest readers, which these cases use and never rewrite. | `leaf_generation_root`; `generation_directory`; `read_manifest`; `COMPARISON_MANIFEST_NAME` | mcp/src/agents_remember/application/review_comparison_generation.py:126-126; mcp/src/agents_remember/application/review_comparison_generation.py:501-504; mcp/src/agents_remember/application/review_comparison_generation.py:507-510; mcp/src/agents_remember/application/review_comparison_generation.py:586-620 |
| The durable-evidence pair every record is published and read back through. | `durable_reports_root`; `publish_durable_evidence`; `read_back_evidence` | mcp/src/agents_remember/memory/knowledge/durable_evidence.py:58-69; mcp/src/agents_remember/memory/knowledge/durable_evidence.py:137-166; mcp/src/agents_remember/memory/knowledge/durable_evidence.py:169-203 |
| The shipped endpoint fixture whose enclosure this module's fixture stands on. | `build_endpoint_fixture` | mcp/tests/test_knowledge_review_source_endpoints.py:220-252 |
| The merge-case support whose authored identities and readers the module reuses. | `BASE_REVISION_ID`; `set_label`; `add_anchor`; `labels_of` | mcp/tests/merge_case_test_support.py:54-54; mcp/tests/merge_case_test_support.py:309-314; mcp/tests/merge_case_test_support.py:323-338; mcp/tests/merge_case_test_support.py:635-644 |
| The read-scope support's authorship factory both halves of every dataset are authored with. | `make_read_authorship` | mcp/tests/read_scope_test_support.py:246-256 |
| **The module's lane row and its four exact-scope consumer rows in the evidence catalog.** | "mcp/tests/test_review_sync_rebinding.py" | mcp/tests/test-evidence-lanes.toml:311-311 |
| The catalog digest the added consumer rows move, pinned by the structural check. | `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:46-46 |
| **The reopen owner's fifth channel, which is what makes this record a production read rather than a dead one.** | `read_review_sync_rebinding`; `sync_rebinding` | mcp/src/agents_remember/application/review_comparison_reopen.py:68-71; mcp/src/agents_remember/application/review_comparison_reopen.py:202-202; mcp/src/agents_remember/application/review_comparison_reopen.py:378-378 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every case builds a real enclosure, a real
generation store, a real published dataset and a real transaction inside one repository boundary; the
publication read-back consults that repository's authority home, which is exactly why the fixture creates
its datasets bound to the repository the contract names instead of reusing the endpoint fixture's
invented namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **citation re-anchoring and history only; no claim wording changed and no row deleted.** This leaf's change set moved the lines several of this card's rows cite — `mcp/src/agents_remember/application/knowledge_curator_ingest.py` grew 3587 → 3861 while `mcp/tests/test-evidence-lanes.toml` gained one `unit-regression` row and `mcp/tests/evidence-lifecycle.toml` gained two consumer rows, each shifting every row below it — so every affected range was re-derived against the candidate's own bytes rather than shifted by a remembered delta and re-anchored to the construct it names. Nothing in the body above was deleted to clear a finding, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-23T17:15:00+02:00 — 260921-ICR-L22 curator (uncommitted change set on `ar/260921-icr-l22`, base `e605822eb3bf83bf63a45963c5f51d5fc28859ee`): created this one-to-one card for the module this leaf introduced as **ICR-R22@v1**'s sync-side case evidence — the managed sync that measures the source/knowledge pair it resolved against the comparison generation the leaf published and records the measurement as one durable `ar-review-sync-rebinding/v1` artifact. It records what the cases actually prove: `ReviewSyncFixture` is the product path (the enclosure is the shipped endpoint fixture's own, but the leaf's two review datasets are created through the store, because a dataset bound to another repository's authority home is another repository's publication and the route refuses it); `CANDIDATE_ONLY_INVARIANT_ID` makes the two halves different datasets so "the published dataset is the reviewed candidate" is a measurement rather than a file name; the assertions compare against the store's own reopened truth (the sealed manifest re-read from disk, the reader's state and sentence, `git rev-list --parents`, the dataset identity); the sync's real merge parents are asserted; and recording movement never rewrites the judged generation. Three boundaries are carried as boundaries and not as defects: `F3`'s docstring names three generation-store states while the case drives two — the ambiguous tie is covered only by the owner's table and is **not** driven here; the record's own validator cannot refuse a forged identity carried beside a matching verdict, so `rebinding_names_the_generation` against the sealed manifest is the half the case pins; and the durable location is one file per (leaf, generation), which is why the four not-carried states assert an absent file. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name this leaf's recorded base commit `e605822eb3bf83bf63a45963c5f51d5fc28859ee` because every construct cited here exists only in this leaf's uncommitted working tree — the module and its four catalog rows are not in any commit yet; what was actually read is that working tree, and the governed closeout owns the real stamp once the code commit exists.
