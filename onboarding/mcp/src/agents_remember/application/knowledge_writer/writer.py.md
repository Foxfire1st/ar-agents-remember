# mcp/src/agents_remember/application/knowledge_writer/writer.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**`write_knowledge(WriteRequest) -> WriteReport`: the curator writer's one operation.** It reads the hand-off document (`handoff.read_handoff`), loads the memory tree
(`MemoryState.load`), captures the code candidate tree C (`CodeSnapshot.capture`), applies the document
(`Authoring.run`), carries every `carried` entry forward at C (`carry_entries`), checks every row of the owner's history file (`owner_history_problems`), renders each
touched document canonically and validates its model (`_render`), rebuilds the layout marker's dependent lookup, then runs the knowledge validator
(`validate_tree`) over the **whole resulting tree**, with the state's validation bases: the memory worktree's `HEAD`, or
its conversion when `HEAD` is unconverted and the candidate is converted, and during a merge the incoming parent `MERGE_HEAD` converted the same way. Only then does it write, and only in a committing run.

A committing leaf forwards its admitted owner to file publication. When records or onboarding changed, publication includes a required briefs ignore line with the memory changes. The mounted route uses the resulting changed paths to refresh the affected source briefs.

`WriteRequest` adds optional `repo_name`, and `write_knowledge` resolves `_base_code_blobs(request, snapshot)` at `request.code_base` and passes `repo_name` and `base_code_blobs` into `Authoring` for dependent document-edit checks and task-fact validation.

## Code Commentary

### Logic

- **Onboarding source selection.** An existing `onboarding_trace` item owns its subject's source list. Its subject excludes unexplained-group selection even when the trace metadata is unusable. Without a trace item, uncovered `unexplained_hunk` and `unexplained_file` items contribute the member-path keys of `sourceBlobs` for their matching trace subject. The selector unions and sorts those paths; the existing snapshot authoring owner supplies their actual candidate blobs or `absent`. Covered items, unrelated kinds and malformed maps contribute nothing. Without either item, the existing single-file fallback remains; an overview cannot invent a source set.

- `WriteRequest` carries the two roots, the `Owner`, the hand-off path as `origin.handoff.path` records it,
  the parsed document, the commit word and the `authorization` reference. The file format has no field for
  the authorization, so the report records it. It also carries `decisions`, the task
  owner's `DecisionResolver` for a planned `dropped` row's cited decision, which `write_knowledge` hands to
  `Authoring`; a write without a task owner (a wave, `decisions=None`) refuses such a row. The leaf route
  binds it (`application/knowledge_write_route.leaf_decisions`). `WriteRequest.memory_base` supplies the
  leaf’s recorded memory base for the onboarding-card comparison in the candidate’s format. A readable recorded base controls even when the persisted count disagrees. If that comparison is unavailable, the writer uses the persisted count for the subject when present and otherwise compares against the operation base.
- **Caller provenance.** The route resolves the caller stamp from the launch binding and receipt and supplies it in `WriteRequest.stamp`. The writer gives it to in-memory authoring, which uses an unknown stamp with a reason when the route has none. The hand-off supplies the record’s meaning.
- **Requirement endpoints.** The optional coordination root resolves endpoints for records touched by the run and compares the stored links with their prior identities. With no root, endpoints are observations only. With the root supplied, newly introduced or changed unresolved links refuse before any knowledge file is published; unchanged inherited unresolved links are still reported, not newly refused. Requirement observations do not become validator-layer task access.
- **Reconsideration rows.** `WriteRequest.worklist` (optional) is the leaf's persisted worklist:
  `_reconsideration_items` keeps its `reconsideration_candidate` items by subject and hands them to `Authoring` as
  `reconsiderations`, so a `still_rejected` row refreshes the links whose trigger fired on its item; without it no
  link is refreshed. `WriteRequest.questions` (optional) is the leaf task document's `openQuestions` port, handed to
  `Authoring` as `questions`; without it a `raise` is refused. After validation passes and **before `_finish`**,
  `_append_raised` submits the queued `raise` questions in one `append_many` batch in a committing run; any refusal refuses the operation with
  a problem at `openQuestions` ("the raise is refused: …"), and no knowledge file is written. A planned run appends
  nothing (the question was already checked by a dry run during authoring). The leaf route passes the persisted
  worklist (`read_leaf_worklist`) and a lazy `LeafQuestions` port (`application/knowledge_write_route.py`).
