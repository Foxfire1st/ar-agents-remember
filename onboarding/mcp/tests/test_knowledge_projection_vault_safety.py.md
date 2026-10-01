# mcp/tests/test_knowledge_projection_vault_safety.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

**The 7 `integration` cases that carry `KS-R20@v1` §5.9 as one acceptance case end to end, plus the two
proof obligations that only real records can discharge.** The whole vault-safety contract is a single
scenario rather than a clause-by-clause suite, because a safety contract tested clause by clause is a
contract that fails in combination: one real dataset built through the public write operations, one real
projection destination, and eight checkpoints driven in sequence over the same manifest lineage, with the
exact refusal or action and the resulting manifest generation recorded for each. The remaining cases are the
two proof obligations the plan attaches to real records: the derived-artefact regeneration proof, which
deletes every projection and re-projects while showing that no canonical record changed, and the
row-and-column no-second-authority proof, which shows that no record table gained a content-address, digest
or fingerprint column and that no record identity reads the manifest's digest material. The four read-side
cases that sit between them measure the other half of the same contract over the real records: two
byte-identical runs at one snapshot and one renderer, which is the differential that makes an ordering key
recomputed from live state visible; the records-unchanged differential, which pairs an unchanged row order
with an unchanged dataset digest; the classification completeness scan over every view's serialized rows;
and the bounded-continuation walk, which reaches the rest of a selection that did not fit one page.

## Code Commentary

### Logic

**One scenario, one destination, one manifest lineage, and eight recorded checkpoints.**
`test_the_vault_safety_contract_holds_for_all_eight_checkpoints_in_one_scenario` is the case the plan's
"one acceptance case covers it" produces: it opens the destination through `_open_the_scenario`, runs
`_checkpoints_one_to_four` and `_checkpoints_five_to_eight` against the *same* root and the same manifest,
records each checkpoint's outcome in a `checkpoints` dictionary, appends the manifest generation, and then
asserts that `set(checkpoints)` equals the eight checkpoint ids plus `manifest` and that the generation is at
least two. That last assertion is the one that keeps the scenario from decaying: a checkpoint that was
deleted, renamed or silently stopped recording makes the set comparison fail, so the eight facts cannot
collapse into one behaviour seen twice. The three helpers exist because the scenario has to read as one run:
`_open_the_scenario` performs the prior generation and the user's own edits, `_checkpoints_one_to_four` and
`_checkpoints_five_to_eight` drive the eight events, and `_tree_bytes` returns every file under the
destination with its exact bytes so a prior state can be compared byte for byte rather than described.

**The eight checkpoints run in the plan's order, and each asserts the pair — the refusal or action and the
destination state it left behind.** `_open_the_scenario` writes four managed outputs and then acts as the
user: it edits `invariants/INV-014.md` and `incidents/INC-009.md`, creates its own `user-notes/note.md`, and
plants a real symlink at `knowledge` pointing outside the root; `families/GUA-010.md` is left edited by
nobody so that checkpoint 6 has an unchanged orphan to delete. Checkpoint 1 (confinement) projects
`../../etc/passwd.md` and gets `destination_escape` with the resolved root named and nothing staged.
Checkpoint 2 (collision) projects two records onto paths that differ only by case, gets
`destination_collision`, and asserts the first record's bytes were not written. Checkpoint 3 (escaping link)
projects through the symlink and one ordinary path, gets a `projected` report, and asserts the outside
directory gained nothing while the other output published and the modified file was reported. Checkpoint 4
(stage/publish) raises from the writer's publish hook after every output is staged and before the first
rename, asserts the tree's bytes are unchanged and that the staging directory does not exist. Checkpoint 5
(externally edited) finds `INV-014`'s user-edited bytes preserved, the other managed output published, and
exactly one `modified` discrepancy. Checkpoint 6 (unchanged orphan) drops `families/GUA-010.md`, which nobody
edited, and finds it `removed` and gone from disk. Checkpoint 7 (edited orphan) drops `incidents/INC-009.md`,
which the user did edit, and finds it retained with the reason `edited-since-last-projection` and still on
disk — the case a writer that removed it would be destroying a user's work. Checkpoint 8 (never recursive)
finds `user-notes/note.md` byte-identical and the symlink still a symlink, so no sweep occurred.

**The interruption is deterministically inducible through the writer's own declared seam.**
`ProjectionHooks(before_publish=...)` is the one hook the writer exposes, and checkpoint 4 uses it with a
lambda that throws, so the failure lands at the exact instant between staging and the first rename: no
sleep, no thread and no signal. That is the answer to the packet's Open Truth Gap, which recorded that
whether this checkpoint was deterministically inducible was unverified; the module's own comment says so
where the hook is used, and the hook is a declared field of the writer rather than a patched function, so the
case exercises the production path.

