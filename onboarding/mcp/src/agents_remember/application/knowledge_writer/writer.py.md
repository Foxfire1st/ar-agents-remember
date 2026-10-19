# mcp/src/agents_remember/application/knowledge_writer/writer.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**`write_knowledge(WriteRequest) -> WriteReport`: the curator writer's one operation (MIK-R12 rules 2, 4
and 7).** It reads the hand-off document (`handoff.read_handoff`), loads the memory tree
(`MemoryState.load`), captures the code candidate tree C (`CodeSnapshot.capture`), applies the document
(`Authoring.run`), carries every `carried` entry forward at C (`carry_entries`, MIK-R08), checks every row of the owner's history file (`owner_history_problems`), renders each
touched document canonically after model validation (`_render`), rebuilds the layout marker's dependent lookup, then runs the MIK-R22 validator
(`validate_tree`) over the **whole resulting tree**, with the state's base: the memory worktree's `HEAD`, or
its conversion when `HEAD` is unconverted and the candidate is converted (L37, MIK-R24 rule 7). Only then does it write, and only in a committing run.

## Code Commentary

### Logic

- `WriteRequest` carries the two roots, the `Owner`, the hand-off path as `origin.handoff.path` records it,
  the parsed document, the commit word and the `authorization` reference. The file format has no field for
  the authorization, so the report records it. Since MIK-R11 it also carries `decisions`, the task
  owner's `DecisionResolver` for a planned `dropped` row's cited decision, which `write_knowledge` hands to
  `Authoring`; a write without a task owner (a wave, `decisions=None`) refuses such a row. The leaf route
  binds it (`cli/knowledge_write_route.leaf_decisions`). `WriteRequest.memory_base` supplies the
  leaf's paired K_B for the onboarding-card comparison; a persisted worklist flag cannot override
  a known paired base. Without it, a persisted subject's counted flag is used, then own HEAD as fallback.
- **Requirement endpoints.** The optional coordination root resolves endpoints for records touched by the run and compares the stored links with their prior identities. With no root, endpoints are observations only. With the root supplied, newly introduced or changed unresolved links refuse before any knowledge file is published; unchanged inherited unresolved links are still reported, not newly refused. Requirement observations do not become validator-layer task access.
- **Reconsideration rows (MIK-R14 rule 4).** `WriteRequest.worklist` (optional) is the leaf's persisted worklist:
  `_reconsideration_items` keeps its `reconsideration_candidate` items by subject and hands them to `Authoring` as
  `reconsiderations`, so a `still_rejected` row refreshes the links whose trigger fired on its item; without it no
  link is refreshed. `WriteRequest.questions` (optional) is the leaf task document's `openQuestions` port, handed to
  `Authoring` as `questions`; without it a `raise` is refused. After validation passes and **before `_finish`**,
  `_append_raised` submits the queued `raise` questions in one `append_many` batch in a committing run; any refusal refuses the operation with
  a problem at `openQuestions` ("the raise is refused: …"), and no knowledge file is written. A planned run appends
  nothing (the question was already checked by a dry run during authoring). The leaf route passes the persisted
  worklist (`read_leaf_worklist`) and a lazy `LeafQuestions` port (`cli/knowledge_write_route.py`).
- An unconverted memory tree is refused by name (`UNCONVERTED`, placed at `LAYOUT_MARKER_PATH`) before C is
  captured.
- Problems from reading, authoring, the history check and rendering are all collected; any of them refuses
  the operation before validation runs.