- An unconverted memory tree is refused by name (`UNCONVERTED`, placed at `LAYOUT_MARKER_PATH`) before C is
  captured.
- Problems from reading, authoring, the history check and rendering are all collected; any of them refuses
  the operation before validation runs.
- **Carry-forward.** After authoring and before the history check, every operation
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
- `_render` computes canonical text, validates history documents with `parse_history_document` and other
  documents with `parse_document`, then retains the validated bytes for publication; model validation
  errors become individual `Problem` entries.
- **The dependent lookup.** After rendering, the writer rebuilds the layout marker's
  `dependent_links`: an index from each target a dependent stands on — `file:<path>` for a file or anchor link,
  `record:<id>` for a record link — to the dependent record files that name it. It covers the stored dependents
  this write did not remove and is written into the marker at `LAYOUT_MARKER_PATH`; the field is absent when
  there are none. The landing reads this index to find the dependents a change can move, instead of opening
  every dependent record body.
- **The base and what makes a tree unwritable.** The writer loads the memory worktree’s `HEAD` as
  its operation base and also uses `MERGE_HEAD` for validation during a merge. It converts an
  unconverted operation base for a converted candidate. `_load` returns `UNCONVERTED` for an
  unconverted candidate and a `base` problem if it cannot read or build either required operation base.
  The counted-card comparison separately uses the recorded leaf memory base when readable.
  Conversion uses the base’s paired code commit when available. Otherwise it uses `WriteRequest.code_base`
  when supplied, or the code worktree’s `HEAD`. The leaf route supplies the recorded leaf code base when
  set. The writer, worklist and gate can reuse a cached conversion when the memory commit, format
  version and resolved code commit match.
- **A crossing owner resolves and records, it does not author.** For an owner of kind
  `crossing`, `_crossing_problems` refuses `entries`, rulings and any record without an `id`
  (`CROSSING_ROWS_ONLY`): the owner may update an existing record its sync left conflicted, which the writer
  resolves at one more than the higher side's revision, and write `history` rows.
- **Persisted worklist facts.** Before candidate capture, a leaf requires a readable persisted worklist whose consumed shapes pass `worklist_shape_problem`; this preflight does not check complete state, `incomplete`, schema, owner or digest. An incomplete-state document with an empty items list is not refused by this shape check alone. Complete gate recomputation is a separate later route; non-leaf owners keep their separate admission. After authoring, worklist checks validate explicit item tokens and applicability before publication. Existing item/source/count projections still feed row authoring and paired-base onboarding comparison; overview source sets cannot be invented from a file subject.

### Conventions

- Report assembly uses `dataclasses.replace` on the frozen `WriteReport` at each stage.

### Invariants And Boundaries

- **Prepublication refusals and recovery:** refusals before question/file publication write no question or knowledge file and name the problems and refusing violations. A later `refused` result is not a zero-effect guarantee: already-published questions remain durable, and failed file publication distinguishes verified restoration from incomplete or unverifiable rollback. Report-only findings do not refuse this writer run; they are not permanent
  publication exemptions. A base-present violation still refuses unless the validator's specific
  carried/deferred policy or the registry's inside-writer split applies; direct repair remains available.
- Nothing is written before validation: `MemoryState.write` is reached only from `_finish` with
  `commit=True`.
- **The carry never edits authored fields or another owner's row.** It never
  changes a locator kind, a name or `content`, and it leaves closed history files and other owners' rows
  alone; with this owner's own file closed, the history check then refuses the write ("closed and frozen").