**Three read-side differentials run over the real dataset.**
`test_every_view_renders_two_byte_identical_runs_at_one_snapshot` renders every view in `VIEW_NAMES` twice
at one snapshot and one renderer version and requires the two payloads' serializations to be equal, naming
the view in its failure message — an ordering key recomputed from live state is invisible in a single run and
obvious in a differential. `test_the_records_unchanged_differential_leaves_the_order_unchanged` takes one
bounded `source_context` request ordered on `registered_role`, reads it twice, and asserts the row identity
order is identical while the dataset's own `dataset_identity` logical digest is unchanged: reading does not
recompute the order and does not write. `test_the_classification_scan_finds_no_third_value_and_no_empty_class`
walks every view's serialized rows, requires the position's class, the row's class and any consequence's class
to be one of exactly two values, and asserts the observed set is a subset of those two — a third value, or a
position with no class at all, fails the case.

**The bounded-continuation walk and the regeneration proof need the real scope.**
`test_a_bound_payload_carries_a_snapshot_bound_continuation_and_the_next_page_follows` reads one row of the
invariant view, asserts the payload still has rows remaining, that it carries a continuation whose
`snapshot_logical_digest` is the payload's own snapshot, and then presents that continuation and asserts the
next page's subjects differ from the first — so the token reaches the rest of a selection that did not fit
one page. `test_deleting_every_projection_and_reprojecting_loses_no_canonical_information` is the
derived-artefact regeneration proof: it records the dataset's logical digest, projects two views into a real
destination, asserts four rendered outputs, then deletes every file and directory under the destination,
asserts the destination is empty, re-projects the same requests, asserts the second run's manifest names
exactly the same destination paths as the first, and asserts the dataset's logical digest is unchanged. The
destination is derived, so deleting it loses nothing canonical — and the digest comparison is what makes
"nothing canonical changed" a measurement rather than a claim.

**The no-second-authority proof is taken at the row and column level over the dataset itself.**
`test_no_record_table_gained_an_identity_column_and_no_identity_reads_the_manifest` first sweeps
`CANONICAL_COLUMNS` for every declared table and refuses any column name containing `content_address`,
`logical_digest`, `fingerprint`, `manifest_digest` or `sha256`, naming the table and the column. It then
reopens the fixture store through `ReadScopeFixture.reopen`, enumerates every real table from
`sqlite_schema`, skips the `sqlite_` internals, and runs `PRAGMA table_info` over each one to assert that no
*actual* declared column carries any of the five forbidden tokens. The declared schema and the database on
disk are therefore both checked, which is what makes it a row-and-column proof rather than a restatement of
the vocabulary: a record identity cannot read the manifest's digest material because no such column exists.

**The item-25 typing pass narrowed the payload union rather than suppressing it.** The read-side cases take
their rows off a `payload` whose declared type is the discriminated union of the five views, so the union is
now narrowed to the concrete view *before* any row is read — `isinstance(first.payload, SourceContextView)`
for the records-unchanged differential, `isinstance(..., InvariantView)` in the bounded-continuation walk —
which also strengthens those cases: a source-context request that answered with another view's rows used to be
compared row-for-row with itself. A new local helper `subject_identity(subject)` returns
`(record_kind, record_id, revision_id)`, because a `SubjectRef` is a model and therefore not hashable, so the
two pages' subject sets are sets of those three recorded values; and the acceptance scenario asserts its
manifest generation is a real `int` (`isinstance(generation, int) and not isinstance(generation, bool)`)
before the `>= 2` comparison and before it is rendered into the checkpoint string. No case was added, removed
or reordered, no asserted fact moved, and no `# type: ignore` or `cast` was used to silence a narrowing.

### Conventions

- **Lane and marker.** The module declares `pytestmark = pytest.mark.integration` at module level, and
  `mcp/tests/test-evidence-lanes.toml` files it under the `integration` lane; the project default
  (`-m "not integration"`) therefore deselects it, and the boundary suite selects it explicitly.
- **The shared fixture is the real one.** A module fixture named `fixture` returns
  `read_scope_test_support.build_read_scope_fixture(tmp_path / "candidate")`, and all seven cases take that
  `ReadScopeFixture`: `database_path` and `repository_id` address the store, and `reopen()` gives the one
  case that must query the database directly a real connection. The fixture builds one repository
  through the public knowledge-store operations — four invariant identities with their revisions, three
  families with their memberships, eight realization claims, and a real committed Git tree beside the
  database. The fixture's own lifecycle registration names this module among its declared consumers, so the
  integration lane and the unit lane assert the same topology.
- **Modules are imported by their public names.** `project_knowledge` from
  `agents_remember.application.knowledge_projection`, `read_knowledge_view` and `VIEW_RENDERER_VERSION` from
  `agents_remember.application.knowledge_views`, `open_read_context` from
  `agents_remember.application.knowledge_read`, `dataset_identity` from
  `agents_remember.memory.knowledge.logical`, `CANONICAL_COLUMNS` from
  `agents_remember.memory.knowledge.schema`, `ManagedProjectionWriter` and `ProjectionHooks` from
  `agents_remember.memory.knowledge.managed_projection`, and the manifest and view vocabulary from their
  model modules. `read_scope_test_support` is imported as a bare top-level module because pytest puts the
  test file's own directory on `sys.path`; there is no `mcp/tests/__init__.py`.
