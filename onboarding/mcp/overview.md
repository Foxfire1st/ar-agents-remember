# mcp/ — MCP Package Overview

## Imported native host package boundary

The package now contains strict Paseo configuration, bounded provision/status/stop, native bridge/catalog/frame integration, immutable role-launch intent and identity-bound task tools. Explicit-model and native-default creation use the same declared feature channel while retaining native permission/tool behavior. Converted MIK readers/writers, worklists and review/lifecycle owners remain intact. Transport, source qualification, authored knowledge and paired publication each require their own evidence.

- Current imported source owns this scoped route boundary. [228]
- Current imported source owns this scoped route boundary. [229]
- Current imported source owns this scoped route boundary. [230]
- Current imported source owns this scoped route boundary. [231]

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/`                                     |

## Governing Overview

[overview.md](../overview.md)

## Recorded Reads, Parsed Diffs And The Reviewer's Worklist Processes

Three kernel modules and the dashboard's composition root carry the reviewer's leaf-wide worklist and the two memos
that keep results computed from Git trees and plain files.

- **The read recorder.** [`kernel/recorded_reads.py`](src/agents_remember/kernel/recorded_reads.py.md) collects, inside
  a recording block, one row for every file that a recording reader reads outside a Git tree (the SHA-256 of the bytes
  read, `absent`, or `unreadable (...)`) and one row for every path resolution and existence probe made through it
  (`resolve:` and `exists:` rows). A key recorded with two identities becomes `conflicting reads`.
  `changed_observations` checks a kept set against the file system, the selection rows first; byte rows are read only
  when every selection still gives its recorded answer.
- **Who records.** The shared readers record through it for every caller: the contract loader
  (`worktrees/worktree_contract.load_contract`), the ledger loaders (`kernel/memory_ledger.py`), the settings parsers
  and the root selection of `kernel/coordination_context/`, `kernel/memory_mode.legacy_internal_memory_root`, the task
  document reader (`tasks/store.read_task_doc`), and the requirement manifest and packet readers
  (`memory/knowledge/requirement_endpoint.py`, `tasks/task_intent.py`). Outside a recording block each of them records
  nothing and answers and raises as a plain read does.
- **Who keeps results with their rows.** The invariant gate's memo (`application/knowledge_gate/memo.py`) and the
  reviewer's leaf-view memo (`application/review_leaf_view_memo.py`). Neither keeps a result whose rows hold a
  conflict or an unreadable row.
- **The worklist processes.**
  [`kernel/reviewer_worklist_process.py`](src/agents_remember/kernel/reviewer_worklist_process.py.md) starts, shares,
  bounds, stops and reaps the child processes that compute the reviewer's leaf-wide worklist, and validates what a
  child returns. A child is `python -P -m agents_remember.application.reviewer_worklist_child` in its own session;
  request and reply travel through pipes, and the module keeps no cache. `MAX_ACTIVE_CHILDREN` is 2,
  `MAX_WAITING_COMPUTATIONS` is 8, `DEADLINE_SECONDS` is 60 and `CHILD_DEADLINE_SECONDS` is 65. Identical requests
  share one child, and the bound counts computations, not the requests that share them. A child whose build identity
  differs from the parent's is refused, and the refusal asks for a restart of the dashboard.
- **Parsed diffs.** [`kernel/git_command.py`](src/agents_remember/kernel/git_command.py.md) remains the only module
  that starts `git`. It declares `PARSED_DIFF_OPTIONS` (`--no-color`, `--no-ext-diff`, `--src-prefix=a/`,
  `--dst-prefix=b/`), which every caller that parses `git diff` output passes, and `shared_blob_reads()`, a block
  inside which a blob read from one repository is not read from Git again.
- **Composition.** `cli/dashboard.py`'s `serving_collaborators` creates one `ReviewerWorklistProcesses` per composed
  app, passes it to the tree view port and supplies its `shutdown` as `review_trees_shutdown`, which the app's lifespan
  calls when serving ends.

- A recording block collects the rows of one computation. [246]
- A kept set is checked with its path selections first. [247]
- A conflict or an unreadable row is a failed observation. [248]
- The contract loader reads through the recorder. [249]
- The ledger loader reads through the recorder. [232]
- The removed repository memory root is resolved through the recorder. [250]
- The limits of the worklist processes. [234]
- One request: digest, join or start, wait, leave. [235]
- The one command line of a child, in its own session. [236]
- The build-mismatch failure asks for a dashboard restart. [237]
- The options every parsed diff passes. [238]
- The shared-read block of the batched blob reader. [239]
- The composition root creates the process owner. [240]
- It supplies the owner's shutdown to the app. [241]
- The waiting bound counts computations, not the requests sharing them. [242]
- A build mismatch asks for a dashboard restart. [243]
- Every parsed diff names its own prefix, colour and driver options. [244]
- Bytes the child consumed are identified across a change and restore, a conflict, an absence and a read error. [245]

## 260928-MIK-L37 The Cutover To Text Storage: The Installed Build Governs Converted Memory

`260928-MIK-L37` (MIK-R37). What earlier sections of this overview call "inert until the cutover" is what the code does on converted memory: a
memory tree that holds `knowledge/layout.json`. On a converted line:

- knowledge is written through the curator file writer and read through the derived index;
- the knowledge database is frozen: the database writer and the publication sink refuse a converted tree and name
  the file writer, and `knowledge.sqlite` stays in place until MIK-R26 removes it;
- the cutover lock (`src/agents_remember/worktrees/cutover_lock.py`) refuses every write, check, managed sync,
  closeout and landing of memory that is unconverted on every side once its memory repository holds converted
  memory, naming the crossing sync.

Files this overview governs directly:

- **[`cli/knowledge_ingest.py`](src/agents_remember/cli/knowledge_ingest.py.md) and
  [`cli/knowledge_write_route.py`](src/agents_remember/cli/knowledge_write_route.py.md).** `knowledge-ingest` gains
  `--crossing <task-id>-crossing-<n>`: with the master's series contract, a crossing sync's curator resolves a
  record both sides changed (at the higher side's revision plus one) and records the rows into the crossing history
  file. The leaf route passes the contract's code base as the converted base's fallback commit.
- **[`cli/knowledge_bootstrap.py`](src/agents_remember/cli/knowledge_bootstrap.py.md).** The database route takes
  the cutover lock.
- **[`cli/memory_citations.py`](src/agents_remember/cli/memory_citations.py.md).** On converted memory `--fix` takes
  `--document` alone and authors that card.
- **[`kernel/memory_init.py`](src/agents_remember/kernel/memory_init.py.md).** The failed-Git early return carries
  `layoutMarker`.
- **The packaged skills.** The c-05 skill gains
  [`workflows/converted-card-workflow.md`](src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/converted-card-workflow.md.md),
  and the c-02 skill, the c-05 skill, its file-level workflow and the curator role each gain their converted-memory
  paragraph. [`c-12-closeout/SKILL.md`](src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md.md) and
  [`c-09-git-worktree-manager/SKILL.md`](src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md.md)
  say that the closeout preview and apply ask the mandatory gate on converted memory, and the
  [curator hand-off template](src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md.md)
  states the rules for a row's items, a cover's rationale and the governing row of a changed record.
- **[`kernel/git_command.py`](src/agents_remember/kernel/git_command.py.md) and
  [`kernel/memory_cache.py`](src/agents_remember/kernel/memory_cache.py.md).** `copy_git_index` copies a Git index
  with its file's modification time, so a capture through the copy still sees a file rewritten in the second the
  index was written (INV-656CYW). `ignore_memory_cache` is the cache preparation's one write to memory content,
  which the gated closeout makes before it judges the tree.

- The crossing owner's route of knowledge-ingest. [222]
- The bootstrap's database route takes the cutover lock. [223]
- The converted-card workflow's opening. [224]
- The lock every memory route asks. [225]

- A copied Git index keeps the index file's modification time. [226]
- The cache's ignore rule alone. [227]


## 260928-MIK-L33 Review Triage Order And Change-Kind Badges, Inert Until The Cutover

`260928-MIK-L33` (MIK-R33, adopting ICR-R32@v1 with the storage substitutions of D18) makes the reviewer's family tree
say what kind of recorded change brings each family and member occurrence into review, list the changes first
without hiding unchanged siblings, and move between them with `j`/`k`.

- **Where:**
  - `application/review_change_kinds.py` (new): the facts, on the server, for the members a roster page returned,
    over MIK-L32's lane (no second hunk classifier); `models/knowledge/review_change_kinds.py` (new): their
    vocabulary and validators; `review_family_context.py`: the entry's optional `change_kinds`;
    `knowledge_review.py`: one call; `knowledge_worklist/classify.py`: the public `carried_mechanically` and
    `reanchored`; `review_lane_classification.py`: `changes_lines` exported.
  - Dashboard: `data/reviewFamily.ts` (the mirror); `panels/review/changeTriage.ts`, `ChangeBadges.tsx`,
    `changeTraversal.ts`, `triageOrderPreference.ts`; hooks in `FamilyTree.tsx`, `familyWalkMerge.ts`,
    `FamilyReviewCenter.tsx`, `ReviewSurface.tsx`, `ReviewWorkspace.tsx`, `MarkerTargetState.tsx`; the keymap's
    `review` zone and `REVIEW_CHORDS`; the `?` page's group.
- **Architect rulings** (`33_review-triage-order-and-change-kind-badges.json`): 15:11:20 start; 16:22:22 worker items
  1–11 (5, 6b, 4 and 9 changed); 17:47:43 review R1 (F1–F4, the notes, the landing order and merge plan); 18:57:45
  review R2; 21:41:02 the merge round with MIK-L34 (and `j` at 390 px reveals the centre); 21:55:02 review R3 (R3-1
  fixed, R3-2 notes, R3-3 to curation). Recorded in the panels and application overviews and on the cards.
- **Candidate invariants (not ingested; no speculative ingestion):** (1) change-kind facts are computed on the server,
  for returned members only, from recorded comparison facts, with the hunk intersection only from MIK-L32's
  classification and never recomputed by the client; (2) unreadable or partial knowledge produces `unknown` with a
  stated reason, never `unchanged` or a complete-looking total; (3) changed intent text is never `unchanged`, even at
  the same revision; (4) triage order never hides unchanged siblings, and traversal never forces unreturned pages to
  load; (5) each fact is stated once per node, visually and to assistive technology.
- **Inert before MIK-R37:** only a converted leaf's tree comparison carries `change_kinds`; the worker's 29
  unconverted reads are identical to base once the null field is dropped, and this curation's `memory_quality_check`
  runs returned no worklist.
- **Tests and evidence:** `test_review_change_kinds.py` (12, lane row `:128`); `changeTriage.test.ts` (12),
  `FamilyTree.triage.test.tsx` (18), `FamilyTree.triageReal.test.tsx` (3), `ReviewSurface.triage.test.tsx` (1),
  `ReviewSurface.triageMarkers.test.tsx` (2), and the extended `shell.test.tsx` and `ReviewSurface.markers.test.tsx`;
  22 captured bodies with receipts (MIK-L34's twelve re-captured). Real data on scratch clones
  (`notes/reports/260928-MIK-L33-evidence/`): FAM-R6R095RW reads 2 intent · 6 impl · 1 membership · 0 unknown of 24
  after curation, and every hunk-established fact is a link in the lane's per-file response (2 of 2). Checks on the
  merged tree: the whole vitest suite 1,951 passed; the reviewer's focused pytest 150 passed.

- The facts and where they come from. [1]
- Their vocabulary. [2]

## 260928-MIK-L09 The Mandatory Invariant Closeout Gate, Inert Until The Cutover

`260928-MIK-L09` (MIK-R09@v2; D5: "Invariant work is MANDATORY! Never just reporting.") makes invariant maintenance a
gate, not a report. No route that commits a leaf's memory commits while an item of the leaf's **recomputed** worklist
(MIK-R08) lacks a current satisfying row in its history file (MIK-R07), while the worklist run is `incomplete`, or
while the validator (MIK-R22) fails; each is one repair finding in `curatorActionableCount`. A master or checkpoint
lands only when no entry at a path its net code diff changed is stale or unverifiable (MIK-R03). No waiver, override
flag or report-only mode exists.

- **Where:**
  - `application/knowledge_gate/` (new, six modules, carded under the application overview): `predicates` (each
    kind's own predicate; rule 2's invariant and family currentness), `gate` (`evaluate_leaf_gate`: probe, tip, memo,
    recompute over the exact trees, decide, validate as a leaf publication against the parent line's memory tip),
    `memo` (the bounded memo keyed by the exact trees, contract, parent tip, task document and build, and kept with
    every row the evaluation recorded outside the trees), `direct` (direct landing's sides and leaf), `landing` (record landing's closed history
    and the master's net staleness), `adapter` (`KnowledgeGate`, the port implementation).
  - `worktrees/knowledge_gate.py` (new): the marker probes, `GATE_UNBOUND`, `close_owner_history` (the closeout's own
    `closed: true`, MIK-R07 rule 7), the direct landing's per-generation closing receipts, and the prepared path's
    fail-closed refusal; `worktrees/services.py` declares `KnowledgeGatePort`; `application/worktree_services.py`
    binds it.
  - The routes: the curator publication (`application/memory_quality/controller.py`: every gate finding is a
    `knowledge-gate` repair finding), the closeout validator (`curator_coherence._require_knowledge_gate`), the
    closeout memory commit (`closeout_external`: close, validate the exact tree, restore on refusal), direct landing
    (gate, close, validate, keep the closing until the generation is decided; cancellation restores it), record
    landing (probe first; the landed commit validates and a leaf's file is closed), master and checkpoint landing
    (`integrate._knowledge_gate_block`), and the prepared path (`certification/execution.py`,
    `prepared_certification.py`: refuses on converted memory).
  - `memory_quality/knowledge_validator/rules_history.py` (new): `R09-history-rows` (every history file's subjects
    resolve; open files, and at leaf publications every file not closed in a base, re-anchor-checked) and the
    report-only `R09-history-rows-merged`; `ValidationContext.leaf_publication` and `GitKnowledgeValidation.leaf_refusal`.
  - `kernel/recorded_reads.py`: the read-set recorder. The shared readers of files outside any tree record
    through it (see "Recorded Reads, Parsed Diffs And The Reviewer's Worklist Processes" above).
  - The worklist: `leaf.py` (`CandidateTrees`, `worklist_over`, the strict maintenance scope, fail-closed probes),
    `compute.py` (`_linked`, the symmetric definition 8; `git_failure`), `observe.py` (`read_failed`,
    `CodeObjectUnavailable`), `code.py` and `memory/conversion/code_objects.py` (`has_blob`), `onboarding_trace.py`,
    `knowledge_worklist_section.py` (`item_facts`, `_trace_facts`); L32's `review_lane_classification.py` docstring
    and `review_tree_entries.py`.
- **Rulings** (`09_mandatory-invariant-closeout-gate.json`).
  - **Carried obligations and D29, gathered by the start decision 2026-09-30T13:15:47:** validator wiring at every
    route (L22, `memory_commit_refusal` with a refusal test at each); the L12 history-row rule through the registry;
    `SubprocessError` → `incomplete` naming `git` (L03, 19:15:20); per-kind stored-item predicates (L30 N6, L06 Q7,
    L10, L14); the admission base is the parent line's memory tip (L27 Q6); fail-closed task-document reads and
    always recompute (L11); subject-keyed family route items (L06 N2); the insertion-only symmetry (L10 N3); an
    unanswered reconsideration candidate blocks (D29).
  - **14:38:47, gaps 1–4:** gap 1, MIK-R09 rule 6's second bullet (refuse unconverted trees at the routes, naming the
    crossing sync) is **carried to L37**, not built here; gap 2, direct landing infers its leaf (the one open history
    file) on converted memory only, with no schema change; gap 3, the prepared path fails closed on converted memory;
    gap 4, the bounded memo keyed by exact inputs. Accepted smaller choices: the history-row rule's scoping and a
    master's record landing without the staleness check.
  - **15:09:25:** refusals over complete inputs may be memoised; the memo records every requirement file it read and
    reuses a verdict only while each still hashes the same.
  - **16:07:55, review R1 (changes-required) F1–F9:** F1 the row rule applies to every file not closed in K_B, scoped to
    leaf-publication routes; F2 a refused closeout restores the file it closed; F3 direct landing keeps its closing
    until the generation is decided, and an exact retry reaches the existing generation before the gate; F4
    unverifiable blocks at landing; F5 one refusal test per public route entry; F6 the admission base and memo key
    tested; F7 record landing probes first; F8 L32's docstring; F9 Git failures are incomplete and never memoised,
    the conversion probe fails closed, probe timeouts are named, the settings fallback joins the read set, a
    conflicting read is never kept. **Sync merges:** a merge-caused mismatch is report-only (`R09-history-rows-merged`);
    one already present on the leaf's side refuses.
  - **16:08:08, carried to L37:** reopen after the cutover (a closed-out leaf's history file is frozen in K_B).
  - **17:59:48, review R2 (pass-with-notes):** R2-1 `unknown_subjects` over every history file at every route (the L22
    validator fixtures now keep the retired record `INV-RET1R3`, per MIK-R22 rule 3); R2-2 per-generation receipts
    (N12) and the pinned guards; R2-3 `CodeObjectUnavailable` named, not a Git failure; R2-5 a corrupt receipt is a
    named refusal; R2-4 accepted as a note.
  - **19:16:07, review R3 (pass):** R3-1 the landed-generation backstop hashes with `git hash-object` (the repository's
    own object format); R3-2 `has_blob` tells a missing object from a Git failure.
- **Candidate invariants (not ingested; no speculative ingestion):**
  1. No memory reaches a leaf-publication route (worktree closeout, direct landing, a leaf's record landing) without
     the gate's recomputed worklist fully answered and the validator passing; no waiver, override or report-only mode
     exists (`judge`, the route refusals, `GATE_UNBOUND`; the gate and route tests, and `gate-1..4` on real data).
  2. The gate always recomputes from the exact trees; a kept verdict is reused only for identical trees, contract,
     parent tip, task document, build and recorded requirement-file reads; incomplete runs and Git failures are never
     kept (`recompute_for_gate`, `GateMemoKey`, `_Kept`, `GateResult.memoisable`; the memo, approval-state, tip and
     Git-failure tests).
  3. An unreadable input (a Git failure, an unreadable task document or knowledge) makes the run incomplete with a
     named reason; it is never read as unchanged, answered or absent (`git_failure`, `strict_leaf_doc`,
     `has_layout_marker`, `read_failed`, `has_blob`; the incomplete, predicate/validator, probe and blob tests).
  4. On unconverted memory every route behaves exactly as before the gate (the marker probes; the unconverted test;
     `unconverted.sh`, base against this build on the real memory: identical apart from the build label).
  5. A history file closed in K_B is frozen; at leaf-publication routes every other history file's rows must agree
     with their entries, whatever the file's own closed flag says (`checked_history_files`, `leaf_publication`; the
     F1, N01, N08 and N09 tests).
  6. Every subject a history row names resolves in the tree, at every route (`check_history_rows`; the ghost-subject
     master-landing test).
- **Inert until the cutover.** Every gate path runs only on converted memory (the layout marker on K_B or K_C); on
  unconverted memory, which is all production memory before MIK-R37, closeout, landing and sync behave exactly as on
  base. The exceptions, not behind the marker probe: a Git failure in the conversion's `has_blob` now refuses instead
  of reading "absent"; `has_blob` itself distinguishes a missing object from a Git failure; and the reviewer lane's
  cards read names such a failure `unavailable` instead of raising. The gate goes live with MIK-R37's installed build
  (rule 8); the cutover's own closeout is its first real-workflow evidence.
- **Tests and evidence.** `test_knowledge_closeout_gate.py` (18 cases), `test_knowledge_gate_routes.py` (27 cases), two
  sync-merge cases in `test_knowledge_validator_routes.py`, adapted counts in `test_knowledge_worklist_leaf.py` (0 → 4)
  and `test_onboarding_trace_gate.py` (2 → 3), and the `RETIRED` fixture in `test_knowledge_validator.py`. Mutations:
  26, 37 and 4 of the worker's killed, and the reviewer's N01–N21 set as recorded. Real data on converted scratch
  copies (`notes/reports/260928-MIK-L09-evidence/`): `gate-0` pass, `gate-1` refused with 5 findings (the packet's
  `_not_listed` edit), `gate-2` pass once rows were ingested, `gate-3` refused with 2 (edited again), `gate-4` pass;
  the scripted closeout and landings (`closeout.txt`); the maintenance scope (178 entries, 15 findings); the memo
  timing (about 67 s → 17 s and 31 s → 8 s per run). Final checks (R3): unit suite 3,406 passed, integration lane 457
  passed.

- The gate over a leaf's exact candidate. [3]

- Each kind's own predicate, registered beside the kind. [4]
- The worktree layer's probes, the unbound refusal and the closeout's own write. [5]

- The history-row rule over every file's subjects and the leaf's own file. [6]

- The two lane rows. [233]


## 260928-MIK-L38 Finalize Completes The Master Row: One Rule For A Leaf's Master

`260928-MIK-L38` (MIK-R38, developer direction D32: "Completing a status on a task should also show the status on the
master as completed") makes the finalizer resolve a leaf's master by the task-document master sync's rule. Before it,
the sync resolved a leaf naming no `master` to its folder's `task.json` and kept that row current, while the
finalizer called the same leaf standalone and skipped the row, so every finished 260928-MIK leaf (none names its
master) stayed `inProgress` on the master; the developer saw 15 such rows, repaired by resync writes.

- **Where:**
  - `tasks/master_sync.py`: the public `folder_master_json_path`, the one rule for a leaf naming no master (a
    `subTask` only; the folder's `task.json` when it exists). The sync's own path and behaviour are unchanged.
  - `worktrees/modules/finalize.py`: `_resolve_parent_target` dispatches to `_named_parent` (unchanged) or
    `_folder_parent` (the helper, then every named-master check and the demotion rule); no folder master, or no row
    for the leaf, stays standalone; an asserted parent without a row names that cause.
  - `worktrees/reopen.py`: `_reopen_master_path` uses the same helper (ruling 2026-09-30T12:33:07 Q2), so a `light`
    `task.json` no longer resolves to itself.
  - `tasks/leaf_doc.py`: `require_task_document_in_place`, called by finalize and reopen on the leaf and on the
    master before any write (review R1 finding 1, ruling 13:11:32; the master side by ruling 13:35:32).
  - The `lifecycle_finalize_task` description, `docs/reference/mcp-tools.md` and the c-09 skill (source, package copy
    and the eight starter copies) name the folder-master row and the refusal of a sub-task naming none whose folder
    `task.json` is not a master (ruling Q3; R1 note 5; "sub-task", ruling 14:12:52).
- **Rulings** (`38_finalize-completes-the-master-row.json`). 12:33:07: Q1 the new cases stay in the integration lane
  with the finalize tests; Q2 reopen resolves through the same helper; Q3 the tool description, `mcp-tools.md` and the
  c-09 skill are updated; Q4 the packet's standalone and refusal cases as specified (a folder master without the
  leaf's row leaves it standalone; an unnamed `subTask` whose folder `task.json` is not a master is refused).
  13:11:32 (review R1 pass-with-notes): finding 1 the misplaced-leaf guard; note 2 the unreadable `task.json` pinned;
  note 4 the named cause; note 5 the docs; note 3 (named-master resolution differences) out of scope. 13:35:32: the
  master-side guard. 14:12:52: review R2 pass, and the wording "a sub-task naming none". Sync: the leaf was synced onto
  L32 (`59daf505`) with a clean 3-way apply; its finalize, reopen and dependency-ownership tests pass on the synced
  tree.
- **Candidate invariants (not ingested; no speculative ingestion):** (1) finalize, reopen and the task-document master
  sync resolve a leaf's master by one rule: the named master, else the folder's `task.json` master; (2) a finalized
  leaf that a master lists shows `Completed` on that master's row; (3) no task-document writer overwrites a document
  whose read path differs from the store's write target for it (finalize and reopen guard it before any write).
- **Not inert:** unlike the knowledge leaves, this is not gated on the memory conversion; once this build is
  installed, finalize and reopen use the rule on every task folder. Real-path evidence on scratch copies of the real
  task folder (the worker with L31, review R1 with L35 and L38): base leaves L35's row `inProgress` and the sync re-plan reports `updated`; the fixed build completes
  the row and the re-plan reports `unchanged`; a named leaf (L38) is identical on both.
- **Tests:** `FolderMasterFinalizeTests` (5 cases, 9 subtests), one new `LifecycleFinalizeTests` case, four new
  `ReopenResetTests` cases.
  Review R2: unit suite 3,298 passed, integration lane 457 passed.

- The one rule, named for its three writers. [8]
- The finalizer's dispatch. [9]
- The placement guard. [10]

## 260928-MIK-L32 The Unexplained-Changes Lane In The Reviewer, Inert Until The Cutover

`260928-MIK-L32` (MIK-R32, adopting ICR-R33@v1 with the storage substitutions of D18) makes changed source that no
recorded entry's range intersects a first-class review destination. On a tree comparison the task entry shows the
count of unexplained and of unknown-attribution files beside `+N −N`, the reviewer's tree offers `Unexplained changes`
and `Unknown attribution` after the families, and a file opens on its actual diff focused on the hunks of that class.
One classification serves all of it, and it is the gate's: MIK-R08's hunk, range, intersection and non-text
definitions.

- **Where:**
  - `application/review_lane_classification.py` (new): the one classification (`TreeLane`): buckets, hunk classes
    and the non-text gate linkage, with no hunk arithmetic of its own, an entry supplying a range only at its own
    recorded blob, and bounded reasons.
  - `application/review_unexplained_lane.py` (new): `lane_summary`, `unexplained_lane` and `classify_changed_path`.
  - `models/knowledge/review_lane.py` (new): the lane's vocabulary and its reconciliation validators; `review_trees.py`
    gains `lane` and `file_classification`, `review_intent_summary.py` gains `attribution`.
  - `application/knowledge_worklist/code.py` (`change_hunks`, moved verbatim) and `compute.py` (the exported
    `non_text_linked`): the gate and the lane share both; the gate's output is unchanged.
  - `application/review_tree_knowledge.py` and `serving/review_trees.py`: `lane=files` and `file=<path>`, one focused
    question per request, every focused read reopening its comparison; `application/review_intent_summary.py`: the
    entry's count on the same summary response.
  - Dashboard: `data/reviewLane.ts`; `panels/review/laneFocus.ts`, `UnexplainedLane.tsx`, `LaneFileFocus.tsx`; the
    surface's one lane read handed to the workspace and the technical details; the entry's `AttributionCount`.
- **Architect rulings** (`32_unexplained-changes-lane.json`). PS-1 was already fixed by L31. 12:19:20: Q1 on tree
  comparisons the explorer takes the lane's buckets; Q2 the exact-blob rule is the packet's, carried to L37 as a check
  item (47 of 178 converted real entries sit at an older blob); Q3 and Q4 placement of gate-held non-text changes and
  of unexplained hunks in files of unknown attribution; Q5 the membership states (L34 may refine; it kept them as
  mapped); Q6 the entry
  count shows even when the intent counts are refused; Q7 a rename is a deletion plus an addition. 13:07:38 (review
  R1 pass-with-notes): F1 the technical details follow the lane; F2 long `file=` values answer the typed refusal; F3 a
  partial index gives `unknown`, never "gate unexplained"; F4 bounded reasons; F5 carried to L34 and resolved there
  (every hunk a lane window draws carries its own intent mark); F6 accepted. Review
  R2: pass. Sync: the L35 word-diff surface test was rerun on the L35-synced tree and passes.
- **Candidate invariants (not ingested; no speculative ingestion):** (1) the reviewer classifies changed files and
  hunks through MIK-R08's definitions only, one classification shared with the gate; (2) an entry supplies a range
  only when a side's blob is exactly its recorded blob; (3) on tree comparisons the explorer and the technical
  details take their attribution from the lane, so no two surfaces disagree; (4) the lane says unknown when the gate
  could not be computed, never "gate unexplained"; (5) lane reads are bounded and validated, and every answer to a
  validated request is typed.
- **Inert before MIK-R37:** only a converted leaf's tree comparison reaches the lane, and a dataset review makes no
  lane read. On the 29 unconverted reads of L25 and L31, base against the worktree, 29 are identical once the new
  null `attribution` field is dropped (the served body omits it), and this curation's own `memory_quality_check` runs
  returned no worklist.
- **Tests and evidence:** `test_review_unexplained_lane.py` (11 cases, lane row `:125`), `laneFocus.test.ts` (3),
  `ReviewSurface.lane.test.tsx` (7) and `intentReviewEntry.attribution.test.tsx` (8), over six real captured bodies of
  the MIK-L32 scratch leaf. Real data on scratch clones (`notes/reports/260928-MIK-L32-evidence/`): comparison 1
  (pre-curation) `· 3 unexplained · 1 unknown` with the appended helper attribution unknown while the gate raises
  `unexplained_hunk`; comparison 2 (post-curation) the helper unexplained, agreeing with the gate. The reviewer's
  agreement check matched the gate on every path's hunks and non-text linkage. Final checks (R2, synced tree): unit
  suite 3,359 passed, integration lane 447 passed, the whole vitest suite 1,811 passed.

- The one classification and where it differs from the gate. [11]
- The three reads. [12]
- The lane's shapes and validators. [13]

## 260928-MIK-L14 Reconsideration Surfacing, Inert Until The Cutover

`260928-MIK-L14` (MIK-R14@v2) makes a decision's rejected or deferred alternative come back up when an explicitly
linked ground changes. When a target a `reconsider_on` link names changes in a leaf, the worklist raises a
`reconsideration_candidate` (subject `reconsider:<DEC-ID>#<alternative index>`), and the curator answers it with a
`reconsideration` history row: `still_rejected` with a reason, or `raise`, which sets the decision
`under_reconsideration` and appends a question to the leaf's task-document `openQuestions` for the developer. The
curator never reverses a decision. An unanswered candidate blocks closeout through MIK-R09's generic rule (D29, L09).

- **Where:**
  - `application/knowledge_worklist/reconsideration.py` (new): the kind and its four triggers over every K_B
    decision's links, one hop only, with a `reconsideration.links` summary; `compute.py` step 8 (after L10's step 7)
    reuses the run's classifier; `classify.py` splits `_classify_anchor` out so `classify_anchor` classifies a link
    anchor like an entry, never as one; `leaf.py` and `__init__.py` pass the coordination root and register the kind.
  - `models/knowledge_files/reconsideration.py` (new): the subject, `TRIGGERS` (with `anchor_stale`),
    `REFRESHED_TRIGGERS`, `link_target_key` and the gate predicate; `history.py`: `ReconsiderationRow`, the sixth row
    kind.
  - `memory/knowledge/requirement_endpoint.py`: the manifest lookup `latest_approved_requirement_version` and
    `requirement_approval` (`approved` / `not_approved` / `unknown`, `latestPacket`).
  - `application/knowledge_writer/reconsideration.py` (new): what a row names, the `raise` question, and the
    `still_rejected` refresh with its link states (unchanged, carried, a new change as an earlier version or changed
    again, stale item, re-authored) and the explicit answer by item ID; `open_questions.py` (new): the question
    through `task_doc`; `authoring.py` (the rows), `writer.py` (the worklist and questions in the request; the append
    before any file) and `carry.py` (the public `mapped_anchor`).
  - `memory_quality/knowledge_validator/rules_reconsideration.py` (new): `R14.1-linked-alternative-order`;
    `memory_quality/knowledge_worklist_section.py`: the checklist's reconsideration facts.
  - CLI: `knowledge-ingest --config`, `knowledge-worklist --coordination-root`, and `cli/knowledge_write_route.py`'s
    lazy `LeafQuestions` and persisted worklist.
  - Skills: the hand-off template's reconsideration-row bullet and the decision section's reorder refusal, synced to
    all copies.
- **Architect rulings** (`14_reconsideration-surfacing.json`). 01:45:56 (carried from L13): reuse
  `resolve_requirement_endpoint`, and guard index stability (resolved: the manifest lookup starts at the resolver's
  `task_root`; `R14.1` refuses a reorder). 04:37:56: Q1 route targets fire through history rows only (a row that
  reroutes, retires or deletes the route or a family that has it); Q2/Q3 `still_rejected` refreshes the link to the
  judged state, and a `raise` leaves it; Q5 superseded decisions are skipped and listed; Q4 (the guard follows
  options by text, a move with a reword is not caught) and Q7 (the two-call `task_doc` read-modify-write window;
  rerun appends nothing twice) are recorded limits; Q6 and Q8 accepted. 05:31:11 (review R1): F1 the refresh maps a
  `line_range` through the diff (`mapped_anchor`) and refreshes only fired links; F2 the revision is bumped once per
  leaf through the record path; F3 a stale link anchor fires `anchor_stale`; F4 the re-point takes the item's
  `latestApproved`/`latestPacket`; F5 and F6 fixed; F7 recorded; F8 notes; F9 step 8 after the sync onto L10; F10
  carried to L37 (installed mode and `--config`). 06:17:11 (R2): N1 the K_C link must still be the fired target
  (`link_target_key`); N2 tested; N3, N4 notes. 07:13:54 with the 09:18:48 reconciliation: R3-1 (one ruling with the
  duplicate N5 from two concurrent architect instances) a rerun of the same answer is an idempotent no-op; the code
  was consolidated by one worker and the memory worktree was reset and curated again by one curator. 10:05:18 and
  10:39:15 (R4): the carried state, refusal messages that name the real cause, and the explicit answer by naming the
  new item's ID. 11:01:18 and 11:24:12 (R5): carried only when the anchored content survives, the stale-item state,
  and a curator-set unapproved version (v4) refused as re-authored. 11:53:13 (R6): pass-with-notes, R6-1 to R6-4
  accepted as notes.
- **Candidate invariants (not ingested):** (1) a `reconsider_on` link fires only on the packet's triggers, one hop
  only, and an unresolved endpoint or a task without a manifest never fires; (2) every new change to a judged target
  needs a new explicit answer, a rerun of the same answer is idempotent, and nothing absorbs an unjudged change;
  (3) `still_rejected` refreshes only the fired link, to the judged state mapped through the diff, and refuses a link
  that was re-authored or cannot be mapped; (4) `raise` puts the question in the task document before any knowledge
  file is written, and on failure writes nothing; (5) a linked alternative cannot be reordered to another index
  (R14.1); (6) unconverted memory reads are unchanged.
- **Inert before MIK-R37:** an unconverted leaf gets no worklist and no file write; the real unconverted L14
  contract gives `leaf_worklist → None` on the base and L14 builds (`unconverted.txt`), and this curation's own
  `memory_quality_check` runs returned no worklist. The validator rule runs only over converted trees.
- **Tests and evidence:** the new `test_reconsideration_surfacing.py` (29 cases, lane row `:127`, 1,172 lines, note
  R6-2), the history-registry case compared as a set, and the final Forty-second catalog re-pin (`4477446e…`). Real
  data on scratch clones (`notes/reports/260928-MIK-L14-evidence/`): 1 candidate before the change, 3 after it
  (`record_file`, `anchor`, `requirement_version`); the `raise` refused without task-document settings, then written
  with the question in a scratch copy of the task document; both decisions at revision 2; the answered items
  satisfied with the stored predicate agreeing; a rerun clean; the next leaf 0 candidates; the reorder contrast
  passing on the base build and refused twice on the L14 build. Reviews R1 to R5 changes-required, R6
  pass-with-notes; final unit suite 3,327 passed, integration lane 447 passed. After L29 landed, the leaf was synced
  onto `ce459423` (its 36 files re-applied cleanly).

- The worklist registrant: what is read, the triggers, route and superseded rulings, the items. [14]
- The writer's rows, the refresh and its link states. [15]
- The manifest lookup. [16]
- The reorder guard, registered on import. [17]
- The lane row. [18]

## 260928-MIK-L29 The Path-Based Knowledge Reader, Inert Until The Cutover