- **Task-plane endpoint admission and validator reporting are distinct.** The writer may refuse a newly changed unresolved requirement link when the coordination root is supplied. This is not an R13 validator violation and does not let commit validation import the task plane.
- **A `raise` publishes one question batch before knowledge files.** Validation runs first; the committing run submits all queued questions through one `append_many` call before `_finish`. A batch refusal prevents knowledge-file publication. This is not a cross-store transaction: a successful batch remains durable if later memory-file publication fails; the refused report retains question identities and the same-command recovery instruction. File restoration is verified or explicitly reported incomplete/unverifiable; retry uses the existing question keys rather than duplicating them.
- **Publication failure and question custody.** `_finish` catches publication `OSError`, returns a refused report and distinguishes a verified restored `PublicationError` from incomplete or unverifiable rollback. If questions were already published, the report keeps their identities and the same-command recovery instruction. No refusal report may present planned record actions as committed writes.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the category-authoring requirement with its architect rulings in the task records,
and the coordination-root note on the text-canonical knowledge layout; they live outside the code and memory
repositories, so they are not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The operation and its stages.








- Existing trace subjects retain source-set priority, including exclusion of malformed trace metadata from group selection. [26]
- Uncovered unexplained items contribute a sorted union of matching member paths; supplied blob values are not adopted. [27]


- The refusal text for an unconverted memory tree. [1]





- After validation, a committing run submits raised questions before knowledge-file publication. A refused append prevents file publication. [28]


- Committing question append returns published keys and refusals [6]


- The carry-forward call and its report field. [29]
- The carry itself. [8]


- Planned or written. [30]


- Canonical text is model-validated before its bytes enter the publication set. [31]
- The registry side of the writer-reported rules. [12]
- A duplicate-ID validator refusal reports its violation, exposes no written actions and preserves the memory tree. [32]
- Route rules are reports in the writer and refusals at a commit route. [14]


- With a coordination root, newly changed unresolved links refuse before validation and publication. Without that root, the unresolved endpoint is an observation. [15]

- The writer captures prior link identity before authoring and checks endpoints after authoring. [16]


- The memory tree and its base, or why the writer cannot write it. [17]

- A crossing owner authors no entry, ruling or new record. [18]

- The writer compares an unconverted HEAD through its converted base. [19]
- A master line's crossing records its rows through the writer. [33]
### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.


- The request carries the persisted leaf worklist and recorded card-comparison base. [2]


- Registry-marked `writer_reports` refusals become reasoned reports inside the writer; the refusing commit/landing route is named. [34]


- The writer builds trace links, source sets and counted flags from admitted worklist items. It uses the counted flag for the subject when the recorded card comparison base is unavailable. [35]




## Current writer publication and refusal contract

The current converted writer checks persisted leaf worklist shape and authored item applicability, admits only resolvable newly changed task links when the root is supplied, and refuses a physically stored derived superseded decision. All knowledge-file publication remains after whole-tree validation. Task question publication is a separate durable effect, reported honestly on later refusal; file rollback is verified rather than presumed. These are source observations of the candidate, not self-use of its repaired writer or an executed fault-injection grade.


- Worklist and changed-link admission precede validation and file publication. [37]




- File publication reports actual restoration and already-published question recovery. [24]


- A stored derived superseded field refuses before canonical rendering. [25]

- Current request inputs include paired memory-base binding and leaf-required worklist admission [2]






- New or changed unresolved requirement links refuse when the coordination root is supplied; absent-root observations do not [15]



- Endpoints are resolved with stored prior-link identity before the pre-publication refusal check [16]



- After validation, committing runs publish raised questions before knowledge files. [28]






- Worklist and changed-link admission precede validation and file publication. [37]

- The committing writer supplies the admitted owner to file publication. A leaf mutation that changes a record or onboarding bytes participates in the tracked brief ignore preparation. [47]

- The operation reads and authors, carries entries, checks history, renders, validates the entire candidate and finishes or refuses. [3]
- A leaf requires the persisted worklist before capture; question publication has its separate task-owner port [4]
- The writer gives recorded card-comparison inputs to authoring and validates the produced tree against the operation’s bases. The report registry governs writer findings. A file publication refusal preserves question receipts and distinguishes verified restoration from incomplete or unverifiable rollback. [36]
- The request carries a resolved caller stamp in addition to the hand-off and contract inputs. [44]
- The writer passes the resolved stamp to virtual authoring before validation and file publication. [45]
- The authoring operation assigns an unknown stamp with a reason when no caller was resolved. [46]
