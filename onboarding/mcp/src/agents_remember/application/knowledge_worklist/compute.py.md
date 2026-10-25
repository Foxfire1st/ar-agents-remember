# mcp/src/agents_remember/application/knowledge_worklist/compute.py

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

One worklist run. `compute_worklist(inputs)` takes the code trees B and C, the knowledge sides K_B and K_C,
the maintenance-scope flag, the declared effects, the route coverage and the coordination root, and returns
one `knowledge-worklist/v1` document. The run is a function of these inputs: equal inputs give equal items
and an equal digest. An input that cannot be read makes the document `incomplete`, naming the input, with
no items.

## Code Commentary

### The run (`_Run.document`)

1. **Changes.** `_changes` reads the changed paths from `tree_difference_observation` and the renames from
   `git_rename_inference`. An unavailable or partial inventory, or unavailable renames, raises
   `WorklistIncomplete` naming `B/C change inventory` or `B/C renames`.
2. **Read-ahead.** `inputs.code.warm(...)` reads the blobs of every changed text path on both sides in
   batches before any of them is asked for singly. It changes no answer and no failure: a blob it cannot
   read is read again, and fails, where it is used.
3. **Scope** (`_scope`). Every K_B entry at a changed path is classified, or every K_B entry when the
   leaf sets the maintenance scope. The knowledge-side changes between K_B and K_C are computed. Every K_B
   family that contains a touched invariant, or whose record changed, is reached, and every K_B entry of
   those families' members is classified once. What this last step finds raises items and reaches no
   further family.
4. **Items.** `touched_invariant`, `stale_invariant`, `reached_family` and family route conditions
   are joined by MIK-R53 `unassigned_invariant` membership items, `touched_record` decision/facet items,
   and, since MIK-R118 and MIK-R124, the `weakness_anchor` and `changed_document` mark items.
5. **Planned effects.** `reconcile_planned_effects` marks the combined items `planned` or `unplanned`
   and raises `planned_untouched` for a declaration no row delivers; only declared invariant/family
   subjects can be `planned`.
6. **Linkage.** `linkage.change_linkage` marks each hunk of each changed path `linked` or not; the former `_Run` helper body now lives in the extracted linkage owner. A hunk is linked when its
   changed lines on the B side hit a K_B entry's range there, or its changed lines on the C side hit a
   K_C entry's range there (`linkage._linked`). A change without text hunks, and the mode fact of a mode change,
   are linked at file level, by an entry with a `file` locator at the path (`non_text_linked`).
7. **Unexplained changes and reconsideration.** `unexplained_items` applies exact generated-copy filtering and equal-change grouping before raising the remaining unlinked hunk/non-text items; `reconsideration_candidates` raises one for each decision alternative whose linked
   target changed.

The document holds the pairing, the scope counts, the classified entries, the changes with their linkage,
the summaries of planned effects, unexplained changes and reconsideration, and the combined items
(including membership and touched records) sorted by kind and subject, the registered kinds and the digest.

### Failures

`compute_worklist` turns `WorklistIncomplete`, `CodeReadError` (named `C`) and any
`subprocess.SubprocessError` (named `git` by `git_failure`) into `incomplete_worklist(...)`: state
`incomplete`, one named input, no items, and a digest over that.

### Identity

`Item.id` is `item_id(kind, subject, identities)`; the identities of an item are the content facts that
make it a new item when they change. `worklist_digest` is the prefixed SHA-256 of the state, the items and
the incomplete entries.

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
  `id`, `kind`, `subject` and `facts`. The route items use it for `satisfiedBy`. The final assembly
  applies `planned.mark` to rendered items, including route, unexplained, reconsideration and R53 items.
- **Items.** `_touched` collects K_B invariants with a raising entry or a knowledge-side change.
  `_touched_item` carries each classified entry's facts, the added, retired and re-anchored entries, the
  record's K_B and K_C revisions, and the context (families on both sides, `linkedFrom` in K_C). Its
  identities are the raising entries' contents, the added, retired and re-anchored contents, and the record
  revisions only when the record changed; carried and untouched siblings are listed but excluded.
  `_stale_item` carries each stale entry's blob, B blob and both content identities. `_family_items` gives a
  `reached_family` per reached family (reasons `touched:<INV>`, `record-changed` and, since L37, `guarantee-changed`
  when K_C states another guarantee for the family than K_B: `_guarantee_changed`) and per family of a
  stale invariant (reason `stale:<INV>`); `_family_item` lists the union of members with each side's revision
  and both sides' routes, and its identities are the members' `{ id, revision }` per side.
