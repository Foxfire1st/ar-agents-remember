# mcp/src/agents_remember/application/knowledge_worklist/compute.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/compute.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:18:54+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `../overview.md` |

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
  unchanged. The symmetric case (an insertion-only hunk still linkable by a K_B range through `hits_old`)
  was not changed; it is carried to L09 as a note (ruling 03:24:28 N3).
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
  input, no items. A `CodeReadError` during the run becomes `incomplete` naming `C`.

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Step 7 in the docstring: the linkage marking, the delete-only rule and MIK-R10's items. | "7. marks every changed hunk" | mcp/src/agents_remember/application/knowledge_worklist/compute.py:22-26 |
| The schema name. | `WORKLIST_SCHEMA` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:100-100 |
| One item, its ID from the registry, and `extra` for a registrant's top-level fields (MIK-R06 `satisfiedBy`). | `Item`; `item_id`; `extra` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:120-144 |
| The run's inputs, with MIK-R10's route coverage and MIK-R14's coordination root last. | "class WorklistInputs:" | mcp/src/agents_remember/application/knowledge_worklist/compute.py:147-162 |
| The one representation of unreadable input. | `incomplete_worklist` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:169-183 |
| Inventory and renames; a partial inventory is incomplete, naming the paths. | `_changes`; `_partial_detail` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:199-212; mcp/src/agents_remember/application/knowledge_worklist/compute.py:215-225 |
| The document: the items of every step, one sort and the digest. | `document` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:233-292 |
| Steps 1 to 4, split out of `document` at the L06/L11 merge. | `_scope`; `_first_entries`; `_stale` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:294-321; mcp/src/agents_remember/application/knowledge_worklist/compute.py:323-331; mcp/src/agents_remember/application/knowledge_worklist/compute.py:333-340; mcp/src/agents_remember/application/knowledge_worklist/compute.py:302-310 |
| The persisted `scope` and `entries`. | `_scope_document`; `_entries_document` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:342-352; mcp/src/agents_remember/application/knowledge_worklist/compute.py:354-363 |
| Step 3: families reached by a touched member or a changed record. | `_reached` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:387-395 |
| The `touched_invariant` facts and identities. | `_touched_item` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:405-440 |
| The `stale_invariant` item. | `_stale_item` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:442-460 |
| The `reached_family` items and their member identities. | `_family_items`; `_family_item` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:462-479; mcp/src/agents_remember/application/knowledge_worklist/compute.py:481-500 |
| The leaf's declarations, one input of the run. | `expected_effects` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:157-157 |
| Step 5: marks, `planned_untouched` items, one sort over both, and the summary. | `reconcile_planned_effects`; `plannedEffects` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:249-249; mcp/src/agents_remember/application/knowledge_worklist/compute.py:286-286 |
| Step 6 in the docstring: the route conditions of reached families and of killed routes. | "evaluates the family route conditions" | mcp/src/agents_remember/application/knowledge_worklist/compute.py:20-21 |
| Step 6: the route items, with `satisfiedBy` carried in `extra`. | `_route_items`; `family_route_conditions`; `satisfiedBy` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:502-525 |
| Step 7: one linkage, the unexplained items in the one sort, `changes` and `unexplained`. | `unexplained_items`; "\"unexplained\": unexplained.summary()" | mcp/src/agents_remember/application/knowledge_worklist/compute.py:253-253; mcp/src/agents_remember/application/knowledge_worklist/compute.py:287-287 |
| Step 8 in the docstring: MIK-R14's reconsideration candidates. | "8. evaluates every K_B decision's" | mcp/src/agents_remember/application/knowledge_worklist/compute.py:27-28 |
| Step 8: the run's classifier bound once and reused; the candidates join the one sort; the `reconsideration` key. | "reconsideration = reconsideration_candidates("; "classifier = Classifier(inputs.code, inputs.base, renamed)"; "\"reconsideration\": reconsideration.summary" | mcp/src/agents_remember/application/knowledge_worklist/compute.py:237-238; mcp/src/agents_remember/application/knowledge_worklist/compute.py:259-275; mcp/src/agents_remember/application/knowledge_worklist/compute.py:288-288 |
| A delete-only hunk is linked only by a K_B range (ruling Q2). | "hunk.new_count > 0" | mcp/src/agents_remember/application/knowledge_worklist/compute.py:560-560 |
| Gate linkage, text and file level. | `_change`; `_path_hunks` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:534-564; mcp/src/agents_remember/application/knowledge_worklist/compute.py:566-569 |
| The non-text predicate the gate and the lane share (MIK-L32). | `_file_covered`; `non_text_linked` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:584-598 |
| A body edit raises one invariant and its family and carries the rest of the file. | `test_a_body_edit_raises_its_invariant_and_family_and_carries_the_rest_of_the_file` | mcp/tests/test_knowledge_worklist.py:336-361 |
| A comment between functions raises nothing; one inside raises. | `test_a_comment_between_functions_raises_nothing_and_one_inside_raises` | mcp/tests/test_knowledge_worklist.py:364-379 |
| A binary change touches a file anchor and links at file level. | `test_a_binary_change_touches_a_file_anchor_and_links_at_file_level` | mcp/tests/test_knowledge_worklist.py:451-466 |
| A partial inventory is incomplete and names the path. | `test_a_partial_change_inventory_makes_the_run_incomplete_naming_the_paths` | mcp/tests/test_knowledge_worklist.py:673-686 |
| A mode change keeps its hunks' linkage and adds the mode fact. | `test_a_text_change_with_a_mode_change_links_its_hunks_and_the_mode_fact` | mcp/tests/test_knowledge_worklist.py:689-699 |