`260928-MIK-L29` (MIK-R29@v1) adds a read-only **Knowledge** area to the dashboard: a reader of one repository's
knowledge at any memory tree, browsed like a file explorer and needing no task. A commit selector defaults to the
published memory tree (MIK-R23 rule 6) and offers any converted memory commit and a live leaf's candidate
(`leaf:<scope>`). A **path view** shows a file's or directory's onboarding prose with its `[n]` references resolved
(every target listed; code opens at the locator, records at their truth view), the realization and proof entries
grouped by invariant with their MIK-R03 states, the families of those invariants and those routed over the path
(MIK-R05) with their other locations, and every record linking to the path or its invariants. A **truth view** shows
an invariant, family, decision, incident or other facet record with every field, links both ways and a timeline,
newest first, from three sources: the record file's log with meaning diffs, the history rows of every leaf
(MIK-R07) and the log of the sidecar entries that realize or prove it (moves and re-anchors). A census view
(MIK-R20), a without-proof list by path (MIK-R28 rule 5) and a code view complete it. The URL hash encodes the
repository, commit and path or ID, so every link is a navigation and a view can be shared.

- **Where:**
  - `application/knowledge_reader/` (new package): `__init__.py` (the entry point and envelope), `selection.py` (the
    three tree spellings and the code tree), `files.py` (memory and code reads, path validation, bounded code text),
    `paths.py` (explorer, path view, without-proof), `subtree.py` (the paged subtree), `records.py` (summaries,
    decisions in full, links, references), `truth.py` (truth, census, record list and code views) and `timeline.py`.
  - `memory/knowledge_index/query.py`: five additive lookups (`entries_under`, `entries_in_directory`,
    `live_entry_paths_under`, `links_to_path`, `records_of_kind`) and a shared `_links`.
  - `serving/knowledge_reader.py` (new): `GET /api/knowledge/reader/{view}`; `serving/_app_common.py` (the
    `knowledge_reader` port), `serving/app.py` (its registration) and `cli/dashboard.py` (its composition).
  - `dashboard/src/data/knowledgeReader.ts` (new) and `dashboard/src/panels/knowledge-reader/` (new: the panel,
    explorer, path views, truth view, shared parts, 14 component tests and a real-data fixture);
    `dashboard/src/cockpit/Cockpit.tsx` (the Knowledge mode and the `#knowledge?…` initial view).
  - `mcp/tests/test_knowledge_reader.py` (new, 21 cases) and its `unit-regression` lane row.
- **Architect rulings** (`29_path-based-knowledge-reader.json`). Carried from L13 (2026-09-30T01:45:56): a decision's
  chosen and rejected alternatives with reasons and `reconsider_when`, and its derived superseded status, are shown
  whole wherever the decision appears, read through `models/knowledge_files/decisions`. 06:22:39: started under D31
  on `48f680d5`. 09:42:58 (worker questions and review R1): Q1/N1 a memory commit measures at its `Code-Commit`
  pairing, `published` and a leaf at `HEAD` of the code checkout (matching L03; revisit with L03 gap 1), and every
  answer names `codeTree`, `codeSource` and `codeNote`; Q2 the index cache is L23's design (no repository write);
  Q3-Q10 accepted as built; N2 a link pinned to the memory revision when the tree is clean; F1 `--pickaxe-all`
  dropped; F2 the directory view bounded (own level, children with counts, the full list paged through L02's
  continuation; the root summary as the landing); F3 a malformed locator answers 400; F4 no `[n]` rewrite inside code;
  F5 re-anchored, not moved; F6 guard tests; F7 a bounded timeline cache; F8 radon splits; F9 the derived status in the
  header; F11 failures partial or unavailable, never empty; F12 dead code removed; F13 stale explorer answers ignored;
  F14 a binary or oversize blob answers a bounded notice; F10 accepted as a note. 10:44:14 (R2): F15 NUL and control
  characters answer 400; F16 a resumed subtree page measures at the walk's code tree; F17 tests for the four surviving
  Python mutants and the unreadable-links display; F18 the code view of a directory is a typed `absent`; the "more"
  button's in-flight guard. 11:24:12 (R3 and post-sync on `b54d1b03`): pass-with-notes; R3-1 a resumed page's
  envelope comes from the measured selection; R3-2 a test for refusing a continuation that names a tree the repository
  no longer holds; unsigned tokens stay as L02 designs them; the test file's size noted.
- **Candidate invariants (not ingested; listed on the cards and in the `application` overview):** the reader never
  writes a repository, reading only the derived index and Git objects; every reader answer names the code tree it
  measured and its source; a directory view is bounded, the full subtree is paged by a continuation bound to tree,
  policy and path, and a resumed page measures at the walk's tree; a failed source is shown as partial or unavailable,
  never as empty; unconverted memory reads are unchanged.
- **Inertness:** the installed runtime does not serve the route yet (MIK-R37 cuts over). An unconverted tree answers
  `not-converted` before any index is built, and the landed routes answer byte-identically base against worktree
  (`4ab45ec3…` on the synced base `b54d1b03`, reviewer R3). Two workers built the first version (backend and
  dashboard, split in writing); from the R1 fix round one worker owned both.
- **Tests and evidence:** 21 Python cases and 14 dashboard cases; full unit suite 3,319 passed, integration lane 447
  passed, dashboard vitest 1,784 passed (reviewer R3, synced tree). Real data on converted scratch copies of the real
  repositories (SCRATCH-AUTHORED routes, decisions, incident, proof, history rows and census): the packet's conforming
  example (`worktrees/`), a file, a test file, an invariant with a seven-event three-source timeline, a family, a
  decision and its superseded predecessor, the census; the root summary's 179 subtree entries in 2 pages within 8,000
  tokens; the invariant timeline reads 7 blobs instead of about 2,590 (F1); a real-browser walkthrough at 1600×1100 and
  390×844 (task-local evidence).

- The reader's entry point: one read-only question per call, the envelope and the typed failures. [19]
- The route: 200 for typed answers, 400 for invalid requests, 503 unwired. [20]
- The Knowledge area's own statement. [21]

## 260928-MIK-L31 Focused Expression Cards In The Reviewer, Inert Until The Cutover

`260928-MIK-L31` (MIK-R31@v1) replaces the reviewer's whole-file accordion with **focused expression cards** for a
tree comparison: every code and test location of the selected family's members is one card per (path, range),
naming its role (a realization) or facet (a proof), the side path and the resolved range on each side (MIK-R08
definition 3), the authored rationale directly above an excerpt from the exact side blobs, a changed range as its
real diff and an unchanged range once, labelled and excluded from the changed count, and a not-current MIK-R03 state
when there is one. A missing rationale is an explicit gap; the renderer writes no explanation of its own. The
statements are decluttered by the ICR 13:40 decision ("Wording unchanged · revision a → b" only when every authored
field is identical; added or removed statements as labelled prose). Full-file inspection and the complete changed
inventory stay one step from every card. A dataset (unconverted) review makes no tree read and keeps its landed file
view.

- **Where:**
  - `application/review_tree_entries.py` (new) and `models/knowledge/review_tree_entries.py` (new): each entry of
    the named invariants located on B and C, with bounded excerpts and per-side state.
  - `application/review_tree_knowledge.py`, `models/knowledge/review_trees.py`, `serving/review_trees.py`: the
    on-demand `invariants=` read, the comparison pinning, snake_case on the wire, the `facts.row` history lookup.
  - `application/review_source_admission.py` and `review_source_realization_link.py`: a tree comparison's proof
    admits its unchanged path; the initialize remedy. `application/review_curator_records.py`: the Q8 fix.
  - `dashboard/src/panels/review/`: `ExpressionCards.tsx`, `focusedCards.ts`, `statementWording.ts`,
    `worklistGroups.ts`, `LeafKnowledgeChanges.tsx` (new); `FamilyReviewCenter.tsx`, `SubjectReview.tsx`,
    `ReviewWorkspace.tsx`, `ReviewExpressions.tsx`; `data/reviewTrees.ts`; `changeset/DiffPane.tsx` and
    `file-viewer/FilePane.tsx` (optional `firstLine` and `fit`, with `file-viewer/lineNumbering.ts`).
  - Fixtures: the git-trees bodies re-captured from L31's scratch leaf plus the new `gitTrees.cards` body; the six
    family fixtures L44 left at their old capture re-captured from the current route (rule 6, the L44-R1-F5
    remainder); the stale transport refusal re-measured (O2).
- **Architect rulings** (`31_focused-expression-cards.json`). Carried in: L11 (planned/unplanned marks and
  `planned_untouched` on the reviewer), L25 Q2 (the panel for MIK-R25 rules 2-3), L25 F9 (snake_case), L25 Q8 (the
  pre-existing `ValidationError`), L10 (unexplained items grouped by file and coverage), PS-1 (`facts.row`).
  2026-09-30T05:36:19: Q1 proof admission for full-file reads; Q2 the `invariants=` on-demand read (at most 500);
  Q3 a SYNTHETIC unit body for the no-member branch; Q4 roster order stays with MIK-R33 (L33); the Q8 fix and PS-1
  accepted. 06:10:21 (review R1): F1 one full file keyed by card; F2 "loaded n of m"; F3/F4/F6/F12 tests; F5 prose
  once only with both sides present; F7 re-capture with provenance; F10 each key at most 64 characters; F11 the
  comparison pinned; F8/F9 report corrections. 06:47:03 (R2): pyright clean, R2-2, R2-3, R2-5, R2-7; R2-6 accepted.
  09:38:03 (R3): pass-with-notes, R3-N1 accepted as a note.
- **Candidate invariants (not ingested; listed on the cards and in the `application` overview):** focused cards
  group by (path, range) with the rationale above the excerpt and a missing rationale shown as a gap; a card excerpt
  comes only from the pinned tree's exact blob, bounded, with per-side state; a bounded roster never reads as the
  whole family (the cards state the loaded n of m); card planning marks come only from a leaf-wide read of the same
  comparison; dataset reviews make no tree read.
- **Inertness:** only a converted leaf's tree comparison reaches the new server paths, and the dashboard asks them
  only when the payload declares `review:trees:<n>`. Unconverted reads: 26 of L25's 29 byte-identical to base, the
  other 3 being the fixed `ValidationError`.
- **Tests and evidence:** 9 new Python cases (6 in `test_review_git_trees.py`, 2 in the attributed-source module, 1
  Q8 case); 25 new dashboard cases (19 in the three new test modules), with updated expectations in five more; full unit suite 3,298 passed,
  integration lane 447 passed, dashboard vitest 1,779 passed (reviewer R3). Real data on a converted scratch leaf:
  11 cards for `FAM-2HBJREC2`, exactly 4 in `review_source_admission.py` (one changed diff, three unchanged), the
  proof card with its facet; mounted-browser screenshots at 1600×1100 and 390 against the accepted HTML (task-local
  evidence).
- **Stale comments refreshed:** a comment-only follow-up (after curation; the change set is now 46 files) made the
  headers of `ReviewWorkspace.family.test.tsx` and `ReviewReadCycle.family.test.tsx` name the MIK-L31 re-capture,
  and `familyExpressions.test.ts`'s measured-shape comment name the re-captured `walkFinal` revision `a08a87b4`.

- The entries module statement. [22]
- The on-demand cards read at the route. [23]
- The card component's own statement. [24]

## 260928-MIK-L05 Route-Chain Family Retrieval, Inert Until The Cutover

`260928-MIK-L05` (MIK-R05@v2) makes a path's leaf read also return, compactly, every live family with a route
equal to, or an ancestor of, the path's directory, even when the path realizes none of its members (D4, D12,
D20). The chain is the directory and its ancestors, computed at read time and labelled `mechanical`; each family
found is one `chain_family` row (ID, revision, title, guarantee, routes, live member count, `via`,
`memberAtSeed`, and an `expand` family seed), after the MIK-R01 content, counted toward the MIK-R02 threshold.
Each path page states `routeChain` (`governed` or `no_governing_family`); an entry-less path with a governing
family is a page stating `registration_absent`, and one with none stays refused `registration_absent` with the
same `routeChain`. A family seed (`knowledge_read` `source_context` with `familyRevisionId` and no `sourcePath`)
returns one family's full MIK-R01 content. Only `read_ar_files` may shorten a chain row already served in the
lifecycle to a `served_earlier` row; `knowledge_read` never does.

- **Where:**
  - `application/knowledge_leaf/chain.py` (new): the chain, the lookup over L23's `families_governing`, the
    compact row, `routeChain`, and the `served_earlier` rendering.
  - `application/knowledge_leaf/selection.py`, `pages.py` and `__init__.py`: the chain rows last, the family
    seed (`select_family`), `routeChain`/`registration` on path pages, `absent_chain`, policy `v2`.
  - `application/knowledge_paging/tree_read.py`: the family seed on `source_context`, the family-seed resume,
    one rule for a named revision; `application/published_intent.py`: the refusal's `routeChain`;
    `application/read_files.py`: `_chain_rendered`.
  - `models/tools/knowledge_responses.py`: the optional `routeChain` field; `mcp/registration/knowledge.py`: the
    read docstring; skill c-04 (the authored copy, the package copy and the 8 harness copies): one paragraph.
  - The knowledge index and `mcp/tools/knowledge.py` are untouched.
- **Architect rulings** (`05_route-chain-family-retrieval.json`). 2026-09-30T03:32:18 Q1 (the family seed on
  `source_context`; the old tree behaviour ignored the family, a defect; projected UUIDs accepted), Q2
  (`memberAtSeed` families keep their chain row), Q3 (nearest route then family ID; `routeChain` gives the
  directory and link count; an uncovered entry-less path stays refused), Q4 (policy `family-complete-leaf/v2`),
  Q5 (the c-04 paragraph). 04:12:49 review R1: F1 (test radon splits), F2 (a v1-policy token refused), F4
  (`familyRevisionId` spelling normalised on a family-seed resume); F3 and F6 accepted as designed; F5 (the pin
  renumbered after L10). 04:45:22 review R2 pass, R2-1 (a revision the tree does not hold is refused
  `selector_absent` on resume and fresh read alike, including a bare `ID@`).
- **Candidate invariants (not ingested):** (1) a leaf read returns the governing route chain after the leaf
  content, each chain row exactly once, within the bound; (2) a continuation is bound to tree, policy and seed,
  and resuming under another family, path, policy or tree is refused `continuation_binding_mismatch`; (3) a
  revision the tree does not hold is refused `selector_absent`, on fresh read and resume alike; (4) unconverted
  memory reads are unchanged.
- **Inert before MIK-R37:** only a converted memory tree reaches the new code. Unconverted reads were
  byte-identical to base (105,164 bytes, including a `source_context` read naming `familyRevisionId`). Real
  families have `routes: []` today, so every real read states `no_governing_family` until routes are assigned.
- **Tests:** `test_knowledge_route_chain.py` (13), lane row `:110`; `test_knowledge_leaf_read.py` adapted and split
  (13); the Forty-first catalog re-pin (`f8b04814…`). Real data on scratch clones with routes assigned in scratch:
  the conforming example `mcp/src/agents_remember/worktrees/new_helper.py` returns `FAM-QWVGDSYX`
  "attribution-and-landing-pairing" compactly; 84/84 entry paths agree across surfaces, each row once, within
  threshold (largest 7,957 tokens), chain last; 982 of 3,440 entry-less files became pages. Review R1
  pass-with-notes, R2 pass; post-sync full unit suite 3,289 passed, integration lane 447 passed.

- The chain module statement. [25]
- The compact row with its family seed. [26]
- The family seed on the mounted read. [27]
- The lane row. [28]

## 260928-MIK-L10 Unexplained Change Disposition, Inert Until The Cutover