- **Carry-forward (MIK-R08 definition 4).** After authoring and before the history check, every operation
  calls `carry.carry_entries(state, snapshot, owner)`: each `realizes` or `proves` entry whose file's blob
  moved at C while its anchored content is identical is re-recorded at C (`blob`, and a line range's lines),
  and this owner's own open history row that still names the old anchor as `after` follows it. The IDs go
  into `WriteReport.carried`. This is the mechanical update the worklist's `carried` class promises, so such
  an entry needs no disposition. The carry runs over the whole tree, not only the leaf's changed paths.
- `_writer_split` uses `writer_reported_rule_ids()` from the registry, not a fixed three-rule list.
  Alongside the original added-route/Coverage/Non-empty rules, the registry includes R53
  existing-record, carried-route-absent, unrealized-family, carried-stale and governs refusals.
  Inside the writer these become reports so the leaf can repair across runs; each converted refusal
  names that reason and the refusing commit/landing route. Validator/commit enforcement is unchanged;
  `merge_reports` has its separate sync/conversion deferral and migration debt has its own carried/new policy.
- `_finish`: without `commit` the state is `planned` and `written`/`removed` list what *would* change; with
  it, `MemoryState.write` writes and the state is `written`.
- `_render` validates a history document with `parse_history_document` and every other document with
  `parse_document`, then renders `canonical_text`; a model refusal is a `Problem` per pydantic error.
- **The dependent lookup (MIK-R124).** After rendering, the writer rebuilds the layout marker's
  `dependent_links`: an index from each target a dependent stands on — `file:<path>` for a file or anchor link,
  `record:<id>` for a record link — to the dependent record files that name it. It covers the stored dependents
  this write did not remove and is written into the marker at `LAYOUT_MARKER_PATH`; the field is absent when
  there are none. The landing reads this index to find the dependents a change can move, instead of opening
  every dependent record body.
- **The base and what makes a tree unwritable (L37).** `_load(request)` loads the state with
  `BaseCode(request.code_root, request.code_base, <coordination root>/runtime/knowledge-worklist-bases)`, so the
  writer, the worklist, the onboarding gate and the validator read one converted base, cached once. It returns a
  problem for an unconverted tree (`UNCONVERTED`, which now says that an unconverted line crosses the boundary
  first once its repository holds converted memory) and for a base that cannot be built (`state.base_problem`).
  `WriteRequest.code_base` is the commit a trailerless unconverted `HEAD` is converted at: the leaf route passes
  the contract's code base B, the gate's and the worklist's fallback, so all three share one cache key.
- **A crossing owner resolves and records, it does not author (L37, MIK-R24 rule 8 step 4).** For an owner of kind
  `crossing`, `_crossing_problems` refuses `entries`, rulings and any record without an `id`
  (`CROSSING_ROWS_ONLY`): the owner may update an existing record its sync left conflicted, which the writer
  resolves at one more than the higher side's revision, and write `history` rows.
- **Persisted worklist facts.** Before candidate capture, a leaf requires a readable persisted worklist whose consumed shapes pass `worklist_shape_problem`; this preflight does not check complete state, `incomplete`, schema, owner or digest. An incomplete-state document with an empty items list is not refused by this shape check alone. Complete gate recomputation is a separate later route; non-leaf owners keep their separate admission. After authoring, worklist checks validate explicit item tokens and applicability before publication. Existing item/source/count projections still feed row authoring and paired-base onboarding comparison; overview source sets cannot be invented from a file subject.

### Conventions

- Report assembly uses `dataclasses.replace` on the frozen `WriteReport` at each stage.

### Invariants And Boundaries

- **Prepublication refusals and recovery (rule 4):** refusals before question/file publication write no question or knowledge file and name the problems and refusing violations. A later `refused` result is not a zero-effect guarantee: already-published questions remain durable, and failed file publication distinguishes verified restoration from incomplete or unverifiable rollback. Report-only findings do not refuse this writer run; they are not permanent
  publication exemptions. A base-present violation still refuses unless the validator's specific
  carried/deferred policy or the registry's inside-writer split applies; direct repair remains available.
- Nothing is written before validation: `MemoryState.write` is reached only from `_finish` with
  `commit=True`.
- **The carry never edits authored fields or another owner's row (architect ruling 5, MIK-R08).** It never
  changes a locator kind, a name or `content`, and it leaves closed history files and other owners' rows
  alone; with this owner's own file closed, the history check then refuses the write ("closed and frozen").
- **Task-plane endpoint admission and validator reporting are distinct.** The writer may refuse a newly changed unresolved requirement link when the coordination root is supplied. This is not an R13 validator violation and does not let commit validation import the task plane. The earlier blanket never-refused sentence described the predecessor, not the current writer.
- **A `raise` publishes one question batch before knowledge files.** Validation runs first; the committing run submits all queued questions through one `append_many` call before `_finish`. A batch refusal prevents knowledge-file publication. The former sequential per-question append/failure account is retired. This is not a cross-store transaction: a successful batch remains durable if later memory-file publication fails; the refused report retains question identities and the same-command recovery instruction. File restoration is verified or explicitly reported incomplete/unverifiable; retry uses the existing question keys rather than duplicating them.
- **Publication failure and question custody.** `_finish` catches publication `OSError`, returns a refused report and distinguishes a verified restored `PublicationError` from incomplete or unverifiable rollback. If questions were already published, the report keeps their identities and the same-command recovery instruction. No refusal report may present planned record actions as committed writes.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The operation and its stages.

- The refusal text for an unconverted memory tree. [1]

- Read, author, check history, render, validate, then finish or refuse. [3]



- A leaf requires the persisted worklist before capture; question publication has its separate task-owner port [4]


- The questions reach the task document after validation and before any file. [5]


- Reconsideration items are projected by subject; committing question append returns published keys and refusals [6]


- The carry-forward call and its report field. [7]
- The carry itself. [8]
- Planned or written. [10]
- Model validation then canonical rendering of every touched document. [11]
- The registry side of the writer-reported rules. [12]
- A validator refusal writes nothing and names every violation. [13]
- Route rules are reports in the writer and refusals at a commit route. [14]


- New or changed unresolved requirement links refuse when the coordination root is supplied; absent-root observations do not [15]




- Endpoints are resolved with stored prior-link identity before the pre-publication refusal check [16]



- The memory tree and its base, or why the writer cannot write it. [17]
- A crossing owner authors no entry, ruling or new record. [18]
- The writer compares an unconverted HEAD through its converted base. [19]
- A master line's crossing records its rows through the writer. [20]


### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.



- Current request inputs include paired memory-base binding and leaf-required worklist admission [2]


- Registry-marked `writer_reports` refusals become reasoned reports inside the writer; the refusing commit/landing route is named. [9]
- The worklist's well-formed items and trace links, plus covered-source and counted-change projections passed with the paired memory base. [21]
- Paired-base/source projection and registry-driven writer reports retain validation, carry and conversion; later refusal preserves actual question effects and distinguishes verified from incomplete file restoration. [22]


## Current writer publication and refusal contract

The current converted writer checks persisted leaf worklist shape and authored item applicability, admits only resolvable newly changed task links when the root is supplied, and refuses a physically stored derived superseded decision. All knowledge-file publication remains after whole-tree validation. Task question publication is a separate durable effect, reported honestly on later refusal; file rollback is verified rather than presumed. These are source observations of the candidate, not self-use of its repaired writer or an executed fault-injection grade.

- Worklist and changed-link admission precede validation and file publication. [23]
- File publication reports actual restoration and already-published question recovery. [24]
- A stored derived superseded field refuses before canonical rendering. [25]
