# mcp/tests/test_review_sync_rebinding.py

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
(`mcp/tests/test-evidence-lanes.toml:372-373`) and as four `consumer_scope = "exact"` consumer rows in
`mcp/tests/evidence-lifecycle.toml` (`:801-803`, `:1305-1309`, `:1431-1435`, `:1477-1481`). It measures **942
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

## Evidence

### Docs References

No domain documentation source is configured for this repository — the memory layer's `system/sources.md`
records no entries at all. The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The claims on this card are checkable in the module's own docstrings, its fixture and its cases, and in
the owners those cases drive. What a reader should carry: the fixture is the product path (the endpoint
fixture's own datasets are refused by the publication route, so the leaf's halves are created through the
store); the assertions compare against the store's own reopened truth; and the four `F` cases exist
because each of them pins one sentence a verifier could otherwise reproduce as false.

- **The module's own frame: the file-size seam, and that the four cases drive the real managed path with nothing injected.** [1]
- The sibling that keeps every pre-existing managed-sync case, which is why the seam falls here. [2]
- The two review identities, the candidate-only invariant that makes the halves different datasets, and the two fixed row identities the union case uses. [3]
- **The enclosure itself: the shipped endpoint fixture's pair, the authority binding, the store-created review datasets.** [4]
- The MCP authority the tool's own contract admission reloads, written and loaded by the fixture. [5]
- The authored common ancestor a three-way knowledge merge needs, and its adoption as review candidate and published line. [6]
- The two ways the official line is advanced here: a committed leaf candidate, and a source-branch action that restores the previous checkout. [7]
- **The real freeze and the real publication owners at the read route's own declared location.** [8]
- The production sync tool, and the owners the cases read the store back with. [9]
- **Case 1: the moved official line measured against the reviewed generation, the real merge parents, the byte-identical judged manifest, and the durable read-back.** [10]
- **Case 2: the conforming example — a real union, both sides' changes surviving, the parked WIP returned with no stash entry left.** [11]
- **The two-sided divergence stage, including the store's own derived lock kept out of the park/restore path.** [12]
- **Case 3: the eight forged verdict shapes the record's own validator refuses, in the order the case checked them.** [13]
- **The validator's blind spot, pinned against the sealed manifest instead: a forged reviewed identity stops describing the generation.** [14]
- `F1`: the four states that carried nothing each name their own store fact, and the durable location stays empty. [15]
- `F2`: the state where the head does not carry the add-all capture, and the wording that locates it instead. [16]
- `F3`: no generation and an unreadable generation store are two states, with the selection owner's sentence kept under its own key. [17]
- `F4`: the named reclamation owner removes the record, and the reader reports an empty location that says which fact it observed. [18]
- The helpers the cases read the dataset, the publication admission and Git with. [19]
- **The sync-side owner's own statement of what it measures, that it re-implements no owner, and that nothing there can refuse a sync.** [20]
- **The three carrying states, and the table of every state that carried nothing with the reason no pair was resolved.** [21]
- **The success conjunct and its own stated reason for existing, which `G2` on the sibling module pins.** [22]
- One durable file per leaf and judged generation, under the shipped reports root. [23]
- **The recorder: the store's own selection, the resolved capture, the sealed manifest, and the published record with its read-back.** [24]
- **The never-raising entry point the sync tool calls, with each state it can report instead of raising.** [25]
- The reader's three states, its sentence, and its own statement that a discarded record and one never written read the same. [26]
- **The half that compares a record against the generation store rather than against itself.** [27]
- The named reclamation owner, and its own statement that no mounted tool calls it yet. [28]
- **R22's own words for a carried pair with no measurable generation, and the selection owner's answer carried under its own keys.** [29]
- Assembly that selects nothing and re-derives no reviewed value, asking the vocabulary for the channel matches and the verdict. [30]
- The resolved knowledge channel read through the route a later reader selects its knowledge with. [31]
- The record's own version, selection rule, channel-match vocabulary and three-valued verdict. [32]
- The one verdict rule, stated once so a writer and the record's validator cannot disagree. [33]
- **The validator the eight forgeries are aimed at: every verdict re-derived from the identities the record carries.** [34]
- **The clause `F2` pins: the head locates the capture, it does not carry it.** [35]
- **The production call site: the rebinding is attached to the tool result after the transaction has finished and the contract is written.** [36]
- The shipped capture owner that derives the resolved source side after the sync. [37]
- The freeze owner whose options name the predecessor — the operation the record's remedy names. [38]
- The generation store's own layout and manifest readers, which these cases use and never rewrite. [39]
- The durable-evidence pair every record is published and read back through. [40]
- The shipped endpoint fixture whose enclosure this module's fixture stands on. [41]
- The merge-case support whose authored identities and readers the module reuses. [42]
- The read-scope support's authorship factory both halves of every dataset are authored with. [43]
- **The module's lane row and its four exact-scope consumer rows in the evidence catalog.** [44]
- **The reopen owner's fifth channel, which is what makes this record a production read rather than a dead one.** [46]

### Cross-Repo References

No cross-repository behavior is implemented in this file. Every case builds a real enclosure, a real
generation store, a real published dataset and a real transaction inside one repository boundary; the
publication read-back consults that repository's authority home, which is exactly why the fixture creates
its datasets bound to the repository the contract names instead of reusing the endpoint fixture's
invented namespace.

No meaningful cross-repo references found.