## Cross-Repo References

No meaningful cross-repo references found: the run reads one code repository and two parsed memory sides.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): **body update for MIK-R32.** A Logic bullet and an Invariants bullet record that `_path_hunks` now calls `code.change_hunks` and `_file_covered` the exported `non_text_linked`, the two functions the reviewer's lane shares, with the gate's output unchanged. One row added (`_file_covered`; `non_text_linked`); the `_path_hunks` range re-measured by the exact shift (`564-578` → `566-569`); the other moved rows were re-pointed by the installed fixer (its bullets kept, since no claim was reworded). No verification stamp was advanced.
- 2026-09-30T12:07:03+00:00: Generated citation repair: `WORKLIST_SCHEMA` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:100-100. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T12:07:03+00:00: Generated citation repair: `expected_effects` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T12:07:03+00:00: Generated citation repair: "hunk.new_count > 0" repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:560-560. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): **body updated for MIK-R14.** Purpose, Inputs (`coordination_root`), a new Step 8 bullet (the classifier bound to a local and reused through `classify_anchor`; the candidates in the one sort; step 8 because L10 kept step 7, review F9, ruling 05:31:11), the Document bullet (`reconsideration`) and an Invariants bullet. The `WorklistInputs` row is reworded and re-measured (`138-151` → `145-160`; the class gained `coordination_root`). The `_family_items`/`_family_item` row, which the fixer's normalisation left with a stale third range (`441-458`, now inside `_stale_item`), is reduced to its two functions. Two rows added. The other rows were projected or normalised by the installed fixer, and its generated bullets are kept (none of their claims was reworded). No verification stamp was advanced.
- 2026-09-30T10:05:11+00:00: Generated citation repair: `WORKLIST_SCHEMA` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:98-98. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:05:11+00:00: Generated citation repair: `_reached` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:385-393. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:05:11+00:00: Generated citation repair: `_stale_item` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:440-458. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:05:11+00:00: Generated citation repair: `expected_effects` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:155-155. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:05:11+00:00: Generated citation repair: `unexplained_items`; "\"unexplained\": unexplained.summary()" repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:251-251; mcp/src/agents_remember/application/knowledge_worklist/compute.py:285-285. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:05:11+00:00: Generated citation repair: "hunk.new_count > 0" repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:558-558. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): **body updated for MIK-R10.** Purpose, Inputs (`coverage`), the new Step 7 bullet (`unexplained_items` over the one linkage, joined to step 5's sort, unmarked), the Document bullet (`unexplained`) and the linkage bullet (a delete-only hunk is linked only by a K_B range: ruling 01:56:39 Q2, a correction of L08's output; the insertion-only symmetry carried to L09, ruling 03:24:28 N3). **Two reopened claims re-read and reworded:** the docstring row (its anchor "that marking raises nothing here" is gone from the code; it is re-anchored on "7. marks every changed hunk") and the `WorklistInputs` row (the class gained `coverage`; its range had been rewritten by an earlier curator pass's generated repair, so the row is re-read and re-anchored on the line-exact quote "class WorklistInputs:"). The invariant "the marking raises nothing here" is replaced: every unexplained change now raises an item. Two rows added. Other rows were projected or normalised by the installed fixer, or re-pointed by exact line shift. No verification stamp was advanced.
- 2026-09-30T02:32:44+00:00: Generated citation repair: `_scope`; `_first_entries`; `_stale` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:273-300; mcp/src/agents_remember/application/knowledge_worklist/compute.py:302-310; mcp/src/agents_remember/application/knowledge_worklist/compute.py:312-319. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:44+00:00: Generated citation repair: `_scope_document`; `_entries_document` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:321-331; mcp/src/agents_remember/application/knowledge_worklist/compute.py:333-342. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:44+00:00: Generated citation repair: `_reached` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:366-374. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:44+00:00: Generated citation repair: `_stale_item` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:421-439. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:44+00:00: Generated citation repair: `expected_effects` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:148-148. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:44+00:00: Generated citation repair: `reconcile_planned_effects`; `plannedEffects` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:239-239; mcp/src/agents_remember/application/knowledge_worklist/compute.py:266-266. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:32:44+00:00: Generated citation repair: `test_a_text_change_with_a_mode_change_links_its_hunks_and_the_mode_fact` repointed to mcp/tests/test_knowledge_worklist.py:689-699. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): recorded MIK-R06's step 6 (`_route_items`, `family_route_conditions` over the reached families, `satisfiedBy` through the new `Item.extra`), the split of `_Run.document` into `_scope`, `_first_entries`, `_stale`, `_scope_document` and `_entries_document` (ruling 2026-09-29T23:14:41+02:00), and the resolved stage numbering (ruling F7). Purpose and the invariants reworded; five rows added; the `Item`, `_changes`, reached-family, step-5 and linkage rows re-measured by hand against the new code (the fixer declined them: the code moved unevenly). The fixer's seven bullets above cover rows whose claims were not reworded, so they are kept.
- 2026-09-29T23:15:28+00:00: Generated citation repair: "that marking raises nothing here" repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:24-24. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c718f054d6f4666aac0289d7878fea56fae3168ee18c9058b74578d7e9f7b0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:15:28+00:00: Generated citation repair: `WorklistInputs` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:129-140. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c718f054d6f4666aac0289d7878fea56fae3168ee18c9058b74578d7e9f7b0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:15:28+00:00: Generated citation repair: `incomplete_worklist` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:147-161. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c718f054d6f4666aac0289d7878fea56fae3168ee18c9058b74578d7e9f7b0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:15:28+00:00: Generated citation repair: `_reached` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:343-351. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c718f054d6f4666aac0289d7878fea56fae3168ee18c9058b74578d7e9f7b0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:15:28+00:00: Generated citation repair: `_touched_item` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:361-396. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c718f054d6f4666aac0289d7878fea56fae3168ee18c9058b74578d7e9f7b0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:15:28+00:00: Generated citation repair: `_stale_item` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:398-416. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c718f054d6f4666aac0289d7878fea56fae3168ee18c9058b74578d7e9f7b0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:15:28+00:00: Generated citation repair: `expected_effects` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:139-139. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c718f054d6f4666aac0289d7878fea56fae3168ee18c9058b74578d7e9f7b0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:47:51+00:00: Generated citation repair: "that marking raises nothing here" repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:22-22. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:47:51+00:00: Generated citation repair: `WORKLIST_SCHEMA` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:73-73. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:47:51+00:00: Generated citation repair: `_reached` repointed to mcp/src/agents_remember/application/knowledge_worklist/compute.py:300-308. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): recorded MIK-R11's step 5 (the `expected_effects` input, the `planning` marks, the `planned_untouched` items sorted with the rest, and `plannedEffects` outside the digest), with the architect rulings of 22:35:34 (F4 carried to L09, F7 the stage numbering with L06). Two rows added; existing ranges re-measured by the installed fixer.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): created this card for the new file MIK-R08 adds.  The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
