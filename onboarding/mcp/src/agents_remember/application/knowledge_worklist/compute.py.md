# mcp/src/agents_remember/application/knowledge_worklist/compute.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**One worklist run (MIK-R08 definitions 5 and 8, rules 2 to 6).** `compute_worklist(inputs)` reads the
changed paths from the landed ICR change inventory, the renames from ICR's Git rename inference, runs the
one-pass scope, builds the `touched_invariant`, `stale_invariant` and `reached_family` items, the MIK-R11
`planned_untouched` items and the MIK-R06 `family_route_condition` items, marks every changed hunk linked
or unexplained and raises MIK-R10's `unexplained_hunk` / `unexplained_file` item for every unlinked change,
raises MIK-R14's `reconsideration_candidate` for every K_B decision alternative whose `reconsider_on` target
changed, and returns the `knowledge-worklist/v1` document with its digest. The run is a pure
function of its inputs.

## Code Commentary

### Logic

- **Inputs.** `WorklistInputs` holds the `CodeTrees`, the two `KnowledgeSide`s, the pairing, the
  `maintenance_scope` flag, the owner leaf and (MIK-R11) `expected_effects`, the leaf's declared
  `expectedKnowledgeEffects` as `Declaration`s, or `None` when it declares none, and (MIK-R10) `coverage`,
  K_B's onboarding routes and census statuses (`RouteCoverage`; `None` means every route is `pending`), and
  (MIK-R14) `coordination_root`, where requirement endpoints' owning tasks live (`None` resolves none; `leaf.py`
  passes the contract's root).
- **Changed paths and renames** (`_changes`): `tree_difference_observation` (ICR-R02) gives the entries;
  `git_rename_inference` (ICR-R08) gives the renames, because ICR-R02's inventory runs with `--no-renames`
  (architect ruling 3). An unavailable inventory, a **partial** inventory, or unavailable renames raise
  `WorklistIncomplete`; `_partial_detail` names the observation's own detail, every path that is not valid
  text (by `byte_form`) and every path with no content classification.
- **One-pass scope** (`_Run._scope`, steps 1 to 4; `_Run.document` calls it and assembles the items):
  1. classify every K_B entry at a changed path, or every K_B entry when `knowledgeMaintenanceScope` is set;
  2. compute the knowledge-side changes, and add to the classified set any entry classified only to decide
     a re-anchor whose class covers it;
  3. reach every K_B family with a member that has a `touched_invariant` item, or whose record changed
     (`_reached`);
  4. classify every K_B entry of those families' members (K_B and K_C membership, restricted to K_B
     invariants), once.

  `_scope` returns the knowledge changes, the touched invariants, the reached families and the stale
  invariants. `_first_entries` gives step 1's entry list, `_stale` the invariants with a `stale_at_base`
  entry, and `_scope_document` and `_entries_document` build the persisted `scope` and `entries`. This split
  was made by 260928-MIK-L06 at the merge with L11 (ruling 2026-09-29T23:14:41+02:00: `_Run.document`
  reduced to radon 10 or less by whichever of L06 and L11 landed second); the steps run in the same order
  and the worklist is unchanged (the worker's and reviewer's real-data preservation runs).
- **`Item.extra`** (MIK-R06): a registrant's further top-level fields, merged into `to_document` after
  `id`, `kind`, `subject` and `facts`. The route items use it for `satisfiedBy`; it is empty for every other
  kind, so their documents are unchanged.
- **Items.** `_touched` collects K_B invariants with a raising entry or a knowledge-side change.
  `_touched_item` carries each classified entry's facts, the added, retired and re-anchored entries, the
  record's K_B and K_C revisions, and the context (families on both sides, `linkedFrom` in K_C). Its
  identities are the raising entries' contents, the added, retired and re-anchored contents, and the record
  revisions only when the record changed; carried and untouched siblings are listed but excluded.
  `_stale_item` carries each stale entry's blob, B blob and both content identities. `_family_items` gives a
  `reached_family` per reached family (reasons `touched:<INV>` and `record-changed`) and per family of a
  stale invariant (reason `stale:<INV>`); `_family_item` lists the union of members with each side's revision
  and both sides' routes, and its identities are the members' `{ id, revision }` per side.