`260928-MIK-L10` (MIK-R10@v2) makes every change the gate linkage (MIK-R08 definition 8) leaves unlinked a
worklist item that needs an authored disposition, so new code enters the knowledge graph (D8). Two kinds are
registered, `unexplained_hunk` (subject: the path plus the `sha256` of the hunk's changed lines on each side) and
`unexplained_file` (the path plus the C-side object), raised in every changed file. Coverage decides only which
record answers them: a **covered** file (a realization entry in K_B, or its governing route `migrated` in the
latest census status) takes an attach or author, which links the change, or the leaf's `no_invariant` row with a
reason; an **uncovered** file takes its onboarding trace (MIK-R30).

- **Where:**
  - `application/knowledge_worklist/unexplained.py` (new): the kinds, the coverage lookup, the items, the
    settling on the onboarding trace. `compute.py` (step 7, and delete-only linkage only through K_B), `leaf.py`
    (coverage at K_B, settling), `__init__.py` (the kinds registered on import).
  - `models/knowledge_files/unexplained.py` (new): the subjects and the gate predicate; `history.py`:
    `UnexplainedChangeRow`, the fifth row kind.
  - `application/knowledge_writer/authoring.py` (the `no_invariant` row; attach to a retired invariant refused)
    and `code_anchors.py` (`file:` subjects checked at C).
  - `application/memory_quality/controller.py`, `memory_quality/knowledge_worklist_section.py` and
    `worktrees/modules/onboarding_trace.py`: the checklist renders the items, and needed onboarding rows are not
    reported unnecessary.
  - The curator hand-off template gains the no_invariant-row bullet (all harness copies and the package copy).
- **Architect rulings** (`10_unexplained-change-disposition.json`). 2026-09-30T01:56:39 Q1 (an attach or author
  cannot answer a delete-only hunk; enforced by linkage: the item stays open and the gate refuses), Q2 (the strict
  reading of MIK-R08 definition 8 for delete-only hunks, a correction of L08: four `changeSetBar.tsx` hunks on ICR
  L47 flip to unlinked), Q3 (an onboarding row that answers an uncovered item is never reported unnecessary), Q4
  (coverage read at K_B; identical-line hunks share an item; symlinks and submodules keyed by their C tree object;
  rows answering no item reported only; item volume by design, grouping carried to L31/L32). 03:24:28 N1 (the
  complexity bar is 10 or less), N2 (the answering set is built from covered items only, so a `no_invariant` row
  about an uncovered item is reported unnecessary, report-only), N3 (the symmetric insertion-only note carried to
  L09), N4 accepted, N5 and N6 fixed.
- **Candidate invariants (not ingested):** (1) every changed hunk in range is either explained by a knowledge
  change or answered by an explicit disposition, and an unexplained hunk keeps its item open; (2) a delete-only
  hunk can be answered only by a disposition, never by attach or author; (3) `no_invariant` answers only covered
  items, and a row about an uncovered item is reported unnecessary and closes nothing; (4) unconverted memory reads
  are unchanged.
- **Inert before MIK-R37:** an unconverted leaf gets no worklist, so no item is raised on today's production
  leaves; the base and worktree builds both return `None` on the real unconverted pair, and this curation's own
  `memory_quality_check` runs returned no worklist.
- **Tests:** `test_unexplained_change_disposition.py` (10), lane row `:124`; the Fortieth catalog re-pin
  (`449b69ef…`). Real data on ICR L47 scratch clones: 160 items, `openCount` 0 after one attach and 22 rows. Review
  R1 pass-with-notes, R2 pass (R2-1 low); full unit suite 3,236 passed, integration lane 447 passed.

- The two kinds and the coverage lookup. [29]
- The subjects and the gate predicate. [30]
- A delete-only hunk is linked only by a K_B range (and, since MIK-R09, an insertion-only hunk only by a K_C range). [31]
- The lane row. [32]

## 260928-MIK-L25 The Reviewer On Git Trees, Inert Until The Cutover; The Archive Hook Once Installed

`260928-MIK-L25` (MIK-R25@v1) makes a converted leaf's review comparison four Git trees — code base, code
candidate, memory base (the worklist's pairing) and memory candidate — with the uncommitted candidates pinned by
`refs/ar/review/<task-directory>/<leaf>/<n>` before the comparison is shown, each memory side read through the
MIK-R23 derived index of its tree, and no knowledge dataset created, retained or read for a review. It adds the
tree view (the Git diff of the memory trees by record and by source path, MIK-R03 currentness per side, the MIK-R08
worklist view), historical reopen from tree ids, the legacy answer for comparisons recorded before a conversion,
and the archive hook that deletes a task's review artifacts.

- **Where:**
  - `application/review_tree_comparison.py`, `review_legacy_comparison.py`, `review_tree_knowledge.py` and
    `review_artifact_cleanup.py` (new); `review_candidate_resolution.py`, `review_committed_leaf.py` and
    `review_comparison_freeze.py` (touched); `worktree_services.py` binds the hook.
  - `models/knowledge/review_trees.py` (new): the record and the tree view's answer.
  - `serving/review_trees.py` (new), `_app_common.py`, `app.py` and `cli/dashboard.py`: `GET /api/review/trees`.
  - `worktrees/services.py` (`ReviewArtifactCleanupPort`) and `worktrees/modules/finalize.py`
    (`_with_review_artifact_cleanup` → `taskArchive.reviewArtifacts`).
  - L23's `memory/knowledge_index/projection.py`, `schema.py` (`INDEX_FORMAT` v2) and `query.py` (`record_ids`):
    the revision rows carry the store's own seal.
  - Dashboard: `dashboard/src/data/reviewTrees.ts` (adapter and hook), its test and real captured body, and
    `panels/review/ReviewSurface.gitTrees.test.tsx` with three real captured bodies and their receipt.
- **Architect rulings** (`25_reviewer-on-git-trees.json`). 2026-09-29T22:22:37 Q1–Q8 (the derived index is the
  permitted read path; the panel to L31/L32; the report location; the hook also cleans unconverted tasks once
  installed, recorded on L37; idempotent GET writes; the L23 seal fix; the K_B choice, committed rule and
  same-repository limit accepted as listed; the pre-existing ValidationError to L31) and the complexity split.
  23:15:34 F1–F9 (exact own-task selection; the hook never raises; a refused generation is held; lost code trees
  reported; one task-id function; Q5 extended to the record and caches; L37 states that archival deletes all legacy
  dataset copies including curator scratch copies; F8 accepted; key casing to L31). 2026-09-30T00:08:39 the record
  sweep removed; 01:00:07 deletion scope from the task's own identity; 01:37:42 physical confinement; 02:12:06 the
  `task.json` id confirmation; 02:32:42 review refs keyed by the task directory name only, the trust line for
  legacy cleanup, the TOCTOU window accepted, and the test split.
- **Candidate invariants (not ingested):** (1) a review comparison pins its candidates before it is shown, and a
  repeat read writes nothing; (2) archival deletes only targets derived from the archived task's own identity,
  confined to its physical folder; (3) review refs are named by the task directory name only; (4) a tree Git can no
  longer produce is reported `unavailable-history`, never substituted; (5) unconverted memory reads are unchanged.
- **Inert before MIK-R37, except the hook once installed:** every production leaf's memory is unconverted, so its
  review takes exactly the old path (29 payloads byte-identical between base and worktree, worker and reviewer R6).
  The archive hook is not gated on conversion (Q4): once this build is installed it also deletes unconverted
  tasks' legacy pins and dataset copies (65 in the ICR task on a scratch copy), which L37's cutover notes state.
- **Tests:** `test_review_git_trees.py` (13) and `test_review_artifact_cleanup.py` (14), lane rows `:122`–`:123`;
  the dashboard adapter and UI cases on real captured bodies. Review R6: pass-with-notes; full unit suite 3,231
  passed, integration lane 447 passed.

- The four-tree comparison, pinned and recorded. [33]
- The archive hook's identity sources and confinement. [34]
- The tree view route. [35]
- The index format bump for the seal fix. [36]
- The two lane rows. [37]

## 260928-MIK-L13 Decision Records With Rejected Alternatives, Inert Until The Cutover

`260928-MIK-L13` (MIK-R13@v2) adds the content rules for decision records (`ar-decision/v1`, whose shape is
MIK-R21's), the requirement-endpoint resolution the writer reports, and the curator guidance for lifting decisions
at closeout. A decision keeps the chosen alternative and the rejected or deferred ones with their reasons and
`reconsider_when`; its `links` name what it governs and, per alternative index, what should reopen it.

- **Where:**
  - `models/knowledge_files/decisions.py` (new): the pure content rules and the derived reads
    (`governs_links`, `reconsider_links` with MIK-R14's subject `reconsider:<DEC-ID>#<i>`, `superseded_by`,
    `derived_status`).
  - `memory_quality/knowledge_validator/rules_decisions.py` (new): five rules, `R13.1-alternatives`,
    `R13.1-reconsider-when`, `R13.2-superseded-derived` and `R13.3-reconsider-on` refusing, `R13.3-governs`
    report-only; imported by `validator.py` and named in the package docstring.
  - `memory/knowledge/requirement_endpoint.py` (new): locates `<coordination root>/tasks/<repository>/<path>` and
    asks the requirement owner (`consume_owner_resolution`); its only own answers are two root codes.
  - `application/knowledge_writer/requirement_links.py` (new), `writer.py` (`WriteRequest.coordination_root`) and
    `report.py` (`EndpointOutcome`, `requirementEndpoints`, `_endpoint_line`).
  - `cli/knowledge_write_route.py` and `cli/knowledge_bootstrap.py` pass the coordination root (the leaf's
    contract, the wave's admitted authority).
  - `rules_admission.py` (L27's): `_exported` is `False` for every decision (review F6).
  - Skills: the hand-off template's "Decision records (MIK-R13)" section and `roles/curator.md` step 3, synced to
    all copies.
- **Architect rulings.** 2026-09-30T01:45:56: Q1 `origin.task` plus the ruling named in the attached entry's
  evidence satisfies "origin names the task or ruling", and the `knowledge-bootstrap:<repo>` origin is valid wave
  provenance; Q2 `R13.3-governs` is report-only and a `reconsider_on` link to the chosen alternative is refused;
  Q3 the content rules apply to every decision, new or carried (the conversion exports none); Q4 packet rule 6
  (reads) is carried to L29; Q5 and Q6 are carried to L14 (reuse `resolve_requirement_endpoint`; guard
  `reconsider_on` index stability when alternatives are reordered; both met by L14, see its section above); Q7 accepted; Q8 carried to L26 (the resolver
  moves with `requirement_owner.py` if `memory/knowledge` is retired). 2026-09-30T02:05:07 (review R1): F3 the
  render helper `_endpoint_line`, so `WriteReport.render` keeps its base complexity; F4 the bootstrap-wave test
  asserts a resolved endpoint through the admitted coordination root; F6 a decision is never an export for
  admission; F1 and F2 stay with L14 and L29; F5 accepted; F7 resolved by the sync onto L06.
- **Candidate invariants (not ingested):** (1) a decision has at least two alternatives and exactly one chosen; (2) every rejected or deferred alternative
  says when to reconsider; (3) superseded is derived, never stored; (4) an unresolved requirement endpoint is
  reported, never refused; (5) a decision is never treated as an export for admission.
- **Inert before MIK-R37:** the validator runs only over converted trees, the conversion writes no
  `knowledge/decisions/` directory, and the writer's new field defaults to `None`. Base and leaf builds gave
  byte-identical `knowledge-validate` reports on a freshly converted scratch copy of the real memory, and the same
  "unconverted" line on the unconverted leaf memory. On real data (scratch only), D12 and D18 were lifted as
  decision records with 0 refusals, both requirement endpoints resolved against the real task, and a rerun wrote
  nothing.
- **Tests:** the new `test_knowledge_decisions.py` (9 cases, one `unit-regression` lane row at `:121`) and two new
  cases plus the adapted bootstrap dispatch case in `test_knowledge_writer.py`. No catalog row or re-pin.

- The content rules and derived reads. [38]
- The five registered decision rules. [39]

- The owner resolves each requirement endpoint; unresolved is reported. [40]

- The writer reports each endpoint of the records the run touched. [41]
- A decision is never an export. [42]

## 260928-MIK-L01 The Family-Complete Leaf Read, Inert Until The Cutover

`260928-MIK-L01` (MIK-R01@v2) makes a read seeded with one source path reach its whole family: from a converted
memory tree's derived index it returns the path's own invariants, every family containing them with its
guarantee and routes, every member's statement, conditions and entries, and the advertised frontier, in one
declared order -- one response when it fits the MIK-R02 threshold, otherwise pages `knowledge_read` continues.
At intake a leaf read returned 3 of 25 items and never the family.

- **Where:** the new package `application/knowledge_leaf/` (selection, pages, currentness), read through
  `application/published_intent.py` (a path seed of a converted tree) and `knowledge_read`'s `source_context`
  view with `sourcePath` (`application/knowledge_paging/tree_read.py`), with one selection under one manifest
  digest on both surfaces. `knowledge_paging/block_pages.py` takes both prepared kinds and refuses a tail too
  long for one queue (`seed_queue_exceeded`); the `invariant` view names its families; every converted-tree
  refusal names the memory tree; `application/knowledge_projection.py` projects a converted tree's views whole;
  `mcp/tools/knowledge.py` refuses a `repositoryRoot` with no commit by name;
  `memory/knowledge/read_refusals.py` names proof claims for the leaf read; the token model gains `leaf` and a
  public `MAX_QUEUED_SEEDS`; the read response gains the optional `families`. Skill c-04 names the view (rule
  6), synced to all its copies.
- **Carried obligations, all met:** the header reference as a literal first row; the 64-row projection cut
  removed on converted trees; a no-commit `repositoryRoot` refused by name; no path in continuations;
  `seed_queue_exceeded` for more than 64 queued seeds.
- **Architect rulings:** 2026-09-29 23:21:57 (Q1 a derived reference title from the statement's first
  sentence; Q2 seed invariants not repeated; Q3 proof entries seed the read; Q4 conformance by the manifest
  digest; Q5 the block's policy label; Q6 route-chain families are MIK-R05's; Q7 one declared order) and
  2026-09-30 00:08:39 (N1 radon 10 or less; N2 identity seeds on a tree keep the scope read, pinned by a test;
  N3 refusals name the memory tree; N4 one advertised row per family with `via`; N5 the block policy follows
  the seeds asked; N6 the proof wording; N9 the c-04 rewrap; the Thirty-ninth re-pin).
- **Candidate invariants (not ingested):** a converted leaf read returns the complete one-hop family
  selection, the same on both surfaces (equal manifest digest); a member already returned appears later only
  as a reference row; every page continuing a family starts with a header reference row; refusals on
  converted trees name the memory tree; unconverted reads are unchanged.
- **Inert before MIK-R37:** only a converted memory tree reaches the new code; the worker and both review
  rounds measured unconverted reads, and the 25 database projections, byte-identical to base. On a converted
  scratch copy of this repository, all 84 paths with entries agree on both surfaces and return every row
  exactly once within the threshold; the conforming example `dashboard/src/data/review.ts` is one response.
- **Tests:** `test_knowledge_leaf_read.py` (11 collected cases), the adapted L02 paging, index-reuse and
  conversion-toolchain cases, one lane row, two catalog consumer lines and the Thirty-ninth re-pin.

- The leaf package statement. [43]
- A path seed of the published-intent block is read as a leaf. [44]
- The mounted read's leaf response, of a path or (since MIK-R05) a family seed. [45]

## 260928-MIK-L06 Family Route Maintenance In The Worklist, Inert Until The Cutover

`260928-MIK-L06` (MIK-R06@v2) keeps each family's routes maintained with the code. A family becomes a
worklist item, `family_route_condition` with subject `<FAM-ID>#<condition>`, when one of its routes no longer
exists (`route_path_absent`), contains none of its realization entries (`route_emptied`, waived for an
`unrealized_family`), when an entry lies outside every route (`realization_uncovered`), or when it has no
routes (`route_unassigned`). The item is answered only by the leaf's family row with disposition `rerouted`,
`assigned`, `changed` or `retired`, never `no_impact`, while the family record in K_C satisfies MIK-R04 or is
retired. Retired families raise nothing. Nothing is rerouted automatically.

- **Where:** the new `application/knowledge_worklist/route_conditions.py` (the kind, the conditions, the
  suggestion and `family_route_item_open`); step 6 and `Item.extra` in `compute.py`, whose `_Run.document` was
  split into helpers at the merge with L11; the package exports; the checklist renderer
  `memory_quality/knowledge_worklist_section.py` (`_route_facts` and the `_FACT_RENDERERS` table); and the
  writer (`knowledge_writer/handoff.py` and `authoring.py`), whose `moved` row may now relocate an entry to
  another file through a cover `path`.
- **Carried from L04:** a dead carried route that the validator only reports becomes a mandatory item.
- **Architect rulings (2026-09-29):** 21:49:19 (Q1: reached families get all four conditions, unreached
  families only `route_path_absent` on a route killed in this leaf's range, and a route already dead at B
  stays the validator's report for R19; Q2: both route sets are judged and one family row answers all of a
  family's items; Q3: `route_unassigned` needs a non-empty route set that satisfies MIK-R04, the
  `legacy-unassessed` waiver does not answer it; Q4: a rename target is ambiguous when the renamed files land
  in more than one outermost directory; Q5: the suggestion uses the rename-mapped locations, else none, with
  `renameCandidates` and `unmappedLocations`; Q6: the writer's moved-row relocation, fixing a conformance gap
  of landed L12; Q7: recorded on L09); 22:40:22 (F1: path validation in the hand-off reader; N1: conditions
  judged at the entries' effective locations at C; N2: carried to L09; N6: complexity; N7: remove plus path
  refused); 23:14:41 (`recordSatisfiesRoutes` holds both as recorded and at the effective locations;
  `_Run.document` reduced at the merge).
- **Candidate invariants (not ingested):** a family route problem the leaf causes cannot survive closeout
  without a non-`no_impact` family row and routes that satisfy MIK-R04; a route already dead at B is not
  charged to an unrelated leaf; the stored predicate and the live `satisfiedBy` agree; the writer refuses a
  malformed cover path rather than crashing; retired families raise nothing.
- **Inert before MIK-R37:** an unconverted leaf gets no worklist. The worker's preservation runs found both
  builds returning no worklist on the unconverted pair, and on converted ICR L47 only one added item
  (`route_unassigned` for the reached exported family); this curation's own `memory_quality_check` runs
  produced no worklist.
- **Tests:** the new `test_family_route_conditions.py` (10 cases, `unit-regression`) and one case in
  `test_knowledge_writer.py`. No catalog row or re-pin.

- The module statement. [46]
- The stored predicate for the gate. [47]
- Step 6 of the run. [48]

## 260928-MIK-L27 The Admission Rule In The Knowledge Validator, Inert Until The Cutover

`260928-MIK-L27` (MIK-R27@v1) makes every **new** invariant, family and decision record state the admission
criterion it meets with a one-sentence justification (the `admission` field is MIK-R21's). The knowledge
validator refuses a new record with `legacy-unassessed`, with a justification made only of references and
provenance words, or with a `spans_locations` / `guarded_by_test` claim its sidecar entries do not support; a
record with no criterion fails the shape rule. Every other record is only reported, and the live
`legacy-unassessed` records are counted. A code change alone is never an admissible reason; a statement that
meets no criterion stays prose.

- **Where:** the new `memory_quality/knowledge_validator/rules_admission.py` (three rules: `R27.2-new-record`
  refusing, `R27.2-existing-record` and `R27.4-legacy-unassessed` report-only, none writer-reported), imported
  by `validator.py` and named in the package docstring (`__init__.py`); the criteria's meanings in the
  `models/knowledge_files/shapes.py` docstrings; the curator template's admission section, c-14 step 3, and
  the reviewer criteria's OM-4 (skills, synced to all copies).
- **Architect rulings (2026-09-29):** 22:11:24 (Q1: "supported by the index" is checked against the sidecar
  `realizes`/`proves` entries the index is built from; Q2: developer-ruling IDs and commit hashes are
  references, so a justification made only of them is refused; Q3: OM-4 enters the reviewer criteria by
  requirement; Q4: whichever of L06 and L27 lands second updates its pins for the legacy count; Q5: demotion
  details and the census outcome go to the R19 follow-up; Q6: closeout and landing validating admission
  against the parent line go to L09); 23:04:57 (F1: the tightened reference-only detector; F2: a record is an
  export only when its ID equals the converter-derived ID of its `legacyId`, and the rest of F2 goes to R19;
  F3: the CLI JSON case pins the full list; F4 already carried to L09; F5: the skill paragraphs rewrapped; F6
  noted for the L06 sync).
- **Candidate invariants (not ingested):** a new record is refused unless it carries a supported admission
  criterion with a justification stated in words; existing and exported records are only reported, never
  refused; a record counts as exported only when its ID is the one the converter derives from its
  `legacyId`; nothing is refused until records are authored on a converted line; retired records are exempt.
- **Inert before MIK-R37:** the validator runs only over converted trees. The worker and the reviewer found
  unconverted `memory_quality_check` output byte-identical to the base build, and 0 R27 refusals over a
  converted scratch copy of the real memory (108 exported records counted as `legacy-unassessed`).
- **Tests:** 9 cases in `test_knowledge_validator.py` and 1 in `test_knowledge_writer.py`; L22's and L04's
  exact pins gain the one report-only legacy count. No lane row, catalog row or re-pin.

- The admission rule's module statement. [49]
- The three registered rules. [50]
- The export test. [51]

## 260928-MIK-L11 Planned Invariant Effects Reconciliation, Inert Until The Cutover

`260928-MIK-L11` (MIK-R11@v2) lets a leaf's task document declare, before implementation, the invariant and
family effects it expects (`expectedKnowledgeEffects: [{subject, effect, requirementRef}]`, subjects
`invariant:<ID>`, `family:<ID>` or `new:<hand-off label>`). The change-to-knowledge worklist then marks every
invariant and family item `planned` or `unplanned`, raises a `planned_untouched` item for each declared effect
no history row delivers as declared, and the curator answers each with a planned row
(`planned:<declared subject>#<effect>`: `realized_elsewhere`, `deferred` or `dropped`, with a `ref`). A
`no_impact` row never clears a declared strengthening.

- **Where:** the task plane (`tasks/document.py` field and refusals, `document_field_effects.py` `NORMATIVE`,
  `task_intent.py` optional slot, `render.py` header block, the new `tasks/leaf_decisions.py` strict lookup),
  `application/task_docs/task_doc_tools.py` (`set_field`), the forms in the new
  `models/knowledge_files/planned.py` and the `planned` row kind in `history.py`, the new
  `application/knowledge_worklist/planned_effects.py` with `compute.py` step 5, `leaf.py`, `surface.py` and
  `__init__.py`, the writer (`authoring.py`, `handoff.py`, `writer.py`) and `cli/knowledge_write_route.py`
  (the task owner's decision resolver), the checklist section
  (`memory_quality/knowledge_worklist_section.py`), the curator template's planned-row bullet and the
  reviewer role's declaration check (skill l-01, synced to all copies).
- **Architect rulings (2026-09-29):** 21:56:18 (Q1: the reviewer UI is carried to L31; Q2: no real task
  document declares the field before the L37 install; Q3: the reviewer line; Q4: `new:` matches
  writer-authored invariants only; Q5: the detail choices); 22:35:34 (F1: strict leaf lookup, ambiguity
  refuses; F2: an unreadable leaf document makes the worklist incomplete; F3: the four matching assertions;
  F4: the pre-build digest mismatch goes to L09; F5, F6 accepted; F7: the stage-number merge note for L06).
- **Candidate invariants (not ingested):** with no declaration every item is `unplanned` and there are no
  `planned_untouched` items; a `planned_untouched` item is answered only by a planned row that resolves its
  ref; an unreadable leaf document never reads as "nothing declared"; the subject key is built from the
  declared subject and effect, never from list position; an absent field leaves existing task-intent digests
  unchanged.
- **Inert before MIK-R37:** unconverted leaves get no worklist; the worker (597) and the reviewer (889) found
  every real task document's intent digest, render and stored JSON byte-identical to base.
- **Tests:** `test_planned_knowledge_effects.py` (5 collected cases), one lane row, one catalog consumer line
  and the Thirty-eighth re-pin (`cb853f72…`); the history-registry case asserts four row kinds.

- The reconciliation module statement. [52]
- The declaration on the task document. [53]
- The planned row. [54]

- The task owner's strict lookup and decision answer. [55]


## 260928-MIK-L02 Bounded Continuation Accepted By The Mounted Read, Inert Until The Cutover

`260928-MIK-L02` (MIK-R02@v2) cuts every bounded knowledge read of a converted memory tree to one declared token
threshold (8,000 `tiktoken:o200k_base` tokens), and gives every page one continuation token that the mounted
`knowledge_read` resumes whichever surface minted it. The published-intent block's cursor that `knowledge_read`
refused (`continuation_unreadable`, observed 2026-09-28) is replaced on converted trees.

- **Where:** the new package `application/knowledge_paging/` (threshold, pager, bindings, scope and view
  pages, the whole-block bound, once-per-page currentness, the tree read), the token model
  `models/knowledge/continuation.py`, the seams in `application/published_intent.py`,
  `application/knowledge_read.py` (`select_knowledge_scope`) and `mcp/tools/knowledge.py`, the read response's
  `page` and `threshold`, the currentness seam in `knowledge_currentness/surface.py`, and a projection that
  continues in parts (`application/knowledge_projection.py`, refusal `oversized_row`). Skill c-04 teaches the
  route (rule 6), synced to all its copies.
- **Architect rulings (2026-09-29):** carried from L23 (`knowledge_project` never raises over 20,000
  characters); 19:56:40 (the whole knowledge block is bounded and the remaining seeds deferred; the database
  byte budget stays private until L26; `page.headerReference` is interim and L01 makes it a row; the
  threshold, not `limit`, bounds converted reads; the continuation binds the effective ordering and page 1's
  code tree; projection parts are split by the file limit); 20:40:40 (an empty `orderingInput` is refused;
  `oversized_row` only for a row too large on its own; no local path in the token; the deferred tail collapses;
  currentness at the walk's code tree, once per page, counted in the threshold; refusals state the threshold);
  21:32:34 (the binding is the Git tree ID plus a root check; the 64-seed edge is carried to L01).
- **Inert before MIK-R37:** only a converted memory tree reaches the new code; the worker and both review
  rounds measured unconverted reads byte-identical to base (305 responses in round 2).
- **Tests:** `test_knowledge_paging.py` (11 collected cases), one lane row, two catalog consumer lines and the
  Thirty-seventh re-pin.

- The paging package statement. [56]
- The mounted read's converted-tree branch. [57]
- The whole-block bound of the published-intent block. [58]

## 260928-MIK-L30 The Onboarding Refresh Gate On History Files, Inert Until The Cutover

`260928-MIK-L30` (MIK-R30@v1) builds the onboarding gate that replaces Update History and the verification
stamps once memory is converted (D23).

- **The rule:** `worktrees/modules/onboarding_trace.py`, a pure function over K_B and K_C. One
  `onboarding_trace` item per changed sidecar-stored source with a card (`onboarding:<path>`) and per nearest
  governing route (`onboarding:<route>/overview`, `onboarding:overview` at the root). An item is satisfied by
  a counted change or by the leaf's `no_impact` row; a mechanical anchor refresh (`blob`, line numbers,
  `content`) never counts.
- **The sides and the one list:** `application/knowledge_worklist/onboarding_trace.py` registers the kind,
  resolves the sides (the converted base read through the extended cache in `base_cache.py`) and merges the
  items into `knowledge-worklist.json`; `leaf.py` exposes `leaf_onboarding_trace_sides`.
- **Enforcement where today's gate runs:** `application/memory_quality/controller.py` (one repair finding per
  missing trace) and `application/prepared_certification.py` (the closeout refusal names every missing trace).
  `worktrees/modules/onboarding.py` holds the two entry points and stops stamping `lastVerifiedCommit*` on a
  converted tree; the history-order fixer is not applicable there. The writer accepts the onboarding row
  (`knowledge_writer/authoring.py`), and the hand-off template documents it.
- **Architect rulings (2026-09-29):** 18:49:50 (on converted trees only a counted change or a history row satisfies a trace, so curator-coherence no-impact judgments no longer count there; `onboarding_trace` items go into the persisted `knowledge-worklist.json`; the root route's subject is `onboarding:overview`; the converted-base cache is v2 and also holds onboarding Markdown; deleting `memory_quality/style/update_history/` is left to MIK-R37; the wiring outside the Scope list is accepted); 19:23:45 (mixed formats give an incomplete side, never a vacuous pass; items are sorted by `(kind, subject)`; a v1 cache file is ignored and rewritten; an unreadable sidecar never satisfies a trace); 19:53:54 (`onboarding_item_open` agrees with the live gate; an unreadable K_B sidecar is an incomplete input, an unreadable K_C sidecar keeps the item open, and a readable repair counts).
- **Inert before MIK-R37:** `leaf_onboarding_trace_sides` returns `None` for every unconverted leaf, so the
  installed runtime keeps today's gate; the worker and reviewer measured today's refusal and stamps
  byte-identical to base on an unconverted clone.
- **Tests:** `test_onboarding_trace_gate.py` (15 cases) and one lane row; two worklist-leaf assertions count
  the new items. No catalog change and no re-pin.

- The rule's statement for converted trees. [59]
- The memory-quality dispatch between the two gates. [60]
- The gate chooser both enforcement points share (since MIK-R09 a probe Git cannot answer is an incomplete side). [61]

## 260928-MIK-L03 Stale Invariants Flagged At Read Time, Inert Until The Cutover

`260928-MIK-L03` (MIK-R03@v2) makes every read that returns an invariant from a converted memory tree also
return its **currentness** at the requested code tree: `stale`, `unverifiable`, `unrealized` or `current`.
A stale invariant stays visible and names each differing entry; reads never write, re-anchor or judge.

- **Where:** the new package `application/knowledge_currentness/` (`observe`, `state`, `surface`), attached
  by `knowledge_read` (`mcp/tools/knowledge.py`) and the published-intent block of `read_ar_files`
  (`application/published_intent.py`), with the optional `currentness` field on `KnowledgeReadResponse`.
  The one state function is reused later by the reviewer (MIK-R25) and the reader (MIK-R29).
- **Architect rulings (2026-09-29):** the carried L28 stale-proof clause (a proof whose test changed or
  disappeared is stale); 18:42:37 (the published-intent block uses its own resolved source tree, named, with
  uncommitted edits stated as not reflected; `knowledge_read` uses only `codeTreeId`; no `HEAD` fallback);
  19:13:41 (the check order no tree → absent path → unchanged blob → unsupported locator; failures are
  `unverifiable`, never refuse a read and are never cached; the cache is bounded at 8,192 entries; the counts
  cover every invariant carried; compact entries under a read-wide reason).
- **Inert before MIK-R37:** an unconverted tree carries no `currentness`, and the worker and reviewer
  measured unconverted reads byte-identical to base.
- **Tests:** `test_knowledge_currentness.py` (13 cases), one lane row, one catalog consumer and the
  Thirty-sixth re-pin.

- The package statement. [62]
- The `knowledge_read` surface, reached through the per-page extras since MIK-R02. [63]
- The published-intent surface. [64]

## 260928-MIK-L08 The Change-To-Knowledge Worklist, Inert Until The Cutover

`260928-MIK-L08` (MIK-R08@v2) computes, for each leaf, the complete list of knowledge items its change
requires a disposition for, from the exact code and memory trees of its base and candidate (B, K_B, C,
K_C), and persists it as `knowledge-worklist/v1` beside the leaf's series contract:

- the new package [`application/knowledge_worklist/`](src/agents_remember/application/overview.md) holds the
  hunks and ranges, the entry classes, the knowledge-side changes, the item-kind registry, the one-pass
  scope, the gate linkage (every changed hunk linked or unexplained), the leaf's sides and the
  converted-base cache; the curator writer carries `carried` entries forward mechanically
  (`knowledge_writer/carry.py`);
- the curator's memory-quality run and a completed managed sync recompute it (**architect ruling 1**:
  closeout validation and landing pre-commit are L09's, through `recompute_leaf_worklist`); the checklist
  shows it as information, never counted
  ([`memory_quality/`](src/agents_remember/memory_quality/overview.md),
  [`worktrees/`](src/agents_remember/worktrees/overview.md));
- `knowledge_integrity_check` returns a leaf's latest worklist by `contractPath`
  ([`mcp/tools/`](src/agents_remember/mcp/tools/overview.md),
  [`mcp/registration/`](src/agents_remember/mcp/registration/overview.md),
  [`models/`](src/agents_remember/models/overview.md));
- the task document gains `knowledgeMaintenanceScope`, classified `LIFECYCLE` (**ruling 4**)
  ([`tasks/`](src/agents_remember/tasks/overview.md),
  [`application/task_docs/`](src/agents_remember/application/task_docs/overview.md));
- `cli/` gains [`knowledge-worklist`](src/agents_remember/cli/knowledge_worklist.py.md), the umbrella's
  thirteenth subcommand ([card](src/agents_remember/cli/__main__.py.md)).

Also ruled: the knowledge-side comparison runs in memory over the index builder's parse (**ruling 2**);
renames come from ICR's rename inference (**ruling 3**); carrying updates only this leaf's own open row
(**ruling 5**); definition 4 wins when the blob is unchanged, a partial inventory makes the run
`incomplete`, and the converted K_B is cached under the coordination runtime cache (**review R1 rulings**).
**Nothing the installed runtime does changes before MIK-R37**: the worklist is inert while both memory
sides are unconverted.

- The one recompute entry point L08's triggers call (since MIK-R09 a Git failure is named `git`; the gate recomputes over its exact candidate instead). [65]
- The CLI subcommand. [66]

## 260928-MIK-L28 First-Class Test Proofs Are Read Back And Listed, Not Yet Used

`260928-MIK-L28` (MIK-R28@v1) makes the tests that prove an invariant first-class. The curator writer
already writes them as `proves` entries (MIK-R12); this leaf reads them back and names the missing ones:

- the hand-off evidence names a test as `path::name` or, **by architect ruling**, as the pytest selection
  `path -k name` with one identifier; a test module named without a test is reported `unresolvable`
  ([`application/`](src/agents_remember/application/overview.md));
- `knowledge_read`'s `invariant` and `family` views of a converted tree carry an optional `proofs` field,
  **accepted by architect ruling**, and never present on a database read
  ([`mcp/tools/`](src/agents_remember/mcp/tools/overview.md), [`models/`](src/agents_remember/models/overview.md));
- the derived index answers `proofs_of` and `invariants_without_proof`
  ([`memory/`](src/agents_remember/memory/overview.md)), and the curator checklist lists the invariants
  without proof **as information, not a gate** (architect ruling), outside `curatorActionableCount`
  ([`memory_quality/`](src/agents_remember/memory_quality/overview.md));
- the package copy of the curator hand-off template carries the new evidence and proof guidance
  ([card](src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-handoff-list.md.md)).

**Rule 3 (proofs in change detection) and the stale-proof clause moved to L08 and L03 by architect
ruling.** No `cli/` or `kernel/` file changed. **Nothing the installed runtime does changes before
MIK-R37**: every new answer is `None` or absent for an unconverted tree and for a database.

- The two readings of proofs. [67]
- The package template copy's proof guidance. [68]

## 260928-MIK-L24 Conversion And Boundary Crossing, And The CLI Gains `knowledge-convert`

`260928-MIK-L24` (MIK-R24@v1) adds the deterministic conversion of a memory tree and its `knowledge.sqlite`
into the text knowledge format. It lives in the new package
[`memory/conversion/`](src/agents_remember/memory/overview.md), governed by the `memory` route overview.
The leaf also adds the boundary crossing: the converted base of a comparison (rule 7), and the crossing sync
in the managed sync (rule 8; see the `worktrees` route overview). It adapts the master line's toolchain to
read the converted format (rule 5: `read_ar_files`, the citation check and fixer, route indexing, memory
quality) and adds the unconverted-repository rules (rule 9). **Nothing it adds changes how the live memory
repository is read or written by the installed runtime**, and no conversion is committed to a real line
(MIK-R37 converts this master's line).

The facts that belong to this route, because `cli/` and `kernel/` have no overview of their own:

- **`cli/`.** The umbrella now registers **twelve** subcommands. The new
  [`knowledge-convert`](src/agents_remember/cli/knowledge_convert.py.md) converts a memory working tree in
  place, anchoring each card's citations at its own `lastVerifiedCommitHash` in the object store of `--code`.
  It validates the whole result before writing, refuses any conversion-format version other than `1`, and
  commits nothing. [`knowledge-ingest`](src/agents_remember/cli/knowledge_ingest.py.md) gains the rule 9
  write refusal through [`knowledge_write_route.unconverted_write_refusal`](src/agents_remember/cli/knowledge_write_route.py.md).
- **`kernel/`.** [`git_command.merge_file_bytes`](src/agents_remember/kernel/git_command.py.md) is a raw
  `git merge-file -p` that writes nothing, used for a crossing's Markdown.
  [`memory_init`](src/agents_remember/kernel/memory_init.py.md) creates a **new** memory repository with
  `knowledge/layout.json` and never marks an existing or legacy root.
  [`route_index`](src/agents_remember/kernel/route_index.py.md) feeds a converted overview's `overview.json`
  reference targets into its hot-path hints; the route indexes themselves are not converted.

**Architect rulings recorded on the cards (2026-09-29):**

- **Rule 9 refusals are inert until the official line is converted.** `unconverted_line_refusal` refuses an
  unconverted leaf tree only when its official branch tip holds the layout marker, and no line does before
  MIK-R37.
- **Legacy-format reads are active in this build.** `read_ar_files` marks an unconverted tree's onboarding
  `legacy-format` and returns no knowledge section. The taskless knowledge tools are unchanged.
- **Conversion and crossing are separate routes.** An unconverted official line, or a repository without
  one, converts by the conversion command and its normal commit route. The crossing sync is only for lines
  that descend from a converted official line.
- **No citation text is lost.** Anchor text no symbol target carries is kept in the reference's `note`.
- **Crossing conflicts are marked and reported.** A conflicted JSON item holds a `crossing-conflict`
  marker the validator refuses, and the durable crossing report lists every item with each side's value.
- **The moved markers are a list.** An `onboarding_trace` history row carries its no-impact markers in
  `markers`.
- **Conversion-format version 1 is pinned by a golden digest.**

- The umbrella registers the conversion command. [69]
- The command converts, validates before writing, and commits nothing. [70]
- The pinned conversion-format version. [71]
- A raw three-way line merge that writes nothing. [72]
- A new memory repository is created with the layout marker. [73]
- A converted overview's sidecar feeds the hot-path hints. [74]
- The rule 9 refusal for a leaf whose official line is converted and, since L37, the cutover lock for every other unconverted tree. [75]

## 260928-MIK-L12 The Curator Writer, And Two CLI Entry Points That Choose Their Writer By Memory Tree

`260928-MIK-L12` (MIK-R12@v2) adds the curator file writer, `write_knowledge`, in
[`application/knowledge_writer/`](src/agents_remember/application/overview.md) (governed by the `application`
route overview): it reads the curator hand-off document (the producer's list, or an object with `entries`,
`records` and `history`), writes every knowledge kind into the memory working tree with every mechanical field
filled, checks every row of the owner's history file against the result, and runs the knowledge validator over
the whole resulting tree; any problem or refusing violation refuses the whole operation and nothing is
written. The one definition of an anchor's `content` bytes is
[`models/knowledge_files/anchor_content.py`](src/agents_remember/models/overview.md). By architect ruling, the
database ingest and bootstrap modules are unchanged and stay until MIK-R26 (leaf L26). One fact belongs to this
route, because `cli/` has no overview of its own:

- **`cli/`.** No subcommand was added; the umbrella still registers eleven. The new
  [`cli/knowledge_write_route.py`](src/agents_remember/cli/knowledge_write_route.py.md) is the file route both
  existing commands share. [`knowledge-ingest`](src/agents_remember/cli/knowledge_ingest.py.md) loads the leaf
  contract once and, when the contract's memory worktree is converted (`knowledge/layout.json`), writes
  through the file writer as the leaf (the database-only arguments are refused by name; exit 0 written or
  planned, 1 refused, 2 invocation refused). [`knowledge-bootstrap`](src/agents_remember/cli/knowledge_bootstrap.py.md)
  gains `--wave` and writes a converted admitted memory root as that wave, with the bootstrap scope as task.
  Every unconverted tree takes the database route exactly as before.

`knowledge_change` stays registered and refusing; only its description and refusal text now name the file route
(the `mcp/registration` and `mcp/tools` route overviews). Before MIK-R37 no production memory tree holds
`knowledge/layout.json`, so no production route changes behaviour.

- The ingest dispatch on the loaded contract's memory worktree. [76]
- The bootstrap run mode's dispatch on the admitted memory root. [77]
- The layout-marker test both commands use. [78]
- The writer refuses an unconverted memory tree. [79]

## 260928-MIK-L20 The Migration Census As Files, And The CLI Gains `knowledge-census`

`260928-MIK-L20` (MIK-R20@v2) records the migration census as text files in the memory repository, under
`knowledge/census/<census-id>/`: a pinned `baseline.json` (code and memory commits), a mechanical
`inventory.json` (every in-scope source file and onboarding artifact with its governing onboarding route),
`claims/<route-slug>.json` (the legacy claims agents extracted, with append-only assessments and a
migration disposition) and `routes/<route-slug>.json` (each route's append-only status history). The four
`ar-census-*/v1` schemas live in [`models/knowledge_files/census.py`](src/agents_remember/models/knowledge_files/census.py.md);
reading, the nine census rules registered in the validator, the Doc12 measures and the report live in
[`memory_quality/knowledge_census/`](src/agents_remember/memory_quality/overview.md); the Git-reading
inventory and the checked census writer live in [`memory/knowledge_census/`](src/agents_remember/memory/overview.md).
The legacy database census tables stay until MIK-R26 (leaf L26) retires them, by architect ruling, and the
reader's census view is MIK-R29's (leaf L29). One fact belongs to this route, because `cli/` has no overview
of its own:

- **`cli/`.** The umbrella [`cli/__main__.py`](src/agents_remember/cli/__main__.py.md) now registers eleven
  subcommands. The new [`agents-remember knowledge-census`](src/agents_remember/cli/knowledge_census.py.md)
  has `inventory MEMORY_ROOT --census ID --code CODE [--code-commit REV] [--memory-commit REV] [--scope DIR ...]`,
  which pins and writes a new census into a converted memory tree (exit 2 on an unreadable baseline, 1 on a
  refused write), and `report MEMORY_ROOT [--revision REV] [--census ID] [--json]`, which only reads.

Before MIK-R37 no production memory tree holds `knowledge/layout.json`, and the writer refuses an
unconverted tree, so no production route changes behaviour.

- The subcommand registration. [80]
- Inventory pins the baseline and writes through the census writer. [81]
- The writer refuses an unconverted memory tree. [82]

## 260928-MIK-L04 Family Routes Are Validated, And The CLI Gains `knowledge-routes`

`260928-MIK-L04` (MIK-R04@v2) makes a family's `routes` checkable: each route is a repository directory (or
`.` for the repository root route) where part of the family's code lives, and the directory tree is the route
hierarchy. Six rules join the knowledge validator's one registry in
[`memory_quality/knowledge_validator/`](src/agents_remember/memory_quality/overview.md): every member's
realization lies under a route (Coverage), every route holds a realization (Non-empty), and an added route
must be a directory of the paired code tree; a carried absent route, `unrealized_family` and
`route_unassigned` are reported, never refused. The route logic lives once in `family_routes.py`, for the
validator and later for MIK-R06's route maintenance. `FamilyRecord.routes` in
[`models/knowledge_files/`](src/agents_remember/models/overview.md) now accepts `.`, and the derived index's
`families_governing` answers a `.`-routed family for every path. One fact belongs to this route, because
`cli/` has no overview of its own:

- **`cli/`.** The umbrella [`cli/__main__.py`](src/agents_remember/cli/__main__.py.md) now registers ten
  subcommands. The new
  [`agents-remember knowledge-routes MEMORY_ROOT --code CODE [--code-commit REV] [--family ID ...] [--json]`](src/agents_remember/cli/knowledge_routes.py.md)
  prints each family's routes, its route state and the mechanical route suggestion, labelled `mechanical`.
  It only reads and never writes a route (exit 0 read, 2 unreadable).

Before MIK-R37 no production memory tree holds `knowledge/layout.json` or a family record, so no production
route changes behaviour.

- The subcommand registration. [83]
- The command reads the families and prints them; it writes nothing. [84]
- The six route rules in the registry. [85]

## 260928-MIK-L23 The Derived Knowledge Index, And The CLI Gains `knowledge-index`

`260928-MIK-L23` (MIK-R23@v1) adds the derived knowledge index: the new package
[`memory/knowledge_index/`](src/agents_remember/memory/overview.md), governed by the `memory` route overview.
From one memory tree — a working tree's captured state or a Git tree read through objects — it builds an
SQLite file keyed by the Git tree id that answers every relationship lookup in both directions, and that is
also a dataset of the knowledge store's schema, so the existing read, view, comparison and scope code runs
over it unchanged. The file is cached under `<coordination-root>/runtime/knowledge-index/`, never inside a Git
working tree, and can be deleted at any time. Two facts belong to this route, because `cli/` has no overview
of its own:

- **`cli/`.** The umbrella [`cli/__main__.py`](src/agents_remember/cli/__main__.py.md) now registers nine
  subcommands. The new
  [`agents-remember knowledge-index (--memory-root DIR | --repository R --revision REV) (--cache-dir D | --coordination-root C)`](src/agents_remember/cli/knowledge_index.py.md)
  builds or reuses one tree's index and prints its key, state and counts as JSON (exit 0 complete, 1
  partial, 2 unreadable).
- **The read switch.** A knowledge read whose `databasePath` names a converted memory tree (its root, or its
  published `knowledge.sqlite` location) — `knowledge_read`, `knowledge_diff`, `knowledge_project` and the
  published-intent block of `read_ar_files` — now reads that tree through its index, and reports the tree and
  the index state; a partial index is never presented as complete. Every other path, including every
  unconverted memory root, reads exactly as before. No writer reaches the index.

Before MIK-R37 no production memory tree holds `knowledge/layout.json`, so no production route changes
behaviour.

- The subcommand registration. [86]
- The command's report and exit statuses. [87]
- The one dataset resolution every knowledge read applies. [88]
- The cache that refuses any location inside a Git working tree. [89]

## 260928-MIK-L22 The Mandatory Knowledge Validator, And The CLI Gains `knowledge-validate`

`260928-MIK-L22` (MIK-R22@v1) adds the integrity check for the text knowledge format that MIK-R21 declared:
the mandatory validator [`memory_quality/knowledge_validator/`](src/agents_remember/memory_quality/overview.md),
governed by the `memory_quality` route overview. Two facts belong to this route, because the `cli/` and
`kernel/` directories have no overview of their own:

- **`cli/`.** The umbrella [`cli/__main__.py`](src/agents_remember/cli/__main__.py.md) now registers eight
  subcommands. The new
  [`agents-remember knowledge-validate MEMORY_ROOT --code CODE_ROOT [--code-commit REV] [--base REV ...] [--json]`](src/agents_remember/cli/knowledge_validate.py.md)
  is the curator's standalone run of the validator; it only reads, has no option that skips a rule, reports
  unconverted memory as out of scope (exit 0), and exits 1 when a violation refuses the tree and 2 when an
  input cannot be read. [`cli/knowledge_format.py`](src/agents_remember/cli/knowledge_format.py.md) now uses
  the validator's `is_excluded_from_knowledge` predicate, so the formatter and the validator agree on which
  files are knowledge (a dot-named file is; a hidden directory and the `*.index.json` cache are not).
- **`kernel/`.** [`kernel/git_command.py`](src/agents_remember/kernel/git_command.py.md) gained
  `read_git_blobs_bytes`, which reads many blobs as exact bytes through one `git cat-file --batch`, and the
  private `_run_git` now encodes stdin for raw-output runs. The validator's Git tree reader is its caller.
  `git_command.py` remains the only module that spawns `git`.

The validator runs at the managed sync's memory merge through the worktree layer's
`KnowledgeValidationPort` (see the `worktrees` route overview). Before MIK-R37 no production memory tree
holds `knowledge/layout.json`, so no production route changes behaviour.

- The subcommand registration. [90]
- The command's inputs, scope answer and exit statuses. [91]
- The shared exclusion predicate. [92]
- The batch blob reader. [93]

## 260928-MIK-L21 The Package Declares The Text Knowledge Format, And The CLI Gains `knowledge-format`

`260928-MIK-L21` (MIK-R21@v1) adds the first piece of the maintained-invariant-knowledge master: the
**declaration** of the text knowledge format that will replace the SQLite store as the source of truth at
MIK-R37. It is a new model package, [`models/knowledge_files/`](src/agents_remember/models/knowledge_files/__init__.py.md)
(IDs, shared shapes, the ten record kinds, file and route sidecars, locations and schema dispatch, and the
canonical JSON formatting), and one new CLI subcommand,
[`agents-remember knowledge-format [--check] PATH...`](src/agents_remember/cli/knowledge_format.py.md), which the
umbrella [`cli/__main__.py`](src/agents_remember/cli/__main__.py.md) registers as its seventh subcommand. The
command rewrites knowledge JSON files into the canonical formatting (or, with `--check`, only reports) and
skips `*.index.json` caches and hidden directories; exit 0/1/2 means canonical / not canonical / unparseable.

**Nothing in the installed runtime reads or writes these files yet.** The package sits at the `models`
rank (no `layers.toml` change), its only production consumer is the new command, and the live memory
repository keeps being written through the knowledge store until the layout switch. The canonical curator
hand-off template (and its package and harness copies, regenerated by `scripts/sync-skills.py`) gained an
informational section mapping hand-off fields to the future files; it changes nothing a producer emits.

- The format package's own map and its shape-only boundary. [94]
- The subcommand registration. [95]
- The command's exit statuses. [96]
- The template's informational section. [97]

## Ordinary comparison recording

The installed review-record-comparison CLI remains the one review producer. Its explicit unchanged-knowledge mode supports code-only work without authored knowledge or publication. The synchronized curator and curation instructions invoke the producer and preserve its result; closeout carries that evidence without becoming a semantic approval gate.

- `add_arguments` owns the behavior described above. [98]
- `run` owns the behavior described above. [99]

## 260921-ICR-L45 The Curator Writer Stops Generating Rationale, And The Package Copies Carry The New Target Shape

`260921-ICR-L45` (ICR-R20@v1 repair, developer ruling "require rationale") changes the package in two
places. In code, the application route gains `curator_realization_authoring.py` (per-target realization
role/rationale and five named admission refusals) and `curator_stored_revisions.py` (which recorded
revisions a candidate already stores), and `knowledge_curator_ingest.py` no longer writes the generated
sentence "The statement is realized at <path>." — a new realization target without an authored rationale
refuses its entry before any identity is minted, while an already committed operation's exact retry
replays unchanged (see the application route overview). In instructions, the canonical curator hand-off
template, curator role, curation operation and `c-14-knowledge-bootstrap` procedure now require a
per-target rationale and spell a missing route by omitting `governing_route`; their package-owned copies
under `package_data/runtime/skills/` (and the eight harness starter copies) were regenerated by
`scripts/sync-skills.py`, not hand-edited, and `sync-skills.py --check` / `sync-harness.py --check` pass.
The template's element shape `{path, locator, governing_route?, rationale, role?}` supersedes rule 1's
element shape in the external schema note *260915-KS-curator-handoff-list-schema.md* revision 1, which
lives outside this repository and was not edited.

- The realization admission owner. [100]
- The admission call before minting, exempting committed allocations. [101]
- The package-owned template copy stating the superseding target shape. [102]

## 260921-ICR-L34 The Reviewer's Comparison Becomes Recordable, And A Placed Baseline Becomes Openable

`260921-ICR-L34` (D62) closes the gap the Intent Reviewer's whole knowledge column sat behind: the
package had a complete, measured **producer** of a durable per-leaf comparison generation and **no
caller for it outside the test suite**, so every leaf reopened from a bare recorded source range and
the family plane rendered its empty sheet.

**The package gains a sixth subcommand, and it is a caller rather than a mechanism.**
`cli/review_comparison_record.py` registers `agents-remember review-record-comparison` on the umbrella
CLI: required `--config` (the coordination authority the freeze reads) and required `--contract` (the
write guard — a generation is published under the task root that document records, so no argument list
can aim a record at another leaf's line), plus repeatable `--evidence` and `--historical-absence` and a
`--json` shape. It authors no knowledge, places no dataset and establishes no before half: those remain
`knowledge-ingest`'s and the first-generation owner's. It resolves the review exactly as the surface
does, names the leaf's **standing** generation as the successor's predecessor (a caller that names none
publishes an index 1 generation, and a second index-1 record under a different binding is the ambiguity
the reopen refuses by design), and prints the outcome with the freeze's own refusal fields. The
per-file detail is on the new sidecar.

**The one rule that changed: a dataset's namespace comes from the record beside its bytes.**
`review_namespace` read `candidate-receipt.json` alone. A *candidate* half has one — an admission wrote
it — but a **before** half placed by a run handed a published `--baseline` never does, because a
published dataset is not an admitted candidate: it carries `baseline-generation.json`, written by
`application/knowledge_baseline_generation`. The read therefore fell back to the requested repository
name while the bytes were bound to a namespace id, and the storage owner refused the mismatch with
`candidate_dataset_absent` (*"the candidate database is not bound to repository namespace
agents-remember"*). **Every leaf on the ordinary continuity route — `knowledge-ingest --baseline` — had
a comparison that could not be frozen**, and nothing could see it: the fixtures hand-assemble their
pairs, and the first-generation path hides it because the empty before half it creates is built by the
candidate-creation owner, which does leave a receipt beside it. The rule is now **the record beside the
bytes** — the receipt when there is one, otherwise the before half's own generation record — with the
requested repository used only when **neither** exists, which is the caller-assembled shape.

**What a reader of this package route should carry.** The Intent Reviewer's three GET routes did not
change, and neither did the resolution, the composition or the subject catalogue: what changed is that
their producer now has a caller and a placed baseline is openable, so a leaf of this master answers for
a recorded comparison instead of `candidate_dataset_absent`, and the mounted reviewer renders families,
joint guarantees, member statements, linked expressions and evidence from the record. Two limits are
recorded rather than smoothed: the producer is **live-leaf-only** (the retention owner requires a
captured candidate identity, and both closed-leaf resolutions pass `None`), so a closed leaf cannot
publish; and the new command is **not idempotent as its own docstring claims** — `lineage` sits inside
the seal, so naming a standing generation changes the derived id and an ordinary retry appends a
successor rather than reusing the record. Both are carried on the new sidecar and in this leaf's
curation report for the next leaf.

- **The `review-record-comparison` subcommand: the adapter's registration on the umbrella CLI, and the declarative pair it uses.** [103]
- **The run this command is: the argument-list answer, the standing generation named as predecessor, the request from the contract's own identities, the one freeze call and the outcome as an exit code.** [104]
- **The record-beside-the-bytes namespace, corrected in place: the receipt when there is one, otherwise the before half's own generation record, and the requested repository only when neither exists.** [105]
- **The seal's omission set, which is why naming a predecessor changes the derived id — the fact behind the carried non-idempotence limitation.** [106]
- The case that protects the corrected namespace rule on the real placed-baseline journey. [107]

## 260921-ICR-L32 The Repair Leaf: The Seat Policy Moves, And Two Long-Route Defects Close

`260921-ICR-L32` is a repair leaf, so this route's own record is about what it closed rather than what it
delivered first.

**The taskless admission now includes the curator (D56).** `serving/task_binding.py`'s `TASKLESS_SEAT_ROLES`
is `{chat, terminal, bootstrap, curator}` — the developer's 2026-09-24 ruling — and the route-level case
pins the whole status table rather than the constant. The package half of the coupling is **generated**: the
six instruction carriers under `mcp/src/agents_remember/package_data/runtime/skills/` were rewritten by
`scripts/sync-skills.py` from the canonical `skills/**` tree and all nine targets report `ok`. The L27
section below, which correctly said this constant was **not** modified by **that** leaf, is history and not
current policy.

**The write plane is named by both its entry points (D55).** The mounted refusal's description and the module
comment above it now say one writer and **both** shipped CLI entry points; the singular form was true when
`ICR-R20@v1` landed it and incomplete once `ICR-R29@v1` shipped the second, and the sentence was completed
rather than deleted.

**Two test-side moves reach this route.** `mcp/tests/test_curator_family_authoring.py` is split (1320 → 818
plus a 578-line sibling, `test_curator_ingest_write_and_retention.py`), so the ≥1200 census is back to its
pre-L28 value in both scopes while the catalog keeps **16 contracts / 66 artifacts**; and the D02 NUL-safe
Git family's cases live in `test_master_net_generation.py` over an eight-name fixture that includes a literal
backslash on each side.

## 260921-ICR-L27 The Package Publishes A New Procedure, And Its Generated Copies Carry It

`260921-ICR-L27` (`ICR-R27@v1`) delivers `c-14-knowledge-bootstrap` — the procedure that authors a
repository's first or resumed **knowledge foundation** — and it reaches this package through the
**generated** route rather than by a hand edit here. The canonical instruction home is root
`skills/c-14-knowledge-bootstrap/SKILL.md`; `scripts/sync-skills.py` copies the root `skills/` tree into
the package-owned copy at `mcp/src/agents_remember/package_data/runtime/skills/` **and** into the eight
harness starter packages (`.claude/`, `.codex/`, `.cursor/`, `.github-vscode/`, `.hermes/`,
`.openclaw/workspace/`, `.pi/`, `.agents/`) — nine generated targets, and a change is made in the root
and propagated by running the generator.

**What this package's route owns in the delivery.** The served catalog is the delivery route: a session
does not read `skills/` directly, it lists what the MCP server publishes and reads one entry back. The
new procedure must therefore appear in that catalog, and the bytes a reader receives must be the
canonical tree's — a stale or hand-edited copy would be indistinguishable, from inside a session, from
shipping the wrong instruction. The leaf pins that by comparing what the catalog serves with `skills/`
rather than trusting it, and by running every invocation the procedure prints through the shipped
parser.

**The package-side consequence of the admission gate is unchanged code, not new code.** The procedure's
entries are the product's real ones because the opener admits a role with no task document only for the
taskless seats; the constant behind that gate (`TASKLESS_SEAT_ROLES` in
`mcp/src/agents_remember/serving/task_binding.py`) is **not** modified by this leaf, so the procedure is
corrected to the product rather than the product to the procedure.

**Where the route's own files changed**, the change is in test evidence registration rather than in
production code: `mcp/tests/test_knowledge_bootstrap_procedure.py` is new (453 L, seven cases), and the
two evidence-lane TOMLs gain their consumer rows. Those row additions shift the line numbers of the
tables they are inserted into, which is why cards citing those TOMLs by line were re-anchored in the
same pass.

## 260921-ICR-L28 The Package Gains The Curator's Two Planes, And One Report Carries Both

`260921-ICR-L28` (`ICR-R28@v2`) gives the MCP package the owners that carry a curator's **authored
family plane** and **external-source plane** into the knowledge dataset. Five new modules under
`application/` (`curator_family_authoring.py` 539 L, `curator_family_planning.py` 766 L,
`curator_family_coverage.py` 287 L, `curator_ingest_planes.py` 285 L, `curator_source_manifest.py`
456 L), one new test module (`tests/test_curator_family_authoring.py`, twenty cases), and the wiring in
`application/knowledge_ingest.py`, `application/knowledge_curator_ingest.py` and
`cli/knowledge_ingest_report.py`.

**The wiring is thin on purpose.** `knowledge_ingest.py`'s `CuratorEntry` gains two fields — the
resolved `family` authoring and `replayed` — and `curator_entry_commands` delegates the family
commands to `curator_family_planning.family_commands`; `curator_command_list` becomes the **one**
composition of a whole list's commands, separable from the batch so the operation can ask what the
batch *would* carry. The two identity commands (`add_family`, `add_family_revision`) are hoisted to the
front, because a membership checks its family-revision endpoint against the rows that exist at that
instant and the producer's entry order says nothing about that.

**The report carries two new blocks.** `cli/knowledge_ingest_report.py` renders `family` and `sources`
in the JSON payload and one summary line each in the human text, each plane with its **own** state
(`recorded` / `projected` / `not-recorded`). A plane that did not record reports null counts, never
zeroes that would read as a measured empty result.

**A closed defect this route must keep visible.** The operation could report `recorded` / `authored` /
`added` over a store holding zero family rows, because the replay short-circuit asked the
*invariant-revision* replay set instead of the batch. `knowledge_curator_ingest._run` now short-circuits
on `read.planned and not pending`, where `pending` is the command list the batch would carry; the route
leg, the commit and the receipt counts all use that one predicate; and `_record_what_the_batch_will_write`
records the allocation journals and the manifest only for a run that writes something, so a
non-committing run cannot burn a family identity or report a digest for bytes no reader can find.

**Catalog accounting.** The new test module took its existing lane row and two consumer rows in
`evidence-lifecycle.toml`; no byte or count of a catalog is pinned. Nothing else in the package's public surface moved: no tool name, response model or refusal
code changed.

## 260921-ICR-L14 The Review's Record Collection Gets One Production Owner, And An Empty Tuple Stops Meaning Three Things

`260921-ICR-L14` (primary requirement `ICR-R14@v1`) adds **one `application/` owner, one `models/`
vocabulary module and one case module**, and changes the production dashboard composition's record
loader. At this altitude the package-wide facts are three:

**The record half of a review now has an owner of its own.** `application/review_evidence_records.py`
resolves, for one resolved candidate, **every** owner-produced collection — the curator authority's
published assessments, the detection owner's signals, the evidence owner's verification observations and
evidence claims, and the review matrix's authored effects — plus the one quantity nobody in that
composition measures (dependency currentness). The resolver used to be a private function at the bottom
of `application/knowledge_review.py` that read the assessments and returned an empty collection for an
absent *or* unreadable authority; that body is gone, the adapter re-exports the name from its new home,
and the adapter is **831 → 819 lines** while gaining the channel assembly. No second store, no second
reader of an owner's tables and no re-derived content: every collection is the owner's own answer.

**Availability became a fact per collection rather than an empty tuple.** The new
`models/knowledge/review_records.py` declares `ReviewRecordChannel` with five states — `recorded`,
`none_recorded`, `unavailable` (with the owner's own refusal as provenance), `not_measured`,
`not_selected` — and its validator makes "a count nobody measured" unrepresentable: an unreadable
authority carries no count, and every non-answer must say what would produce one. The vocabulary is
carried on the bundle and on `ReviewEvidencePane.channels`, whole and underived. The vocabulary was
extracted from `models/knowledge/review.py` (which had crossed the 900-line soft rail at 940 and is 851
now) and re-exported from it, so no importer moved.

**Two owners on the memory route gained an identity listing, so a damaged record is named rather than
fatal.** `detection.recorded_run_ids` and `evidence_records.claim_ids` list identities without decoding,
and the composing reader then reads each record through that owner's own single-record reader — the
reason one damaged detection run, or one claim whose payload no longer decodes, is named on its channel
(`unreadable`) while its siblings are still supplied. Each is a split rather than a second reader:
`all_claims` and `read_detection_run` are unchanged.

The ten cases live in `mcp/tests/test_knowledge_review_evidence_channels.py` and drive
`cli.dashboard.serving_collaborators`, so the packet's failure — a production port supplying only
assessments while claiming a complete bundle — is caught at the composition rather than at the resolver.

- **The production record owner: five collections and one measured currentness channel, each read through its owner.** [108]
- **The per-record guard and the two identity listings it composes.** [109]
- **The availability vocabulary and the field that carries it on the served payload.** [110]
- **The production port the cases drive, and the two states F09 collapsed.** [111]
- The two per-record damage cases, and the task-context collection that reports `not_selected`. [112]

## 260921-ICR-L11 The Package Gains The Durable-Comparison Chain, And Two Typed Failures Beside The Candidate's

Six production modules and one test module arrived on this package route with `260921-ICR-L11` (primary
requirement ICR-R11@v1), whose obligation is that **a frozen comparison retains resolvable source,
knowledge and evidence inputs through cleanup and restart**. Five are `application/` owners — the record,
the freeze, the retention, the reclamation and the reopen — and one is
`worktrees/modules/code_object_retention.py`, the Git-object retention they depend on. Each has its own
file-level card and its own route section; what belongs at this altitude is the shape of the chain and
the one package-wide fact it adds.

**The chain, in one line each.** `review_comparison_generation` owns *the record* (an immutable manifest,
its layout under `<task_root>/notes/reports/`, the unavailable-history record and the reads);
`review_comparison_freeze` owns *the act* (resolve and compose exactly as the surface does, stage, read
every referenced byte back, seal, and publish by **one rename**); `review_comparison_retention` owns
*where the bytes come from* (custody measured against named durable history only, both knowledge halves
copied by the storage snapshot owner); `review_comparison_reclamation` owns *the two operations that may
delete them* (record first, measure the deleted digest, never alias today's data); and
`review_comparison_reopen` owns *the read-back* (one state per channel, never one verdict). The chain
composes owners that already existed and adds **no second store, no second capture path and no second
measurement**.

**The package-wide fact: two typed failures joined `errors.py` beside `FutureCodeCandidateError`.**
`CodeObjectRetentionError` (retention could not be created, or was not released) and
`ComparisonReclamationError` (a durable artifact could not be reclaimed as its own record describes it)
are ordinary `AgentsRememberError` members, each carrying a machine-readable `status`. They are **raised
rather than returned** at two different boundaries: a retention failure happens inside a publication that
has not happened yet, so the freeze converts it into a typed refusal; a reclamation failure happens at a
deletion, where a returned value would make "nothing was removed" easy to overlook at the one
irreversible step. The insertion is **not additive at the tail** — it lands at `180`, so every class
below it moved, and the citations into `errors.py` held by this package's cards were re-derived rather
than shifted.

- **The keystone record: the manifest, its layout under the one durable root, the re-derived id and the directory-name agreement.** [113]
- **The production entry and the one-rename publication.** [114]
- **Custody over named durable history only, and the two snapshots copied by the storage owner.** [115]
- **The two deletion owners and the record that precedes every deletion.** [116]
- **The read-back: per-channel states and `unavailable_channels()`.** [117]
- **The Git-object retention member this route's `worktrees/` gained.** [118]
- **The two typed failures, and the two boundaries that decide why they are raised.** [119]
- **The one durable-root owner the layout asks instead of restating.** [120]
- The fifteen production-composition cases that measure the chain end to end. [121]

## 260921-ICR-L6 The Review Surface's Statement Sides Get An Owner, And A Served Field Value Stops Reading As Absent

One route-level fact this package route now carries, and one served-value change a consumer of the
Intent Reviewer's payload should know about.

**The fact.** `mcp/src/agents_remember/application/review_statement_sides.py` is a new module on the
application route and the owner of the review surface's pane-1 statement-side data contract: what a
statement side is (three outcomes — `absent`, `unresolved`, `present`+text — read from the comparison
item rather than inferred from empty text), the essential conditions each side recorded, the
comparison's own mechanical field roster, and the value reader that reserves `None` for absence.
`application/knowledge_review.py` delegates to it (888 → **831 lines**) through one import block and
four calls inside `_knowledge_pane`; the adapter keeps its composition, and this is the **fourth**
responsibility it has handed out on this master line and the only one that leaves no alias, because no
module under `mcp/` imported the old private names. The rendering half of the same rule lives in
`dashboard/src/panels/review/KnowledgeStatements.tsx`: a knowledge addition or removal now draws the
complete available statement beside a **named** absent side, and a side that is `binary`/`unresolved`
draws its available text with its reason and no diff, instead of the whole statement disappearing.

**The served-value change.** `ReviewFieldChange` reads `None` on either value as the recorded fact that
the field was absent on that side. The base value reader returned `None` for any structured value, so
a **changed** structured field — `provenance` is the shipped one — was served as `None` on both sides:
an absence the snapshot does not hold, stated twice, in the one slot reserved for absence. Each side
now carries the pane's own text projection of the value it really holds (canonical compact JSON,
bracketed with `<recorded as a structured value, rendered as compact JSON: …>` and bounded with a
visible truncation). That is a value change inside an existing field, not a wire-shape change: no new
field, no new type and no transport change, and `models/knowledge/review.py` is untouched.

- The new module's whole surface, and the rule that a side's state is read rather than inferred from an empty string. [122]
- **The projection that keeps a present structured value out of the absence slot, and the contract that makes `None` mean absence.** [123]
- The adapter's delegation, with the composition unchanged. [124]
- **The served-value change measured through the real composition.** [125]
- The added and the removed statement, each keeping its complete available text beside the named absent side. [126]
- The renderer that decides the four branches from declared state. [127]

## 260921-ICR-L20 The Ingest Publishes To The One Location The Read Route Declares, And Reads It Back

Two route-level facts this package route now carries, both inside the curator write plane and neither
public: no advertised tool name changed, no response model changed and no refusal vocabulary moved —
the mounted `knowledge_change` docstring gained a sentence naming the ordinary route, and that is the
whole of this package's public-surface delta. The per-file detail lives in the new sidecars for
`mcp/src/agents_remember/application/knowledge_publication_route.py`,
`mcp/src/agents_remember/cli/knowledge_ingest_report.py` and
`mcp/tests/test_knowledge_ingest_publication_route.py`, and in the reconciled sidecars for
`mcp/src/agents_remember/cli/knowledge_ingest.py`, `.../application/published_intent.py` and
`.../mcp/registration/knowledge.py`.

- **The write side reached the read side's location, and it is one spelling.** `--publish` selects the
  repository's declared published dataset (`<this enclosure's resolved memory root>/knowledge.sqlite`),
  resolved through `application/published_intent.published_dataset_path` for the enclosure's own
  coordination context — the same declaration the ordinary read resolves. A caller-named `--publish-to`
  is the other selection and the two are mutually exclusive; `--commit` stays the knowledge-batch write
  word and does not imply a publication.
- **What the run admits at that location is derived, not typed.** When `--baseline` names the declared
  location, the bytes the run captured at the top of the run are the dataset standing there, and their
  identity is the one the publication may replace: that is the explicit update. Every other case is
  admitted as holding nothing, and the publication owner refuses by name if it holds something.
- **A successful exit is not a publication claim, and the report says which it was.** `publicationRoute`
  names the destination selected (or that none was), `publication` carries the owner's own result, and
  `publishedIdentity` is an independent read of the location through the reader's owner
  (`confirmed` / `mismatch` / `unavailable`). A refused publication is read back not at all, because it
  established nothing about the destination.
- **The CLI kept the decision and gave up the shape.** The CLI owns the selection and its three
  invocation refusals; the *meaning* of the declared selection lives in the new application module; and
  the 135-line report renderer moved to `cli/knowledge_ingest_report.py`, so the CLI's growth to 692
  lines is R20's own decision surface rather than absorption. This is the same "keep the adapter a
  delegator" rule this route applied at ICR-L1 and ICR-L18.

- **The declared location, resolved through the read route's own owner, and the context that keeps the read-back in the scope the write was made in.** [128]
- **The admission as four ordered facts, the fourth of which is the ordinary update.** [129]
- **The read-back through the reader's owner, and the three states the report carries.** [130]
- **The destination selection the CLI owns, its refusals, and the route line it completes from the run's own report.** [131]
- **The renderer that left the CLI, and the two fields this leaf added to the caller's answer.** [132]
- The mounted refusal that now names the ordinary publication beside the writer, and the operation whose docstring carries it. [133]
- The declaration this route resolves against, whose own docstring and constant comment this leaf restated as current truth. [134]
- **The cases that drive the whole route through the shipped CLI over a production-shaped enclosure.** [135]
- The lane row the new module occupies and the two governed consumer rows it joined. [136]

## 260921-ICR-L18 The Review's Before Half Gets A Generation Owner, And The Ingest Fills It Once

Two route-level facts this package route now carries, both inside the curator write plane and neither
public: no advertised tool name, no response model and no refusal vocabulary moved. The per-file detail
lives in the new sidecar for `mcp/src/agents_remember/application/knowledge_baseline_generation.py` and
in the reconciled sidecars for `.../knowledge_before_half.py` and `mcp/src/agents_remember/cli/knowledge_ingest.py`.

- **A comparison's before side is now a recorded generation rather than whatever the latest run was
  handed.** A run whose `--baseline` differs from the dataset the comparison already opened on places
  nothing: it names the generation the half holds, that generation's dataset identity, and the explicit
  `--rebase-baseline` action that begins a new one. Without that argument the original baseline is kept,
  which is what stops a second successful write from re-filling the half with the first run's own
  publication and reporting the addition the review exists to show as present on both sides with an
  empty delta.
- **A deliberate rebase is a new generation with lineage, and its failure window is bounded by an
  ordering.** The replacement record is durable **before** the bytes it names, so the one window a rebase
  can leave is the previous bytes beside a record that disagrees with them — the named `damaged` reading
  — and never replacement bytes with no record, which would read as the comparison's original. A failure
  line names the leg that refused *and* re-reads the half, because the write owner flushes the directory
  after the rename and a leg can therefore fail after its bytes landed; both leg clauses say only "did
  not report success" rather than claiming a byte outcome the caller never measured.
- **The CLI gave up a responsibility it should not have owned.** The placement machinery that used to
  live in `cli/knowledge_ingest.py` moved into the new application owner, and the CLI is **541 lines**
  where it was 620. What stays there is the one question only the run's own report can answer —
  *whether* this run may fill anything — plus the invocation refusal for `--rebase-baseline` without
  `--baseline`.

- **The application owner that decides what a before half is afterwards, and the four ordered answers behind that decision.** [137]
- **The recorded generation, the four-state read of what the half holds, the one first placement, and the deliberate rebase with lineage.** [138]
- **The two publication legs whose order is the failure contract, and the read-back that states what the half holds when one refuses.** [139]
- **The CLI's one remaining placement question, the handoff that delegates the rest, and the new argument with its invocation refusal.** [140]
- **The run that reaches that handoff is the database route: since `260928-MIK-L12` `run` first sends a converted memory worktree to the curator file writer.** [141]
- The sibling owner the half's layout and provenance record stay with, whose docstring was reconciled by this leaf to state the one-record rule. [142]
- **The successful journey and the failure windows, driven through the shipped CLI on real enclosures.** [143]

## 260921-ICR-L5 The Cold-Start Ingest Establishes A Before Half, And A Selected One Is Read On Every Run

Two route-level facts this package route now carries, both inside the curator write plane and neither
public: no advertised tool name, no response model and no refusal vocabulary moved. The per-file detail
lives in the sidecars for `mcp/src/agents_remember/application/knowledge_before_half.py`,
`.../knowledge_first_generation.py`, `.../knowledge_curator_ingest.py`,
`.../knowledge_review.py` and `mcp/src/agents_remember/cli/knowledge_ingest.py`.

- **A repository's first knowledge write now has a truthful before side.** A cold-start
  `knowledge-ingest` run that names no `--baseline` used to commit its candidate and leave the review's
  before half absent, so the review refused the pair and the first invariant a repository ever recorded
  could not be displayed as an addition. The run now *establishes* the half as an explicitly identified
  empty first generation — a schema-valid empty dataset in the candidate's own namespace, built by the
  shipped creation owner and exposed atomically, with `baseline-origin.json` beside it recording the
  generation, the code base the run observed, and that pre-feature history is not recorded. The
  populated candidate is never copied backward as its own origin.
- **A *selected* baseline that is missing or corrupt is a different fact and is never answered that
  way.** It is the shipped `selected_input_unavailable` refusal naming the path and the reason, and the
  read now happens on **every** run — resume included — because reading it only on the clone path made
  a corrupt fork point invisible exactly where a later run would go on to act on it: the run committed
  and the before half was then reported *placed* from bytes that were no longer a dataset. The
  operations this route gains are the two new application modules; `application/knowledge_review.py`
  gained one import and two call sites so a present-but-unreadable side is a named refusal on both the
  composition and the entry list.

- The before half's owner: its layout, its origin record, its four states and the one refusal. [144]
- The establishing operation, and the admission it reads from the committed candidate's own record. [145]
- **The admission's read of a selected baseline, taken before anything else is decided and on the resume path too.** [146]
- **The CLI's two filling paths behind one placement gate, and the cold-start branch.** [147]
- The two adapter call sites that state the unreadable-half refusal on both routes. [148]
- The cases that measure the operation at the CLI and the surface's before half. [149]

## ARSPAWN-L4 Public Advertisement And Starter Contract

The MCP public surface is now reconciled through one permanent validator over public FastMCP APIs:
the exact ordered `PUBLIC_TOOLS` inventory, live registration, response models, and the closed
`dispatch_agent` schema/description must agree. MCP `server_info` and dashboard served state share
one process-scoped, content-addressed Python candidate identity so an equal-version stale artifact
cannot pass as the code under review.

260831-LOCR-L37 added one advertised name to that inventory — `worktree_pause`, the stop-only pause
registered by the working-half worktree registrar and carried by `PUBLIC_TOOLS` and
`TOOL_RESPONSE_MODELS` in the same leaf — so the ordered inventory, the live registration and the
response-model registry agreed at 63 names from that leaf until 260915-CAPS-L4 raised the count. The
verb publishes nothing: it releases one atomic
master's activation selection and hands the turn back, and the explicitly requested publication of an
unfinished master remains the separate `worktree_checkpoint_landing`. This package route owns the
advertisement of both; the semantics live on the `registration/`, `tools/` and `worktrees/` child
routes.

260915-CAPS-L4 added three more advertised names — `role_capsule_compile`, `skill_catalog_list` and
`skill_catalog_read` — so the three surfaces still agree at **66** names. They are declared by the new
`mcp/registration/capsule_serving.py` family (the thirteenth registrar), reached through the new
`mcp/tools/capsule_serving.py` payload builders, and carried by `RoleCapsuleResponse`,
`SkillCatalogListResponse` and `SkillCatalogReadResponse` in `models/role_capsule_resources.py`. All
three names were **appended** to `TOOL_REGISTRARS`, `PUBLIC_TOOLS` and `TOOL_RESPONSE_MODELS` together,
so no existing tool's advertised position moved.

That same family also made this package advertise **MCP resources** for the first time, and it carries
the SEP-2640 skills transport: every file of the 14 shipped skills plus this server's own
`skill://index.json` resource (85 registered resources), the `io.modelcontextprotocol/skills` capability
declared in the `initialize` result, and the extension's **two mandatory protocol methods**
`skills/list` and `skills/get`. The methods are implemented in
`mcp/registration/skills_extension.py` as bounded explicit method support, because the pinned
`mcp==1.29.1` SDK has no skills affordance at all (zero case-insensitive `skill` matches, no
`extensions` field on `ServerCapabilities`, and an unmodelled method refused with `-32602`).
`skill_catalog_list` and `skill_catalog_read` are this server's own tool reads over the same registry
for a client that is not resource-aware. The resources are read from the package's generated
`package_data/runtime/skills/` copy rather than the canonical root `skills/` tree, which is what makes
a served revision reproducible.

Two distinctions a reader of this route must not flatten:

- **The declaration is a commitment.** SEP-2640 §Capability Declaration: *"declaring the extension
  itself commits the server to `skills/list` and `skills/get`."* The capability is therefore installed
  in the same function that installs the methods, so the advertisement cannot outrun the implementation.
  A round-1 candidate declared the capability and answered neither; that gap is what the review blocked
  on and what the shipped code closes.
- **`skill://index.json` is this server's own convenience resource, not the extension's enumeration
  surface.** SEP-2640 enumerates through `skills/list`, whose entries carry verbatim frontmatter and
  per-file digests; the index keeps the Agent Skills well-known-discovery shape and its wire description
  says so.


The same canonical dispatch-advertisement validator is reusable at real-client boundaries that
expose only one deferred tool-search result. The Codex clean-room proof therefore records the exact
schema digest and caller-boundary description accepted by the full MCP validator; it does not own a
second, weaker schema interpretation.

Starter policy remains self-updating by design. Claude, Codex, Cursor, VS Code, Hermes, OpenClaw,
Pi, and Antigravity all retain `uvx --refresh-package agents-remember-mcp
agents-remember-mcp@latest`. Only the disposable acceptance process pins exact local source, because
launching `@latest` there would certify PyPI instead of the candidate. These are complementary
proofs, not alternative starter strategies.

## IAS Contract-Scoped Activation Boundary

Task documents remain upstream canonical planning truth and are always authorable. A task mutation
never waits on queue or atomic-series activation state: it publishes first, invalidates semantic/readiness-affected
disposable scheduling projection, and lets current waiting candidates be recomputed.

Atomic implementation admission uses one replace-in-place activation record per canonical series
contract, addressed by a fingerprint of that contract path. Multiple live series are normal, and
because the record is per contract rather than per protected source pair, two atomic masters that
share one sprint's code and memory source branches keep independent records: neither one's
`reconciling` or `active` state pauses the other. A contract remains `reconciling` until a
contract-addressed sync brings the exact code/external-memory base pair current, and only then
becomes `active`. The only activation waiting reason is `atomic-series-reconciling`; a vacant,
`active`, or foreign-master record is never this contract's reason to wait, and a record that does
not name the addressed contract is unreadable rather than adopted. Genuine Git conflicts are
retained in an operation-owned worktree and stable enclosure-root journal for agent resolution,
continuation, or explicit cancellation.

The activation record is not a lifecycle ledger, and the queue owns no claim, commit, certification,
integration, recovery, or terminal evidence. Terminal cleanup vacates only an exact selected owner
before its canonical contract pointer is deleted. Normal readers never fall back to task prose,
queue rows, old files, or ambient Git when activation/journal authority is absent or unreadable.
The focused route owner is [worktrees/overview.md](src/agents_remember/worktrees/overview.md).

## Computed Memory Ledger For Consumers

The external-memory ledger remains a newest-first consumer view of reachable memory commits and their `Code-Commit:` trailers. Repeated code revisions can have later memory states without deleting older attributed history. `kernel/memory_ledger.py` owns the row format, `kernel/memory_attribution.py` owns Git attribution, and `kernel/memory_cache.py` derives and materializes the disposable cache. Cache rows never become a second source of mappings or a prerequisite for Git publication.

## L3 Canonical Scheduling-Register Boundary

The closeout queue consumes sprint judgments only from the exact orchestration-task Judgment and
Priority Register sections. Their template headings, headers, rectangular separator rows, and
outer Markdown pipes are part of the authority grammar; width-shaped prose or malformed table
rows fail closed before they can grade or order a candidate. Since 260815-DAG-L13 the fail-closed
side is the write/mutation path: sprint creation scaffolds the empty canonical registers,
`task_doc` writes validate register shape, and the queue's `status` read instead degrades to a
facts projection (absent/ok/malformed per register). Graph-less sprints project the
atomic-sequential default — the sprint's shape, in which every commanded master executes
atomically — and it serializes nothing: the sprint declares no dependencies, so no master is held
because another is selected, and activation waiting reasons come per contract from each canonical
series contract's own activation record (a vacant, `active`, or foreign-master record is never this
contract's reason to wait). A real authored graph still gates its masters on genuine predecessors.
The retired series-lane owner is not reconstructed.

## Current Structural Agent Boundary

Agent-facing dispatch, messaging, seat management, and gates use canonical task documents and roles.
A plane-injected hosted seat proves the caller. An ambient launcher has no plane identity and does
not declare a caller role in request data; the process-derived absence of plane identity selects the
ambient authorization branch. `dispatch_agent` is the one public spawn tool for both caller kinds:
ordinary role-shaped work targets the sprint architect with the canonical pinned brief, while an
explicit developer-declared task-seat takeover may target the named role at its canonical task
altitude. Ambient dispatch has no parent seat or child-scope authority. Plane dispatch uses the
injected seat and exact structural direct-child scope, and a plane refusal never falls back to the
ambient branch. `spawn_agent_session` remains an internal primitive only. Runtime
session/lifecycle/gate/inbox identities stay plane-only. Role-table `dispatch` and `tools` rows are
structural authority/capability descriptions, not settings keys. The application resolves
authorized parent/child seats and current occupants, with one internally exact-pinned initial brief
and replacement-aware ordinary messages. Startup migration is one-way before strict current
readers; there is no public exact-id compatibility surface.

## Historical milestone context: 260821-ARSPAWN-L2 Idempotent Structural Dispatch

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The one public `dispatch_agent` operation now converges on the canonical task-document-and-role
seat for both ambient and plane callers. A bounded per-seat serializer covers spawn, durable
pinned-brief publication, receipt repair, and one proven-failed-generation replacement. Unknown
or contradictory post-commit state refuses without cleanup. Ordinary messages remain address-only
and re-resolve the incumbent or staged heir at delivery; public outcomes omit runtime occupant ids.

## Development And Certification Policy

Ordinary Python development is supported directly through `mcp/.venv/bin/python -m pytest`; four workers run the isolated unit population. `-m integration` selects the small real-boundary population and `-m ""` selects both. Focused file/node execution, including serial debugging, is valid development work and does not acquire certification authority. The repository declares `unit_case_budget = 4000` and `integration_case_budget = 1000` parametrized collected cases (`pyproject.toml:278-279`), raised from 3000 / 600 by the 260918-TSIP-L13 budget-and-landable-closeout leaf on 2026-09-20 under a second direct developer decision — the pair before that having been raised from 2300 / 400 by the 260918-TSIP-L7 agreement leaf under a direct developer decision. Extend or consolidate distinct behavior protection before adding cases; do not restore deleted matrices, private-branch tests or unused fixture machinery because an old milestone names them.

Coverage, including changed-line coverage, is diagnostic only. No percentage floor requires additional tests. Production-only CRAP retains 20 as a review trigger, not a delivery blocker; tests and verification support are excluded. Lint, formatting, typing, structural rules and test failures still enforce. Diagnostic-tool execution errors remain visible failures distinct from metric findings. There is no coverage baseline, score-exception registry or ratchet.

Only genuine Dagger admission and the existing lifecycle owners can issue immutable candidate-bound certifying evidence. A host pytest pass, copied report, green helper result or use of Dagger alone is insufficient. Reuse the existing shared engine and preserve process identity, disposable state, credential isolation, exact candidate and publication ownership. Full-suite execution and whole-master independent review belong to the master aggregation boundary under the current execution policy; this overview does not impose either on every leaf. Focused development evidence remains useful without pretending to be final acceptance.

## Five-Gate Certification Contract Foundation

`agents_remember.certification` now owns a repository-neutral immutable registry, plan-authority,
bounded-validation, and typed terminal-result foundation for five ordered closeout gates:
pre-test code quality, the large static suite, post-test quality that consumes suite artifacts,
clean-room integration/E2E, and memory quality. Gate meaning is fixed, while concrete Gate 1–4
rails, adapters, commands, applicability, and ownership remain repository-profile declarations;
Gate 5 retains memory-domain authority.

The foundation admits raw declarations before expensive allocation, returns all findings within
one measured budget, binds plans to an exact profile/registry/candidate, and requires complete
terminal results with typed evidence, artifact, owner, and blocker semantics. It contains no
Agents Remember rail inventory, no safe-full or compatibility fallback, and no executor. The
repository profile and Dagger executor are now integrated through the worktree quality gate,
including the pre-Gate-1 R11/R22/R21 admission bridge and green-generation certificate-record seam.
R05 typed finalization, R16 ordinary closeout telemetry, and R07/R08 final-memory execution still
lack production callers; existing journal recovery and interactive memory readiness do not prove
those new protocols are integrated. Detailed ownership begins at
[the certification route overview](src/agents_remember/certification/overview.md).

## Memory Preparation And Final Certification

Memory quality is useful before gate admission: a contract-scoped full request observes the exact code/memory pair and candidate trees, runs quality checks, and builds an enclosure-local curator worklist covering repair findings, commit-owned findings, missing onboarding, stale route indexes and source drift. Use that worklist to perform the authorized semantic onboarding updates before entering the expensive certification sequence. It is not necessary to obtain code-gate certificates merely to discover the memory work.

Preparation does not grant a final certificate. The interactive catalog projection explicitly lacks affected-closure and code-prefix authority. The existing prepared-memory adapter consumes the selected four original code terminals and exact prepared candidate, runs the final memory producer, publishes its physical result and selects Gate 5 through the normal owner. Finalization requires that selected original fifth certificate and its bound memory inputs. MCAR continues from these existing owners; this overview does not declare the unfinished master accepted or create a second final proof path.

Candidate capture uses an isolated add-all index and stable observed HEAD, leaving the user's real index unchanged. External-memory identity binds configured repositories, worktree roots, branches, bases, onboarding root and contract digest; the ledger path is informational and excluded from candidate authority. A changed pair or candidate must refuse stale publication. Metadata stamping and cache refresh cannot substitute for substantive memory repair.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The role-launch constructor now compiles one leaf-seat handover value: a leaf Worker, Reviewer or Curator receives `leafSeats` with the exact sibling `role_message` arguments for the other two seats and no sibling agent id. The package's role-launch, task-tool and capsule behavior is otherwise unchanged.

## Evidence

### Repo-Internal References

These current source and policy ranges establish the development/certification distinction and the existing memory preparation surfaces. A citation is source evidence, not a recorded test execution.

- Development commands, budgets, diagnostic metrics and isolation. [150]
- Certifying publication and accepting consumers. [151]
- Exact contract scope, full check and curator worklist publication. [152]
- Interactive catalog names missing authority without eligibility. [153]
- Final memory adapter requires the selected four-code-terminal prefix. [154]
- Finalization consumes original selected fifth-certificate inputs. [155]

Current working-candidate evidence for this route:

- A ledger view is derived from Git and cache write failure is only an availability result. [156]
- Existing preparation retains actual Git binding and allows a distinct memory content view. [157]
- Baseline adoption commits memory content and returns a cache observation. [158]

## Purpose

Terminal cleanup and abandonment exclude the computed root ledger cache from memory dirtiness and discard only that cache before ordinary Git worktree removal. Actual code/memory edits and branch ancestry remain protected. Abandon preview passes its preview state to result validation. The existing Git and public-terminal tests cover these boundaries.

260718-CHATS-L1 implements the active conversation serving the structured Chats architecture
assigned to the active child. Under `serving/conversation/active/`, the two authorized
production routes (native-hydrated page plus resumable SSE events) project the exact running
Codex/Claude/Pi conversations behind the L0 composition — HMAC-signed purpose-branded cursors
re-bound per wire, epoch verified against the live authority per request, a bounded
reconstructable-projector LRU per app — while `serving/conversation/projectors/` holds the pure
per-harness frame grammars (codex thread items/notifications, claude stream-json plus the exact
submission echo, pi durable entries/live tool upserts) with stable native identity and
unknown-vendor preservation. Hydration re-pages native authority only (never the flattened
transcript deque); the idempotent store unions tool-call blocks (review F1); established streams
fail as one typed gap + close (review F2/F3); the canonical `ConversationStatusService` is now
the single classification both Chats and orchestration consume
(`hosted_control_projection.snapshot_turn_state` delegates); capabilities stay fixture-gated
(claude `unverified` for a never-probed contract reason — since 260718-CHATS-L5F R4 THE CONTRACT
IS THE ONLY GATE and no version-string comparison demotes any capability, so the prior "installed
2.1.214 vs locked 2.1.211" version demotion is removed; codex historical tool loss visible). The
L0 composition, wire grammar, and library/control shells are untouched. The
`mcp/tests/` regression set gains four focused suites, and the foundation pin asserts the active
child's exact two routes.

260718-CHATS-L2 implements the dormant native conversation library inside the L9 contract roof.
Under `serving/conversation/library/`, five authorized routes expose each normalized harness's
native catalog/history (Codex direct app-server; Claude/Pi through the repository-locked Node
helpers gained operation entries `claude.ts`/`pi.ts` plus protocol serve/probe/sign/page
primitives) and open a selected native identity as a new idempotently tracked AR session only
after exact catalog proof. Live production-path gates decide capability honesty per
installed-executable fingerprint; a per-app HMAC-signed cursor/key authority binds scope,
purpose, and content-derived catalog generations; the bounded open ledger keys one stable
requestId/fingerprint, and record-spawned failures retire honestly while absorbed foreign
sessions are never disturbed. The L0 composition and wire grammar are untouched. The
`mcp/tests/` regression set gains six focused suites plus the opt-in
installed-runtime gates, and the foundation pin asserts the library child's exact five routes.

260718-CHATS-L0E lands the additive, read-only native evidence and resume substrate inside the
existing hosted harness-control family. Per-harness mappers stop dropping native frames by placing
full payloads under one reserved `arEvidence` event key; the control bridge diverts them at its
single consumption point into a bounded per-session evidence deque and publishes redacted events,
so every existing snapshot/catalog/SSE projection stays byte-identical. Three additive
epoch-scoped IPC reads — deque-domain evidence pages, native-domain history pages with typed
identity and opaque continuation (codex `thread/read`, pi `get_entries`; claude honestly
fail-closed), and the all-sources submission-provenance batch — cross only the user-private
control socket under the unchanged v1 protocol, with strictly validated client reads across two
disjoint coordinate domains. A codex-only `resume_thread_id` launch channel rides the opener →
runner payload → factory path into the sole `CodexAppServerSettings` site, refusing non-codex or
malformed values before any spawn. The substrate enables no feature; it is the closed baseline
later conversation leaves consume without editing shared harness-control seams.

260718-CHATS-L2E lands the additive native control-plane substrate inside the same hosted
harness-control family. A native interrupt write dispatches bridge-side through a structural
`InterruptCapableAdapter` sub-protocol — epoch-guarded and bridge-stamped, codex exact-active-turn
`turn/interrupt`, pi expected-operation-guarded RPC `abort`, replay-once per pair, claude
fail-closed typed, settlement untouched on the landed completion path. A paged never-bodies
operation-timeline enumeration reads the authority's retained ledger (all prompt sources plus
set-model/set-effort identity) under a count cap and the shared 48 KiB-class budget with
latestSequence/eviction-floor/truncated/epoch on every page, delegated authority → queue →
bridge → IPC → validated client. An asset channel rides submit as digest-verified references only
— resolve-and-verify confinement under the endpoint's own assets root, admission plus
construction-time sha256 verification, codex `localImage` and pi base64 native forms, unsupported
receipts on non-capable adapters — and the withdrawal-recovery payload crosses the exact
pre-tombstone body once inside the already `cockpit_only` response. Two additive IPC actions keep
`ar-harness-control/v1` (now 20 actions) with every pre-existing action, DTO, consumer, deque,
and snapshot reduction byte-preserved; redacted `control-plane/*` fixture rows record the
installed-runtime proof without enabling anything. The `mcp/tests/` regression set gains the
contract suite plus the opt-in installed-runtime capture.

260718-CHATS-L3 implements the authoritative control child over that L2E substrate, filling the
last behavior-empty conversation router. Under `serving/conversation/control/`, seventeen registered
routes deliver exact-turn interrupt (idempotent request/status/reconcile with acknowledgement never
equal to settlement), the complete source-aware never-bodies operation queue with cockpit-only
withdrawal and a bounded authorization-bound 900 s recovery lease, typed attachment stage/rebind/
submit through the L2E asset channel into a confined 0700/0600 spool, read-only effective policy
with no mutation surface, and evidence-bound telemetry (codex cumulative token usage). Opaque
control references are HMAC-signed, purpose-branded, and re-bound per wire; the per-app service holds
bounded per-(session, epoch) ledgers with per-session serialization above the L2E replay cache; the
pi settlement reads the L3E-preserved evidence terminal identity. The `mcp/tests/` regression set
gains four focused service/route suites, a shared control topology, and an opt-in installed-runtime
proof; the slice is governed by `conversation/control/overview.md`.

260715-FEUI-L9 established the stable protocol-neutral contract roof under `serving/conversation/`:
strict wire models and exactly two read ports now sit above the active transcript, conversation
library, and control child routes. Under `native_helpers/conversation_library/`, a locked private
Node helper normalizes repository-resolved harness observations into redacted evidence; it is not a
second server, store, or capability authority. The existing harness-control application factory
registers the conversation root once. The current child routes own their behavior beneath that roof;
the package does not thereby grant unrelated projector or renderer authority.

260718-CHATS-L0 repairs the production composition boundary under that contract roof. The same
single harness-control registration now constructs and installs one immutable app-scoped
`ConversationRuntime` — workspace/coordination scope, terminal catalog/host, effective harness
registry, liveness clock/config, and capability evidence — plus a server-resolved local-operator
authorization resolver on the app exactly once, with `create_app` passing `coordination_root` for
the scope. Child leaves consume the runtime only through two narrow request dependencies
(`get_conversation_runtime`, `resolve_conversation_authorization`) and never edit the shared
registration again; the local-operator ruling is loopback-only with no browser principal/tenant
channel. The shared error family gains `ConversationCompositionError` for missing, duplicate,
foreign, or missing-member composition failures. The route remains behavior-free: no projector,
native-history service, control implementation, or renderer.

### Historical Package, HFX And Early Hosted-Adapter Account

These dated additions retain their original public names and intermediate authority models. Current structural dispatch, protocol-backed delivery, application-owned response finalization and the completed conversation children above govern present behavior.

`mcp/` is the package-managed Agents Remember MCP server. It turns coordinator
startup and provider lifecycle behavior into typed, host-side operations backed
by importable Python services instead of model-edited coordinator scripts or
coordinator `system/settings.json`. The tool surface gained `task_reopen` cit:([`task_reopen`], mcp/src/agents_remember/mcp/registration/tasks.py:64-76):
reopen a fully landed leaf task under its exact leaf id — a task-domain state reset
whose worktree recreation stays with `worktree_start`. The agent-orchestration L2
adds `spawn_agent_session` — the agent-facing **dispatch** tool that CREATES a
role-configured, leaf-attached, context-primed hosted session by composing the
existing serving primitives (the shared session opener + optional leaf attach with
server-arbitrated `leaf-taken` + a capture-VERIFIED context paste (260707-HFX-L3) with optional
submit), resolves model/effort/free-form spend controls from settings only, rejects caller spend
overrides before spawning, and records spawned-by provenance — so orchestrators spawn managers and
managers spawn workers without dashboard clicks. HFX-L6 splits the developer-facing architect from spawned backend
orchestrators and adds the curator role to the runtime skill/package mirrors, settings role vocabulary,
dashboard role projection, and manager/worker dispatch chain. The package-data runtime skill mirror now carries the L5
super-integration doctrine for orchestrated series: super branches from main,
masters branch from super, leaves branch from masters, C-11 carries every edge,
the orchestrator integrates completed masters from a super-sourced worktree, and
the final super-to-main PR is followed by main-memory carry-over and push. L6
sharpens the same runtime skill mirror's adversarial review procedures: managers
spawn master-exit reviewers, orchestrators spawn super-exit reviewers, verdicts
land in series `notes/reports/`, and the handover gate carries
`reviewer-verdict` evidence refs that L4 policy may require. Since L12 every managed
provider container carries an explicit compose memory cap (watchers 512m,
falkordb/ollama 2g, runner 1g, postgres 512m) with self-recycling OOM behavior.
260707-HFX-L1 adds the containment layer above those per-container caps: the
on-disk authority settings — never a running server's boot snapshot — are the
provider LAUNCH authority (launch-capable operations re-read them fail-closed;
stop/status/cleanup are never gated, so `providers: {}` on disk is a live
fleet-wide kill-switch), provider setup is serialized host-wide by a
HOST-scoped setup-lock flock in the system temp dir (one non-dry-run prepare
at a time bounds the aggregate container load — the 2026-07-07 OOM was
concurrent setups summing past the host; the lock lives outside every
coordination root because those trees are prunable/per-workspace), and the
serving daemon centrally samples labeled provider containers
into a metrics store that provider status attaches. 260707-HFX-L2 extends the
same posture to the INDEX lifecycle: a HEAD difference between a seed source
and a worktree checkout is a state to catch up from, not a teardown — small
diffs become index UPDATES via watcher-event catch-up (the seed clones the
near-perfect graph and fresh mtimes/touches drive the event-driven watchers
over exactly the delta), the implicit refresh-all fallback is off by default,
and from-zero rebuilds are explicit only (`cgc refresh` or the opt-in
fallback flag); index-lifecycle rows ride the same central metrics log.
260707-HFX-L7 builds the RESPONSE protocol on top of that same central metrics log: NEW
`providers/degradation.py` is a provider-only detector/state-machine
(healthy/degraded/critical, hysteresis-gated so alerts do not flap) that `serving/app.py`'s
sampling loop calls once per tick; on a state-change transition it writes a durable event/state
pair under `logs/observer/providers/degradation-*` (survives daemon restart), posts
role-addressed `degradation-alert` inbox rows to the orchestrator and every active manager
(instructing managers to stop starting providers with no kill authority, and the orchestrator to
dispatch the new `system-specialist` role before ordering a fix or stopping providers), and — at
`critical` with the failsafe armed — stops provider stacks through the always-legal teardown path,
capturing (never losing) a raising stopper's failure inside the durable event. NEW
`mcp/provider_degradation_settings.py` is the dedicated `providerDegradation` settings parser
(15-key fail-loud allowlist, conservative enabled/armed defaults) `mcp/config.py` wraps into
`ConfigError`. This iteration is providers-only by developer ruling; Sentry
(260703_spotlight-dev-observability) is the designated future detection source that can
replace/feed the same response protocol without redoing it.
260707-HFX-L8 adds seat lifecycle management to the terminal catalog tool surface: NEW
`session_retire` (+ `POST /api/terminal/{session}/retire`) terminates a tracked chat session and
marks the catalog row retired with provenance, authority-checked server-side (owner-never-self-
retires; a manager may retire only its own master's worker/reviewer seats; the orchestrator may
retire any seat) via NEW `serving/retire_policy.py` + `serving/retire.py`. **Superseded by
260707-HFX2-L11**: the `worktree_integrate`/`lifecycle_finalize_task` completion edges no longer
call `retire`/terminate a successful seat automatically; they call NEW `serving/landing.py::
land_seats_for_leaf` instead, which marks the row `status:"landed"` (kept alive, non-terminated,
fully inspectable) — successful completion is not chat cleanup (ruled design constraint 10);
explicit `session_retire` or the dashboard's landed-archive group-cleanup control are what actually
reclaim chat volume. Settings are `autoLandOn{Integration,Finalize}` (still config-gated, both
default ON, still best-effort so a catalog fault can never fail the edge it rides; legacy
`autoRetireOn*` keys are honored as aliases). `serving/retire.py`'s manual/authority-checked retire
behavior described above is otherwise unchanged. NEW `session_rename` (+
`POST /api/terminal/{session}/rename`) updates a chat's display label post-spawn without touching
its role. NEW `serving/turn_state.py` classifies live seat turn-state (working/turn-ended/
awaiting-input/stale) from pane text on the existing L5 liveness-sweep cadence; NEW
`serving/seat_events.py` emits observer events on retire/rename/turn-state transitions.
260707-HFX-L12 closes a master-exit-review-caught gap: `controlplane/operator_inbox_records.py`'s
`AgentRole` gains `"architect"` and `"curator"`; `InboxMessageKind` gains `"decision-item"` and
`"decision-ruling"`. The HFX-L6-ratified minimal decision-item relay (orchestrator posts a
decision-item to the architect; architect posts a decision-ruling back) was landed as doctrine but
the schema previously rejected both calls with `ValidationError` — the architect seat could not
receive any typed inbox row. No other consumer of these Literals enumerates them exhaustively, so
this is a pure schema extension with no downstream edits; a new round-trip test in
`mcp/tests/test_operator_inbox.py` pins the fix through the real tool-payload seam.
260707-HFX2-L1 adds a durable what-must-happen-by-when layer that spans three tool families at
once, not just one route: NEW `controlplane/expectation_rows.py` is the `ExpectationRowStore`
primitive (`briefed-by`/`turn-report-by`/`verdict-by`/`ack-by` rows, `pending`/`overdue`/
`find_by_source` queries, idempotent `mark_met`/`mark_missed`); `mcp/tools/terminal.py`'s
`spawn_agent_session_payload`, `mcp/tools/gates.py`'s `gate_create_payload`/`gate_decide_payload`,
and `mcp/tools/operator_inbox.py`'s `operator_inbox_post_payload`/`operator_inbox_consume_payload`
each now write (or meet) their expectation row in the SAME call as the dispatch/decision/ack
itself (R2) — a deadline is a durable row an L2 sweep can scan, never an in-memory timer a
daemon/MCP restart would erase. R1 sharpens the operator-inbox ack contract to match: `consume` is
the ONLY terminal outcome on `OperatorInboxEntry` (new `attemptCount`/`lastAttemptAt`/
`nextAttemptAt`/`escalatedAt` fields) — a confirmed `delivered` paste still schedules a further
redelivery attempt, since pasted is not perceived. NEW `controlplane/inbox_backoff.py` (R3) is the
redelivery backoff-ladder math and per-target rate limiting a future sweep will drive; NEW
`controlplane/signal_routing.py` (R4) derives a one-hop routed owner (worker→its manager,
manager→its orchestrator, `decision-item`→architect) from `serving/terminal_catalog.py` spawn
provenance, and `OperatorInboxEntry` gains `ownerRole`/`ownerAgentId`/`ownerLifecycleId` fields
stamped once at post time from that derivation. `kernel/agentic_settings.py` gains the
`orchestration.expectations` settings family (`ExpectationSettings`,
`DEFAULT_EXPECTATION_SLA_SECONDS`) — an SLA-per-kind duplicated by hand against
`ExpectationKind` to avoid a kernel↔controlplane import cycle. The redelivery sweep, escalation
ladder, and dashboard consumption of `escalatedAt` are explicitly OUT of scope for this leaf (a
sibling leaf's job); this leaf only lands the durable rows, the backoff math, and the routing
derivation the sweep will consume.
260707-HFX2-L2 adds the `orchestration.supervisor` settings family to the same package-level
loader — `SupervisorSettings` (enabled/interval/staleness-cutoff/redeliver-rate-limit) parsed by
`kernel/agentic_settings.py` — consumed across TWO other package routes: `serving/app.py`'s new
supervisor-sweep lifespan task (the sweep subsystem itself — the predicate library, action
dispatcher, and self-liveness heartbeat — is documented in full in `serving/overview.md`, which
this file governs) and `mcp/tools/base.py`'s per-tool-call staleness banner attachment
(`supervisorBanner`, exception-contained at the call site). Same cross-route-consumption shape as
the 260707-HFX2-L1 expectation-row family documented above.
260707-HFX2-L4 adds the `orchestration.escalation` family to the same loader (`EscalationSettings`
— per-`message_kind` ack SLA, per-rung dwell timings, the renudge rate limit, the
respawn-after-rung threshold), consumed by the SAME `serving/app.py::_agent_notifier_context()` call
site the supervisor family already wires through — no new lifespan task, no new settings-read
seam. The family backs the P-15 tier-3 escalation ladder (`controlplane/escalation_ladder.py`,
`controlplane/orphan_policy.py`, and a new two-hop `signal_routing.derive_skip_level_owner`/
`is_seat_dead` pair kept SEPARATE from the existing one-hop `derive_signal_owner`), fully documented
in the `controlplane/` and `serving/` route overviews this file governs.
260707-HFX2-L5 closes the loop on the same P-15 mandate from the doctrine side: the role files this
package data ships (`package_data/runtime/skills/l-01-agent-lifecycles/{SKILL.md, roles/manager.md,
roles/orchestrator.md, roles/worker.md, templates/turn-report.md}`) invert from active owner-side
vigilance ("Monitor the worker" / "monitor turn-report artifacts") to a passive process-and-ack
contract: the HFX2-L2 sweep + HFX2-L4 ladder do the watching, and a role's own duty is to be woken
with its pending signals, process and ack every one, then end its turn — silence is supervised, so
`lifecycle_turn_end_notification` is never a liveness gap. An explicit watcher ban (uniform-mechanism
ruling 2026-07-07) forbids any seat-local watcher/poll/monitor of any kind, one mechanism for
everyone. Doctrine-only change set, propagated by `scripts/sync-skills.py` to all 9 downstream
package copies plus the canonical `skills/` source — zero Python touched. The SAME leaf adds NEW
`mcp/tests/test_liveness_simulations.py` (11 tests, 8 named P-15 fixture-zoo incident classes),
driving `run_agent_notifier_sweep` across multiple simulated ticks per incident: 6/8 pass fully
end-to-end; 2/8 (chip-stacked delivery stall, and the pane-classified half of never-briefed) are
proven hybrid (predicate-unit classify + real downstream sweep response) because `evaluate_predicates`
hardcodes a real, non-injectable `tmux capture-pane` call — documented as a real product gap and the
natural next leaf (make the pane capturer injectable through `AgentNotifierContext`), not silently
worked around. Results are filed in `notes/reports/260707-HFX2-L5-liveness-report.md`.

The packaged lifecycle/task-workflow projections now also carry M40@v2/M44@v2: semantic revisions
require explicit developer approval; formal worker attempts advance only at review handoff or after
reviewer rejection; internal implementation/test/evidence runs remain separate protocol events.
Lightweight requirement-specific journal records link content-addressed frozen expanded evidence,
and rebuildable summaries exclude protocol events and never become lifecycle, task, closeout,
integration, or queue authority. `scripts/sync-skills.py --check` remains the projection identity
proof.

260707-HFX2-L8 closes the two liveness gaps a live dead-seat-storm incident (2026-07-08) exposed in
the supervisor loop itself, spanning four package routes. `kernel/agentic_settings.py` gains one
`orchestration.supervisor` field — `redeliverBudget` (default 250, defaults-safe) — the per-sweep
redelivery floor so a large redeliverable set degrades gracefully instead of one sweep grinding the
whole backlog. `controlplane/operator_inbox_records.py` gains a durable `ladder-resolved` terminal
inbox state (distinct from ack): a pending row at the terminal escalation rung whose target seat is
provably dead (retired / no hosted session) terminates instead of redelivering forever — excluded
from `redeliverable()`/`is_due()` via a state-keyed predicate in `controlplane/inbox_backoff.py`
(mid-climb / live-seat rows untouched, L1-R1 preserved) and dropped by
`controlplane/interaction_retention.py` compaction. HFX3 supersedes the old immortal-pending
contract: pending rows expire after 48 hours, the folded inbox is capped at 500 current ids, and
durable truth lives in artifacts rather than notification rows.
`serving/supervisor.py` threads ONE in-sweep operator-inbox snapshot/index through every
finding/mutator (`record_delivery`, `mark_escalated`, `advance_rung`, `mark_ladder_resolved`,
respawn reads), killing the per-finding full-log re-fold (O(n^2)) so a sweep's cost is bounded by
finding count and the self-liveness heartbeat ticks unconditionally under backlog;
`serving/supervisor_heartbeat.py` surfaces `pendingInboxCount`/`redeliverableInboxCount`/
`lastSweepDurationSeconds` onto `/api/state` and the dashboard header as a forward backlog signal.
`worktrees/leaf_refs.py` gains a minimal boot-safety skip of non-task JSON siblings (schema-marked
malformed task docs still fail loud). The cross-route change is documented in the `controlplane/`,
`serving/`, and `dashboard/src/` overviews this file governs; a non-destructive recovery runbook
lands in `docs/design/observable-lifecycle.md` and the settings table in
`docs/reference/settings-json.md`. New scale regression: a 2000-row dead-seat-storm sim in
`mcp/tests/test_liveness_simulations.py`. Results filed in
`notes/reports/260707-HFX2-L8-worker-report.md` and `-reviewer-report.md`.
260707-HFX2-L7 is the hotfix release tail for `3.0.0rc4`: package/version strings move from rc3 to
rc4, the packaged lifecycle doctrine refines Developer Clarification Triage to read the active
queue before choosing note-only handling, and the serving supervisor defers generic unacked
escalation for hosted-delivery failures until the persistent redelivery threshold has exhausted.

The serving package also contains the protocol-neutral harness control seam: normalized state,
one-adapter hosted bridges, bounded ordered input, private exact-identity IPC, and a surface-owned
draft/transcript layer. L1 defines this contract and reports unsupported adapters explicitly; no
vendor driver is registered or production cutover is implied.
260713-PHA-L3 extends that seam with a stable-only Codex app-server adapter. The pinned 0.144.3
 JSON-RPC transport and session own initialize, model/effort discovery, and exact thread
 start/resume; the adapter/state pair own correlated turns, structured approvals and elicitation,
 explicit steer-or-queue busy behavior, bounded evidence, and reconnect reconciliation without
 blind resend. This is a leaf-local protocol path: production registration and cutover remain L5
 scope.

260715-FEUI-L5 is the current production authority over that historical seam. One
`HarnessSubmissionAuthority` per bridge generation orders prompt/model/effort work, linearizes
withdrawal against guarded native dispatch, completes only exact full operation refs, and exposes
bounded raw-free lifecycle status. `HarnessControlQueue` was a facade, not a second actor, and
260731-EFA-L6 deleted it outright. The shared
typed error family now distinguishes certified pre-dispatch busy, immutable-id conflict, and epoch
mismatch so only the exact certificate is retry-safe.

The hosted harness-control and conversation layers are multiplexed for harness sub-agents. The
codex app-server connection auto-attaches every spawned sub-agent thread to the seat's connection,
and the adapter demultiplexes per thread: a bounded thread registry tracks per-thread turns,
operations, and pending interactions; collab items (`collabAgentToolCall`, `subAgentActivity`) bind
agent identity into a snapshot-carried registry; malformed non-parent traffic degrades to preserved
raw evidence while parent shape errors still fail loud; server→client requests (approvals) are
accepted from any thread and answered by JSON-RPC request id. The wire grammar gains an additive
agent dimension (`ConversationAgentRef` on items, `EvidenceFrame.thread_id`,
`AdapterSnapshot.pending_interactions`), the active projector serves one multiplexed projection per
seat (one page, one SSE, one cursor domain) with per-thread native/live dedupe, the library groups
sub-agent conversations under their parent on both harnesses (codex `subAgent` source kinds, claude
`subagents/*.jsonl` enumeration), and claude launches gate `--forward-subagent-text` on a
version-floor probe with fail-closed fallback. That probe stops and re-launches the SAME subprocess
transport, so the transport is a restartable resource: a completed stop releases process ownership
while a start against a live process still refuses.

The multiplexed surface is load-shedding and concurrency-safe under real vendor traffic.
Server→client requests pend per thread in bounded maps keyed by rpc id (concurrent approvals
across any threads are normal traffic, answered by request id; the vendor's own clients track
them the same way); an unknown or experimental request method is answered with decline
semantics and preserved as degraded evidence on any thread, while a malformed shape on a known
stable method still fails loud on the parent only. Concurrent pendings — parent included — all
project into the interaction lane with singular-rotation settlement (the oldest holds the
singular slot; answering rotates the next in without falsely resolving it), and the authority's
parent guard is decided by the entry's own thread. The adapter's bounded event queue never
fails the bridge under a delta flood: the oldest high-volume delta events shed first with every
shed counted, and one load-shed notice crosses with the count when the consumer catches up
(including on consumer-side drain and before the close sentinel).

## Hot Path Summary

The imported native Paseo role route retains canonical task/workspace identity, exact launch/replay and independent model/effort/tier validation alongside the existing converted MIK memory and publication owners.

The kernel separates Git attribution, ledger formatting and cache materialization. Memory-domain snapshots retain actual Git head/tree facts while comparing content without root `memory.md`; the exclusion does not apply to the code repository. Baseline adoption and carryover produce real attributed content only when needed and report cache refresh separately.

## 260915-CAPS-L10 Measured Result — The Capsule Did Not Reduce Startup Context (adoption FAILED)

**This section is the measured truth about the capsule chain the rest of this package builds, and it is
negative.** Every other section on this route describes **structure, correctness and design intent**;
none of them is evidence of a context reduction, and this section says so explicitly so a reader cannot
infer one.

- **The delivered capsule is larger than the legacy chain at the one elevation measurable.** `CAPS-R10@v1`
  behaviour 6 requires a demonstrated reduction in AR-added startup material for matched worker, manager
  and architect cases. At the **worker** elevation the measured run's **delivered** `orientation` capsule
  is **11,828 tokens against a 5,928 baseline — +5,900**; the like-for-like `implementation` capsule is
  **11,645** (**+5,717**). The delivered figure governs.
- **Manager (`coordination`) and architect (`planning`) are UNMEASURED** — `refused`,
  `binding-unresolved`, because the frozen world carries no series contract at the master or sprint
  altitude. They are unmeasured elevations **inside** the adoption failure, not passes.
- **Obligation preservation is intact: 36/36** across **ten** declared roles plus launcher routing, with
  the E1 falsification observed. The failure is on the reduction half alone.
- **The two sides are different kinds of object.** The capsule side is a role- and operation-selected
  payload; the baseline side is an **unscoped** chain identical for every role and operation. No "saving"
  across them is claimed anywhere on this route.
- **Adoption acceptance FAILED; the disposition is REVISE** — a recommendation to the owner, not a
  decision. A complete report recommends revise/discard and stays a failed adoption acceptance; it never
  closes an unresolved functional requirement and never weakens mandatory native-eve functionality. **No
  IAS landing is authorized** by this leaf or by any green result, and the 4k-in-a-32k-window figure
  remains a stretch direction, never a truncation rule and never an achieved result.

**What the same evidence positively supports — this package's delivery claim, which did hold.** A started
session really does receive its compiled capsule, and the evidence class is the started session's own
state:

- **Native eve:** the started session's **own system block** carries the capsule **exactly once** — on the
  second call, after **compaction**, after **clear** and after **resume**. A **forged** delivery never
  reached the system block. An **edited carrier** was **refused** (`carrier-digest-mismatch`) and made
  **no model call**; the seat wrote only its admitted workspace, and an unbound launch was refused with no
  model call. Scenario summary **8 / 8**. The runtime process was staged from the builder's own worktree
  and asserted **byte-equal** to the authored tree (`agent.ts` sha256 `287dbbf0…`), with `AR_EVE_EFFORT`
  present.
- **Codex:** the capsule arm completed a real representative code leaf end to end — the repair landed in
  the **admitted** worktree and the fixture check went `1 failed, 2 passed` → **`3 passed`, exit 0**.
- **Boundary:** the eve arm's model is the fixture's deterministic local provider; what is native is the
  runtime process, the HTTP transport, the durable event stream and the adapter. `--real-model` was **NOT
  run** (no hosted credential) and is **UNRUN**, not a pass. The matched **Codex baseline completion is
  UNRUN-AS-MATCHED** — the legacy chain fails closed without the plane-injected `AR_HOSTED_SESSION_ID`,
  and a matched baseline therefore needs a **production-control-plane** launch, an owning-seat action.

**Unobservable stays unobservable.** Peak context occupancy is unobservable on **both** harnesses —
Codex's stream carries cumulative usage only, and `serving/eve_events.py::EveEventMapper._HANDLERS` maps
no usage frame. Cumulative usage is unobservable on eve. Occupancy and cumulative usage were reported in
separate columns and **never summed**; the baseline arm's compilation cost is `not-applicable`, an honest
absence rather than a zero in a total.

**What this result does NOT say.** It is not a claim that the capsule is worse for a real session: the
legacy figure counts the always-injected routing layer only, while the skill corpus it routes to is read
on demand and deliberately excluded from the measure — a fair total-instruction-read comparison is a
session-level measurement that does not exist yet. It is also **not** attributed to the compiler, because
the two arms differ in installation mechanism as well as in content.

**Design intent, labelled as intent rather than as a measured saving.** The L1 corpus restructure
(`SKILL.md` 620 → 179 lines) is a **single-source restructuring**; the L2 compiler's determinism,
refusal-as-value and one-block-per-identity properties are **correctness** properties; and the L9
installation cutover is an **installation** change whose measured effect on startup material was, at the
one elevation measured, the **opposite** of a reduction.

**Frozen artifacts.** Method `notes/reports/caps-l10-measurement-method.md` (digest
`sha256:902676a630075f34b21c70e412eecee51bf8acc42488f3d1fc35a5b4b81ce528`); frozen evidence
`notes/reports/260915-CAPS-L10-evidence/` (991 entries, index digest `sha256:c6581df2…`); builder report,
disposition and both verdicts under `notes/reports/260915-CAPS-L10-*` and `notes/reports/caps-l10-*`.
Both review rounds closed with no open findings; clearing six findings did **not** convert the negative
result into a pass.

## 260915-CAPS-L18 Complete Curation Reaches This Route

CAPS-R18@v1 inverted the optional/narrow-curation doctrine in the shipped instruction sources. The
sentences that presented the full `memory_quality_check` operation and the `curator_coherence`
certification as developer-request-only diagnostics, "never routine closeout/integration prerequisites",
are gone. The rule is now normative: **curation is complete on every leaf** — the full operation runs at
the leaf's contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every
curator-actionable finding is repaired or escalated as blocked with its exact returned code, and the
operation is re-run after every repair until `curatorActionableCount=0` and the **raw**
`qualityChecklistStatus=ready-for-closeout`.

**The two status fields are different fields, and a reader who merges them loops forever** (`D35`, a
landed-defect repair recorded by 260915-CAPS-L10). Read the **raw** `qualityChecklistStatus` to decide
whether the repair loop can end. Once it reaches `ready-for-closeout`, the **combined** `checklistStatus`
is rewritten to `coherence-required` **only when the coherence record is then missing or stale**; on the
success path, where the record is already current, the combined field is not rewritten at all and keeps
its incoming `ready-for-closeout` value, with `closeoutReady=true`. `ready-for-closeout` therefore *is*
observable in the combined field, but only once the whole pipeline — repairs and validation — is already
complete. `application/memory_quality/controller.py` is the authority: `:664` publishes the raw field,
`:671` gates on it, `:678` publishes the combined `coherence-required`, `:685-687` leave the combined
field untouched when the record is current and set `closeoutReady` after validation.

**Warrant corrected by `CAPS-R19` (leaf `260915-CAPS-L19`).** This card's `D35` correction originally
rested on the sentence *"`ready-for-closeout` is never a value of the combined field."* That absolute
claim is **literally false**, and `CAPS-R19`'s revision note records it as superseded by the three-path
model above. The field-name correction the sentence supported is still right; only its stated warrant was
wrong. **Attribution is complementary and both halves hold:** `260915-CAPS-L10`'s curator corrected the
**onboarding cards** that carried the wrong form, and `CAPS-R19` (`260915-CAPS-L19`) corrected the
**shipped sources** — the five loop-gate carriers, their nine generated copies, the guard registry's own
docstring — and brought `docs/reference/mcp-tools.md` into both the loop-gate census and the guard's
`LOOP_GATE_DOCUMENTS`.
The sentence this section previously carried named the combined field as the loop's termination
condition; that was wrong in the shipped sources and in the cards that quoted them, and it is corrected
here and on the other affected cards.

Two corrections the inversion must not collapse, both preserved: closeout still owns only the Git
transaction and **invokes** nothing — it **carries** the completed curation as a prerequisite; and the
rule is about the completeness of curation, not about unscoped runs, so "complete" always means the whole
operation at the leaf's contract scope. The ruling is forward-looking: the already-landed and finalized
leaves are not re-curated, and whole-layer completeness is discharged by L11's full-scope run at the
frozen tip.

## 260915-CAPS-L15 Launch-Path Capsule Delivery Route Impact

**Route meaning changed for the launch path this package serves, so this card carries a real route
impact rather than a bare `No route impact` marker.** The master built and individually proved every link
of the capsule chain — the compiler (L2), the admission/MCP surface (L4), the Codex instruction seam
(L5), the eve carrier (L7) — and **no production launch point supplied a capsule to any session**. Two
of the three production launch points are now wired, and the third is a declared exclusion with its
reason:

| Launch point | State | What supplies the instructions |
| --- | --- | --- |
| `application/terminal_tools.py::_spawn_launch_request` (the primitive `dispatch_agent` drives) | **wired** | the capsule compiled at the launch from the role and the admitted binding, on the launch request; `instructionMode` published per run; `capsule-unavailable` refuses by name before any host side effect |
| `serving/_app_terminal_routes.py::_open_terminal_response` (the dashboard opener — the only production point that starts a **free agent**) | **wired** | the same gate through the injected application-rank port; HTTP 400 `capsule-unavailable`; `instructionMode` on the response |
| `serving/conversation/library/open_service.py` (the library reopen) | **declared-excluded** | `LIBRARY_REOPEN_LEGACY_REASON` — the route proves the vendor identity it resumed, and a capsule would resolve as a fresh thread |

**The launch runs where its capsule admits.** The admitted workspace is read back out of the carrier the
runtime re-verifies, so the session cwd, the settings selection the runner itself requires to equal the
cwd, and the child's `AR_WORKSPACE_ROOT` are **one value** — no launch may be described as running at the
server's workspace root unconditionally any more.

**Two limitations carried, not smoothed.** A role-configured **eve** seat still cannot be dispatched:
the capsule gate passes and the next refusal is the inherited settings-chain effort gate (`D22`, owner
**L17**). And the dashboard route cannot start the *shipped* eve row (it does not set
`session_backend`), which is pre-existing and also **L17**'s.

**The D13 repair is on this package's registered surface.** `role_capsule_compile` now resolves a
repository through the schema it actually registers, and a case fails if that schema loses the field the
resolution depends on. The evidence for both halves is
`notes/reports/260915-CAPS-L15-evidence/E8-fix-r1-production-chain.txt` and
`mcp/tests/test_capsule_launch_wiring.py`.

- The one decision point every launch point calls, with its three answers and named refusals. [159]
- The one workspace rule and the selection that follows it. [160]
- The compiler the port is bound to, including the eve path that reads the admitted workspace back out of the carrier. [161]
- D13's repair, on the registered operation's own resolution path. [162]
- The declared legacy exclusion, and the enumeration case that keeps a fourth launch point from appearing silently. [163]
- The production chain read at the consumer's own gate and at the live runtime's system block. [164]

## 260915-CAPS-L6 Native eve Session Adapter Route Impact

The `mcp` route gains a native **eve** protocol adapter (`CAPS-R06@v1`). The structural change a
future reader must know about:

- `serving/` gains seven modules: `eve_adapter.py` (the adapter), `eve_protocol.py` (the wire contract,
  route builders, the one `TURN_POLICY_QUEUE` literal, and the single `EveEventDeduplicator`),
  `eve_events.py` (event translation and normalized state), `eve_interactions.py` (the bounded pending
  interaction queue), `eve_runtime_client.py` (the HTTP transport and its request-body builders),
  `eve_runtime_launch.py` (application-root resolution, staging and launch environment), and
  `eve_stream_cursor.py` (the absolute-index NDJSON decoder).
- `serving/harness_control_factories.py` is the one seam that changes an existing registry:
  `BUILTIN_PROTOCOL_HARNESSES` is now `claude`, `codex`, `pi`, **`eve`**, and `_LAUNCH_KNOBS` maps eve
  to its environment-only launch vocabulary.
- `kernel/harnesses.py` is **unchanged in behaviour** — its curated `HARNESSES` tuple still holds three
  rows and its docstring now records why. The two registries answer different questions:
  terminal-launchable `PATH` harnesses versus constructible hosted protocol adapters. An `eve` harness
  id resolves through the protocol factory only, and terminal-harness exposure remains the
  capability-catalog/packaging leaf's decision.
- The runtime application itself is a **repository-root** tree (`eve_runtime/`) rather than a package
  under `mcp/`; see the root overview's route-impact note for its onboarding boundary.
- `mcp/tests/` gains the five-module eve test population (two collected suites, three support or
  explicit-run scripts); the route-level account is on `mcp/tests/overview.md`.

Route consequence: the adapter boundary, the capability port and the interrupt port are all AR's
existing seams. This leaf adds an implementation of them, not a new plane — so no new service,
registry or orchestration layer appears in this route.

## 260915-CAPS-L1 Packaged Lifecycle Corpus Restructured

**Read this section as STRUCTURE, not as a saving.** The consolidation was a design intent — one
single-source, role-addressed corpus — and it is **not** a measured context reduction: the doctrine
moved into the new `core/` · `operations/` · `reference/` siblings rather than disappearing, and the one
measurement that exists (§ 260915-CAPS-L10 Measured Result above) reports the assembled capsule
**larger** than the legacy startup chain at the worker elevation (**11,828** vs **5,928** tokens, +5,900),
with adoption acceptance **FAILED**.

The packaged runtime skill tree under `mcp/src/agents_remember/package_data/runtime/skills/` gained 14
files and had 17 rewritten in 260915-CAPS-L1 (`CAPS-R01@v1`), because the canonical
`skills/l-01-agent-lifecycles/` corpus was consolidated and `scripts/sync-skills.py` propagated it. For
this route the load-bearing facts are:

- **The packaged copy is generated, never authored.** `SKILL.md` is now a 179-line router (was 620) and
  carries no doctrine; the rules it used to hold live in the new `core/` (six blocks), `operations/`
  (eight blocks), and `reference/` (two files) siblings, with `composition-manifest.json` holding the
  prose-free routing metadata a future deterministic compiler selects from. Editing any packaged file
  directly is drift — the canonical tree is `skills/`, and `scripts/sync-skills.py --check` proves the
  copy byte-identical.
- **The nine packaged role files were rewritten into one readable order** and now declare their shared
  sources with `**Inherits:**` rather than restating them. A packaged role file names a sibling role file
  only to wear that hat or dispatch that seat.
- **That readable order is itself superseded — the packaged role files now carry the function shape.**
  leaf `260915-CAPS-L22` (under the developer's 2026-09-17 ruling) rewrote all **ten** packaged role files
  (`package_data/runtime/skills/l-01-agent-lifecycles/roles/{architect,orchestrator,strategist,designer,manager,worker,reviewer,curator,system-specialist,bootstrap}.md`)
  into `# <Role>` + `## Inputs` + `## Process` + `## Outputs` + `## What you may do` +
  `## What you must not do` + a closing `## Stop and …` section. The numbered L1 sections, the
  `## Knobs, Tool Surface, And Dispatch Authority` block and the `**Inherits:**` line are gone from every
  one of them, so a card on this route that still cites one of those headings is stale; the canonical
  `skills/l-01-agent-lifecycles/roles/` sources were rewritten first and this copy was propagated by
  `scripts/sync-skills.py`, so the packaged and canonical copies remain byte-identical.
- **This route's cards are the corpus's governed onboarding.** The canonical `skills/**` tree is outside
  this memory root's `pathRules` include set, so this generated `mcp/**` copy is the mapped surface: it
  gained 18 new cards (the manifest, `core/` ×6, `operations/` ×8, `reference/` ×2) and 17 existing cards
  were updated in the body.

## 260915-CAPS-L2 Deterministic Role-Capsule Compiler And Its Cross-Leaf Manifest Change

`mcp/src/agents_remember/models/role_capsules/` and
`mcp/src/agents_remember/application/role_capsules/` are **new packages** on this route: one pure,
harness-independent compiler that turns admitted AR facts plus canonical instruction sources into
an ordered role capsule, and one application-tier boundary that does the file I/O the compiler
refuses to do. The split is the route's load-bearing structure — `models` holds the frozen value
types, the manifest parser, selection, resolution and the seal; `application` holds admitted-context
resolution and source reading. Nothing in the `models` half opens a file, reaches a network, or
calls a model, and two shipped cases assert that composition succeeds with model and network access
denied and that no network client is imported at all.

The compiler is deterministic by construction: fixed composition order (core → role → operation →
specialization) that is itself part of the semantic digest, one block per canonical instruction
identity, sorted tool ids, no timestamps and no diagnostics inside the digest, and no concurrency
(eve's concurrent resolver was deliberately **not** adopted, because resolution timing would make
the composed order nondeterministic). Identical admitted facts and source bytes produce identical
ordered content and the same digest; the nine shipped roles compile from disk twice to one digest
each, and they compile to nine **different** digests.

Two properties are worth carrying forward. First, **a refusal is a value, not an exception that
escapes**: `CapsuleCompilationOutcome` is exactly one of a capsule or a refusal, a refusal still
carries the admitted-facts half of the diagnostic manifest so a failure explains itself, and
`mcp/src/agents_remember/errors.py` gained the `CapsuleCompilationError` family to type it (two
subclasses today — `CapsuleManifestError` and `CapsuleSourceError`; a third, `CapsuleBindingError`,
was removed by this leaf's review repairs). Second, **a required block's absence is falsifiable**:
the admitted file set is validated against the locked plan in both directions, because a loader that
only fetched what the manifest asked for could never report that something mandatory was never
admitted.

**A third property matters because it is the easiest to get wrong: the two capability channels are
not the same shape.** Requested **tool ids** are narrowed against the admitted `CapsuleToolPolicy`
snapshot, and a request outside it is refused. Declared **skill references** are **carried**, not
narrowed: `compiler.skill_references` builds one content-addressed reference per declaration
(`identity`/`origin`/`uri`/`revision`) and consults no policy at all, because a skill reference
points at separately delivered content rather than asking for a capability. Saying the compiler
"narrows tool identities and skill references against the permission policy" is false for skills —
and the shipped cases assert the two channels separately precisely so that a merged description
cannot pass.

**Cross-leaf effect on this route's packaged corpus.** This leaf extended L1's
`skills/l-01-agent-lifecycles/composition-manifest.json` with per-role `tools[]` and `skills[]`
plus `launcher.operations[]`, and the governed generated copy under
`mcp/src/agents_remember/package_data/runtime/skills/` moved with it (all ten copies share one
sha256). The change is purely additive — 38 keys added, 0 removed, 0 values changed — and it is
**not** a permission model: the manifest declares what a role *asks for*, the admitted
`CapsuleToolPolicy` snapshot decides what is *permitted*, and the compiler refuses a request
outside it. `launcher.operations` changing from `[]` to `["orientation","coordination"]` is the one
addition with a behavioral consequence; reverting it makes every launcher compilation refuse
`operation-not-applicable` by design. The owning seat ruled the change ACCEPTED on 2026-09-16 after
independently reproducing the structural diff, L1's unedited corpus test (6 passed) and
`scripts/sync-skills.py --check` (exit 0).

**Layer contract status.** `layers.toml` declares a target order and deliberately fails against the
current tree; measured on this candidate the tree reports 16 pre-existing violations (all
`worktrees -> memory_quality` and its siblings). None names a role-capsule module, every internal
import from the new modules points at a strictly lower rank, and there are 0 undeclared imports. Do
not read the layer contract as currently satisfied.

## Detailed Route Context

The MCP package routes mutation tools through closed configured-contract admission, journal-rooted lifecycle controls, explicit enclosure adoption/legacy repair, and disposable door-based scheduling.

**260731-EFA-L21 — checkout coordination isolation.** An undeclared source-checkout invocation is
classified before runtime configuration is read: a linked worktree receives a synthetic
provider-disabled configuration rooted at `provider-runtime/dev-ar-coordination`, while a primary
checkout refuses live coordination access. Trusted MCP/dashboard declarations and installed
package execution retain the configured coordinator. The detached task-operation worker uses the
separate explicit `lifecycle-operation` mode because it must finalize one plane-owned durable
operation but is not a store daemon. The kernel policy and durable-store guard carry the invariant;
application startup, worker entry, and test bootstrap declare only their respective modes.

**260731-EFA-L1: `package_data/dashboard/` is no longer in this package's version-controlled
surface.** The bundle, its `dashboard.fingerprint` sidecar, and local `mcp/build/` / `mcp/dist/`
output are git-ignored. The recursive `package_data/**/*` glob in `mcp/pyproject.toml` still ships
whatever is present at build time, so the wheel and sdist carry a cockpit — placed by the release
job, verified by the release job. Building the package from a checkout with no bundle succeeds and
yields an installation whose `/` answers 503 with the build command. Two consequences for anyone
working in this package: a dashboard change produces **no packaged-asset churn to review**, and
`serving/build_info.py`'s `dashboardBuild` is routinely absent in a source checkout, so it must be
consumed as optional.

FEUI-MX-FIX-2 changed no MCP package source contract. Its `package_data/dashboard/` index,
fingerprint, and content-hashed assets were shipped output from the reviewed `dashboard/src/`
build, deliberately excluded from one-to-one onboarding: browser open authority is documented under
the dashboard source cards and overviews. (Historical: package parity was then proven by
`scripts/sync-dashboard.py --check`, and a generated rollover had to land as one complete
add/delete set. Neither applies now — the tree is untracked, the `--check` mode is gone, and the
release-time refusal to place a non-current `dist` is the surviving proof.)

260715-FEUI-L9R crosses `mcp/` through the existing `agents_remember.serving` route and the shipped
dashboard boundary. Serving resolves the optional packaged dashboard fingerprint into
`build.dashboardBuild`, revalidates entry HTML while leaving content-hashed assets on ordinary
static caching, keeps pre-session `GET /api/harnesses` rows to `id`/`name`/`detected`, treats raw
event offsets as untrusted hints and emits only server-aligned top-level-object records parsed once,
and gives every dashboard-owned tmux client a clean tmux identity with `TERM=xterm-256color`.
Product mismatch/reattach behavior and request ownership remain governed by `dashboard/src/`; the
implementation contract lives in `mcp/src/agents_remember/serving/` and its regression boundary in
`mcp/tests/`. The synchronized `package_data/dashboard/` rollover is shipped output, not a second
source implementation.

260715-FEUI-L9 is a contract/foundation path, not yet a runtime projection path. Python consumers
validate normalized products and address separate active/library cursors through the new serving
route. The repository-only native helper and three installed-runtime fixtures supply redacted,
non-enabling evidence. Hostile contract tests and topology tests fail closed on provenance,
identity, generation, contradictory status/capability state, router drift, helper path drift, and
fixture promotion.

260715-FEUI-L5 routes exact-session submit/reconcile/status/withdraw through the daemon and private
IPC into one epoch-bound authority. Async adapter preflight precedes a lock-linearized final write
claim; Codex, Claude, and Pi dispatch now without native queues. Direct exact-ref completion reaches
authority before coalesced publication, early terminal truth can dominate unknown, and bounded
retention never evicts live/active/unknown work. Public responses remain cockpit-only/raw-free;
post-write loss remains ambiguous and reconciles under the same request id.

260714-ACPUI-L4 freezes the package's daemon-side own-adapter contract. A bounded
`HarnessCapabilityCatalog` discovers the installed/authenticated native catalog without a model
turn, fingerprints the executable/argv, single-flights by built-in harness, and quarantines the
observed entry after failed explicit auth refresh. FastAPI routes expose that normalized catalog,
an optional complete launch pair, exact-session advertise and honest setters, whole-message submit,
and same-id reconciliation. Live reopen returns retained process truth or conflicts without
rewriting it; request-byte ambiguity never triggers blind resend; duplicate ids converge on the
retained receipt; public responses strip adapter-private raw evidence; and liveness precedes
support classification. The route is server-only and preserves role spawn and the durable bus.

260714-ACPUI-L3 adds normalized same-session model/effort mutation to the native hosted-control
package. `HarnessControlBridge` sends both setters through the same bounded FIFO as prompts, and
the queue validates the exact five-value `SetResult` truth contract without inventing an effective
value. Claude uses structured stream-json commands plus exact replay/terminal evidence; Codex
binds each accepted prompt to its selection epoch and applies pending settings on a fresh
`turn/start` without reconnecting; Pi holds mutation, state readback, and refreshed catalog inside
one finite evidence transaction so model errors and thinking clamps stay distinct. Cancellation or
late vendor replies cannot poison the shared reader/queue, and no setter depends on composer,
tmux, session-command, or injector paths. Existing role/leaf spawn provenance and the durable
inter-agent inbox remain independent moats rather than alternate configuration transports.

260714-ACPUI-L2 connects the existing role-settings authority to the native hosted launch
boundary. A role-configured Claude, Codex, or Pi seat carries one complete typed
`ResolvedLaunch`; the hosted runner performs token-free per-install discovery, validates effort
under the selected model, refuses duplicate adapter-owned selectors before discovery, and applies
Claude flags, Codex `thread/start` configuration, or Pi's provider-qualified flags before the
configured vendor session starts. Missing selections refuse before tmux; later discovery/startup
failures remain queryable as exact failed/rejected control snapshots. Normalized model/effort is
never synthesized into a session command. Role/leaf provenance and the durable inter-agent inbox
continue through their existing catalog and control-plane paths.

The package-data lifecycle and install skills now teach the same dynamic/native contract. Their
canonical sources and harness mirrors are sync products outside this onboarding slice; the
eligible package-data copies remain the shipped runtime evidence documented here.

260713-PHA-L6 extends the package's protocol-backed serving contract with structured Claude,
Codex, and Pi capability negotiation and a strict two-field rolling inbox-reader compatibility
seam. The full cutover reload boundary includes the daemon, MCP-owning clients, per-session runners
and adapters, and browser tabs; R10 resource performance remains queued.

260713-PHA-L4 adds four unregistered serving modules for the pinned Pi 0.80.6 RPC boundary:
strict framing/schema parsing, owned subprocess transport, normalized event settlement, and the
L1-backed adapter with exact-session reconnect and post-cursor no-resend reconciliation. The
paired tests and isolated smoke live under `mcp/tests`; production registration remains L5 scope.

HFX2-L20 closes the live consume/redelivery resurrection race without changing a public payload:
consume remains an append-only terminal fact, and the shared current-state/retention fold refuses to
let a later stale pending delivery snapshot reverse it. Polling and supervisor redelivery therefore
stay terminal after acknowledgement; compaction remains the cleanup boundary.

HFX2-L17 splits immutable `spawnRole` provenance from current `seatRole` binding. The catalog
migrates legacy rows in place; spawn/attach liveness-check only the same `(leafKey, seatRole)`;
retire authority, expectations, inbox/supervisor findings, chain credit, landing, provider role
discovery, and dashboard rendering use the binding. The MCP/HTTP attach surfaces accept role and
return `role-required` for an untyped hand-opened harness, while role-suffixed leaf refs refuse with
canonical pair guidance. Tests cover the workaround museum and supervisor behavior at fleet sizes
3 and 30.

The regenerated dashboard assets are deliberately not onboarding subjects. Durable proof stays at
the dashboard source, `scripts/sync-dashboard.py` build/package parity check, and serving static
boundary. HFX2-L21 follows that existing boundary: its adjustable Chats sidebar is frontend-only,
while this route carries only the regenerated `package_data/dashboard/` bundle and fingerprint.

HFX2-L15 replaces screen-grammar dispatch credit with one repository-wide acceptance path:
`HarnessSessionLog` binds the unique id-bearing message in the spawn cwd, `injector.deliver`
applies calibrated Claude/Codex windows, and `TerminalPaster` permits one Enter re-press plus one
verified-absence clear/replace re-paste. Spawn, durable inbox, supervisor redelivery, and REST paste
all compose that path. Catalog provenance records resolved knobs, log binding, and an optional
`replacementForLeaf`; tests are pinned to this checkout so the full gate cannot import a sibling
editable install.

260707-HFX2-L13 closes the L12 package residuals and reconciles the reviewed HFX3 runtime seams that
round 2 actually changed. Observer storage now coalesces lifecycle heartbeats into bounded sidecars,
fully reclaims dormant unprotected lifecycle directories, and lock-guards live workspace compaction
with virtual cursor offsets. Projection/state broadcasts carry bounded body-free task/series summaries
with `bodyRevision`; the serving package exposes the path-confined on-demand task-body endpoint and
the dashboard fetches only the visible body. Control-plane/supervisor changes route leaf signals and
completion wake to the current manager, suppress stale predicates when the leaf chain progressed,
enforce a five-minute later-rung floor, and prevent duplicate same-sweep transitions. The CS-6 tests
pin two-size river/heartbeat/task-payload bounds plus the corrected lifecycle-log cache property.
Current code still excludes an unbound worker from active-phase chain credit; reviewer S1 remains the
accepted HFX2-L14 S7 follow-up, and this summary does not certify the separate post-integration HFX3
retro gate.

Start in `src/agents_remember/mcp/config.py` for trusted settings parsing, then
`src/agents_remember/mcp/registration/` for the exposed MCP tools — since
260731-EFA-L2 the `@server.tool()` declarations live there, one module per tool
family, and `server.py` is reduced to process wiring: it installs
`mcp/compact_content.py` (tool-result text minification), installs the ambient
lifecycle, and walks `TOOL_REGISTRARS`, which is the only place that decides
which families a server advertises and in what order. The `mcp/tools/` package
still holds the payload builders those declarations call; verbose tools
additionally file bulk diagnostics under `temp/tool-reports/` via
`mcp/tool_reports.py` and return compact outcomes with a `reportPath`. Then
`models/tools/tool_registry.py` for public response contracts,
`application/context_packet.py` for compact `ContextPacketV2` startup packets,
and `application/runtime/install.py` plus `install/runtime.py` for MCP-owned
runtime installation. Provider status is composed in `providers/status.py`; the serving/observer path can
refresh the persisted provider current-state snapshot before live dashboard projection so provider rows are
not limited to the last explicit diagnostics/status command.
`providers/metrics.py` (260707-HFX-L1, containment R4) is the central
containment metrics module: the serving daemon samples labeled provider
containers (label-discovered, read-only, dockerless-safe) into its store under
`logs/observer/providers/` (`metrics.jsonl` + replace-atomic
`metrics-current.json`), and `provider_status` attaches the current snapshot
even while providers are disabled so leftover stacks stay observable.
provider lifecycle settings are generated from MCP settings in
`providers/settings.py`. Provider lifecycle implementation is now split between
the `providers/lifecycle/` facade/shared helpers and provider-owned
`providers/cgc/lifecycle/` plus `providers/grepai/lifecycle/` packages; there
is no legacy `provider_lifecycle.py` facade. Memory-layer quality control lives under
`src/agents_remember/memory_quality/`: integrity checks include the onboarding
drift classifier/summary, and style checks currently include update-history
newest-first ordering. Shared onboarding-document parsing, route-overview discovery, and the
"meaningful body vs metadata/history" change classification live in
`kernel/onboarding_doc.py`; the closeout body gates in
`worktrees/modules/onboarding.py` consume them and accept explicit
`No content impact:` / `No route impact:` Update History markers as in-band
reviewed-no-impact attestations. Branch freshness (issue #54: is a local
branch current with its upstream, plus ahead/behind counts) lives in
`kernel/git_freshness.py` beside `kernel/git_facts.py`; the `context_packet`
application entry point surfaces it as the opt-in `include_freshness` packet section
while the computed ledger remains an informational consumer view, forming the lifecycle-start
staleness checkpoint. Route-index generation is split between
`kernel/route_index.py`, which renders route-local metadata, and
`kernel/route_index_census.py`, which validates the repository root and freezes
one exact Git/path-rule source snapshot for membership, coverage, and counts.
Tracked and untracked records are NUL-delimited, ignored/generated paths are
excluded by Git plus resolved storage rules, symlinks are classified without
following their targets, and ambient Git repository selectors are scrubbed by
`kernel/git_command.py` — which since 260731-EFA-L3 is the **only** module in
this package that spawns git at all, so that scrubbing is no longer a census
property. Application entry points and worktree closeout pass the resolved
repository identity and `StorageSettings` explicitly rather than rediscovering
authority inside the builder.

**`kernel/git_command.py` is the package's one git runner (260731-EFA-L3).** Six
near-identical private copies had drifted apart — in `worktrees/modules/git.py`,
`code_quality/diff_coverage.py`, `memory/carryover.py`,
`memory_quality/integrity/check_missing_onboarding.py`,
`memory_quality/integrity/onboarding_drift_check/git_ops.py` and
`kernel/route_index_census.py` — and only the kernel's passed
`env=git_environment()`. With `GIT_DIR` exported, the same logical operation
therefore landed in a *different repository* depending on which copy ran, and the
unguarded worktree copy sat behind `commit`, `merge --ff-only`, `reset --hard`,
`rebase`, `branch -D`, `worktree remove --force` and `push origin --delete`.
The historical EFA-L3 census counted twenty-six imports from the single runner; it is not a current count. Twenty-four took the symbol
(`from agents_remember.kernel.git_command import ...`) and two take the module
(`from agents_remember.kernel import git_command`, in `code_quality/check.py` and
`code_quality/diff_coverage.py`). One importer wants `git_environment()` rather than, or as well as,
`run_git`: `worktrees/modules/landing.py::_pr_for` spawns `gh pr list`, which is not git but
resolves the repository *through* git, so an inherited `GIT_DIR` would list another repository's
pull requests. (`benchmarks/runner_modules/commands.py` used to be named here for composing its own
argv; since 260731-EFA-L3 it calls `run_git` like every other module, and the historical census above
is what still lists it.) The quality-gate adapter no longer launches a host wrapper or builds a host
environment; it hands the reconstructed candidate and ancestry bundle to the pinned Dagger graph.

The runner always scrubs the eight selectors, always declares its stdin — `DEVNULL`, or
`input_text` for the `git patch-id` call in `memory/carryover.py` — and carries three
timeout classes in place of the former hard-coded `timeout=5`:
`GIT_LOCAL_TIMEOUT_SECONDS = 300` (a rebase or status over a large tree can
legitimately churn for minutes), `GIT_REMOTE_TIMEOUT_SECONDS = 120` (a remote that
has not moved bytes is wedged, and a wedged remote inside an MCP tool call has no
cancellation path), and `GIT_METADATA_TIMEOUT_SECONDS = 30` for constant-time reads
on interactive paths. Consolidating onto the old five-second bound unchanged would
have replaced a redirection bug with a five-second failure on every integrate.

**Since 260913-LCA-L3 those three ways to aim a command are one object.** `run_git(repo_root, args,
options=None)` takes a `GitRunnerOptions` — `work_dir`, `input_text`, and a `timeout` defaulting to
`GIT_LOCAL_TIMEOUT_SECONDS` — plus a fourth field, `identity`, which adds `GIT_AUTHOR_*` and
`GIT_COMMITTER_*` names on top of the sanitized environment. `identity` exists for exactly one
command: `git commit-tree` reads the author, the committer and both timestamps from those variables
and from nowhere else, so the memory-history rewrite that must reproduce an existing commit byte for
byte has no argv spelling for it. It can never reintroduce a repository selector — the selector strip
runs first, and a name in `GIT_REPOSITORY_SELECTOR_ENV` raises `ValueError` instead of being set — and
the reason the runner's signature collapsed back to two positional facts is that these are one
concept rather than four unrelated keywords. 38 call sites across 19 files were migrated
mechanically, and not one of them changed which command it runs or which timeout class it names.

**The class belongs to the command, not to the module that calls it.** Consolidating onto a runner
whose *default* is the local bound would have silently moved every `rev-parse` from 5s to 300s — a
60x loosening on reads that sit under `resolve_context`, which runs on essentially every tool call,
with no cancellation path for the client. So the band is named per command:
`rev-parse --is-inside-work-tree`, `rev-parse HEAD`, `branch --show-current` and
`rev-parse --abbrev-ref <branch>@{upstream}` take the metadata bound, while `status --porcelain`
and `rev-list --left-right --count` are not constant time (one stats the whole work tree, the other
walks history) and keep the local bound **explicitly named** rather than defaulted.
`kernel/git_facts.py::_git_stdout` makes `timeout` a *required* keyword-only argument for exactly
that reason — a call site that leaves the class to the default is a type error, not a quiet
inheritance — and it passes that bound on through `GitRunnerOptions`.
`kernel/git_freshness.py::fetch_remote` keeps its own 30s `DEFAULT_FETCH_TIMEOUT`.
The former cross-module timeout-comparison suite (`TimeoutClassTests` in
`mcp/tests/test_git_command.py`) was removed by the 2026-09-06 test-inventory reduction at
`d3610903`; the current call sites and the canonical constants own the contract now, and the
`mcp/tests` route records that reduction.

`mcp/tests/test_git_command.py` holds the retained single-runner half: a decoy repository the
selectors point at, a stalled command asserted to trip an explicit bound, an isolated
candidate-index case, and the exact private-preparation refusals (forged or cancelled authority,
hidden index flags, physical drift, stale bindings). The AST sweep that failed on a second runner,
the guard-on-the-guard suite that planted each bypass form, and the per-command timeout assertions
were part of the same reduction and are **not** current coverage; the single-runner boundary is
carried by the source and by this route's description of it rather than by a test.

Branch-memory carryover (`memory/carryover.py`)
plans route-overview candidates beside file sidecars (route-keyed, never
auto-carried when content differs), requires effective official-memory storage
authority through `memory/carryover_authority.py` before any write, regenerates
official-side route indexes after a carry from that same authority, guarded on
a clean official-ref checkout, and fast-forwards memory `main` to the official checkout tip
(`memory_main_advance`, issue #54) so non-main cycles no longer leave memory
main behind. Worktree lifecycle finalization lives in
`worktrees/modules/finalize.py` and is exposed as `lifecycle_finalize_task`;
it proves the landed commit is reachable from the contract's local
target/source branch, checks memory carryover, runs or verifies cleanup, and
reconciles JSON-primary task documents after landing. Runtime package data under
`src/agents_remember/package_data/` is synchronized from canonical root runtime
asset folders by `scripts/sync-runtime.py`, and the sync behavior is covered by
`mcp/tests/test_sync_runtime.py` plus the generated-copy check that runs in both hook tiers. The
built dashboard cockpit ships under `package_data/dashboard/`, placed there from `dashboard/dist/`
by `scripts/sync-dashboard.py`. Since 260731-EFA-L1 that placement is a **release build step**: the
bundle is git-ignored, no hook or CI job checks it, and `scripts/sync-dashboard.py` has no
`--check` mode. It is covered by `mcp/tests/test_sync_dashboard.py` and driven by
`.github/workflows/publish-mcp-to-pypi.yml`.

`package_data/` has a **third population** since 260731-EFA-L3, and it is neither synced from a
canonical root folder nor built at release: `package_data/tiktoken/` holds the vendored `o200k_base`
vocabulary that `models/tokens.py` counts response tokens with. Unlike the dashboard bundle it is
**tracked in version control**, its file name is `sha1(<download URL>)` because that is the only name
`tiktoken.load.read_file_cached` can hit, and root `.gitattributes` names **that exact filename**
`-text` so no EOL filter can touch it on a `core.autocrlf=true` clone. It ships
because `mcp/tools/base.py` imports `models/tokens.py` and `DEFAULT_TOKEN_COUNTER` is built at module
scope: before the file was vendored, `tiktoken.get_encoding("o200k_base")` opened an HTTPS connection
to `openaipublic.blob.core.windows.net` while the server was still importing, so a fresh container,
an offline machine and a hermetic CI job could not start the server at all.

**This package verifies the vocabulary itself, and that is a correctness property rather than
belt-and-braces.** `vendored_vocabulary_cache` calls the private `_verify_vendored_vocabulary` first,
*before* it touches `TIKTOKEN_CACHE_DIR` at all, and that helper raises `TokenizerVocabularyError`
for three cases: an encoding this package does not ship, an absent file, and a file whose SHA-256
does not match `VENDORED_VOCABULARY_SHA256`. Leaving the digest check to tiktoken would not have
been equivalent — tiktoken checks the same hash but does **not** fail closed on it:
`read_file_cached` deletes the offending file and downloads a replacement over it, which pointed at
this package's directory means a network fetch on the startup path plus a rewrite of the installed
tree, or a `PermissionError` from the write-back on the read-only installs this is written for.
Checking first is what makes corruption behave like absence. Only the *verified* file's own parent
directory is then handed to tiktoken, so it cannot be pointed at a directory whose contents were not
checked, and the override is scoped to the one load (the vendored directory sits inside the
installed package, which is routinely read-only). `_CACHE_DIR_LOCK` is a `threading.RLock` rather
than a `Lock` because the guarded region spans the `yield`: the obvious use of an exported context
manager — `with vendored_vocabulary_cache(name): TiktokenTokenCounter()` — has the counter's own
load re-enter it on the same thread, which on a plain `Lock` is a permanent hang with no timeout and
no diagnostic. Counts and the reported `tiktoken:o200k_base` name are unchanged — the shipped bytes
are the download — and `mcp/tests/test_cold_start.py` is the regression line.

## Route Model

- `src/agents_remember/serving/conversation/` — strict normalized structured-conversation models,
  exactly two read ports, and one root composing the independently owned `active`, `library`, and
  `control` child routers. The serving overview carries the detailed authority boundaries.
- `native_helpers/conversation_library/` — private locked Node helper for redacted repository-only
  runtime observations. Its output and fixture versions are evidence, never capability promotion.
- `serving/pi_rpc_protocol.py`, `serving/pi_rpc_process.py`, `serving/pi_rpc_events.py`, and
  `serving/pi_rpc_adapter.py` — the currently registered Pi RPC protocol/process/event/adapter chain beneath the shared factory; historical leaf-local evidence includes
  `mcp/tests/test_pi_rpc_adapter.py`, `test_pi_rpc_process.py`, `test_pi_rpc_real_smoke.py`, and
  the two `fixtures/pi_rpc/` files provide the fake, subprocess, and isolated pinned-smoke proof.

The MCP package separates three surfaces:

- `agents_remember.mcp` owns transport wiring, tool registration, and trusted
  settings parsing. Since 260703-L13 the authority file owns BOOT INFRASTRUCTURE
  only: the agentic orchestration family (`orchestration.*` — gate delegation,
  loop knobs, role knobs flat + per-level (`roles`/`rolesPerLevel`, incl. the
  L16 free-form launchArgs/promptKeywords/sessionCommands escape hatch),
  concurrency caps, spawn harness preference, and the L16 harness-definition
  table `orchestration.harnesses`) lives in
  the GLOBAL `<coordinationRoot>/system/settings.json` with
  `<code-repo>/system/settings.json` repo-local overrides, parsed PER-USE by the
  kernel loader `kernel/agentic_settings.py` (leaf-key deep merge, arrays
  replace, unknown `orchestration.*` keys fail loud naming the file; unknown
  top-level families tolerated — `contextProviders` is reserved to return
  there). `mcp/config.py` keeps ONE boot-snapshot consumer: gateDelegation is
  read from the global file at boot, with a warned one-cycle authority-file
  legacy fallback. The authority file's `providers` map runs the OPPOSITE way
  since 260707-HFX-L1 (containment R1): the boot snapshot is NOT launch
  authority — launch-capable operations re-read the map from disk through
  `reload_provider_authority`/`require_provider_launch_authority` (unreadable
  or invalid ⇒ fail-closed refusal, never a snapshot fallback), so editing
  `providers` to `{}` bites running servers immediately while stop/status/
  cleanup stay legal; starter/setup (the renderer) writes the shared coordination settings file when it is absent and
  `spawn_agent_session` resolves its spend knobs through the loader (260703-L16 + HFX2-L10:
  repo-local level override > global level override > repo-local role default >
  global role default > spawn preference/detection-gated default; ids against
  the EFFECTIVE registry; model/effort validated per-harness at dispatch and
  APPLIED onto the harness argv; legacy caller spend fields, direct launch/session controls, and
  maintained harness-native spend/endpoint env keys refuse with `spend-override-unsupported` before
  spawning — manual: `docs/reference/harnesses.md`).
- `agents_remember.application` owns operation-level composition such as
  `context_packet`, provider tools, worktree tools, memory tools, benchmarks,
  and `runtime_install`.
- `agents_remember.models` owns public MCP response contracts and the
  tool-to-response-model registry used by the `mcp/tools/` payload builders.
- `agents_remember.certification` owns repository-neutral five-gate rail registry, canonical
  plan, bounded validation, and typed terminal-result contracts. It does not own concrete
  repository profiles or execution.
- `agents_remember.tasks` owns JSON-primary task documents plus the strict persisted execution
  vocabulary: commanded-master nature, sprint reasoned AON graph, exact cross-document membership,
  deterministic derived waves, rendering, and rollback-safe publication. The application layer
  owns the explicit finite migration and validates supported task-doc edits before publication.
- First-class service domains such as `kernel`, `providers`, `memory_quality`,
  `worktrees`, and `install` own deterministic behavior.
- `agents_remember.observer` owns the observable-lifecycle **event substrate +
  projection** (the 3.0 browser-dashboard direction): the append-only
  `ar-observer-event/v1` log, local ULID minting, the per-lifecycle event store,
  the ambient lifecycle + six `lifecycle_*` signal tools (with the `_tool_payload`
  emission hook attributing every tool call), and the **projection read side**: the
  pure reducer that folds the logs plus file snapshots into the resolved state tree
  — the structural surfaces (slice 3a) plus the slice-3b analytical surfaces (drift
  read from a persisted snapshot, sidecar staleness, setup, route coverage, tool
  reports, ledger), the derived rollups, and — slice 05 — the server-computed
  **attention queue** (`build_attention_queue` → the derived `Analytics.attentionQueue`), plus —
  slice 05 (5c) — paused **persistent lifecycles** synthesized from worktree contracts,
  **per-worktree provider stacks** (surface 4, bound to worktree/repo/role), Task 12's repo-covered
  workspace provider nodes (CGC watcher rows and GrepAI configured `targetRepos` become repo satellites;
  GrepAI `targetRepos` are addressable project targets inside one aggregate provider instance, not
  separate per-repo provider processes, while providers without explicit target evidence stay aggregate),
  and body-free task summaries on
  `TaskDocNode`; the path-confined on-demand task-document endpoint supplies full reader content. Task 29 adds lifecycle-aware raw-event lifetime
  handling and projection freshness hygiene: terminal lifecycle `events.jsonl` logs are physically
  pruned after the post-completion grace window, fresh raw-event SSE connections start from retained
  offsets instead of replaying all history, projection reads cache repo surfaces briefly, and worktree
  provider/runtime projection admits only active enclosure-backed groups instead of parked or stale
  worktrees. Task 29 S7 adds actionable-drift provenance/dismissal and keeps raw Event River row
  lifetime at the backend retention boundary rather than a frontend count cap. Task 34 re-keys that
  raw-event retention on **inactivity** rather than termination: `event_retention.py` prunes a fleeting
  or enclosure lifecycle log after >1h with no real (non-heartbeat) activity (not on `lifecycle.ended`),
  `ambient.py`'s heartbeat ticker decays after ~10 min idle so a dormant log ages out, and `/api/events`
  does one retained-backlog scan per connect, filters `lifecycle.heartbeat`, and streams a bounded
  chunked backlog. Task 32 adds physical retention for persisted
  drift snapshots: cleanup deletes the exact code-worktree snapshot for the contract being reclaimed,
  and projection prunes valid deleted-worktree drift snapshots before reading the analytical surface.
  Task 33 adds the `WorkspaceProjection.activeWorktreeGroups` field (sourced from the same
  `active_enclosure_worktree_groups` admission the Engine Room uses) that the dashboard Topology consumes
  to bound its constellation to active worktree enclosures.
  Task 21 adds the folder-keyed master token aggregate:
  `SeriesNode.seriesTokenTotal` is composed from projected sibling leaf task docs and lifecycle token totals.
  Slice 05l Part 1 (backend teardown
  visibility) extends the Engine Room surface: the reducer now projects the `abandoned` worktree
  phase (from `worktrees/modules/guidance.py`) and **drops disposed** (cleaned-up/abandoned)
  enclosures from the active `engineProcesses` so the frontend (05k) animates the teardown.
  Slice 05l Part 2 hardens the **landing-arc probe** (`worktrees/modules/landing.py`) so the
  dashboard follows a REAL remote landing: the protected target `origin/<base>` is probed **directly**
  via `git ls-remote` (visible across the whole landing window before any PR and even when `gh` is
  absent), and the PR ref carries gh's open/merge timestamp on the additive `LandingRefNode.at`.
  Slice 05m lands **carryover-before-cleanup** lifecycle correctness in `worktrees/modules/`
  (`guidance.carryover_done` proves the real memory output reaches the official source; `lifecycle_guidance` routes a
  `carryover-pending` phase before `cleanup-pending`; `cleanup_result` hard-refuses cleanup until the
  parked memory is carried home), and the observer reducer now follows it — `_GUIDANCE_PHASE` projects
  `carryover-pending` and the engine-room node carries the display-only `carryoverDoneAt` milestone
  (5k renders the seam). Task 13 corrects cleanup's branch and dry-run preview rules in the same
  worktree domain: task work branches are deleted only after explicit reachability proof against the
  contract source branch, and dry-runs classify worktree group directories after planned
  worktree/provider-runtime removals. Task 14 narrows cleanup to the finalized child edge: cleanup
  retires task work branches only and preserves parent/source branches for their own lifecycle edge.
  Task 23/24/L3 adds the interaction-retention read side: gate logs and operator-inbox rows are treated as
  disposable interaction records; reads project retained state while approved writer-owned compaction reclaims logs, and `AgentPickupNode` projects
  pending inbox entries as waiting-for-agent/check-chat feedback for the dashboard, including L3
  sender/recipient role, message kind, artifact, and hosted-delivery metadata.
  The series-contract resolver in `worktrees/task_resolver.py` owns task-name lookup,
  nested parent-task disambiguation, raw leaf `enclosures/<leaf-id>/series-contract.md` resolution, archive
  exclusion, and root-task archival into `tasks/<repo>/0_archive/`. Since 260913-LCA-L5 the
  task-layout **path vocabulary** it publishes is defined one layer down in `tasks/task_paths.py`
  (`series-contract.md`, `0_archive`, `enclosures/`, `slugify`, the two path builders and the two
  predicates) and re-exported here under an explicit `__all__`, so `layers.toml`'s `tasks`(9) <
  `worktrees`(10) order holds while every existing caller keeps importing `worktrees.task_resolver`, and
  there is exactly one definition of each rule. `worktrees/leaf_refs.py` owns
  qualified/doc-id/legacy-stem leaf-ref validation and canonical id normalization for write surfaces,
  including schema-marker screening for sibling task-document JSON and standalone/light `task.json`
  doc-id candidates.
  Current contract loading parses the named contract without healing task identities as a read side effect; explicit migration and startup own repairs. Package startup composes the optional dashboard daemon through its trusted runtime entry. The damaged legacy paragraph recovered in L31 cannot supply further current claims.

## Historical milestone context: L23 Plane-Owned Source Lineage

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The MCP now resolves task identity to contract-backed super/master/leaf Git
edges before structural spawn, assignment, attach, start, or reopen. Strict
models, application translation, observer projection, and dashboard transport
share one evidence shape. Unavailable or stale ancestry fails closed and points
to ordered contract-addressed `worktree_sync`; agent-carried ids are not part of
the protocol.

## Historical milestone context: L23 Current Lineage And Package Boundary

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The MCP package now groups runtime installation, startup, and skill installation under
`application.runtime`, and lifecycle responses, finalization, and durable operation DTOs under
`models.lifecycles`. Task-derived source lineage is enforced at start/resume, immediately before
curator dispatch, and through closeout/integration preflight, post-quality, and final mutation
boundaries. The MCP transport remains a thin registration/forwarding layer over those application,
model, and worktree owners.

## Development And Delivery Separation

Ordinary isolated host pytest is the supported development loop. Only the genuine Dagger quality publication and lifecycle owners provide certifying authority. The retired host diagnostic analyzer is not required to permit that loop and must not be restored.

## Historical milestone context: R42 Recovery And Test Ownership

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The finalization proof and typed memory-closeout outcome now live with the other irreversible-cell
recovery primitives in `worktrees/closeout_recovery.py`; `worktrees/modules/closeout.py` imports
them and remains the coordinator. Two focused test modules split direct environment authorization
and exact staged gate scope out of oversized suites without changing the production boundary.

## Historical milestone context: 260815-DAG-L2 Packaged Planning Doctrine

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The packaged `l-01-agent-lifecycles` assets now mirror the canonical nature-aware planning
contract. Architect owns the initial strategist and plan-review loop; orchestrator adopts the
ruled topology choice and a graph only when one exists, records queue judgment, and recomputes the
ready frontier; managers distinguish organizational direct-super leaves from atomic branch-backed
blockers. Graph-less atomic-sequential execution is a valid reviewed topology. A sanctioned
strategist skip transfers the complete dependency, route, seam, classification, priority, and
topology-reasoning duty to the orchestrator rather than requiring a graph. The package also carries
the exact proposed-candidate master-exit handoff and leaf-owned remediation boundary.

## Historical milestone context: 260821-DAGQC-L4 Doctrine And Review Closure

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

Packaged review inventories treat untracked input as hostile filesystem evidence: NUL-safe
enumeration precedes no-follow type/mode/content inspection, and reports record disposition plus
race limits instead of silently omitting or following entries. Candidate priority has one effective
value — candidate override, otherwise master default — while the orchestrator retains portfolio
comparison authority. Graph-less atomic-sequential is valid; choosing a graph from that state first
attaches every master, then publishes one complete nodes-plus-evidence-edges batch.

Master handover packets cite canonical candidate, code ancestry, memory ancestry, and per-leaf
ledger references so receivers revalidate authority without copied maps. Existing `add_edge`
examples already carried `judgmentId`; no fabricated code fix or lifecycle evidence was added.
Delegated-authority redesign, disabled-memory behavior, mandatory-graph runtime, and declared-caller
trust redesign remain outside this leaf. Canonical and generated skill copies were synchronized,
but that sync check and direct targeted Vitest diagnostics are not Dagger acceptance evidence.

## Historical 260815-DAG-L3 Closeout Queue Control Plane (Superseded By CLIVE)

`closeout_queue` is the MCP route for declaring reviewed leaves before history moves, recomputing
their current readiness, and exposing deterministic ready/waiting/blocked/in-flight projections.
The application layer derives the structural caller from the ambient seat; the worktree service
separates manager logistics from orchestrator grading/selection; the models hold strict bounded
requests and durable state; the control plane owns the canonical sprint artifact plus one-record
WAL; and lifecycle hooks claim, certify, revalidate, consume, or reversibly release the exact
candidate around closeout and integration. The queue consumes canonical task-document judgment and
priority rows but never authors them.

## Historical milestone context: 260815-DAG-L4 L4 Integration-Authority Plane

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The MCP runtime now owns repository-global protected-ref census, durable closeout/integration operations, cross-operation leases, queue-before-repository lock ordering, exact named-ref compare-and-swap, atomic-series sealing, and guarded terminal/memory writers. Public tools preview the same authority they apply; direct CLI/helper paths cannot widen it.

## Historical milestone context: 260815-DAG-L14 Sprint-Structure Plane

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The MCP `task_doc` surface now registers the sprint-structure operations — `attach_master`,
`detach_master`, `linkage_report` — routed to `application/task_sprint_linkage.py`; a sprint `get`
carries `linkageFacts`, and the task-document writer census admits the linkage module. The
`ar-task-document/v1` route carries first-class sprint `seats` and typed `masterRef` rows.

## Historical milestone context: 260815-DAG-L12 Route Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The MCP package renders and projects the sprint execution graph for humans: `tasks/render.py` emits the deterministic mermaid document diagram, `tasks/execution_graph_titles.py` owns the shared title join, `observer/projection_graph.py` builds the render-ready `executionGraphView`, and the serving task-documents readers wire it onto `TaskDocNode`. Application writers thread the joined titles through every publish/preview site.

## Historical milestone context: 260815-DAG-L15 Route Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

New `tasks/serving_preflight.py` (served-build preflight, L15-R4) and `application/memory_quality_runs.py` (bounded async run registry, L15-R7); the `memory_quality_check` registration gained `wait`/`run_id`; topology/linkage authoring hardened (typed refusals, `create=False` dry-run locks); the L7 `worktrees/orchestration_portfolio.py` module + its test were deleted (recorded decision: doctrine + queue mechanism).

## Historical milestone context: 260815-DAG Master Full-Gate Repair Route Impact

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

New sub-package routes `application/task_docs/`, `models/queue/`, `worktrees/queue/`, `worktrees/integration/` (32 moved modules); the `task_doc` special-op wire-shape fix (`TaskDocResponse` fields + `_sprint_doc_identity`); closeout/reopen refactors; the package_data orchestration-task template copy re-synced.

## Historical 260821-CLIVE-L1 Closeout Architecture

Closeout now crosses one explicit input boundary before lifecycle authority or Git. `worktrees/closeout_input.py` derives typed enabled/not-applicable legs and emits one stripped `EffectiveCloseoutInput`; worktree closeout journals that value and per-repository mutation evidence, while direct landing shares the input contract but remains synchronous, lock-serialized, and intentionally not crash durable in L1. Lifecycle records—not queue rows—own accepted input, mutation proof, recovery projection, and exact contract-finalization identity. The queue remains a scheduling projection outside this leaf. Strict schema 3.0 replaces compatibility readers, and `contract_publication_text` is the one serializer used by publication and hashes.

## Historical milestone context: 260821-CLIVE-L2 Current Architecture

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The package surface now exposes retry, recover, cancel, revise, integrate, retire/supersede, bounded legacy handling, and enclosure adoption without private operation ids. Read-only degraded status remains separate from mutation admission. Expected lower reader/authority failures have one public projection; unexpected faults stay loud.

### Reconciled Source Evidence

- Public closeout payload delegates the current task-bound request. [165]

## Historical milestone context: 260821-DAGQC-L2 Packaged Doctrine Synchronization

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

No root-route responsibility changed. Packaged c-02 and curator doctrine mirrors now use the same
strict memory-quality request grammar as canonical sources; the package remains a synchronized
distribution target rather than a compatibility owner.

## Historical milestone context: 260824-PDLS — Python Testing Route

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

`agents_remember_test_support.testing` is the verification-only route for structural direct-test
eligibility, shared hermetic pytest bootstrap, Dagger admission composition, the canonical direct
runner, and route-neutral phase/causal reporting. Its lifecycle catalog governs 35 durable support,
data, policy, and task/date proof artifacts. Its explicit lane manifest classifies the complete
test-file population; nothing unmarked becomes unit evidence. The direct route is an explicit
content-sealed seven-node cohort, not a generic repository analyzer.

`models/test_evidence.py` separates diagnostic and certifying altitudes. The code-quality plane
keeps all Python lint/type/size/execution coverage while scoring product modules only, and one
source-derived dependency graph serves targeted selection, retry invalidation, and exact-node
causal localization. Lifecycle declarations are cross-checked against observed consumers and do
not self-prove completeness. The worktree plane consumes typed Dagger admission/evidence instead of reimplementing
test-route failure families. Removed analyzers, task/date baselines, and former global/random helper
owners have no compatibility facade.

## Historical milestone context: 260824-PDLS Final Package Reconciliation

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

The final tree moves the certifying pytest bootstrap to the verification-package root, keeps
diagnostics and route measurements non-certifying, consolidates dependency ownership and causal
failure evidence, and splits lifecycle and queue helpers by authority. The package retains one
Dagger acceptance path and introduces no fallback runner, compatibility facade, or queue-owned
commit evidence.

## MCAR Exact Future-Code Candidate Boundary

Ordinary leaf closeout now has one frozen, plane-derived pre-commit route identity: contract base,
stable observed HEAD, and the canonical isolated-index full add-all tree. Callers provide intent
and evidence but never the authoritative tree. Each concurrent observation uses a distinct
automatically cleaned enclosure-local index, so preview and admission cannot corrupt each other's
identity calculation or stage the user's real index.

This tree-bound semantic identity remains separate from lifecycle-operation reconciliation. A moved
HEAD is not treated as an operation output without unchanged operation identity or journaled commit
proof. Series/direct-existing landing stays on its committed-tree route. The focused source owner
and boundaries are documented in [worktrees/overview.md](src/agents_remember/worktrees/overview.md).

## MCAR Structured Curator-Coherence Authority

The MCP package now exposes one `curator_coherence` lifecycle API with
`status`/`prepare`/`publish`/`validate` actions. A stable task-local structured manifest selects one
content-addressed record and deterministic human projection; exact source-candidate judgments are
agent-owned and evidence-digest-bound. Requirement revision, delivery attempt, and immutable
content identity stay separate. Public memory readiness, closeout-door evidence, and closeout
admission invoke the same validator, so a ready memory result cannot later disagree with closeout
over a different hardcoded report. No historical-filename search or Markdown authority remains.

## MCAR-L03 Exact Code-Memory Pair Boundary

Every worktree-backed memory acceptance route now resolves one strict
`ar-memory-candidate-pair/v1` identity from the configured leaf contract. The identity binds the
exact code and memory repositories, worktree roots, source/work branches, base commits,
onboarding root and contract digest; the cache location is informational; a code tree or memory tree observed outside that
pair is not acceptance evidence. Memory-quality sync/start/poll, source-candidate attestation,
curator coherence, closeout preview/apply, and closeout recovery all carry and revalidate the same
pair before publishing or consuming evidence.

Repository-only memory quality remains an explicitly labeled diagnostic route. It cannot be
promoted to closeout evidence, and a moved base, wrong valid checkout, changed contract, or
candidate change produces a typed refusal with the exact sync/reprepare route. No path guessing,
ambient-checkout inference, duplicate resolver, or compatibility fallback was added.

## Historical milestone context: 260831-CCR-L23 No-Symlink Confinement

This retained milestone account records its implementation-time context. Current policy and source-backed route statements above govern; old test populations, proposed surfaces and intermediate acceptance procedures are not current obligations.

`kernel/sidecar_pairing.py` gained `confine_non_symlink_rel`: the stricter path guard for
immutable artifact roots (the task-local requirements surface) that requires every component to
exist and refuses symlinks — including in-root aliases — unlike the symlink-following
`confine_rel` used for code/onboarding pairing.

### L32 Citation Publication Evidence

- Projection admission precedes staging; declined claims retain their original bytes. [166]
- Accepted batches check complete document bytes and held source/cell bindings before atomic publication. [167]

## L34 Preparation Ownership

The kernel's [private preparation capability](src/agents_remember/kernel/git_preparation.py.md) and [closeout publication capability](src/agents_remember/kernel/git_closeout_publication.py.md) are distinct. Both use the singular Git command owner; preparation creates named private objects while publication binds exact expected-old logical refs. See the [preparation route](src/agents_remember/worktrees/integration/closeout/preparation/overview.md) for journal and memory execution composition.

## CCR-R12@v5 Current Closeout And Integration Contract

Normal worktree closeout/integration are transaction routes. Closeout preserves explicit approval,
candidate/source identity, Git safety, and recoverable mutation evidence; it commits code, performs
raw external-memory metadata/entity/route-index refresh, then commits substantive memory content and refreshes the consumer cache
mapping. Integration validates and publishes a prepared code/external-memory pair with ref/tree
compare-and-swap and no merge commit. These normal routes do not automatically run strict code
quality, memory quality, selected certification, curator coherence, or independent review. Full
suites are only an explicit developer request. Quality and memory tools remain available as explicit
preparation or diagnostic routes, and retained certification models/documentation are historical or
explicit evidence rather than a normal closeout prerequisite.

## Historical milestone context: 260913-LCA-L2 Ledger Attribution Reader In The Kernel

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

The package's ledger plane gained its second kernel authority, and the two are deliberately separate.
`kernel/memory_ledger.py` still owns the ledger **format** — parse, validate, serialize, prepend. The
new [kernel/memory_attribution.py](src/agents_remember/kernel/memory_attribution.py.md) owns the
ledger's **attribution**: it reads the `Code-Commit:` trailer each memory-content commit carries back
out of the history (`attributed_commits` walks the whole ancestry from a given commit,
`ledger_rows_from_attribution` turns each trailer into one row, `parse_code_commit_trailer` is the
message-level reader) and it declares the one `git cat-file -e <commit>^{commit}` object test.
`worktrees/ledger_projection` imports both: its `code_commit_exists` is a delegation, and its
`read_ledger_source` merges two records instead of reading the blob at `commit:memory.md` alone — the
attribution rows, and the rows the source commit's **own table** recorded, read on every path rather
than as a fallback for a history with no trailer. That distinction is not cosmetic: the L2 form
returned the trailers *alone* as soon as one existed, so a partially backfilled line read as a
nearly empty source; **260913-LCA-L11 corrected it** and also made the read exclude, with a recorded
reason and a reported count, any row the exact source commit cannot prove. The reader changes are
documented on the [worktrees route](src/agents_remember/worktrees/overview.md).

Two boundaries belong on this route because they are package-level. The trailer is inside the hashed
commit object, so an attribution cannot be added or altered after the fact — `git notes` was rejected
for exactly that reason, and that is what makes the attribution evidence rather than a claim. And the
tracked ledger commit is **not** retired: `memory.md` is still written, committed and proved by the
closeout family, and retiring that tracked form across closeout, direct landing, queue recovery,
series closeout, integration and sync is a separate leaf of the same master.

The key is declared once, here in the kernel, and since 260913-LCA-L4 it is also **written** here, by the
same module. The first version of this change set left two literals — one in this module and one in
`models/closeout/input.py`, which declared its own `CODE_COMMIT_TRAILER_KEY = "Code-Commit"` while
claiming to import it — and that shape fails silently, because a writer emitting trailers the reader
ignores looks like "no attribution exists" rather than like a bug. L2 made the model import the constant
(`input.py:9`); L4 went the rest of the way and made the model import the **renderer**
(`render_memory_content_message`, `kernel/memory_attribution.py:72-97`) instead of naming the key at all,
because a key that is one literal in two directions should have one function that interpolates it. So
`grep -rn '"Code-Commit"' --include=*.py mcp/` has exactly one hit, this module's declaration, and that
hit is now the only place the format exists — the identifier *and* its interpolation. The direction is the one `layers.toml` permits rather than a
preference: `order = [errors, kernel, models, ...]` with "a module in package P may import package Q
only when rank(Q) < rank(P)" means a kernel module importing a model would import upward, and a grep
over `mcp/src/agents_remember/kernel/` finds zero imports of `agents_remember.models`. The round trip
is guarded by a case that renders through the real writer, commits the message and reads the code
commit back out through the real reader.

### The Producer Surface Is Total, And It Is Five Sites

L4 closed the transition rather than leaving it three-quarters done, because a projected ledger cannot
tell "this producer kept the old shape" apart from "no attribution exists": the pairing is simply gone.
The census was taken at base `5bb124d4` from source and **corrects** the master's 2026-09-13T22:05
decision in two places — `worktrees/queue/closeout_recovery.py:209` is that route's CODE leg, not a
memory-content producer (a resumed closeout still owing its memory commit goes through
`closeout_external.py`, the producer the first attempt uses), and the producer the first census missed is
`worktrees/integration/closeout/preparation/memory_output.py:92`, the preparation route's memory-content
leg. The five memory-content producers are:

| Producer | Code commit it names |
| --- | --- |
| `worktrees/modules/closeout_external.py:165` | the accepted commit of the same closeout (and, transitively, a resumed closeout that still owes its memory commit) |
| `worktrees/integration/direct_landing/direct_landing_execution.py:270` | `operation_input.codeCommit` |
| `worktrees/integration/closeout/preparation/memory_output.py:92` | the candidate's certified code commit |
| `memory/carryover.py:846` | `official_head`, the commit its mapping already names |
| `memory/baseline.py:210` | the code source-branch commit its initial ledger row maps |

Every other commit site is trailerless **by rule, with a recorded reason** rather than by omission: each
ledger leg; `closeout_recovery.py:209` as a code commit; `sync_transaction_git.py`'s memory merge commits
(two memory parents, no single code commit to name); and carryover's nothing-to-carry path, which creates
no commit at all. Two of the five take their message as a **public argument of another tool**
(`memory_carryover_apply`, `memory_baseline_adopt`), which is why the renderer appends the trailer as its
own final block after a blank line instead of weaving it into the body — the caller's multi-paragraph
message survives byte for byte. `mcp/tests/test_memory_attribution_producers.py` holds the census: it
requires the key identifier and its interpolation in exactly one production module, forbids the trailer
being spelled as a quoted literal anywhere in production, and asserts each of the five producers reaches
a shared renderer entry. Its residual gap is stated rather than hidden — a future producer building the
string some third way is caught only by its own route's behavioural case, and the prepared leg has none.

## Historical milestone context: 260913-LCA-L3 The History Backfill, And Why It Is Deferred

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

The trailer rule decided how every memory-content commit is written **from that point on**. The
history written before it carries no trailer at all, so the ledger's rows for that history are proved
by the table each commit's own tree records rather than by its message. The third kernel module in
this plane, [kernel/memory_backfill.py](src/agents_remember/kernel/memory_backfill.py.md), is the
migration that closes that gap: it derives which commits must receive a trailer from the table the
history already records, and rewrites exactly those commit objects with the trailer appended.

**The rule that picks which pairings survive is declared, and it has two halves.**
`%(trailers:key=Code-Commit,valueonly)` renders one line per matching trailer and both readers take
the last, so one memory commit can carry exactly one code commit while the table records more pairings
than that allows. The selection is therefore: a **maximum matching** first, so no code commit is left
unnamed while a memory commit that could have named it stands empty — code commits offered
most-constrained-first, with a tie between two equally constrained claims going to the older row, read
off the table rather than off object names — and then a **fill** giving every memory commit the
matching did not reach its own oldest row. The fill is load-bearing rather than cosmetic: a matching is
symmetric and the format is not, so a matching alone leaves dozens of named memory commits
unattributed. Every row the rule passes over is reported, from a closed five-literal vocabulary that
splits into **holes** no selection could repair (a memory cell that names no object, a memory commit
outside the tip's ancestry, a code commit the code repository does not hold) and **declines** the rule
chose (a memory commit already carrying another code commit, a code commit already named by an earlier
row), and every code commit left with no trailer at all is named in `lost_claims` together with the
memory commit and the code commit that took its pairing — because a migration that silently collapsed
rows would look exactly like one with nothing to do, and a loss reported as a number is not
adjudicable. A plan that lost a mapping can never report empty. The
rewrite changes messages and nothing else: tree, parents, both identities and both timestamps are
replayed through `git commit-tree`, and the dates are read in git's internal `<timestamp> <tzoffset>`
spelling rather than strict ISO, because strict ISO renders a `+0000` offset as `Z` and the replay
would no longer be byte-for-byte the object it replaces. That is why the runner grew
`GitRunnerOptions.identity`, and it is also why idempotence is structural rather than plan-level: a
no-op rebuild reproduces a commit's exact object id, so a second run is the identity function. The
recoverable order is plan, optional digest pin, the empty-plan short-circuit, the rescue-ref guard,
every name resolved to an exact commit, rescue refs written and read back before the first new
object exists, then every named ref moved in one `git update-ref --stdin` transaction. Because the
table records the *old* ids, the migration has a second half — `carry_ledger_cells` rewrites the
tracked table's memory column onto the total old→new map — and the kernel now declares
`LEDGER_RELATIVE_PATH` itself so a kernel-level reader of that table needs no feature-package import.

**An external review found two defects and both are fixed; the module has not been applied to any real
repository.** The first was the selection: keeping one row per code commit and letting the last
assignment win meant a dictionary's hash order decided a conflict and 16 code commits lost their
mapping, and it left every memory commit the matching did not reach without a trailer. Measured on the
real history at `7aa4cd97`, the fixed selection names **418 of the table's 428** code commits — the
maximum, confirmed independently with Hopcroft-Karp — and carries a trailer on **455 of 455** memory
commits, recovering 52 of the 60 omitted pairings the review counted. Of the remaining 8, five are
provably uncarryable (two equally constrained claims with nothing to fall back on) and three are the
same tie resolved by the table's own order; a variant that scored 55 of 60 selects by hash order and
was deliberately refused. The bound is structural: 472 pairings compete for 455 single-trailer memory
commits and at most 418 matchable code commits. The second defect was on the CLI's own path, where
`request.tip` is a branch NAME: a rescue set verified against a name can never read back equal to a
hash, so the run wrote its rescue refs and then refused, and the retry tripped the existing-ref check
on refs its own predecessor had created. Every name is now resolved to an exact commit before any ref
is written, the same fix covers short names handed to `update-ref --stdin`, and the empty-plan check
now precedes the rescue guard so a retry is a no-op. The acceptance proof was also the defect's
accomplice: it read the table the migration carries forward, and because `read_ledger_source` unions
table rows into trailer rows it proved the table had survived rather than that the trailers alone
preserve the pairings — which is how 60 omissions passed a green suite. It now reads the rewritten tip
through an **absent ledger path**, so the comparison is against Git-parsed trailers alone.

**The earlier confined apply was reverted by developer ruling, and the reason is lineage rather than
correctness.** The pre-fix confined rewrite of this master's own memory line
(`7aa4cd97` → `df863a24`) behaved exactly as scoped: one branch changed plus the leaf's work branch,
every other ref byte-identical, tree sequences, identities, dates and subjects identical, 405 commits
rewritten, and a re-plan over the real repository empty. But rewriting the **shared ancestors**
renumbered them, so
the master's memory line and its super branch shared no common ancestor: the plane's own lineage gate
then refused everything downstream (`closeout-door-source-lineage-stale`, blocking the master's
memory edge at ahead 978 / behind 954), the named recovery route `worktree_sync` could not help
because git refuses to merge unrelated histories and nothing passes
`--allow-unrelated-histories`, and all eleven sibling enclosures would have failed the same way. The
revert moved the two refs back to `7aa4cd97`, restored the leaf's carried table and the merge base,
and deliberately kept `refs/backup/pre-migration` as the audit trail of the reverted attempt. The
consequence is recorded as an obligation rather than a gap: the shared line still carries **0**
`Code-Commit:` trailers, the fixed tool is proven on fixtures plus a read-only plan measurement and has
**not** been applied to any real repository, and the backfill is an explicit step at this master's
integration into IAS, where the shared line's ids change anyway. The worker's re-measurement also
replaced the leaf document's census — 474 tracked rows and 419 distinct code commits at the shared line
are exact, "104 duplicate rows" is 55, "513 trailers" is 419 there and 428 at the master's tip, and
"10 skips" is 67 and 44 under the superseded vocabulary, of which 23 are unreachable memory commits and
two name no object at all.

## 260915-KS-L1 Experimental Knowledge Storage Route
## 260915-CAPS-L14 Route Impact — The Citation Index's Shared Exclusion Register

This package gained one experimental storage route and one kernel primitive; it gained no public surface and no
new authority.
**Route impact recorded rather than a no-impact marker.** The citation surface this package exposes
changed meaning: the source index now consumes a **shared exclusion register** fed by three sources,
and the CLI gained a caller-supplied `--exclude`.

`mcp/src/agents_remember/memory/knowledge/` (six modules) is the concrete APSW-backed SQLite candidate holding
repository, invariant and revision identity. Its route overview is
[`memory/overview.md`](src/agents_remember/memory/overview.md); the shared vocabulary it writes is
`models/knowledge/` (nine modules, governed by the
[models route](src/agents_remember/models/overview.md)), and its only consumer is
`application/knowledge.py`, the composition seam.
- **One register, three sources.** `pathRules.exclude` (`onboarding.pathRules.exclude.paths` in the
  memory layer's `settings.json`), the code repository's `.gitignore`, and optional caller-supplied
  excludes now reduce to one answer and one **record**: the rule set is serialized onto the manifest
  of every published generation, so a reader sees which rules produced the population. Inside a Git
  work tree Git remains the authority and the register records the patterns; outside one a bounded
  matcher applies them.
- **The caller-exclude surface is additive and scoped.** `citation_fix` (MCP) declares
  `exclude: list[str] | None`, and `agents-remember-memory-citations` declares a repeatable
  `--exclude GLOB`. Both narrow **one call's** population on top of the register; a pattern that
  cannot mean anything (empty, absolute, or escaping the code root) is refused by name.
- **Exceeding a cap is reported, never a whole-tree refusal.** Per the developer's 2026-08-20
  ruling: an oversized file is **skipped with a report entry naming it and its size**, the aggregate
  default is 512 MiB applied to the post-exclusion/post-skip set, caps are settings-overridable
  through `onboarding.citationIndex`, and a hard stop remains only past ~2 GiB, reported with
  offenders and a `nextStep`. The manifest schema is now **v10**; a v9 manifest is refused and
  rebuilt rather than read as "no register".
- **The quality surface and the closeout gate both refuse by name.** A capped index is `checked`
  with its skip list; an unbuildable index is a reported `citation-source-index-unavailable` state;
  and the closeout certification's `_admitted_source_index` raises a typed
  `CertificationContractError` instead of letting a bare `ValueError` out of the gate.
- **The register, the caps and the settings key are mode-independent** — nothing on this surface
  branches on the memory storage mode.

`mcp/src/agents_remember/kernel/canonical_json.py` is the package's single canonical JSON encoder for
content-addressed digests: sorted keys, compact separators, literal Unicode, `allow_nan=False`, plus a decoder that
refuses duplicate keys. It sits in `kernel` (rank 1) so both `models` (rank 2) and `memory` (rank 12) may import it
downward.
Full account on the [memory_quality route](src/agents_remember/memory_quality/overview.md); the
governed-artifact rows the leaf adds are on the [tests route](tests/overview.md).

`mcp/pyproject.toml`, `mcp/requirements.txt` and `mcp/uv.lock` gained an exact `apsw==3.53.4.0` pin. APSW is the
repository's first binary-wheel runtime dependency whose capability is a **build-time SQLite option**: the session
and changeset machinery a later merge leaf needs requires `ENABLE_SESSION`, the standard library's `sqlite3`
module exposes neither session nor changeset, and the release is pinned exactly because that capability has to be
proven per platform rather than assumed from the upstream project. The declared Linux wheel (`cp313` manylinux
x86_64) was exercised by the leaf's spike; macOS remains unexecuted and is carried as an unresolved acceptance item
for the owning seat.
## 260915-CAPS-L9 Route Impact — The Experimental Packaging And Cutover Boundary

`layers.toml` gained one charter **wording** paragraph inside `[package.memory]`; no rank, order or sequencing
entry moved. It records the storage home and the import direction: consumers that rank below `memory` — `worktrees`
and `memory_quality` among them — receive `models/knowledge` values or an already-prepared result from
`application`, and never import the storage package.
This leaf packages the capsule experiment and owns the **experimental installation**, and it records
three boundaries this overview must carry because a reader who misses them will over-read it.

Scope this route does **not** claim: L2 family/anchor/relation behaviour, L3's admitted batch contract, L4 snapshot
publication, L5 Git merging, L6 export/import and the read/diff surfaces. This is an experimental increment on the
master's branch pair only, with no IAS landing implied, and legacy Markdown remains operational authority.
**1. The cutover is an INSTALLATION cutover, and the residual is not settled here.** In `capsule` mode
the installer does not write the four coordinator `AGENTS.md` targets and **removes** any copy an
earlier install left, so an opted-in installation injects no legacy startup chain; the disabled run is
its own positive control.

- The exact binary-wheel pin and the in-file reason tying it to the session build option. [168]
- The same pin in the requirements manifest. [169]
- The storage home and the one-way import direction, declared as charter wording only. [170]
- The storage package's own boundary statement. [171]
- The one canonical encoder, its policy and its duplicate-key-refusing decoder. [172]
- The composition seam that is the storage package's only consumer. [173]
- The route overview this section introduces. [174]
**Measured qualification (260915-CAPS-L10, finding `F-6`) — read the sentence above as root-scoped.** The
withholding is complete **inside the coordination root** and it is **not** complete on the machine. The
install does **not** manage the developer harness's own skill root, and in the measured arms **both** arms
read `~/.agents/skills/l-01-agent-lifecycles/SKILL.md`. So the cutover withholds the coordination root's
chain while the harness's copy of the same corpus stays readable — the duplicate-corpus path the cutover's
own docstring says it exists to prevent. Until that surface is decided, **no card and no report may claim
the legacy corpus is off**, and the surviving read is an **E-harness** effect, never a compiler benefit.
The duplicate-corpus claim itself was already forbidden (audit `C6`/`C7`); this paragraph adds the
*measured* reason. Owner: **L9 / the harness-surface owner**, not this leaf.

 The installed coordinator `skills/` tree is still installed, and it is the
**authored copy the coordination root carries** — what a human, the dashboard or a curator reads —
**not** the compiler's input. In production the compiler resolves its corpus from the *packaged* tree
(`application/skill_resources` → `packaged_source_root()/runtime/skills`), so the installed copy is
never injected and never compiled; it is not a second delivery of the corpus. **Do not write that "the
legacy corpus is fully deduplicated."** The traceability audit named **C6** (this leaf's cutover and
L5's adapter boundary both claimed "no duplicate legacy corpus" with no single acceptance point) and
**C7** (L5's fresh session per operation boundary versus this leaf's startup cutover are two routes to
instruction replacement). This leaf's evidence settles the **installation/cutover route** for the four
`AGENTS.md` targets; the session-start hook surface and the adapter-side prompt construction are the
residual, and adjudicating the union is **L11's**, not this leaf's.

**2. The selection is recorded per run, and the no-global-switch proof is root-scoped.** The primary
production input is the registered `runtime_install` tool's own `experiment` parameter; the ambient
`AR_EXPERIMENT` variable is a documented fallback for a short-lived CLI/developer route, and the run
record's `selectionSource` says which one won. A selected run whose capsule path is unavailable is
**refused before its first write** — never quietly `legacy`. The proof that no global switch is left on
is the root-scoped reading: every regular file under the coordination root is searched as bytes and
every hit must be a **byte-identical authored asset** (the corpus legitimately names the experiment),
with a control that the scan found something at all. **Do not write that the experiment is simply
"on".** There is no persistent switch to leave on, and a deselected run restores the unmodified
installation.

**3. Nothing here is a production cutover.** The whole leaf is local and unlanded: no commit, no stage,
no push, no release, no protected branch moved, and no user-level harness configuration written. An eve
seat **launches** with a real effort consumer since L17 landed, but the **dashboard** route still cannot
start the shipped eve row because it does not set `session_backend`, so no card may present a
dashboard-started eve row as a live seat.

**What the route changed.** `install/experiment.py` is new (selection, the three-answer delivery
decision, the blocking probes, the run record, the rollback plan). `install/runtime.py` gains
`RuntimeInstallScope` (whose `selection` is a required **resolved** value), a second entry point
`install_experimental_runtime` over the same private `_install_runtime`, `_capsule_cutover` /
`WITHHELD_STARTUP_TARGETS`, `_install_assets`, and `install_eve_application`.
`RuntimeInstallRequest` gains `experiment`. `scripts/sync-runtime.py` gains a fifth target,
`eve_runtime/` → `package_data/runtime/eve-runtime/`, with a **per-target** ignore set and a
`source_missing` refusal; that packaged mirror is **generated content, never hand-edited**, and the only
currency proof is the generator's read-only `--check`. The installed application lands at
`<coordination_root>/runtime/eve-agent`, reachable through the documented `AR_EVE_RUNTIME_ROOT`
override; the launch path's packaged probe (`runtime/eve-agent` inside the package) is deliberately left
unpopulated in a checkout, because populating it would repoint every checkout launch at a
dependency-less copy. The per-card detail is on the `install` route's cards and the
[tests route](tests/overview.md).

## 260915-KS-L45 The Reviewer Becomes Two Routes, And The Candidate Pair Gets A Producer

**Superseded count (`260921-ICR-L3`): the surface now serves three routes over three ports, and it is no
longer true that no review route accepts a path.** This section records the two-route landing as it was;
its reasons for the split remain current, and the `260921-ICR-L3` section at the end of this narrative
records what the third route added and which sentence of the route model it corrected.

The Intent Reviewer surface is reached through **three GET routes**, and the second one is what makes
the first reachable from a task view:

| Route | Answers | Port | Inputs |
| --- | --- | --- | --- |
| `/api/review/intent` | what one comparison renders | `KnowledgeReviewPort` | task context + one recorded subject selector |
| `/api/review/intent/entries` | which subjects the resolved pair can be compared on | `KnowledgeReviewEntriesPort` | task context alone |
| `/api/review/intent/source-content` | one listed entry's actual content at the two bound code trees (`260921-ICR-L3`) | `ReviewSourceContentPort` | task context + the entry path + both bound code tree ids |

The split is a second **path** rather than a second adapter, and the source comment gives the reason: a
caller that had to guess a subject id to reach the comparison route would be choosing the candidate,
which the browser may not do. Both answer from **one application resolution**, so the entry a task view
is offered and the review it then opens cannot name different candidates. The entry route is the only
one a caller can invoke *before* it knows a subject, so it takes the task context and nothing else.

**No adapter is a named refusal on all three routes, and neither the entry route nor the expansion route may answer it with a list or with an empty file (`260921-ICR-L3` added the third).**
The comparison route's `503` says the surface is not served rather than served empty. The entry route
has its own body (`_UNWIRED_ENTRIES`, `status: "unavailable"`) because an empty entry list would say
"nothing is reviewable here" — a different fact from "this process cannot answer", and only one of them
is true when the process was composed without the port. `_status_for` now reads success as
`refusal is None` (so an `entries` state and a `review` state both serve `200` from one mapping) and
`subject_unresolved` joins the candidate codes answering `404`.

**The candidate pair now has a production producer, and its two halves are named once.** The ingest CLI
derives its candidate directory from the **contract's own recorded worktree group** through the
review's published `REVIEW_CANDIDATE_RELATIVE_ROOT` / `REVIEW_CANDIDATE_DIRECTORY`, so an ingest that
names no directory authors the candidate the review then opens; and when a caller supplies
`--baseline` on a committing run, that fork-point dataset is **copied** into the baseline half (never
moved or linked, because the review's own recorded decision is that both halves live in the leaf's
disposable local root). Nothing is placed on a way out that did not commit, and a run with no
`--baseline` **no longer leaves the half absent**: since leaf `260921-ICR-L5` it *establishes* the
before side as an explicitly identified empty first generation (a schema-valid empty dataset in the
candidate's own namespace, with `baseline-origin.json` beside it recording the generation, the code
base the run observed and that pre-feature history is not recorded), because a pair with one side
missing is refused and the first invariant a repository ever records could not otherwise be displayed
as an addition. Three outcomes now stand where this paragraph used to name one: a named `--baseline` is
copied, and is never written over an identified generation or over a damaged half; no `--baseline`
establishes; and a *selected* baseline that is missing or corrupt is refused by name
(`selected_input_unavailable`, carrying the path and the reason) rather than answered with a freshly
empty dataset. An absent half remains its own truthful answer — `candidate_dataset_absent`, now
**naming which half** is missing — for the case where the establishing run itself left nothing.

**The pair is opened under the namespace recorded beside each dataset, and the receipt-only rule is
corrected here (`260921-ICR-L34`).** The paragraphs below as first written said the namespace is read
from the candidate's sealed **receipt** and that a dataset handed directly with no receipt keeps the
requested identity. That was false for a **before** half placed by a run handed a published
`--baseline`: a published dataset is not an admitted candidate, so no receipt exists beside it — it
carries the before half's own `baseline-generation.json`, written by the ingest's placement owner — and
the read therefore fell back to the requested repository name while the bytes were bound to a namespace
id. The storage owner refuses that mismatch, so **every leaf on the ordinary `knowledge-ingest
--baseline` route produced a leaf whose comparison could not be frozen** (`candidate_dataset_absent`,
*"the candidate database is not bound to repository namespace agents-remember"*), and no test could see
it because the fixtures hand-assemble their pairs. The rule is now **the record beside the bytes**: the
receipt when there is one, otherwise that generation record, and the requested repository only when
**neither** exists. The text below is retained as the L45 record of the reading at that time.

A request names a *repository*; a dataset the write plane placed is bound to a *namespace id* derived
from it, and a side opened under the requested repository spelling refuses against the dataset's own
binding — measured on this leaf's fixture as `bound to 40d350a6-…, not to the requested repository
namespace agents-remember`, which in the live product would have failed the review of every real
candidate. So `review_namespace` reads the namespace from the record standing beside the bytes —
`candidate-receipt.json` when an admission wrote one, otherwise `baseline-generation.json` — and both
sides and the review matrix are opened under that. A dataset with **neither** record beside it (a
fixture, a caller-assembled pair) keeps the requested identity as it always did, and a record that
exists but cannot be read is refused rather than guessed past.

Production wiring lives in the composition root, and it now supplies both ports:
`cli/dashboard.py`'s `serving_collaborators` builds `review_port` and `review_entries_port` — the
application adapter's two halves — and passes them as `knowledge_review` and
`knowledge_review_entries`. Every `create_app` call in that module goes through that function, so a
served dashboard either has both adapters or refuses the corresponding route by name.

- **The comparison route constant, GET-only.** [175]
- **The entry route constant, and the comment recording why it is a second path rather than a second adapter.** [176]
- The typed request the query string parses into, with no path among its inputs. [177]
- **The entry route's unwired answer: a named refusal with the "not served rather than served empty" reason, never an empty list.** [178]
- **The status mapping success reads as `refusal is None`, so one function serves all three typed results; the four candidate codes answer `404` and the expansion's `source_content_unresolved` falls through to `400`.** [179]
- The two port fields on the collaborators dataclass, and the rank reason they exist — with the third review port beside them since `260921-ICR-L3`. [180]
- The registration that passes both ports. [181]
- The composition root's two adapter functions. [182]
- **The two published half-names the ingest CLI derives its candidate directory from — defined in `review_candidate_resolution` and re-exported by the adapter, which is the import path the ingest CLI uses. The three constant ranges were re-derived against this leaf's candidate, whose import block moved them.** [183]
- **The ingest run's review handoff: two filling paths behind one placement gate — the fork-point dataset copied into the before half, or an identified empty first generation established there.** [184]
- **The namespace read from the record beside the bytes rather than from the request — the sibling module's operation, which the adapter delegates to. Corrected in place by `260921-ICR-L34`: the receipt-only rule made the before half of every `knowledge-ingest --baseline` run unopenable, and therefore every such leaf's comparison unfreezable.** [185]
- **The pair preflight: the absent half named as `baseline` or `candidate` — the sibling module's operation, called only when a subject was named, because a task-context review compares no dataset — and the sibling fact beside it, a side that is present but cannot be read.** [186]
- The cold-start branch that fills the half when the caller named no baseline, and the two rules that guard the fork-point copy. [187]

## 260915-KS-L22 The Intent-Review Route, Its Port, And The Wiring Behind It

The L22 section below records the surface as it was first shipped: one route and one port. The section
above supersedes its count; the status idiom, the path-free property and the rank reason it recorded
are still right.

This route gained one read-only HTTP route and the composition seam it is reached through.
`GET /api/review/intent` (`serving/review.py`) is GET-only and accepts **no filesystem path**: the
query string carries `repo`, `master`, `leaf`, `selectorKind` and `selectorId` and nothing else, and
the candidate whose two knowledge datasets are compared is resolved behind the route from that
canonical task context. A browser therefore cannot address a database the resolution did not select —
the same path-free property the change-set routes' own selectors establish, applied here to a review
whose subject is one recorded invariant or family identity.

The route is transport over a port, not a decision. `KnowledgeReviewPort` is a callable from the typed
request to the typed result, and `ServingCollaborators.knowledge_review` carries it into the app
through `register_review_routes`. `serving` ranks below `application` in `layers.toml`, so the serving
module may not import the read, diff and view operations the surface composes; it takes the port the
way the launch route takes the capsule compiler. A process that omits the port refuses the route by
name with `503` — the surface is not served rather than served empty, because an empty pane and an
unreachable adapter are different facts. The other statuses reuse the change-set routes' own idiom:
`404` for a candidate that does not resolve, is not live, or has no dataset; `400` for a selector kind
the surface does not admit; `200` for the typed result serialized once through the model that declares
its shape.

Production wiring lives in the composition root. `cli/dashboard.py`'s `serving_collaborators` builds
`review_port` — the application adapter called with the candidate's own published assessment
collection — and passes it as `knowledge_review`. Every `create_app` call in that module goes through
that function, so a served dashboard either has the adapter or refuses by name; a process that
assembles collaborators some other way and omits the field gets the refusal rather than a silently
empty surface.

- The one route this leaf adds. [188]
- The GET-only registration. [189]
- The typed request the query string parses into, with no path among its inputs. [190]
- The port field on the collaborators dataclass, and the rank reason it exists. [191]
- The registration that reads that port. [192]
- The composition root's two adapter functions. [193]
- **The three review ports passed into the shared collaborators.** [194]
- **The two-shape status idiom the routes inherit, `503` included; the signature now accepts all three typed results.** [195]
- **The two ports passed into the shared collaborators.** [196]
- **The two-shape status idiom both routes inherit, `503` included; the signature now accepts both typed results.** [197]

## 260915-KS-L30 Route Impact — The Curator Ingest Becomes Continuous, And It Publishes

This leaf changed `mcp/src/agents_remember/application/knowledge_curator_ingest.py`,
`mcp/src/agents_remember/application/knowledge_ingest.py` and
`mcp/src/agents_remember/cli/knowledge_ingest.py`, and every change is inside the **curator write
plane** this route publishes: no public tool signature, no response model, no refusal vocabulary and no
read-rail behaviour moved.

Two route-level facts are worth carrying here. First, **repository identity stopped being a function of
the baseline**: the namespace is now read from the repository's own dataset (`_repository_namespace`)
and derived under the ingest namespace only as a cold-start fallback keyed on the repository name, so
one repository keeps one namespace as its baseline advances. An absent candidate now **forks the
selected baseline** rather than starting empty, an entry may name the invariant it revises with
explicit predecessors instead of re-declaring one, and a file may carry more than one anchor. Second,
**the operation publishes**: a run that selects an `IngestPublication` publishes the candidate it just
committed through the shipped publication owner, and the operator reaches it as
`agents-remember knowledge-ingest --commit --publish-to <dataset> [--expected-destination <identity>]`,
so a curated candidate no longer stops at the candidate directory.

What this route does not gain: no second write path (the publication owner stays
`application/knowledge_snapshot.py`), no change to the five published `knowledge_*` tools, and no new
refusal vocabulary — a destination the caller did not admit is refused by the publication operation
with its own code. The per-file detail lives in the sidecars for those three modules.

## 260915-KS-L39 Route Impact — The Curator's Front Door Selects Its Baseline, And Its Identities Move To The Repository

This leaf changed `mcp/src/agents_remember/cli/knowledge_ingest.py` and `mcp/src/agents_remember/application/knowledge_curator_ingest.py` (and the
list-level test module under `mcp/tests/`), and every change is inside the **curator write plane** this
route publishes: no public tool signature, no response model, no refusal vocabulary and no read-rail
behaviour moved. Three route-level facts are worth carrying here, and they are the three points a
follow-up review kept open on the CYCLE-01 finding.

- **The front door can select the dataset it forks from.** `agents-remember knowledge-ingest` now declares
  `--baseline <published dataset>` and hands it to the one `IngestSelection` as a `Path`. Without it a
  task's candidate held only that task's new entry, so the repository's existing invariants were absent
  from it and the next task began blind to knowledge the repository had already published. Omitting the
  flag is still the correct cold start for a repository's first task, which is why the argument and the
  selection field are one pairing rather than an option and a default.
- **A citation's identity belongs to the repository, not to the code baseline.** `_identity` derives a
  citation's route, anchor and claim over the repository's own `repository_id` — read from the selected
  dataset, derived under the ingest namespace only as a cold-start fallback — instead of over the
  enclosure's recorded base commit, and `ingest_curator_list` resolves that value **before** planning, so
  one value reaches every mint in the run rather than one value per step. Two repositories that share a
  base commit therefore no longer collide on one record identity. **L43 narrowed the scope of this
  sentence**: the invariant and its first revision are no longer *derived* at all, and the clause "the
  same obligation is the same record at a later baseline" was true of the citations and, for the
  invariant, rested on the entry's local label being its whole distinction — which is the reading the
  developer's 2026-09-20 ruling replaced.
- **A new truth's identity is ALLOCATED, and the label is not an input to it.** `_creation` hands each new
  creation operation a fresh `uuid4` pair and records it in the candidate's own allocation journal under an
  idempotency key scoped by the enclosure's task identity, so two independent tasks that both numbered an
  entry `R-LOCAL` mint two distinct truths — they used to be handed one invariant and one revision, and
  production sync refused `duplicate_identity` on it and offered only to discard one of two truths that had
  never been in conflict. A repeat of one operation resolves to the identities it already holds and is
  reported `replayed`; different content under one key is refused `allocation_content_conflict`. Continuity
  across a task boundary is by **explicitly naming the stored identity** — an entry names `invariant_id`
  and a target now names `anchor_id` — and **scoping the stored identity to the authoring enclosure is
  forbidden** by the ruling, not merely disfavoured: enclosure identity scopes the retry key and
  distinguishes creation operations only.
- **Two constructs in one file are two stored records, and each citation identity is keyed on what it
  is.** The anchor is keyed on the **allocated revision id** with the locator's qualified name as the
  disambiguator inside that creation, and the claim on its own **revision-plus-anchor edge**, while the
  route stays one scope per path — so `resolve_budget` and `other` in one `pkg/module.py` commit as two
  anchors and two claims sharing the one route row. The route/anchor fix alone was not enough: with the
  claim still keyed on the label, two independent tasks citing one construct minted ONE claim identity for
  two different realizations, and the batch refused the second.

What this route does not gain: no second write path (publication is still
`application/knowledge_snapshot.py`), no change to the five published `knowledge_*` tools, and no new
refusal vocabulary. The per-file detail lives in the sidecars for those modules.

- **The public selection the next task uses to begin from a prior task's published dataset — and, since 260915-KS-L45, the run that also authors the candidate the review opens (on unconverted memory; since `260928-MIK-L12` a converted memory worktree goes to the curator file writer first).** [198]
- **The handoff that places that dataset into the review's baseline half.** [199]
- The operation, and the selection value that carries the baseline into admission. [200]
- The identity derivation, keyed on the repository rather than the base commit, and the three identities one target's own place mints. [201]
- The case that measures the journey through the public operation on a real SQLite store. [202]
- The public selection the next task uses to begin from a prior task's published dataset (the database route; a converted memory worktree goes to the file writer first). [203]
- The allocation a new truth's identity comes from, and the journal a repeat resolves through. [204]
- The retry key, the content guard, and the explicit anchor reuse a producer may name instead of authoring. [205]
- The citation derivation, keyed on the repository rather than the base commit, and the three identities one target's own place mints — each now on its own discriminator. [206]
- The case that measures the journey through the public operation on a real SQLite store, and the case L43 re-pointed at the ruled semantics. [207]

## 260915-KS-L23 The Terminal Leaf: What Changed Under This Route, And The Three Rails It Must Respect

`KS-R23@v1` is the fix-and-certification pass over the accumulated `L10`–`L22` candidate. Every
change below is inside this route, every one is **uncommitted** in the delivered code worktree (code
base `c5a74a85`), and each is carried by its own module sidecar — this section is the route-level
statement of what a reader of `mcp/` should know before opening one.

| Change | Where | The defect it answers |
| --- | --- | --- |
| The memory-quality and citation responses now stamp **which build measured** (`servingBuild`: `commit`, `sourceDigest`, `version`, `dirty`, `packageRoot`) | `application/runtime/startup.py::measuring_build_stamp`, stamped at all three entry points in `application/memory_quality/controller.py`, and in `application/memory_tools.py` | D-33 — the MCP tool surface executes a *fixed* serving build, so a count could not be told apart from one produced by the candidate's own tree |
| `read_steps` returns a payload its own `TaskDocResponse` model accepts | `models/task_doc.py` + the handler in `application/memory_tools.py` | D-9 — `steps: Extra inputs are not permitted` made a documented read operation unusable on every document |
| A next-step hint is **omitted** when its `nextArgs` path fields contradict the response's own address | `application/next_step.py::compute_next_step` (contract-derived) and `application/tool_response.py::bound_next_step` | D-13 — two addressed contracts answered with the same foreign `enclosure_path` |
| `atomic_replace`'s two legs are distinguishable to a caller | `kernel/atomic_write.py` | D-6 — a post-rename durability failure was reported as a replace failure |
| A leaf's own **memory worktree** is an accepted memory shape, and an unsupported root is refused by naming both supported shapes | `kernel/coordination_context/paths.py`, consumed by `memory_quality/integrity/check_missing_onboarding.py` | D-34 — the package-local checker refused the exact root the contract-scoped route measures |
| The cleanup **preview** and the cleanup agree on the same collection | `worktrees/modules/terminal_validation.py` | D-15 — the `driftSnapshot` branch forgot `preview=result.preview` |
| The closeout hint names `curator_coherence action="validate"`, and the bound attestation survives the cleanup that reclaims the enclosure | `worktrees/modules/guidance.py`, `worktrees/integration/closeout/curator_coherence_publication.py` | D-25 — and the measured fact that every published authority's `attestationPath` was already gone |
| The citation checker's reopen rule, the registries' append point, the pre-existing-provenance demotion and the history-bullet stamp frame | `memory_quality/style/citations/*`, `memory_quality/style/finding.py`, `mcp/tests/test-evidence-lanes.toml` | D-21 (decorator widening), D-23, D-24, D-27 |
| The knowledge substrate's own contradictions | `memory/knowledge/{merge,merge_changeset,routes,detection_walk,record_envelope,schema_generations}.py`, `models/knowledge/citation.py`, `models/knowledge/view.py` | the merge's right-side `UPDATE` key, the collapsed detection `signal_id`, three docstrings that disagreed with their own registries, and the broad-form pyright debt |

**Three rails a reader of this route must not lose.** (1) The **integration population is exactly
400 / 400** against `integration_case_budget = 400` (unit `2278 / 2300`), so a new integration case
anywhere makes `pytest_collection_finish` raise `UsageError` and that lane then executes **zero**
tests — which is why all five of this leaf's new case modules are in `unit-regression`. (2) The case
budgets are the **repository-root** `pyproject.toml`'s `[tool.pytest.ini_options]` pair
(`:244-245`); `mcp/pyproject.toml` declares no ini section, and `mcp/tests/conftest.py` now registers
the two ini names with `addini` and **no `default=`**. (3) The evidence catalogue's counts stayed
**15 contracts / 65 artifacts** while its digest moved to `25b00f88…` — a consumer-only change moves
the bytes, never the counts.

## 260915-KS-L47 The Write Path Binds Three Claims To The Truth It Actually Writes

The master-exit review of the knowledge write path confirmed three failures this leaf repaired, and
each one is a claim the route was making that the code did not keep. **All three touch this route's
ingest entry point**, which is why the route overview records them here rather than only on the two
sidecars.

**A changed request under a held retry key is no longer reported as already committed.**
`application/knowledge_curator_ingest.py`'s `_content_digest` now digests the complete normalized
semantic write intent, so it gained `dispositionSource` (the newly reachable field), `namedInvariantId`,
`predecessors` as an ordered list, the **normalized** `RealizationRole` the write path stores rather
than the caller's raw spelling, and `roleRationale`. Two inputs stay out deliberately: `entry_id`, which
is the retry key's own scoping half, and `declares_invariant`, which is derived as `not predecessors` by
construction. Before the repair the digest covered five of the eleven fields the write path consumes, so
changing the realization role, the disposition source, or the invariant with its predecessors returned
exit 0 with `batchState: replayed`, an empty `refused`, `recordsWritten 0`, and a database byte-identical
to before -- the CLI reporting committed while echoing text the stored revision did not carry. The three
measured variants now refuse with `allocation_content_conflict`, name the digest the allocation was
minted for beside the one that arrived, and leave the database untouched; an exact retry still replays
and writes nothing.

**An explicit anchor reuse is now resolved against the stored anchor before any plan exists.**
`_require_stored_anchor` and its `_stored_anchor` read refuse a supplied path, blob or locator that
disagrees with the stored row (`anchor_reuse_mismatch`, and `anchor_id_not_stored` when no dataset holds
the identity), and the check runs inside `_plan_target_inner` ahead of `_target_identities`. The measured
defect was a target naming symbol `other` while supplying the anchor that identifies `resolve_budget`:
the run returned `changed`, committed and published, the receipt echoed locator `other`, and the stored
claim cited the `resolve_budget` anchor. A matching reuse still succeeds, adds no anchor row, and
produces a reference agreeing with the receipt and the public read. The memory layer gained one small
public reader for this -- `memory/knowledge/anchors.py`'s `read_anchor`, with `get_anchor` delegating to
it -- so the intake resolves a stored anchor through one source of truth instead of a second decoding of
the anchor row.

**The review's before half is captured before publication can overwrite its source.**
`cli/knowledge_ingest.py` now reads the admitted baseline at the top of `run` (`_CapturedBaseline` /
`_capture_baseline`) and `_place_review_baseline` writes those captured bytes rather than re-reading
`args.baseline`. When one path is used as both `--baseline` and `--publish-to`, publication replaces that
file in place, so the old post-ingest copy put the published candidate into the review's before half and
the review answered `present` on both sides with no field changes. Measured after the repair: the before
half is byte-identical to the true fork point, the review answers before `absent` / after `present` over
two different digests, and a retry leaves the half unchanged.

The route's own reference tables were re-measured rather than shifted: every citation this leaf's edits
moved was rewritten to the extent its construct actually occupies, the `compatible` declaration this
leaf's change set makes explicit is now stated on the `models/tools/knowledge_responses.py` sidecar with
the wire-omission rule beside it, and `mcp/tests/test_knowledge_views_and_projection.py`'s two reconciled
assertions are stated on that sidecar. **No route-level behaviour outside the knowledge write path
changed**, and the merge guard (`memory/knowledge/merge.py`) was not touched: it is byte-unchanged and
its `_independent_insert_refusal` still refuses two independent insertions of one identity with equal
payloads.

## 260921-ICR-L19 The Package's Ordinary Read Route Gains Its Published-Intent Half, And Its Carriers Move

**This package's route impact is one application module, one response field, and the retrieval carrier this
package ships (ICR-R19@v1).** `application/published_intent.py` is new on the application route: it resolves
the repository's published knowledge dataset from the coordination context, seeds the shipped selective read
with the requested paths or with exact record identities, and returns one bounded page per seed with every
absence named. The MCP surface itself is unchanged — `mcp/tools/read_files.py`'s payload wrapper and the
`read_ar_files` tool registration were not touched, and the tool's advertised contract is the same call it
always was; what changed is that the payload now carries a `published_intent` block beside `files`
(`models/read_files.py`). `application/knowledge_read.py` was reused unchanged.

**The carrier this package ships moved with it, and that is the half a reader of this route has to know
about.** The canonical retrieval skill `skills/c-04-retrieval-strategy-router/SKILL.md` gained a
**Published Intent Before Planning** section (179 → 239 lines), and the repository's own
`scripts/sync-skills.py` regenerated all nine targets from it, including this package's
`package_data/runtime/skills/c-04-retrieval-strategy-router/SKILL.md` — the copy `runtime_install` serves.
The three facts the section states are the ones an agent needs to use the route at all: where the route
reads (`<memory_root>/knowledge.sqlite`, declared by the read side because no shipped owner defaults a
publication destination), the memory-root rule with no fallback, and the exact payload spellings plus the
named absences. One measurement keeps the carrier honest: a case in `mcp/tests/test_read_ar_files.py`
derives the field spellings from a **real page** and rejects the camelCase variants, so the carrier cannot
drift into a second vocabulary. **Six of the seven installed harness skill roots still carry the 179-line
carrier** (`c-04-retrieval-strategy-router/SKILL.md`, 179 lines, sha256
`45174b88161cfc57365ac56c27b143cbf1c23f1f032d4f235403d009aedcc66b`, and **no `c-14`** — measured
absent): `~/.claude/skills`, `~/.codex/skills`, `projects/.claude/skills`, `projects/.codex/skills`,
`projects/.pi/skills` and `projects/.hermes/skills`. **The seventh — `~/.agents/skills`, the root the
delivered server reports as `server_info.harnessSkillRoot` — moved on 2026-09-24** to `c-04` at 241 lines
(sha256 `4a8bf5a83d202ca72685aa68c89d575ff4a1870e127d026c8e48273580c09c88`) and `c-14` at 311 lines
(sha256 `87aaacd18fd072563ba71af10ca40a25506d18a00d2c97f5460377cfa036ed8d`), byte-identical (`cmp`) to
this package's canonical `skills/**`; the `260921-ICR-L25` curator corrected this sentence, which was true
of all seven when it was written and false of one by 2026-09-24. Installing and verifying the remaining
copies is the orchestrator's acceptance step, not a package change, and no test under `mcp/tests` can
assert an installed copy.

- **The new application module on this package's route, and the shipped read it delegates to rather than duplicating.** [208]
- **The response field the block travels on, carried by the strict response model rather than re-declared.** [209]
- **The generated carrier this package ships, regenerated from the authored root skill by the repository's own sync script.** [210]
- **The case that holds the carrier to the payload's real field spellings instead of a second vocabulary.** [211]

## 260921-ICR-L3 The Reviewer Gains An Expansion Route, And Its Inventory Rows Open Into Bound Content

**This route gained one HTTP route, one collaborator port and one application owner, and one sentence
of the reviewer surface's route model became false rather than incomplete.** `GET
/api/review/intent/source-content` opens **one listed entry's actual content** at the two bound code
trees the inventory published. It is the third review route and the third `ServingCollaborators` review
port (`ReviewSourceContentPort`), and it exists as its own **path** rather than a field on the review
payload because the inventory is the whole task's change set: a payload carrying every changed file's
text would be a document dump, so the browser asks for exactly the row a reader opened.

The corrected boundary is the package-level fact this section exists to state. Every earlier statement
that the review surface **accepts no path** is now true only of the comparison and entry routes: the
expansion route takes a **repository-relative entry path** together with both bound code tree ids, and
the application owner behind the port reads it only if a **measured** change set lists it — the requested
generation's own, or, when that measurement cannot be made, the change set the leaf's review publishes —
publishing which measurement admitted it as `path_bound`. No route accepts a filesystem path and no
route accepts a root, so the browser still cannot choose which dataset or which repository is read.

The refusal shape is the same idiom with one new fact: `_UNWIRED_SOURCE_CONTENT` refuses a process that
composed no expansion port with `503` and **"not served rather than served as an empty file"** — an
empty document would read as a file this repository does not hold — and the expansion's refusal code
`source_content_unresolved` reaches `400` through the same fall-through as `comparison_refused`. The
application owner, its vocabulary, its route-local overviews and the dashboard renderer are recorded on
their own routes; this section records only what this package's route model gained.

- **The third review route constant, GET-only, with the comment recording why it is a third path rather than a payload field.** [212]
- **The third collaborator port, with the reason it is a port rather than a field on the review payload.** [213]
- **The expansion route's own unwired answer, which refuses an unwired process rather than serving an empty file.** [214]
- **The application owner the port carries: the admitted paths (a changed path of a measured change set, or unchanged context a recorded realization of the same comparison links — decided by the admission owner), both bound trees read by object id, and the per-side states.** [215]
- The composition root's third review port, and the registration call that passes all three collaborators. [216]
- **The two new owners this route reaches: the application module's own statement of what it answers and does not own, and the vocabulary's own statement of why it is separate from the review payload.** [217]
- The production-composition cases that drive the new route over a real enclosure: an incomplete query refused by the transport, an unwired process refused by name, and an unmeasured generation that still confines the path to a measured change set. [218]


## 260921-ICR-L16 The Review Transport's 400/404 Idiom Collapses To One Mapping, And Its Bodies Gain Actions

The Intent Reviewer's HTTP shim changed in exactly one place, and in two ways that belong together.

**One mapping.** The `try/except AuthorityError/FileNotFoundError` pair that the comparison handler and
`_source_content_response` each carried is now one `_port_outcome(port, request)` that both adapters reach,
building its two bodies through one `_transport_refusal(status, detail, *, next_action,
offending_input=None)`. Each call site is now `result = _port_outcome(port, request)` plus a
`isinstance(result, Response)` return, so the `400`/`404` idiom and the fields on its bodies cannot come to
differ between the two routes.

**Two bodies that published no next action now do.** `bad-path` carries
`_AUTHORITY_NEXT_ACTION` ("name a repository the configured workspace authority admits, then reopen the
review; these routes read no other repository in its place") and `not-found` carries
`_NOT_FOUND_NEXT_ACTION` plus the offending path in both the `path` and `offendingInput` spellings. The
requirement is that every refusal on this route be actionable in the body of its own status, and these two
were the ones that named only their message.

No route, status, key or model was removed, and no other client read those fields, so the change is
additive on this route's own bodies. `serving/review.py` grew 349 → 401 lines and stays under its rail.
`application/knowledge_review.py` — this campaign's global write mutex — is **untouched**: nothing this
packet owns lives there, because no new application behaviour and no new refusal code were introduced.

- **The one mapping both adapters reach, and the one body builder it uses.** [219]
- **The two actions the bodies gained, and the not-found body's offending input.** [220]
- **The result-to-status mapping, unchanged, which the new bodies are used beside.** [221]

## 260921-ICR-L10 Complete Bounded Pagination On The Review Surface

`260921-ICR-L10` (`ICR-R10@v1`) carries the two bounded review collections' **existing**
snapshot-bound cursors through composition, transport and a reachable control, without minting a second
pagination authority. The knowledge comparison's own knowledge-diff cursor and the review matrix's own
view continuation are the only cursors; a new `application/review_pagination.py` owns how a page of
either is stated and how a moved generation is mapped onto the surface's explicit new-generation action;
the review models publish `ReviewCollectionPage` (with the constructor check that refuses a remainder
without a cursor) and a separate `page_refusal`; the serving route admits the page size in its own
vocabulary and names the input each refusal is about; and the dashboard renders the bounds, the scope and
one action that reaches the rest from a captured real server body.

Two facts a reader of the mcp route should carry away. **A page with a remainder cannot exist without its
cursor** — the shape that produced the requirement's own non-conforming example is unrepresentable, not
merely avoided. And **only the owners' binding-mismatch code is a moved generation**; every other refusal
keeps the owner's own remedy and is reported as `comparison_page_unreadable`, so a reader is never told to
open a new comparison when nothing moved. The manifest side is one lane row and three consumer rows.

## 260921-ICR-L26 Three Of This Route's Rows Re-Cited After The Review Adapter Moved

`260921-ICR-L26` (`ICR-R26@v1`, subject and comparison isolation) changed this route only through the
**files it references**: the review adapter's `_knowledge_pane` (`1034 → 1036` lines) and the three
helper declarations the leaf moved out of or into the owners beside it, namely `_claim_records` (now the
evidence owner's `548-572`), `_knowledge_pane` (now `knowledge_review.py:926-978`) and
`evidence_pane`/`signal`/`observation` (now `review_record_rendering.py:213-252`, `456-473`, `431-453`).
Three reference rows on this overview cited those constructs by their pre-change lines, so they were
re-derived from each construct's own extent in the candidate; **no route-level fact changed** — this
overview's account of the MCP surface, its tools and its registration is untouched by the leaf, and the
route's own index was regenerated with the rest of the tree.

## 260921-ICR-L12 Historical Committed-Leaf Review: A Closed Leaf Reopens Its Recorded Comparison

`260921-ICR-L12` (`ICR-R12@v1`) makes a committed or closed leaf reviewable again. The intake
defect was exact: the ordinary committed diff succeeded for a cleaned leaf while Intent Review answered
`candidate_not_live`, because the history route required `contract.code_worktree.exists()`. The leaf
adds one owner — `application/review_committed_leaf.py`, reached only through the resolution's
closed-enclosure branch — which reopens the leaf's **published comparison generation** (R11's durable
record, re-read through R11's own reopen owner) or, for a leaf that never published one, the **recorded
source range** its enclosure contract holds (R01's own `recorded_committed_range`).

**The three facts a reader should carry.** (1) The record is the authority: a reopened comparison is
reproduced **byte for byte** after worktree cleanup, after a process restart and after a later task
lands on the leaf's protected branch, and nothing falls back to the current tip, `HEAD` or today's
knowledge. (2) A state the record itself declares — R05's typed absences — is stated as the absence it
is and is never worded as a channel that is unavailable, while expected content that no longer resolves
is reported unavailable on its own channel with R11's deletion record; `candidate_not_live` survives
only for the one state in which it is true, a leaf that is neither live nor recorded. (3) The request
carries which record it is addressed to (`history`, one admitted spelling), the route refuses every
other spelling in its own 400 vocabulary, and the dashboard offers a closed leaf its Intent review bound
to that record.

**Preservation.** Existing committed and working change-set actions stay usable; historical inspection
creates no worktree and no filesystem entry; retaining, freezing and reopening remain R11's owners, the
source inventory R02's and the record bundle R14's. `ICR-R24@v1` owns the leaf-history navigation,
`ICR-R17@v1` live refresh and `ICR-R25@v1` the assembled browser acceptance. The diff adds exactly one
suppression (a local import's `# noqa: PLC0415 - cycle`) and widens no limit or rail.

## 260921-ICR-L29 The Package Gains A Taskless Bootstrap, And The Ingest Stops Requiring An Enclosure

`260921-ICR-L29` (`ICR-R29@v1`) makes a repository's **first** knowledge writable without a task. Before
it, the package's only knowledge-write admission was a leaf enclosure contract, so
`agents-remember knowledge-ingest` required `--contract` and a repository with no leaf had no entry
point at all; the memory initializer said nothing about where knowledge would live.

**Five application owners and one CLI adapter** carry the delivery: `application/knowledge_write_admission.py`
(the admission value and the enclosure adapter), `application/knowledge_bootstrap_admission.py` (the
taskless admission resolved from the settings document and the ordinary read route),
`application/knowledge_bootstrap.py` (the run), `application/knowledge_bootstrap_staging.py` (the
retained progress record and the bounded cleanup owner), `application/knowledge_dataset_contents.py`
(the four-valued contents read both of the last two use) and `cli/knowledge_bootstrap.py` (the
`knowledge-bootstrap` subcommand with its `--status` and `--discard-staging` modes).

**The existing owners are untouched.** `ingest_curator_list` is still the only writer and is now bound
to a `KnowledgeWriteAdmission` instead of a document; the candidate, namespace, identity allocation,
first generation, batch, snapshot and publication machinery is the shipped code. The package therefore
still has **one** write plane: what changed is how a write is admitted, not how it is performed.

**The memory initializer finally says where knowledge lives.** `memory_init_tool` attaches a `knowledge`
block — the location the ordinary read route selects, and the state a read of it finds now
(`not-recorded`, `recorded`, `unusable`, or `context-not-admitted` with the admission's own refusal and
named next action). It still creates no knowledge: a memory root is a *place*, and the dataset is an
authored result no initializer may invent. What the block removes is the misreading, not the boundary.

**Two CLI adapters, two admissions.** The umbrella `agents-remember` registered **five** subcommands when
this section was written; it registers **six** since `260921-ICR-L34` (see that section at the top of
this document), the sixth being `review-record-comparison`. `knowledge-ingest` remains the leaf's entry
point and `knowledge-bootstrap` is the taskless one. The
ingest report's `contractPath`/`contract_path` became `admissionSource`/`admission_source`, because the
document a run is admitted under is a settings document for a bootstrap and calling it "the contract"
was false about it (no test and no consumer read the old key).

**A retained progress record is a projection, not a store.** The bootstrap writes
`bootstrap-progress.json` into its own staging root, derived on every run from the run's report, the
candidate's allocation journal and a read of the published dataset — never from the plan. `remaining`
(measured absence, or no creation operation at all) and `unmeasured` (a read this run could not complete)
are two fields, and cleanup removes the staging root only when a read establishes that the published
location holds exactly the staged dataset, or that the staged candidate holds no authored revision at
all.

## Normal comparison capture and explicit recovery

The existing review-record-comparison command now records actual owner-produced assessment inputs through the normal resolved-pair freeze. Its paired recovery controls select an exact retained parent and original curator generation. The packaged curation operation documents both paths and remains synchronized from the canonical skill. No new knowledge writer, semantic store or automatic historical repair is introduced.


## 260928-MIK-L96 Host install, start and shared authority

The `mcp` route now carries the host step of `runtime_install`, the start-only host supervision behind a dashboard start, the packaged host and Node contract, the installation-wide host authority and the product's session-environment list; the host modules live in `serving/paseo/` and are reached from install and serving alike.

- The host step of the install. [251]
- The packaged host contract. [252]