- **Gate linkage** (`linkage._Linkage._change`, definition 8): each changed path's text hunks are linked when a changed line
  hits a K_B entry's range at B or a K_C entry's range at C (`linkage._Linkage._spans`). Base resolution passes
  `tree_side="base"`; candidate resolution keeps the `"candidate"` default, so each uses its own
  tree's symlink modes. Non-text changes (binary, symlink, submodule, type change, empty files) and
  the mode fact of a mode change are linked at `fileLevel` exactly when a `file`-locator entry on
  either side covers the path (`linkage._Linkage._file_covered`). An added or deleted text
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
- **Shared linkage owners.** `code.change_hunks` retains hunk parsing and `linkage.non_text_linked` retains file-locator coverage. The old `_Run._path_hunks`, `_file_covered`, `_spans` and `_linked` placement is historical; current worklist orchestration delegates to `linkage.change_linkage`. The existing per-side insertion/delete-only rule is preserved by the extracted helper. Earlier passing-run statements are historical evidence, not this preparation's execution grade.
- **Step 5, planned effects (MIK-R11, `planned_effects.py`).** The run calls
  `reconcile_planned_effects(inputs.expected_effects, base, candidate, inputs.owner)`. Final assembly
  applies `planned.mark` to invariant, family, route, unexplained, reconsideration, membership and
  touched-record items; only declared invariant/family subjects can be `planned`, all others are
  `unplanned`. Each declaration no row of the leaf's history file delivers adds `planned_untouched`.
  The combined items are sorted by `(kind, subject)` before the digest, which covers their marks.
  Without a declaration the whole list is `unplanned` and nothing is added.
- **Step 6, family route conditions (MIK-R06, `route_conditions.py`).** `_route_items` passes
  `family_route_conditions` a `RouteInputs` (K_B, K_C, C's files, B's files, the run's rename map and the
  owner) and the families that have a `reached_family` item (touched, record-changed or stale-reached).
  Every returned condition becomes a `family_route_condition` `Item` with `satisfiedBy` in `extra`. In code
  In code order the route items join the initial item list; final assembly applies `planned.mark`
  to them too, so they carry `planning: unplanned` and are sorted and digested with the rest.
- **Step 7, unexplained changes (MIK-R10, `unexplained.py`).** `_Run.document` computes the linkage once
  (`linkage.change_linkage`), passes it with an `UnexplainedSides` (C, K_B, K_C, `inputs.coverage`, the owner) to
  `unexplained_items`, applies `planned.mark` to each returned item, and adds them to the one sort
  by `(kind, subject)`. The same linkage object is the document's `changes`, and
  `unexplained.summary()` is its `unexplained` key.