- **Gate linkage** (`_change`, definition 8): each changed path's text hunks are linked when a changed line
  hits a K_B entry's range at B or a K_C entry's range at C (`_spans`). Non-text changes (binary, symlink,
  submodule, type change, empty files) and the mode fact of a mode change are linked at `fileLevel` exactly
  when a `file`-locator entry on either side covers the path (`_file_covered`). An added or deleted text
  file is one whole-file hunk. **A delete-only hunk (`new_count == 0`) is linked only by a K_B range at B**
  (260928-MIK-L10, ruling 2026-09-30T01:56:39 Q2): it has no changed line at C, so L08's `hits_new`
  "strictly inside" extension no longer links it through a K_C range. This is the strict reading of
  definition 8 and a correction of L08's output: on ICR L47 exactly four delete-only hunks of
  `changeSetBar.tsx` flip `linked` from true to false; classification and every non-MIK-R10 item are
  unchanged. **The symmetric case was applied by MIK-R09 (260928-MIK-L09, the L10 N3 carry of ruling 03:24:28,
  gathered by the start decision 2026-09-30T13:15:47):** `_linked(hunk, base_spans, candidate_spans)` links a
  hunk only through the sides where it changes lines, so an insertion-only hunk (`old_count == 0`) is linked only
  by a K_C range at C, as a delete-only hunk is only by a K_B range at B. The change can only add
  `unexplained_hunk` items, never drop one; L32's lane docstring states the same per-side rule (review R1 F8).
