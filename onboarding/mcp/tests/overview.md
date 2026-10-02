# mcp/tests

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/tests/` |

## 260928-MIK-L37 The Cutover And Reopen Cases In Two New Modules, And Fourteen Adapted Modules

`260928-MIK-L37` (MIK-R37) adds two case modules and two lane rows, and extends fourteen modules:

- [`test_knowledge_cutover.py`](test_knowledge_cutover.py.md) (new, 9 cases, `unit-regression`): the cutover lock
  at fourteen routes, the converting candidate, the probe's fail-closed cases, the frozen database, no read of a
  converted tree's database, and the hand-off evidence shape.
- [`test_knowledge_reopen.py`](test_knowledge_reopen.py.md) (new, 19 test functions, `unit-regression`): a reopened
  leaf's next attempt through the writer, the gate, the validator's freeze, the index, the onboarding gate and record
  landing; the gate at the worktree closeout, entered through `closeout_result`, and its preview; a leaf that
  continues after a closeout that was not integrated; the commit bound to the judged tree; the governing row of a
  changed record across attempts; and the writer's `items`.
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): the two rows at `:124` and `:125`.
- [`test_knowledge_conversion_toolchain.py`](test_knowledge_conversion_toolchain.py.md): eleven test functions for
  the census on a converted candidate, the card authoring (with the refusal of merged tables), the converted check's
  base, and the one-document fix with its bounded response.
- [`test_knowledge_crossing.py`](test_knowledge_crossing.py.md): the crossing owner's resolution at the higher
  side's revision plus one, the writer's converted base, and cancel inside the crossing case.
- [`test_knowledge_writer.py`](test_knowledge_writer.py.md): the bootstrap lock, the crossing owner's rows, and a
  cover that revises a rationale in place.
- [`test_knowledge_gate_routes.py`](test_knowledge_gate_routes.py.md): the N23 to N25 guards, and a hand-closed
  file refused also when landed a commit later.
- [`test_knowledge_index_surfaces.py`](test_knowledge_index_surfaces.py.md): unheld read seeds.
- [`test_memory_attribution_producers.py`](test_memory_attribution_producers.py.md): carryover on converted memory.
- [`test_worktree_sync.py`](test_worktree_sync.py.md): cancel after a memory conflict (integration lane).
- [`test_onboarding_trace_gate.py`](test_onboarding_trace_gate.py.md): the run's converted check gets its base.
- [`test_knowledge_closeout_gate.py`](test_knowledge_closeout_gate.py.md),
  [`test_knowledge_history_files.py`](test_knowledge_history_files.py.md),
  [`test_knowledge_index.py`](test_knowledge_index.py.md) with
  [`knowledge_index_test_support.py`](knowledge_index_test_support.py.md),
  [`test_knowledge_reader.py`](test_knowledge_reader.py.md) and
  [`test_review_git_trees.py`](test_review_git_trees.py.md): the gated memory commit and the memo key, the
  governing-row rules, a rewrite in the second of the index write, a history row's incoming link, and the
  reviewer's latest-attempt rows.

- The new cutover module's docstring: what it covers. [489]
- The new reopen module's docstring. [490]
- The two lane rows. [491]

- The public closeout refuses an open item and commits once it is answered. [492]


## 260928-MIK-L33 The Change-Kind Cases In One New Module

`260928-MIK-L33` (MIK-R33) adds one case module and one lane row:

- [`test_review_change_kinds.py`](test_review_change_kinds.py.md) (new, 12 collected, 682 lines, `unit-regression`):
  a store-authored live leaf over four real Git trees, resolved and composed as the reviewer does, with one member per
  badge kind and the review rounds' cases (a moved stale entry, an unresolved range beside an established fact, a
  retired record, a same-revision text change, definition 8 on a rewritten binary, an unparseable sidecar, family
  record and trees). The cases pin every kind, the shared member, returned members only, the unknowns with their
  reasons (never `unchanged`), the total, the derived facts and their validators, and the dataset review. The
  dashboard's `triage.*` bodies are captured from this world.
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): the row at `:128`, after L32's unexplained-lane row;
  every later row moves down one line (L10's row is now `:130`, L14's `:131`), and this leaf re-pointed the citations
  to them through the installed fixer or by that exact shift. No evidence-lifecycle consumer line and no re-pin.

The worker's mutation sets (46 of 46 at the R1 fix round, 4 of 4 at R2, 9 of 9 at the merge round, 4 of 4 at R3)
were caught by these cases and the dashboard suites. Review R3 reran the focused suites on the merged tree (150 passed:
change kinds, lane, git trees, worklist ×2, L10 disposition, L09 closeout gate and gate routes, onboarding trace,
evidence lanes).

- The new module's docstring: one member per badge kind. [1]
- The lane row. [2]

## 260928-MIK-L09 The Mandatory Closeout Gate Cases In Two New Modules, And Four Adapted Modules

`260928-MIK-L09` (MIK-R09@v2) adds two case modules and two lane rows, adds two cases to one module and adapts three:

- [`test_knowledge_closeout_gate.py`](test_knowledge_closeout_gate.py.md) (new, 18 collected, 1,198 lines,
  `unit-regression` `:122`): a converted leaf on real repositories (two invariants of one family, the official `main`
  line and the leaf's `leaf` branches). It pins rule 2's currentness through the packet's conforming, non-conforming
  and both boundary examples, new invariants needing no row, the recompute after a sync, incomplete runs naming their
  input, the per-kind dispatch (`set(GATE_PREDICATES) == set(ITEM_KINDS)`), the validator's history-row rule at the
  gate (the leaf's own closed file is no waiver), the closeout validator (and `GATE_UNBOUND`), the closeout memory
  commit, direct, record, master and checkpoint landing, the insertion-only symmetry, the unconverted leaf, the
  prepared path, the memo and the approval-state recompute. Its fixture is module-local by the dependency-ownership
  census's rule. It is 2 lines under the 1,200 limit (review R1 note 14: split before the next case).
- [`test_knowledge_gate_routes.py`](test_knowledge_gate_routes.py.md) (new, 27 collected, 992 lines, `unit-regression`
  `:123`): one refusal test per public route entry (review R1 F5: `external_closeout_commits`, `direct_landing` preview
  and apply, `record_landing_result`, `_handover_or_apply_integration` for the master and the checkpoint) and the
  pinned fixes F1–F4, F6, F7, F9, R2-1 to R2-5 (N01, N04, N05, N08, N09, N12, N21) and R3-1/R3-2 (N16 in SHA-1 and
  SHA-256 repositories, N20 at its real raise site). It imports the gate module's fixture world.
- [`test_knowledge_validator_routes.py`](test_knowledge_validator_routes.py.md): two parametrised sync-merge cases (a
  merge-caused row mismatch syncs, reported by `R09-history-rows-merged`; one already wrong on the leaf's side is
  refused), kept here beside `SyncFixture` so no governed catalog row was needed.
- [`test_knowledge_validator.py`](test_knowledge_validator.py.md): the `RETIRED` fixture keeps `INV-RET1R3` in the
  trees as a retired record (review R2-1; MIK-R22 rule 3), assertions unchanged.
- [`test_knowledge_worklist_leaf.py`](test_knowledge_worklist_leaf.py.md) and
  [`test_onboarding_trace_gate.py`](test_onboarding_trace_gate.py.md): the controller cases capture real candidate
  trees, and their counts change as MIK-R09 requires (0 → 4 and 2 → 3).
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): the two rows; every later row moves down by two.

Mutations: the worker's 26 (fix round), 37 (R2) and 4 (R3) are killed, and the reviewer's N01–N21 set as recorded in
the review. Final checks (R3): focused 267 passed, unit suite 3,406 passed, integration lane 457 passed (including the
dependency-ownership census). The catalog and its pin are unchanged.

- The packet's examples: ready once current rows answer every item; a new edit reopens two. [3]
- One refusal test per public route entry, starting with the worktree closeout. [4]
- The sync-merge cases. [5]
- The two lane rows. [6]

## 260928-MIK-L38 The Folder-Master Finalize Cases And The Reopen Placement Cases

`260928-MIK-L38` (MIK-R38) adds cases to two existing integration-lane modules, beside the finalize and reopen cases
they extend (ruling 2026-09-30T12:33:07 Q1); no lane row, no evidence-lifecycle consumer line and no re-pin:

- [`test_lifecycle_finalize.py`](test_lifecycle_finalize.py.md): the fixtures move to a base `_FinalizeFixtures`.
  `LifecycleFinalizeTests` keeps its two cases and gains the misplaced named-master refusal (ruling 13:35:32). The new
  `FolderMasterFinalizeTests` (every leaf `master: null`) pins the listing folder master's row under the demotion
  rule, the dry run and its accepted assertion, three standalone subtests, six refusal subtests (including an
  unreadable `task.json` and an asserted master without the row, review R1 notes 2 and 4), and the misplaced
  `light` leaf (finding 1). Each refusal compares both documents' bytes before and after.
- [`test_task_reopen.py`](test_task_reopen.py.md): four `ReopenResetTests` cases: an unnamed `subTask` still resets
  its folder master's row; a `light` `task.json` is not its own master (the planner directly, because the public
  route's preflight refuses first); and the misplaced leaf and the misplaced named master are refused `blocked`
  with nothing written.

The worker and both review rounds removed each guard in turn and each removal failed at least one case; the base build
fails every new guard's case. Review R2 on the fixed tree: focused 168 passed, unit suite 3,298 passed, integration
lane 457 passed (15 skipped). After the sync onto L32 (`59daf505`), the finalize, reopen and dependency-ownership
tests pass on the synced tree.

- The folder-master finalize cases. [7]
- The four reopen cases. [8]

## 260928-MIK-L32 The Unexplained-Changes Lane Cases In One New Module

`260928-MIK-L32` (MIK-R32) adds one case module and one lane row:

- [`test_review_unexplained_lane.py`](test_review_unexplained_lane.py.md) (new, 11 collected, 709 lines,
  `unit-regression`): each comparison is four real Git trees (a code repository and a converted memory repository,
  each with a base and a candidate commit) reopened as the reviewer reopens a recorded comparison, so every
  knowledge side is read through its tree's derived index. One fixture change set of ten paths covers every locator
  kind (`symbol`, `line_range`, `file`), a stale and an unresolved entry, a proof, a mode-only change, an added file,
  a binary with a `file` entry, and an insertion strictly inside a symbol the gate would link. The cases pin: the
  three buckets and their reconciliation with both destinations and `paths` (ruling 2026-09-30T12:19:20 Q1); the
  entry count reading no hunk (`CodeTrees.hunks` patched to fail); hunks classified on their changed lines at each
  side's recorded blob, before and after curation; links with invariant revisions, keys, a proof's facet and the
  membership states; an unread side (never unexplained) and a partial index (only its unparsed files unknown; the
  gate linkage `unknown`, review R1 F3); bounded reasons over 300 stale entries (F4); unmeasured change sets (no
  count); the route's one-question rule; the live tree leaf's lane, file read and refusals, including `file=` values
  of 1,025 and 4,096 characters answering the typed 200 (F2); and a dataset leaf's summary carrying no
  `attribution`. The route and live-leaf cases reuse `test_review_git_trees.py`'s `world` fixture.
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): the row at `:125`, after L25's git-trees row; every later
  row moves down one line (L10's row is now `:127`, L14's `:128`), and this leaf re-pointed the citations to them
  through the installed fixer or by that exact shift. No evidence-lifecycle consumer line and no re-pin: the module
  imports no test support module.

The worker and the reviewer removed each guard in turn (mutation checks); each removal failed at least one case. Review
R2 reran the focused suites (144 passed, including L08, L10, L14 and L29's modules), the full unit suite (3,359 passed,
62 skipped) and the integration lane (447 passed, 15 skipped) on the tree synced onto L14 (`f9e12622`).

- The new module's docstring: the fixture's ten changed paths. [9]
- Buckets and destinations reconcile; long paths answer typed. [10]
- The lane row. [11]

## 260928-MIK-L14 The Reconsideration Cases, The Registry Compared As A Set, And The Forty-Second Re-Pin

`260928-MIK-L14` (MIK-R14@v2) adds one case module and adapts one:

- [`test_reconsideration_surfacing.py`](test_reconsideration_surfacing.py.md) (new, 29 collected, `unit-regression`):
  it reuses MIK-R08's real Git code and converted memory world, with two decisions in K_B (D18's rejected and
  deferred alternatives reconsidered on an assumption, a symbol anchor and a requirement endpoint; D12's on a family
  and on D18). The manifest lookup (the integer after `v`, drafts and other IDs ignored, `unknown` without a
  readable manifest); every trigger (a revised assumption, a `rerouted` row, a touched or absent anchor, a newer
  approved version) and what does not fire (`no_impact`, `carried`, an unresolved endpoint, no coordination root);
  one hop; both rows through the real writer, with the stored predicate agreeing and the `raise` refused writing
  nothing without a task owner; a real `task_doc` append that keeps the earlier question; the reorder guard (both
  loops); route targets (Q1), superseded decisions (Q5) and the refresh (Q2/Q3); F1, F3 and F4; N1 and N2; the R3-1
  reruns; the R4 carried state, committed lookalikes and the explicit answer by item ID; the R5 second change in the
  range, the stale worklist and a curator-set unapproved version. Every refusal case asserts the decision file is
  byte-identical. The module is 1,172 lines, 28 under the limit (note R6-2: the next addition splits it).
- [`test_knowledge_history_files.py`](test_knowledge_history_files.py.md): the registry lists six row kinds and is
  compared as a set, because leaves register in landing order (review F9; note N4: the duplicate-name check is gone,
  subject disjointness still asserted).
- [`test_dependency_ownership_ast_helpers.py`](test_dependency_ownership_ast_helpers.py.md): the **Forty-second**
  deliberate re-pin, `f8b04814…` → `4477446e…`, 16 / 80, for the one consumer line the census derived on the
  package-lock row ([`evidence-lifecycle.toml`](evidence-lifecycle.toml.md) `:839`); L05's Forty-first paragraph is
  only re-wrapped.
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): the row at `:127` (after L29's row at `:108`); every later
  row moves down one line,
  and this leaf re-pointed the citations to them by that exact shift.

The worker and reviewers removed each guard in turn (mutation checks), and each removal failed at least one case.
Review R6 (pass-with-notes) reran the full unit suite (3,327 passed, 62 skipped) and the integration lane (447 passed,
15 skipped) on the tree synced onto L31 (`b54d1b03`); the leaf was then synced onto L29 (`ce459423`), where its files
re-applied cleanly.

- The new module's docstring: the fixture's two decisions. [12]
- The registry compared as a set. [13]
- The Forty-second re-pin note. [14]
- The lane row. [15]

## 260928-MIK-L29 The Knowledge Reader Cases In One New Module

`260928-MIK-L29` (MIK-R29@v1) adds one module, [`test_knowledge_reader.py`](test_knowledge_reader.py.md) (21 cases,
1,182 lines, under the 1,200-line cap; the architect noted its size at R3, so a later reader case belongs in a new
module), and one `unit-regression` lane row at `:108` (between the index-surfaces and paging rows; every later row
moves down one line). The module is self-contained: it imports no test support module, so the evidence-lifecycle
catalog and its pin are unchanged, and the dependency-ownership integration test passed without a re-pin.

- **The fixture world:** a code repository and its converted memory repository with an unconverted commit and two
  converted ones (`Code-Commit`-paired): MIK-R23's review-example tree, a family across four files, a test proof, a
  decision and an incident, a retired invariant, a sibling-prefix file, onboarding prose with numbered references and
  a census; the second commit revises the invariant, re-anchors one realization in place and moves another, adds a
  history row and an assumption, and supersedes the decision.
- **The cases:** the file, bounded-directory (F2) and test-file path views; the subtree walk (every whole answer within
  the bound, F17), a walk resumed after a code commit measuring at page 1's tree in both its page and its selection
  (F16, R3-1) with a token naming an absent tree refused (R3-2), and another walk's token refused; the explorer and the
  without-proof list; the invariant view with a three-source timeline, moves against re-anchors while reading only the
  sidecars naming them (F1, F5), the bounded timeline cache (F7; a failed source not cached, F17); the family,
  decision (derived supersession), incident and facet (unreadable links named, F11) and census views; the selections
  (hexadecimal names only, F6; published with a pin only when clean, N2; a leaf's code note, N1; a partial index with no
  code tree); the route over every view with nothing written, 503 unwired; and bad requests (locators F3, `..`, an
  unknown view, NUL and control characters F15), a directory as code `absent` (F18), binary and oversize blobs never
  read (F14, F17).
- **Suites (reviewer R3, synced tree):** 21 passed in the module; full unit suite 3,319 passed and 62 skipped;
  integration lane 447 passed and 15 skipped.

- The module's own statement of its fixture. [16]
- The walk-tree case (F16, R3-1, R3-2). [17]
- The route case: every view, 503 unwired, nothing written. [18]
- The lane row. [19]

## 260928-MIK-L31 The Focused-Card Read Cases, The Proof Admission At The Route, And The Q8 Cases

`260928-MIK-L31` (MIK-R31@v1) adds cases to three modules and no new module, lane row or catalog line:

- [`test_review_git_trees.py`](test_review_git_trees.py.md) (19 collected, 1,022 lines): the cards read locates each
  entry of the named invariants on both code sides (a changed range with each side's own excerpt and MIK-R03 state,
  a retired entry carried once, a proof with its facet, an unresolved locator with its reason), names an unreadable
  side `unavailable` and a missing file `absent`, bounds the excerpt (500 lines give a stated 400-line prefix) and
  the placement cache (answers only, 8,192; review F3), finds history rows by `facts.row` (PS-1), and at the route
  (review F12, ruling Q1) admits an unchanged test file only after a K_C proof names it. The route case gains the
  pinned numbered read (review F11), the cards read, and the 400s for a 65-character key (F10) and 501 keys; the
  tree-view case asserts snake_case keys (MIK-L25 review F9).
- [`test_knowledge_review_attributed_source_content.py`](test_knowledge_review_attributed_source_content.py.md):
  never-initialized knowledge asks to initialize it (MIK-R31 rule 6, O1), a tree index's proof entry links its
  path while a dataset links none (Q1), and the undetermined case asserts the Q1 wording.
- [`test_review_assessment_history.py`](test_review_assessment_history.py.md): the Q8 case, with 100 artifacts
  summarised and 10 kept exactly (review F6, R2-2 pinning the two branches apart).

No new C block in any touched test (the pre-existing D block of the tree-view case rose from D26 to D28). On the
synced tree the full unit suite passed (3,298 passed, 62 skipped) and the integration lane passed (447 passed, 15
skipped), rerun by the reviewer in R3 (pass-with-notes); the collection budget holds with L05's and L10's cases.

- The cards-read case and its four helpers. [20]
- The proof admission at the route. [21]
- The never-initialized remedy. [22]
- The Q8 case. [23]

## 260928-MIK-L05 The Route-Chain Cases, The Adapted Leaf-Read Module, And The Forty-First Re-Pin

`260928-MIK-L05` (MIK-R05@v2) adds one case module and adapts one:

- [`test_knowledge_route_chain.py`](test_knowledge_route_chain.py.md) (new, 13 collected, `unit-regression`): the
  chain over nested directories (nearest route first, never a child or a sibling, ties by family ID, a root file
  seeing only `.`); compact entries after the leaf content, `memberAtSeed` (ruling 2026-09-30T03:32:18 Q2) with
  live member counts, and `no_governing_family` as a state; the conforming example
  (`mcp/src/agents_remember/worktrees/new_helper.py`); expansion from a family seed and its spellings (ruling Q1);
  the budget (each row exactly once, within the threshold, the chain last); the family-seed resume under any
  spelling (review F4) and a lacking revision refused on resume and fresh read alike (ruling 04:45:22 R2-1); a
  v1-policy token refused (review F2, ruling Q4); and the `served_earlier` rendering only `read_ar_files`
  applies. It reuses L01's leaf-read helpers and `test_read_ar_files`'s context builders.
- [`test_knowledge_leaf_read.py`](test_knowledge_leaf_read.py.md): the selection test gains the two chain rows,
  `chainFamilies: 2` and 17 rows; the policy assertions name `family-complete-leaf/v2`; the failure test was split
  (review R1 F1, 04:12:49) into the entry-less page, the refusal carrying `routeChain`, and the partial-index case
  (13 collected).
- [`test_dependency_ownership_ast_helpers.py`](test_dependency_ownership_ast_helpers.py.md): the **Forty-first**
  deliberate re-pin, `449b69ef…` → `f8b04814…`, 16 / 80, for the four consumer lines the census derived
  ([`evidence-lifecycle.toml`](evidence-lifecycle.toml.md) `:459`, `:838`, `:1553`, `:1829`); final after the sync
  onto `31d761a2`.
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): the row at `:110`; every later row moves down one line,
  and this leaf re-pointed the citations to them by that exact shift.

No new or adapted test function is at radon C (review F1). Post-sync, the full unit suite passed (3,289 passed, 62
skipped) and the integration lane passed (447 passed, 15 skipped); review R1 pass-with-notes, R2 pass.

- The MIK-R05 lane row. [24]
- The budget and resumption case. [25]
- The lacking-revision case on resume and fresh read. [26]
- The entry-less page in the adapted leaf-read module. [27]

## 260928-MIK-L10 The Unexplained-Change Cases, Three Adapted Modules, And The Fortieth Re-Pin

`260928-MIK-L10` (MIK-R10@v2) adds one case module and adapts three:

- [`test_unexplained_change_disposition.py`](test_unexplained_change_disposition.py.md) (new, 10 collected,
  `unit-regression`): it reuses MIK-R08's real Git code and converted memory world. Registration and the
  `no_invariant` row model; coverage by realization entries or the latest census status of the governing route (an
  unreadable census is `incomplete`, naming K_B); a covered hunk answered by `no_invariant`, attach or author and
  never by an onboarding row; a delete-only hunk that only `no_invariant` answers (ruling 2026-09-30T01:56:39 Q1: a
  line-range attach around the deletion point leaves the item open); non-text changes bound to the C blob;
  currentness; the review N6 case (a symlink's tree object, a deleted binary `@absent`, an uncovered deletion); an
  uncovered new file answered by its card, whose `no_invariant` row is reported unnecessary (ruling 03:24:28 N2);
  the writer's refusals (absent and retired invariants, blank reason, `covers`); and ruling Q3 (an answering
  onboarding row is not unnecessary). Every case asserts that the gate's stored-item predicate agrees with
  `satisfiedBy`. Reviewer R2-1 (low): the N6 case commits its rows directly, so the writer's `file:` subject check
  has no unit assertion for a symlink or `@absent`.
- [`test_knowledge_worklist.py`](test_knowledge_worklist.py.md): a `knowledge_items` helper; three L08 assertions
  that meant "no knowledge item" use it, and the comment-between-functions case asserts exactly one
  `unexplained_hunk`.
- [`test_knowledge_history_files.py`](test_knowledge_history_files.py.md): the registry lists five row kinds.
- [`test_dependency_ownership_ast_helpers.py`](test_dependency_ownership_ast_helpers.py.md): the **Fortieth**
  deliberate re-pin, `a571a70f…` → `449b69ef…`, 16 / 80, for the one consumer line the census derived on the
  package-lock row ([`evidence-lifecycle.toml`](evidence-lifecycle.toml.md) `:836`).
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): the row at `:124`; every later row moves down one line,
  and this leaf re-pointed the citations to them by that exact shift.

Review R1 (pass-with-notes) and R2 (pass) reran the full unit suite (3,236 passed, 62 skipped at R2) and the
integration lane (447 passed, 15 skipped).

- The MIK-R10 lane row. [28]
- Delete-only: only no_invariant. [29]
- The knowledge items, without the unexplained kinds. [30]

## 260928-MIK-L25 The Reviewer-On-Git-Trees Cases, And The Archive-Hook Cases In Their Own Module

`260928-MIK-L25` (MIK-R25@v1) adds two case modules and one lane edit:

- [`test_review_git_trees.py`](test_review_git_trees.py.md) (new, 13 collected, `unit-regression`): a converted
  memory repository and a live leaf with uncommitted code and knowledge; four trees with the candidates pinned and
  reused; **a repeat read writes nothing** (every ref, object and record file compared; ruling 2026-09-29T22:22:37
  Q5); committed candidates need no ref and a failed pin refuses naming repository and ref; the tree view (diff by
  record and by source, currentness per side, the worklist); a partial index; reopen and `unavailable-history` for
  memory and code trees (review F4); the converted base; the legacy comparison; the no-`.sqlite` check (Q1); the
  unconverted dataset review; never frozen; directory-name pins (ruling 2026-09-30T02:32:42 (a)); the route.
- [`test_review_artifact_cleanup.py`](test_review_artifact_cleanup.py.md) (new, 14 collected, `unit-regression`):
  the archive hook, split out of the first module by ruling 02:32:42. Identity (F1, the record sweep removed at
  00:08:39, the `task.json` confirmation of 02:12:06, the planted-contract case V10), never raising and holding a
  refused generation (F2, F3), a planted foreign manifest (01:00:07), and physical confinement against symlinks
  (01:37:42). Self-contained: plain repositories and a leaf contract, no shared support module.
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): the two rows at `:122` and `:123`; every later row
  moves down two lines, and this leaf re-pointed the citations to them by that exact shift.

No catalog row and no re-pin. The dashboard cases are under `dashboard/src/data` and `dashboard/src/panels`. Review
round 6 (pass-with-notes) reran the full unit suite (3,231 passed, 62 skipped) and the integration lane (447
passed, 15 skipped).

- The two MIK-R25 lane rows. [31]
- A repeat read writes nothing. [32]
- Archival deletes only the task's own artifacts. [33]

## 260928-MIK-L13 The Decision-Record Cases, And The Writer's Endpoint Cases

`260928-MIK-L13` (MIK-R13@v2) adds one case module and touches two more files:

- [`test_knowledge_decisions.py`](test_knowledge_decisions.py.md) (new, 9 collected cases, `unit-regression`):
  the packet's D12 and D18 as records pass every rule; one alternative, none chosen and two chosen; a rejected or
  deferred alternative without `reconsider_when`; a stored `superseded` named by field; `reconsider_on` at the
  chosen alternative or out of range; a governs-less decision reported, not refused; the derived `superseded` and
  the `reconsider:<DEC-ID>#<i>` subjects; the requirement resolver (resolved, version mismatch, missing packet,
  outside `tasks/`, no root); and review F6, a decision is never an export. It builds its own tree and task
  directory, with no shared support module or catalog fixture.
- [`test_knowledge_writer.py`](test_knowledge_writer.py.md) (20 collected): a lifted D12 round-trips with one
  requirement endpoint resolved and one reported unresolved, and a rerun is unchanged; a content-rule break is
  refused with nothing written; the bootstrap dispatch case now asserts that the wave resolves an endpoint through
  the admitted coordination root (review F4, ruling 2026-09-30T02:05:07).
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): one lane row at `:121`; every later row moves down
  one line, and this leaf re-pointed the citations to them by that exact shift.

No catalog row and no re-pin. Review round 2 reran the full unit suite (3,237 passed, 62 skipped) and the
integration lane (447 passed, 15 skipped) on the staged tree synced onto L06 and L01.

- The decision-record lane row. [34]
- A lifted decision round-trips with its requirement endpoints reported. [35]
- A decision is never an export (review F6). [36]

## 260928-MIK-L01 The Leaf-Read Cases, Three Adapted Modules, And The Thirty-Ninth Re-Pin

`260928-MIK-L01` (MIK-R01@v2) adds one case module and touches six more:

- [`test_knowledge_leaf_read.py`](test_knowledge_leaf_read.py.md) (new, 11 collected cases, `unit-regression`):
  the selection and its declared order over a three-family graph (shared member, retired member, proof entry,
  advertised family), one selection under one manifest on both surfaces, the `invariant` view's families, the
  conforming example in one response, `registration_absent` and the partial index with refusals naming the
  tree, the carried obligations (a root with no commit refused by name, a leaf walk resumed at its code tree
  with no path in the token, `seed_queue_exceeded` at 104 deep seeds within the threshold, a tree projection
  of more than 64 rows whole), the derived reference title, and identity seeds beside a leaf with the
  mixed-block policy pinned (ruling N2).
- [`test_knowledge_paging.py`](test_knowledge_paging.py.md): L02's walks read the leaf `rows` instead of the
  scope `items`; the 40-member case uses 150-word statements to still span three pages, the continued-family
  check reads the literal reference row at `rows[0]`, and the code-tree case is renamed
  `test_a_resumed_leaf_walk_observes_entries_at_page_one_code_tree` (entries current at T1, stale at T2).
- [`test_knowledge_index_reuse.py`](test_knowledge_index_reuse.py.md) and
  [`test_knowledge_conversion_toolchain.py`](test_knowledge_conversion_toolchain.py.md): one line each, reading
  statements from `rows`.
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): one lane row at `:109`; every later row moves
  down one line.
- [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md): one consumer on the `package-lock.json` row
  (`:835`, after L11's) and on the `knowledge_index_test_support.py` row (`:1824`).
- [`test_dependency_ownership_ast_helpers.py`](test_dependency_ownership_ast_helpers.py.md): the
  Thirty-ninth re-pin (`cb853f72…` → `a571a70f…`, 16 / 80), renumbered from a provisional ordinal at the sync
  onto L11 (architect ruling of 2026-09-30 00:08:39).

The worker's final full unit suite passed (3,205 passed, 62 skipped) and so did the integration lane (447
passed, 15 skipped); review round 2 reran them on the staged tree.

- The leaf-read lane row. [37]
- The leaf-read module's two consumer lines. [38]
- The Thirty-ninth re-pin note. [39]

## 260928-MIK-L06 The Family Route Condition Cases, And The Moved-Row Writer Case

`260928-MIK-L06` (MIK-R06@v2) adds one module and one lane row, and one case to an existing module. There is
no catalog consumer row or re-pin: the integration lane passed unchanged.

- [`test_family_route_conditions.py`](test_family_route_conditions.py.md) (new, 10 collected, `unit-regression`
  at `test-evidence-lanes.toml:69`): the four family route conditions as `family_route_condition` worklist
  items over MIK-R08's real Git world (`test_knowledge_worklist.World`). It covers the packet's conforming
  directory move (four worklists with stable IDs, and the R2-N1 stage where a `rerouted` row cannot answer the
  items while K_C still records the old files), the non-conforming example (`no_impact` never satisfies; a
  kept dead route stays open), the boundary example, the carried L04 decision (a killed route the validator
  only reports becomes a mandatory item), a route already dead at B not charged to the leaf (ruling Q1),
  `route_unassigned` answered only by routes (Q3), the ambiguous rename target (Q4), the rename-mapped
  suggestion and `unmappedLocations` (Q5), retired families, and the registry. Every case checks that the
  stored predicate agrees with the live `satisfiedBy`.
- [`test_knowledge_writer.py`](test_knowledge_writer.py.md): one case (18 collected), appended after L27's:
  a `moved` row relocates its entry into the moved file's sidecar; a path on another disposition, a
  malformed path and a cover with both `remove` and `path` are refused as named problems (ruling Q6; review
  F1 and N7).
- **The legacy count (L27 ruling Q4).** L06 landed second. Its cases filter the validator's reports by rule,
  so no pin needed the `R27.4-legacy-unassessed` count.
- **The lane row** moved every later row of `test-evidence-lanes.toml` down one line; the citations in this
  overview and in the cards that cite those rows were re-pointed by that exact shift, each checked to hold its
  anchors.

- The lane registration. [40]
- The conforming directory move. [41]
- The moved-row writer case. [42]

## 260928-MIK-L27 The Admission Cases, And The Legacy Count In Earlier Pins

`260928-MIK-L27` (MIK-R27@v1) adds no module, lane row, catalog consumer row or re-pin: its 10 new cases
were folded into modules that already consume the support modules.

- [`test_knowledge_validator.py`](test_knowledge_validator.py.md): a MIK-R27 section of 9 cases (46
  collected): reference-only justifications refused and real prose admitted (rulings 2026-09-29T22:11:24 Q2
  and 23:04:57 F1), no criterion and `legacy-unassessed` refused, unsupported checkable claims refused, an
  existing record whose test was deleted only reported, exported, retired and merge-parent records never
  refused, a forged legacy ID treated as new (ruling F2), the legacy count, and the rules' registration.
- [`test_knowledge_writer.py`](test_knowledge_writer.py.md): one case (17 collected): the writer refuses an
  unsupported `guarded_by_test` claim, leaves the tree byte-identical, and writes once the proof is added.
- **L22's and L04's pins gain the legacy count.** Every validation of the Doc14 fixture tree now carries
  one report-only `R27.4-legacy-unassessed` finding (`LEGACY_COUNT` in
  [`knowledge_validator_test_support.py`](knowledge_validator_test_support.py.md)), so the exact pins in
  `test_knowledge_validator.py`, [`test_knowledge_family_routes.py`](test_knowledge_family_routes.py.md) and
  [`test_knowledge_validator_routes.py`](test_knowledge_validator_routes.py.md) include it and stay exact;
  the CLI JSON case pins the full sorted list with its report-only flags (ruling F3). Whichever of L06 and
  L27 lands second updates its new pins likewise (ruling Q4).
- **Two support fixes.** The validator fixture's two added invariants claim `prevents_costly_mistake`
  (they have no entries to support the checkable criteria), and
  [`knowledge_writer_test_support.py`](knowledge_writer_test_support.py.md)'s base records are genuine
  exports whose IDs derive from their legacy IDs, with `ADMISSION` claiming an unchecked criterion.

- The legacy count every fixture validation carries. [43]
- A forged legacy ID does not make a record exported. [44]
- The writer refuses an unsupported admission claim. [45]

## 260928-MIK-L11 The Planned-Effects Cases, And The Thirty-Eighth Re-Pin

`260928-MIK-L11` (MIK-R11@v2) adds one case module and touches four more:

- [`test_planned_knowledge_effects.py`](test_planned_knowledge_effects.py.md) (new, 5 collected cases,
  `unit-regression`): the `expectedKnowledgeEffects` field (optional, `NORMATIVE_INTENT`, settable, rendered,
  refused when malformed, digests unchanged when absent); matching and the `planned`/`unplanned` marks,
  including the four branches review R1 F3 asked for (ruling F3); a planned row answering its item, with the
  stored predicate agreeing; the writer's planned rows, every refusal and the strict leaf lookup (ruling F1);
  and the leaf route with the checklist, the tool rows and the fail-closed run on an unreadable task document
  (ruling F2).
- [`test_knowledge_history_files.py`](test_knowledge_history_files.py.md): the registry case asserts four row
  kinds, adding `planned`.
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): one lane row at `:118`; every later row moves
  down one line.
- [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md): one consumer on the `package-lock.json` row
  (`:834`).
- [`test_dependency_ownership_ast_helpers.py`](test_dependency_ownership_ast_helpers.py.md): the
  Thirty-eighth re-pin (`5c0a1594…` → `cb853f72…`, 16 / 80), renumbered from a provisional ordinal at the
  sync onto L02 (architect ruling of 2026-09-29T22:35:34+02:00).

- The planned-effects lane row. [46]
- The planned-effects module's consumer line. [47]
- The Thirty-eighth re-pin note. [48]

## 260928-MIK-L02 The Paging Cases, And The Thirty-Seventh Re-Pin

`260928-MIK-L02` (MIK-R02@v2) adds one case module and touches three more:

- [`test_knowledge_paging.py`](test_knowledge_paging.py.md) (new, 11 collected cases, `unit-regression`): the
  cross-surface 40-member walk (page 1 from `read_ar_files`, later pages from `knowledge_read`, every row
  exactly once), threshold adherence over eight seeded randomized families, the oversized row, binding
  refusals with no page, the projection over the artifact limit, the whole-block bound at 5 and 16 seeds, the
  ordering and code-tree bindings, and the empty ordering on every path.
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): one lane row at `:107`; every later row moves
  down one line.
- [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md): one consumer on the `package-lock.json` row
  (`:833`) and on the `knowledge_index_test_support.py` row (`:1821`).
- [`test_dependency_ownership_ast_helpers.py`](test_dependency_ownership_ast_helpers.py.md): the
  Thirty-seventh re-pin (`dcc1ab1d…` → `5c0a1594…`, 16 / 80), renumbered from a provisional Thirty-sixth at
  the sync onto L03 (architect ruling of 2026-09-29 20:40:40).

L03's `test_knowledge_currentness.py` passes unchanged over the new tree read.

- The paging lane row. [49]
- The paging module's two consumer lines. [50]
- The Thirty-seventh re-pin note. [51]

## 260928-MIK-L30 The Onboarding Trace Gate Cases

`test_onboarding_trace_gate.py` (new, 15 cases, carded) pins MIK-R30@v1 on converted-format fixtures with
real repositories and a leaf series contract: the counted-change rule and the writer's mechanical carry, the
card and nearest-route items, rows and unnecessary rows, moved markers, the fail-closed cases (mixed formats,
unreadable history, unreadable K_C and K_B sidecars, unestablished sides), the converting leaf with the v1
cache file rewritten as v2, the retired checks, the memory-quality count, the persisted worklist in
`(kind, subject)` order and the unconverted leaf that keeps today's gate. It is registered in
`unit-regression` (`test-evidence-lanes.toml:116`). `test_knowledge_worklist_leaf.py` now counts
`onboarding_trace: 2` in two `itemsByKind` assertions and patches the conversion in `base_cache`. The file
builds its own legacy fixture, so **no catalog change and no re-pin** (the dependency-ownership integration
test passes unchanged). The cases pin the architect rulings of 2026-09-29T18:49:50, 19:23:45 and 19:53:54.

- The onboarding gate's lane row. [52]
- The gate cases' fixture description. [53]

## 260928-MIK-L03 The Currentness Cases, And The Thirty-Sixth Re-Pin

`260928-MIK-L03` (MIK-R03@v2) adds one case module and touches three more:

- [`test_knowledge_currentness.py`](test_knowledge_currentness.py.md) (new, 13 cases, `unit-regression`):
  each entry state on real Git fixtures, the rule-2 precedence, stale proofs, the per-side computation, the
  cache key, Git failures (never cached), and the `knowledge_read` and published-intent surfaces. The
  `INV-HHHHHH` fixture pins the ruling-N1 check order.
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): one lane row at `:112`; every later row moves
  down one line.
- [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md): one consumer on the `package-lock.json` row
  (`:832`).
- [`test_dependency_ownership_ast_helpers.py`](test_dependency_ownership_ast_helpers.py.md): the Thirty-sixth
  re-pin (`11ce8089…` → `dcc1ab1d…`, 16 / 80).

- The lane row. [54]
- The consumer addition. [55]
- The re-pin note. [56]

## 260928-MIK-L08 The Change-To-Knowledge Worklist Cases, And The Thirty-Fifth Re-Pin

`260928-MIK-L08` (MIK-R08@v2) adds two case modules and touches four more:

- [`test_knowledge_worklist.py`](test_knowledge_worklist.py.md) (new, 21 cases): every class and precedence
  rule, line-range mapping, the one-pass scope, the knowledge-side changes, gate linkage (binary and mode
  changes included), the registry and item-ID stability, determinism, `incomplete`, the definition-4 ruling
  and the partial-inventory ruling, on real Git code and converted memory repositories.
- [`test_knowledge_worklist_leaf.py`](test_knowledge_worklist_leaf.py.md) (new, 14 cases): pairing by
  trailer, sync, persistence, the tool, the checklist, the controller-level run, the writer's carry (ruling
  5), a writer-authored proof, the sync recompute that never fails a completed sync, and the converted-base
  cache.
- [`test_knowledge_crossing.py`](test_knowledge_crossing.py.md): the managed crossing sync now also asserts
  no worklist on the unconverted first sync and a `complete`, persisted one after the crossing.
- [`test_memory_quality_runs.py`](test_memory_quality_runs.py.md): the census reaches the checklist as
  `prepared=_PreparedInputs(...)`.
- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md) registers both new modules as `unit-regression`
  rows (`:113`, `:114`); [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md) adds the leaf module as one
  consumer of the `package-lock.json` row, and
  [`test_dependency_ownership_ast_helpers.py`](test_dependency_ownership_ast_helpers.py.md) takes the
  Thirty-fifth re-pin (`b96198c3…` → `11ce8089…`, 16 / 80).

- The two lane rows. [57]
- The Thirty-fifth re-pin note. [58]

## 260928-MIK-L28 The First-Class Test Proof Cases, And The Thirty-Fourth Re-Pin

One module covers MIK-R28, in `unit-regression` directly after the anchor-content row
(`test-evidence-lanes.toml:112`); every later lane row moves down by one line.

- [`test_knowledge_proofs.py`](test_knowledge_proofs.py.md) (22 cases) covers rule 2 (both evidence forms,
  `path::name` and the ruled `path -k name`, the curator's facet, unresolvable evidence reported), rule 4
  (the `proofs` of the `invariant` and `family` views of a converted tree, and none for a database), rule 5
  (the index's "without proof" list and the checklist section that moves no count) and rule 6 (migrated
  evidence listed, then turned into a proof by a curator pass). **Rule 3 and the stale-proof clause are not
  covered here: by architect ruling they move to L08 and L03**, which carry the proof test cases.

Two existing files changed, as the L24 follow-up below required:

- [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md): the new module is appended to three
  `consumer_scope = "exact"` rows (`package-lock.json`, `knowledge_index_test_support.py`,
  `knowledge_writer_test_support.py`), insertion-only; 16 contracts and 80 artifacts, unchanged.
- [`test_dependency_ownership_ast_helpers.py`](test_dependency_ownership_ast_helpers.py.md): the
  Thirty-fourth deliberate re-pin (`6fb4934d…` → `b96198c3…`).

- The lane row. [59]
- The three consumer additions. [60]
- The re-pinned catalog digest. [61]
- The migration-pass case. [62]

## 260928-MIK-L24 The Conversion And Crossing Cases, And The Lane Repaired

Three modules cover MIK-R24, in `unit-regression` directly after L12's writer row
(`test-evidence-lanes.toml:108-110`). This splits L12's two rows: the writer row stays at `:107` and the
anchor-content row moves to `:111`.

- [`test_knowledge_conversion.py`](test_knowledge_conversion.py.md) (6 cases) covers rules 1–4 and 6 over
  fixture cards and a legacy database. That includes the version 1 golden digest, and the evidence-only
  back-to-prose renderer lives there.
- [`test_knowledge_crossing.py`](test_knowledge_crossing.py.md) (8 cases) covers rules 7 and 8: the item
  rules, reference-number collisions, the marker move with its `markers` list, the master-line crossing
  history file, the converted base, and the managed crossing sync on real Git repositories.
- [`test_knowledge_conversion_toolchain.py`](test_knowledge_conversion_toolchain.py.md) (5 cases) covers
  rules 5 and 9: `read_ar_files` on both formats, the reference check and fixer, memory quality on a
  converted tree, the unconverted-line refusal and `memory_init`.
- [`knowledge_conversion_test_support.py`](knowledge_conversion_test_support.py.md) is the shared fixture:
  a code repository, cards covering every row case, and a legacy database in the real column spelling.

Three existing modules changed:

- [`test_read_ar_files.py`](test_read_ar_files.py.md): the ICR-R19 cases measure the database block
  directly, because an unconverted read is `legacy-format`. The two mounted cases are rewritten.
- [`test_knowledge_history_files.py`](test_knowledge_history_files.py.md): the registry has three kinds.
- [`test_dependency_ownership_ast_helpers.py`](test_dependency_ownership_ast_helpers.py.md): the Thirty-third
  deliberate re-pin (16 / 80, `6fb4934d…`). **By architect ruling this leaf repaired the integration lane,
  which was red on its base**: [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md) gains fourteen rows
  for the L12 and L20–L24 shared support and L21's fixtures, plus five consumer additions, insertion-only.
  L28 must add its `test_knowledge_proofs.py` to two of these rows after L24 lands (done by `260928-MIK-L28`,
  see the section above).

- The three lane rows. [63]
- The version 1 golden digest. [64]
- The re-pinned catalog constants. [65]
- The five new shared-support rows. [66]

## 260928-MIK-L12 The Curator Writer Cases

Two modules cover MIK-R12, both in `unit-regression` directly after L23's index rows (`test-evidence-lanes.toml:107-108` on L12's candidate; since L24 the writer row is at `:107` and the anchor-content row at `:111`).
[`test_knowledge_writer.py`](test_knowledge_writer.py.md) (16 collected cases) drives real `tmp_path` Git code and
converted memory repositories built by [`knowledge_writer_test_support.py`](knowledge_writer_test_support.py.md):
the conforming example, the command-line round trip of every kind, idempotence, unresolvable evidence, the
validator refusal, revisions against the base, evidence on another leaf's record stored in this leaf's row,
history-row agreement, rerun removal, the ingest and bootstrap file routes, and the MIK-R04 route rules reported
in the writer but refused at a commit route. [`test_knowledge_anchor_content.py`](test_knowledge_anchor_content.py.md)
(5 collected cases) pins the one definition of an anchor's `content` bytes.

- The two lane rows. [67]
- The world the writer cases run in. [68]

## 260928-MIK-L20 The Migration Census Cases

Two modules cover MIK-R20. [`test_knowledge_census_files.py`](test_knowledge_census_files.py.md) (28 collected
cases) covers the census file formats and route slugs, the mechanical inventory over real `tmp_path` Git
repositories (and the refused unreadable baseline), the census writer (appends that pass the validator,
refusals that write nothing, the unconverted-tree refusal, the repeatable interrupted create) and the nine
census rules in the validator's registry (pinning, append-only statuses and assessments at one base and at a
merge, stable claim fields, and the eight integrity cases). [`test_knowledge_census_report.py`](test_knowledge_census_report.py.md)
(6 cases) covers the Doc12 measures with their counts, zero denominators, the cohort, the report on the
fixture census (the packet's conforming example: 42 claims, 73.8% and 88.6%, 6 of 6 routes migrated), the
governing status across censuses and the `knowledge-census` command. The helper module
[`knowledge_census_test_support.py`](knowledge_census_test_support.py.md) extends the validator's converted
fixture tree with six onboarding routes and the census `wave-1`. The two modules are registered in
`unit-regression` directly after `test_knowledge_validator_routes.py`, which moves L23's three index rows and
every later lane row down two lines; this leaf re-pointed the citations that moved.

- The conforming example's measures carry their counts. [69]
- A recorded assessment is never edited; a correction appends. [70]
- The two lane rows. [71]

## 260928-MIK-L04 The Family Route Cases

[`test_knowledge_family_routes.py`](test_knowledge_family_routes.py.md) (33 collected cases) covers MIK-R04
over the converted Doc14 fixture tree: the Doc14 §4.2 family validated with every route holding
realizations, Coverage and Non-empty naming the family, the route and the path (a proof-only route is
refused), added versus carried absent routes (a merge carries a route either parent lists), the writer-reported
rule set, the root route `.` and its refused spellings, the reported states and the retired exemption, the
mechanical suggestion, and the read-only `knowledge-routes` command. The helper
[`knowledge_validator_test_support.py`](knowledge_validator_test_support.py.md) now carries the family's other
four realizations, so L22's baseline passes with the route rules active. Two assertions in
[`test_knowledge_validator.py`](test_knowledge_validator.py.md) changed: the report-only pin is filtered to
MIK-R22's own rules, and the empty-code-tree case also expects `R04.1-carried-route-absent`. The
[`test_knowledge_index.py`](test_knowledge_index.py.md) module gained one case: a family routed at `.`
governs every path. The new module is registered in `unit-regression` in alphabetical order at `:96`, which
moves every later lane row down one line; this leaf re-pointed the citations that moved.

- The Doc14 family example validates. [72]
- The family's other realizations in the fixture. [73]
- The lane row. [74]

## 260928-MIK-L23 The Derived Knowledge Index Cases

Three modules cover MIK-R23. [`test_knowledge_index.py`](test_knowledge_index.py.md) (22 collected cases since MIK-R04 added its root-route case)
covers rules 1–5 and the Failure rule with real `tmp_path` Git repositories: both tree sources, the key
(the captured tree id, content-only, written nowhere), every rule-3 answer including history rows by subject
and by leaf, freshness after an edit, the `partial` state, the cache (reuse, rebuild, eviction, the
working-tree refusal, index flags) and the `knowledge-index` command.
[`test_knowledge_index_reuse.py`](test_knowledge_index_reuse.py.md) (6 cases) proves rule 6's reuse: parity
of the recorded-scope selection against a legacy database, views and comparison over index files, and the
published-intent selection of a converted, a partial and an unconverted memory root.
[`test_knowledge_index_surfaces.py`](test_knowledge_index_surfaces.py.md) (10 cases) covers the registered
scope over the index, retired records, the mounted `knowledge_read`/`knowledge_diff`/`knowledge_project`
tools, the partial and unbuildable index on every surface, and the unconverted-root preservation case. The
helper module [`knowledge_index_test_support.py`](knowledge_index_test_support.py.md) writes the
conforming-example tree and holds the fixture converter (not the MIK-R24 conversion). The three modules are
registered in `unit-regression` after L22's two validator rows (since 260928-MIK-L20, after L20's two census
rows, which follow the validator rows), which moved every later lane row down three lines; this leaf
re-pointed the citations that moved.

- A file failing its schema marks the index partial and is named. [75]
- Parity of the reused selection over the index and the database. [76]
- Every tool surface reports a partial index as incomplete. [77]
- The three lane rows. [78]

## 260928-MIK-L22 The Knowledge Validator Cases

Two modules cover MIK-R22. [`test_knowledge_validator.py`](test_knowledge_validator.py.md) (37 collected
cases) drives rules 1–9 over converted fixture trees: each case changes one thing and asserts that exactly
the owning rule answers, with its file, field and rule, and every packet example (the parallel mint, the
hand-added `[4]`, the edited or deleted closed history file, the one-parent-deleted merge, the history
rename) is covered. [`test_knowledge_validator_routes.py`](test_knowledge_validator_routes.py.md) (7 cases)
covers rule 8's integration points with real `tmp_path` Git repositories: the tree readers, the commit-route
adapter, the worktree gate (including the fail-closed marker probe), the managed sync after a merge on both
the automatic and the retained-conflict path, and the `knowledge-validate` command. The helper module
[`knowledge_validator_test_support.py`](knowledge_validator_test_support.py.md) assembles the MIK-R21 Doc14
fixtures into one converted tree. Both test modules are registered in `unit-regression` directly after
`test_knowledge_history_files.py` (the route module imports `SyncFixture` from `test_worktree_sync.py`, and
the integration lane is at its 400-case ceiling), which moves every later lane row down two lines; this
leaf re-pointed the citations that moved.

- The baseline and the pinned report-only set. [79]
- The managed sync refuses, keeps the merge staged, and syncs after the repair. [80]
- The two lane rows. [81]

## 260928-MIK-L07 The History-File Cases

One unit module covers MIK-R07: [`test_knowledge_history_files.py`](test_knowledge_history_files.py.md)
(9 tests, 29 collected cases) pins the `ar-history/v1` file shape and owner path, the row-kind registry,
every invariant and family disposition with its covers or examined members, re-anchoring against the
candidate, the revision binding, the freeze predicate (edits, reformatting, deletion, merge parents) and,
in a real `tmp_path` git repository, that two leaves' closed history files merge without conflict.
[`test_knowledge_file_formats.py`](test_knowledge_file_formats.py.md) changed one probe: its unknown-schema
case now uses `ar-census/v1`. The new module is registered in `unit-regression` directly after
`test_knowledge_file_formats.py`, which moves every later lane row down one line; this leaf re-pointed the
citations that moved.

- The freeze cases. [82]
- The parallel-merge case. [83]
- The lane row. [84]

## 260928-MIK-L21 The Text Knowledge Format Cases And Their Fixtures

Two hermetic unit modules cover MIK-R21: [`test_knowledge_file_formats.py`](test_knowledge_file_formats.py.md)
(IDs with golden derived values, all ten record kinds, sidecar/reference/anchor/link refusals, locations,
and the Doc14 §4 worked examples) and [`test_knowledge_file_canonical.py`](test_knowledge_file_canonical.py.md)
(formatter idempotence and content preservation, the identified-entry sort rule, refusals, and the
`knowledge-format` command end to end). The worked examples live as nine canonical JSON fixtures in
`fixtures/knowledge_files/` (each with its own card); the formats module requires the directory to hold
exactly those nine and each to round-trip byte for byte. Both modules are registered in `unit-regression`
directly after `test_knowledge_citation_bindings.py`, which moved every later lane row down two lines (since
260928-MIK-L04 the `test_knowledge_family_routes.py` row sits between them, in alphabetical order).

- The nine fixtures and the model each must parse as. [85]
- The two lane rows. [86]

## 260921-ICR-L44 The Member-Source Locator Cases

One ordinary unit module joins the family review cases: `mcp/tests/test_review_family_member_sources.py`
(six cases) drives the roster owner over two real datasets and two real Git commits and pins that each
member source carries its own recorded locator, resolved ranges and locator state — two members in one
file at distinct ranges, an unchanged range on both sides of a changed file, explicit unresolved states,
a recorded range past the blob end, a doubly-defined symbol, and unchanged legacy fields. The value module
`test_review_family_context_values.py` gained the matching construction case. The new module is registered
in the `unit-regression` lane and as a consumer of `read_scope_test_support.py`; both insertions moved the
lines below them by one.

- The module's own statement of what it pins. [87]
- Its lane registration. [88]

## Public exact-sibling family updates

The family-retention suite drives baseline and successor authoring through separate ordinary leaf scopes. It covers exact old/new rosters, unchanged old rows and provenance, the one genuine new invariant, projected preview, exact retry, invalid/foreign references and retain/retire conflicts. Controlled fixture results do not replace actual project publication.

- Public successor publication preserves exact stored siblings across leaf scopes. [89]

## Reviewer delivery regressions

test_curator_candidate_progression.py adds exact working-source capture, predecessor-bound progression, original-baseline preservation and source-movement refusal checks through the ordinary writer.

test_curator_scope.py covers authored scope and exact-retry boundaries. test_review_recorded_knowledge.py exercises exact historical memory endpoints and family continuation. test_review_unchanged_knowledge.py exercises the normal live code-only pair and reopened record. These are focused regression evidence; mounted workflow proof remains separate.

- `test_authored_scope_survives_ingest_and_scope_change_is_not_an_exact_retry` owns the behavior described above. [90]

## 260921-ICR-L32 The Over-Rail Module Is Split, A False Seat Sentence Is Corrected, And Four Git Cases Land

Four test-side movements, and the first is a **standing rail condition** restored rather than a new case.

**The split (D54).** `mcp/tests/test_curator_family_authoring.py` crossed the 1200 hard rail during L28's own
fix round (1056 lines and 15 cases when that leaf took its census, **1320 lines** when it landed), which broke
L22's F5 ruling that the ≥1200 census must not gain a new offender. `260921-ICR-L32` extracts a purpose-named
sibling — **818** lines plus **`mcp/tests/test_curator_ingest_write_and_retention.py`**, 578 lines — so the
census returns to its pre-L28 value in both scopes (**27** under the rail's own `git ls-files '*.py'` file set,
**26** under the narrower `mcp/`-only one, each quoted with its scope because the number is scope-dependent).
The case population moved rather than shrank (20 collected: 11 + 9), the catalog still reports **16 contracts /
66 artifacts**, its `LIFECYCLE_CATALOG_SHA256` pin was re-taken from a fresh `sha256sum`, and the two
`consumer_scope="exact"` rows the shipped census named were derived from **its own failing-run output**
(`mcp/tests/fixtures/repository_profiles/node/package-lock.json` and
`mcp/tests/snapshot_lifecycle_test_support.py`, each missing this module) rather than guessed. No limit was
widened and no `# noqa` was added.

**The false sentence (F1 of the round-one verdict, `blocking`).** The bootstrap-procedure case module asserted
in four places that a taskless curator seat is refused — true when L27 wrote it, false the moment L32 changed
the constant, and false about its own module 200 lines above the case that asserts the admission. All four
copies were corrected to the delivered truth, and the case names they cite now resolve (8/8).

**The Git cases (D02, and D02's own bite-proof).** Four cases in `test_master_net_generation.py` drive the
NUL-safe path-enumeration family over an eight-name fixture that includes a literal backslash on each side —
tracked and untracked — plus a tab and a newline; restoring the old `\` → `/` rewrite makes two of them fail,
which is the property the first verdict found unpinned.

**`test_memory_branch_authority.py`** carries the updated taskless-set pinning assertions and the route-level
five-arm status case, and `test_tool_refusal_conformance.py` gains the guard that reads the mounted refusal's
own detail when it is asked to name the write plane.

## 260921-ICR-L34 The Comparison-Generation Module Gains A Fourth Case, And It Protects The Recording Half Of Its Journey

This route's own change for `260921-ICR-L34` is one case in one module, and it belongs at this altitude
because the defect it seals was invisible to every fixture shape this route already had.

**The module.** `mcp/tests/test_knowledge_ingest_comparison_generation.py` (3 → **4** cases, 323 → 370
lines) owns the successful journey of one comparison's before side — the shared-path fixture, the two
retries and the deliberate rebase. Its three cases end with the before half correctly *placed*; the
fourth, `test_the_placed_baseline_is_opened_under_its_own_recorded_namespace` (`:329-370`), protects the
step after placement: **recording** the comparison. Recording retains each half by copying it through
the storage owner, and that owner refuses a dataset opened under a namespace it is not bound to.

**The defect, and why no existing fixture could see it.** The namespace was read from
`candidate-receipt.json` **alone**. A *candidate* half has one, because an admission wrote it; a
**before** half placed from a named `--baseline` never does, because a published dataset is not an
admitted candidate — it carries `baseline-generation.json` instead. The read therefore fell back to the
requested repository name while the bytes are bound to a namespace id, and the freeze refused
`candidate_dataset_absent`. **Every leaf on the ordinary `knowledge-ingest --baseline` continuity route
produced a comparison that could not be frozen**, and the fixtures that pass hand-assembled pairs
exercise the *no-record* shape, so the seven modules that already drove this surface were blind to it;
the first-generation path hid it too, because the empty before half it creates is built by the
candidate-creation owner, which does leave a receipt beside it. The rule is now **the record beside the
bytes** — the receipt when there is one, otherwise the before half's own generation record, with the
requested repository used only when neither exists.

**What the case measures, and that it bites.** It asserts first that the requested repository and the
dataset's own namespace **differ** (so it cannot pass vacuously), then opens the half under
`review_namespace` and reads its own snapshot identity back through `open_read_only_store`. Reverted in
a scratch copy of the module it fails at `:362` with `+ agents-remember` — the exact value that produced
the recorded refusal. This is the **narrowest possible** case for the rule: it drives the real
placed-baseline journey through the shipped CLI and adds no second fixture shape.

- **The case `260921-ICR-L34` adds, and the three owners it names: the namespace read, the record it now consults, and the store it opens under that namespace.** [91]
- The three cases whose journey this one completes, and the shared-path fixture they start from. [92]
- The rule the case seals, and the second record that answers it. [93]

## 260921-ICR-L25 One Case Renamed, One Route-Level Case Added, And No Lane Or Catalog Row

`mcp/tests/test_knowledge_review_source_endpoints.py` grew **1434 → 1515 lines** and this route's case
inventory moved with it, but nothing structural was added: **no new module, no new lane row, no new
consumer row and no catalog re-pin.** What is new is one **route-level** case, and the reason it exists
is the distinction between a unit answer and a served one.

`test_an_unrecorded_committed_endpoint_is_refused_rather_than_read_from_head` is renamed to
`test_an_unrecorded_committed_endpoint_is_answered_with_its_own_state_rather_than_read_from_head`,
because the endpoint is no longer refused: it is **answered** with the body's `state="unrecorded"` plus
the route's own `stateDetail` sentence. The case keeps what mattered — `HEAD` is never substituted for
the missing endpoint and never named in the detail, and the counters stay a measured zero — and it now
also asserts the part that makes the state a **discriminator rather than a constant**: after
`fixture.recorded_range(head)` the same view reads `state="recorded"` with an empty `stateDetail`.

`test_the_route_answers_an_unrecorded_committed_view_without_a_status_error` is **new**, and it is the
whole of register B6: the pure function answering `unrecorded` is not enough, because the defect was
that the **route** turned it into a `404` — which the browser logs as a console error on the page whose
accepted criterion is zero. It registers the real routes through `register_changeset_routes` (the new
import), reads `GET /api/changeset/task?…&mode=committed` and asserts **200**, that the state survives
serialization, and — so the fix cannot have been bought by answering everything — that an **unknown
leaf is still a named `404`**.

- **The renamed case: the unrecorded endpoint answered with its own state, the head absent from the detail, and `recorded` read back after `recorded_range` so the state discriminates.** [94]
- **The new route-level case: the served `200`, the state after serialization, and the unknown leaf that is still a named `404`.** [95]
- The one-half degradation, unchanged, whose docstring now records that the code side reads `recorded` beside it. [96]
- The producer both cases drive. [97]

## 260921-ICR-L43 The Attributed Source-Content Cases

One ordinary unit module joins the review's source-content evidence:
`mcp/tests/test_knowledge_review_attributed_source_content.py` (eight cases) measures that an unchanged
path a realization recorded in the same comparison's knowledge links opens at the exact endpoints
without entering the inventory, and that unlinked, cross-comparison, unrecorded-superseded and
whitespace-padded paths refuse, with unreadable knowledge refusing as *undetermined*. Unlike its
sibling `test_knowledge_review_source_content.py` (whose fixture binds no knowledge and whose
confinement case is kept), its fixture builds both knowledge halves. It is registered in the
`unit-regression` lane and as a consumer of `read_scope_test_support.py`; both insertions moved the
lines below them by one, and the cards citing those files were re-pointed.

- The module's own statement of the admitted population and its cases. [98]
- Its lane registration beside the sibling module. [99]

## 260921-ICR-L42 The Bounded Task-Document Body Read Cases

One ordinary unit module protects the cost and the meaning of the dashboard's single task-document
read: `mcp/tests/test_task_document_body_lookup.py` (3 functions, 5 cases). The cost is checked by
**counting what one call touches**, the directories it lists and the task JSON it reads, at 4 and at 40
unrelated tasks. It is not checked by timing, so the case is deterministic and names the offending
file. The meaning is checked by comparing the bounded read, byte for byte, with the corpus-wide join
it replaced, over a corpus seeded with decoys: a `notes/` copy, an archive, a symlinked repository
folder, and a schema-less master-shaped document. Each decoy fails a specific mutation. The
enumeration case keeps the earlier recursive glob inline as the reference that `_iter_task_json` must
equal. Registered in `unit-regression` at `:208`; that insertion moved every manifest line below it by
one, and the cards citing those lines were re-pointed.

- The module's own statement of the read bound and the preserved projection. [100]
- The count-based scaling case. [101]
- Its lane registration. [102]

## 260921-ICR-L45 The Per-Target Realization Rationale Cases, And Two Builders That Now Author Rationale

One ordinary unit module joins the curator-ingest evidence: `mcp/tests/test_curator_realization_authoring.py` (12 cases)
drives the real `ingest_curator_list` and proves that each target stores its own authored rationale and
role over an explicit entry-level default; that a target with no rationale, a non-text value, an unknown
role, an over-long rationale, a non-text route or the placeholder route word `absent` (any case) refuses
only its own entry, by name, before anything is written; that nothing is generated; and that already
committed operations — including ones the **real base writer** committed with no rationale — replay and
publish unchanged, while a recorded-but-uncommitted allocation is still refused. The base-writer case
`git archive`s the base commit and skips with a reason where that history is absent; a history-free guard
carries the same protection. Two shared builders changed with it: `test_knowledge_curator_ingest_list.py`'s
`entry` states an explicit entry-level `realization_rationale` default, and `test_knowledge_bootstrap.py`'s
`entry` gives each target its own `rationale`, because the writer both suites drive now refuses a new
realization without one. Registered in `unit-regression` at `:24` and as an exact consumer in two
`evidence-lifecycle.toml` artifacts (`:699`, `:1286`); both insertions moved the lines below them, and the
cards citing those files were re-pointed through the exact line map.

- The module's own statement of the cases it proves. [103]
- The committed-versus-recorded distinction for the admission exemption. [104]
- The ingest-list builder's explicit entry-level default. [105]
- Its lane registration. [106]

## 260921-ICR-L55 The Notes-Listing Cases

One ordinary unit module is the first Python evidence for the coordination-notes routes:
`mcp/tests/test_notes_listing.py` (5 functions, 6 cases). The listing's cost is checked by **counting
`realpath` calls and refusing any note-content open**, at 6 × 1 B and at 240 sparse 64 MiB notes: 4
calls at both sizes, whereas the old walk made 49 and 751. It is not checked by timing. The listing's
meaning is checked as **exact wire bytes** over a tree holding every entry kind the walk classifies,
including looping and file-traversing symlinks (the L55-R1-F1 regression). A monkeypatched open swaps
a directory for an escaping symlink at the moment the walk opens it, and the case requires the
directory to be refused. Registered in `unit-regression` at `:162`; that insertion moved every manifest
line below it by one, and the citation-table rows citing those lines were re-pointed.

- The module's own statement of what it protects. [107]
- The count-based scaling case. [108]
- Its lane registration. [109]

## 260921-ICR-L56 The Anchor-Observation Memo Cases

`mcp/tests/test_read_anchor_memo.py` (8 functions, 9 cases) pins the process-lifetime memo behind anchor
observation against a **real Git repository**, with spies that count Git calls and parses while
delegating to the real runner and extractor. Its route-level lesson is the review's: a memo keyed by
immutable ids is safe for *content*, never for *availability* — the pruned/revoked case warms the memo and
then requires every anchor to be reported `recorded_object_unavailable`, and the isolation cases use an
empty and a blobless neighbour repository so no answer crosses a repository root or a grammar. One
`unit-regression` row, inserted at `:173`, moved every manifest line below it by one.

- The module's own statement of what it protects. [110]
- Availability loss reported, not remembered. [111]
- Its lane registration. [112]

## 260921-ICR-L57 Three File-Size Splits, And A Catalog Pin One Red Case Was Hiding

The master's exit gate found three case modules over the 1200-line rail. `260921-ICR-L57` split each by
moving one cohesive section verbatim into a new ordinary unit module. Each new module imports its
sibling's helpers and defines its own three-line fixture. No case was added, dropped or changed: the
collected node names are identical per pair apart from the module name.

| Original (lines, cases after) | New module (lines, cases) | What moved |
| --- | --- | --- |
| `test_knowledge_diff_scope.py` (790, 13) | `test_knowledge_diff_attribution.py` (626, 9) | the `ICR-R04` attribution-partition cases |
| `test_knowledge_review_source_endpoints.py` (1093, 14) | `test_knowledge_review_attribution_precedence.py` (450, 6) | attribution precedence across knowledge availability, and the two receipt cases |
| `test_knowledge_review_surface.py` (1056, 22) | `test_knowledge_review_resolution_and_route.py` (470, 9) | candidate resolution, the before-half refusals, the transport and the loader |

**A split test module owes three declarations, and the gate checks all three.** It needs a lane row
(placed beside its sibling in `unit-regression`), a path on every exact `consumers` row the ownership
census derives for it (here the diff-scope and read-scope support artifacts), and a deliberate catalog
re-pin, because those consumer paths change the catalog's bytes. The same leaf added the consumer paths
of eight ICR case modules that had landed undeclared. It found that the catalog pin had been stale since
L43–L45, and the Thirty-second re-pin repairs it. That staleness was invisible because the
inventory-closure assertion fails before the byte assertion runs. Separately, the facet seed-page
digests were re-measured for L44's additive `resolved_ranges` field, with the cause and original digests
kept beside the constants.

- The three new lane rows beside their siblings. [113]
- The Thirty-second re-pin. [114]
- The re-measured seed-page digests and their stated cause. [115]

## 260921-ICR-L27 The Bootstrap Procedure's Seven Cases: Four Readings, One Base Defect, Three Consumer Rows

`260921-ICR-L27` (`ICR-R27@v1`) adds **one** ordinary unit module,
`mcp/tests/test_knowledge_bootstrap_procedure.py` (**453 L**, **seven** cases), together with **three
consumer rows** across the route's two census TOMLs (`mcp/tests/evidence-lifecycle.toml`,
`mcp/tests/test-evidence-lanes.toml`) and the re-pin of
`mcp/tests/test_dependency_ownership_ast_helpers.py` (**896 → 917** lines, under the 1200 hard rail). No
production module is added.

**Why the cases are split four ways.** The delivery is **instructions**, and an instruction can be false
in independent ways: the procedure may not be served at all, the commands it prints may not exist on the
shipped command line, the seats it names may not be admitted by the opener, and the instructions that
*are* delivered may never name it. Each reading has its own case(s), so one green run cannot be read as
the others:

- the **catalog** publishes the procedure, and the bytes a reader receives are compared with the
  canonical tree's rather than trusted;
- every **printed invocation** is filled and run through the real parser, grading subcommand declaration
  and option ownership together while executing nothing;
- the **seat gate** is measured at the route by observed status, with the admitted arms as the control,
  because the launch *compiler* accepts any declared role while the *opener* refuses a document-less
  session for every role outside the taskless set;
- the **delivered instructions** name the procedure — the taskless bootstrap seat's capsule, the curator
  shape the compiler produces, and the two served skills an ordinary setup follows.

**The case name that had to change is part of the record.** An earlier revision asserted the compiled
capsule of a *taskless curator* while the shipped opener refused exactly that session
(`400 task-binding-required`), and the round-one verdict called that mismatch `blocking`. The case is now
`test_the_compiled_curator_shape_names_the_procedure_it_would_receive` — named for the compiler, because
that is all it measures — and three route-level cases carry the admission reading instead.

**Base defect, reproduced rather than asserted.** On the leaf's base `06ed70cf` the module is **5 failed
/ 2 passed**; on the candidate it is **7 passed**. The two base-passing cases are the seat gate itself,
disclosed as the measurement that constrained the correction rather than as delivered work — a case that
passes on base cannot be evidence that the leaf delivered anything.

**What this route should carry forward.** The three consumer-row additions shift the line numbers of the
tables they are inserted into, which is why several cards — and this overview — that cite those two TOMLs
by line were re-anchored in the same curation pass rather than left to a later one.

## 260921-ICR-L28 The Curator Family Cases: One Module, Twenty Cases, One Lane Row, Two Consumer Rows

`260921-ICR-L28` (`ICR-R28@v2`) adds **one** ordinary unit module,
`mcp/tests/test_curator_family_authoring.py` (1320 L, **twenty** cases), plus its `unit-regression` lane
row in `test-evidence-lanes.toml`, two consumer rows in `evidence-lifecycle.toml` and the
`LIFECYCLE_CATALOG_SHA256` re-pin in `test_dependency_ownership_ast_helpers.py`. The catalog population
is unchanged at **16 contracts / 66 artifacts**, because the module joined lane rows that already
existed rather than creating a population.

**What the cases drive is the real operation**: `ingest_curator_list` over a real pair of repositories
beside a real `ar-series-contract/v1` enclosure, with the CLI (`cli.__main__.main`) and the public read
route (`open_read_context` → `read_knowledge_view`) exercised in their own cases. **Every claim that
matters is asserted against the reopened dataset** — `table_counts`, `members_of`, `guarantees`,
`conditions_of`, `provenance_of`, `family_memberships` — so the report is a claim under test and never
the oracle.

**The fixture is imported, not duplicated.** The module takes `SourcePair`, `pair`, `entry`, `target`,
`symbol`, `AUTHORIZATION`, `CODE_FILE`, `CODE_SYMBOL` and `GONE_PATH` from
`test_knowledge_curator_ingest_list`, so there is one enclosure shape in the suite rather than two; the
module's own helpers build nothing but an authored decision and one declared source.

**The case that exists because a false sentence was reachable.**
`test_a_replayed_revision_still_writes_the_family_plane_its_entry_now_authors` step 1 authors an entry
with a deliberate no-family outcome; step 2 re-runs the **same entry id** with the same targets and a
new membership, then counts rows in the dataset — the four family tables, the exact stored member set,
the stored guarantee text, and the allocation journal's `familyRevisionId` against the reported
guarantee id. It fails the moment a run can report a family row it did not write.
`test_an_exact_replay_writes_nothing_and_spends_no_identity` is its deliberate complement and is **not**
presented as proof of the fix: on a fully-stored list both the old and the corrected predicate agree, so
it is not the discriminating case.

**The eight properties, one case group each.** A declared family stored as **its own** guarantee with
exact memberships; one revision in **two** families and one family across revisions; membership never
**inferred** from a file or a route; the **deliberate** no-family outcome retained with its basis while
an unexamined entry is reported as unexamined; a changed guarantee stored as a **successor** that
preserves the earlier membership, and a changed guarantee under one key **refused** rather than
rewritten; a stored revision **examined** and joined without being re-declared; an external source
retained in a **bounded manifest** with no source anchor fabricated for it; and a stored membership
**retired** by the identity this run read.

## 260921-ICR-L21 The Final-Output Cases: One Module, Eleven Cases, One Lane Row, Three Exact-Scope Consumer Rows

`260921-ICR-L21` (`ICR-R21@v1`, review-to-closeout identity continuity) adds **one** ordinary unit module,
`mcp/tests/test_review_final_output_receipt.py` (871 L, **eleven** cases), plus its lane row in
`test-evidence-lanes.toml`, three `consumer_scope = "exact"` rows in `evidence-lifecycle.toml` and the
`LIFECYCLE_CATALOG_SHA256` re-pin in `test_dependency_ownership_ast_helpers.py`. The catalog population is
unchanged at **16 contracts / 66 artifacts**.

**What the cases drive is the whole operation, against the store's own reopened truth**: a live enclosure
with two real datasets and a real captured candidate, the real `freeze_review_comparison`, the real
publication owners (`freeze_closed_snapshot` + `publish_prepared_snapshot`) at the repository's declared
location, and the real `worktree_closeout_preview_tool` / `worktree_closeout_apply_tool` /
`worktree_integrate_tool`. Every identity the receipt recorded is then compared against the generation
store, the Git objects and the published dataset — and the record is re-read from disk — so **no case
asserts a prebuilt payload**.

The three packet examples are cases rather than prose: the conforming pair, a published dataset the
review never compared (which must read `moved` and must **not** contain the coverage string), and a moved
candidate whose prior receipt keeps byte-identical content while a successor supersedes it by naming it.
Four further cases exist because a round-1 verifier reproduced a false sentence and an unprotected
narrowing: the preview's selection sentence may never claim a recording the store lacks; a selected
knowledge operand with nothing published is `unmeasured` (never `bound`); a forged `bound` in canonical
bytes reads back `unreadable`; and the reopened generation reports the delivered output phase by phase.

**Two limits are recorded rather than implied.** The browser halves of A17/A20/A22 remain **ICR-R25@v1**'s
per `notes/05-acceptance-plan.md`; and the failed/partial-transaction clause is evidenced by the
no-generation case plus the `ok`-gated attachments plus the fact that recording happens only after the
contract write — not by a crashed-closeout fixture carrying a frozen generation.

## 260921-ICR-L8 The Relationship Cases: Three Modules, Twenty-Three Cases, Three Lane Rows, Six Consumer Rows

`260921-ICR-L8` (`ICR-R08@v1`, movement and relationship evolution) adds **three** ordinary unit modules
and no fixture of its own. Every population is authored through the public store operations over the
existing `test_knowledge_review_source_endpoints.py` enclosure and read back through the production
composition (`read_knowledge_review`), and the two later modules import the first one's builders rather
than duplicating them:

- `test_knowledge_review_relationship_movement.py` (891 L, **eleven** cases) — the packet's own cases:
  the moved realization under one preserved identity, the non-conforming after-only reading measured as
  a population the after side cannot produce, the withdrawn realization that keeps its deleted file and
  its reason, present-outside-selection never rendered as a deletion, the labelled Git rename inference,
  the same rename with no authored edge producing a retraction and an addition, the authored split and
  merge, the family reassignment, the route reassignment, the ungoverned identity that is never placed
  in the repository root, and the unresolved anchor that keeps its own state and reason.
- `test_knowledge_review_relationship_reach.py` (591 L, **seven** cases) — the master's ruling: a member
  identity's movement displayed at its own established head, a multi-ended line unresolved and never
  denied, a withdrawal that names the row it must not deny, member-wise family pairing, the stated
  pairing basis, an address resemblance that never pairs, and the two rename non-pairing states.
- `test_knowledge_review_relationship_line.py` (405 L, **five** cases) — the authored line: a split whose
  recorded relationships are named, a multi-ended line that never claims a unique head, the split-only
  negative complete over the revisions read, an intermediate descendant that is displayed, and a
  membership moved onto an unselected family revision.

**Their governed registrations are the other half of the leaf's footprint.** Each module is a
source-derived consumer of **both** exact-scope rows in `mcp/tests/evidence-lifecycle.toml` (the
Eighteenth, Nineteenth and Twentieth deliberate re-pins; the catalog is 1689 lines and its digest is
`d2d6dc6a…`), and each has an `unit-regression` lane row in `mcp/tests/test-evidence-lanes.toml` at
`:114-116`, which moves every line below `:113` by three.

- **The movement module's own statement of what it measures, and the fixture it authors through the store's operations.** [116]
- **The packet's conforming example and the non-conforming reading measured beside it.** [117]
- The withdrawal boundary and the labelled inference with its no-fabrication control. [118]
- The family, route and ungoverned cases, and the unresolved anchor that keeps its reason. [119]
- **The reach module's own statement of the five states the ruling turns on, and the member-head case.** [120]
- The multi-ended line, the named-instead-of-denied withdrawal, and the member-wise family pairing. [121]
- **The authored-line cases: the split that names its rows, the multi-ended line that never claims a head, and the intermediate descendant that is displayed.** [122]
- **The three lane rows and the six consumer rows the same change registered.** [123]

## 260921-ICR-L9 The Complete-Subject-Catalogue Cases: One New Module, Ten Cases, One Lane Row, Two Exact-Scope Consumer Rows

This route gained **one module** — `mcp/tests/test_review_subject_catalogue.py`, 545 lines and ten
cases — and the manifest rows that let it be collected: one `unit-regression` lane row
(`test-evidence-lanes.toml:161`, newest-last in file order, 337 → 338 lines) and **two** appended
consumer paths on the exact-scope `[[artifact]]` rows of `mcp/tests/evidence-lifecycle.toml`
(`:1416` on `diff_scope_test_support`, `:1453` on `read_scope_test_support`; 1681 → 1683 lines,
re-pinned to `8d60a34c…` as the Seventeenth deliberate re-pin). The module is the **population half**
of ICR-R09@v1: it drives the production catalogue read and the production review composition over
real two-snapshot populations built through the shipped store operations — copies of the shared diff
fixture extended by `create_invariant`/`create_revision` (retired and added subjects) and
`insert_invariant_identity` (a recorded identity with no authored content), never hand-written
payloads. The ten cases pin: the union of both snapshots' identity tables with labels and per-row
presence; the globally kind-grouped order **with retired invariants present** (the fix-round F1 pin);
a retired `before_only` row opening one-sided; an `after_only` row listed beside it; the
statement-free family; **every** row opening through the normal review (falsifying
"only the first is reachable"); a recorded-but-unselectable subject staying listed with the
comparison's own refusal carried by its open; the labelled totals; zero subjects as a valid catalogue
beside a measured source inventory; and the no-comparison tripwire (both `diff_knowledge_scope`
bindings rigged; the catalogue read answers with the whole list without entering the comparison).
The KS-era mechanism block in `test_knowledge_review_surface.py`'s pane-types case — which measured
the old compare-to-earn-a-row entry mechanism the packet deletes — was re-contracted to the catalogue
in the same change. Routed, not closed: paging is R10's, browser journeys R24's, relationship
traversal R08's, labels R26's.

- **The new module's own statement of what it measures, and its lane and consumer registrations.** [124]
- **The union and the kind-grouping pin, and the bounded-loading tripwire.** [125]
- **The re-contracted mechanism case in the surface module.** [126]

## 260921-ICR-L7 The Explicit-Revision-Comparison Cases: One New Module, Ten Cases, Two Rewrites, And One Lane Row

This route gained **one module** — `mcp/tests/test_knowledge_review_revision_selection.py`, 615 lines
and ten cases — and one lane row, which is the first thing on this route a reader should check because
it is what keeps the module selected at all. The module is the **policy half** of ICR-R07@v1: it drives
the real two-snapshot comparison over **real** snapshot pairs built through the public store operations
(`_build_pair` over `_build_snapshot`, one invariant with fixed recorded statements, chained or forked),
then runs the exact head-selection function the review adapter calls (`_select`). Nothing re-implements
a read, a comparison or a predecessor lookup — except the two fault-injection cases, which say so in
their own docstrings (a corrupt snapshot cannot be authored through the validating write path, so the
corruption is inserted as SQL into a scratch copy). The final case closes the loop through the served
payload: `compose_review` over two real Git trees renders the head pair's own recorded statements as
`present` beside the compared selection.

**The lane row, and the pure-move consequence a citation into that manifest must know about.**
`mcp/tests/test_knowledge_review_revision_selection.py` is registered in the **`unit-regression`**
lane at `mcp/tests/test-evidence-lanes.toml:113-113` — the lane the module declares for itself through
`pytestmark = pytest.mark.evidence_unit`. The row is **inserted mid-list** in the knowledge run between
`mcp/tests/test_knowledge_review_one_sided_statements.py` (`:110`) and
`mcp/tests/test_knowledge_review_source_endpoints.py` (`:112`), so every row and lane key at or below
`:111` reads one line lower than the last account recorded: `public-contract` `:212` → `:213`,
`integration` `:216` → `:217`, `architecture-fitness` `:294` → `:295`,
`provider-conformance` `:316` → `:317`, `stress-durability` `:332` → `:333`,
`migration` `:334` → `:335`. Measured on this leaf's candidate from the manifest and the modules on
disk: **318 declared entries against 318 modules**, 0 declared-but-absent, 0 present-but-undeclared,
**336 lines**, `unit-regression` **206** — the one population that moves. `evidence-lifecycle.toml` is
untouched, so no catalog digest moves.

**The ten cases and the property each one owns.** Two chain defaults with exact selected revision ids
(`r1`-vs-`r3`, and the advanced `r2`-vs-`r3`); selectable history (the default still compares the heads
while `r2` is compared on demand through the per-side explicit selector); two fork ambiguities (both
heads listed, no pair); the known-empty side as a removal under the R06 contract; the successor cycle
and the dangling authored edge as unresolved selections naming the reason; order-independence (the
successor relation beats sorted position); and the pane case. **Exactly two existing surface cases were
rewritten from the old both-sides rule to ambiguity assertions** (`test_knowledge_review_surface.py`
1261 → 1314 lines): the pane case and the knowledge-only case now assert the explicitly ambiguous
selection with both sides `unresolved`, because the fixture's retry identity is branchy on both
snapshots.

- **The new module's scope statement: heads from authored successors, the six load-bearing properties, and the fault-injection disclosure.** [127]
- The unit-regression registry includes the revision-selection test module. [128]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [129]
- **The fixture that makes a chain, a fork and a history real: two independently built snapshots under one namespace through the public write path.** [130]
- **The two chain defaults with exact selected revision ids.** [131]
- **The two fork ambiguities and the two lineage failures, each with no pair recorded.** [132]
- **The pane case that closes the loop through the served payload.** [133]
- **The two rewritten surface cases: the old both-sides assertions replaced by ambiguity assertions.** [134]

## 260921-ICR-L13 The Master-Net Generation Cases, And The One Lane Row That Confirms Them

This leaf adds **one** case module, `mcp/tests/test_master_net_generation.py` (488 lines, nine cases),
and **one** lane row for it.

**The module is the production-composition evidence for `ICR-R13@v1`.** Every case builds a real
series contract on disk, real leaf enclosure contracts, real code and memory repositories with real
branches, and the real `master_changeset` / `master_file_diff` resolution plus the HTTP routes that
serve them: add-then-remove across two leaves nets to exactly `[]` with zero counters while both leaf
rows stay nonzero; net-zero source with a one-line `memory.md` effect; pinned generation reopening
byte-identically after branch advance (`superseded`) while the live view moves on; pinned file
expansion returning the recorded bytes; broken child leaving the net intact; missing endpoints
refused by name with no tip substitution; live leaves labelled `working` with their drafts out of
the net; routes carrying the generation with its named refusal; and the F1 post-validation diff
failure refused as `unresolvable`, never reported as zero.

**The module is hermetic, and the lane row is what makes it run.** `pytestmark =
pytest.mark.evidence_unit`; it touches no live coordination tree, no network and no service — so
`unit-regression` is the behaviour-preserving classification rather than a budget convenience. Its
one row is `mcp/tests/test-evidence-lanes.toml:114`, inserted mid-list after
`mcp/tests/test_knowledge_review_source_content.py` at `:113` (L16's row now reads `:115`).
**It is the fifth mid-list insertion this master has made into that lane** (after L14, L3, L16 and
L7's `:111` revision-selection row above it), so every lane key and every row at or below it moved one
line down, and the manifest now measures **319 declared entries against 319 modules on disk, 0/0
undeclared or absent, over a 337-line file** with `unit-regression` at **207** rows.

`mcp/tests/evidence-lifecycle.toml` is **unchanged**, so `LIFECYCLE_CATALOG_SHA256` is **not** re-pinned:
the module registers no contract and no artifact and consumes no catalog-registered support module.

- **The module's own statement of what it measures — endpoint-correct, generation-bound, through the operations the dashboard really calls.** [135]
- **The shared master-shaped world and its builder.** [136]
- **The lane row, and the manifest extent it sits in.** [137]

## 260921-ICR-L16 The Review-Route Refusal Cases, And The One Lane Row That Confirms Them

This leaf adds **one** case module, `mcp/tests/test_review_route_refusals.py` (204 lines, six cases), and
**one** lane row for it.

**The module is the fast transport contract for the review route's refusals.** The route answers a refusal
with the change-set routes' `400`/`404`/`503` idiom and puts the answer in the body, in one of two shapes —
this route's own typed refusal (`state = "refused"`) or one of the transport-level bodies it builds
itself. The cases drive the **real** `register_review_routes` on a bare `FastAPI()` app with injected
ports, and assert the bodies field by field: an unwired adapter answers `503` with an actionable body on
both routes; an unadmitted selector is refused by the transport **before the port runs** (proven with a
port that raises if called) and names the offending input and both admitted kinds; the two port-level
exception mappings this leaf made actionable are asserted with their new `nextAction` (and the
not-found path in both spellings); a typed refusal travels whole with **no `payload` key**, so it cannot be
read as a degraded success; and a parametrized case pins the status family from the refusal's own code
(`candidate_dataset_absent`/`candidate_not_live`/`candidate_unresolved`/`subject_unresolved` → `404`,
`comparison_refused` → `400`) through the entry route.

**The module is hermetic, and the lane row is what makes it run.** `pytestmark =
pytest.mark.evidence_unit`; the module builds its own app, names no real root
(`/nonexistent-workspace`, `/nonexistent-coordination`, …) and touches no enclosure, network or
temporary repository — so `unit-regression` is the behaviour-preserving classification rather than a
budget convenience. Its one row is `mcp/tests/test-evidence-lanes.toml:113`, inserted mid-list after
`mcp/tests/test_knowledge_review_source_content.py` at `:112`. **It is the third mid-list insertion this
master has made into that lane**, so every lane key and every row at or below it moved one line down
(`public-contract` `:211` → `:212`, `integration` `:215` → `:216`, `architecture-fitness` `:293` → `:294`,
`provider-conformance` `:315` → `:316`, `stress-durability` `:331` → `:332`, `migration` `:333` → `:334`),
and the manifest now measures **317 declared entries against 317 modules on disk, 0/0 undeclared or
absent, over a 335-line file** with `unit-regression` at **205** rows.

`mcp/tests/evidence-lifecycle.toml` is **unchanged**, so `LIFECYCLE_CATALOG_SHA256` is **not** re-pinned:
the module registers no contract and no artifact and consumes no catalog-registered support module, which
the census gate (`test_dependency_ownership_ast_helpers.py`) confirms unchanged.

- **The module's own statement of what it is — the fast transport contract, driving the real route — and of the two shapes a refusal arrives in.** [138]
- **The module's own definition of actionable, asserted as a set inclusion in every transport-level case.** [139]
- **The bare app with the real routes registered, which is what makes the ports the only injected part.** [140]
- **The conforming example at the transport, with no `payload` key so a refusal cannot read as a success.** [141]
- **The status family derived from the refusal's own code.** [142]
- **The lane row, and the manifest extent it sits in.** [143]

## 260921-ICR-L3 The Source-Content Cases, And The One Lane Row That Moved Every Manifest Line Below It

This route gained **one module and one lane row**, and the leaf they belong to (`260921-ICR-L3`, primary
requirement ICR-R03@v1) is the regression surface for one promise: *every inventory entry opens the exact
available before/after source content for its bound comparison*, with truthful per-side states for content
that cannot be rendered and **no silent fallback to a working tree**.

- **`mcp/tests/test_knowledge_review_source_content.py` (new, 840 lines, 20 cases)** drives the two routes
  the dashboard really serves — the review payload's own inventory (`/api/review/intent`) and the
  expansion (`/api/review/intent/source-content`) — over a **real leaf enclosure with a real linked
  worktree**, with the routes wired through `register_review_routes` exactly as the composition root wires
  them and exercised over the real HTTP transport (`TestClient`), so a passing case has proved the query
  contract, the refusal status and the served body together.
- **Nothing here is a restatement of the owner under test.** Every text the expansion serves is compared
  against an **independent subprocess `git show <tree>:<path>`** observation whose failure is an assertion
  failure and never an empty string, and the fixture materializes each content class the packet names as a
  real filesystem object — a binary blob, a symlink, a nested repository recorded as a gitlink, a mode-only
  change, a file→symlink type change, an oversized document and a name containing a tab and a newline.
- **The generation is the caller's, never the server's.** The expansion carries the two tree ids the
  listing published; the cases prove the listed bytes survive the branch advancing (`currentness` says
  `superseded` and a re-listing control shows the new generation), that one unreadable side stays
  `unavailable` while the other is served — twice, once for an unheld tree and once for a **real prune of
  one loose blob** — and that a commit id in a tree-id field is refused by the object's own type. The
  verifier's finding is measured directly: with an unmeasurable requested pair the path is still confined
  to the leaf's own measured change set, and both falsifying paths are refused by name.
- **The lane row moved every manifest line below it, and that is this route's citation fact.** The
  module's row was inserted in the existing `unit-regression` array at
  `mcp/tests/test-evidence-lanes.toml:113-115` — immediately after `mcp/tests/test_knowledge_review_source_endpoints.py`
  (`:110`) and above `mcp/tests/test_knowledge_requirement_reference_contract.py` (`:112`) — so every lane
  row at or below `:111` shifted by one. Every citation this route and its sibling cards carry into that
  manifest was re-derived against the post-edit bytes rather than shifted by a remembered delta.
- **The census delta is consumer-only.** The module extends the existing R01 source-endpoint enclosure
  fixture (`build_endpoint_fixture(datasets=False)`) rather than introducing a second one, so it registered
  no artifact and no contract: one path joined the `consumer_scope = "exact"` list of
  `mcp/tests/diff_scope_test_support.py` (row `:1412`) and one the list of
  `mcp/tests/read_scope_test_support.py` (row `:1445`), both derived from the census's own
  `missing=[…]` / `unsupported=[]` finding. The population stays at **sixteen contracts / sixty-six
  artifacts**, the catalog is **1677 lines** and `LIFECYCLE_CATALOG_SHA256` is re-pinned from
  `aedb2636844faf41ca63b7099e6c62bcaf888720e7e7dd78e203e3a1c9e061ff` (L11's measurement) to
  `dc6e380867302d7e2fff89f8c36549c85528ed4dafa28b4510981b573f09739b`, with the reason written beside the
  constant as its **Fifteenth deliberate re-pin** (L3's own candidate). **At the sync the merged catalog measured 1681 lines and
  `3e9105c2116422debaa01c295294fc0c714288f701ee5902e6552884b64a52d8`**, which is the value the constant carries now and which this leaf's own four consumer rows share the file with.

- **The module's own statement of the requirement and of the property behind each case.** [144]
- **The first case: both bound objects' own bytes, each against an independent `git show` observation.** [145]
- **The content classes the fixture materializes for real, and the routes wired as the composition root wires them.** [146]
- **The generation binding, the two availability cases, and the verifier's path-confinement finding.** [147]
- **The refusal family and the closing identity case.** [148]
- **The shared R01 fixture these cases extend rather than duplicate.** [149]
- **The lane row the insertion created, and the two rows it displaced.** [150]
- **The two consumer rows this module joined, and the counts they do not move.** [151]
- The expansion owner and route constant these cases are the regression surface for. [152]
## 260921-ICR-L14 The Production Composition's Record Channels: One Module, Ten Cases, And Damage Measured Per Record

`mcp/tests/test_knowledge_review_evidence_channels.py` is `ICR-R14@v1`'s case module and this route's
newest arrival: **ten cases** in the `unit-regression` lane (`mcp/tests/test-evidence-lanes.toml:108`),
all driving `cli.dashboard.serving_collaborators(...).knowledge_review` — the same port `create_app` is
given — over a real leaf enclosure whose candidate dataset holds records written by their owners.

**Why the route cares about the module rather than only the cases.** Each record class is produced
through the operation that owns it before it is read back (`detection.record_detection_run`, the
application evidence writer, the candidate batch operation, the curator-coherence publication), so the
suite fails the way the packet requires the defect to fail: a production port that supplied only
assessments cannot pass any of them. The load-bearing properties, one case each: every available class
arrives with its owner's fields; an unpublished authority is a **measured absence** while a corrupt one
is **unavailable** (the two states F09 collapsed); one unreadable authority leaves the readable classes
supplied; a task-context review reports the matrix-owned collection `not_selected`; no measurement is
reported as one; **one damaged detection run, and one damaged claim, are each named while their siblings
are supplied** (the last two added for independent-verification findings F1/F2); an unresolvable
candidate reports every collection unavailable; the channel vocabulary refuses a count no owner
measured; and the channels travel in the served payload schema.

**Fixture footprint.** It builds on `mcp/tests/test_knowledge_review_source_endpoints.py`'s endpoint
fixture (whose `memory_mode="external"` shape this leaf added) and on
`mcp/tests/curator_coherence_test_support.py`'s publication helper rather than introducing a third
fixture — so the evidence catalog's delta is four consumer rows and no registered artifact, and this
route's own population count moves by one module.

- **The module whose cases are the production-composition evidence, and its lane row.** [153]
- **The two per-record damage cases, which are the ones that make the partial-collection states measured rather than asserted.** [154]
- **The production port the cases read through, and the bundle they read beside it.** [155]
- The fixture's external-memory shape, which the assessment channel needs. [156]
## 260921-ICR-L4 The Attribution Cases: Nine Partition Cases, Six Precedence And Receipt Cases, Two Extensions

This route gained **no module and fifteen cases across the four existing ones**, and the leaf they
belong to (`260921-ICR-L4`, primary requirement ICR-R04@v1) makes one claim per route half: *the
measured changes are partitioned once, and one unreadable side never licenses a negative
conclusion*. `test_knowledge_diff_scope.py` (789 → 1384 lines) gained nine cases — the disjoint and
exhaustive partition, the outside-selection boundary, the family-subject membership, the two
stale/unresolvable-mapping precedence cases, the half-inspected undetermined rule, the
legitimately-empty side, the unavailable-partition honesty rule and the partial-denominator scope.
`test_knowledge_review_source_endpoints.py` (938 → 1364) gained six — the unreadable-half
precedence, the identified empty generation, the complete-read control, the damaged-half refusal of
a negative conclusion, and the two receipt states. `test_knowledge_diff_boundaries.py` extended the
unavailable-observation case with the partition's own assertions, and
`test_knowledge_review_surface.py` corrected the knowledge-only case to the measured empty
partition. No lane row and no catalog row was added: no new test module, so no catalog re-pin —
the whole footprint is cases inside already-registered modules.

- **The nine partition cases, appended after the module's former end.** [157]
- **The six precedence and receipt cases on the real enclosure route.** [158]
- **The extended unavailable-observation case and the corrected knowledge-only case.** [159]

## 260921-ICR-L11 The Durable-Comparison Cases: One Module, Fifteen Cases, And The Journey Measured Rather Than Simulated

This route gained **one module**, `mcp/tests/test_knowledge_review_comparison_generation.py` (1194
lines, fifteen cases) — its one-to-one card is
[`test_knowledge_review_comparison_generation.py.md`](test_knowledge_review_comparison_generation.py.md) —
and the leaf it belongs to (`260921-ICR-L11`, primary requirement ICR-R11@v1)
makes one claim: *a frozen comparison retains resolvable source, knowledge and evidence inputs through
cleanup and restart*. What belongs at this route's altitude is the three things the module deliberately
does **not** do, because each one is what makes its evidence production-composition evidence rather than
a re-read of what the implementation just wrote:

- **It does not build a fixture of its own.** The cases call `build_endpoint_fixture` from the existing
  `test_knowledge_review_source_endpoints.py` — the R01 enclosure fixture — so they measure the *same*
  real enclosure, linked worktree and capture path the source-endpoint cases measure rather than a
  second, drifting one. That is also why the module needed no third fixture and why it appears as a
  **source-derived consumer** in two existing `consumer_scope = "exact"` rows.
- **It does not simulate a restart.** The reopen runs in a **child process** that builds its own config
  from a JSON payload, resolves the generation from the task artifact plane alone, and reads the
  candidate bytes back with `git show`; a child failure raises with its exit code and stderr, so a broken
  child can never be read as an empty result.
- **It does not assume reclamation happened.** The first case writes an unreferenced **control object**,
  runs `git gc --prune=now`, and checks the control is gone before asserting that the pinned tree
  survived — so survival is attributable to the pin and not to a reclamation that did nothing. It then
  removes the whole worktree group (worktree, live datasets and stage) before reopening.

Two further properties the route should carry: the **fabrication case injects a full reseal** — a record
with edited bound fields and a recomputed digest, internally consistent — which only the re-derived
generation id plus the directory-name agreement can catch; and the **custody cases reproduce the
verification falsifier** (commit on the leaf's own work branch → `custody="retained"` → worktree removed,
branch deleted, gc → child-process reopen `available`) beside the genuine committed-history path where no
ref is created at all.

Governance shape: the module is registered as a `unit-regression` row in `test-evidence-lanes.toml`
(`:107`, mid-list in the knowledge run) and its path was appended to the two exact-consumer rows in
`evidence-lifecycle.toml` (`:1405` and `:1429`) that its imports make it a consumer of, which is a
consumer-only catalog change: **16 contracts / 66 artifacts, counts unmoved**. The digest this leaf
measured on its own candidate was `6b73894f…`; on the merged line — which also carries
`260921-ICR-L20`'s two consumer rows — `LIFECYCLE_CATALOG_SHA256` is
`aedb2636844faf41ca63b7099e6c62bcaf888720e7e7dd78e203e3a1c9e061ff`.

- **The module's own statement of the packet's journey and of the property behind each case.** [160]
- **The shared R01 fixture the cases build on instead of a second one.** [161]
- **The real restart: the child program and the helper that fails loudly.** [162]
- **The reclamation control that makes survival a measurement.** [163]
- **The fabrication a seal-only check would accept, and the four unreadable shapes.** [164]
- **The two custody cases, one of which is the verifier's own falsifier.** [165]
- The per-channel damage case, and the stage-sweep case driven through a real child process. [166]
- The lane row and the two consumer rows this module's registration produced. [167]
- The module's own header, which names the requirement and the journey its cases measure. [168]
- The module's own header, which its one-to-one card expands; the card itself is linked in this section's prose because a memory-relative citation cannot be resolved against the memory commit this row's verification stamp maps to. [169]

## 260921-ICR-L20 The Ordinary Publication Route's Eleven Cases, And The Lane Row That Moved Every Manifest Line Below It

This route gained **one module and one lane row**, and the leaf they belong to (`260921-ICR-L20`,
primary requirement ICR-R20@v1) is the regression surface for one forbidden inference: a successful
process exit read as proof that every entry committed — or that the repository now holds what was
written.

- **`mcp/tests/test_knowledge_ingest_publication_route.py` (new, 756 lines, 11 cases)** drives the
  shipped `agents-remember knowledge-ingest` entry point through the umbrella `main` over a
  **production-shaped enclosure**: a real code line with its own work branch, a real external memory
  repository, a real Git memory worktree cut from it, and a contract recording all of them under a real
  coordination root. The declared location is resolved by the *read* route's own owner rather than
  restated in the fixture, so the fixture cannot quietly agree with the implementation about a path
  neither of them should be computing.
- **The six operations and the refusal family.** The ordinary first publication and the mounted read
  surface answering from the published dataset; a custom `--candidate-directory` that must be the one
  reviewed *and* published, with the canonical review path never created; a partial refusal naming each
  entry and publishing only what committed; the explicit update (the identity replaced is the one the
  run read from its own baseline, and the earlier truth survives into the successor); the exact retry
  (`no_change`, bytes unmoved, identity still confirmed); and a run that names no destination and says
  so. The refusals are their own cases: a refused publication leaving the destination untouched, two
  contradictory selections, an absorbed `--expected-destination`, and a declared location that cannot
  be resolved.
- **The lane row moved every manifest line below it, and that is this route's citation fact.** The
  module's row was inserted in the existing `unit-regression` array at
  `mcp/tests/test-evidence-lanes.toml:91-91`, so every lane row below `:88` shifted by one and the
  `mcp/tests/evidence-lifecycle.toml` consumer rows moved by one and two respectively; every citation
  this route and its sibling cards carry into those two manifests was re-derived against the post-edit
  bytes rather than shifted by a remembered delta.
- **The census delta is consumer-only.** The new module composes the existing ingest-list fixture module
  and `mcp/tests/snapshot_lifecycle_test_support.py` (reached through it) rather than introducing a
  third support artifact, so the population stays at **sixteen contracts / sixty-six artifacts**, two
  `consumer_scope = "exact"` rows gained the path, and `LIFECYCLE_CATALOG_SHA256` was re-pinned to
  `4da562629ba16373ce387f0b7cfe83f110eede155fced865de9fa92f7eb41df7` with its own documented reason.
  **Superseded on the sync line:** `260921-ICR-L11`'s two consumer rows landed below this leaf's, so the
  merged catalog carries `aedb2636844faf41ca63b7099e6c62bcaf888720e7e7dd78e203e3a1c9e061ff` (`1675` lines); `4da5626…` is this
  leaf's own-candidate measurement, exactly as `260921-ICR-L6`'s `7920a0f9…` is its own.

- **The eleven cases: the ordinary publication, the custom candidate, the partial refusal and the explicit update.** [170]
- **Exit zero is not a publication claim, made measurable: the retry, the run that named no destination, and the two reasons a selected destination can publish nothing.** [171]
- **The refusal family: a refused publication, two contradictory selections, an absorbed expectation and an unresolvable location.** [172]
- **The production-shaped fixture and the helpers that keep it an independent side.** [173]
- **The lane row the insertion moved every line below, and the two consumer rows the module joined.** [174]
- **The catalog digest the two consumer rows moved, and the counts they do not move.** [175]
- The production route these cases are the regression surface for. [176]

## 260921-ICR-L18 The Comparison-Generation And Failure-Window Modules, And One Case That Left The Over-Rail File

This route gained **two modules and two lane rows**, and the leaf they belong to (`260921-ICR-L18`,
primary requirement ICR-R18@v1) is the regression surface for one defect: with a single path named for
both `--baseline` and `--publish-to`, two successful writes re-filled the review's before half from what
by then *were* the first run's published bytes, so the comparison showed the addition present on both
sides with an empty delta.

- **`mcp/tests/test_knowledge_ingest_comparison_generation.py` (new, 323 lines, 3 cases)** owns the
  successful journey and its fixtures: two successful writes over one shared path, the exact retry and
  the refused changed retry, and the deliberate rebase whose record names the generation it replaced by
  id *and* by exact dataset identity. Every case drives the shipped CLI as a real process on a real
  enclosure, so nothing here asserts a prebuilt payload in place of the production composition.
- **`mcp/tests/test_knowledge_ingest_failure_windows.py` (new, 631 lines, 9 cases)** owns the failure
  surface: an adopted half kept rather than treated as an empty slot, a record that disagrees with its
  bytes and a record path that is obstructed, the rebase-flag refusal, the write site's own
  "only bytes that read as a dataset" precondition, and the two separately-failing publication legs —
  including the two post-rename flush windows that forced the legs to say only "did not report success"
  and let the appended read-back state what actually landed.
- **The split is an extraction, not a subject boundary.** The F3 cases pushed the first module to 901
  lines, one over the repository's 900-line soft rail, and the repository's rule is to clear that by
  extraction; the failure module imports the journey module's fixtures rather than copying them. The
  route's over-rail file, `mcp/tests/test_knowledge_curator_ingest_list.py`, **shrank** — 3192 → 3162 —
  because the write-site case moved out with the placement owner it measures, and a note where it stood
  names the move.

The route-level consequence a reader should carry: the two new modules are ordinary `unit-regression`
entries with **no artifact and no contract of their own** — they compose the existing
`snapshot_lifecycle_test_support` and ingest-list fixtures rather than introducing a third support
module — so the census population stays at sixteen contracts and sixty-six artifacts, and the catalog's
bytes move for consumer rows only.

- **The successful journey and the fixtures every other case starts from.** [177]
- **The failure surface: the adopted half, the damage, the two failing legs, and the fault injection that makes a leg fail after its bytes landed.** [178]
- The generation owner whose placement, ordering and two legs these cases measure. [179]
- The two lane rows these modules joined, and the lane key they are members of. [180]
- **The case that left the over-rail ingest-list module, cited where it now lives, and the note left where it stood.** [181]
- The two consumer lists both new modules joined, and the counts they do not move. [182]

## 260915-KS-L41 The Mounted Read Family's Successful Path, Driven Against A Real Store Without A New Case
## 260918-TSIP-L5 The Whole Tool Surface Driven Through Its Entry Point

This route gained **one module and one lane row**, and the row moved every manifest line at or
after `:153`; the population, the arithmetic and the repairs are on the lane card
(`test-evidence-lanes.toml.md`). This section records what the route now carries.
The regression this leaf protects could not be seen below a real store, so the case that protects it
drives one — and it does so **without adding a collected case and without raising either lane's ceiling**.
Family membership lives in the dedicated `family_member` table and is not duplicated into the
`knowledge_record`/`record_revision` envelope a generic kind read consults, so a renderer that asked the
envelope reader for the kind `family_member` returned no members on a dataset that holds them, and
reported a joint guarantee, no members, no implementation locations and `completeWithinDeclaredScope:
true`. A stub reader supplies the rows the production reader cannot, which is exactly why an earlier
pass's verification missed it; every assertion here is therefore made against a real SQLite store built
through the shipped typed operations (`create_repository`, `create_invariant_revision`,
`create_family_revision`, `create_family_member`, `create_realization_claim`) and read through a real
mounted `FastMCP` handler.

**`mcp/tests/test_tool_entry_point_sweep.py` (new, 1274 lines / 14 cases, sha256 `4223c626…`)** is
the durable form of the leaf's happy-path trace: every registered public tool — 67 of them, with
the roster asserted equal to the live server's own advertisement — is invoked through the
production entry point, a real in-memory MCP client session against a server built by
`create_server`, in one hermetic scratch world. Each answer must be a validated payload, a typed
refusal carrying a machine-readable identity, or one of two **pinned** defect families: `T34`'s
nine envelope-losing raisers, and a second pin for the lifecycle family's *state* precondition
measured as a four-state matrix over a population derived **by rule** from the roster. A third pin
records `T64`'s `citation_migrate` preview answering `ok:false` where its sibling `citation_fix`
answers `ok:true`. The rule on every pin is that a repaired tool leaves the pin in the same
change, and each pin is asserted **equal** to what the sweep observed, in both directions.
The protection is four **non-collected** helpers — `_build_mounted_family_fixture` (which builds the
store and records why in its own docstring), `_assert_family_traversal_from_one_path`,
`_assert_the_path_seed_selects_in_every_view` and `_assert_the_context_is_constructible` — composed by
`_assert_the_family_read_returns_stored_membership_and_the_path_seed`, which
`test_the_read_family_refuses_a_sixth_view_before_it_touches_a_dataset` calls at its own end;
`test_the_read_family_refuses_a_continuation_minted_for_another_walk` calls the constructible-context
helper beside its refusal. Reverting only `application/knowledge_view_render.py` to its base version turns
the first case red on the member rows it asserts, which is how the regression became visible to the suite
at a moment when the unit lane stands at exactly **2300 / 2300** and the integration lane at **400 / 400**
— neither can take a new case.

**The sweep carries its own controls and its own boundary.** `ChokePointControlTests` drives
`finalize_tool_response` with a payload its model forbids and requires it to refuse, and executes
both `T7`-class break shapes at the entry point; `EntryPointCensusControlTests` proves the
hermeticity case can see a write, a rewrite and a delete. The only files the world's own memory
repository may gain are the two scaffold files the product's `memory_init` repair writes.
**The fixture is module-local on purpose, and it should not be "simplified" back to the shared corpus.**
The larger branching corpus lives in `knowledge_fixture_test_support`, a governed shared-support artifact
whose consumer list is a pinned evidence catalog; importing it here would have added this module to that
catalog and reddened the integration lane's structural check. This case needs three recorded rows — a
family whose members are realized at one path, a sibling family that is not, and one path recorded
nowhere — not a corpus, so it builds them through the same public operations a real caller uses, and its
three path constants carry the shared corpus's own names so a reader moving between the two is not
confused.

**Lane.** `unit-regression` at `mcp/tests/test-evidence-lanes.toml:154` — a `tempfile` world, no
docker, no network, no real state and no `-m` override, so the cases run in the ordinary default
selection. The manifest file is `269 → 270` lines and now carries **252** entries for **252**
modules on disk.

**The citation population the insertion moved** was enumerated from the leaf memory worktree
rather than inferred: **115 moving anchors across 20 documents — 48 live, 67 exempt under
`## Update History`; 111 lines, 45 live**. The baseline `range_resolution` run reported **31** of
those 48, so 17 moved citations were green and a repair driven from the finding set would have
left them stale (`T52`). All 48 live rows are repaired; the lane-bracket rows are re-derived to
this candidate's measured brackets; nine stale `row N now` prose figures and a fifth
`… Lane Row (Declared)` mention — 38 lines stale, and one row short of the previous leaf's own
list — are set to their true rows. One claim whose literal anchor resolved twice was re-worded to
its unique owning key, because this leaf had to touch that document and provenance is enforced on
any document a task touches.

## 260918-TSIP-L3 The Publish Contract, The Mode Pins, And `T51`'s Class Repair

Three of this route's modules changed and **no module was added**. **`mcp/tests/test_tools.py` (364 →
468 lines, 10 → 12 cases)** gained `CuratorCoherencePublishContractTests`, which pins `T50`'s two
disagreements separately because either can regress alone: the registered `curator_coherence`
description must name all nine fields `publish` requires, and a real `publish` request must be
refused with `missing: <field>` once per omitted field — with the complete request accepted first as
the positive control, so a mistyped field name cannot make the case pass for an unrelated reason. The
same case pins that the JSON schema **cannot** carry the requirement
(`required == ["action","contract_path"]`, because it is conditional on `action == "publish"`), which
is why the published description is the load-bearing surface.

**`mcp/tests/test_checkout_coordination_isolation.py` (180 → 241 lines, 8 → 10 cases)** gained two
cases that assert the execution-mode boundary **as it is**: a two-arm case whose arm A is the plane's
real refusal — the positive control — and whose arm B shows one unauthenticated
`declare_execution_mode("mcp")` lifting the refusal *and* switching the process to the live authority
settings, plus a case driving `declare_lifecycle_operation_process()`, a mode the plane reserves in
words to a plane-owned operation record and which nothing in the product calls. Both are **pins, not
endorsements**: authentication is deliberately not implemented (`D-L3-1` in `notes/defect-index.md`),
so the day it is, these cases go red on purpose.

**`mcp/tests/test_record_integrity.py` (1000 → 1140 lines, still 37 cases)** had four live-state reads
frozen by class (`T51`). `DECLARED_LEAVES` / `DECLARED_LEAF_COUNT` and `_frozen_leaf_snapshot` prune
the copied master to the two leaves L1 and L2 landed, write their document statuses and reduce the
master's rows to them, so the subject count, the unmatched-row verdict, the register's `authority`
count and the CLI's clean-world exit are the case's own rather than the world's. The module's real
claims held while those counts failed, which is the finding: a fixture that asserts a live population
is green exactly while the world happens to match it.

**`mcp/tests/test-evidence-lanes.toml` was not touched**, because the two new cases ride
already-registered modules, so no lane row moved and no citation below one is invalidated. This leaf
is the first on the master to avoid `T31` by construction rather than by repair, and it paid for that
in the integration lane's population (274 → 276 of 300) rather than in 212 renumbered manifest lines.

## 260918-TSIP-L2 Record-Integrity Module And Its Lane Row

This route gained one module and one lane row. `mcp/tests/test_record_integrity.py` (**1000 lines, 37
cases** as the L2 curator measured it on that candidate; the case count still holds, and the file is
**1140 lines** after L3's `T51` repair — see the section above) — measured on this candidate: 37
`def test_` methods in five classes, **0** module-level
cases, **0** parametrisations, and `pytest --collect-only -q` → **`37 tests collected`**, so the
collected count and the defined count are the same 37) pins the four record comparisons shipped in
`mcp/test_support/agents_remember_test_support/code_quality/record_integrity.py`, each against the
historical artifact it was written for and in both directions: the check must FAIL on the artifact as
it stood when the drift was live, and PASS on the artifact that replaced it.

Its row was added in the existing **`architecture-fitness`** lane at `:246`, as that array's last
entry — between `test_wire_vocabulary_exhaustiveness_boundary.py` (`:245`) and the lane's closing
bracket (`:247`). `architecture-fitness` is the behaviour-preserving lane for it for the same reason
as its sibling: the module imports the verification package and executes nothing over a real boundary,
so `unit-regression` and `integration` are both wrong for it.

**The insertion moved every entry below `:246` by one, and the shift could not be avoided.** An
`architecture-fitness` entry must sit between its header (`:227`) and the next lane header
(`provider-conformance`, `:248`); the array read 18 entries at `228-245`, so `:246` — the array's last
row — is the minimum-displacement position. Three citations were invalidated and all three were
repaired in the same pass, with the ranges **re-derived from the post-edit bytes rather than from the
numbers the edit was planned against**: `test-evidence-lanes.toml.md`'s aggregate rows `:262-265` →
`:263-266` and `:4-265` → `:4-266`, and `test_codex_capsule_delivery.py.md`'s `:254-254` → `:255-255`.
That card's `:242-256` row was checked and left alone. The product's own `range_resolution` check
reported two of those three; the stale `:4-265` end was invisible to it, which is `T45`'s class.

**This leaf's own finding about the loader belongs on this route.** `load_lane_manifest(<repository
root>)` **refuses** at this candidate — `test files without an explicit lane:
['mcp/tests/test_atomic_series_chain_pair_order.py']` — a module added by `260915-CAPS-L25` at
`f0313143` and never registered. The gap is one row at every commit since: 247 entries / 248 modules
on disk at `f0313143`, 248 / 249 at `d9becade`, 249 / 250 here. So it is neither this leaf's doing nor
this leaf's to repair — registering that module is a change to the lane manifest and belongs to its
owner — but the route should carry the correction, because the run the section below cites for the
loader's silence does not exercise the loader at all.

Fourteen of this module's cases read the real record, so they **skip** without
`AR_COORDINATION_ROOT` and a green default-lane run says nothing about them; the `T45` documents those
cases assert against are read **by Git object** at `e116e5ee`, the revision that committed them.

## 260918-TSIP-L1 Instrument-Discipline Module And Its Lane Row

This route gained one module and one lane row. `mcp/tests/test_instrument_discipline.py` (**537 lines,
27 cases** — re-measured on the current candidate: 26 `def test_` methods in five classes plus 1
module-level `def test_`, with **0** parametrisations and **0** subtests, so `pytest
--collect-only -q` reports `27 tests collected`) pins the measurement-admissibility conditions shipped
in `mcp/test_support/agents_remember_test_support/code_quality/instrument_discipline.py`, each against
the historical artifact it was written for and in both directions: the shipped function refuses the
artifact that carried the fault, and accepts the artifact that replaced it. A check asserted in only
the refusal direction cannot be shown to be non-vacuous, which is the fault the module exists to
catch.

Its row was inserted in the existing **`architecture-fitness`** lane at `:232`, between
`test_file_size_detector.py` (`:231`) and `test_layering.py` (`:233`) — the lane that owns structural
invariants. The module imports the verification package and executes nothing over a real boundary, so
`unit-regression` and `integration` are both wrong for it. **Corrected by the `260918-TSIP-L2`
curator, and wrong when written:** the fail-closed loader is **not** silent at this candidate. The run
cited here — `pytest tests/test_evidence_lanes.py tests/test_suite_budget.py -q` → **4 passed in
0.54 s** — never calls `load_lane_manifest`; its one registry case validates the lane *categories*.
Called directly, the loader already refused at this candidate for the unlisted
`mcp/tests/test_atomic_series_chain_pair_order.py`, an unregistered module from `260915-CAPS-L25`. The
module does collect into the lane, which is what the row above establishes. See the section above.

**The insertion moved every later row down by one, and that is the fact a reader of this route needs
most.** `test_pause_is_not_publication.py` moved `:235` → `:236` and `test_codex_capsule_delivery.py`
moved `:253` → `:254`. Four memory documents cited the pre-insertion numbers and all four were
repaired in the same pass — three mechanically through the shipped citation fixer (`ccr-r10@v1`:
`test-evidence-lanes.toml.md`, `test_codex_capsule_delivery.py.md`,
`test_pause_is_not_publication.py.md`) and one aggregate row in this document's own
`Repo-Internal References` by hand, because it mixed two anchors across four cited ranges and the
fixer declined it. A line number recorded on this route before this leaf must have one added for
every row at or below `:232`.

**One case skips rather than passes.** The transcriber case re-reads
`memory-refresh-finding-21-routes.json` under the previous master's task root and skips when that
package is absent, so a green run in a workspace without it has not checked the transcription. And
the suite's own recorded limit belongs in this route too: the **then-16** cases passed while the
module under test still carried a `\b` that cannot match the plural `findings` — a hand-written
fixture cannot license a pattern, only the real artifact can. (The count is stated in the past tense
deliberately: it is a fact about the suite as it stood, not about the current 27 cases, which were
added after the repair.)

## 260915-CAPS-L9 Experiment-Installation Test Population

`mcp/tests/test_capsule_experiment_install.py` is **new** in this leaf: **19 cases** driving the real
installer entry points against scratch coordination roots, and reading the resulting tree, the
returned run record and the compiled capsule text. It is **not** a seventh `D9` module — the
fail-closed lane loader still names exactly the same six at this tip as at the clean base — and its
manifest row plus its two `evidence-lifecycle.toml` consumer rows are the whole catalog delta this
leaf contributes.

What the population is for, stated so the route is not read as more than it is: the cutover pair with
the disabled run as its positive control and the removal half; the documented way back executed as a
run; the selection surface (request-then-environment precedence and `selectionSource`) driven through
the **registered payload builder**; fail-closed refusals that name the capability **and** create no
coordination root; three separately-labelled screens (received startup material on disk, the
delivered capsule from the production compile route, and the installed root's corpus read as authored
source); the run record compared against the pinned `package.json`; the rendered rollback rows; the
install's confinement to its destination; and the **no-persistence guard**, which content-digests
every regular file under the coordination root before and after the selected run and demands that
every hit be a byte-identical authored asset — the root-scoped reading that replaced a first revision
whose `rglob("*.json")` guard was blind to a `.toml`, a `.txt` or an extension-less switch.

`test_sync_runtime.py` gained two cases (two methods → four): the per-target ignore rule and the
refusal to report an absent canonical source in sync.

## 260915-KS-L34 The Series Reopen's Three Arrivals, Held In One Budget Slot

`mcp/tests/test_task_reopen.py` already carried the series half of `task_reopen` — one gathered case, two
facts, written against a lane that could not afford a second subject. This leaf tells that same case from
its other two arrivals and adds no collected case at all, which is the part of this section a reader of
the route needs to understand before concluding anything from the case count.

The arithmetic is the reason. **Both lanes sit at exactly their configured budget — 2300 / 2300 unit and
400 / 400 integration** — and `pytest_collection_finish` raises `UsageError` on an over-budget selection,
after which that lane executes **zero** tests. One more collected case in this module would therefore buy
a red lane and no coverage. So the two new scenarios are **plain methods**,
`_assert_an_interrupted_series_reset_is_resumed` and `_assert_a_live_unaddressed_series_is_re_addressed`,
called from inside the collected case's body. They execute on every run of that case; they are simply not
independent collection units. A reader should treat "we added no case here" as a deliberate budget
decision with a named mechanism behind it, not as an untested claim — and should reach for consolidation
in this module rather than a new `test_*` method if more series behavior needs pinning.

What the gathered subject now pins, and why all three belong to one case: a series reaches the publication
from a terminal state, from a state that is **already live** at a collected address (`cleanup: pending`,
both progress cells virgin, integration branch carrying the series' own landed work), and from an
interrupted reset whose tombstone is durable while the locator is still collected. They are one promise —
"the reopen re-cites the archived generation and never moves an existing ref" — told from three sides, so
the ref rule and the reset are not two subjects but two halves of one, and the live arrival is the same
publication entered without a reset. The counter belongs here for the same reason: it is that reset applied
to the document instead of the contract, and the fixture drives a completion that spent three rounds so the
clearance is measured (`round: 3` in, `(0, False, 0, None, [], [])` out) rather than assumed.

Every scenario records the landed commit before the call and asserts the same commit after it, which is
what makes "never moved" an assertion in this module instead of a claim in a docstring.

- One collected subject covering all three arrivals at the series publication. [183]
- The interrupted reset resumes rather than stranding the branches the series stands on. [184]
- The already-live arrival is re-addressed: `advance` reported, branch unmoved, successor citing the archived predecessor, spent counter cleared. [185]

## 260915-KS-L35 The Chain Admits The Reconciled Line A Step Merged With

`mcp/tests/test_atomic_series_chain_pair_order.py` is the forcing test for the spine step rule the
atomic-series closeout walks, and this leaf added the third direction to its single leaf-sync case. The
route-level fact a reader needs is the same one the production card records, stated where a test reader
meets it: **a step that adds a line is admitted only when the chain's own contracts recorded the position
that line came from.**

The case already told two directions apart — a recorded leaf-level sync position is admissible, and a
position no contract recorded is refused with the foreign commit named. This leaf adds the shape the
260915-KS master is actually in: when a step's **endpoint** is the merge of the previous landing with a
recorded position, the whole step *is* that position's own line, and the validator used to admit the
position while refusing every commit the line introduced — 22 of them on the live master (register row
`D-60`). The new statements build exactly that merge with `git merge --no-ff`, place the series branches on
it, assert the chain still orders `["L1", "L2"]`, and assert the step's own non-merge count is `4` —
counted precisely so the direction cannot pass vacuously on an empty step.

There is no new collected case, and the reason is a route-level constraint rather than a preference. **Both
lanes sit at exactly their configured budget — 2300 / 2300 unit and 400 / 400 integration** — and
`pytest_collection_finish` raises `UsageError` on an over-budget selection, after which that lane executes
**zero** tests. One added collected case would therefore buy a red lane and no coverage. The new directions
are plain statements inside the existing case body, so they execute on every run of it while remaining
outside the collection unit count. A reader should take "the case count is unchanged" here as a deliberate
budget decision with a named mechanism, and should reach for consolidation in this module rather than a new
`test_*` method.

The counter-case is deliberately untouched. `test_a_position_that_descends_from_a_step_does_not_vacate_it`
still pins that a recorded position reaching *past* a step cannot erase a foreign commit inside it, which is
the property that made enumeration necessary in the first place; the new admission is bounded to positions
lying strictly **inside** the step, so it does not weaken that case, and both cases' own assertions are
unchanged.

- The one collected case that now pins all three directions of the step rule. [186]
- The counter-case the new admission must not weaken: a position descending from a step cannot vacate it. [187]
- The production step rule these cases force, and the two helpers the repair added. [188]
- The positions a step is measured against: the chain's own contracts' sync logs unioned with the recorded base. [189]

## 260915-KS-L39 The Public Curation Journey, Pinned Inside The Existing Budget Slot

`mcp/tests/test_knowledge_curator_ingest_list.py` carried the CYCLE-01 continuity case before this leaf and carries the closure of the three
points a follow-up review kept open, so a reader of this route should know what the case now measures and
why its **collected count did not change**.

The case `RepositoryIdentityStabilityTests.test_repository_knowledge_continues_across_baselines_and_tasks`
now ends by calling `_cycle01_public_identities`, which pins three route-level facts. **(f)** The
identities the **write path** stores distinguish two constructs of one file: `_target_identities` mints the
anchor on the allocated revision id with the symbol's qualified name as the in-creation disambiguator, and the
claim on its own revision-plus-anchor edge, while the route stays one scope per path — so two constructs of
one `pkg/module.py` get two anchor ids, two claim ids and one shared route id. The observation identity the
case already separated was not enough on its own, because the stored anchor and claim were still keyed on the
path and the entry id alone and the batch refused the second with `duplicate_identity` on `source_anchor`; and
the entry id was not enough either, which is what L43 corrected below. **(g)** The **public operation** is driven for real: task A commits
two constructs of one file and publishes, task B forks that published dataset with a selected `baseline`,
keeps A's invariant and revisions by exact id, stores an explicit successor under the invariant it names
with a recorded `invariant_predecessor` edge, adds an unrelated record, and republishes over the dataset it
forked from (`previous_identity` equal to A's). The assertions are read from the databases themselves: the
published `knowledge.sqlite` holds exactly the candidate's invariants and revisions, and the candidate
holds four distinct anchors, three of them for the one file. **(h)** This point was **re-pointed by L43** and no longer reads as it was
written here. It used to say that a reused local label resolves to the repository's record — one repository
read at two code baselines mints the same invariant and revision identity, "which is what makes the
obligation recorded at the first baseline findable at the second". That was true of the fixture it measured
(one repository, one label, two baselines, one statement) and became misleading only because it was read as
covering a case the fixture never separated: two *independent* tasks authoring different truths under a
reused label. The developer's 2026-09-20 ruling names the case — `R-LOCAL` is a **local hand-off label**, the
label is not an identity input, the knowledge API **allocates and persists** the canonical identity,
continuity across a task boundary is by **explicitly naming the stored identity**, and a retry rides a
**separate idempotency key** — and `_cycle01_reused_label_identity` now measures exactly that: two sibling
enclosures differing in nothing but their leaf id, one reused label, two different statements, **distinct**
stored invariant and revision ids, and then a third enclosure naming the first side's stored `invariant_id`
to evolve that record. The legitimate worry the old sentence carried is still answered, by the route that
actually provides it.

**No collected case was added, and the reason is a route-level constraint rather than a preference.** Both
lanes sit at exactly their configured budget — 2300 / 2300 unit and 400 / 400 integration — and
`pytest_collection_finish` raises `UsageError` on an over-budget selection, after which that lane executes
**zero** tests. One added collected case would therefore buy a red lane and no coverage, so the new
protection is plain statements and helper functions called from inside the existing case: it executes on
every run of that case while remaining outside the collection unit count. A reader should take "the case
count is unchanged" here as a deliberate budget decision with a named mechanism, and should reach for
consolidation in this module rather than a new `test_*` method.

The journey publishes into a private pair's memory root, so it builds its own repositories through the
fixture's own builder (`pair.__wrapped__`) under a small private tmp factory rather than reusing the
session pair, whose memory root the other cases read but never write. That keeps the session fixture's
"never mutated by a case" invariant intact.

- The one collected case that now runs the public journey, and the entry point it calls. [190]
- The public journey itself: a private pair, task A's publication, task B's baseline fork, and the measurements read from the databases. [191]
- The reused-label identity, asserted as one record for one repository at two baselines. [192]
- The write-path identities the journey's first assertion pins. [193]
- **The public selection the next task uses to begin from a prior task's published knowledge — and, since 260915-KS-L45, the run that also places that dataset into the review's baseline half.** [194]
- The reused-label identity, asserted as the ruled semantics: a label is not an identity input, and continuity is naming the stored id (re-pointed by L43 — see the section below). [195]
- The public selection the next task uses to begin from a prior task's published knowledge. [196]


## Governing Overview

[MCP package overview](../overview.md)

## 260921-ICR-L6 The One-Sided-Statement Cases: One New Module, Six Cases, And One Lane Row

This route gained **one module** — `mcp/tests/test_knowledge_review_one_sided_statements.py`, 410 lines
and six cases — and one lane row, which is the first thing on this route a reader should check because
it is what keeps the module selected at all. The module is the **production-composition half** of
ICR-R06@v1: it drives the real `compose_review` over **two real datasets**, each built through the
public store operations by `read_scope_test_support.build_read_scope_fixture` and then extended with
one authored invariant apiece, so the addition and the removal are a real difference between two real
snapshots rather than an edit of one dataset. Its renderer half is
`dashboard/src/panels/review/KnowledgeStatements.test.tsx`, and the two assert the same statements,
the same absent/unresolved details and the same `acceptance_ref`/`provenance` field rows.

**The lane row, and the pure-move consequence a citation into that manifest must know about.**
`mcp/tests/test_knowledge_review_one_sided_statements.py` is registered in the **`unit-regression`**
lane at `mcp/tests/test-evidence-lanes.toml:105` — the lane the module declares for itself through
`pytestmark = pytest.mark.evidence_unit`. The row is **inserted mid-list** in the alphabetical
knowledge run, so every row and lane key below `:105` reads one line lower than it did, including the
`260921-ICR-L1` source-endpoint row (`:105` → `:106`). Measured on this leaf's candidate from the
manifest and the modules on disk: **310 declared entries against 310 modules**, 0 declared-but-absent,
0 present-but-undeclared, **328 lines**, `unit-regression` **198** — the one population that moves.

**The six cases and the property each one owns.** An **addition** serves the complete after statement
beside an `absent` before side with `text is None` and the comparison's own
`side_absence:before:selector_absent`; a **removal** is the mirror image; a **one-sided field row**
keeps the side that recorded a value and names the side that did not, with the roster asserted by exact
key set; a **structured field** the comparison reports as changed carries each side's own projection,
the two differ, and each round-trips back to the stored authorship envelope; a **one-sided record**
keeps an empty field roster and is reported by its coverage instead; and a **task-context review**
(`selector=None`) serves no operand at all, both sides `unresolved` with the same reason, so a
one-sided rendering cannot swallow it.

- **The new module's scope statement: six cases over the real adapter and two real datasets, and the load-bearing property each one owns.** [197]
- **The lane row, inserted mid-list, and the row it displaced.** [198]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [199]
- **The fixture that makes an addition and a removal real: two independently built snapshots under one namespace, plus the four authored revisions.** [200]
- **The addition and the removal: the complete present-side statement beside the named absent side, with the comparison's own side-absence code.** [201]
- The field-row cases: the roster asserted by exact key set, and the structured value served as its own projection on both sides. [202]
- The one-sided-record case and the task-context case. [203]
- **The catalog consumer row the same registration produced, on the shared read-scope fixture.** [204]
- **The catalog consumer row the same registration produced, on the shared read-scope fixture.** [205]
- **The renderer half that uses these same values, which is what makes a change to either half fail in one of the two.** [206]

## 260921-ICR-L5 The Before Half's Cases: Eleven Added, None Replacing A Measurement

This route gained **eleven collected cases and six helpers across two existing modules**, and no new
module: `mcp/tests/test_knowledge_curator_ingest_list.py` grew 2,533 → 3,192 lines (eight cases plus
five helpers) and `mcp/tests/test_knowledge_review_surface.py` grew 946 → 1,136 lines (three cases plus
one task-context builder). What they measure is the review's *before* side, which had no case coverage
at all before this leaf: a cold-start CLI run establishes an identified empty first generation and the
shipped comparison then reads the first invariant as an addition; a *selected* fork point that is
missing or corrupt is refused by name and establishes nothing; an establishment that cannot be exposed
claims nothing; a resume run naming an unreadable baseline replaces nothing; a damaged half is named
and left exactly as it is; an identified generation is not replaced by a later selected baseline; the
write site places only bytes that read as a dataset; and on the review surface an absent before half,
an unreadable before half, and the entry route's own damaged-half refusal each answer as named states
rather than as an empty substitution or a traceback.

Two route-level registration facts were **corrected** in the same pass rather than carried, and both
matter to anyone reading this route's manifests: `test_knowledge_curator_ingest_list.py` **is** placed
in the `unit-regression` lane (`mcp/tests/test-evidence-lanes.toml:86`) — an earlier card claimed it
carried no placement — and it carries two `consumers` rows in
`mcp/tests/evidence-lifecycle.toml` (`:730`, `:1265`), not one. The budget the added cases are
collected under is the current `pyproject.toml` declaration (`unit_case_budget = 4000` at `:278`,
`integration_case_budget = 1000` at `:279`); the "hard 2300" quoted in older sections of this route is
a historical figure from an earlier series line, not the current ceiling.

- The cold-start operation end to end, and the non-conforming case the requirement names. [207]
- The failure and recovery boundaries: an establishment that cannot be exposed claims nothing, and a resume naming an unreadable baseline replaces nothing. [208]
- The half's own states: damage named in both of its forms, and an identified generation that a later selected baseline may not replace. [209]
- The write site's own byte precondition, and the pair the cold-start run authored read back as an addition. [210]
- The five helpers, each existing because the before half is derived from an enclosure's own recorded worktree group. [211]
- The review surface's three before-half cases, and the task context the entry-route case has to *be*. [212]
- The lane row this route's ingest-list module occupies, and the current case budgets. [213]

## 260915-CAPS-L15 Launch-Wiring Test Population

One new module, `mcp/tests/test_capsule_launch_wiring.py`, **14 cases**, and it is the acceptance test
this master lacked: every earlier capsule case hand-supplied the intermediate value, so none of them
could have failed if no production launch point supplied a capsule at all. This module drives the
production path and reads the artifact from the **consumer's own side**.

| Case group | What it pins |
| --- | --- |
| the acceptance pair | a task-attached seat through the spawn primitive, and a free agent (`bootstrap`, no task document) through the dashboard route — the runner argv the launch point itself built is parsed back out of the base64 the child would exec, the real runner preparation and adapter factory run, and the capsule is read from the session's own `thread/start`, compared against the compiler's own result |
| the production-chain pair (fix round 1) | the route's own `TerminalSessionSpec` (cwd **and** env) fed to `parse_runner_config` → `_prepare_controlled_launch` → `launch_spec_binding` → `verify_capsule_binding`, and the spawn side's agreement with its own capsule — **replacing a deleted hand-supplied case** (`L15R-2`'s evidence class) |
| the mode gate and the refusals | every seat class's answer, and an un-compilable role refusing by name with `host.ensured == []` |
| behaviour 6 | the capsule-free payload byte-identical to the pre-capsule one |
| the payload bound (`D12`) | exactly one `trustedInstructions` key, and no task context in argv |
| the enumeration guard | every `TerminalLaunchRequest(` site is wired or declares its legacy chain, and the site **set** cannot change silently |
| `D13` / `D20` | the registered operation resolves a repository through its declared schema; a first refusing stage refuses again in the same process |
| the free agent's admission | the named absence, and an identity that moves with the seat |

Its lane row is `unit-regression` (`mcp/tests/test-evidence-lanes.toml:19`) — the cases run in process
with the vendor boundary recorded and the tmux host doubled — and it made three governed artifacts gain
a consumer row, which is why `evidence-lifecycle.toml`'s byte pin moved at this leaf's tip without any
population changing. **The live system-block half of the evidence is not here**: it is
`notes/reports/260915-CAPS-L15-evidence/E8-fix-r1-production-chain.txt`, which starts a real eve runtime
from the production chain's own captured cwd and env.

- The acceptance pair, read out of each started session's own first prompt. [214]
- The production-chain pair that replaced the hand-supplied case. [215]
- The refusal before any host effect, the mode gate, the byte-identical legacy payload, the single-carrier bound and the site enumeration. [216]
- The declared legacy exclusion, the free agent's admission, and the two defect pins. [217]
- The production-chain evidence the module's in-process cases complement. [218]

## 260915-CAPS-L5 Codex Capsule-Delivery Test Population

One module and two fixtures join this route. `test_codex_capsule_delivery.py` collects **28 cases**
(`pytest --collect-only -m ""` → `28 tests collected`; the default selection collects the same 28 — the
module carries **no `integration` marker**), registered in `test-evidence-lanes.toml` under
**`provider-conformance`** at entry row 216, between `test_codex_app_server_adapter_turns.py` and
`test_harness_control_claude.py`. That lane is its behaviour-preserving one: its subject is the vendor
app-server's instruction channel — a schema fixture generated from the installed `codex-cli 0.151.0`,
one live native case, and the Codex adapter/session seam — exactly like its sibling
`test_codex_app_server_*` modules.

Two fixtures arrive with it, both **expiry artifacts pinned to the installed CLI version**:

- `codex_app_server_instruction_channels.json` — the independent side of the wire comparison: the
  instruction fields per thread-open request (`baseInstructions` + `developerInstructions` on
  `thread/start`, `thread/resume`, `thread/fork`; **none** on `turn/start`, which is the fact the whole
  lifetime design rests on) and the response's `instructionSources`. Read by the test, never imported
  from the module under test.
- `codex_app_server_model_page.json` — one captured real `model/list` page, because the leaf's first
  hand-written drafts were rejected by the production parser. The durable answer was to capture the
  vendor's real reply and pin it.

The module's shape is worth naming: it drives **production** seams and doubles only two things — the
transport (so wire shape is asserted without a vendor process) and the transient capability-preflight
discoverer (so the launch-boundary case does not start a second vendor process); the real adapter in
those cases still comes from the production factory. Its load-bearing cases are noted on its sidecar.
The live case is gated by a `skipif` version check, so a skip is never a pass.

## 260915-CAPS-L4 Capsule And Skill-Serving Test Population

One module joins this route: `test_capsule_serving.py`, **30 collected items** — **28 in the unit
population and 2 marked `integration`** — registered in `test-evidence-lanes.toml` under
`unit-regression` at entry row 19. It grew from 21 to 30 items across the leaf's two repair rounds.

Its shape is worth naming because two different kinds of case live in one module:

- **Twenty-eight hermetic cases** over a `World` fixture: a disposable coordination root with a contract
  and leaf/master task documents, plus a synthetic skills corpus whose bytes the cases can predict
  (including a nested skill). They cover capsule admission and refusal (the role string cannot acquire
  another role, an unknown role gets its own status, a task path escaping the task root is refused, the
  manifest decides the source set rather than the caller, a moved task document is **re-read** while a
  recorded admission whose bytes moved is **refused**, the operation writes nothing to the tree it
  reads, and altitude admission is pinned across **every** role the document can carry so a hardcoded
  role fails) and skill serving (origin and revision kept, a body whose bytes changed since the catalog
  refused, reading grants none of the tools the frontmatter names, a resource read leaves the tool
  surface and response registry unchanged, same-named skills from two servers stay distinct, the
  discovery registry is not the model-visible catalog, a skill body is not composed into the instruction
  stream, a non-conforming skill directory is recorded not served).
- **Two real-process exchanges**, the only `integration` members: the shipped entry point is started as
  its own process and driven by the **installed SDK's own client** (`mcp.client.stdio` +
  `ClientSession`) — an implementation independent of the server code under test. The exchange observes
  the negotiated capabilities, the resource list, the index, a selected body, a supporting file, a
  refusal, **and both extension methods** (`skills/list`, plus `skills/get` with an absent URI refused
  `-32602`); the other attempts a traversal path from the live process and requires the read to be
  refused.

The cases the repairs added are the ones worth naming here, because they are what makes the module's
coverage claim honest rather than self-derived: `test_every_sep_2640_entry_is_complete_and_carries_verbatim_frontmatter`,
`test_this_servers_own_index_resource_keeps_the_agent_skills_discovery_shape` (this server's own index
shape, asserted separately from the enumeration surface),
`test_a_catalog_record_that_escapes_its_skill_directory_is_refused`,
`test_the_index_reader_refuses_while_a_skill_cannot_be_served`,
`test_a_skill_whose_directory_name_disagrees_with_its_name_is_recorded_not_served`,
`test_the_extension_declaration_is_installed_once_per_server`, and
`test_a_nested_skill_is_published_flat_like_any_other`. Each drives one previously-unpinned guard
directly instead of asserting from a neighbouring surface.

Three cases run against the **shipped corpus** rather than the synthetic one (the corpus parses and
every served skill has a root revision, the composition manifest declares the skill that is served, the
index document is the expected shape); those are the cases that would catch packaging drift between the
canonical root `skills/` tree and the served copy. The module also carries
`test_the_mutation_harness_can_actually_fail`, which is what keeps the leaf's seeded-mutation evidence
honest.

- The fixture world and the synthetic corpus every hermetic case is built from. [219]
- The admission guarantees: no role acquisition by string, no caller-selected source, no write to the read tree. [220]
- The guards the repairs pinned, each driven directly by its own case. [221]
- The SEP entry contract, asserted separately from this server's own index shape. [222]
- The two independent-SDK-client exchanges, including both extension methods and the `-32602` refusal. [223]
- The case that keeps the seeded-mutation evidence honest. [224]
- The lane row that selects this module into the unit population. [225]

## 260915-CAPS-L20 The Governing-Overview Guard And Its Wiring

This route gained one module and one case, and they protect two halves of one defect that were
separately invisible.

`tests/test_governing_overview_resolution.py` guards
`memory_quality/integrity/governing_overview_resolution.py`'s **discrimination**. Its single case
seeds, in one temporary tree, a card with a live field and a dead body link (`D3`'s shape), a card
whose field resolves under no base and which is broken in the body too (`D16`'s shape — the card the
per-declaration rule exists for), and both observation shapes, beside a clean card and a route
overview that must stay green. It asserts the **identity** of the finding set as `(card, code)` pairs
rather than a total, because a count cannot show that both representations were reported, and it
asserts `unresolvedField` and `unresolvedLink` separately so a first-match-wins regression cannot hide
behind a sum. It also pins the walk population, so a widened root would red it.

The second half lives in `tests/test_memory_quality_runs.py`, because the silence was the product
defect: `test_a_dead_governing_overview_reaches_the_gated_repair_set` drives
`_attach_curator_checklist` with a real onboarding tree holding one card whose body link resolves to
nothing, and asserts the finding arrives in the gated repair set the curator's loop reads — its code
exactly `["governing-overview-link-unresolved"]`, and the published `unresolvedLinkCount` beside it. A
correct checker whose findings never reach `repair_findings` still reports a clean
`curatorActionableCount`, which is exactly how 41 dead declarations passed every gate.

Both new modules are registered in this route's `test-evidence-lanes.toml`, so the fail-closed lane
loader stays complete: the new test module is its own row, and the extended module keeps its existing
one. The unit population moved 11 → 12 cases in `test_memory_quality_runs.py` and gained this leaf's
one new module case — a net **+2** against the leaf's measured base.

## Purpose

Terminal cleanup and abandonment exclude the computed root ledger cache from memory dirtiness and discard only that cache before ordinary Git worktree removal. Actual code/memory edits and branch ancestry remain protected. Abandon preview passes its preview state to result validation. The existing Git and public-terminal tests cover these boundaries.

This route retains a small behavior-oriented verification population plus shared fixtures. The
terminal-evidence cursor suite is a focused unit-regression module for no-loss deque envelopes,
unsupported-harness refusal, bounded Pi continuation, and liveness failure containment. A file
named `test_*.py` may still contain only builders; its filename and historical sidecar do not
establish current test coverage. Read the current file card and source before claiming a scenario
is protected or restoring an old matrix.

## 260915-CAPS-L6 Native eve Adapter Test Population

Five modules join this route for the native eve session adapter (`CAPS-R06@v1`), and their shapes
differ in a way a reader must not flatten: **two are collected suites and three are support or
explicit-run scripts.**

- `test_eve_protocol.py` (collected) — wire-contract conformance, nine classes. Beyond the original
  framing/parsing/routing faces it now carries `EveReplayWindowTests` (the bounded replay window's
  eviction, size-1, id-less and non-positive cases), `EveWireBodyTests` (create *and* follow-up both
  spell the queued policy), and `EveWireRequestTests`, which drives the **production**
  `EveRuntimeProcess` through `httpx.MockTransport` so the sent request is asserted instead of
  inferred from a double.
- `test_eve_adapter.py` (collected) — ten case classes, one per named scenario, driving the real
  adapter and mapper through the transport seam; only the eve process is replaced.
- `eve_adapter_test_support.py` (not collected) — the deterministic **transport** double, shared by the
  adapter suite. It is not an adapter double; replacing the adapter there would make every case
  vacuous. Its cancel observation records the `(session_id, turn_id)` pair so a wrong-turn cancel can
  fail.
- `eve_fixture_model.py` (not collected) — a deterministic OpenAI-compatible model **provider** the
  live fixture starts as a child process.
- `live_eve_native_fixture.py` (not collected, run explicitly) — the live proof against a real eve
  process, real HTTP and a real durable stream. It needs Node ≥ 24 and an installed dependency tree,
  which is exactly why it must not join the default suite; its JSON artifacts are the evidence, not a
  pytest exit code.

`test_harness_launch.py` is extended rather than joined: `_knob_values` now collects `knobs.env`
beside argv and session config, because eve's model and effort are compiled application values with no
argv spelling. The parametrized launch-vocabulary contract therefore covers four harnesses, driven
from `sorted(BUILTIN_PROTOCOL_HARNESSES)` — the registry the factory itself consults.

Route consequence: "the suite protects this scenario" now depends on `test_*.py` collection for the
two adapter/protocol suites and on an explicit `--report-dir` run for the live fixture. A live
scenario is only proved by its artifact, and a blocked run is not a pass.

## 260915-CAPS-L2 Role-Capsule Compiler And Admission Coverage

Two new modules cover the deterministic role-capsule compiler, split by the boundary they exercise.
`test_role_capsule_compiler.py` holds **49 test functions (50 collected)** on the compiler's
observable properties, built on an in-memory fixture that mirrors the canonical manifest schema so a
case varies exactly one fact; `test_role_capsule_admission.py` holds **43 test functions (54
collected)** covering the frozen vocabulary, the manifest parser, source admission, the shipped
corpus end to end, the routing agreement between each role's own file and the compiled capsule, and
the carried skill channel. Together: **104 passed**. Unit population 885 → **989** against a budget
of 1000; integration 225 of 250 and unchanged — no integration case was added.

**Three boundaries carry the review repairs.** First, **routing agreement**: the admission module
now cross-checks each role's own canonical source against the manifest it routes from, over every
declared operation, so a manifest that quietly disagrees with the prose it routes to fails. Second,
**the carried skill channel**: a declared skill produces exactly one reference per declaration with
a revision that follows the admitted bytes; a role declaring none gets an empty tuple; a missing or
unknown skill is refused rather than dropped. Third, **source-value integrity**: revision-equals-
digest, decodes-to-nothing, and non-UTF-8 are refused in the compiler module, and
`test_a_source_that_is_not_utf8_text_is_refused` is the only case proving the `source-not-utf8` code
is reachable.

**The two capability channels are asserted separately, and that is deliberate.** Tool ids are
policy-narrowed — a request outside the admitted snapshot is refused. Skill references are carried —
**no permission assertion exists over a skill reference anywhere in either module**, because the
implementation makes no policy call for them. Merging the two into one "capability" case would hide
exactly the distinction the code draws.

The split is deliberate and worth preserving. The compiler module must **not** read the real corpus:
a fixture that mirrors the shipped tree can only be mutated by editing the thing under test, which
is how a vacuous assertion gets written. `test_role_capsule_admission.py` is therefore the only
role-capsule test that reads the real tree, and its 9-way parametrization is what makes "every
shipped role compiles from disk twice to one digest" a corpus claim rather than a single-role claim.

Two cases carry more weight than their size suggests. `test_the_role_and_operation_literals_agree_with_their_runtime_tuples`
guards a **deliberate duplication**: the frozen registry is declared twice — a PEP 695 literal for
the type checker and a runtime tuple for selection — because PEP 695 `type` aliases do not answer
`get_args`, so the ruff-preferred alias form silently produced an *empty* runtime registry. The
duplication is the fix, and this case is its guard.
`test_every_tool_the_shipped_manifest_requests_exists_in_the_public_roster` holds every tool id the
manifest declares against the published roster, so a typo is an error rather than an inert request.

The determinism assertions must stay **falsifiable**. An order-insensitive or input-insensitive
digest would make the whole determinism group vacuous, which is exactly what a seeded-mutation probe
found in an early candidate: the case then compared one fixed order with itself. Two cases were
added as the repair — order is identity, and a real binding change moves the digest — and the
structure-only guard `test_the_compiler_modules_import_no_network_client` sits beside the behavioral
`test_composition_succeeds_with_network_and_model_access_denied`.

Independent falsifiability for these cases came from a task-local probe (seeds M01–M10, `all 10
seeded mutations were caught`) that is **not** a product artifact and is deliberately not promoted
into `mcp/tests/`; it lives in the coordination task tree and expires on the next change to
`mcp/tests/test_role_capsule_*.py`, at which point these shipped cases are its executable
replacement.

## 260915-CAPS-L3 Task-Context Projection Coverage

One new module covers the task-context projection: `test_task_projection.py` holds **9 test
functions (9 collected)**, all unit, built on a synthetic coordination tree that mirrors the real
enclosure's topology. Unit population 989 → **998** against a budget of 1000; integration 10
deselected and untouched — no integration case was added, because no boundary under test is
integration-only.

**The module's docstring states the anti-vacuity rule as contract:** every case derives its expected
side from a source the projection does not feed — the fixture files written to disk, the task
layer's own frozen vocabularies, or an independently parsed copy of the projection's output. A
comparison whose two sides both came from the projection would be vacuous, and this repository's
reviews have rejected that class twice. Hold a new case to the same rule.

**Three cases carry more weight than their size suggests.** The **import-surface case** parses every
module in the package and asserts no writer, transport or task-JSON import appears — that is what
makes "task truth is read only through the owners" and "the projection is read-only" checkable
properties rather than prose claims. The **byte-identical case** digests the whole synthetic task
tree before and after both a successful projection *and* every refusal, which is the observable
consequence of the read-only contract. The **seam case** runs the projection through the compiler
protocol and then forges a digest to prove the compiler refuses it, so the seam is shown to be
two-way rather than decorative.

**The remaining six own one property each:** cross-task isolation (two leaves never leak each
other's private content), altitude scope (a sprint's decision log reaches an orchestrator but is
never injected for a leaf), operation specificity (each frozen operation selects its own channels and
document), the failure taxonomy (each unresolvable input returns its own status), three-plane
separation (a historical record and a proposal never read as a current obligation), and no
truncation (an obligation is carried verbatim while a section the packet lacks is a reported gap).

**A fixture trap worth not repeating.** The synthetic tree took three rounds (`CAPS-L3-EV5`–`EV7`)
to mirror the real topology: a leaf enclosure needs `kind: leaf` *with* a `leaf_id`, an
external-memory contract needs its ledger leg, and — the subtle one — **an internal memory root
silently wins over an external coordination hint**, so a fixture with an internal memory root
searched the task tree in the wrong place. A new fixture that does not reproduce the external
topology will exercise the wrong resolution path and still look green.

Independent falsifiability for these cases came from a task-local probe (seeds `M01`–`M20`, `all
seeded mutations were caught`, `vacuous: 0`) that is **not** a product artifact and is deliberately
not promoted into `mcp/tests/`; it lives in the coordination task tree and expires on the next change
to `mcp/src/agents_remember/application/task_projection/**` or `mcp/tests/test_task_projection.py`, at
which point these shipped cases are its executable replacement. That probe found a vacuous seed in
its own first run (`CAPS-L3-EV10`: a planted "silent fallback" was blocked by a second guard, so the
target case passed for the wrong reason); the probe now fails on a vacuous seed by design.

**Pyright reports exactly one finding for this module** — `Import "pytest" could not be resolved` —
which is this repository's pre-existing condition for every pytest-importing test module, reproduced
on the untouched shipped `test_role_capsule_compiler.py` as the control. No scoping change and no
`# type: ignore` was added to hide it.

**This module has no evidence-lane row, and the route must not be read as if it did.** The
fail-closed loader `load_lane_manifest` derives the expected test population from the
tracked-and-untracked modules under `testpaths = ["mcp/tests"]` and raises `LaneManifestError` for any
test file without an explicit lane, so `test_task_projection.py`'s absence from
`test-evidence-lanes.toml` means the manifest **does not load** as this candidate stands — the
`pytest_collection_modifyitems` hook that calls the loader and `code_quality/check.py` both turn that
into a failure. This is a code-side gap for the owning seat, not an onboarding one, and it is **not
this leaf's alone**: `test_role_capsule_compiler.py` and `test_role_capsule_admission.py` (from
`CAPS-R02@v1`) and `test_role_instruction_corpus.py` (from `CAPS-R01@v1`) are missing from both
manifests too, so the correct repair is a four-row change. Derived from the loader's source rather
than executed: this curation seat runs Python 3.10 and the repository requires `>=3.13,<3.14`, so
`import tomllib` fails and the loader could not be run here.

## Hot Path Summary

For the ledger retirement, start with transaction-only delivery, direct landing, integration/checkpoint concurrency, memory ledger projection and backfill tests. Assertions distinguish cache-only conditions from actual content, ancestry, ref and ownership failures. The retained producer census checks every active attributed memory writer; no scenario expects a third ledger commit.

Start with the distinct failure or user operation, then locate its retained owner. Checkout isolation, Dagger registry locking, private Git preparation, protected-ref recovery, durable-store races, submission authority and native framing each retain concrete behavioral protection. Compiler/certificate fixtures establish library contracts; they are not live Dagger, Codex or final-memory execution evidence. Preparation checks can guide memory repair before certification without becoming Gate 5.

For the knowledge substrate, start with the five knowledge modules and their two shared support artifacts: `test_knowledge_store.py` (invariant identity and lineage), `test_knowledge_family_revision.py` (family revisions and the family lineage), `test_knowledge_relation_rules.py` (anchors, memberships and claims, including the anchored-claim transaction), `test_knowledge_graph_reads.py` (the two relation directions compared by identity) and `test_knowledge_revision_seals.py` (the sealed predecessor field on both payloads, which exists because round 1 could not kill it). Both support modules are registered contracts in `mcp/tests/evidence-lifecycle.toml` with exact consumer lists, and all five modules are unit-regression rows in `mcp/tests/test-evidence-lanes.toml`. **The read half adds three more** and one shared support artifact:
`test_knowledge_read_scope.py` (unit-regression — the selection policy, the corrected page counts, revision
grouping, budget, the execution bound and typed absence), `test_knowledge_read_boundaries.py` (integration —
the seven anchor observations against a real committed Git tree, the snapshot/namespace/schema refusals and the
continuation bindings) and `test_knowledge_read_paths.py` (integration — what a *path* is to this read: an
address, not a pattern), all three consuming the governed artifact `read_scope_test_support.py` under contract
`knowledge-read-scope-cases`.

**The schema-generation and envelope half is its own pair plus one shared support module.**
`test_knowledge_schema_generations.py` covers the generation registry: that generation 1's fingerprint
recomputes byte-identically to its pinned constant and that the gate **raises** when one recorded
generation-1 field is perturbed (one DDL string, one trigger body, one column tuple — a pin observed only
passing is a comment), that the artifact key lookup is type-strict so `1.0`, `"1"` and `true` are refused
while the integer `1` resolves, that an unregistered version is refused by the open path, that creating a
store declares generation 2 while opening a generation-1 file reports generation 1 **with generation 1's
recorded fingerprint**, and the acceptance check a partial fix fails: adding and populating a
generation-2 table **changes** the generation-2 logical digest.
`test_knowledge_merge_generations_and_envelope.py` covers the mixed-generation preflight and the payload
seam: a v1/v1/v2 merge refused before any session exists with its positional role and expected/observed
versions and all three inputs byte-identical afterwards, **a v1/v1/v1 merge on this generation-2 build
passing** with generation 1's ten tables attached, an envelope payload refused with `invalid_payload` and
no row written, and the route hierarchy cases. `generation_test_support.py` is their shared harness: it
builds a **real generation-1 dataset from generation 1's own recorded DDL**, which is what every case
asserting a generation-1 fact must use — a fixture created by the build is generation 2, so a digest or
context built from the literal `"ar-knowledge-sqlite/v1"` describes a dataset the fixture does not hold.
`test_knowledge_routes.py` adds eighteen cases over the route *write* layer: confinement refusals for every
refused path form, an existing route returned for an already-authored path rather than a second row, an
unauthored parent refused, a three-node cycle refused with the rollback restoring the hierarchy, the
association's four refusals, idempotent re-statement, and `None` for an explicitly ungoverned row.

**The candidate and snapshot half now has its own pairs.** `test_candidate_batch_transaction.py` and
`test_candidate_batch_commands.py` cover the batch boundary and its command union (sharing
`candidate_batch_test_support.py` as their registered harness, with `test_knowledge_label_operations.py` existing
for the standalone label guard the batch path could not see), and `test_knowledge_candidate_workspace.py` and
`test_knowledge_snapshot_publication.py` cover the candidate lifecycle and the publication contract, sharing
`snapshot_lifecycle_test_support.py` — registered as `knowledge-snapshot-lifecycle-cases` with an exact
two-consumer list. **That support module's evidence node is
`test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not`, and the node is chosen for its
subject rather than its convenience:** the suite's load-bearing claim is that a published snapshot is *closed*,
which is only measurable by showing a committed-but-WAL-resident batch surviving into the published file while a
bare main-file copy of the same database does not carry it. The lifecycle suite's two durability nodes are its
other distinctive protection: one reaches the live-reader state that the removed unconditional WAL/SHM peer unlink
destroyed, and one uses a **real child interpreter** that exits with an uncommitted write transaction open. All
four modules registered by L3 and L4, and both support harnesses, are unit-regression rows with registered
contracts; a test-shaped module missing from either registry fails the load rather than passing quietly.

## 260915-CAPS-L1 Role-Instruction Corpus Contract

`test_role_instruction_corpus.py` is the focused check the lifecycle-corpus consolidation added to this
route. It is a **shipped repository test**, not a task-local fixture, and it protects the corpus's shape
rather than its prose: every role in the registry has exactly one readable source; every role source
carries the agreed six-section order, its `**Inherits:**` line, and its knob block after the handoff
section; the composition manifest resolves every role, operation, core block, template, and criteria
catalog it names; the registry is exactly nine roles with the ambient launcher as a routing condition
rather than a tenth role; the manifest carries no instruction prose; every relative path the corpus cites
resolves; and a manifest entry pointing at a missing source is **reported rather than silently accepted**.

Its `SANCTIONED_SIBLING_REFERENCES` table makes the corpus's independence rule executable — a role file
may name a sibling role file only to wear that hat or dispatch that seat, and anything else fails the
check by design. Because the assertions are property-based on the corpus's shape, they stay valid as role
prose changes; only a corpus shape change should require editing the module.

## 260915-CAPS-L18 Complete Curation Reaches This Route

`test_role_instruction_corpus.py` was extended (6 → 14 cases) with `CurationIsCompleteOnEveryLeafTests`
and `CurationGuardTeethTests`, which read the new `testing/curation_doctrine.py` registry and sweep the ten
shipped surfaces. CAPS-R18@v1 inverted the optional/narrow-curation doctrine in the shipped instruction sources. The
sentences that presented the full `memory_quality_check` operation and the `curator_coherence`
certification as developer-request-only diagnostics, "never routine closeout/integration prerequisites",
are gone. The rule is now normative: **curation is complete on every leaf** — the full operation runs at
the leaf's contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every
curator-actionable finding is repaired or escalated as blocked with its exact returned code, and the
operation is re-run after every repair until `curatorActionableCount=0` and the **raw**
`qualityChecklistStatus=ready-for-closeout`. The **combined** `checklistStatus` is rewritten to
`coherence-required` **only when the coherence record is then missing or stale** — that is the coherence
gate, cleared by publishing the `curator_coherence` authority with `prepare` → `publish` → `validate`.
On the success path, where the record is already current, the combined field is **not rewritten** at all
and keeps its incoming `ready-for-closeout` value, with `closeoutReady=true`; `ready-for-closeout` is
therefore observable in the combined field once the whole pipeline is already complete. **Field-name
correction (`D35`, made by 260915-CAPS-L10):** this sentence previously named
`checklistStatus=ready-for-closeout` as the loop's termination condition; read the raw field to end the
loop and the combined field to decide the coherence gate
(`application/memory_quality/controller.py:664`, `:671`, `:678`, `:685-687`).

**Warrant corrected by `CAPS-R19` (leaf `260915-CAPS-L19`).** The `D35` correction above originally rested
on the sentence *"`ready-for-closeout` is never a value of the combined field."* That absolute claim is
**literally false**, and `CAPS-R19`'s revision note records it as superseded by the three-path model now
stated here. The field-name correction it supported still holds; only its stated warrant was wrong.
**Attribution is complementary and both halves hold:** `260915-CAPS-L10`'s curator corrected the
**onboarding cards** that carried the wrong form, while `CAPS-R19` corrected the **shipped sources** — the
five loop-gate carriers, their nine generated copies, and the guard registry's own docstring — and brought
`docs/reference/mcp-tools.md` into both the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`.

Two corrections the inversion must not collapse, both preserved: closeout still owns only the Git
transaction and **invokes** nothing — it **carries** the completed curation as a prerequisite; and the
rule is about the completeness of curation, not about unscoped runs, so "complete" always means the whole
operation at the leaf's contract scope. The ruling is forward-looking: the already-landed and finalized
leaves are not re-curated, and whole-layer completeness is discharged by L11's full-scope run at the
frozen tip.

## CCR-R12@v5 Transaction-Only Delivery Route

`test_transaction_only_worktree_delivery.py` exercises real public closeout and paired integration. It checks actual code/memory refs and the memory-content `Code-Commit:` trailer, source movement refusals, configured-hook behavior, interrupted recovery and cache rebuilds. Missing, malformed or changed cache bytes do not create commit objects or gate delivery. The suite retains real content/ref failures instead of replacing them with cache checks. This overview describes coverage, not a current aggregate test result.

## Retained Behavioral Routes

| Concern | Current starting point | Boundary |
| --- | --- | --- |
| Checkout/host lock composition | `test_checkout_coordination_isolation.py`, `test_dagger_registry_lock.py` | Real path/lock refusal with temporary state; host authority does not open coordinator writes. |
| Durable state and event-loop liveness | `test_durable_store_contract.py`, `test_cross_store_lock_order.py` | Thread/process ordering and actual store outcomes, bounded by watchdogs. |
| Candidate and protected-ref safety | `test_git_command.py`, `test_integration_branch_authority.py` | Real Git identity, private commits, hooks and race preservation. The former `test_integration_ref_transaction.py` was deleted with the removed mid-crash ref-recovery capability..; mcp/tests/test-evidence-lanes.toml:224-341; mcp/tests/test-evidence-lanes.toml:181-217; mcp/tests/test-evidence-lanes.toml:229-348; mcp/tests/test-evidence-lanes.toml:247-247 |
| Terminal liveness cadence and readiness | `test_terminal_liveness.py` | Controlled-clock sweeper checks preserve the configured full-sweep interval and the one-second starting-row path with its four-row cap; lifecycle production wiring remains a separate candidate proof. |
| Serving-owned steady-state observation and pass-failure isolation | `test_serving_observation_loop.py` | The real `_serving_lifespan` finalizer under a virtual event-loop clock with no HTTP route registered: the completion-relative `DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS` sleep after each attempt (including a failed one), attempt non-overlap when a pass outruns its tick, the sweeper's retained ten-second full-sweep limit, observation continuing while `agent_notifier.enabled` is false, the off-loop refresh through the drained helper, exactly one observer task cancelled at teardown, and a failed pass that neither marks success nor changes cadence. Its `ServingObservationFailureIsolationTests` half then pins the failure boundary itself on the real task collection: one unexpected pass failure leaves the owner scheduled and the five sibling loops plus an in-process ASGI request alive, publishes nothing durable (with a control proving a *successful* pass does change the tree), and retries on the cadence alone from the current persisted catalog while rows, the emitted-signal marker and the workspace cursor survive; cancellation still ends the task because the boundary is `except Exception` and `CancelledError` is a `BaseException`. This module also owns the **shared serving fixture**: `_ServingFixture` is imported by `test_serving_startup_prime.py`, and its `startup` witness plus its `_Gate` parkable probe `inner` are a shared contract — **call 1 of a lifespan timeline is the pre-serve prime and call 2 is the recurring owner's own first pass**, so a case that parks or fails invocation 1 addresses the prime rather than the owner. Unit lane; the sweeper's own cadence files stay the owners of their clocks. The notifier's pre-existing inline refresh, any structured observer-failure *publication* surface, and the prime's own ordering contract are out of this proof. |
| Startup observation prime before projection and recurring loops | `test_serving_startup_prime.py` | The `LOCR-R18@v1` half of the same serving seam, driving the real `_serving_lifespan` through the shared fixture imported from `test_serving_observation_loop.py`: exactly one observation prime at the head of the timeline, dispatched off-loop through the drained helper and parked while event-loop timers keep firing, positioned before `runtime.projector.prime()`, before every recurring task and before the lifespan yield; the seeded `ready` row committed as the adapter's `unsupported` verdict and read back by both the captured initial projection and the captured first notifier sweep; a prime taken with a real `GET /api/terminal/sessions` route registered and never dispatched and with the notifier loop started but never sweeping; and the committed entry equal to one reference canonical pass over an identical seed, so no startup-only reader, cursor or write path took part. A raised prime is contained — startup, the projection prime and the recurring owner all survive and the owner retries on its first cadence. Unit lane, hermetic, ordinary test source; it asserts no health or readiness payload, and its ordering witness does not constrain prime-versus-migration/compaction (that edge rests on the production straight-line order). |

| Deferred terminal work | `test_terminal_liveness_deferred_work.py` | Real catalog/sweeper proof that hosted-interaction syncs and turn callbacks run after commit, aborted batches dispatch nothing, and post-commit failures preserve durable truth. Caller ownership remains adjacent lifecycle work. |
| Terminal catalog liveness | `test_terminal_liveness.py` | Fake-clock host/control-read hysteresis, restart continuity, and successful reset against existing production transitions. This row is the LOCR-R21 hysteresis proof only: cadence (`R12`) and sweep non-overlap (`R22`) cases for the same module are still in their own unlanded worktrees, so the composed module's case count and extents will be larger than this leaf's four cases. |

| Terminal catalog batch and sweep non-overlap | `test_terminal_catalog.py`, `test_terminal_liveness.py` | Counted `_write_disk` replacements (zero clean, one dirty, one dirty-partial) and real-thread sweep contention returning the committed snapshot without a second probe; cadence (`R12`) and hysteresis (`R21`) values stay with their leaves. |
| Candidate and protected-ref safety | `test_git_command.py`, `test_integration_branch_authority.py`, `worktrees/integration/integration_ref_transaction.py` | Real Git identity, private commits, hooks, race preservation and exact recovery..; mcp/tests/test-evidence-lanes.toml:223-340; mcp/tests/test-evidence-lanes.toml:207-207; mcp/tests/test-evidence-lanes.toml:244-244; mcp/tests/test-evidence-lanes.toml:246-246; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:103-103; mcp/tests/test-evidence-lanes.toml:210-210 |
| Registry/certificate semantics | `test_certification_rail_registry.py`, `test_gate_certificate_authority.py` | Typed plan/result contracts and dependency-aware reuse, not a live producer claim. |
| Memory preparation and repair | `test_memory_quality_runs.py`, `test_citation_document_transaction.py`, `test_memory_citation_fix_scopes.py` | Exact-pair revalidation, document isolation, conflict refusal and preserved evidence. |
| State-signal structural routing | `test_state_signal_relay.py` | Action-time current-manager replacement, per-subject topology refusal, no-row/no-marker behavior while an owner is absent, and no owner wake while a seat's own turn is still open. |
| State-signal boundary delivery | `test_state_signal_boundary_delivery.py` | Row persisted before the emitted marker, zero adapter submission while the target is `working`, and delivery of that same durable row at the target's next admissible boundary across occupant replacement, fresh notifier context, and failed submission. |
| State-signal crash and restart recovery | `test_state_signal_restart_recovery.py` | The durable order row persisted → marker stamped → delivery attempted across a failed marker write, a stop after the marker, and a same-seat structural rebind: one pending row per exact seat/evidence identity, zero adapter submissions while that source marker is unstamped, and an action-time fence on the shared delivery action that state-signal recovery alone may lift. Seven cases, each rebuilt from the durable files through new store objects. |
| Curator turn owner wake | `test_state_signal_curator_wake.py` | The curator seat's own canonical terminal turn reaches the same shared role predicate and current-manager routing as the worker seat, with the durable payload carrying the curator role, the subject leaf document, the mechanical outcome and the terminal evidence identity — all derived by the real liveness sweep and the real agent-notifier sweep, never written by a curator post. A `completed` ending and an `interrupted` ending each mint exactly one durable signal and never a second on re-observation; `failed` reaches terminal truth and emits nothing while leaving the seat eligible; a curator seat whose own master has no current manager fails closed instead of routing to another master's manager; and the wake neither validates nor declares curator coherence or memory readiness. Unit-regression, one new module, no production byte changed. |
| Parked external-await separation | `test_parked_external_await_separation.py` | The parked open-turn external-await design stays out of the ended-turn relay: no `waiting` expectation kind is parseable, no wait-registration tool is advertised, and no wait/recheck/check-descriptor machinery ships. Absence guard only, not relay behavior evidence. |
| Reviewer turn owner wake | `test_lifecycle_owned_completion_relay_reviewer.py` | The reviewer role's own production-wiring relay: a short-lived reviewer seat's canonical terminal truth, produced by a real observation pass rather than a seeded row, wakes the reviewer's **current** manager as one durable inbox row — with no completion post from the reviewer and no dependence on the terminal-session read route. Six cases pin the boundaries separately. The row is truthless before the pass (`turn_state`, `terminal_outcome` and `terminal_evidence_id` all absent) and carries `completed` plus its evidence identity after it; the durable row holds while the owner is mid-turn with zero submissions and lands exactly once at the owner's next boundary. Liveness, a ready `control_state` and even a pane whose own diagnostic reads `turn-ended` authorize nothing, with a control proving the identical row does wake once canonical evidence exists — so the silence is about missing evidence, not an inert fixture. An `interrupted` turn is reported as `interrupted` with `interrupted_by=unknown`, no verdict vocabulary and a byte-unchanged leaf document. The wake is addressed by current occupancy, so a recorded `spawned_by_session` naming an exited manager generation receives nothing while the live manager gets the one row. Re-observing the same evidence identity mints no second signal even after the first row has landed and can no longer absorb a repeat by coalescing. And `failed` — production-reachable with a real evidence identity, since the pi projector settles `stopReason="error"` into it — is refused while leaving the seat eligible, so a later canonical turn still wakes the manager. Unit lane: a temporary coordination root, a scripted single-seat adapter endpoint and a tmux double at the process boundary; the lift, the outcome and the evidence identity are production's, and the relay's own structural rules stay `test_state_signal_relay.py`'s contract. |
| Worker turn owner wake | `test_state_signal_worker_wake.py` | A worker is not required to author a second completion message, so the wake must arrive on its own: an owned `worker` row whose **catalog terminal evidence** says `completed` or `interrupted` becomes a state-signal finding and the notifier persists and routes exactly one durable row to the leaf's **current** manager through the existing inbox path. Seven cases pin the boundaries separately. No inbox row is created for the worker at all, and the whole store is asserted rather than its state-signal subset, so a worker-authored row would be visible rather than filtered out. The eligible-outcome set is pinned from both sides: `completed` and `interrupted` wake the manager, and `failed` or `unknown` must not however real the evidence identity is — with a final leg re-reporting the same seat and evidence identity as `completed` and requiring the wake, which makes the empty store a measured refusal rather than an inert relay. Per-turn dedupe is pinned in both directions too: the same evidence identity projected twice mints one row, and a **second distinct terminal turn** on the same seat mints its own wake instead of being swallowed by the first turn's marker. An `interrupted` turn travels with its origin and is not mislabelled as completed; a report on disk is not terminal evidence, so the adapter evidence identity is the discriminator; the leaf and master documents are captured around the sweep and compared byte for byte, because reporting a seat turn never closes task work; and a worker below a managerless master wakes nobody, stamps no marker and guesses no global owner while staying eligible for the next sweep. An empty live terminal-session read is a measured zero on a host the delivery path demonstrably reached, because `_RecordingHost` counts every contact the sweep makes. Unit lane: a temporary coordination root with real task documents, a real catalog file, a real inbox log and the real durable stores; no HTTP request, no server, no process. The relay's own structural rules stay `test_state_signal_relay.py`'s contract, and the pre-existing dead-upstream supervision row the same sweep separately raises is outside this module's assertions. |
| Incremental memory scope | `test_memory_incremental_scope_compiler.py` | Dependency-complete work and exact reuse remain non-accepting with final-full pending. |
| Native submission and IPC | `test_harness_submission_authority.py`, `test_harness_control_ipc.py` | One request authority, idempotence, withdrawal races and ambiguous receipt reconciliation. |
| Conversation projection and assets | `test_conversation_active_service.py`, `test_conversation_control_attachments.py` | Ordering, honest pagination, one-use assets and unknown-outcome retention. |
| Canonical terminal-evidence mapping | `test_terminal_evidence_mapping.py`, `test_conversation_native_ingestion.py` | Native projectors remain the terminal-outcome authority; malformed or open frames make no terminal claim and do not hide a later canonical outcome. |
| Protocol framing | `test_codex_native_history.py`, `test_pi_rpc_process.py` | Bounded paging/correlation and real fixture subprocess behavior. |
| L38 actionable admission and closeout transport | `test_activation_admission_registered.py`, `test_worktree_closeout_route_review_transport.py` | Registered response-shape and refusal-projection checks, including bounded malformed-contract parser detail, for the frozen candidate. The activation admission is contract-scoped: a refusal carries no `classification`/`blocking`/`sourcePair*` key and never names a foreign master as blocker or retry precondition. Preparation evidence only. |
| CCR-R12 transaction-only delivery | `test_transaction_only_worktree_delivery.py` | Public code/memory delivery, interruption recovery, source/ref safety, hooks, memory attribution and cache-only no-op behavior. |
| Ledger attribution and the projected source ledger | `test_memory_ledger.py`, `test_worktree_sync.py` | Git-only computed rows, cache misses/malformed bytes and hand edits, attributed source history, and cache-independent synchronization. |
| Producer census and the one renderer | `test_memory_attribution_producers.py` | Five memory-content producers and zero untrailered, measured from source: the trailer key identifier and its interpolation appear in exactly one production module, no production module spells the trailer as a quoted literal, each of the five producers reaches a shared renderer entry, and a hostile multi-paragraph caller body survives byte for byte with the trailer appended as its own final block. The two non-closeout producers are driven end to end through the public `memory_carryover_apply` and `memory_baseline_adopt`. Source census plus real-repository cases. **Superseding the note this row used to carry: the module's `unit-regression` lane row now exists** (`.; mcp/tests/test-evidence-lanes.toml:1-223; mcp/tests/test-evidence-lanes.toml:122-122 |
| Leaf document master-link binding | `test_leaf_doc_master_link_binding.py` | The derived master link, end to end on real repositories: a leaf authored through `task_doc` with no series contract acquires `seriesContractPath` and its one `enclosures[]` ref when it is started; an already-damaged document (`lifecycleId` stale, no link) is repaired by its next start with objective, requirements, steps and title unchanged; a leaf under a task root with no master document is refused with `seriesContractPath`, the exact missing `task.json` and the remedy, writing nothing; and the planning flow (master plus two leaves, no start) still succeeds, still unstamped. Integration lane: one disposable code repository and one external memory repository per case. The restamp decision table is the unit half in `test_task_document_application_1.py`. |
| Closeout recovery attribution | `test_transaction_only_worktree_delivery.py` | Interrupted closeout proves actual journaled code/memory commits and refuses forged output evidence; cache state is immaterial. |
| Closeout auto-carry and parked candidate | `test_source_lineage.py` (`CloseoutSourceLineageHealTests`), `test_sync_parked_candidate.py` | The closeout boundary carries a settleable stale break, refuses a preview without mutating, escalates an unprovable break, and returns a parked dirty candidate through the sync transaction (restore on completed/resume/cancel, kept unmerged-index refusal); transaction-level detail lives in the new unit-lane module. |
| Memory-history trailer backfill | `test_memory_backfill.py` | Disposable history rewrite selection, loss reporting, byte-faithful objects, trailer-only acceptance, idempotence and multi-ref CLI publication. |

| Terminal evidence cursors | `test_terminal_evidence_cursors.py` | Focused deque envelope validation, no-advance refusal, bounded Pi continuation, and liveness containment; unit evidence only. |
| Public tool-surface inventory | `test_tools.py` (`PublicSurfaceInventoryTests`) | Live registration order against a probe `FastMCP` equals `PUBLIC_TOOLS`, and the advertised names have response models that validate. Two further cases pin the advertised **text** rather than the roster: the checkpoint landing's description must present a partial publication and deny being the pause (L36), and `worktree_pause`'s must present a stop that publishes NOTHING, name the checkpoint as the separate publication, carry no refusal the verb no longer performs, and still name the release it does perform (L37, extended by L38). Hermetic inventory contract: the probe starts no server and touches no provider. |
| Worktree next-move typing and enforcement | `test_worktree_status_terminal_next_tool.py` | The `terminal-archive-ready` branch of `worktree_status` names the accepted cleanup operation, its emitted args bind to the real tool signature (checked with `inspect.signature(...).bind`), the envelope declares `nextAction`/`nextTool`/`nextArgs`, and the `PUBLIC_TOOLS` membership validator is driven in both directions. Integration lane: real worktree services and a real repository under `tmp_path`. First coverage of that branch. |
| Stop-only pause, and the pause/publication split | `test_pause_stop_only_end_to_end.py`, `test_pause_is_not_publication.py` | The public `worktree_pause` stops an atomic master over one real temporary Git world holding two masters: it releases only this contract's activation record to `vacant`, leaves the other master's record byte-identical and still `active`, moves no ref and creates no commit (both repositories' tips, complete object databases, coordination tree, both worktrees, the enclosure and every task document measured identical before and after), reports `paused: true` with **no** `nextTool`/`nextArgs`/`nextOperation` at the top level or inside `nextStep`, reports a never-selected master as the explicit `atomic-series-already-vacant` success (that case asserted a refusal before the 260831-LOCR-L38 change set) — naming in its summary that no selection was held, and carrying an observation with no `record` where a released pause carries the one its own release wrote — and keeps the four refusal shapes apart without writing anything: a leaf contract (`pause-requires-atomic-master`), a record this contract does not own and an unreadable record (both `atomic-series-activation-release-unreadable`), and a **vacant** record naming another master (`atomic-series-activation-selected-contract-mismatch`), which is the only foreign shape that reads `vacant` and therefore the only one that could be mistaken for the success — an *active* foreign record is refused one step earlier by the observation, so the two cases prove different guards. It is idempotent, and resumes through `worktree_sync` with nothing published. Its sibling is the structural half: `test_pause_is_not_publication.py` (architecture-fitness) asserts the pause module's static import closure is disjoint from all twelve publication modules — measured 60 modules including the root, 5 direct imports, 54 beyond them — with non-vacuity assertions and named witnesses so a walker stopping at the direct imports fails rather than passes, so the stop cannot become the checkpoint publication. `worktree_checkpoint_landing` is the separate, explicitly requested publication and no case here reaches it. Integration + architecture-fitness lanes. |
| Checkpoint landing plan/apply parity | `test_checkpoint_landing_end_to_end.py` | Public unfinished-master checkpoints, actual paired refs, idempotent retry, cache independence, and real source/content/ref-race refusal parity. |
| Sub-task index reachability across a writer skew | `test_task_documents_graph_projection.py` (`SubTaskIndexReachabilityTests`) | Projection-only unit evidence that a completed leaf whose durable JSON carries a field this reader's schema does not know stays reachable from the master's sub-task index, an unstarted row keeps resolving, and a document with a required field deleted is still withheld. `_index_doc` reproduces the dashboard's own index rule (`sliceForRef`) rather than approximating it. Hermetic temporary task root; one case, one helper, no lane change. |
| Cross-master concurrency on one protected source pair | `test_cross_master_concurrency.py`, `test_atomic_series_activation.py` | One sprint commands every atomic master from its own source branches, so two atomic masters share one protected source pair; each keeps its own activation record. Both masters stay ready and progress, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks no sibling (the same statement the stop-only pause now makes as a real public operation, `worktree_pause`, proved separately in `test_pause_stop_only_end_to_end.py`), a conflicting or stale publication is refused at the pair (`blocked-non-ff`, `atomic-series-checkpoint-candidate-moved`), and a master that reconciles with a landed sibling finishes through ordinary public closeout and final integration rather than a checkpoint. A graph-less sprint serializes nothing — `executionGraph=None` resolves to the `atomic-sequential` sprint shape (every commanded master executes atomically, no dependency is declared) and both masters hold their own activation concurrently with no waiting reason. Only a real sprint-graph wave edge still gates (`predecessor-incomplete:`). Integration lane: real temporary Git repositories and the public operations. |
| Capacity refusal source classification | `test_closeout_projection_source_classification.py` | The three states of a projected source stay distinct on the code its own raiser published. `graph_context` refuses a sprint whose authored graph is one node past `MAX_CLOSEOUT_MASTERS` with `closeout-queue-master-capacity-exceeded` — its own declared code, read back from the refusal rather than retyped — and that code classifies `invalid`, because the source was read and is past its bound; `contract-unreadable` and `atomic-series-contract-unreadable` still report `unreadable`; and the ordinary projected source stays readable with no problems and classifies `active`. The classifier tests membership of `closeout_queue_errors.py`'s `CAPACITY_REFUSAL_CODES` instead of the substring `cap-exceeded`, which neither surviving capacity code contains. Integration lane: real temporary Git repositories through `QueueFixture` and the production graph admission path. |
| Registration before compaction | `test_terminal_liveness_registration_order.py` | The full sweep's post-commit order, pinned where it happens: the traced terminated-row read records the batch-commit state observed **at the read**, so the chain `batch-enter → batch-exit → enumerate[include_terminated=True, batch=closed] → register → compact` fails if the enumeration moves inside or ahead of the observation batch. The registrar's returned proved-id set is the only argument `compact` receives, an absent registrar yields the empty proved set (so a task-bound leaf row survives), a raising registrar stops the pass before `compact`, a crash after registration re-registers idempotently on the next pass, and the starting-row fast path does neither stage. Hermetic unit lane; no production byte changes for this contract. |
| Terminal observer health | `test_terminal_observer_health.py` | The observer stage's own health reading (`LOCR-R17@v1`), sixteen cases in three classes: the exact atomic v1 record and its writer (constant-size row, no partial document, the failed-write source of truth being the persisted row rather than the newer in-memory accumulator), the status ladder `initializing`/`degraded`/`healthy`/`stale` at exactly `6 ×` the configured sweep interval, omission-and-no-repair for every unusable source (missing, unreadable, wrong marker, extra or missing key, wrong type, naive stamp, prior-lifetime stamp, above-ceiling counter), the bounded ordered secret-safe failure vocabulary, publication on the observer CALL for success and failure alike through the real lifespan, the fixed write-failure log line with retry, and the served tail driven through the real `_state_response` handler and `stream_events` generator (additive key, untouched ETag/304 path, health on the snapshot and none on a delta, plus the packet's cross-read rows including "healthy beside a fresh notifier"). Unit lane: no HTTP transport, no server, no real second. |
| Terminal blocker reasons | `test_terminal_blocker_reasons.py` | A cleanup or finalize blockage always names the component it stopped on and a non-empty reason. The L6 shape — terminal archive proven, provider runtime already gone — finalizes on the first call with an empty `notRemoved` inventory; a real permission failure on the provider tree blocks with `remove_tree`'s own `permission denied: ...` reason, closes nothing and refuses identically on retry; and both invariant owners are driven directly (`_blocker` refuses a missing, blank or non-string reason, and `remove_tree` names a reason whenever it reclaimed nothing). The L6 payload is reproduced through the provider port boundary, not by re-enacting the original physical event. Integration lane; one new module, no deleted module. |
| Pane diagnostics are non-authoritative for turn truth | `test_terminal_liveness_pane_authority.py` | The pane's own reading is persisted only as `control_raw["paneDiagnostic"]`; adapter snapshots plus the canonical terminal projection own `turn_state`, terminal outcome/identity, interruption origin and state-signal eligibility. Ten cases pin the boundary: contradictory pane/adapter readings in both directions, **readiness** (an adapter `control="disconnected"`/`"failed"` snapshot with a `working` pane keeps the adapter's `control_state`, activity/acceptance `unknown`, turn `stale`), below-threshold retention with the `controlReadFailures` counter, the R21 third failure owning `disconnected`/`stale`, alive-starting retention, the legacy no-`control_endpoint` `unsupported`/`stale` projection proved never to consult the control surface, a failed terminal page advancing nothing, startup-prime and steady-pass sharing one boundary (`host.calls == 3` discriminates the fast path), a four-reading pane-independence matrix, and a negative AST source guard over `terminal_liveness.py` itself. This module is a **deliberate split** from the 574-line `test_terminal_liveness.py`, which it leaves byte-unchanged and from which it imports its fixtures; an in-place extension had reached the coding-guidelines 900-1200 band, so the two cards must not be merged. The source guard is defence-in-depth over behaviour, not the sole pin: it is measured blind to a pane-derived constant inside an enclosing `if`, to positional writer arguments and to `CatalogTurnEvidence(state=…)`, all three of which stay caught behaviourally. Integration lane; one new module, no production byte changed. |

| Observer-to-notifier handoff latency | `test_serving_notifier_handoff.py` | `LOCR-R04@v1`'s completion-relative relay proof, eight cases over one disposable world that enters the real `_serving_lifespan` under a deadline-correct virtual clock, so the real observation loop, the real `TerminalCatalogLivenessSweeper.refresh`, the real catalog commit boundary and the real `run_agent_notifier_sweep` are what is measured. The two loops share no wake-up channel: the observer polls every `P` (1.0 s) after each attempt returns and the sweeper admits one full sweep per `F` (10.0 s) from the previous full sweep's **start**, while the notifier evaluates the durable catalog and sleeps `N` (10.0 s) after its pass returns — so the delivered worst phase is `F + P + R_observer + D_commit + N + R_notifier`, 21.0 s of logical scheduling for the default knobs plus only measured overrun. Each case asserts the bound **and** its decomposition from measured terms, and each protects one clause: the nominal phase, the previous full sweep's own overrun, a starting-row fast-path overrun, a notifier pass in flight at the commit (whose interval starts at its own completion, not at the commit), committed-truth-only reads (a read attempted before the commit and returned after it carries the committed rows in the notifier's own `include_terminated=True` scope), coalesced missed ticks for both loops, a live pass that did not observe the fact being unable to satisfy the stage, and notifier disablement with in-place re-enabling. The oracle documents three relations it deliberately does **not** assert — the telescoping decomposition, the observer phase's maximum, and `bound` as the sum — because each holds in every reachable state; an assertion that cannot fail is not evidence. Unit lane: no HTTP request, no server, no process. |

## 260831-LOCR-L04 Overrun-Accounted Observer-To-Notifier Handoff

`test_serving_notifier_handoff.py` (unit-regression, manifest row `:97`) is the proof half of a
**preservation** requirement. `LOCR-R04@v1` requires zero production change, so the leaf's entire
deliverable is the timing oracle and its evidence envelope and `mcp/src` is byte-unchanged by the change
set; the two support modules that carry the instrument — `_handoff_clock.py` (the deadline-correct
virtual timeline plus `_Gate` and `_Sequence`) and `_serving_handoff.py` (the disposable world and the
oracle's terms) — take no manifest row, by the same rule that keeps this directory's other support
modules out of it.

**What the oracle states.** The serving lifetime owns two independently scheduled loops and neither can
be woken by the other, so the relay is correct only if their cadences compose into a bounded handoff:

```
observer_release = max(previous_full_sweep_start + F,
                       completion of any observer refresh() still holding the shared sweep lock there)
consuming_sweep  = the first lifecycle poll at or after observer_release, at most P later
commit           = the consuming full sweep's own durable catalog commit
next_notifier    = last_notifier_pass_end + N

worst phase      = F + P + R_observer + D_commit + N + R_notifier
```

`R_observer` is the remaining duration, measured at eligibility, of any refresh holding the shared sweep
lock — the previous full sweep **or** a starting-row fast-path pass; `D_commit` is the consuming sweep's
own duration up to its commit; `R_notifier` the remaining duration of a notifier pass already in flight
at that commit. For the default knobs the fixed part is 21.0 s of logical scheduling; everything beyond it
is a measured overrun rather than an allowance, and a case that met the bound by a different
decomposition still fails because the decomposition is asserted, not illustrated.

**Why each case exists.** The nominal phase; the previous full sweep's own overrun, where the sweep is
parked inside its batch after it already read the evidence row unarmed; a starting-row fast-path overrun
with a nonzero commit duration, where the observed latency is exactly the oracle's sum; a notifier pass in
flight at the commit, whose interval starts at its own completion; committed-truth-only reads, where the
read is attempted before the commit and returns after it carrying the committed rows; coalesced missed
ticks for both loops, so three expiring ticks behind a parked pass queue nothing; a negative control in
which rate-limited polls and a live notifier pass exist while the fact is readable and none of them is the
consuming pass; and notifier disablement, where observation keeps sweeping and commits with signal
derivation off, the loop re-parks without running a pass, and in-place re-enabling reaches the
already-committed truth on the next completion-relative pass.

**Two design properties, recorded because a passing run cannot show them.** Case 1's strict
observer-phase assertion (`observer_term < F + overrun`) is a constraint on **that case's arming
scenario** — it arms the fact `P / 2` after the previous sweep's start — and not a claim about production
behaviour; its failing state is the tight arming the other cases use, and the arithmetic identity that
would restate the arming constant has no such state, so it is not asserted. And `assert_oracle` documents
three relations it deliberately does not assert — the telescoping decomposition, the observer phase's
maximum, and `bound` defined as the sum it is compared against — because each holds in every reachable
state, reachable or not; asserting them would add lines that cannot fail rather than evidence.

**The lane-row insertion moved citations, not just a row.** The new module's row sits at `:97`, above
every previously-latest unit-regression row, so every manifest line at or after it shifted by one —
`test_serving_observation_loop.py` `:97` → `:98`, `test_serving_startup_prime.py` `:98` → `:99`, L17's
`test_terminal_observer_health.py` `:122` → `:123`, and every later lane key with them. The 59 live
citations into the manifest were therefore re-derived against the current file rather than carried, and
the dated `## Update History` bullets below record which of them the shipped fixer projected
mechanically.
- 2026-09-18T17:04+02:00 — 260918-TSIP-L4 curator (uncommitted change set on `ar/260918-tsip-l4-ar`, base `0dd04d6a`): this route's governed source changed, so a body section was **added rather than annotated** (`## 260918-TSIP-L4 …`) and every citation into the changed files was re-derived in the same operation. Verification stamps stay at the recorded verification — the candidate is uncommitted and the governed closeout owns the real code commit.
the dated `## KS-R15@v1 Lane Registrations And The Citation Shift`

the dated `## Update History
- 2026-09-21T22:50:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **route body updated for this leaf's case module.** `mcp/tests/test_knowledge_review_evidence_channels.py` joins this route with ten `unit-regression` cases that drive the production dashboard port over a real enclosure and produce every record class through its own owner; the section records the ten properties one case each — including the two per-record damage cases added for independent-verification findings F1/F2 — and the fixture footprint that keeps the evidence catalog's delta at four consumer rows with no registered artifact. Four reference rows and one section were added, and no earlier section was re-worded. **Stamp accounting:** the verification pair is retained as recorded (`d80a0513…` / `2026-09-21T19:51:20+02:00`), which is the production line this reading was against; the candidate row added at the top names the uncommitted candidate and no stamp was invented.
- 2026-09-21T15:35+02:00 — 260921-ICR-L18 curator, **catalog citations re-derived rather than shifted, and this leaf's section merged beside the incoming ones.** The lane-row and consumer-row citations into `mcp/tests/test-evidence-lanes.toml` and `mcp/tests/evidence-lifecycle.toml` that this document carries were uniformly one line low — a base inaccuracy earlier leaves had carried forward by adding a delta instead of re-reading — and every one whose row's own quoted anchor resolves to a single line in the merged candidate was re-pointed to that line. Rows whose anchor is genuinely ambiguous across several lines were left exactly as they were and are reported rather than guessed. This leaf added the `260921-ICR-L18` route section above and advanced no verification stamp: the tuple on this card is the master line's.
- 2026-09-21T15:17:00+02:00 — 260921-ICR-L2 curator, **post-sync re-derivation on this route: the merged candidate added one case and the four R02 cases kept their ranges.** The sync's code-side resolution added `test_a_task_context_review_states_a_damaged_half_and_still_lists_the_source_inventory` (`903-938`) to `mcp/tests/test_knowledge_review_source_endpoints.py` — the property neither leaf could measure alone — and adapted two existing cases inside their own extents, so the section above now states five cases and 938 lines rather than four and 900. The two rows of this document that cite `test_knowledge_review_surface.py` by line were re-pointed (`1161-1210`, `1213-1251`, from the pre-merge `971-1020`, `1023-1061`). Nothing was added to the lane manifest, the artifact catalogue or the contract count by either side of the merge. No verification stamp was advanced.

- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator, **memory-side sync conflict resolved as a UNION; no side dropped.** The memory source branch advanced to `92f444b04` (260915-KS-L45) while this leaf's curation was in flight, so the sync's re-apply conflicted in this file. Both sides were kept because both are true: 260915-KS-L45's landed additions (the Intent-review entry path, the two published half-names `REVIEW_BASELINE_DIRECTORY`/`REVIEW_CANDIDATE_DIRECTORY`, the `missing_dataset_half` pair preflight, the receipt-derived `review_namespace`, and the enumerating reads) and this leaf's 260915-KS-L43 edits (the allocated-identity/derived-citation split, the retry key and its journal, the explicit anchor reuse, and the recovery's journaled decisions with the bounded cycling refusal). Where the two sides carried the same row in different line numbers, the row was re-measured against the moved line rather than picked: L45 curated against `fb719f89` and this leaf's source moves every citation below `:306` of `knowledge_curator_ingest.py` and renumbers `cli/knowledge_ingest.py` entirely, so the surviving ranges are the post-merge measurement for both. One **contradiction** is recorded rather than silently resolved: the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` frontmatter pair is L45's (recorded against the moved line, the newest verification on record), while the candidate reading recorded in the entry is this leaf's reading — two different claims, kept beside each other instead of one overwriting the other. No verification stamp was advanced by this leaf.
- 2026-09-20T06:52+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `f79f4db7`): **route body updated.** `mcp/tests/test_worktree_sync.py` grew the acceptance for the public conflict boundary — `_assert_knowledge_conflict_is_diagnosed_and_reconciled`, `_assert_delete_reference_conflict_is_retracted` and `_assert_schema_disagreement_is_reported_not_reconciled` — driven from the existing retained-conflict integration case, so no collected case was added to a lane that already sits at its exact ceiling. The module now builds one scenario at an older recorded schema generation and therefore consumes the registered `generation_test_support` fixture, whose `consumer_scope = "exact"` required the consumer list in `mcp/tests/evidence-lifecycle.toml` to gain this module **and** `mcp/tests/test_sync_parked_candidate.py` (which imports it), and required the catalog digest pinned in `mcp/tests/test_dependency_ownership_ast_helpers.py` to be re-derived to `c499cbcc…` — the eleventh deliberate re-pin, recorded in that module's own docstring. **Nothing was registered, no artifact row was removed and no identity moved**, so the governed populations stay at fifteen contracts / sixty-five artifacts. A body change, not a metadata-only refresh.

- 2026-09-18T19:23+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **retargeted the eight reference rows this leaf's own module split made wrong, and verified each by reading the new module.** L24's `KS-R24@v1` rows at `:2814-2821` cited the eight publication-input cases in `mcp/tests/test_final_full_memory_coherence_certification.py` at `:1059-1076`, `:1079-1089`, `:1092-1108`, `:1111-1124`, `:1127-1147`, `:1150-1163`, `:1166-1180` and `:1192-1192` — ranges the split left **out of bounds** (the module is 954 lines) and whose anchors now live in `mcp/tests/test_curator_coherence_publication_discoverability.py`. Each row was re-cited to the range its own case occupies there (`:145-162`, `:165-175`, `:178-201`, `:204-217`, `:220-240`, `:243-256`, `:259-273`, `:276-283`), and each new range was **verified to contain that case's own `def` line** before it was written. This is the engine's own prescribed action for `anchor_left_live_file` — re-cite where the fact now lives — that the serving build's pass declined because the old module still exists; it is recorded here rather than left to the reader. No other row was touched: the route's remaining absent-anchor rows are the anchor-**multiplicity** class, which the leaf's own item 16(b) now reports as *report-only* rather than curator work, and the engine's declines for them are carried in the curator's declined worklist.
- 2026-09-18T08:30+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 2 generated projection bullet(s) by hand** — `mcp/tests/test_knowledge_family_composition.py`, `mcp/tests/test_knowledge_family_composition_boundaries.py`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.
- 2026-09-17T11:20+02:00 — 260915-CAPS-L15 curator: the suite gained one module, 14 cases, and this
  card records what it is *for* rather than only that it exists: the acceptance test the master lacked,
  driving both production launch points and reading the capsule from each started session's own first
  prompt, with the expected side being the compiler's own result. A declared section lists the case
  groups — including the production-chain pair that **replaced a deleted hand-supplied case**
  (`L15R-2`'s evidence class) — and states where the live system-block half of the evidence lives
  instead. Five reference rows added. Verification metadata moves to this leaf's base `15fa0e2c`; the
  candidate is deliberately uncommitted, so the governed closeout stamps the real code commit and no
  hash or fingerprint was invented here.
` entries below were left as written because they are as-of records of earlier
candidates. No case budget is quoted or changed here: `pyproject.toml` is the authority, and this leaf
adds no collected case to any capped population.

**Boundaries.** No case edits or imports a production module's internals; every case measures production
through the harness's recordings. The oracle claims the two loops compose within the bound — not the
sweeper's internals beyond its retained ten-second full-sweep limit, not the notifier's internal predicate
set, and not the catalog's on-disk format. Lane membership is classification, not execution or acceptance
evidence, and the verification stamps remain closeout-owned.

## 260831-LOCR-L10 State-Signal Crash And Restart Recovery

`test_state_signal_restart_recovery.py` (unit-regression, manifest row `:101`) is the executor for the
relay's restart idempotency contract that no earlier module forced: for one exact catalog seat plus its
`terminal_evidence_id`, retries and process restarts converge on **one** durable state-signal row and
one emitted marker, in the order row persisted → marker stamped → delivery attempted. Seven cases,
each building one temporary durable world and then re-reading it through brand-new catalog/store/context
objects: a marker write that raises leaves exactly one pending unmarked row, zero adapter submissions
and a restart that renews that same row id before delivering once; the two competing finders' findings
(the generic redelivery finder run over that generation, and the boundary-drain finder) are both fenced
at the shared action with no delivery-state mutation before state-signal recovery stamps and delivers in
the same sweep; a stop after the marker leaves one *marked* pending row that the ordinary pending-row
path lands once; a same-seat rebind between row persistence and marker retry renews and re-addresses the
original row id instead of minting a sibling; two distinct seat ids sharing document, role, outcome and
evidence hold two rows that never renew each other; a later evidence identity re-arms the seat as a
successor row while the older row still delivers; and the non-state preservation control keeps the
structural coalescing key and its occupant-blind behavior. Reverting the three source hardenings turns
six of the seven red, with that preservation control the single pass — the module is sensitive to the
ordering it claims, not to its own scaffolding.

**The fence's reachable route is the boundary drain, not the generic finder.** Case two obtains the
competing findings by calling each finder and acting the finding, because the sweep's *generic*
redelivery path cannot select such a row by construction: `state_signals.state_signal_held_on_boundary`
excludes a non-landed state-signal row whose target seat is alive. The reachable caller is
`evaluate_predicates` → `evaluate_boundary_drain_findings` → `_drain_boundary` → the shared `_redeliver`,
which carries no held-on-boundary filter; the independent baseline review reproduced that route on a
real sweep and observed the skip (`('boundary-drain', 'skipped', 'state-signal source marker not
stamped')`, zero submissions, row untouched) with recovery then stamping and landing the same row. A
future touch of this module would be stronger with that real-sweep drain-fence assertion recorded as a
case; it is not authorized scope for this leaf. Case inventory, helpers and the contract narrative live
on `test_state_signal_restart_recovery.py.md`.

| Terminal catalog reads are side-effect free | `test_serving_terminal_catalog_read.py` | The real registered `GET /api/terminal/sessions` route driven over `fastapi.testclient.TestClient` and the real composed `create_app`: one hundred requests produce one hundred equivalent answers with every ledger at zero; probe, cursor advance, row mutation and compaction each fail on their **own** instrument rather than as one aggregate; the no-adapter-probing clause is pinned at the readers themselves, by name **and** by object identity, so a route-side read bound through a module-level `import … as` alias is counted too; a catalog change between two reads is attributable to the background observer, and an observer that has failed still serves the stored snapshot instead of being repaired by the request; and path, declared model, conditional-key behaviour and status semantics are unchanged through the composed app. Integration lane, one new module, no production route behaviour beyond removing the handler's sweep. Two limits are recorded rather than papered over: a reader reached through anything that is not a module global (a function default, closure cell, class attribute, dict entry or instance attribute) stays outside the reader ledger, and the 100-GET case is content-vacuous on its own, so content is pinned by the composed-app and failed-observer cases. |

## 260831-LOCR-L07 Curator Turn Owner Wake

`test_state_signal_curator_wake.py` (unit-regression, manifest row `:102`) is the executor for the
curator half of the terminal-turn wake: a curator's durable output is its structured coherence
authority rather than a chat message, so the curator must not have to hand-author a completion post
for its manager to resume. The module starts where production starts — the adapter's own evidence
frames — and lets the real `TerminalCatalogLivenessSweeper` derive the catalog turn truth before the
real agent-notifier sweep relays it, so no row in any scenario is written with a turn claim, a
terminal outcome or an evidence identity, no terminal-session GET is issued, and no curator-authored
completion row exists. Five cases: a `completed` ending wakes the **current** manager of the
curator's own master with exactly one durable signal carrying the curator role, the subject leaf
document, the outcome and the evidence identity, and re-observing that same terminal evidence mints
no second signal and no second row; an `interrupted` ending carries interruption truth
(`outcome interrupted`, `interrupted_by=developer`) and is re-emission-guarded on that path exactly
as the completed one is; `failed` is the negative control that keeps the two-outcome boundary honest
from the outside — the seat does reach terminal truth, and the relay still emits nothing, leaving the
seat eligible so a later canonical outcome can still wake; a completed ending appends no verdict —
the payload equals the canonical `state_signal_ask` / `state_signal_response` derivation, contains
none of the acceptance vocabulary, and the coordination root read **after** the sweep is the same
population as the premise, so a relay that wrote its own coherence or readiness artifact would show
up there and nowhere else; and a curator seat whose own master has no current manager fails closed
instead of routing to a live other-master manager, with the seat left eligible rather than consumed.

Two things are deliberately *not* claimed. The wake is terminal-truth relay only: it neither
validates nor declares curator coherence, memory readiness or closeout acceptance — the manager opens
and validates the canonical curator authority itself, and `accepted` is a transport fact here rather
than a verdict about the curator's memory. And the stale spawn-ancestry address registered on the
curator row is never selected: routing resolves the owner from the task hierarchy, so the cases
assert the manager the topology names rather than the session the seat was spawned from. Case
inventory, helpers and the fixture contract live on `test_state_signal_curator_wake.py.md`.

## Evidence

### 260915-KS-L12 Two Supporting-Record Case Modules, And A Shared Fixture That Is Registered Evidence

`KS-R12@v1` adds two case modules to the `unit-regression` lane — `test_knowledge_evidence_claims.py`
and `test_knowledge_evidence_observations.py`, twenty cases each, both carrying
`pytestmark = pytest.mark.evidence_unit` — and one **shared support module**,
`evidence_test_support.py`, that both build on. The cases cover the claim contract and the observation
contract in the order the requirement states their clauses: the typed aggregates under the shipped
envelope, the structural subject and coverage kinds, the resolved links and their five endpoint kinds, the
required limitations field served visibly, the opaque assessment references, the verbatim command identity,
the artifact digest measured against real bytes, the closed five-member execution result, the run
environment, the generation gate in both directions, and the read projections that report facts and no
verdict.

**The support module is registered evidence, not an unregistered helper.** It is
`contract:knowledge-evidence-cases` with an owning contract row and a `shared-support` artifact row in
`mcp/tests/evidence-lifecycle.toml` — authority `internal-canonical`, category `unit-regression`, fidelity
`in-process`, cadence `affected`, `introduced_by = "260915-KS-L12"`, lifetime `permanent`, and
`consumer_scope = "exact"` naming exactly its two consuming modules. Its executable evidence node is
`test_knowledge_evidence_claims.py::test_a_claim_reads_back_with_every_field_including_an_empty_limitations`.
Its permanence rationale is the reason it is shared rather than copied: an evidence claim resolves four
links across two subject kinds and two coverage kinds, so a per-module copy of that topology would let the
two modules disagree about which identity is the facet revision and which is the invariant revision, which
is exactly the property the refusal cases assert. The fixture holds **real bytes** under a temporary root,
because a digest checked against bytes at write time is only meaningful against real bytes.

The route's file-size rail bit here as it has elsewhere: the shared refusal module sat four lines from the
1200-line limit, so this leaf's three refusal factories live in `evidence_refusals.py` beside their own
record group rather than in the shared module — whose own diff is empty.

### 260915-CAPS-L7 The Eve Capsule/Workspace Binding Evidence

This route gained three modules proving the eve capsule/workspace binding seam, split by what each can
actually observe:

- `eve_capsule_test_support.py` — **shared support, not a test module.** It builds a real git repository
  with real `git worktree` checkouts, a real coordination root with a sprint/master/leaf document and an
  enclosure contract, and an authored composition corpus. It is the reason the route's other two modules
  can compare against something the code under test does not feed: the workspace identity is compared
  against `git` itself, the carrier digest is recomputed from disk, the task facts against the fixture's
  own task document. Its frozen role/operation vocabularies are deliberately **spelled rather than
  imported** — a fixture that imported what the compiler enforces could not disagree with it.
- `test_eve_capsule_binding.py` — **unit-regression.** The Python half. Most of its cases assert a
  **named refusal** rather than merely that something raised, because an over-strict verifier that
  refused everything would otherwise pass the whole refusal group.
- `test_eve_capsule_runtime.py` — **integration.** The TypeScript half, which no Python case can observe:
  it executes the **shipped** `eve_runtime/agent/lib/*.ts` under the same Node a launch would pick, with
  a `node:module` loader hook supplying only the eve compiler's `./x.js`-for-`.ts` specifier convention.
  Carrier and launch defects are declared as **data** carrying the exact refusal code they must produce.

Two fixture changes in this route belong to the same seam and are recorded here rather than only in the
individual cards. `eve_adapter_test_support.py` gained `fixture_launch_binding()`, because the launch
path is production even when the transport is a double: it now verifies the carrier and the admitted
worktree before a process would exist, so `test_eve_adapter.py`'s launches take their `cwd` and
environment from a real worktree, commit and carrier instead of hand-written values. And
`eve_fixture_model.py`'s trace gained a **`messages`** key carrying the provider's own view of the
request — the only place the *effective prompt* is observable, which is what makes the live fixture's
"the binding reaches the model" assertion a measurement instead of a restatement.

Whole-seam boundary a reader of this route should carry: the live end-to-end claim is
`live_eve_native_fixture.py`'s two capsule scenarios, which drive the real pinned eve runtime. The
produce side they exercise still has **no production caller**, and wiring one is `CAPS-R15@v1`'s
obligation under an explicit transfer.

- The shared fixture world the seam's cases are built on, and the one place the produce side is currently called. [226]
- The Python half, whose refusal cases assert a named defect. [227]
- The TypeScript half, executing the shipped modules under a real Node. [228]
- The launch-binding fixture that makes the adapter suite's launches verifiable. [229]
- The trace's effective-prompt key, which the live capsule scenarios assert against. [230]
- The live end-to-end capsule scenarios, which are the whole-seam proof rather than a unit claim. [231]
- The lifecycle catalog registration for the shared support module, with its four derived consumers. [232]
- The lifecycle catalog registration for the shared support module, with its four derived consumers. [233]
- The lifecycle catalog registration for the shared support module, with its four derived consumers. [234]
- The lifecycle catalog registration for the shared support module, with its four derived consumers. [235]

### Repo-Internal References

These current source and policy ranges establish the development/certification distinction and the
existing memory preparation surfaces. A citation is source evidence, not a recorded test execution.

- Development commands, budgets, diagnostic metrics and isolation. [236]
- Certifying publication and accepting consumers. [237]
- Exact contract scope, full check and curator worklist publication. [238]
- Interactive catalog names missing authority without eligibility. [239]
- Final memory adapter requires the selected four-code-terminal prefix. [240]
- Finalization consumes original selected fifth-certificate inputs. [241]
- The citation index's exclusion register, its ruled caps and its reported-skip behaviour, defended case by case. [242]
- The divergence between the register's re-inclusion rule and Git's, measured on both sides. [243]
- The consumer of record for the three new `scripts/e2e_harness` governed artifacts, and the fixture/scenario shape it pins. [244]
- The lane rows that admit both L14 modules to the `unit-regression` lane. [245]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [246]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [247]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [248]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [249]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [250]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [251]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [252]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [253]
- The lane rows that admit both L14 modules to the `unit-regression` lane. [254]
- The live public-surface inventory contract for the advertised MCP tool tuple. [255]
- The advertised roster the inventory comparison uses, in its new zero-import `models` leaf. [256]
- The worktree surface's declared next move and the membership validator this route's new module pins. [257]
- The worktree surface's declared next move and the membership validator this route's new module pins (second citation of the same pair, from the post-L32 section). [258]
- The L32 module itself: archive-ready reachability for both cleanup verbs, the declarations, and the validator in both directions. [259]
- The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane. [260]
- The contract-scoped activation record: one record per series contract, keyed by the contract fingerprint rather than a source pair. [261]
- The L36 cross-master forcing module: both masters stay ready, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks nobody, a conflicting or stale publication is refused at the pair, and a master that reconciles with a landed sibling completes through ordinary closeout and final integration. [262]
- The L36 lane registration the fail-closed manifest requires. [263]
- The L37 stop boundary proof: the public pause, the measured world, the ten independently-failing cases and the four refusal shapes. Its never-selected case asserts the already-vacant success rather than a refusal, and the two L38 cases added after it pin the unreadable record and the vacant foreign record. [264]
- The L37 structural half: the pause's import closure is disjoint from every publication module. [265]
- The L37 lane registrations the fail-closed manifest requires, one per new module, re-derived at this candidate: the pause suite's row at `:253` and the publication guard's row at `:294`. Both moved with this master's three registry insertions at `:120`, `:201` and `:267`; the two ranges below are the rows those lines actually carry. [266]
- The ordered lifecycle playthrough that is the regression proof for the deleted atomic-series child-admission seal: master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf commanded after the landing still starts. [267]
- The lane registration the fail-closed manifest requires for that module. [268]
- The L4 census module's lane row, which closed the gap the L4 route section recorded. [269]
- The L5 binding module's lane registration, added by the same change set that created it. [270]
- The L23 registration-order proof: the observed chain with the terminated-row read carrying its own batch-commit state, the partial-proof singleton, the raising registrar that stops the pass, the restart that re-registers and loses nothing, and the fast-path exclusion measured in both directions. [271]
- The L23 lane registration the fail-closed manifest requires, inserted between two alphabetically adjacent rows so no other entry moved. [272]
- The L27 pane-authority proof, its fixture import from the sibling sweeper suite, and the lane registration the fail-closed manifest requires. [273]
- The shared fixtures the L27 module imports instead of rebuilding. [274]
- **260913-LCA-L8:** the new module's lane registration, added by the same change set that created it — integration, because it drives the public landing, integration and finalization routes over real temporary repositories and worktrees. [275]
- **260913-LCA-L8:** the L6 shape finalizes on the first call, a real permission failure blocks with its own reason and refuses identically on retry, and the two invariant owners are driven directly. [276]
- **260913-LCA-L8:** the only construction path for a terminal blockage, and the operator-language answer for a reasonless or malformed result item. [277]
- **260913-LCA-L8:** the producer whose result could answer `removed: False` with no reason, now naming every non-removal. [278]
- **260913-LCA-L8:** the nine exact-consumer rows the new module's change set adds to the evidence registry. [279]
- **260913-LCA-L8:** the declaration that gives the new module ownership of the ambient-role runner for targeted selection. [280]
- The removed case's scenario, now refused by design: the guard that makes a task root with no master document unbindable. [281]
- The L36 cross-master forcing module: both masters stay ready, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks nobody, a conflicting or stale publication is refused at the pair, and a master that reconciles with a landed sibling completes through ordinary closeout and final integration. Anchor N is the node whose span is range N. [282]
- The L37 stop boundary proof: the public pause, the measured world, the eight independently-failing cases and the refusals. Its never-selected case now asserts the already-vacant success rather than a refusal. [283]
- The lane registration the fail-closed manifest requires for that module (row 165 after the KS-L2 and KS-L3 insertions). [284]
- The architecture-fitness lane registration the fail-closed manifest requires for that proof. [285]
- The L27 pane-authority proof, its fixture import from the sibling sweeper suite, and the lane registration the fail-closed manifest requires. [286]
- The shared fixtures the L27 module imports instead of rebuilding. [287]
- **260913-LCA-L8:** the exact-consumer rows `mcp/tests/test_terminal_blocker_reasons.py` adds to the evidence registry under the `synthetic-test-evidence-candidate` contract, one per artifact whose consumer list gained it. [288]
- The refusal the two corrected closeout fixtures had to satisfy. [289]
- **The mid-flight reporting boundary:** a completed pass beside a reconciling selection is not this call's success, and a refusal left beside one leads with the mid-flight state. [290]
- The rewritten contract-scoped activation forcing suite and its shared-source-pair fixture. [291]
- The registered admission refusal now addresses only the addressed contract's own state. [292]
- **Row corrected against the current source (L2 curator, 260915-KS-L2):** the L2 mid-cycle *test node* this row cited, `test_a_code_tip_with_no_attributing_memory_commit_refuses_by_name`, **no longer exists in the suite** — a source-wide search finds no such node and no fragment of its name, so the documented coverage is stale and this row no longer claims it. What survives and is cited here is the helper the row also named. A successor that wants to re-establish the refusal-by-name coverage must write the node and re-cite it; a plausible-looking range was deliberately not substituted. [293]

Current working-candidate evidence for this route:

- Public closeout exercises the actual pair, attribution and cache-independent delivery. [294]
- Cache damage cannot change the accepted integration pair or block ref publication. [295]
- The migration acceptance proof reads only committed trailers. [296]
- Cache damage cannot change the accepted integration pair or block ref publication. [297]
- The migration acceptance proof reads only committed trailers. [298]

### Docs And Cross-Repo References

No Domain Documentation entries are configured in the resolved memory root. Current local policy and source owners are cited above; no live external system or sibling repository is used to grant authority.

## Fixture Roles And Claims

`test_agent_notifier.py` and `test_agent_notifier_ladder.py` supply row/topology builders. `test_codex_app_server_adapter.py` and `test_codex_adapter_thread_demux.py` supply transport/observation helpers. `test_closeout_queue.py`, `test_closeout_projection_member_helpers.py`, `test_final_codex_models.py`, `test_gate_certification_evidence.py`, `test_memory_citation_fix.py` and `test_observer_projection.py` likewise retain shared setup rather than their former standalone matrices.

**The citation fixtures now build real Git provenance (260831-LOCR-L33).** The continuity rule the
leaf introduced — a tree-wide relocation is admitted only when no cited file survives and the anchor
existed in a cited file at the document's `lastVerifiedCommitHash` with the same extent kind — is
only expressible against a real repository, so `test_memory_citation_fix.py`'s shared `Tree` gained
`history()`, `stamp()` and `remove_source()`, and its `document()`/`card()` accept a `stamp` that
lands a `lastVerifiedCommitHash` row **inside** the metadata table (never below the citation header,
where it would parse as another claim). `Tree.row()` locates a citation row by its table header
rather than a fixed index, so card metadata cannot shift it. `test_citation_document_transaction.py`'s
`Scenario` carries the same stamp and its fixture commits the verified tree before deleting both
cited files; the TypeScript move fixtures in `test_memory_citation_grammars.py` and the
`_two_failing_cards` helper in `test_memory_citation_fix_scopes.py` were given provenance the same
way. The previously pinned relocation tests therefore still test the legitimate kind-preserving move
instead of having their expectations relaxed, and `test_memory_citation_resolution.py` adds
`MechanicallyProjectedRangeTests`, which pins that a range written by the mechanical projection is
surfaced with the support question rather than an assertion that the citation is current.

Preserve useful shared fixtures only for real consumers. Fake inspectors, synthetic profile inputs, hand-built report payloads and pending finalizers must stay labeled as such. A source-range citation proves the described assertion exists; only a retained execution record proves it ran. Whole-master review and aggregation must assess actual protection rather than historical test names or counts.

## Isolation And Collection

Root test conftest sets candidate imports and disposable home/config/data/cache paths, removes inherited credentials and live-provider opt-ins, and restores owned global state. Ordinary units do not automatically bootstrap application composition; tests request `worktree_services` when that boundary matters. Integration-only modules are skipped before import during unit runs. Collection budgets inspect already selected items without nested pytest or a second repository scan.

## Deliberate Test Inventory Reduction

The test route was reduced on purpose, and a card that cites a name which no longer exists is
evidence of that reduction, not evidence of a lost or damaged file. Commit `d3610903` ("Reduce test
inventory and make coverage diagnostic", 2026-09-06) is the large one: 594 files changed, 604
insertions against 235,366 deletions, stating that it reduced Python test/support code by 79% and
that it replaced coverage floors with collected-case budgets. Four later cuts removed specific
named surface as well: `173bb01e` (2026-09-10) deleted the detached lifecycle worker and drove every
fixture onto the synchronous path; `b06b3a27` (2026-09-10) removed the master route-review gate that
integration never consulted, under an explicit developer ruling that quality is checked focused
within the leaves; `6982c6a7` (2026-09-10) cut the door-operation-journal plane and deleted the
`closeout_door` tool entry point; and `2ec5d244` (2026-09-11) deleted the tests its own remaining
failures exposed as dead. Recover a deletion's cause with `git log -S '<symbol>' -- mcp/tests` (or
`git log --diff-filter=D -- mcp/tests`) before treating a missing test name as an accident. A
shrinking coverage table therefore belongs in the card as recorded negative knowledge, with the
removing commit where it can be proven, and never as a silently shorter list.

## Historical Context

The original milestone narratives documented substantially larger cohorts. Their counts, deleted symbols, source-pinning assertions and percentage-driven repair obligations are retired as current guidance. Relevant incident reasoning survives in the retained cards and source comments. The preserved history below records what earlier waves did without instructing future agents to reconstruct those waves.

## Development And Certification Policy

Ordinary Python development is supported directly through `mcp/.venv/bin/python -m pytest`; four workers run the isolated unit population. `-m integration` selects the small real-boundary population and `-m ""` selects both. Focused file/node execution, including serial debugging, is valid development work and does not acquire certification authority. **The budgets are declared once, in the repository-root `pyproject.toml` under `[tool.pytest.ini_options]` — `unit_case_budget` = 4000 at `:278` and `integration_case_budget` = 1000 at `:279` when this was read — and `mcp/tests/conftest.py` carries no number of its own**: it registers the two ini names with `addini` and no `default=`, because `mcp/pyproject.toml` declares no `[tool.pytest.ini_options]` and the root file is the `inifile` pytest reads. Read the pair from there; it moves, and the dated tradeoff comment above it records every raise. The 150/200/250/400/600 integration ceilings and the 1000/1100/1250/1500/2300/3000 unit ceilings named below are the dated readings of the leaves that raised them, kept as as-of records — none is the current rail. Extend or consolidate distinct behavior protection before adding cases; do not restore deleted matrices, private-branch tests or unused fixture machinery because an old milestone names them.

Coverage, including changed-line coverage, is diagnostic only. No percentage floor requires additional tests. Production-only CRAP retains 20 as a review trigger, not a delivery blocker; tests and verification support are excluded. Lint, formatting, typing, structural rules and test failures still enforce. Diagnostic-tool execution errors remain visible failures distinct from metric findings. There is no coverage baseline, score-exception registry or ratchet.

Only genuine Dagger admission and the existing lifecycle owners can issue immutable candidate-bound certifying evidence. A host pytest pass, copied report, green helper result or use of Dagger alone is insufficient. Reuse the existing shared engine and preserve process identity, disposable state, credential isolation, exact candidate and publication ownership. Full-suite execution and whole-master independent review belong to the master aggregation boundary under the current execution policy; this overview does not impose either on every leaf. Focused development evidence remains useful without pretending to be final acceptance.

## Memory Preparation And Final Certification

Memory quality is useful before gate admission: a contract-scoped full request observes the exact code/memory pair and candidate trees, runs quality checks, and builds an enclosure-local curator worklist covering repair findings, commit-owned findings, missing onboarding, stale route indexes and source drift. Use that worklist to perform the authorized semantic onboarding updates before entering the expensive certification sequence. It is not necessary to obtain code-gate certificates merely to discover the memory work.

Preparation does not grant a final certificate. The interactive catalog projection explicitly lacks affected-closure and code-prefix authority. The existing prepared-memory adapter consumes the selected four original code terminals and exact prepared candidate, runs the final memory producer, publishes its physical result and selects Gate 5 through the normal owner. Finalization requires that selected original fifth certificate and its bound memory inputs. MCAR continues from these existing owners; this overview does not declare the unfinished master accepted or create a second final proof path.

Candidate capture uses an isolated add-all index and stable observed HEAD, leaving the user's real index unchanged. External-memory identity binds configured repositories, worktree roots, branches, bases, onboarding root and contract digest; the cache path is informational. A changed pair or candidate must refuse stale publication. Metadata stamping and cache refresh cannot substitute for substantive memory repair.

The frozen L38 candidate added two registered integration checks to the retained population; the two L38 integration cards above describe admission/status projection and route-review transport. The current manifest records 224 test-shaped modules: 130 unit-regression, 2 public-contract, 62 integration, 17 architecture-fitness and 13 provider-conformance, with stress-durability and migration empty (the landed master added 260831-LOCR-L06's `test_lifecycle_owned_completion_relay_reviewer.py` to unit-regression at entry row 68 and this leaf adds `test_serving_notifier_handoff.py` to that lane at entry row 98, so both insertions moved every later manifest line; 260831-LOCR-L17 had added `test_terminal_observer_health.py` to that lane at entry row 122, now row 124) (260831-LOCR-L32 added one integration member — `test_worktree_status_terminal_next_tool.py` — 260831-LOCR-L34 added `test_checkpoint_landing_end_to_end.py`, 260831-LOCR-L36 added `test_cross_master_concurrency.py`, 260831-LOCR-L37 added two: `test_pause_stop_only_end_to_end.py` to integration and `test_pause_is_not_publication.py` to architecture-fitness, and the 260831-LOCR seal-removal change set added `test_lifecycle_playthrough_end_to_end.py` to integration; the declared collected-case budgets are 1,100 unit and 300 integration, the integration ceiling having been raised from 200 by L37 and to 300 by L24 with the explicit tradeoff block in `pyproject.toml`). That population was repaired, not merely recounted. The authorized repair restored three CCR landing-debt registrations that commit `8885939e` created but omitted from this manifest (`test_review_state.py`, `test_task_doc_review_public.py` and `test_transaction_only_worktree_delivery.py`), all three in `unit-regression`: those modules previously ran unmarked, and the integration lane sits at its 200-collected-case cap, so an `integration` row for them pushed full-suite collection past the cap and failed collection. The same cap reason moved this route's own `test_terminal_liveness_deferred_work.py` row from integration to `unit-regression`; the module is hermetic. The remaining new unit-regression row is the parked-external-await separation guard in the route table above. Every restored module already had its file card. Membership remains selection and cost classification only; it is not execution or acceptance evidence, and it does not restore any retired matrix.

**Superseded counts (260913-LCA-L5 curator, measured at the current change set):** the sentence above records the
pre-L4 population. The manifest now holds 204 modules on disk and 204 entries — 115 unit-regression,
2 public-contract, 58 integration, 16 architecture-fitness, 13 provider-conformance, with
stress-durability and migration empty — the growth being L4's `test_memory_attribution_producers.py`
(row 68, unit-regression) and L5's `test_leaf_doc_master_link_binding.py` (row 152, integration). The
`test-evidence-lanes.toml` card carries the per-lane brackets and is the owner of record.d it does not restore any retired matrix.

**Current counts (260913-LCA-L7 curator, measured at the current change set):** the L5 paragraph
above is superseded. The manifest now holds 205 modules on disk and 205 entries — 115
unit-regression (entry rows 5-120), 2 public-contract (122-124), 59 integration (126-185), 16
architecture-fitness (187-203), 13 provider-conformance (205-218), with stress-durability and
migration empty. The single addition is this leaf's `test_closeout_projection_source_classification.py`,
registered in the **integration** lane at row 137 by the same change set that created it: it composes
the real `QueueFixture` over temporary Git repositories and drives the production graph admission and
projection path, so that is its behaviour-preserving lane. The `test-evidence-lanes.toml` card owns the
per-lane brackets; membership is selection and cost classification only, never execution or
acceptance evidence.

**Current counts (260913-LCA-L8 curator, measured at the current change set):** the L7 paragraph
above is superseded. The manifest now holds 206 modules on disk and 206 entries — 115 unit-regression
(entry rows 5-120), 2 public-contract (122-124), 60 integration (126-186), 16 architecture-fitness
(188-204), 13 provider-conformance (206-219), with stress-durability and migration empty. The single
addition is this leaf's `test_terminal_blocker_reasons.py`, registered in the **integration** lane at
entry row 177 by the same change set that created it: it drives the public landing, integration and
`lifecycle_finalize_task` routes over real temporary repositories and worktrees, so that is its
behaviour-preserving lane. The `test-evidence-lanes.toml` card owns the per-lane brackets;
membership is selection and cost classification only, never execution or acceptance evidence.

**Current counts (260831-LOCR-L23 curator, measured at the current change set):** the L8 paragraph
above is superseded. The manifest now holds 208 modules on disk and 208 entries — 117 unit-regression
(entry rows 5-122), 2 public-contract (123-126), 60 integration (127-188), 16 architecture-fitness
(189-206), 13 provider-conformance (207-221), with stress-durability (222-223) and migration (224-225)
empty. The single addition is this leaf's `test_terminal_liveness_registration_order.py`, registered in
the **unit-regression** lane at entry row 118 by the same change set that created it: it drives the
real `TerminalCatalog` over `tempfile` catalogs and the real
`TerminalCatalogLivenessSweeper.refresh` with in-process registrar/compactor doubles and no
`worktree_services`, so it is hermetic and the default unit lane is its behaviour-preserving
classification — the same lane as the sibling `test_terminal_liveness_deferred_work.py` at row 117. The
insertion sits between two alphabetically adjacent rows, so it moved no other entry. The
`test-evidence-lanes.toml` card owns the per-lane brackets; membership is selection and cost
classification only, never execution or acceptance evidence.

260831-LOCR-L30 registered eight more members and, in doing so, repaired a manifest that could not
load. `load_lane_manifest` is fail-closed — it derives the repository's actual test modules and
refuses a manifest that omits one — so the seven tracked modules that declared no lane (one of them,
`test_record_landing.py`, shipped by the immediately preceding leaf) were a hard load failure rather
than a silent default. The leaf's own `test_checkpoint_landing.py` joined them. Detail lives in the
`test-evidence-lanes.toml` card, which is the owner of record for lane membership.

The same leaf's follow-up added three more forcing cases, one per behaviour the checkpoint state had
to teach, and this route gained two new file cards with them:

- `test_post_integration_cleanup_guidance.py::test_a_checkpointed_series_keeps_working_instead_of_being_told_to_integrate`
  — a checkpointed contract projects `worktree-started` + `continue_work` + `worktree_status`, not
  `integration-pending` + `worktree_integrate` (the tool that refuses while the series is open).
- `test_record_landing.py::RecordLandingTests::test_a_checkpointed_series_is_not_upgraded_into_a_reclaimable_integration`
  — the pull-request route reports `already-recorded` for a checkpointed contract and leaves both cells
  as the checkpoint wrote them.
- `test_closeout_kept_rules_pins.py::test_r3_closeout_accepts_the_source_head_a_checkpoint_landed`
  — the ancestry validator accepts the commit a checkpoint recorded as its own landed head, with
  `test_r3_closeout_refuses_when_the_source_branch_moved` still refusing foreign movement.

The latter two modules had no file card before this pass and are now covered
(`test_post_integration_cleanup_guidance.py.md`, `test_closeout_kept_rules_pins.py.md`). All three
cases were proven non-vacuous by temporary production mutation, which is why each is documented as the
assertion set that failed without its fix. Lane membership is unchanged: all three files were already
registered, so no manifest row moved.
The current evidence-lifecycle registry declares both registered consumers in each shared
closeout-input and curator-coherence support row. Registry SHA
`15bea1c01f402c382dad1667dec601313bb8aabfc511bb8cedac66076287606a1` and validator PASS42 are
source/diagnostic evidence only; they do not establish execution or acceptance.

## Public-Surface Inventory Contract

`test_tools.py::PublicSurfaceInventoryTests` (260831-LOCR-L29) is the executor of a
surface-agreement invariant that had none. `server_info` reports `PUBLIC_TOOLS` itself, so the
comparison it made possible was self-referential; `worktree_record_landing` shipped registered by
`mcp/registration/closeout.py`, advertised by FastMCP, and absent from both `PUBLIC_TOOLS` and
`TOOL_RESPONSE_MODELS`, and every existing case stayed green while the tool could not return a
payload.

The two cases register `TOOL_REGISTRARS` against a probe `FastMCP("inventory-probe")` and compare
the live `asyncio.run(server.list_tools())` order to `PUBLIC_TOOLS`, then drive one
`finalize_tool_response("worktree_record_landing", ...)` call so a missing registry row fails here
rather than at a caller. `_permissive_registration_config()` only has to satisfy registrars that
close over the config without reading it during registration, so these cases stay about the
inventory rather than about building a runtime; the probe is hermetic and reaches no network.

`test_worktree_status_terminal_next_tool.py` (260831-LOCR-L32) is the same shape of executor one layer
down: the *advertised vocabulary of one surface* had no enforcement. `PUBLIC_TOOLS` moved from
`mcp/tools/base.py` to the zero-import `models` leaf `models/tools/public_roster.py`
cit:([`PUBLIC_TOOLS`], mcp/src/agents_remember/models/tools/public_roster.py:22-97) so that
`models/worktree.py::WorktreeCommandResponse` could read it, declare `nextAction` / `nextTool` /
`nextArgs`
cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-405), and refuse a `nextTool` outside the roster
(`_require_registered_public_next_tool`
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442)). Before that the envelope was `extra="allow"` and
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442)). Before that the envelope was `extra="allow"` and
cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-405), and refuse a `nextTool` outside the roster
declared none of the keys, so `application/worktree_status.py::_project_terminal_contract_status`'s
write crossed the wire verbatim and unchecked. The suite reaches the real `terminal-archive-ready`
state for both `worktree_cleanup` and `worktree_abandon`, binds the emitted args against the real
builder signature, and pins the validator in both directions — including that the registered but
non-public `session_retire` is refused on the worktree surface while the `task_doc` surface still
accepts it. That branch had **zero** coverage before this module.

## Historical milestone context: Checkpoint Landing Plan/Apply Parity

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

`test_checkpoint_landing_end_to_end.py` (260831-LOCR-L34) is the boundary executor for the rule the
leaf is really about: **a preview that plans an operation does not enforce it, and the two surfaces
must be maintained as one.** The seam-level checkpoint suite proved each gate in isolation; this
module drives the registered public operations over one real temporary Git world per case and asserts
that the pair agrees.

It is deliberately not a duplicate of the seam suite:

- it starts from the state the deadlock made unreachable — a master whose `closeout_status` is still
  `not-started`, asserted rather than fabricated — and verifies both destination refs and the ledger
  mapping after a successful checkpoint, so the route is proven reachable end to end rather than only
  eligible;
- it exercises refusal parity by iterating `(dry_run=True, dry_run=False)` for each divergent ledger
  and asserting the same refusal text and the same unmoved refs on both surfaces, which is what
  catches a preview and an apply implemented separately;
- it drives the **public** `worktree_checkpoint_landing_tool` and the public closeout preview/apply
  tools, because the original defect lived in the tool surface a caller actually reaches.

The invariant, its full instance inventory (five fixed, two reported-not-fixed, one adjacent
verdict/state-string shape) and the reasons for each disposition are recorded on the
`worktrees/overview.md` route and summarized in `memory_quality/overview.md`. The module also carries
the only recorded `UNREPRODUCED FLAKE` of this leaf — seen once on a mutated build, never on the real
tree — documented on its own card.

## Historical milestone context: 260913-LCA-L2 Ledger Attribution Coverage

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

The ledger's source became the memory commits' own `Code-Commit:` attribution, and this route carries
the proof for both halves of that sentence.

`test_memory_ledger.py` grew a second fixture world and ten cases. `_AttributedWorld` builds a line
where each mapping is two commits — the content commit carrying the trailer and the ledger commit
pinning the row into `memory.md` and carrying none — with one code commit attributed twice (the
superseding pair the ledger keeps both copies of) and one memory commit carrying no trailer. The
closed-loop case asserts the projection equals the rows the tracked table carried at **every**
checkpoint of that line; the hand-edit case writes a row into the table under a matching header and
asserts the projection does not move; the remaining cases cover the pre-trailer blob fallback, the
bootstrap source that contributes no rows, `exclude` selecting a branch's own commits, the
last-block-wins parse that ignores a body mention, the trailer naming a commit the code repository
lacks, a multi-trailer final block read by key, a mapping that arrived through a merge, and the round
trip that proves the writer's key and the reader's key are one key. The six pre-existing projection
cases in the same file still hold because they reach the reader through the per-commit blob fallback,
which is why that fallback cannot be removed without losing their rows.

**The literal `Code-Commit` text in these test modules is a deliberate independent oracle.** A case
that read `CODE_COMMIT_TRAILER_KEY` would follow a wrong constant instead of catching it, so the
trailer-parse and trailer-round-trip cases spell the key out and must not be "corrected" to import the
constant. The one case that does touch the constant —
`test_the_rendered_trailer_is_the_one_the_reader_parses` — uses it to prove the *writer* renders the
key the reader parses, and proves it through a real commit rather than by comparing two literals.

`test_worktree_sync.py` gained the suite's first coverage of the mid-cycle refusal: a code tip the
official memory line does not map returns `blocked` with `official line is mid-cycle`, leaves the work
branch at its pre-sync head, and syncs once the pair is completed. That refusal is produced by the
**named-ref** ledger read in `sync_transaction_authority.preflight_official_pair`, not by the
projected source ledger, so the case is the regression guard that this leaf's reader change left the
detection where it was.

## Historical milestone context: 260913-LCA-L4 Producer Census And The One Renderer

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

`test_memory_attribution_producers.py` is the leaf's new module and the census that makes the trailer
transition total. A memory commit with no `Code-Commit:` trailer contributes no ledger row, and the
projected ledger cannot tell that apart from a producer that kept the old shape, so the surface is either
complete or silently holey. The module holds five cases: a one-definition census (the key identifier and
its interpolation appear in exactly one production module, and no module spells the trailer as a quoted
literal), a producer census (five producers, each asserted to reach a shared renderer entry), a dialect
case (a hostile multi-paragraph body survives byte for byte with the trailer as its own final block), and
two end-to-end cases driving the public `memory_carryover_apply` and `memory_baseline_adopt` on real
disposable repositories.

The census is measured at base `5bb124d4` and **corrects** the master's 2026-09-13T22:05 decision in two
places: `worktrees/queue/closeout_recovery.py:209` is the recovery route's CODE leg, not a producer, and
the producer the first census missed is `preparation/memory_output.py:92`. The corrected result is 5
memory-content producers and 0 untrailered — `closeout_external.py:165`,
`direct_landing_execution.py:270`, `preparation/memory_output.py:92` (memory-content leg only),
`carryover.py:846`, `baseline.py:210` — with every trailerless site carrying a recorded reason: each
ledger leg, `closeout_recovery.py:209` as a code commit, `sync_transaction_git.py:304`/`:333` memory merge
commits (two memory parents, no single code commit to name), and carryover's nothing-to-carry path, which
creates no commit.

Two durable rules the module enforces from source: the trailer key is declared once and must never be
spelled as a quoted literal in a second production module, and the trailer is **appended as its own final
block** rather than woven into the caller's body — because carryover and baseline take that body as a
public argument of another tool and a caller may pass a multi-paragraph message whose last paragraph is
itself `Key: value` lines.

`test_transaction_only_worktree_delivery.py` gained the behavioural half for the route that has no memory
commit site of its own: `test_closeout_recovery_attributes_the_memory_commit_it_still_owed` interrupts a
real public closeout after its code commit, resumes it through the journalled recovery cell (a wrong cell
is asserted to refuse first), and reads both documented git readers against the resumed shas. The leaf
also moved one import in `test_memory_ledger.py` — `CODE_COMMIT_TRAILER_KEY` now comes from
`kernel.memory_attribution`, because the writing model stopped naming it — and registered the new module
as an exact consumer of two shared-support artifacts in `mcp/tests/evidence-lifecycle.toml`; no case and
no assertion in `test_memory_ledger.py` changed.

## 260913-LCA-L5 Leaf Master-Link Binding, And The Fixture Correction It Forced

The change set's new module is `test_leaf_doc_master_link_binding.py` (integration lane, row 152): the
derived master link proven end to end, plus the fail-closed half — a leaf under a task root with no master
document is refused with its remedy. Its focused decision-table half is the new
`LeafDocMasterLinkBindingTests` class in `test_task_document_application_1.py`.

**One test was removed and must not be restored as it stood.**
`test_task_document_application_1.py`'s `test_create_writes_both_files` authored a bare leaf through
`task_doc` under a task root with no master document; the authoring plane now refuses exactly that
scenario, because nothing would ever bind the leaf's derived `seriesContractPath`/`enclosures[]`. The
file-write behavior it asserted survives in `test_leaf_create_syncs_parent_master_row` and in the new
end-to-end module.

Four existing test modules gained a prerequisite the refusal made mandatory, and each is a fixture
correction rather than a weakened assertion:

- `test_task_document.py` — shared `ApplicationTests._create` now ensures a parent master exists
  (`_ensure_parent_master`), keeping every leaf operation on the flow the plane allows.
- `test_task_doc_review_public.py` — `_create` writes the task root's master document first, because the
  review API is exercised on a leaf.
- `test_closeout_queue.py` — `_leaf` now binds `seriesContractPath` alongside `enclosures[]`.
- `test_transaction_only_worktree_delivery.py` — `_bind_task_without_review` does the same.

The last two are the load-bearing part, and they are why the fixture change is not cosmetic: a leaf
document with an exact enclosure address but no `seriesContractPath` now **refuses closeout by name**
(`task-enclosure-binding-master-link-missing`, raised by `worktrees/task_leaf_binding.py`) where it
previously read as `present` and passed silently. Those two fixtures had been modelling the damage state
that a start repairs, so four unrelated closeout cases began refusing until they carried the field
`task_doc` actually stamps. That is an intended consequence of the change, not an accident.

Lane membership was reconciled against the current manifest in the same change set: 204 modules on disk
and 204 manifest entries, 115 unit-regression, 2 public-contract, 58 integration, 16 architecture-fitness
and 13 provider-conformance, with stress-durability and migration empty. `load_lane_manifest` stays
fail-closed, and both new-module rows (the L4 census and this leaf's binding suite) exist, so the
manifest loads. Detail lives on the `test-evidence-lanes.toml` card, the owner of record for lane
membership.

## 260913-LCA-L10 Sub-Task Index Reachability

The projection reads durable task documents written by other, independently versioned processes, so one
of them may carry a field this reader's schema has never heard of. Until this leaf each of the reader's
five parse sites caught `ValueError` and **dropped the whole document**, so a completed leaf written by a
newer build disappeared from `analytics.taskDocuments` and the dashboard's sub-task row rendered as dead
text while unstarted rows stayed live — a version skew that presented as a status filter. The read edge
now tolerates exactly that skew (purely `extra_forbidden` keys pruned and re-validated) and nothing else.
Authoring did not move: `write_task_doc` still takes a validated `TaskDocument`, so it must refuse such a
document.

`test_task_documents_graph_projection.py` carries the behavioural proof. Its new
`SubTaskIndexReachabilityTests::test_completed_leaf_written_by_another_build_stays_reachable_from_the_index`
builds one master with three rows over a temporary task root, republishes the completed leaf's durable
JSON with an unknown field at the step level, writes a second document with a required field deleted, and
asserts through `read_task_documents`: the skewed completed row resolves with its real identity and
progress (`("01_DONE", "Completed", 1, 1)`), the unstarted row resolves as before, and the broken row is
`None`. The helper `_index_doc` reproduces the dashboard's own index rule (`sliceForRef`) rather than
approximating it, so the assertion is the property the projection owes an authored row; reverting the
single tolerant condition fails exactly this case.

Two mechanics a future reader must not "fix": the skewed JSON is written with `Path.write_text`, not
`write_task_doc`, precisely because `write_task_doc` must refuse it; and the unknown field is spelled
`checkpoint` on a step, mirroring where the live skew landed (`step.note`, `tasks/document.py:121`)
without depending on a field this reader may later learn. The module gained one case and one helper,
its lane row is unchanged, and no budget moved.

## Historical milestone context: 260913-LCA-L11 The Rebuild Outranks The Ledger File: Three Modules Grew Cases, None Was Added

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

**No new test module and no deleted module.** The change set is seven modified files, three of them
test modules, and this route's module population and lane membership are unchanged. What grew is
coverage of a rule that changed direction.

`test_checkpoint_landing_end_to_end.py` is the behavioural proof and six of its cases were rewritten.
Three changed **direction** and now assert an ACCEPTANCE rather than a refusal — a reordered source
region, a reversed superseding pair, and the interleaved projection on the leaf route — because the
file-preservation rule that refused them is gone. Each keeps its scenario and asserts the landing (the
leaf case by measuring that both destination refs really moved), which is the difference between a
relaxed rule and a rule that stopped running; a case that only asserted the surviving refusal would
read as if the file rule were still in force, and a deleted case would hide the change entirely. The
reversal case is the leaf's central piece of negative knowledge: reversing a superseding pair for one
code commit now lands and **nothing at the landing reports it**, so it carries the hazard in its
docstring and points at the transaction card's record of it as a gap pending a decision.
`test_a_unioned_master_line_still_refuses_a_content_difference` narrowed to the untrue row (the
`dropped`/`duplicated` corruptions are deleted with a comment saying why, and the reorderings are
asserted as landing below the refusal), and
`test_a_hand_edited_master_ledger_is_refused_by_the_preview_and_the_apply` kept its fabricated row
precisely so the refusal is attributed to the new row-truth rule rather than to an earlier gate.

`test_integration_branch_authority.py` carries the clause inventory, and this is where the
removed-and-unwitnessed gaps were closed. The landing's four surviving promises now each have their
own case: the mapping clause (including a table that names the landing's code commit with *different*
memory content), the **conditional** source-ancestry clause with a divergent source line the fixture
asserts is really divergent, row truth against both repositories, and the header. Two shapes the old
rule refused — a dropped source row and a duplicated one — are **asserted as accepted** rather than
deleted, and two new module-level cases drive `_require_true_rows` directly over a minimal contract so
the two row-truth clauses are witnessed without a whole enclosure.

`test_memory_ledger.py` gained the reader's two failure-shaped cases: a source row whose memory commit
the source cannot carry is excluded at the read with its reason and its count instead of vanishing,
and a partially trailered line still reads its pre-rule rows. The second is the reader's second,
independent defect — a 479-row source with one trailered commit read as a ONE-ROW source, which is the
"looks like no attribution exists" failure in its most expensive form. The `_content_commit` helper
exists because a row's memory cell must now name a commit git can resolve.

## Historical milestone context: The Sync Half Of The Ledger Rule And The Mid-Flight Result

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

**The sync half of the same ruling is proved in the transaction.** `test_worktree_sync.py` gained
`test_a_descendant_memory_ledger_that_dropped_a_source_row_is_current`
(`:206-243`): it commits a memory content commit, rewrites `memory.md` so its one row maps the code
base to that newer content commit — the stale-duplicate shape a recomputed table produces — and
asserts the public `sync_result` returns `already-current` with no `dropped parent mapping` text
anywhere in the payload and the memory work branch unmoved. Under the removed rule the source's own
row had to survive in the resolution, which is why that same thirteen-row shape left a correctly
closed master permanently unsyncable. The case is the transaction's regression guard; the
projection's own exclusion reporting stays with `test_memory_ledger.py`.

`test_atomic_series_activation.py` gained `ReconcilingResultTests` (`:231-297`) and two cases that
drive `_reconciling_result`, the reporting boundary the public selecting operation composes, against
a mid-flight `reconciling` record. The first asserts a `synced` pass is **not** reported as success:
return code 2, state `atomic-series-reconciling`, the activation observation attached unchanged, and
a summary naming the master's task-document ref and contract path, its publication time, its
revision, both `worktree_sync` exits, and the pass's own message last. The second uses a `blocked`
refusal and asserts the mid-flight identity is stated **before** the refusal's own words, so the
caller reads the state it must resolve rather than the symptom. Neither addition created a module or
moved a lane: both files already carried their rows.

## 260913-LCA-L8 A Cleanup Blocker Always Names Its Reason

**One new module, no deleted module, no lane moved.** The leaf's new module is
`mcp/tests/test_terminal_blocker_reasons.py`, registered in the **integration** lane at entry row 177
by the same change set that created it.

The defect was an operator-facing contradiction. `lifecycle_finalize_task` on one leaf's enclosure
answered `state: cleanup-blocked` with `blockers: [{"provider": "providerRuntime", "reason": null}]`,
while the same payload proved the terminal archive, reported the providers `torn-down` with their
runtime already removed, and said in its own summary that enclosure deletion may continue. Cleanup
stopped on that blockage anyway, preserved the citation-source index with `terminal-operation-failed`,
and left the leaf un-finalized; an immediate retry reclaimed two worktrees, two branches, the reports
directory and the enclosure root, and finalized the edge. Read from source, the **first call was
wrong**, not a real cause the retry re-observed as resolved: the blocker was constructed in
`worktrees/modules/terminal_validation.py`, where a result dict with no `reason` key became `None` and
the item still counted as blocked, and the only producer able to hand it `{"removed": False}` with no
reason at all was `application/provider_runtime.py::remove_tree`'s post-reclaim "still present"
branch — every other non-removal path already named a reason.

The change makes a reasonless blocker impossible to emit rather than merely unlikely.
`terminal_validation._blocker(component, reason)` is now the only construction path for a terminal
blockage and raises `RuntimeError` naming the component when the reason is missing, blank or not a
string; `_blocked_reason(item)` answers a reasonless or malformed item in operator language
(`no reason reported by the terminal result`, `invalid-result`); and every call site routes through
both. `TerminalResult` and `TerminalExpectation` bundle the outputs with preview-versus-real, which is
also what lets the dry-run path read preflight previews as previews and replaced the five-keyword
builder signature with one bundle argument at every call site; the change set adds no `# noqa` and no
per-file ignore. On the producer side, `remove_tree` sets a non-empty reason on every
`removed: False` result. This adds no teardown capability: a genuinely blocked teardown still blocks,
with its own reason.

The module holds seven cases in two groups. The whole-tool cases build a real landed leaf through the
shared external-memory authority fixture, complete the integration through the public
`worktree_integrate_tool`, and call the public `lifecycle_finalize_task_tool`: the L6 shape — provider
runtime already gone, the port answering `already-absent` — must finalize on the **first** call with
an empty `notRemoved` inventory, both worktrees and the enclosure root really gone and the leaf
document `Completed`; and a real permission failure on the provider-runtime tree must refuse as
`cleanup-blocked` / `blocked` with `remove_tree`'s own `permission denied: ...` reason as its single
blocker, close nothing, and refuse identically on the retry. **The L6 payload is reproduced through
the provider port boundary rather than by triggering the original physical event**: the case
substitutes the teardown answer the port would return, so it pins the decision the tool makes given
that answer. The remaining cases drive the two invariant owners directly — the reasonless
`{"removed": False}`, a blank producer reason, an unnameable reason refused at its own source, the
`remove_tree` result shape, and the post-reclaim branch that could answer silently.

The module is a declared exact consumer of nine `mcp/tests/evidence-lifecycle.toml` artifacts —
`closeout_input_test_support.py` (`:331`), `curator_coherence_test_support.py` (`:391`),
`integration_branch_authority_test_support.py` (`:435`), `repository_profile_test_support.py`
(`:565`), the two `repository_profiles/node` fixture files (`:604`, `:643`),
`gate_certification_test_support.py` (`:955`), `source_selection_test_support.py` (`:1012`) and
`selected_lifecycle_test_support.py` (`:1038`) — and of the ambient-role runner in
`dependency_ownership.py` (`:82`). Consumer declarations are ownership accounting only; they are not
execution or acceptance evidence.

## Historical milestone context: 260913-LCA-L3 The Trailer Backfill's Own Contract

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

**One new module, no deleted module, one lane row added.** The leaf's new module is
`mcp/tests/test_memory_backfill.py`, registered in the **unit-regression** lane at
`mcp/tests/test-evidence-lanes.toml:69` by the same change set that created it. It declares no
`mcp/tests/evidence-lifecycle.toml` consumer row, and that is correct rather than an omission: its
only imports are the production modules under test plus stdlib, so it reaches no
`consumer_scope = "exact"` shared support artifact. `mcp/tests/test_git_command.py` was migrated
with it — the stalled-command timeout case and the raw-commit stdin case now build
`GitRunnerOptions(...)` instead of passing keyword arguments, which is the only change either case
carries.

The leaf delivers the migration **tool** and its measurements, not a rewritten history, and an
external review found two defects that are now fixed. The pre-fix backfill had been applied on this
master's own memory line, verified, and then **reverted by developer ruling**: rewriting the shared
ancestors renumbered them, so the master's memory line and its super branch shared no common ancestor
and the plane's lineage gate refused everything downstream. The fixed tool has **not** been applied to
any real repository; its evidence is fixtures plus a read-only plan measurement. The backfill is an
explicit step at this master's integration into IAS, and the shared source line `7317108b` still
carries **0** `Code-Commit:` trailers. The worker's re-measurement also replaced the leaf
document's census, and this route records the measured values: 474 tracked rows and 419 distinct code
commits at the shared line are exact, while "104 duplicate rows" is 55 (every one sharing a code sha
with another row and naming a different memory commit), "513 trailers" is 419 at the shared line and
428 at the master's tip, and "10 skips" is 67 and 44 under the superseded vocabulary.

**The first reviewed defect was the selection, and the cases pin the fixed rule from both sides.**
The rule is a decision the code makes and therefore a decision a test has to pin, and it has two
halves: a maximum matching, so no code commit is left unnamed while a memory commit that could have
named it stands empty — code commits offered most-constrained-first, a tie between two equally
constrained claims going to the older row read off the table — and then a fill giving every memory
commit the matching did not reach its own oldest row, because a matching is symmetric and the format
is not. `test_every_recorded_pairing_that_can_be_carried_gets_its_own_trailer` asserts both pairings of
one code commit keep a trailer, which is what the fill exists for;
`test_the_winner_does_not_depend_on_hash_order` swaps two rows in the same table and asserts the
bottom-most row's owner wins in both, which is the defect stated directly; and
`test_a_contested_memory_commit_names_the_oldest_claim_and_reports_the_loss` asserts the loser through
`lost_claims` with its `winner` named and the plan not empty. The skip vocabulary is now closed at five
literals split into holes and declines, and the two declines are asserted apart:
`test_a_declined_row_names_whether_it_is_a_duplicate_or_a_lost_mapping` holds the two tables a single
count cannot tell apart, and only `lost_code_commits` separates a decline that cost nothing from one
that lost a mapping. A plan that lost a mapping is asserted to be non-empty and to carry a different
digest from a plan that did not, because the digest is what an apply is pinned to.

Idempotence is proved twice — the second plan over a migrated line is empty with the branch tip
unmoved, and the rewrite itself replays tree, both identities, both dates and the subject, so a rebuilt
commit differs from its original in its trailer block alone and an untouched commit reproduces its own
object id.

**The acceptance proof changed shape, and that is the second half of the first defect.**
`test_the_trailers_alone_preserve_every_pairing_the_ledger_file_recorded` reads the rewritten tip
through `_ABSENT_LEDGER`, a declared path no commit carries, so the table contributes nothing and the
mapped historical pairings are compared against Git-parsed trailers by set equality — failing if any
carryable pairing is omitted and asserting the one that cannot be carried as a reported loss. The
earlier proof read the table the migration carries forward, and because `read_ledger_source` unions
table rows into trailer rows it proved the table had survived rather than that the trailers preserve
the pairings, which is how 60 omissions passed a green suite.
`test_a_content_bearing_duplicate_that_would_be_dropped_fails_the_proof` reproduces the documented
drop shape against the trailer-only read.

**The second reviewed defect was on the command path, so the command path has its own class.**
`MemoryBackfillCliTests` drives `run` through the same parser the console script builds against a real
leaf contract whose memory work branch is a NAME: a rescue set built from a name and read back as a
hash can never compare equal, so the reviewed code wrote its rescue refs and then refused, and the
retry tripped the existing-ref check on refs its own predecessor had created.
`test_the_cli_applies_a_branch_name_tip_and_survives_its_own_retry` asserts the first apply completes
from a name, moves the branch and leaves the rescue ref on the pre-rewrite tip, and that a second
apply returns 0 having moved neither the ref nor the branch. Every fixture is a throwaway pair of Git
repositories under `tempfile`; nothing here reads or writes the coordination tree, the installed
memory repository, or any shared ref. The module makes no claim that a backfill has been applied to
the real memory repository — that sequencing decision belongs to the master's integration step, not to
this route's evidence.

## 260915-CAPS-L11 `D9`'s Six Historical Modules Register, And The Route Closes Its Own Gap

This route's `D9` residual is **closed**. Six historical test modules had been unregistered in
`mcp/tests/test-evidence-lanes.toml` while the fail-closed loader reported each one by name; L11
registered all six in `unit-regression` — `test_eve_adapter`, `test_eve_protocol`,
`test_role_capsule_admission`, `test_role_capsule_compiler`, `test_role_instruction_corpus`,
`test_task_projection` — and `load_lane_manifest` now returns `LANE-REGISTRY-OK 243 0` with no
unregistered-module finding.

**Two properties make the registration load-bearing rather than decorative, and both are asserted.**
Each of the six carries its own row and **collects** (198 cases under the unit selection, 0 under
`-m integration`), and the seed `S-D9-lane-row-removed` deletes one row and makes the loader
**refuse by name** rather than fall back to a default classification. Rows added by this master's
other leaves are unchanged, and no module was moved between lanes by name.

**The route's lesson, worth keeping because the leaf lost time to it:** a manifest fingerprint must
be **asked of the product**, never rebuilt by hand. An intermediate draft recomputed the digest from
its own rendering — `file:`-prefixed, merged-sorted terms — and produced a self-consistent value
(`bfbd21af…`) that described no artifact; the product's own `LaneManifest.digest` for this candidate
is `61f9fba8…` over 243 files / 0 overrides. Counts and lane dispositions were never in question;
only the fingerprint was.

## 260918-TSIP-L4 — The Lane Hook Goes Live And The Conformance Module Lands

This leaf's route gained **one module** and one structural change to how the route is collected.

- **`mcp/tests/test_tool_response_conformance.py` (new, 864 lines, 15 cases) is the route's
  response-contract conformance owner.** `ToolResponseSurfaceTests` (`:261-423`) is total and
  structural over the 84 registered response models; `ToolResponseFiringStateTests` (`:424-864`)
  is executed, driving seven real producers through the real `mcp/tools/base.py:_tool_payload`
  adapter against hermetic scratch coordination roots. It replaces the 1,174-line sweep deleted at
  `d3610903`, which is **not restorable**: 11 rot sites, it does not collect verbatim, and its
  sweep class was `@pytest.mark.integration` — so the default lane deselected the very cases this
  leaf exists to land. The rule the new module is built on is the old sweep's failure mode: a
  fixture that sits in a guard's false branch is a false green, so every executed case asserts it
  reached the emitting branch before it asserts validation.
- **The lane registry is now enforced, not merely declared.** `mcp/tests/conftest.py:81-84`
  registers `agents_remember_test_support.testing.evidence_lanes`, whose
  `pytest_collection_modifyitems` calls `load_lane_manifest` and raises `pytest.UsageError` when
  it refuses. Before this leaf the hook was defined and never registered, so the suite passed while
  the manifest refused (`T48`). With it armed, the loader reports
  `251 rows / 251 modules` (`f5f3c262…`), and add a module without its row and **collection refuses
  outright**.
- **A consequence that changes this route's preconditions: collection now requires a Git
  checkout.** The loader enumerates the population through `git ls-files`, so an exported
  (`git archive`/tarball) tree fails collection instead of running. Stated at the registration site
  and in `docs/design/python-pytest-bootstrap.md:22-24`.

Lane membership for the new module is `architecture-fitness`
(`mcp/tests/test-evidence-lanes.toml:247`); the chain-order module registered by `T49` is
`integration` (`:165`). The manifest is **267 → 269 lines**. Because those two insertions moved
every entry below them, the card for that manifest and every card citing it had their citations
re-derived by enumeration — the route's own citation rows into it are among them.

**Two figures in this route's own older prose were already stale before this leaf** and are
reported rather than silently rewritten: `docs/design/python-pytest-bootstrap.md` is cited at
`1-53` (was `1-50`), and the repository's declared case budgets are `unit_case_budget = 2000` /
`integration_case_budget = 300` (`pyproject.toml:168,176`), while several prose passages in this
route still quote 1000/150 or 1500/250.

---

## 260915-KS-L19 The Requirement-Revision Suites, Their Lane Rows, And One Re-Scoped Seam Case

This leaf added two test modules and one lane registration each, and re-scoped one shipped facet assertion.

- `test_knowledge_requirement_revisions.py` — **17 collected cases from 17 definitions**, flat module-level
  functions with no test class. It is the record group's *internal* boundary: the kind's admissible pair, the
  two declared operations as members of the shipped vocabulary, the state/acceptance consistency rule in both
  directions, the promotion refusal measured as the stored payload being byte-identical afterwards, an
  `accepted` payload stored with the envelope lifecycle still `proposed`, the explanation refused by value, the
  four authorship substitutes refused, and the lineage rules including **a stored cycle forced by dropping the
  `record_revision_no_rewrite` trigger** so the shared `lineage.find_cycle` is what refuses the descendant.
  Two facts worth knowing before reading it: immutability is asserted against **re-read stored bytes** rather
  than a return value, and the two forbidden-name sets are **restated in the suite rather than imported from
  production**, so the absence case cannot pass by an import that quietly stopped covering a name.
- `test_knowledge_requirement_reference_contract.py` — **18 cases**, also flat. It is the boundary with the
  task plane and the derived views: the three owner components, the admitted version spelling, the reference the
  payload deliberately does not police, the forbidden operative-obligation and task-authority names at **both**
  the payload and the schema planes, the real owner's refusals carried verbatim with the stored reference
  byte-identical, route governance, the three-way reference resolution, and the views' rebuildability, totality
  and no-winner rules. It drives the **real** `_approved_packet_ref` rather than a stub, because a stubbed
  resolver cannot catch the second resolver the suite exists to exclude.
- Both modules are registered in the `unit-regression` lane at manifest lines 81 and 82, which is what keeps
  them collectable under a named classification rather than by accident.
- **One shipped assertion was re-scoped, additively.** `test_the_seam_registry_is_exactly_the_eight_declared_subtypes`
  pinned `set(KIND_SCHEMAS)` as the union of the three groups L14 left; the fourth family makes that false, so
  the assertion now unions `REQUIREMENT_RECORD_KINDS` as well. It is **equal in strength rather than weaker**:
  the claim is still *exactly* the union, so a group the registry does not declare still cannot be admitted
  without that line changing, the new group is derived from the registry entry rather than restated, and the
  facet-specific assertions around it are untouched. No case was deleted, skipped or xfailed. The module's own
  `RE-SCOPED` note now records two re-scope generations and is the place a reader learns the envelope registry
  is a shared, append-only surface.

**One code-side gate gap is recorded rather than settled here.** Both new modules import the shared-support
artifacts `knowledge_fixture_test_support.py` and `generation_test_support.py`, and both artifacts declare
`consumer_scope = "exact"` consumer lists in `mcp/tests/evidence-lifecycle.toml`. This leaf added the lane rows
but not those consumer entries, so the repository's own read-only evidence-lifecycle validator reports two
`consumer proof differs from source-derived ownership` findings for this change set. It is reported by this
leaf's curator to the owning seat; it is a code-side fix, not a memory one.

- **The two new modules' lane rows, registered by the same change set that created them.** [299]
- The record group's internal-boundary suite and the two facts that make its immutability and absence claims measurements. [300]
- **The re-scoped seam case that pins the registry as the union of all four groups.** [301]
- The two shared-support artifacts both new modules consume, whose exact consumer lists are the gate gap recorded above. [302]

## 260918-TSIP-L6 The Refusal Census, Two New Lane Rows, And Both Pins Emptied

This route gained three modules and lost none. `260918-TSIP-L6` carried the leaf's delivery-shape
rule into a durable check: `mcp/tests/test_tool_refusal_conformance.py` (**349 lines / 7 cases**)
drives **every** advertised tool down a path that cannot succeed and requires the answer to be a
typed refusal (identity, reason, next action), a recorded always-answer, or a recorded bare
raiser — the census it asserts is **67 = 32 refusals + 18 pinned raisers + 17 always-answer**.
`mcp/tests/tool_refusal_census_support.py` (**253 lines**, no collected case, no lane row) holds
the measured population, one production invocation per tool, asserted equal to `PUBLIC_TOOLS` in
both directions before anything is driven. `mcp/tests/test_response_address_binding.py`
(**355 lines / 7 cases**) pins `T54`'s guard, `T71`'s refreshed-onboarding census and `T64`'s
preview `ok` at their own levels.

**`T34`'s nine tools no longer raise**, and the sweep **emptied both pins in the same change**:
`ENVELOPE_LOSING_RAISERS` is now `frozenset()` and `UNMARKED_NOT_OK` is now `{}`, with
`T34_REPAIRED_TOOLS` added beside the pin it belongs to as the single source of truth. A new case
in the sweep (`test_the_t34_family_answers_with_a_named_refusal_instead_of_raising`, `:963-1008`)
asserts the repair where it is observable. `STATE_DEPENDENT_RAISERS` is untouched: its five
members cannot refuse without a contract change (`T66`, deferred), so the pin stays and names
itself as an open, measured defect.

**The lane manifest changed by pure insertion** — `test_response_address_binding.py` at `:112` and
`test_tool_refusal_conformance.py` at `:155`, both `unit-regression`, `270 → 272` lines — so every
citation into it below OLD line 112 moved, and this route's own reference rows were re-derived
from the candidate rather than shifted (`T60`/`T52`).

## 260915-KS-L1 The Knowledge Storage Suite And Its Registered Fixture

This route gained one test module and one governed support module, and both are load-bearing for the repository's
own evidence machinery rather than only for the leaf.

`mcp/tests/test_knowledge_store.py` — 23 nodes, all in the **unit-regression** lane and carrying no integration
marker. (The 23rd arrived with `KS-R03`: it pins the identity operation's two-caller repeat contract, which the
candidate-batch refactor had silently changed. See the KS-L3 section below.) It is the executable counterpart of the knowledge requirement's failure list: the divergent-successor
read, identity reuse with differing content, dangling and cross-invariant predecessors, the two-branch lineage
refusal, database-level immutability, the seal covering the predecessor set, the schema-generation validation and
the layer-direction guard. Two of its nodes are enforcement-load-bearing in the sense that disabling the mechanism
makes a named node fail, which is what makes the guard's coverage real rather than apparent.

Its registration matters twice over. `mcp/tests/test-evidence-lanes.toml` gained the module in `unit-regression`
because a test module with no explicit lane makes `load_lane_manifest` refuse the whole repository, which
`evidence_lanes.pytest_collection_modifyitems` turns into a collection error and the quality path swallows into a
run without retry proof. Registering it is therefore a precondition for the certifying collection path to start at
all, and it is classification only — never execution or acceptance evidence.

`mcp/tests/knowledge_fixture_test_support.py` — the shared branching fixture (one repository, one invariant, a base
`I0` and two `v2` successors `I-A`/`I-B`), built through the real typed operations rather than by inserting rows.
It is registered in `mcp/tests/evidence-lifecycle.toml` as contract `knowledge-identity-branching-fixture` with an
explicit `[[artifact]]` row (`shared-support`, `internal-canonical`, `unit-regression`, `in-process`, `permanent`,
`consumer_scope = "exact"`, one observed consumer).

The fixture's **location is part of its contract, not a preference**. `governed_artifact_paths` discovers durable
support under `mcp/tests/**` plus a small fixed root set; `mcp/test_support/**` is not governed, so the same module
at `mcp/test_support/agents_remember_test_support/testing/knowledge_fixture.py` could not be registered at all —
it is refused both as an ungoverned catalogued path and because a module outside the test roots has no derivable
test-consumer proof. This paragraph exists so a later reader does not "tidy" the module back under `test_support/`
and silently break the registry.

- The knowledge suite and its unit-lane placement (row 74 after the KS-L3 insertions). [303]
- The suite's one-to-one card, which enumerates what each node protects. [304]
- The fixture's registered stable contract row and its matching artifact row. [305]
- The fixture's one-to-one card, including the relocation rationale. [306]
- The enforcement-load-bearing nodes a disabled guard fails (re-cited after the KS-L3 node insertion shifted the file). [307]
- The manifest rule that makes an unregistered module a hard load failure. [308]
- The fixture builder the suite composes — re-cited against the working tree, where the same builder gained the graph half. [309]

## 260915-KS-L2 The Graph Suite And The Corrected Fixture Registry

This route gained four test modules and one governed support module, and — like the L1 increment — two of them are
load-bearing for the repository's own evidence machinery rather than only for the leaf.

`mcp/tests/test_knowledge_family_revision.py` (9 nodes), `test_knowledge_relation_rules.py` (12 nodes) and
`test_knowledge_graph_reads.py` (6 nodes) are the executable counterpart of the graph requirement's failure list:
a guarantee that must not change behind an existing family revision, the two predecessor refusals on the family
lineage, the two-branch lineage wording, the shared rule the family graph applies, endpoint refusals that leave the
whole-database row counts unmoved, the anchored-claim transaction that leaves no orphan anchor on a refusal path,
pair uniqueness versus identity reuse, the stale-caller removal contract, the database-level payload and foreign-key
enforcement, the namespace sweep, and the identity-set equality of the forward and reverse reads. All are in the
**unit-regression** lane and carry no integration marker.

`mcp/tests/knowledge_revision_seals.py` (5 nodes) is a **fix-verification** module and needs a word of explanation,
because its existence is itself a finding's outcome. The round-1 evidence claimed every guard the leaf added was
load-bearing, but no mutation of the sealed predecessor field was caught by any node in the repository (sealed
finding `260915-KS-L2-RV-1`): the node named for the seal also varied `revision_id`/`display_version`, so its
assertion held for a reason other than the field it named. The repaired node now holds every other sealed field
equal, and this module extends the same isolation to the invariant payload and to the read path on both graphs in
both directions. A future reader should take the general rule from it: **a test named for a sealed field must vary
only that field, and removing the field from the payload must make that named node fail.**

`mcp/tests/knowledge_graph_test_support.py` is the new governed support module, registered in
`mcp/tests/evidence-lifecycle.toml` as contract `knowledge-graph-case-support` with exactly three declared
consumers (the three graph modules; the seals module builds its own seeds and does not import it). It follows the
L1 fixture's design rule — every fixture value is built through the public typed operations — and its two raw
writes exist precisely because the operations *forbid* the state the lineage rule is exercised against: a stored
cycle can only be constructed by hand.

**The fixture's registry row was corrected, not merely extended.** `knowledge_fixture_test_support.py` grew a
graph half inside the same builder (a second and third invariant, two overlapping families with a successor and a
same-label sibling, and three recorded realizations), which made its declared consumer list wrong: the row named
one module while five now import it. The validator derives each governed artifact's actual test importers and
refuses a differing declared set, so this was a real registry defect rather than a thin count. The row now declares
all five, and its source-version and permanence text says the same builder carries both scenarios. The artifact's
`introduced_by` stays `260915-KS-L1`: it was extended in place, not forked — which is the design rule the L1
paragraph above states, now demonstrated.

The lane registration is the same precondition it was at L1: four modules without explicit lanes would make
`load_lane_manifest` refuse the whole repository, which `evidence_lanes.pytest_collection_modifyitems` turns into a
collection error and the quality path swallows into a run without retry proof. Registration is classification only
— never execution or acceptance evidence.

- The four graph modules and their unit-lane rows (rows 69-73 after the KS-L3 insertions). [310]
- The four graph modules and their unit-lane rows (rows 69-73 after the KS-L3 insertions). [311]
- The graph case-support contract and its three declared consumers. [312]
- The corrected branching-fixture row, whose consumer list now names all six importers. [313]
- The field-isolating seal node and the four read-path nodes that make the seal's evidence honest. [314]
- The requirement's own falsifier: the two directions compared as identity sets. [315]
- The atomicity nodes: a refusal leaves the whole-database row counts unmoved. [316]
- The node that proves the family graph applies the invariant graph's own lineage rule. [317]
- The graph support module's one-to-one card, which records its owner and consumer set. [318]
- The corrected fixture card, whose graph-half paragraph records the extension-in-place rule. [319]

## 260915-KS-L3 The Candidate-Batch Suite, And The Guard A Passing Suite Could Not See

This route gained three test modules and one governed support module, and the fourth is a case where the missing
evidence was itself the defect.

`mcp/tests/test_candidate_batch_transaction.py` (27 nodes) is the requirement's verification evidence: the
all-or-nothing proof (mutating the rollback to a commit fails a named node), the database-caught rollback at a
**non-final** command, the competing-writer refusal, the lane and admission refusals, the preconditions, the
completed-graph lineage rule with a spy that fails when the shared rule is neutered, and the removal receipts.
`mcp/tests/test_candidate_batch_commands.py` (9 nodes) covers the closed union and the receipt's fidelity.
`mcp/tests/test_knowledge_label_operations.py` (6 nodes) exists because the batch path carries an **independent
copy** of the label expectation rule: deleting the CAS in `labels.py` left every batch case green (sealed finding
`260915-KS-L3-RV-4`), so the standalone operations needed their own module before the guard was load-bearing at
all. All three are in the **unit-regression** lane (rows 18-19 and 70).

`mcp/tests/candidate_batch_test_support.py` is the new governed support module, registered in
`mcp/tests/evidence-lifecycle.toml` as contract `candidate-batch-case-harness` with exactly two declared consumers
and an evidence node that is a real passing node. It builds its candidate through the **real seam** — an admitted
destination plus contexts resolved through `resolve_candidate_context` — so a case authors its batch against an
identity the application actually read; and it measures refusals through a **separately opened store**, which is
what makes "nothing was written" a measurement. Its one deliberate raw write exists because the typed operations
forbid the state a duplicate-pair case needs.

Two rules this leaf's evidence teaches, and both are about what a named node proves:

- **A node named for a mechanism must discriminate that mechanism.** The baseline round's "database-caught" node
  actually asserted the concept's own pre-check (removing it left the node green), and the "context digest" node
  asserted the model validator rather than the operation's re-derivation. Each is now split so the mutation that
  removes the mechanism fails the node that names it.
- **A green suite is not a preservation proof.** `test_knowledge_store.py` grew one node
  (`test_a_repeated_identical_invariant_is_no_change_and_a_relabel_refuses`) because 54 upstream cases passed while
  the refactor had silently changed `create_invariant`'s observable answer for an identical repeat.

- The batch pair's unit-lane rows and the transaction module's atomicity nodes. [320]
- The label-operations suite's row and the reason it exists as a separate module. [321]
- The candidate-batch case-harness contract, its artifact row, evidence node and exact consumer set. [322]
- The branching fixture's row, whose consumer list gained this leaf's label suite. [323]
- The node that pins the identity operation's two-caller contract after the refactor broke it. [324]
- The two split nodes that keep the database path and the concept guard separately proven. [325]

## 260915-KS-L5 The Merge Suites, Split By The Budget Their Contract Could Not Fit

This route gained two test modules and one governed support module, and the split between the two modules is a
**budget decision** rather than a classification preference: the unit population sits exactly at its declared
`unit_case_budget` of 1000 collected cases after this leaf, so the merge's whole contract is carried in five unit
cases and every scenario that needs its own world went to the integration lane.

`mcp/tests/test_knowledge_guarded_merge.py` (5 nodes, **unit-regression**, row 73) carries the contract in five
named nodes rather than one per scenario, and each node asserts the **whole** outcome — the state, the identity,
the refusal code, and that every input is byte-identical to what it was. What each node is the mutation target
for: the declared-manifest preflight (seven structural classes plus a reorder, a rename, a weakened trigger body, a
changed `user_version` and an absent or unreadable input); the **silent-omission** class, where a delta built over
a subset of the canonical tables is accepted by SQLite and refused by the coverage comparison *and* the replay; the
conforming merge into a closed, published candidate that carries no verdict field; the refusal taxonomy, including
the exact conflict-key assertion; and base resolution plus input integrity, including a criss-cross history with
two common bases and a side that rewrote a sealed revision in place.

`mcp/tests/test_knowledge_guarded_merge_boundaries.py` (6 nodes, **integration**, row 139) holds the scenarios that
each need their own three-commit Git world: the conflict-row identity on a row that is **not the first** the table
holds, a table carrying an insert alongside a conflicting update, the old-side key rule with the missing-key case,
and the three final-integrity checks — the structural one reachable through a dangling reference all three inputs
carry, and the applied-change and merged-candidate-immutability ones exercised as **policies** because their call
sites cannot be reached by a black-box case at all.

`mcp/tests/merge_case_test_support.py` is the new governed support module, registered in
`mcp/tests/evidence-lifecycle.toml` as contract `common-base-merge-cases` with exactly two declared consumers and
an evidence node that is a real passing node
(`test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate`). It authors every dataset through
the **real store operations** and closes it through SQLite's own backup; it builds a **real three-commit Git
world** in which the base is the two sides' parent, so the common base is a fact of the commit graph rather than of
the fixture's bookkeeping; it materialises each side's file out of its commit rather than from a working tree; and
its `shape` callback runs *before* the commits are built, so a case's unusual state is inside the history the merge
is asked to prove rather than a rewrite afterwards.

Two rules this leaf's evidence teaches, and both are about what a survivor means:

- **A broken mutation is not a killed guard.** The leaf's first matrix scored an `M16` survivor as killed because
  its mutant module raised `NameError` and every node failed; the harness now classifies each failure and refuses
  to score a `NameError`, `ImportError`, `SyntaxError` or collection error as a kill. Re-derived, the headline is
  **17 of 21 killed with four non-experiments**, each with its cause stated.
- **A guard whose call site is unreachable is described as one.** Two of the merge's postcondition guards cannot be
  falsified by a black-box case under this schema, and the freeze's contribution is invisible to a case for the
  same kind of reason. Each is recorded as a non-experiment beside the reason, with its *policy* exercised by a
  direct node, rather than presented as coverage.

- The five-case unit module, its budget statement and the whole-outcome assertion rule. [326]
- The registered evidence node of `contract:common-base-merge-cases`. [327]
- The two conflict-identity boundary nodes that regression-guard the corrected old-side key. [328]
- The reachable structural guard and the two direct-policy nodes for the unreachable call sites. [329]
- The shared harness: the real three-commit world, the commit-materialised files and the build order. [330]
- The governed-artifact registration and exact two-consumer list this leaf added. [331]
- The governed-artifact registration and exact two-consumer list this leaf added. [332]
- The lane rows the two modules were registered in, and the budget statement they sit under. [333]
- The lane rows the two modules were registered in, and the budget statement they sit under. [334]
- The two guard docstrings that state their own call site's unreachability. [335]

## 260915-KS-L6 The Portable Suites, Split By The 1200-Line Limit

This route gained **two** test modules, both registered in the **integration** lane (rows 140-141), and the split
between them is a **file-size decision** rather than a classification preference: the roundtrip module reached
1155 lines and one file may not exceed the repository's 1200-line hard limit, so the boundary population is a
second module that **imports the first module's helpers** rather than copying them. There is still exactly one
definition of what an artifact, a refusal or a published row count is, and the two modules are one evidence set.

`mcp/tests/test_knowledge_portable_roundtrip.py` (18 nodes) holds the artifact contract and the export/import
population. Its cases are **consolidated by protected property** rather than split one per assertion — the
population has a declared ceiling and each node names the one failure it exists to catch:

- **Completeness** — one node mutates an artifact through thirteen defects (a dropped collection, a truncated
  table, an unknown table, a value the declared type cannot hold, a reordered or renamed column, a repeated key)
  and asserts the check that catches each; the filtered-response pair keeps it honest, because a projection is
  refused *because it is not the format* and a complete projection of the source tables does validate.
- **Refusal without partial acceptance** — the destination's file digest and the destination directory's contents
  are measured after the fact, so "nothing was published" is a measurement rather than a promise.
- **Preservation** — every stored ID, provenance value and relation endpoint is held to the round trip, and the
  `state_at_origin` **value** crosses while nothing promotes it.
- Two nodes make the contract's own claims measurable: the artifact this encoder produces is the one this reader
  accepts (so the round trip is a proof rather than a coincidence), and a dataset that came **through L5's merge**
  is exportable and restorable — the composition the next leaves consume.

`mcp/tests/test_knowledge_portable_boundaries.py` (6 nodes) holds the five properties the ordinary path cannot
fail from outside: the freeze's closure measured on the **published destination**; the canonical form of the whole
document (every non-canonical spelling axis, `canonical_document`'s assertions, and **all seven header keys
respelled with a different JSON type** — each refused, each passing the whole-document gate, which is what proves
the refusal is the header check's); the **staged sealed-aggregate read** with every retained row of both revision
tables tampered and the destination held byte-identical; destination admission before any staging work; and the
typed read of an artifact that is not readable UTF-8 text.

Two rules this leaf's evidence teaches, and both are about what a survivor means:

- **A reachable guard with no killing node is reported, not claimed.** The header's namespace-binding check
  (`export_portable.py:911`) is reachable and verdict-changing — removing it makes a byte-canonical artifact whose
  header names another namespace validate and install — and no node in the leaf's population kills it. It is
  written up as an **observation for L9** with its mutation and reachability proof rather than presented as
  coverage.
- **A non-canonical spelling is a different document, and the cases say which check refused.** The canonical node
  asserts the refusal's identity (`invalid_export`, `record_id == "<canonical document>"`) as well as the verdict,
  and the leaf's final round extended these cases rather than adding a case, so the population stayed at 255
  integration cases.

- The roundtrip module's three falsified properties, the helper set and the two claims made measurable. [336]
- **The node the leaf's guarantee rests on: the canonical form is the only form the reader accepts, including every header type.** [337]
- **The staged sealed-aggregate read, with every retained revision row tampered.** [338]
- The import's close/verify step and the freeze's closure on the published destination. [339]
- The destination-admission and typed-read boundary nodes. [340]
- **The guard this leaf reports rather than claims: reachable, verdict-changing, no killing node.** [341]
- The two lane rows this leaf registered, and the three consumer lists it extended. [342]

## 260915-KS-L7 The Read Suites, And The Path Contract They Measure

This route gained **three** test modules and one **governed support artifact**, and the split between them is a
file-size decision as much as a classification one:

- `mcp/tests/test_knowledge_read_scope.py` — **unit-regression** (row `mcp/tests/test-evidence-lanes.toml:75`),
  21 nodes, hermetic: temporary directories, in-process APSW databases built through the public store
  operations, no repository working tree, no network. **It is at 1 163 of the 1 200-line limit, 37 lines of
  headroom, and L8 must split it before adding cases.**
- `mcp/tests/test_knowledge_read_boundaries.py` — **integration** (`:157`), 20 nodes over a real committed Git
  tree, a real published database and real snapshot/namespace refusals.
- `mcp/tests/test_knowledge_read_paths.py` — **integration** (`:158`), 5 nodes that measure Git's own
  `ls-tree` behavior with their own subprocess calls.
- `mcp/tests/read_scope_test_support.py` — the shared fixture, registered as an **artifact**
  (`shared-support` / `internal-canonical` / `unit-regression`) under the new contract
  `knowledge-read-scope-cases`, with the three modules above as its exactly-declared consumers. Fix round 2
  added the path module to that consumer list after splitting the over-limit integration module — a **consumer
  change, not a new artifact**.

**A new test module costs three registry touch-points and this leaf paid all three**: its lane row, its path in
the support artifact's `consumers` list, and the evidence-catalog digest re-pin
(`LIFECYCLE_CATALOG_SHA256` → `461121ca…`, with the contract/artifact counts 10/51) in
`mcp/tests/test_dependency_ownership_ast_helpers.py`. Miss any one and `load_lane_manifest` or the catalog
validator refuses the repository, so the failure is a **hard collection error rather than a quiet gap**.

**The path module is the one the review made load-bearing, and its contract is worth stating here because it
was corrected twice.** Git pathspec **magic** is the leading-`:` family (`:(exclude)`, `:!`, `:(top)`, `:/`)
plus `..`, absolute paths, `~`, drive/UNC spellings, backslashes and NUL; the characters `*`, `?` and `[` are
**literal characters** to `ls-tree` (measured on `git 2.54.0` by the case itself), so a legitimate anchor
containing them must be authorable, seedable and resolvable. Round 1 refused them, which made such an anchor
un-authorable and reported a file the tree really holds as `path_absent` — *a false statement about the
repository rather than a refusal of a malformed spelling*. The module therefore measures the three genuinely
different facts apart (`path_absent`, `unsupported_locator` with the cause in `detail`, and
`recorded_object_unavailable`), and it drives the two producers of the last one separately.

**Two honest limits travel with these suites, and neither is coverage.** `_tree_entry`'s **non-zero-exit**
branch is reachable by no input on this host; a published mutation claim that it was made reachable was
**withdrawn** by the leaf's own evidence erratum, because the kill that appeared to prove it also appears with
the production line untouched — so the branch stays an **explicitly disclosed unasserted defensive branch**
(L9 ledger **A6**) and must never be read as protection. And `_manifest_digest`'s inclusion of each item's
`selection_reasons` is a **reachable covered gap** with no killing node (L9 ledger **A4**).

**One more rule this leaf's evidence teaches, and it is about what a survivor means:** a sweep must run on the
frozen bytes it claims to describe. This leaf's first sweeps ran before the test module's last write, which is
why the published attribution of one kill was off by one line; the correction is in the erratum, and the
practical rule for a successor is to re-run the sweep after **any** edit rather than re-using a result.

- **The count semantics the review corrected, and the requirement's own non-conformance example.** [343]
- **The completeness node that derives the mandatory set from recorded rows rather than from the implementation's own page manifest.** [344]
- The ordering node the review sealed as HIGH, and the truncated-page node. [345]
- **The three path facts, and the case that authors, stores, seeds and resolves a path holding glob characters.** [346]
- The lookup that ran and could not answer, refused as unavailable rather than absent. [347]
- The lookup that could not be run at all, reported as the same fact. [348]
- The continuation bindings, each with its own control, and the read-only property on a real file. [349]
- The read fixture and its registered contract. [350]
- The unit-lane row the read's selection module occupies. [351]
- The two integration-lane rows the read's boundary and path modules occupy. [352]
- The read fixture and its registered contract. [353]
- The unit-lane row the read's selection module occupies. [354]
- **The catalog digest re-pin that a new test module obliges.** [355]

## 260915-KS-L8 The Comparison Suites, And The Evidence Rules They Teach

This route gained **two** test modules and one **governed support artifact**, and the split between them is a
classification rather than a size decision — both are well under the 1 200-line rail (840 and 779):

- `mcp/tests/test_knowledge_diff_scope.py` — **unit-regression** (row `mcp/tests/test-evidence-lanes.toml:76`),
  13 nodes, hermetic: temporary directories, two in-process APSW databases built through the public store
  operations (the candidate copied from the closed baseline and then curated through the store), and two
  local committed Git trees the fixture writes itself.
- `mcp/tests/test_knowledge_diff_boundaries.py` — **integration** (`:159`), 15 nodes over the same real trees
  but **driving the production Git probe** rather than a substitute, plus a real candidate write that moves
  the logical digest and the serialized response the forbidden-overreach case searches.
- `mcp/tests/diff_scope_test_support.py` — the shared two-snapshot fixture, registered as an **artifact**
  (`shared-support` / `internal-canonical` / `integration` / `local-composition`) under the new contract
  `knowledge-diff-cases`, with exactly those two modules as its declared consumers.

**A new test module costs three registry touch-points and this leaf paid all three twice**: its lane row, its
path in the relevant artifact's `consumers` list, and the evidence-catalog digest re-pin
(`LIFECYCLE_CATALOG_SHA256` → `4cf81f10…`, counts **11 / 52**) in
`mcp/tests/test_dependency_ownership_ast_helpers.py`. It also added the two modules to the **read-scope**
artifact's consumer list, because the diff fixture builds on the read fixture — a consumer change, not a new
artifact. The catalog is now **52 artifacts and 11 contracts**, measured by counting the blocks and hashing
the file, and the lane manifest is **243 declared entries against 243 modules on disk**.

**The coverage-rule reason is the most-corrected contract of this leaf, and its direction is measured rather
than argued.** Rule 1 is load-bearing alone (removing it turns a missing selection into a real absence,
`absent_from_snapshot` where `present_outside_selection` is owed). Rule 2 **cannot decide a state its
neighbours do not** — an authored edge is a foreign key into the snapshot that declares it — so it is kept as
a short-circuit, and the case asserts its **invariant** half through the published read surface while stating
that its **family** half is unexercised, because the fixture authors 0 `family_predecessor` rows. Rule 3 is
load-bearing in the direction that forces its answer **present**: forcing it present turns a genuinely
deleted realization into a missing selection (two kills), while forcing it **absent** changes no asserted
state on this population — variant `C` survives all 28 nodes — because the three items it answers for are
really absent. **Collapsing the three into one is wrong because it turns a missing selection into a real
absence**, the reverse of what the leaf first claimed; the `2 failed` an earlier artifact published for `C`
belongs to variant `G`.

**Three evidence rules this leaf's own history teaches, and they are the reason its documentation debt is
carried rather than papered over:**

- **A citation of a frozen file must be regenerated from that file.** This leaf published a `M25`/`M26`
  line-number pair under the words *"regenerated from the frozen file"* that is the **pre-round** file's
  numbering: on the frozen 779-line module `M26`'s node is at **`:603`** and its failing assertion at
  **`:658`**, and `M25`'s at **`:678`** / **`:716`** — not the `565`/`620` and `640`/`678` the artifacts
  republish. It is carried to `KS-R09`/`L9` (ledger **A9**, finding **`L8-W1`**) with the replacement text
  supplied, and **the ledger is authoritative for it**; this route's own cards cite the measured numbers.
- **A row table attributed to the frozen bytes must have been measured on them.** This leaf's row tables were
  measured **before** its own last edit — **the same class as `L7-X6`** and now its **second instance** — and
  every verdict still reproduces on the frozen bytes under the final verification round's own instrument.
- **A survivor needs a hand-run before it is believed.** An `A2` sentinel that fingerprinted
  `repr(code.co_consts)` was a **false positive by construction** (a nested code object's `repr` is a heap
  address) and reported `LOADED-CODE-CHANGED` on a completely unmutated mirror; the leaf withdrew every
  citation of it and adopted the verifier's content-only fingerprint, whose negative control refuses the run
  when the declared target did not move. **A sweep whose sentinel cannot fail is not evidence.**

**Four non-kill classes travel with these suites and none of them is coverage:** `M4`, `M8` and `M27` are
**covered gaps** against this leaf with their closers named, `M23` is a **non-experiment** with its
reachability bound carried rather than resolved, and `M9`, `M12` and `M21` are **equivalent mutants** with
the measurement that proves the equivalence. The corrected taxonomy over `M1`…`M27` is **19 assertion kills,
1 exception death, 3 equivalent mutants, 3 covered gaps, 1 non-experiment = 27**, and **nothing was skipped,
xfailed, deselected, widened or deleted to reach it** — the final round reproduced all of it with its own
instrument (39 mutation applications, 126 scored node runs, 41 assertion kills, 1 exception death, 0 broken
mutations, 0 refusals).

- **The packet's first non-conforming example, and the node `M1`/`M2` kill.** [356]
- **The present-outside-versus-absent distinction side by side, and the per-table rule-2 subsumption assertion.** [357]
- **`M26`'s node on the frozen file: the limitation validator, failing assertion at `:658`.** [358]
- **`M25`'s node on the frozen file: the truncated comparison, failing assertion at `:716`.** [359]
- **The forbidden-overreach case: nine verdict words searched over the serialized response, with a positive control.** [360]
- **The node that drives a real candidate write and refuses its continuation, and the substituted-snapshot refusal.** [361]
- The expansion, the visible unattributed gap, and the filter that narrows the display and never the comparison. [362]
- **The fixture and the governed contract it is registered under.** [363]
- **The two lane rows this leaf registered.** [364]
- **The fixture and the governed contract it is registered under.** [365]
- **The catalog digest re-pin that a new test module obliges.** [366]

## 260915-KS-L11 The Facet Suite, And The Ceiling It Was Written Against

This route gained **one unit-regression module and one governed support artifact**, and the split between
them is a capability decision rather than a size one:

- `mcp/tests/test_knowledge_facets.py` — **unit-regression** (row `mcp/tests/test-evidence-lanes.toml:71`),
  **17 nodes**, hermetic: temporary directories, in-process APSW databases built through the production
  application seam, and one recorded generation-2 fixture.
- `mcp/tests/facet_test_support.py` — the shared harness, registered as an **artifact**
  (`shared-support` / `internal-canonical` / `unit-regression` / `in-process`) under the contract
  `knowledge-facet-cases`, with exactly one declared consumer. It owns the two things no single case can:
  one **admitted** candidate (whose provenance comes from the admission) and one **recorded** dataset whose
  serialized page and result digests were measured on the base revision **before this leaf existed**.

**The case ceiling is why the module carries loops rather than parametrizations, and that is a cost stated
rather than hidden.** The unit population's declared budget had twenty slots left when this leaf landed and
the repository's own record forbids a KS leaf from raising it, so the per-subtype and per-endpoint-kind
variants are driven *inside* the case that owns their property, with every assertion naming the subtype or
kind it is about. What that costs is independent failure attribution between variants of one property; what
it preserves is every clause, and a population that runs at all — an over-budget population raises
`UsageError` and executes zero tests. The population was then **1250 unit cases against the
`unit_case_budget = 1250`** ceiling, with integration at 322 — the measurement taken at this leaf's own
candidate. The master's owning seat has since raised the pair to `unit_case_budget = 1500` and
`integration_case_budget = 400` at the later `260915-KS-L24` candidate, so the ceiling this section is
titled after no longer reads the same; see that section below.

**This leaf is the one that renders the earlier leaves' byte-identity claim checkable.** The recorded fixture
is built from generation 2's own recorded DDL with fixed identities and a fixed authorship instant, and the
case compares the shipped read's serialized page and result against constants measured before the leaf
existed — so "`KS-R07@v1`'s selection did not move" is a before/after observation rather than a
self-consistency check. The same fixture's dataset digest is asserted equal to its pre-leaf value.

**Three registry touch-points a new test module obliges, and this leaf paid both sides of each:** its lane
row, its path in the relevant artifact's `consumers` list, and the evidence-catalog digest re-pin
(`LIFECYCLE_CATALOG_SHA256` → `19ed0525…`, counts **13 contracts / 54 artifacts**) in
`mcp/tests/test_dependency_ownership_ast_helpers.py`, plus the new artifact's own contract row for the
support module. Missing any one of them is a hard collection error rather than a quiet gap.

**Two honest limits travel with this suite and neither is coverage:**

- **Completeness of the run is host-dependent and was reported as such.** The brief's literal combined
  command does not execute on this host because five anyio-affected modules fail to *import* under
  `filterwarnings = ["error", …]`; the leaf quotes the run **with** the documented `-W
  "ignore::DeprecationWarning"` override (the pre-existing D-7 defect routed to L9) and states both facts
  rather than one. Its own module passes 17/17 without the override.
- **The two checks the leaf did not run are named**: the contract-scoped memory-quality operation with the
  `curator_coherence` authority (the curator seat's step), and `--certify`.

- **The byte-identity node: the shipped page and result compared against digests measured before this leaf existed.** [367]
- **The exact facet page, the empty-but-real selection, the incompleteness refusal and the damaged-seal refusal.** [368]
- **The harness that owns the admitted candidate and the recorded fixture.** [369]
- **The governed contract and artifact this leaf registered, with its one declared consumer.** [370]
- The catalog digest re-pin a new test module obliges. [371]
- The lane row this module is registered under. [372]
- **The unit ceiling this route's suites collect against, cited as the pinned key and value — the L11 suite was written against 1250, the `260915-KS-L24` candidate raised it to 1500, this candidate's owning seat raised it again to 1600, the merge onto the moved super line raised it to 2200 over the merged 2035-case population, `260915-KS-L21` raised it to 2300 over its own measured 2206-case candidate (six cases past 2200, past which `pytest_collection_finish` runs no unit case at all), and `260918-TSIP-L7` raised the pair to **3000 / 600** by developer decision on 2026-09-19, and `260918-TSIP-L13` raised it again to **4000 / 1000** by a second developer decision on 2026-09-20 — which is what `pyproject.toml:278-279` declares now.** [373]
- **The refusal an over-budget population raises, which is why the loops live inside their cases.** [374]

## 260915-KS-L24 The Coherence Tool States Its Own Publication Inputs

This route's final-certification module is where the curator-coherence request contract is pinned, and
this leaf is the one that made the tool state its own inputs:

- **18 new cases in `mcp/tests/test_final_full_memory_coherence_certification.py`**, which grows 943 ->
  1190 lines. Nine parametrized items drive one omitted publication member each, so no member is
  accidentally satisfied by another's presence; one case drives all nine omitted; a positive control
  asserts the declaration equals the request model's own field order **and** that a nine-member request
  validates; one case drives the real `_prepare` and asserts its summary text; one extends the shared
  declaration in a scratch request model and asserts the new member reaches **both** messages with
  neither text edited; three parametrized items cover `status`/`prepare`/`validate`, plus one
  multi-field forbidden refusal that includes `judgments`; and one pins the byte-identical
  `freeze_snapshot` message.

- **What the cases protect is a message, and the message is the requirement.** `publish` required nine
  non-`None` request members while two of them (`semantic_requirement_revision`, `delivery_attempt`)
  were declared `default=None`, were **not** returned by `prepare`, and were **not** named by the
  refusal. Two leaves of this master read that refusal as an impassable tool defect and carried an
  unpublished coherence authority as an external blocker (`notes/DISCLOSURES.md` D-11). The request
  model now refuses by naming the missing members and the read actions name the publication-only field
  they received, so these cases are what stops the message from drifting back.

- **The suite stayed inside the budget raise this master's owning seat made.** This candidate collects
  **1268 unit cases against `unit_case_budget = 1500`** and **322 integration cases against
  `integration_case_budget = 400`**; the raise is the owning seat's change and not this leaf's delivery,
  and the 18 cases consume 18 of the 250 unit slots it added. The module is at 1190 of the repository's
  1200-line rail, so the next leaf that adds curator-coherence cases there must split it first.

- **The card's own `_affected_plan` / `_coherence` / `_evidence` coordinates moved by this leaf.** The
  three import insertions shifted every definition below them by nine lines; the module's card now
  carries the measured extents rather than the pre-leaf ones.

- The publish refusal names the one omitted member, for each of the nine. [375]
- The all-nine refusal names every member in declaration order. [376]
- The positive control binds the declaration to the request model's own field order. [377]
- The prepare text is asserted from the real `_prepare` path. [378]
- A member added to the declaration reaches both messages with neither text edited. [379]
- The sibling refusal names the supplied member for each read action. [380]
- The multi-field refusal names every supplied field in model order, `judgments` included. [381]
- The freeze branch keeps its own named refusal. [382]

## 260915-KS-L14 The Detection Suites, The Registry Rows They Obliged, And Two Re-Scoped Facet Cases

This route gained **two new unit-regression modules and no new governed artifact**:

- `test_knowledge_detection_signals.py` — **28 collected cases from 20 definitions**, one of them a
  nine-parameter construction table over every required field of a detection signal. It measures a typed
  record's own construction boundary: the declared field-set review against the closed conclusion-name
  list, an extra conclusion-shaped field refused, a verdict written into the prose field refused, the
  closed and versioned condition vocabulary, the granularity refusal that stops a whole-file change
  standing for a span change, the three declared input sets with their three distinct refusals, the
  declaration/omission agreement checked in both directions, retention refused at a destination that
  cannot retain, currentness that marks a run stale without relabelling it, the predating-dataset refusal
  with both generation numbers as facts, and generation 4's additive rule asserted as the prefix equality
  `GENERATION_4.tables[: len(GENERATION_3.tables)] == GENERATION_3.tables`.
- `test_knowledge_detection_runs.py` — **19 cases**. It has two halves and says so: a synthetic half that
  builds union items, family memberships and anchor resolutions so each condition is provoked exactly, and
  a store half that opens a real detection store and drives `record_detection_run`/`read_detection_run`
  through it. One case runs a **real** two-snapshot comparison through the shipped application seam, so
  the walk is shown consuming real comparison output rather than a shape invented beside it.

**The registry touch-points, and the one this leaf did not pay.** A plain test module needs a lane row, and
both modules were added to `unit-regression` in `mcp/tests/test-evidence-lanes.toml` — a two-line insertion
that shifts every later line of that file, which is why this route's and other routes' citations to it
moved. The governed-artifact side is the interesting one: the run module uses the **already-registered**
`diff_scope_test_support` and `read_scope_test_support` fixtures rather than a third support module, so
this leaf added **no artifact and no contract** — only two `consumers` rows in
`mcp/tests/evidence-lifecycle.toml`, and the counts stay at **13 contracts and 54 artifacts**. The pinned
catalog digest in `test_dependency_ownership_ast_helpers.py` therefore had to be **re-pinned deliberately**
(`c6956899…`), with the reason written beside the constant rather than the value changed silently.

**Two shipped facet cases were re-scoped, not deleted.** Appending generation 4 falsified exactly two
assertions in `test_knowledge_facets.py`, both of which stated the *shared* substrate's membership as a
closed list this leaf legitimately grew. Each keeps its protected property and gains the replacement fact:
the seam-registry case now states the three groups the registry declares — the internal conformance kind,
the eight facet kinds and the two detection kinds — and states the facet half *more* precisely than before
by asserting `KIND_SCHEMAS[kind] == {FACET_RECORD_SCHEMAS[kind]}` for each of the eight; and the
generation case now asserts the registry is `[1, 2, 3, 4]` with `GENERATION_3` still a member at
`user_version == 3` and `CURRENT_GENERATION is GENERATIONS[-1]`, so the created generation is named as
"the newest registered one" rather than pinned to a literal the next generation would falsify. Every
generation-3-specific assertion in that case is unchanged. Both carry a `RE-SCOPED for KS-R14@v1`
paragraph in their docstring saying what changed and why.

**One pre-existing defect is reported here rather than worked around.** The literal combined-suite command
`pytest mcp/tests -q` collects four errors in `mcp/tests/test_static.py` from a third-party `anyio`
deprecation escalated by the repository's warning filters; the module is untouched by this leaf, and the
documented `-W "ignore::DeprecationWarning"` override is what makes the same command green (1637 passed,
306 subtests). Both facts are stated in the leaf's worker report rather than one of them.

- **The signal suite's 28 cases, including the nine-parameter required-field table and the two halves of "a conclusion is unrepresentable".** [383]
- **The generation-4 additive rule asserted as the prefix equality it is, with the appended table, its key tuple and its two triggers.** [384]
- **The run suite's scenario/control case, the case that consumes a real shipped comparison, and the sealed-sequence case.** [385]
- **The run module's lane row.** [386]
- **The signal module's lane row.** [387]
- **The diff-comparison contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [388]
- **The diff-comparison contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [389]
- **The diff-comparison contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [390]
- **The read-scope contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [391]
- **The read-scope contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [392]
- **The read-scope contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [393]
- **The read-scope contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [394]
- **The read-scope contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [395]
- **The read-scope contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [396]
- **The deliberately re-pinned catalog digest, with the reason written beside it and the counts unchanged.** [397]
- **The two re-scoped facet cases and the `RE-SCOPED for KS-R14@v1` paragraphs that state what changed.** [398]
- The L37 lane registrations the fail-closed manifest requires, one per new module (both rows moved again with the KS-L2 and KS-L3 insertions: the pause suite to row `:253` and the publication guard to row `:294`). [399]
- The L37 lane registrations the fail-closed manifest requires, one per new module (the pause suite's row is at `:253` and the publication guard's row is at `:294`; three registry insertions moved this file — `:120`, `:201` and `:267` — not two). [400]
- The L27 pane-authority proof, its fixture import from the sibling sweeper suite, and the lane registration the fail-closed manifest requires. [401]
- **260913-LCA-L8:** the nine exact-consumer rows `mcp/tests/test_terminal_blocker_reasons.py` adds to the evidence registry under the `synthetic-test-evidence-candidate` contract. [402]
- **260913-LCA-L8:** the declaration that gives the new module ownership of the ambient-role runner for targeted selection — the `REPOSITORY_TEST_INPUT_CONSUMERS` entry for that runner, which is the list the claim is about. [403]
- The governed-artifact registration and exact two-consumer list this leaf added. [404]
- The read fixture and its registered contract. [405]
- The two integration-lane rows the read's boundary and path modules occupy. [406]
- **The fixture and the governed contract it is registered under.** [407]
- **The two lane rows this leaf registered.** [408]
- **The diff-comparison contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [409]
- **The diff-comparison contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [410]
- **The read-scope contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [411]
- **The read-scope contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [412]
- **The read-scope contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [413]
- **The read-scope contract whose consumer list gained the run module (the consumer row is the third entry of that block).** [414]
- **The binding suite's generation-5 append, its identity-column scan and the two `CHECK` constraints read as text.** [415]
- **The shipped-literal identity asserted per shared fact, and the same claim asserted in the reverse direction so the shipped vocabulary cannot acquire a citation member.** [416]
- **The bound closure refusing with the bound reached and no items and no counts, and the result that states no semantic completeness.** [417]
- **The boundary suite's fallback catcher, the rewritten-document case, and the store's own unique-key refusal.** [418]
- **The retention cases measuring both directions of the read-back, and the destination proven outside the enclosure and the archive by construction.** [419]
- **The unit lane row this leaf inserted into the alphabetical knowledge run.** [420]
- **The integration lane row this leaf opened, and the governed contract whose consumer list gained the boundary module.** [421]
- **The integration lane row this leaf opened, and the governed contract whose consumer list gained the boundary module.** [422]
- **The consumer rows the two modules added, the deliberately re-pinned catalog digest whose counts are unchanged, and the provenance paragraph that states the consumer-only change.** [423]
- **The second registry the two modules' path literals registered in: the ambient role runner's declared test-input consumers.** [424]
- **The seam-registry case re-scoped a second time so the union names this leaf's own group constant rather than being trimmed back, and the generation case re-scoped to the structural sequence.** [425]

## 260915-KS-L17 The Composition Suites, The Registry Rows They Obliged, And Two Re-Scoped Facet Cases

This route gained **two new unit-regression modules and no new governed artifact**:

- `test_knowledge_family_composition.py` — **18 cases**, hermetic over temporary directories and
  in-process APSW databases driven through the real admitted destination. It owns the *write* shape:
  the closed command union and its six record tables, the value-boundary policy refusal, the appended
  generation 5 and `descends_from`, a genuine generation-2 and generation-4 dataset that refuses a
  composition write, the authored edge with **unrepresentable** non-family endpoints, the declared
  unique tuple, the revision-altitude owning route and the explicit ungoverned state, the immutable
  context and its successor, and the one shared cycle rule at both check levels.
- `test_knowledge_family_composition_boundaries.py` — **8 cases**. It owns the *boundary*: the
  shipped selection compared **by value** with composition edges present and absent (two seeds, every
  preserved field equal, table counts confirming the edges are the only difference), the call-site
  derivation that no shipped read path consults the composition table, the declared-policy traversal
  reporting its version and widening nothing else, an unknown/a malformed/a not-permitted policy each
  refused **by name**, a traversal past its declared bound **refused rather than truncated**, every
  pre-existing family revision keeping its sealed `payload_digest`, the R07 escalation artifact's
  recorded subject and effect scope, and the read-only application seam end to end.

**26 collected cases across the two modules**, and one structural fact a reader of the builder's own
narrative would get wrong: the projection's absent-state assertions are driven **inside the seam
case** (`test_the_application_seam_is_read_only_carries_the_operation_and_moves_no_selection`, 8
definitions in that module), not by two separate cases of their own. The case count is what the
collection measures; the case *names* in the leaf's implementation rationale are not a second
population.

**The three registry touch-points a new test module obliges, and which this leaf paid:**

1. a lane row each in `mcp/tests/test-evidence-lanes.toml`, inserted mid-list under
   `unit-regression` — which is **why every later line of that file shifted by two** and other
   routes' citations into it had to move with it;
2. `consumers` rows in `mcp/tests/evidence-lifecycle.toml` — three of them, for
   `knowledge-facet-cases`, `knowledge-generation-cases` and `knowledge-read-scope-cases`, because
   the two modules build their admitted candidate through the facet leaf's helpers and read their
   graphs through the generation and read-scope harnesses rather than through a third fixture of
   their own;
3. the catalogue digest in `mcp/tests/test_dependency_ownership_ast_helpers.py`, **re-pinned
   deliberately** with the reason written beside it.

The counts stay **13 contracts / 54 artifacts**, because this leaf adds **no artifact and no
contract**. The measured digest of `mcp/tests/evidence-lifecycle.toml` on this candidate is
`2505cc7dd6eb52f9ab96bb61b25bf11ed1de50db72371d058524290c419d9eeb` and the constant in the rail
carries exactly that value; **the leaf's own report records a different, stale digest for the same
re-pin, which appears nowhere in the tree** — the file's measured bytes are the authority.

**Two shipped facet assertions were re-scoped upward, not loosened.** `test_knowledge_facets.py`
spelled a *closed list* where the protected property was a *derived* one, twice:

- the command-union case now unions this leaf's published `COMPOSITION_COMMAND_KINDS` and
  `COMPOSITION_WRITABLE_TABLES` instead of restating the members, and asserts
  `len(kinds) == 18 + len(COMPOSITION_COMMAND_KINDS)`. The stronger half is kept exactly:
  `set(_TARGET_CHECKS) == kinds` still fails the moment a command is added without a target check;
- the generation-registry case now asserts
  `[g.user_version for g in GENERATIONS] == list(range(1, len(GENERATIONS) + 1))` and the derived
  schema-name list, instead of `[1, 2, 3, 4]`. Every generation-3-specific assertion in it, including
  `GENERATION_2.fingerprint == PRE_LEAF_GENERATION_2_FINGERPRINT`, is unchanged.

No case was deleted, skipped, deselected, xfailed or weakened, and neither budget moved.

**Populations on this candidate**, measured with the host's required `-o "filterwarnings=ignore"`
override: **unit 1341** against the pinned `"unit_case_budget = 1500"`, **integration 322** against
`"integration_case_budget = 400"`, **combined 1663**. The baseline was 1315 / 322 / 1637, so this
leaf's delta is **+26 unit, +0 integration**, and it **raises no ceiling** and adds no entry to the
budget comment block in `pyproject.toml`.

- The composition suite's lane row, inserted mid-list under the unit-regression lane. [426]
- The boundary module's lane row, immediately after it. [427]
- **The facet contract whose consumer list gained both modules.** [428]
- **The read-scope contract whose consumer list gained the boundary module.** [429]
- **The read-scope contract whose consumer list gained the boundary module.** [430]
- **The read-scope contract whose consumer list gained the boundary module.** [431]
- **The read-scope contract whose consumer list gained the boundary module.** [432]
- **The re-pinned catalogue digest, with the reason written beside it and both counts unchanged.** [433]
- **The command-union case re-scoped a second time: it now unions this leaf's published constant instead of a literal, and keeps the target-check half exactly.** [434]
- **The registry case re-scoped to the derived fact the closed list stood in for.** [435]
- The unit ceiling this route's suites collect against, cited as the pinned key and value — 2200 since the merge onto the moved super line raised it over the merged line's 2035 collected cases, to **2300** by `260915-KS-L21` over its own measured 2206-case candidate, to **3000** with the integration ceiling to **600** by `260918-TSIP-L7`'s developer decision on 2026-09-19, and again to **4000** with the integration ceiling to **1000** by `260918-TSIP-L13`'s developer decision on 2026-09-20. [436]
- The integration ceiling, cited as the pinned key and value. [437]

## 260915-KS-L13 The Authored-Effect Suites, The Registry Rows They Obliged, And A Catalogue Pin That Does Not Move

`KS-R13@v1` adds two unit-regression modules for the authored-effect record group — the **change-set**
contract and the **effect-claim** contract — and, unlike the composition leaf before it, it adds **no new
contract and no new artifact**: both suites reach the shipped shared support their neighbours already use,
so the counts stay at **14 contracts / 55 governed artifacts** and only the catalog's *bytes* move.

**The registry touch-points a new test module obliges, measured on this candidate.** A new module needs a
lane row, and a lane member belongs **inside** its lane's own list — which is where the alphabetical
ordering lives — so both rows were inserted mid-file rather than appended, and every absolute line below
them shifted. That is the drift this leaf's own curation carries, and it is inherent to citing an
order-structured registry by line rather than a habit a convention can fix. The two `consumers` additions
are the same shape: a module path belongs inside that artifact's own list, so each insertion moved the
lines below it. Measured here: the lane rows are
`mcp/tests/test_knowledge_change_sets.py` and `mcp/tests/test_knowledge_effect_claims.py`, and the two
consumer lists that grew are the candidate-batch and generation-case shared supports — both **existing**
artifacts whose `consumers` lists gained one row each.

**The catalogue pin moves and the counts do not.** `LIFECYCLE_CATALOG_SHA256` was re-pinned against the
merged catalogue measured on this candidate, while `LIFECYCLE_CONTRACT_COUNT` and
`LIFECYCLE_ARTIFACT_COUNT` are unchanged at 14 and 55 precisely because no contract and no artifact was
added. A reader who saw the digest move and inferred a new artifact would be reading the wrong fact: what
moved is the artifact **records' contents**, not the set.

**The two shipped facet assertions re-scoped again.** A new member of the command union and a new
generation both land on cases that pin a closed set, and the shipped remedy is to re-derive them against
the merged union rather than to loosen them — each keeps its stronger half, and no case was deleted,
skipped or consolidated to make room. The unit and integration ceilings are unchanged (1600 / 400): this
leaf's own case counts stay under them and the merged line does too.

## 260915-KS-L16 The Family-Integrity Suites, The Registry Rows They Obliged, And A Catalogue Pin Whose Counts Did Not Move

`KS-R16@v1` adds three test modules and, like every leaf before it on this route, **no new contract and no
new artifact**: the suites reach the shipped shared support their neighbours already use, so the catalog's
*bytes* move and its *population* does not. The two unit modules are the registered-scope contract
(**14 cases**, `mcp/tests/test_knowledge_registered_scope.py`) and the pipeline contract (**17 cases**,
`mcp/tests/test_knowledge_family_review.py`), both in the `unit-regression` lane because what they measure
is a construction over recorded rows and a composition over typed records rather than a process or a
publication. The integration module (**7 cases**, `mcp/tests/test_knowledge_family_integrity_pipeline.py`)
drives the whole pipeline over two real databases and two real Git trees and publishes real bytes to a real
destination. Each module's docstring states, case by case, the failure it catches — a scope reported without
the policy it was built under, membership inferred from a path prefix, the read frontier leaking in as a
widening axis, a merge that silently dropped a contributing match, five statuses collapsed into one verdict,
a stale binding reused as if it were current, a retention claim resting on a path nobody read back.

**The registry touch-points a new test module obliges, measured on this candidate.** A new module needs a
lane row, and a lane member belongs **inside** its lane's own list — where the ordering lives — so the two
`unit-regression` rows were inserted mid-list among the knowledge suites rather than appended, and every
absolute line below them shifted. The `integration` row was appended at the end of its own list. The three
`consumers` additions are the same shape: a module path belongs inside that artifact's own list, so each
insertion moved the lines below it. Measured here: the lane rows are
`mcp/tests/test_knowledge_family_review.py` and `mcp/tests/test_knowledge_registered_scope.py` at
`mcp/tests/test-evidence-lanes.toml:93-94`, the integration row is
`mcp/tests/test_knowledge_family_integrity_pipeline.py` at `:265`, and the two consumer lists that grew are
the **existing** `diff_scope_test_support.py` artifact (one row) and the **existing**
`read_scope_test_support.py` artifact (two rows), both at `mcp/tests/evidence-lifecycle.toml`.

**The catalogue pin moved and the counts did not — and the value is the file's own digest.**
`LIFECYCLE_CATALOG_SHA256` was re-pinned to the sha256 of `mcp/tests/evidence-lifecycle.toml` as it stands
on this candidate, `143b0cf5c3a8432450f45072b7351057ba51fe6c386f65eb662c0ec4cb729ce6` — re-measured here by
hashing the file, which reproduces the constant exactly — while `LIFECYCLE_CONTRACT_COUNT` and
`LIFECYCLE_ARTIFACT_COUNT` are unchanged because no contract and no artifact was added. **Two records of
this re-pin disagree with the tree and the tree is the authority.** The source's own provenance paragraph
for this leaf says the counts "stay thirteen and fifty-four" while the two constants beside it read **14 and
64** (the merge onto the moved super line raised them), and the leaf's worker report records the re-pinned
digest as `b0bedae9071ec992cb011ba3e327ae67ff4c9728d9290bdfcdd50caff1263dd7`, a value that appears nowhere
in the tree. A reader who saw the digest move and inferred a new artifact would be reading the wrong fact:
what moved is one artifact record's `consumers` list and one support module's registration, not the set.

## 260915-KS-L20 The Two View/Projection Suites, And A Lane Manifest That Was Out Of Service

`KS-R20@v1` adds two test modules and no evidence artifact, and their split is the point: the unit module
holds the cases a store cannot help with, and the integration module holds the one scenario a store is
required for.

**`mcp/tests/test_knowledge_views_and_projection.py` — 30 cases, `unit-regression` lane, no database.**
The view vocabulary, the closed rule registry, the ordering pass and the projection writer are all pure
functions of their inputs, which is exactly why the classification rule can be tested without a store — and
why a renderer that opened one would not typecheck against the port in the first place. The cases are aimed
at failures rather than at lines: the class set closed at two members; an authored classification that
carries its author and is refused when it cites a rule; a mechanical classification that names its rule and
has no author; a class without its evidence refused rather than defaulted; an unregistered rule unable to
produce a classification; the registry admitting exactly one rule per ordering input; no registered rule
reading a name, a path or a score; an unadmitted ordering input refused rather than defaulted; every
admitted position naming the declared tiebreak rule; the two bounding-honesty directions (rows remaining
requires a continuation, complete forbids one); a continuation presented against another snapshot refused
with both identities named; a quantity with no meaning for a view saying so instead of reporting zero; the
curation queue keeping a work item free of any curator judgement; a no-consequence statement refused without
the class that produced it and an authored one naming the stored claim it is; a path that is not purely
destination-relative refused; a case collision naming both paths and both records; and the writer's
behaviours — the generation-one manifest, an unchanged orphan removed against a modified one retained, an
externally edited output reported and never overwritten, the explicit per-path authorization as the only
overwrite route, an escaping path refusing the whole plan and writing nothing, a collision refusing before
either output is written, a symlinked destination entry not followed while the rest continues, an
interruption leaving the destination exactly as it was, the destination never swept, an unreadable manifest
refusing rather than treating the destination as unowned, and the manifest refusing two owners for one path.

**`mcp/tests/test_knowledge_projection_vault_safety.py` — 7 cases, `integration` lane.** Its centre is
`test_the_vault_safety_contract_holds_for_all_eight_checkpoints_in_one_scenario`: one dataset, one
destination and one manifest lineage, driving all eight checkpoints **in sequence** and recording for each
the exact refusal or action and the resulting generation. A contract tested clause by clause is a contract
that fails in combination, so the case asserts `set(checkpoints)` equals all eight ids plus the manifest
generation — dropping a checkpoint fails the case rather than silently narrowing it. The interruption
checkpoint is inducible **deterministically** through `ProjectionHooks(before_publish=...)`, without a
sleep, a thread or a signal; that seam is the answer to the packet's Open Truth Gap, which recorded the
question as unverified. The other six cases carry the obligations that need real records: two byte-identical
runs of every view at one snapshot, the ordering differential, the records-unchanged differential, the
classification completeness scan (no third value and no empty class), the bounded-continuation walk
following the token to the next page, the regeneration proof that deletes every projection and re-projects
with an unchanged canonical digest, and the no-second-authority proof over `PRAGMA table_info` for every
table (no record table gained a content-address, digest or fingerprint column, and no record identity reads
the manifest's digest material).

**The registry cost this leaf paid, and one repair it made.** Two new lane rows (one inserted mid-list in
`unit-regression`, one appended to `integration`) and one `consumers` addition to the registered
`shared-support` artifact `mcp/tests/read_scope_test_support.py` — the integration module builds its
dataset through that fixture, and its `consumer_scope = "exact"` requires the list to equal the
source-derived consumer set, so the module had to be appended there. A `consumers` addition belongs inside
its list and therefore shifts every line below it; that drift is inherent to the registry and is what this
master's per-leaf citation repair exists for. The catalogue counts are **unchanged at 14 contracts / 64
artifacts** and `LIFECYCLE_CATALOG_SHA256` was re-pinned to the file's own measured sha256. The same change
repaired a pre-existing defect in a shared registry: `test_atomic_series_chain_pair_order.py` was committed
by `260915-CAPS-L25` with **no lane row** — 288 test modules against 287 rows — so `load_lane_manifest`
raised `test files without an explicit lane` and took the manifest out of service for its consumers, which
an ordinary `pytest mcp/tests` run does not reveal because the default selection never loads it. The row was
added in the lane where its neighbours sit; no lane was widened and no module moved between lanes.

## 260915-KS-L21 The Census Suite, Its Registered Fixture, And The Catalogue Pin That Moved To 15 / 65

`KS-R21@v1` adds two test modules and one registered evidence artifact, and the split between them is the
same shape the earlier knowledge leaves settled: the case module holds the contract cases, and the support
module holds the one dataset every case reads.

**`mcp/tests/test_migration_census.py` — 48 cases, `unit-regression` lane.** The population is aimed at the
census apparatus's *refusals* rather than at its arithmetic, because the arithmetic is small and the
prohibitions are what the packet spends its words on. The families each pin a distinct property: the inventory
taken over the **scope** rather than over the corpus (a source with no card is a row with
`inventory_state="absent"`, and a card whose declared source is gone still gets a row); the declared
`doc_type` as the authority for an artifact's kind, with the path consulted only when none is declared; the
metadata-table boundary that stops a body table becoming front matter; the four per-artifact parse outcomes,
including the deliberately unsupported generated-bootstrap form; the three reportable reference states with no
repair by resemblance and a mismatch reported as a fact with no field that could hold a curator's verdict; the
`N = T + F + U + P` accounting and its single eligibility rule (`assessable` and non-blank text, with
`unclassified` still counting); both the unique and the occurrence counts; all four slice axes each carrying
the full separation; the unmeasured coverage denominator (`C / K` is `not_measurable` until an independent
reviewer who is not the author is recorded); generation 9's additive composition against the generation it
descends from; the record kinds' declared columns carrying no content-address, digest or fingerprint; the
write path being the shipped candidate batch operation and no second writer; and the cutover's
prepared-and-not-executed boundary, where the criteria are predicates over a census result and an unmet
criterion is reported with its observed measure rather than a boolean. **It adds no integration case, and
that is a measured decision rather than an omission**: the census is a read over records the shipped batch
operation wrote, and the fixture composes it in-process, so the small integration lane has no boundary this
leaf would add protection for.

**`mcp/tests/migration_census_test_support.py` — the registered fixture.** It builds **one real candidate
dataset through the shipped write path**: the route writer for the fixture's recorded scope, then census
inventory-row, claim and disposition commands written through `change_knowledge_candidate`, so every identity
the cases read is one the real write path produced. That is the module's whole reason for existing as a
fixture rather than as an insert helper: the states the accounting has to separate — a claim with no
assessment, a curator's recorded verdict, a piece outside the cohort, one claim text recorded twice, an
artifact that did not parse and a card whose declared source is absent — **cannot be produced by inserting
rows**, and a fixture that did would be testing arithmetic against a state the real write path refuses.

**The registry cost this leaf paid.** One new `[[contract]]` + `[[artifact]]` pair
(`migration-census-cases` / `mcp/tests/migration_census_test_support.py`, `kind = "shared-support"`,
`fidelity = "local-composition"`, `consumer_scope = "exact"` with the case module as its single consumer) and
**one lane row inserted mid-list** in `unit-regression`, which shifts every line below it — the drift this
master's per-leaf citation repair exists for. The catalogue counts therefore move **14 / 64 → 15 / 65** and
`LIFECYCLE_CATALOG_SHA256` is re-pinned to the file's own measured sha256
`633b03ee16893ce3d0e838659d52f2bc609903f5c75b142eb41ca8c4fdabf5e6`; the pin lives in
`mcp/tests/test_dependency_ownership_ast_helpers.py` and is a deliberate re-measurement, not a relaxed
assertion.

**Three shipped assertions were re-scoped rather than deleted, and each re-scope strengthens the case.**
`test_knowledge_change_sets.py`'s generation-8 append case asserted `CURRENT_GENERATION is GENERATION_8`,
which is false the moment generation 9 lands; its property — that the authored-effect group's table still
declares what it declared — is now stated against the generation that actually carries it
(`CURRENT_GENERATION.user_version > GENERATION_8.user_version`) with the direct prefix check the case already
made. `test_knowledge_facets.py`'s seam-registry case and its facet-command case each gained the census
group's **own derived set** (`CENSUS_RECORD_KINDS`, `CENSUS_COMMAND_KINDS`, `CENSUS_WRITABLE_TABLES`) as a
term of their unions, so the subset, disjointness and partition assertions all cover the new group without an
edit and a fourth census kind would be answered by the census's vocabulary rather than by a literal here. **No
assertion was weakened, deselected or deleted, and no lane was widened.** The case population's growth is the
reason `pyproject.toml`'s `unit_case_budget` moved 2200 → 2300, measured rather than projected; that change is
recorded on the root route, not here.

## 260915-KS-L22 The Review-Surface Suite, Its Lane Row, And The Registrations It Obliged

`KS-R22@v1` adds one test module to this route and no support module:
`mcp/tests/test_knowledge_review_surface.py`, **25 collected cases** (`pytest --collect-only` measured on
this leaf's candidate: `25 tests collected`, unchanged by the leaf) marked `evidence_unit`, driving
the **real** adapter over the **real** two-snapshot comparison built by `diff_scope_test_support` and
reading the shipped L20 review matrix through `compose_review`. Nothing in it re-implements a read, a
comparison or a view, fakes a snapshot, or asserts a rendering it did not read back — which is what lets
the same cases carry both the panes' content and the surface's prohibitions.

The population is aimed at those prohibitions rather than at the surface's shape. One case walks the whole
serialized payload schema for any field a generated conclusion could occupy
(`FORBIDDEN_FIELD_NAMES`: summary, narrative, severity, score, verdict, recommendation and their
neighbours), so a field added anywhere under the payload is measured rather than only a field added at the
top. Another reads the vocabulary module for a record kind, a table statement or an insert of its own. A
third is the row-level form of "the surface stores nothing": both datasets' canonical row counts are taken
through the shipped `read_row_counts`, a full render plus a second render forced stale is performed, and
the counts are required to be identical afterwards. A fourth asserts that the adapter selects nothing by
rebuilding the shipped comparison independently and comparing the payload's binding digest, selector
digest, after-snapshot digest, selected claim ids and the two remaining counts to it value for value.

Each refusal state is a case, because a refusal rendered as a favourable default is the failure this
surface exists to prevent: an unassessed subject displays `unassessed`; a corpus with no evidence reads
`none_recorded` while source inspection stays available; a passing observation is an observation and never
an invariant satisfied; a detection signal carries its facts and scope limitations and no severity; a
missing role stays unclassified rather than being guessed from a name; a missing side is its own state and
never an empty string; and a stale comparison keeps its previous input labelled while disabling submission.
The closing group is the worked review of the design's §8 journey, read back at each step, including the
case that a stale assessment is never reused as a review of the new candidate. Two transport cases close
the set: the query parser admits exactly the two reviewable selector kinds, and the route serves the typed
result, answers `400` for a selector kind it does not admit, and answers `503` with no adapter wired.

**The registry cost.** One lane row was inserted mid-list in `unit-regression`
(`mcp/tests/test-evidence-lanes.toml`), which shifts every line below it, and **two** `consumers` lists in
`mcp/tests/evidence-lifecycle.toml` gained the module — `diff_scope_test_support.py`
(`knowledge-diff-cases`, whose comparison every case renders) and `read_scope_test_support.py`
(`knowledge-read-scope-cases`). Both artifacts declare `consumer_scope = "exact"`, so an unregistered
consumer is a hard collection error rather than a quiet gap. **The catalogue counts and digest did not move
for this leaf**: it adds no `[[contract]]` and no `[[artifact]]`, so the constants `260915-KS-L21` re-pinned
under the merge — `LIFECYCLE_CONTRACT_COUNT = 15`, `LIFECYCLE_ARTIFACT_COUNT = 65`, and the catalogue
sha256 `68a64207…` — remain the catalogue's own measured values. The case budgets likewise stand: the
module's 27 cases fit under the `unit_case_budget = 2300` that the L21 census raised over its own measured
2206-case candidate, and this leaf adds no integration case, so `integration_case_budget = 400` is
untouched.

- The new case module and its lane marker. [438]
- The forbidden-name set the whole payload schema is walked against. [439]
- The row-level proof that a full render stores nothing. [440]
- The case that the adapter selects nothing, compared value for value. [441]
- The transport case: typed result, a 400 and a 503. [442]
- **The two cases that were widened rather than added to: the unresolvable context now also proves the entry read refuses with the same code, and the pane-name case measures the entry list against the shipped comparison's own answer.** [443]
- The lane row this leaf inserted mid-list. [444]
- The lane row this leaf inserted mid-list. [445]
- The catalogue pin as this leaf left it — 15 / 65, the counts a consumer-only change does not move; `260918-TSIP-L10`'s `T129` reconciliation then added the two registered rows and moved the pair to **16 / 66**, which the constants read until `260928-MIK-L24`'s Thirty-third re-pin moved the artifacts to **80**. [446]
- The two `consumers` registrations the module obliged. [447]
- The catalogue pin the leaf did not move (16 / 66 then; the artifact count has read 80 since `260928-MIK-L24`). [448]

## 260915-KS-L23 The Terminal Leaf's Five Case Modules, The Split, And The Zero Integration Headroom

`KS-R23@v1` — the fix-and-certification pass over the accumulated `L10`–`L22` candidate — adds **five**
case modules to this route, splits one of the two it inherited at the 1200-line rail, and adds **no**
support module. Every row below is measured on the leaf's candidate (code base `c5a74a85`, the five
modules untracked and the split uncommitted), not copied from a report.

| Module | Lines | Lane row | What it pins |
| --- | ---: | --- | --- |
| `test_next_step_address_binding.py` | 198 | `:191` | the next-step hint describes the task the response addressed, never a process cursor (`D-13`) — and where the binder's reach stops, on the carrier that declares no address |
| `test_terminal_preview_expectation.py` | 116 | `:192` | a cleanup **preview** and the cleanup it previews agree about the same collection (`D-15`), while a genuine drift-snapshot failure still blocks with its reason |
| `test_knowledge_merge_right_side_writes.py` | 285 | `:193` | a right-side `UPDATE` is replayed (its key lives on the **old** side), and a replayed `route` reparent is judged by the acyclicity rule inside the merge's own transaction |
| `test_evidence_catalog_gate_boundaries.py` | 118 | `:195` | the catalog **byte pin** and the **consumer-completeness oracle** are two gates, shown in one run where the oracle is red and the pin's bytes are unchanged (`D-19`) |
| `test_curator_coherence_publication_discoverability.py` | 283 | `:194` | `KS-R24@v1`: the publication inputs are discoverable from the request, the refusal and the `prepare` text — and this is also the second half of the split below |

**The split, on properties rather than on line count.** `test_final_full_memory_coherence_certification.py`
stood at **1199 of the 1200-line hard limit**, so it was split into itself (**954** lines: the Gate-5
orchestration plus the shared fixture scaffold its sibling imports) and
`test_curator_coherence_publication_discoverability.py` (**283**: the publication-input cases). The
scaffold stayed in the module whose name the sibling imports, so
`from test_final_full_memory_coherence_certification import _CODE_TREE, _MEMORY_TREE, _affected_plan,
_coherence, _pair, _passing_checks` still resolves; no non-`test_` module was created, so the split
adds no `[[contract]]` and no `[[artifact]]`. **Both halves still assert what the whole did, measured
by collected node identity**: the pre-split module written from `git show HEAD:…` and the two halves
collect **23** node names each, and the sorted `diff` of the two lists is empty.

**The registry cost, and why it is smaller than a mid-list insertion's.** W1, the single writer,
**appended** all five lane rows to the end of the `unit-regression` list
(`mcp/tests/test-evidence-lanes.toml:195-199`) rather than inserting them in alphabetical position —
item 16's half (a), because a mid-list insertion shifts every row below it and stales every citation
into the file. Three `consumers` entries were appended to `mcp/tests/evidence-lifecycle.toml`'s
exact-scope lists for the two modules that reach a governed support module
(`test_knowledge_merge_right_side_writes.py` → `merge_case_test_support.py:1287`;
`test_evidence_catalog_gate_boundaries.py` → `_evidence_catalog_fixture.py:172` and
`test-evidence-lanes.toml:806`), and one **fourth** consumer was created by the item-16 case itself
(`test_memory_citation_resolution.py` → `test-evidence-lanes.toml:807`). The three remaining new
modules import only `agents_remember` and `pytest`, so they oblige no consumer row. The catalogue was
re-pinned **once** after every registry write; **the counts stayed 15 contracts / 65 artifacts** and
the digest moved only because the closing stamp edits the governed catalogue.

**The measured constraint every later edit in this route must respect.** The integration population is
exactly **400 / 400** against `integration_case_budget = 400` (unit is **2278 / 2300**), both
`--collect-only` runs exit `0` with no `UsageError`. That is legal and it means **zero integration
headroom**: `pytest_collection_finish` raises `UsageError` on an over-budget population, and the
message prints **above** the `N/M collected` summary, so an over-budget lane collects its cases and
executes **zero** of them while a `| tail -2` still reads green. All five new modules are in
`unit-regression` for that reason as well as item 16's.

- The five lane rows, appended rather than inserted. [449]
- **The four consumer registrations the two governed-support consumers and the item-16 case obliged.** [450]
- The catalogue pin's three constants as the landed line leaves them — **16 contracts / 66 artifacts** at `:44-45`, sha256 `ce292758…` at `:46`. A consumer-only change does not move the counts (the artifact count reads 80 since `260928-MIK-L24`'s fourteen new rows); the `T129` reconciliation that registered two rows did, from 15 / 65. [451]
- **The budget pair the populations are measured against, and the `UsageError` that makes an over-budget lane execute zero tests.** [452]
- The catalogue pin's three constants, whose **counts** a consumer-only change does not move (16 / 66 then; 16 / 80 since `260928-MIK-L24`). [453]
- **The split's two subjects and the scaffold that stayed behind.** [454]
- The scaffold the sibling imports, still exported from the kept module. [455]
- The publication-input cases in their new home, asserting the declaration is the model's own field order. [456]

## 260918-TSIP-L7 The Agreement Module, Its Lane Row, And A Budget Screen At The Declared Pair
Three of this route's files move in the agreement leaf, and the route gains one module.
- **`mcp/tests/test_memory_citation_agreement.py` is new** — 793 lines, 26 cases, sha256
`125d9cc414154e1c…` — and it is the durable form of this leaf: the two agreement classes no check in
the memory layer can see (`T52`, a construct that moved *inside* its cited range, and `T45`/`T56`, a
case budget written in prose), proven on trees the module builds and pinned on the leaf memory
worktree by **exact equality** so a repair that is not carried into the pin fails the suite. Its
lane row is `unit-regression` (`mcp/tests/test-evidence-lanes.toml:125-125`), so the default selection
collects it; the registry loader is what makes the row load-bearing, since the module was run before
its row existed and the loader refused it (*"test files without an explicit lane"*). A card exists
at `onboarding/mcp/tests/test_memory_citation_agreement.py.md`.
- **`mcp/tests/test_suite_budget.py`** now derives its stub from the declared pair instead of
restating it (`STUB_UNIT` / `STUB_INTEGRATION`, with a new case tying the stub to `pyproject.toml`),
so the screen can never again prove the boundaries of a ceiling nobody uses. Its card is
`onboarding/mcp/tests/test_suite_budget.py.md`.
- **`mcp/tests/test-evidence-lanes.toml`** gains one inserted lane row and nothing else:
**323 → 324** file lines, one pure insertion at new line **120**, **204** old file lines
renumbered (old 120–323 → new 121–324), and **305 → 306** module entries of which **114** are
static (new lines 1–119), **1** is the inserted row and **191** are moved. The consequence for the
memory layer is a citation worklist rather than a defect: on the leaf memory worktree **253 rows
across 52 documents** cite a range that crosses the insertion, enumerated by
`notes/reports/tsip-instruments/l7-lane-citations.py`. Those rows are the next curation pass's
worklist; this leaf adds one row and does not rewrite citations outside its own change set.
- **The declared case-budget pair is now `unit_case_budget = 4000` / `integration_case_budget = 1000`**
(`pyproject.toml:278-279`), raised from 2300 / 400 by the agreement leaf under a direct developer
decision — a **policy** raise, not a measurement. The populations this route collects against it are
**2433 / 2454** unit and **411 / 2844** integration, and `## Development And Certification Policy`
above now states the pair where it read `2300 / 400 when this was written`.
## 260915-KS-L31 The Knowledge-Conflict Case, Its Shared Harness, And A Pin That Moves Without A Population
This leaf's test delta is one case's worth of new coverage and two consumer registrations, and the shape to
read is how little of the registry moved for how much behaviour is now pinned.
**The case.** `test_worktree_sync.py` gained the proof that the knowledge merge adapter is *wired* rather
than merely callable. `_assert_knowledge_database_conflict_settles` builds a real three-commit branching
scenario over a knowledge database with disjoint valid edits on both sides, commits those datasets into the
memory worktree and the memory repository, and calls `SyncFixture.sync()`. The ordinary Git merge must stop
on the binary file, the transaction must route the three-way merge, and the sync must **complete** with
`state == "synced"`; the merged identity must differ from either side's, the three input datasets must be
byte-identical afterwards, and the resulting merge commit's two parents must be the two sides' own commits.
The test never calls `resolve_knowledge_merge_base` or `merge_resolved_knowledge_datasets`, which is exactly
the property that distinguishes a wired seam from a callable one.
**It shares one collected case with the shipped content scenarios, and that is a lane fact rather than a
style choice.** The integration lane sits at its declared ceiling of 400 collected cases; a further case
would breach it, and above the ceiling `conftest` raises and the lane then runs **zero** tests, which is
worse than either outcome it would report. So the shipped scenarios moved intact into
`_assert_memory_content_conflict_scenarios` and the renamed case drives both shapes.
**The registry delta is two consumer rows on one artifact, appended at the tail.** `test_worktree_sync.py`
now consumes `mcp/tests/merge_case_test_support.py` directly for that scenario, and
`mcp/tests/test_sync_parked_candidate.py` became a consumer of the same harness **transitively** — it imports
`SyncFixture` and friends from `test_worktree_sync` and was not itself edited, but the census derives
consumers from the import graph, so the new edge added the row. The populations do not move — **15 contracts
and 65 artifacts** — and the catalogue pin does, to
`825abfd65a17899cf1334d6191bd944d1f618347db7e599a44629f2bec910ef2`, which is what
`test_dependency_ownership_ast_helpers.py`'s `LIFECYCLE_CATALOG_SHA256` carries beside the unchanged counts.
**That value is the merge of the two re-pins**: the merged candidate carries both leaves' consumer rows —
`260915-KS-L30`'s one on `mcp/tests/snapshot_lifecycle_test_support.py` and this leaf's two on
`mcp/tests/merge_case_test_support.py` — so the digest is their merge while both counts stay **15 / 65**;
the L31 byte value this paragraph was written against was `f786c157…`, correct only at this leaf's own tip.
- The knowledge-conflict case: the sync completes, both sides survive, and the caller invokes no merge entry point. [457]
- The renamed collected case, the three knowledge-conflict scenario helpers this leaf added, and the shipped content scenarios it shares the case with. [458]
- The shared harness the direct row declares, and the two names this module takes from it. [459]
- The transitive row: a module that never mentions the harness and reaches it through its import of `test_worktree_sync`. [460]
- The two consumer rows the exact list carries at the tail, and the catalogue's own byte pin. [461]
## Update History — 260915-KS-L31

## 260915-KS-L42 The Reversed Orientation, And The Field Held To Its Own Derivation

**This route's impact is two already-collected cases and one new helper population, with no collected case added and neither ceiling raised (unit 2300/2300, integration 400/400).** `mcp/tests/test_worktree_sync.py` gained `_shape_delete_reference_reversed` (the arriving side removes the anchor the retained side's realization claim cites, so the arriving delta carries only the DELETE) and `_assert_unretractable_delete_reference_advertises_its_real_route`, driven from the existing `test_memory_merge_settles_content_and_knowledge_conflicts_in_the_transaction` through the module-level helper list. The case asserts the engine's diagnosis unchanged, `precondition == "no_arriving_insertion"`, `decisions == []`, `nextOperation=continue_sync_resolution` with no `knowledge_resolution` in `nextArgs`, a summary that says to restore the removed row, `cancelArgs` still carried — and then drives exactly what the response advertised and requires the state to change (`sync-resolution-incomplete`) with HEAD and all three inputs byte-identical. That last assertion is the acceptance a byte-identical repeat fails.

**The two unit-side cases changed with it, both inside already-collected cases.** `mcp/tests/test_knowledge_guarded_merge.py`'s `test_both_conflicting_edits_refuse_whole_and_preserve_every_input` gained the unit-boundary half — the two orientations' measured preconditions differ and `expressible_decisions` answers `("keep-left",)` and `()` respectively, while the code, attribution, next action and the row-less decision's own nameability are unchanged. `mcp/tests/test_knowledge_curator_ingest_list.py`'s `test_the_report_names_the_candidate_its_receipt_the_lane_and_the_exact_inputs` gained the assertion that holds `IngestReport.derived_identities` to the derivation (`uuid5(_INGEST_NAMESPACE, f"{repository_id}|invariant|E-named|")`) rather than to a phrase, which is the only form of that check that could have failed on the stale text.

**Open, not settled — named for the round-3 reviewer.** The `cancelArgs` probe (`notes/reports/2026-09-21-cycle-fix-verification/evidence/cycle02-orientation-fixed/cancel-probe.json`) returns `sync-operation-refused` in **both** orientations, including the INSERTED-row orientation round 2 verified as working, so the cancel half of the manual continuation is unproven in this fixture. The `continue` half is proven: driving the advertised call moves the state.

## 260915-KS-L43 Two Sibling Enclosures, One Reused Label, And The Ruled Semantics

**This route's impact is what its own case now proves**, and the change is a scope correction rather than a
retraction. `mcp/tests/test_knowledge_curator_ingest_list.py`'s `_cycle01_reused_label_identity` — the (h) point of
the L39 section above — asserted that a reused local label at two code baselines mints ONE invariant and ONE
revision. That was the code's behaviour and it was measured, so the case was not wrong about what it saw; it was
wrong about what the behaviour *meant*, and a reader took "the same label at a later baseline names the SAME
record" as "label reuse across independent tasks is handled". The developer's 2026-09-20 ruling is that a label
carries no identity meaning: two independent tasks numbering an entry `R-LOCAL` are two **creation operations**,
and the truth each authors gets its own canonical identity.

**What the case measures now.** A published baseline, then two sibling enclosures that differ in nothing but
their leaf id (`_cycle01_sibling_contract`, which is also what scopes the retry key), each ingesting one entry
labelled `R-LOCAL` with a different statement and a different cited construct; the assertion is that the two
stored invariant ids and the two stored revision ids **differ**, and that both snapshots publish. Continuity is
then proved the way the ruling names it: a third enclosure hands over `invariant_id=stored["left"][0]` and its
revision as predecessor, and must evolve *that* record — identity preserved, a distinct revision filed under it,
and a recorded predecessor edge readable from the database.

**Two cases in the same module were renamed**, because the rule they measure changed and a reader searching for
the old names would find nothing: `test_identity_is_derived_from_the_enclosure_so_a_second_run_is_diagnosable` →
`test_a_second_run_resolves_to_the_identities_the_operation_was_allocated` (a repeat is now a **replay** —
`batch_state == "replayed"`, zero commands, zero records written, the stored row sets byte-identical — rather
than a `batch_stale_precondition` refusal), and `test_dry_and_real_runs_report_the_same_written_rows_and_a_refused_run_reports_none`
→ `…_and_a_repeat_writes_none`. **The collected count is unchanged at 19**, which is the constraint the L39
section above records: the new protection is plain functions called from inside the existing case.

- The re-pointed case: two sibling enclosures, one reused label, distinct stored identities, and continuity by naming the stored id. [462]
- The replayed repeat, and the count that says nothing was written. [463]
- The allocation the case's distinct identities come from. [464]

## 260915-KS-L44 The Location Rows Are Asserted Against The Record, With A Rationale That Names No File

**This route's impact is two non-collected helpers and a fourth claim inside the mounted-family fixture, folded into cases that were already collected.** `mcp/tests/test_knowledge_views_and_projection.py` gained `_assert_the_invariant_realizations_carry_their_recorded_location` (`:1599-1634`) and `_assert_the_locations_are_recorded_not_read_out_of_the_prose` (`:1637-1665`), driven from `_assert_family_traversal_from_one_path` (`:1482`) and from `_assert_the_path_seed_selects_in_every_view` (`:1668`). **No collected case was added and neither ceiling was raised**: the unit lane stands at exactly 2300 / 2300 and the integration lane at 400 / 400, so every new assertion lands inside an already-collected case.

**The fixture variation is what makes the assertions mean anything, and it is the reason this leaf exists.** `_build_mounted_family_fixture` (`:886-1067`) now records a fourth realization claim at `src/batch.py` with `role="enforcement"`, `locator=LineRangeLocator(12, 18)` and rationale `LIMIT_RATIONALE` ("This implementation enforces the shared attempt limit."), on the same base revision as the other three — a location without a new member. Its rationale names **no file**, so a row that reports the path and the extent cannot have read either out of the statement; the original fixture's filename-bearing rationale is exactly what hid the loss. Both helpers compare each response row with `MountedFamilyFixture.expected_locations`, the **stored** answer the fixture built the claim from, rather than with the sibling view's answer, so the case cannot pass by two renderers agreeing with each other; the invariant helper additionally asserts that every `fact_kind="statement"` row carries `None` in `role`, `path` and `locator`. Mutation check as measured: reverting **only** the two production files makes the collected case fail with `KeyError: 'path'` at `:1620`; restored, 37 passed.

## 260915-KS-L47 The Tests Reconcile To The Response Choke Point, And The Merge Guard Gets Its Equal-Payload Variant

Two of this leaf's six changed files live under this route. **`test_knowledge_views_and_projection.py`**
reconciled two assertions to the shared response choke point, on the developer's ruling that the incoming
choke point wins and `None`-valued declared fields do not ride the wire: the stale
`selected["compatible"] is None` assertion (which raised `KeyError`, because the key is absent when its
value is `None`) is removed, and the no-run branch asserts `"selectedRunId" not in unnamed` rather than
`is None`, with the reasoning recorded inline. **`test_knowledge_guarded_merge.py`** gained the one
regression the master-exit audit kept: the equal-payload variant is built **inside** the existing
collected case `test_both_conflicting_edits_refuse_whole_and_preserve_every_input`, so it adds **no new
collected case** and neither lane's budget moves -- both shapes are one guarantee, that exactly one
insertion identity is refused whatever the two sides wrote in it. The variant's two sides are proved to
hold **identical** complete revision rows by a column-by-column comparison of both sides' stored rows
before the merge runs; without that step the case could silently drift back into re-testing the diverging
shape, which is what the sidecar previously claimed it already did and now states correctly. The verdict
is asserted by one extracted helper, `assert_insertion_collision_refused`, because the first version
pushed the case past the repository's statement rail and the doctrine is to extract a cohesive helper
rather than widen a limit or add a `# noqa`. `memory/knowledge/merge.py`'s `_independent_insert_refusal`
is byte-unchanged: no narrowing, no payload comparison, no blanket equal-payload exception, and the
selection is still by SQLite conflict code alone.

**260915-KS-L47 also adds the refusal-path regression for the review's before half.**
`test_knowledge_curator_ingest_list.py` gained one collected case,
`test_a_refused_rerun_leaves_the_reviews_before_half_at_the_fork_point` (`:1637-1734`), which drives
the operation a curator performs when a review asks for a correction — author the entry, publish over
the dataset the leaf forked from, then re-run the SAME hand-off entry with a changed statement. The
write plane correctly refuses that second run; the case measures that the publishing run still places
the fork point, that the refused run reports `not-placed` and leaves the half byte-identical to it,
and that the review still reads the addition `absent` before and `present` after over two different
digests. It seals a defect in this leaf's own baseline-capture repair: placement was gated on
`COMMITTED_BATCH_STATES`, which admits `no_change`, and an all-refused run reports `no_change` too
because the batch-level state falls back to it when the batch never ran — so the refused re-run
re-placed the before half from the bytes captured at the top of the run, which after the leaf
published over its own fork point are the **published** dataset. The guard now also requires
`report.committed` to be non-empty. A new collected case was required rather than a fold, because the
guard it protects lives in `cli/knowledge_ingest.py` and not in the module that would otherwise have
carried the assertion.

## 260921-ICR-L1 The Source-Endpoint Cases, And The Manifest Row They Inserted

This route gained **one** module, `mcp/tests/test_knowledge_review_source_endpoints.py`, and its footprint
in the two evidence registries is deliberately small: **one lane row and two consumer rows, no artifact and
no contract**.

**The module is the production-composition evidence for `ICR-R01@v1`.** Its eight cases build a real leaf
enclosure, a real linked Git worktree and real commits under `tmp_path`, and then drive the real
resolution, the real capture owner, the real comparison, the real route and the real leaf change-set views
— no injected resolution, no fake index and no prebuilt payload. What they protect, one case each: the
bound endpoints with the real Git index byte-identical before and after the capture; the whole candidate
reached, with the `HEAD`-to-unstaged population **measured** as a different population; a capture input
that moves before publication refused by name with both identities; the capture owner's own mid-capture
head check surfaced as that same refusal; a moved code head naming exactly the side that moved; the
committed range bound to the **recorded** commits and unmoved by a later commit; an unrecorded code
endpoint refused by name without the live head appearing in the message; and an unrecorded memory half
emptying only itself.

**The registry footprint is one inserted lane row plus two appended consumer rows.** In
`mcp/tests/test-evidence-lanes.toml` the module is a `unit-regression` entry inserted mid-list in the
alphabetical knowledge run — between `test_knowledge_review_surface.py` and
`test_knowledge_requirement_reference_contract.py`, at `:105` — which shifts every row and lane key below
it by one; in `mcp/tests/evidence-lifecycle.toml` it joins the two existing shared-support artifacts it
composes (`mcp/tests/diff_scope_test_support.py` and `mcp/tests/read_scope_test_support.py`) as two
appended consumer rows, so the catalog populations stay **16 / 66** and only the deliberately re-pinned
digest moves. Both facts are recorded in full on those files' own cards.
**The consequence for this route's cards is a pure move, and it was taken in the same pass:** every claim
row in this document that cites `mcp/tests/test-evidence-lanes.toml` at or below the insertion point, and
every claim row that cites `mcp/tests/evidence-lifecycle.toml` below its two appends, was re-derived from
the anchor's real position rather than carried; the generated history entries in this document's history
sections keep the ranges they were written with.

- **The module itself: the eight cases and the production composition they drive.** [465]
- **The lane row this leaf inserted, and the row it displaced.** [466]
- **The two consumer rows the module added, on the two shared-support artifacts it composes.** [467]
- The deliberately re-pinned catalogue digest beside the counts this leaf did not move. [468]
- **The production owners the cases measure: the delegated resolution, the capture owner, and the recorded-range resolver.** [469]

## 260921-ICR-L19 The Read-Files Suite Gains The Published-Intent Half, And A Case That Measures A Carrier

**This route's impact is fourteen cases added to an existing module — no new module, and no registry row
(ICR-R19@v1).** `mcp/tests/test_read_ar_files.py` grew from 334 to 736 lines, and the additions are two
classes on the same route: `PublishedIntentRouteTests` (twelve cases at the application layer, driving
`read_ar_files_tool` with a real dataset written at the memory layer's own name) and
`PublishedIntentMountedRouteTests` (two cases driving the **mounted** `read_ar_files` route over a real
coordination tree, so the block is measured through the call an agent actually makes rather than only
beside it). Neither `mcp/tests/test-evidence-lanes.toml` nor `mcp/tests/evidence-lifecycle.toml` was
touched: the cases extend a module the manifests already register, so the lane and artifact populations
are unmoved by this leaf.

**One case measures an instruction rather than a behaviour, and that is deliberate.**
`test_the_carrier_uses_the_field_spellings_the_payload_actually_returns` derives the item and count
vocabulary from a **real page** and requires the retrieval carrier to name those spellings, while
requiring the camelCase variants — which nothing produces — to be absent. A carrier that spells a field the
payload never carries is a reader's dead end that no behavioural case can catch, because the code is right
and the instruction is wrong; the case reads the authored root skill through the module's `CARRIER`
constant, which resolves `skills/c-04-retrieval-strategy-router/SKILL.md` from the test file's own
location. It is a carrier-parity measurement, not a behavioural one.

- **The two new classes and the fixtures they drive, including the `_selection()` narrowing helper the type-checked call sites need.** [470]
- **The headline route case: the ordinary read returns the published intent at its exact identities while the source bytes ride in the same payload.** [471]
- **The cases that measure the named absences and refusals rather than an empty success.** [472]
- **The carrier-parity case: the vocabulary is derived from a real page, and the unproduced camelCase variants are required to be absent.** [473]
- **The mounted-route class, which measures the block through the call an agent actually makes. Since MIK-R24 an unconverted memory tree is read as `legacy-format` there, so its two cases assert that, with and without a database.** [474]


## 260921-ICR-L2 The Review Suites Gain The Inventory's Cases, And The Comparison's Suites Gain Its Measurement

**Route meaning changed: two of this route's suites now carry R02's evidence, and the shared diff
fixture gained the independent, byte-safe Git observation they compare against.** Four modules changed
and none was added, so no lane row, artifact row or contract row moved and the catalogue counts are
untouched.

- `mcp/tests/test_knowledge_review_source_endpoints.py` (integration) gained `build_endpoint_fixture(directory, *, datasets=False)` and `EndpointFixture.task_request` — a leaf with a recorded base, a live worktree and a captured candidate and **neither dataset half** — and four cases: the task-context review lists the complete inventory with no knowledge at all (through the payload **and** the real HTTP route with no selector parameters); the production inventory keeps an unusual filename (`src/tab<TAB>newline<LF>name.py`) as the address it expands by; non-text and mode-changed paths are listed rather than dropped; and a non-UTF-8 pathname leaves the review openable with a **measured and partial** inventory (the real route answered 500 before the fix). The module is now 938 lines and carries a **fifth** case the sync added when leaf `260921-ICR-L5`'s landed unreadable-half refusal met this leaf's task-context entry: `test_a_task_context_review_states_a_damaged_half_and_still_lists_the_source_inventory` (`903-938`) proves the damaged half is *stated* and the complete source inventory is still listed. It sits against the same 900-line soft signal and 1200-line hard rail.
- `mcp/tests/test_knowledge_diff_boundaries.py` (integration) gained `InventoryFixture`/`build_inventory_fixture` — one real repository whose base and candidate carry an edit, a deletion, an addition, a tab+newline name, a binary file, a moved symlink target, a mode-only change, a file→symlink type change and a submodule pointer change — and six cases that assert population, per-path status, filename identity, one entry per renderability kind, `unavailable` versus a measured empty set (with its control), the paths-only partial rendering and the non-UTF-8 byte form. The module is now 1170 lines; that is a **master ruling**, not an oversight (hard rail 1200, file-size gate green, consolidation stays, and the next leaf that adds cases there should extract first).
- `mcp/tests/test_knowledge_review_surface.py` (unit-regression) gained `reviewed_selector` (the narrowing that keeps the optional selector out of the pyright rail), one added assertion in the transport case (the "omit both" answer), and two cases: a knowledge-only change leaving an openable review with a **measured empty** inventory beside an untouched comparison, and the structural rule that an inventory which could not carry a name is partial by construction.
- `mcp/tests/diff_scope_test_support.py` gained one helper, `independent_changed_records(root, before, after)` — `git diff --name-status -z` read through the **production** runner, deliberately a different Git question from the inventory's own `--raw -z` and deliberately not the module's strict fixture helper, because a pathname is bytes and a name that is not valid UTF-8 would raise there. It adds no governed artifact: it lives in the module already registered as `knowledge-diff-cases`.

- **The no-datasets fixture shape and the selector-less request the task-context cases use.** [475]
- **The four cases R02 is measured by through the real composition and the real route.** [476]
- **The real-repository fixture and the six cases that measure the inventory against every change class.** [477]
- **The module already registered as `knowledge-diff-cases`, to which the review suites' independent observation was added.** [478]
- **The independent byte-safe observation the review suites assert against, added to that module.** [479]
- **The independent byte-safe observation the review suites assert against, added to the module already registered as `knowledge-diff-cases`.** [480]
- The shared diff fixture that module is registered under, which this change did not alter. [481]
- **The two new unit cases, the narrowing helper the optional selector obliged, and the selector-kind transport case.** [482]
- The lane rows that keep the changed modules in the certifying collection — unchanged by this leaf, because no module was added. [483]


## 260921-ICR-L10 One Lane Row, Three Consumer Rows, And The Paging Cases Over Real Two-Snapshot Fixtures

`260921-ICR-L10` (`ICR-R10@v1`, complete bounded pagination) adds one ordinary unit module to this route,
`mcp/tests/test_review_bounded_pagination.py`, with **twelve** cases, and registers it in exactly three
places. Its lane row is a `unit-regression` entry appended mid-list at line 163 of
`mcp/tests/test-evidence-lanes.toml`, between `mcp/tests/test_retry_selection.py` above and
`mcp/tests/test_review_state.py` below, which is why every manifest entry at or below that line reads one
line lower than the accounts above record it. Its three exact-scope consumer rows are appended to the
`mcp/tests/evidence-lifecycle.toml` artifacts it consumes, and `LIFECYCLE_CATALOG_SHA256` is re-pinned to
`b4d4a7f9…` as this leaf's deliberate re-pin; the population is unchanged at sixteen contracts and
sixty-six artifacts.

The module is hermetic — every case builds its own two-snapshot fixture through the public store
operations under `tmp_path`, plus two real Git trees that borrow each other's object store — and it reads
every page back through the **real HTTP transport**, so the counts it asserts are the owners' own numbers
rather than a re-derivation of them. Two dataset sizes are walked end to end: the union of the pages is
the collection's own total exactly once, with no duplicate and no loss, and a cursor issued before a
deliberate generation change is refused with the new-generation action while the response is the first
page of the comparison that is there now.

One boundary is stated rather than asserted: a rendered source-location row may name a claim whose item
arrives on another page, because `ICR-R08@v1`'s traversal resolves the recorded relationship line from
the store, so the case asserts the item-window partition and the rendered-row union and deliberately does
not assert page attribution of a location row. Browser keyboard traversal and the assembled acceptance
remain `ICR-R24@v1`'s and `ICR-R25@v1`'s.

## 260921-ICR-L26 The Subject-Isolation Cases: One New Module, Thirteen Cases, One Lane Row, Four Consumer Rows

`260921-ICR-L26` (`ICR-R26@v1`, subject and comparison isolation) adds **one** ordinary unit module,
`mcp/tests/test_knowledge_review_subject_isolation.py` (925 L, **thirteen** cases, all in the
`unit-regression` lane), and registers it exactly as the census says it must be registered: one lane row
in `mcp/tests/test-evidence-lanes.toml` and four `consumer_scope = "exact"` rows in
`mcp/tests/evidence-lifecycle.toml` (`curator_coherence_test_support.py`,
`fixtures/repository_profiles/node/package-lock.json`, `diff_scope_test_support.py`,
`read_scope_test_support.py`). No artifact and no contract is registered, so the population stays at
sixteen contracts / sixty-six artifacts and the ownership gate re-pins the catalog bytes to
`4d874fb54c627549db098177caa477040e09ca63c7ae2cba2246bd1390a338e0`.

**The module measures the attribution half through the production composition**, never against a
prebuilt payload: `cli.dashboard.serving_collaborators` over one real leaf enclosure whose records are
produced by their owning operations — five assessments through the curator-coherence publication, a
detection run holding two signals, an evidence claim and a verification observation through the
application evidence writer, and an authored open question through the admitted candidate batch — plus a
source movement after publication so the same assessment is measured once as this generation's record
and once as historical input of the previous one. The thirteen properties: a sibling's assessment as
labelled context and never the selected subject's (with no disposition in the row); the selected
subject's own record `direct` with the binding its label names; an unreachable subject counted and not
displayed; an unresolvable binding shown with its references; a previous generation `historical` with
the tree it examined; a malformed revision binding `unresolved`; identical treatments at every page
size; a `direct` sentence that cites ICR-R07 only when R07's published list carries the record; the
complete populations on the channels beside the pane's own; the signals and the claim attributed by
their own recorded bindings; the source inventory independent of the selection; and the two vocabulary
refusals.

**The case module is the evidence for the three fix-round findings**: the malformed revision binding
(F-V1), the page-independent classification (F-V2) and the honest `direct` basis (F-V6) are each pinned
by a case rather than described in prose.

## 260921-ICR-L12 The Committed-Leaf Cases And Their Registration

`260921-ICR-L12` (`ICR-R12@v1`) adds **one** case module to this route and one lane row plus three
consumer rows to the registration files that admit it: `test_historical_committed_leaf_review.py`
(637 L, eight cases) measures the packet's whole journey through the real production composition — a
real enclosure, a real linked worktree, R11's real freeze and reclamation owners, and the real HTTP
route, in this process and in a **fresh interpreter** — and never through a preconstructed payload.

**The eight properties, one case each.** The live frozen read and the cleaned read are the same served
**bytes**; a child interpreter sharing no state with the parent reconstructs the same bytes from the
coordination root alone; a **later task** that really commits and really moves the leaf's protected
source branch changes neither the bytes nor the provenance and never enters the inventory; a pre-feature
leaf exposes its recorded source range with its absence stated as a typed absence; a generation that
recorded **no** intent half states that absence as its own fact on the pane and on both refusals; a
recorded range the repository cannot resolve answers `candidate_unresolved` rather than the intake
defect's code; expected content that no longer resolves is unavailable on its own channel with the
record's deletion statement; and a leaf that recorded neither a comparison nor a landed commit is still
refused by name.

**The registration is complete rather than permissive.** The module is `evidence_unit` and its lane row
sits in `mcp/tests/test-evidence-lanes.toml` (the collection gate refuses an unregistered module); the
three `consumer_scope = "exact"` rows in `mcp/tests/evidence-lifecycle.toml` are the diff-scope fixture,
the read-scope fixture and the unit-regression list, exactly the rows the census's own finding names;
and `test_dependency_ownership_ast_helpers.py` re-pins the catalog to
`4ab067e360c7807c3051ad71058c09058225f1e9155e7111da6e95c73cac0258` (the Twenty-third), with the
population unchanged at **sixteen contracts / sixty-six artifacts** and no artifact delta.

## 260921-ICR-L17 The Surface Test Module Gains One Case And Changes One Helper

`260921-ICR-L17` (`ICR-R17@v1`) touches `test_knowledge_review_surface.py` in two places and no other
module on this route.

- **`render` asks the way a refresh asks.** The helper's `previous_binding_digest` no longer travels as a
  keyword beside the request — the adapter's keyword is gone — so it copies the request with
  `model_copy(update={…})` and calls the composition without a parallel argument. The docstring records
  that as the contract it is.
- **One new collected case** (`30 → 31`) drives the real route over `TestClient`: the transport admits the
  parameter and hands it to the port on the request, the composition answers `stale` with the carried
  identity labelled and submission disabled **while the rendered comparison keeps its own digest**, a
  plain read carries nothing and is `current`, and a malformed spelling is a `400` naming the offending
  input.


## 260921-ICR-L15 Measured assessment currentness

`260921-ICR-L15` (`ICR-R15@v1`) rewrites **four governed test sources** on this route and adds no module,
no lane row and no contract. What it measures is one property from four sides: an assessment is reported
**current** only against a measurement that was actually taken.

- `mcp/tests/test_knowledge_review_surface.py` — **1395 → 1475 lines.** The currentness case named
  `test_a_measured_matching_binding_reports_the_assessment_current` was renamed to
  `test_only_a_complete_matching_measurement_reports_the_assessment_current`, and its input is now a
  **real measurement** instead of an empty mapping.
- `mcp/tests/test_review_assessments.py` — **880 → 1028 lines.** New closed-vocabulary cases (the
  disposition vocabulary is exactly its declared values and an out-of-vocabulary value is refused rather
  than coerced) and new count-partition cases (a declared count that contradicts the records it claims
  to partition is refused).
- `mcp/tests/test_knowledge_review_evidence_channels.py` — **796 → 966 lines.** A new case measures the
  currentness collection's **exactly three product states** (`recorded` / `none_recorded` /
  `unavailable`, with a measurement nobody performed refused loudly rather than rendered as
  `not_measured`), and the measurement case was renamed to
  `test_the_composition_measures_the_bindings_it_reads` so its name states what it measures.
- `mcp/tests/test_curator_review_assessment_publication.py` — **948 → 988 lines.** The integration half
  of the same property: the publication route's cases now drive the matching measurement the renamed
  unit case measures.

Each module's own card carries its per-case citations; this route's rows into those modules were
re-derived where this leaf's line changes left them stale, and the entry below records that accounting.

## 260921-ICR-L22 The Rebinding Cases, Their Two Registrations, And Three Deliberate Re-Pins

`260921-ICR-L22` (`ICR-R22@v1`, managed Git recovery rebinding) adds **two** governed test modules and
registers both in the same change set, because this suite refuses an unregistered module at collection:

- `mcp/tests/test_review_sync_rebinding.py` — **942 lines.** The sync-side cases: **seven** cases in
  `ManagedSyncReviewRebindingTests` (`:381`), driving the production `worktree_sync` tool, the real
  transaction, the real binary-stage knowledge merge, the real publication owner and the real
  comparison-generation owner, with the shared enclosure fixture `ReviewSyncFixture` (`:102`) and no
  injected resolution, payload or prebuilt record. It was extracted from `mcp/tests/test_worktree_sync.py`
  for the file-size rail rather than for a budget, and it keeps the module's own module-level helpers.
  One prose fact a reader should carry: the module docstring still says "the four cases" — the four it
  first carried out of the sibling — while the live module declares seven; a reader counting cases should
  count the declarations.
- `mcp/tests/test_review_sync_movement_read.py` — **356 lines.** The read-side cases: **five** cases in
  `LiveReviewMovementTests` (`:38`, cases at `:41`, `:104`, `:169`, `:227` and `:258`), driving the shipped
  `read_knowledge_review` over the enclosure the sibling owns rather than duplicating it — the same
  sibling-fixture pattern this repository's other case modules already use. The seam chosen is the one the
  production owners already have: *what the sync measured* beside *what the read says about it*.

**The registration, measured.** `mcp/tests/test-evidence-lanes.toml` gains both rows in the `integration`
lane at `:300-301`, immediately after `mcp/tests/test_worktree_sync.py` at `:299`; the two insertions move
every entry below them by two lines (`architecture-fitness`'s key `:304` → `:306`,
`provider-conformance`'s `:326` → `:328`, `stress-durability`'s `:342` → `:344`, `migration`'s `:344` →
`:346`, file extent **345 → 347 lines**), and the live lane census is **329** declared entries against
**329** `mcp/tests/test_*.py` modules on disk with **0 / 0** declared-but-absent and
present-but-undeclared. `mcp/tests/evidence-lifecycle.toml` gains **eight** consumer rows — both modules on
the same four exact-scope artifacts (`node/package-lock.json`, `merge_case_test_support.py`,
`diff_scope_test_support.py`, `read_scope_test_support.py`) — at `:802-803`, `:1307-1308`, `:1433-1434` and
`:1479-1480`, moving every line below each insertion by two (extent **1702 → 1710 lines**) while the
catalog's counted shape stays at **66 artifacts / 16 contracts**, so the artifact delta is exactly empty.
The closure change the census derived is the part worth naming: three of those rows **lost**
`test_sync_parked_candidate.py` and `test_worktree_sync.py` (their only route to them was the case module's
own import, which moved) and gained `test_review_sync_rebinding.py`, while `merge_case_test_support.py`
kept both and gained it — and the later split added
`test_review_sync_movement_read.py` to all four.

**The re-pins, and the chain they complete.** `mcp/tests/test_dependency_ownership_ast_helpers.py` carries
**three** new deliberate re-pins, because the leaf's own change set and its fix rounds each moved the
catalog's bytes again: `81a518b5…` (the value the constant carries at this leaf's base `e605822e`) →
`8ce61c57…` (the **Twenty-fourth**, the leaf's own three newly reached rows) → `7c8c1646…` (the
**Twenty-fifth**, fix round 1's module split) → **`d07c2f9d456b0f658228c91aecb2a1f3da8d13e2b6575b6b40b0b0d2ca165f6b`**
(the **Twenty-sixth**, fix round 3's read-side split, and the live value at `:46`, reproduced by
`sha256sum mcp/tests/evidence-lifecycle.toml` on the 1710-line file). The constant's docstring narrative
now starts at `:49` and the leaf's own three entries run `:49-108`, so the module is **782 → 842 lines**
and every line from the base's `:49` onward reads **+60** —
`test_repository_inputs_reach_their_supported_consumers` `:633` → `:693`,
`_assert_the_proof_is_selected_by_the_lane_manifest` `:690` → `:750`,
`_assert_the_governed_inventory_is_closed` `:703` → `:763` and
`_assert_the_catalog_kept_its_bytes_and_identities` `:723` → `:783`. `LIFECYCLE_CONTRACT_COUNT` and
`LIFECYCLE_ARTIFACT_COUNT` stay **16 / 66**, which is what makes all three re-pins consumer-list changes
rather than registrations.

## 260921-ICR-L31 Three Case Modules For The Family Review Context

The existing family-context suite drives real store-authored snapshots through application and HTTP composition. It covers direct family discovery, each revision’s own guarantee/roster, shared canonical members, genuine absent/no-family/unreadable states, partial walks and owner-bound cursor refusals. The value suite retains count, revision-membership and page-shape construction rules.

The population suite now proves that a new member retains its existing family before context and that a removed member cannot pin after context to a retained predecessor. Its revised history case checks independent memberless-head ambiguity, then separately requests an exact revision to inspect recorded history. Primary invariant operands, evidence and source inventory are asserted unchanged. Existing sparse-page/continuation cases remain; no test module or evidence-lane registration was added for this correction.

- New-member context preserves the independent family counterpart. [484]
- Removed-member context follows the real successor while old membership remains stored. [485]
- Genuine ambiguity and exact requested history are distinct assertions. [486]

## 260921-ICR-L29 The Bootstrap Cases: One Module, Fifteen Cases, One Lane Row, One Consumer Path

`260921-ICR-L29` (`ICR-R29@v1`) adds **one** ordinary unit module, `mcp/tests/test_knowledge_bootstrap.py`
(**1050** lines, **nineteen** cases, `pytest.mark.evidence_unit`), registered by one `unit-regression` lane row
in `mcp/tests/test-evidence-lanes.toml` and by exactly one consumer path added to the
`mcp/tests/fixtures/repository_profiles/node/package-lock.json` artifact in
`mcp/tests/evidence-lifecycle.toml`. `LIFECYCLE_CATALOG_SHA256` is re-pinned to `f3dd258c…` and the
contract/artifact counts are unchanged.

**What makes these cases different from an import test.** `knowledge-ingest` requires a leaf enclosure
contract, so before this leaf the only way a repository's knowledge could be written was by a task that
already had a worktree. Each case builds a **real coordination world** — a real code checkout, a real
external memory repository at `<coordinationRoot>/memory-repos/ar-<repo>`, and a real MCP settings
document — drives the shipped `agents-remember knowledge-bootstrap` through `main()`, and then compares
against something other than the run's own prose: the destination against the read route's own owner,
the identity against a read-back, the stored statements against the mounted read surface, and the
remaining-work manifest against the file on disk. The world contains **no contract file at all**, which
is what makes "no enclosure was fabricated" a measurement.

**The four cases the fix round added.** `:897` pins the staging-ownership refusal — another scope's
retained record must refuse by name with the destination untouched, and it is the case that fails when
that guard is removed; `:929` pins a narrowed resume that must still name the owed entry on disk; `:967`
pins a committed run that wrote nothing still refreshing the record; and `:1004` pins a carried entry
being **re-derived** against the run's own store read so it stops being owed once the dataset holds it.
The module's own docstring still opens "Fifteen cases" and does not name these four; the count that
matches the code is nineteen.

**The cases that exist because a false sentence about the store was reachable.** A refused publication
must not be reported as success: the batch commits, the publication is refused, and the entry is named
remaining against a location **measured** to hold no dataset (`storeState == "absent"`, `unmeasured ==
[]`). And a measured zero must not be collapsed into an unknown: the cleanup case removes a staging whose
candidate holds no authored revision, which is a measurement of emptiness rather than an assumption of
it. A third case asserts the destination is derived rather than accepted, by inspecting the argument
surface for any way to aim it.

## Exact population through bounded family pages

The family-population tests read expected membership and claim identities from the public authorship owners and follow actual HTTP continuations at fixed small bounds. They assert exact whole-walk coverage for content-only and claim-only pages, while primary knowledge, evidence, comparison identity and complete source inventory remain unchanged. The companion context-walk cases count unique membership identities instead of repeated sparse projection rows.

## Assessment history through public owners

The two assessment-history modules exercise real curator publication, normal comparison capture, cleanup/restart, pointer/source movement and explicit successor recovery. The repair cases cover nonempty judgment namespaces, confined aliases, pre-replacement integrity rejection, complete positive owner-channel provenance and either retained snapshot disappearing before copy. Existing comparison-generation assertions now check normal supplied owner availability; no extra test lane is introduced.

## 260921-ICR-L47 The Changed-Intent Summary Cases

[`test_review_intent_summary.py`](test_review_intent_summary.py.md) is new, registered in the
`unit-regression` lane of `test-evidence-lanes.toml`. Six hermetic cases pin the summary's count classes
(added/revised/removed as `+`/`−`, relationship-only typed apart, a shared member once per side, record-only
successors counted), `partial` for divergent heads, `unavailable` with no counts for absent knowledge, and
the route's 200-for-every-typed-state / 503-unwired idiom.

- The lane row. [487]
- The record-only successor case (L47-R1-F3). [488]