- **Step 8, reconsideration candidates (MIK-R14, `reconsideration.py`).** `_Run.document` binds the run's
  `Classifier` to a local (it was an inline argument of `_scope`) so step 8 can reuse it: it calls
  `reconsideration_candidates` with a `ReconsiderationInputs` (K_B, K_C, `classifier.classify_anchor`, the owner and
  `inputs.coordination_root`, plus the run's `CodeTrees` for route disappearance). The returned items receive `planned.mark` and join the one sort by
  `(kind, subject)` after the unexplained items; `reconsideration.summary` (every evaluated link) is
  the document's `reconsideration` key. L10 kept step 7, so L14 is step 8 (review F9, ruling 2026-09-30T05:31:11).
- **MIK-R53 additions.** `membership_items(K_B, K_C)` raises `unassigned_invariant` for a new or
  newly unlisted live invariant, but not an old orphan or retired invariant. `touched_record_items`
  compares existing decision/facet JSON and Markdown: new records and deletions raise no item here;
  the leaf's own open `raise` row exempts only its status-only reconsideration mark. Both additions
  receive `planned.mark`, then join the same sort and digest; they do not widen one-pass family scope.
- **MIK-R118 and MIK-R124 marks.** `mark_items(K_B, changed_paths, candidate_files=C, renamed)` returns both
  kinds from the run's own changed paths: one `weakness_anchor` per **open** base weakness whose anchored file
  this task changed, and one `changed_document` per base dependent whose document changed — named at the path
  it now stands at when the document was renamed, and omitted when C no longer holds it. A weakness or
  dependent this task itself records raises nothing, because the items are read from K_B. Both kinds receive
  `planned.mark` and join the one sort and digest. `weakness_anchor` is registered advisory: it shows what the
  change asks and refuses nothing (MIK-R118 rule 4). `changed_document` is answered by the confirmed `record`
  row about the dependent at its confirmed revision (MIK-R124 rule 5). Neither kind widens family reach or
  changes another kind's items.
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

- **Remaining unexplained changes require an answer.** Exact generated projections can be omitted and equal uncovered changes can share their source-bound representative; an uncovered group still needs its current complete-source onboarding answer. Covered remaining hunks retain their separate no-invariant/attach/author domain.
- **An unreadable or partial input makes the run incomplete, never silently complete** (architect ruling
  on review R1, F4: a partial ICR inventory is `incomplete` and names the paths; it never falls back to
  file-level linkage).
- **Stale items never widen the classification.** A `stale_invariant` reaches its families without
  classifying their members unless step 3 already reached them.
- **Only K_B families are reached** by the family-scope pass; a new K_C family raises no reached-family
  item of its own. A new live invariant no family lists can nevertheless raise MIK-R53 membership work;
  new decisions/facets raise no `touched_record` item.
- **A mode change keeps its text hunks** (review R1 F5): they are linked as for any text change, and the
  mode fact is added separately at file level.
- No semantic verdict or severity is recorded. The optional unavailable-recorded-blob reason is a mechanical source-read fact, not an inferred business cause.
- **One hunk and one non-text rule for the gate and the reviewer (MIK-L32):** `change_hunks` and `non_text_linked` are
  the only definitions; part of the candidate invariant recorded on `review_lane_classification.py.md`.
- **`plannedEffects` is outside the digest** (the worker's design, unchallenged by review): the items
  already carry what it summarises. The `planning` mark is inside it, so every converted worklist's digest moves
  against a worklist persisted before MIK-R11; that consequence is carried to L09 (ruling F4,
  2026-09-29T22:35:34+02:00).
- **Historical stage numbering with MIK-R06** (ruling F7, resolved by L06, which landed second): the
  route stage is step 6 in the docstring. Current executable assembly marks route items `unplanned`
  alongside the other items; the former unmarked-route account is no longer the output contract.
- **A link anchor is classified by the run's own classifier** (step 8 reuses the local), so it takes exactly an
  entry's class, yet it never joins `entries` or the scope counts.
- **Route items never rewrite anything** (MIK-R06 Exclusions): the run only reports the conditions and the
  mechanical suggestion; no route is changed automatically.

### Todos

- Mechanical route chains are now added through `route_context.with_route_context` to the four selected item kinds over the already parsed K_C. They are presentation context, not extra reach, an ID change or an independent store read.

## Request-scoped classification sharing

After creating the run's classifier, `_Run.document` now offers that classifier, the input pairing and
already-read candidate knowledge side to `share_classifier`. An active `classification_run` lets the
same request's downstream reviewer facts/gate judgments reuse the actual computed inputs; without
that context the call is inert. Context exit clears the held references even on failure. This is
in-process request sharing, not a serialized worklist field, a persistent cache or permission to use
mapped gate placements as reviewer attribution. Existing item assembly, one-pass reach, deterministic
digest and named incomplete-input rules remain their own mechanisms; no new performance/test grade
is inferred from this source-only addition.

## Evidence

- What one run reads. [34]
- The one representation of unreadable input. [35]
- The entry point and the three failures it turns into an incomplete document. [36]
- The change inventory and the renames, each named when unavailable. [37]
- Classification, knowledge changes, reached families and their members, once. [39]

- A changed path's hunks with their linkage, or its file-level linkage. [40]


- A hunk is linked by changed lines on their own side only. [41]


- A non-text change is linked by a file-locator entry. [42]

- A failed or timed-out Git call is the input named git. [43]
- The read-ahead is one batch and never fails the run. [44]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References


- Step 7 in the docstring: the linkage marking, the delete-only rule and MIK-R10's items. [45]

- The schema name. [46]
- One item, its ID from the registry, and `extra` for a registrant's top-level fields (MIK-R06 `satisfiedBy`). [47]
- The run's inputs, with MIK-R10's route coverage and MIK-R14's coordination root last. [48]
- The one representation of unreadable input. [49]
- Inventory and renames; a partial inventory is incomplete, naming the paths. [50]

- The document: the items of every step, one sort and the digest. [51]

- Steps 1 to 4, split out of `document` at the L06/L11 merge. [52]
- The persisted `scope` and `entries`. [53]
- Step 3: families reached by a touched member or a changed record. [54]
- The `touched_invariant` facts and identities. [55]

- The `stale_invariant` item. [56]

- The `reached_family` items and their member identities. [57]
- The leaf's declarations, one input of the run. [58]
- Step 6: the route items, with `satisfiedBy` carried in `extra`. [61]

- Step 8 in the docstring: MIK-R14's reconsideration candidates. [63]


- A hunk links only through a side where it changes lines: a delete-only hunk only by a K_B range (L10 ruling Q2), an insertion-only hunk only by a K_C range (MIK-R09, the L10 N3 carry). [65]

- A Git call that failed or timed out is `incomplete` naming `git` (MIK-R09). [66]
- The insertion-only symmetry at the gate. [67]

- Gate linkage, text and file level. [68]


- The non-text predicate the gate and the lane share (MIK-L32). [69]

- A body edit raises one invariant and its family and carries the rest of the file. [70]
- A comment between functions raises nothing; one inside raises. [71]
- A binary change touches a file anchor and links at file level. [72]
- A partial inventory is incomplete and names the path. [73]
- A mode change keeps its hunks' linkage and adds the mode fact. [74]
- A reached family whose guarantee K_C restates carries the reason guarantee-changed. [75]
- Whether K_C states another guarantee for a K_B family. [76]

### Cross-Repo References

No meaningful cross-repo references found: the run reads one code repository and two parsed memory sides.

No cross-repo boundary is crossed by this file.


- The module docstring: the historical eight-step outline and the incomplete rule; current assembly also includes R53 items and marks the combined list. [33]




- Current orchestration includes link-target items, grouped-change facts and selective mechanical route context [38]




- Planned reconciliation and the final combined-list marks, `planned_untouched`, sort and summary. [59]


- Historical step 6 outline: route conditions of reached families and killed routes; current assembly also marks route items. [60]


- Step 7: one linkage, marked unexplained items in the one sort, `changes` and `unexplained`. [62]


- Step 8: the run's classifier bound once and reused; marked candidates join the one sort; the `reconsideration` key. [64]


- Current source delta inspected statically: Replace stale no-mark and blanket new-record exemptions with the executable combined-list contract; preserve deterministic identity, one-pass family reach and named incomplete-input behavior. [77]



## Current source contract

The orchestrator now delegates range linkage, emits removed-link-target work, carries equal-change source groups and decorates selected items with mechanical route chains; stale-entry facts may include an unavailable-recorded-blob reason. These are real output additions, not a behavior-preserving extraction alone.

Link-target work is not a row-answerable kind and is not passed through planned.mark in this assembly. Route-chain decoration applies only to touched/stale invariants and unexplained hunk/file items; it does not widen reach or change item IDs. The planned/membership/touched-record and named incomplete-input boundaries remain separate.

These spans and input-card identities were independently rechecked after the supported L61 sync. Source observation supplies no test execution, installed-host acceptance or semantic verdict for unrelated inherited material.



- Current assembly includes removed-link-target items, equal-change groups and selected mechanical route context. [78]


- Stale-entry facts preserve the optional unavailable recorded-blob reason. [79]


- The extracted linkage owner keeps per-side changed-line intersection and file-locator nontext coverage. [80]


- Retained persistent link targets surface removed route, path or symbol observations. [81]

- Route-chain context is a mechanical projection over the parsed candidate. [82]


- The orchestrator shares its actual classifier, exact pairing and candidate knowledge side with the active request-scoped classification owner before computing scope/linkage. [83]

- The classification context clears classifier, candidate, pairing and path references on exit, including failures; no active context makes share_classifier inert. [84]