- **Shared with the reviewer's lane (MIK-L32).** `_path_hunks` now only calls `code.change_hunks` (the body moved
  there verbatim), and `_file_covered` calls the module-level `non_text_linked(locator_kinds)` predicate (exported in
  `__all__`): a non-text change is linked exactly when a `file`-locator entry on either side covers the path. The
  reviewer's unexplained-changes lane (`review_lane_classification.py`) calls the same two functions, so its hunks
  and its "gate" linkage of a non-text change are the gate's own; the gate's output is unchanged (the L08, L10 and
  L14 worklist suites pass, and the reviewer's real-data agreement check matched every path).
- **Step 5, planned effects (MIK-R11, `planned_effects.py`).** After the items are built, the run calls
  `reconcile_planned_effects(inputs.expected_effects, base, candidate, inputs.owner)`: every
  `touched_invariant`, `stale_invariant` and `reached_family` item is marked `planning: planned | unplanned`,
  and each declaration no row of the leaf's history file delivers adds a `planned_untouched` item. The marked
  items and the new items are sorted together by `(kind, subject)` before the digest, so the digest covers the
  marks. Without a declaration every item is `unplanned` and nothing is added.
- **Step 6, family route conditions (MIK-R06, `route_conditions.py`).** `_route_items` passes
  `family_route_conditions` a `RouteInputs` (K_B, K_C, C's files, B's files, the run's rename map and the
  owner) and the families that have a `reached_family` item (touched, record-changed or stale-reached).
  Every returned condition becomes a `family_route_condition` `Item` with `satisfiedBy` in `extra`. In code
  order the route items join the item list before step 5 runs, so they are sorted and digested with the
  rest; they are not in `planned_effects`'s marked kinds, so they carry no `planning` mark.
- **Step 7, unexplained changes (MIK-R10, `unexplained.py`).** `_Run.document` computes the linkage once
  (`_linkage`), passes it with an `UnexplainedSides` (C, K_B, K_C, `inputs.coverage`, the owner) to
  `unexplained_items`, and adds the returned items to step 5's one sort by `(kind, subject)`; the planning
  marks are applied only to the knowledge items, never to these. The same linkage object is the document's
  `changes`, and `unexplained.summary()` is its `unexplained` key.
- **Step 8, reconsideration candidates (MIK-R14, `reconsideration.py`).** `_Run.document` binds the run's
  `Classifier` to a local (it was an inline argument of `_scope`) so step 8 can reuse it: it calls
  `reconsideration_candidates` with a `ReconsiderationInputs` (K_B, K_C, `classifier.classify_anchor`, the owner and
  `inputs.coordination_root`). The returned items join the one sort by `(kind, subject)` after the unexplained
  items, unmarked like them, and `reconsideration.summary` (every evaluated link) is the document's
  `reconsideration` key. L10 kept step 7, so L14 is step 8 (review F9, ruling 2026-09-30T05:31:11).
- **Document.** `state`, `incomplete`, `pairing`, `scope` (the flag, changed and unrepresentable path
  counts, classified count, class counts, reached families), `entries`, `changes`, `plannedEffects` (MIK-R11: `{declared: false}`, or
  `declared: true` with one entry per declaration, matched or not), `unexplained` (MIK-R10: `itemsByKind`,
  `openCount`, `unnecessaryRows`), `reconsideration` (MIK-R14: `links`, each evaluated link with its trigger or
  `null`, its class or endpoint and approval state, or `skipped: superseded`), `items` sorted by kind and subject, `kinds` (the registry) and `digest` (`worklist_digest` over state, items and incomplete).
  `incomplete_worklist` is the one representation of unreadable input: `state: incomplete`, the named
  input, no items. A `CodeReadError` during the run becomes `incomplete` naming `C`; since MIK-R09 a
  `subprocess.SubprocessError` (a Git call that failed or timed out) becomes `incomplete` naming `git`, through the
  exported `git_failure(error)` (the L03 review N2 carry, decision 2026-09-29T19:15:20), never an unhandled error.

### Conventions

- Everything is sorted and no timestamp is written, so identical inputs give identical bytes (rule 6).

### Invariants And Boundaries

- **Every changed hunk is either linked or unexplained, and every unexplained one raises an item** (step 7,
  MIK-R10): an unlinked hunk or non-text change keeps an `unexplained_*` item in the list until a
  disposition answers it.
- **An unreadable or partial input makes the run incomplete, never silently complete** (architect ruling
  on review R1, F4: a partial ICR inventory is `incomplete` and names the paths; it never falls back to
  file-level linkage).
- **Stale items never widen the classification.** A `stale_invariant` reaches its families without
  classifying their members unless step 3 already reached them.
- **Only K_B families are reached**; a family or invariant present only in K_C raises nothing of its own.
- **A mode change keeps its text hunks** (review R1 F5): they are linked as for any text change, and the
  mode fact is added separately at file level.
- No verdict, severity or cause is recorded (Exclusions).
- **One hunk and one non-text rule for the gate and the reviewer (MIK-L32):** `change_hunks` and `non_text_linked` are
  the only definitions; part of the candidate invariant recorded on `review_lane_classification.py.md`.
- **`plannedEffects` is outside the digest** (the worker's design, unchallenged by review): the items
  already carry what it summarises. The `planning` mark is inside it, so every converted worklist's digest moves
  against a worklist persisted before MIK-R11; that consequence is carried to L09 (ruling F4,
  2026-09-29T22:35:34+02:00).
- **Stage numbering with MIK-R06** (ruling F7, resolved by L06, which landed second): the route stage is
  step 6 in the docstring; L11's marking and the one sort run over the combined items, and route items stay
  unmarked.
- **A link anchor is classified by the run's own classifier** (step 8 reuses the local), so it takes exactly an
  entry's class, yet it never joins `entries` or the scope counts.
- **Route items never rewrite anything** (MIK-R06 Exclusions): the run only reports the conditions and the
  mechanical suggestion; no route is changed automatically.

### Todos

- The family route chain (MIK-R05) is not in the context yet; context holds families and `linkedFrom` only.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- Step 7 in the docstring: the linkage marking, the delete-only rule and MIK-R10's items. [1]
- The schema name. [2]
- One item, its ID from the registry, and `extra` for a registrant's top-level fields (MIK-R06 `satisfiedBy`). [3]
- The run's inputs, with MIK-R10's route coverage and MIK-R14's coordination root last. [4]
- The one representation of unreadable input. [5]
- Inventory and renames; a partial inventory is incomplete, naming the paths. [6]
- The document: the items of every step, one sort and the digest. [7]
- Steps 1 to 4, split out of `document` at the L06/L11 merge. [8]
- The persisted `scope` and `entries`. [9]
- Step 3: families reached by a touched member or a changed record. [10]
- The `touched_invariant` facts and identities. [11]
- The `stale_invariant` item. [12]
- The `reached_family` items and their member identities. [13]
- The leaf's declarations, one input of the run. [14]
- Step 5: marks, `planned_untouched` items, one sort over both, and the summary. [15]
- Step 6 in the docstring: the route conditions of reached families and of killed routes. [16]
- Step 6: the route items, with `satisfiedBy` carried in `extra`. [17]
- Step 7: one linkage, the unexplained items in the one sort, `changes` and `unexplained`. [18]
- Step 8 in the docstring: MIK-R14's reconsideration candidates. [19]
- Step 8: the run's classifier bound once and reused; the candidates join the one sort; the `reconsideration` key. [20]
- A hunk links only through a side where it changes lines: a delete-only hunk only by a K_B range (L10 ruling Q2), an insertion-only hunk only by a K_C range (MIK-R09, the L10 N3 carry). [21]
- A Git call that failed or timed out is `incomplete` naming `git` (MIK-R09). [22]
- The insertion-only symmetry at the gate. [23]
- Gate linkage, text and file level. [24]
- The non-text predicate the gate and the lane share (MIK-L32). [25]
- A body edit raises one invariant and its family and carries the rest of the file. [26]
- A comment between functions raises nothing; one inside raises. [27]
- A binary change touches a file anchor and links at file level. [28]
- A partial inventory is incomplete and names the path. [29]
- A mode change keeps its hunks' linkage and adds the mode fact. [30]

### Cross-Repo References

No meaningful cross-repo references found: the run reads one code repository and two parsed memory sides.

No cross-repo boundary is crossed by this file.