- **No parametrisation.** Each of the seven cases is one named scenario; the eight checkpoints are recorded
  as dictionary entries inside one case rather than expanded into eight cases, which is the point of §5.9's
  single acceptance case.
- **Nothing is mocked.** The dataset is real SQLite built by the public write operations, the destination is
  a real directory under `tmp_path`, the symlink is a real `os.symlink`, and the interruption comes from the
  writer's own `ProjectionHooks` field rather than from `monkeypatch` or a patched rename. No clock, store,
  network or subprocess is replaced.

### Invariants And Boundaries

- **One scenario, eight distinct facts.** The acceptance case asserts the checkpoint id set, not a success
  flag, so a dropped or renamed checkpoint fails it and no two checkpoints can pass as one.
- **Every checkpoint asserts a pair.** The refusal or the resulting action and the destination state it left
  behind are asserted together, because either half alone is satisfiable by a writer wrong in the other.
- **Two checkpoints protect files the substrate never wrote.** The user's own `user-notes/note.md` and the
  bytes a user edited in place at a managed path both survive every run, and no case asserts a sweep of the
  destination.
- **The interruption is deterministic, not timing-dependent.** The hook fires after all outputs are staged
  and before the first rename, and the case compares complete tree bytes rather than a listing.
- **Reading is order-stable and write-free.** Two runs at one snapshot are byte-identical, and the
  records-unchanged differential pairs an unchanged row order with an unchanged dataset digest.
- **The class set stays at two values, measured over rendered output.** The completeness scan reads the
  serialized payloads of every view rather than the vocabulary alone.
- **The destination is derived.** Deleting all of it and re-projecting yields the same destination paths and
  an unchanged dataset digest, so nothing canonical lived only in the projection.
- **No record table carries a second authority.** `CANONICAL_COLUMNS` and `PRAGMA table_info` over every real
  table are both swept for content-address, digest and fingerprint tokens.
- **This module does not cover the writer's clause-level refusals.** The paths, collisions, authorization
  flags, unreadable manifest and duplicate-owner refusals are the sibling unit module's cases; here they are
  only the three checkpoints the scenario needs, asserted as part of one lineage.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module docstring states the plan's one-acceptance-case rule, names the eight checkpoints, and names the two proof obligations that need real records.** [1]
- The module declares the integration marker at module level and pins the renderer version its destination profile and rendered outputs both carry. [2]
- **The fixture is the shared real dataset: one repository built through the public write operations, left closed, whose `database_path` and `repository_id` every case addresses.** [3]
- Three local helpers name the acceptance profile, build one rendered output over the pinned renderer version, and read the destination manifest. [4]
- **The one acceptance case drives all eight checkpoints over one destination and one manifest lineage, then asserts the checkpoint id set and the final manifest generation.** [5]
- The prior generation and the user's own edits — two modified outputs, an untouched orphan, a user directory and a symlink out of the root — are planted so checkpoints 3, 5, 6, 7 and 8 each have a real subject. [6]
- **Checkpoints 1 to 4 assert confinement, the collision, the escaping link and the interrupted publication as pairs of refusal and untouched destination state.** [7]
- The writer's own `before_publish` hook is the declared seam that makes the stage/publish interruption deterministic, with no sleep, thread or signal. [8]
- **Checkpoints 5 to 8 keep the externally edited bytes, remove the unchanged orphan, retain the edited orphan with its reason, and leave the user directory and the symlink exactly as they were.** [9]
- A destination-wide byte snapshot is what turns "the prior generation is intact" into an exact comparison rather than a listing. [10]
- **Two runs of every view at one snapshot and one renderer are byte-identical, which is the differential that exposes an ordering key recomputed from live state.** [11]
- With the records untouched, a second read returns the same row order and the dataset's own logical digest is unchanged. [12]
- **The completeness scan reads the serialized payloads of every view and finds no third class value and no position or consequence without one.** [13]
- A bounded payload carries a continuation bound to its own snapshot, and presenting it reaches a next page of different recorded subjects. [14]
- **The derived-artefact regeneration proof: project, delete the whole destination, re-project, and assert the same destination paths with an unchanged dataset digest.** [15]
- **The row-and-column no-second-authority proof sweeps the declared column set and then `PRAGMA table_info` over every real table for content-address, digest and fingerprint tokens.** [16]
- One row subject's whole recorded identity, reduced to its three recorded values so two pages' subject sets can be compared (a `SubjectRef` is a model, not a value type, and so is not hashable). [17]

### Cross-Repo References

No cross-repository behavior is exercised in this file. Its dataset is built in a temporary directory by this
repository's own public write operations, its destination is a temporary directory the case owns, and
nothing it asserts reaches a second repository, a network, a provider or a Git remote.

No meaningful cross-repo references found.
