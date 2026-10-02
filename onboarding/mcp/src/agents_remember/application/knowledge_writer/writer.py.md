# mcp/src/agents_remember/application/knowledge_writer/writer.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**`write_knowledge(WriteRequest) -> WriteReport`: the curator writer's one operation (MIK-R12 rules 2, 4
and 7).** It reads the hand-off document (`handoff.read_handoff`), loads the memory tree
(`MemoryState.load`), captures the code candidate tree C (`CodeSnapshot.capture`), applies the document
(`Authoring.run`), carries every `carried` entry forward at C (`carry_entries`, MIK-R08), checks every row of the owner's history file (`owner_history_problems`), renders each
touched document canonically after model validation (`_render`), then runs the MIK-R22 validator
(`validate_tree`) over the **whole resulting tree**, with the state's base: the memory worktree's `HEAD`, or
its conversion when `HEAD` is unconverted and the candidate is converted (L37, MIK-R24 rule 7). Only then does it write, and only in a committing run.

## Code Commentary

### Logic

- `WriteRequest` carries the two roots, the `Owner`, the hand-off path as `origin.handoff.path` records it,
  the parsed document, the commit word and the `authorization` reference. The file format has no field for
  the authorization, so the report records it. Since MIK-R11 it also carries `decisions`, the task
  owner's `DecisionResolver` for a planned `dropped` row's cited decision, which `write_knowledge` hands to
  `Authoring`; a write without a task owner (a wave, `decisions=None`) refuses such a row. The leaf route
  binds it (`cli/knowledge_write_route.leaf_decisions`).
- **Requirement endpoints (MIK-R13 rule 4).** `WriteRequest.coordination_root` (optional, default `None`) is where
  requirement endpoints' owning tasks live (`<root>/tasks/<repository>/<path>`). `write_knowledge` fills
  `WriteReport.requirements` from `requirement_links.requirement_endpoints(state, authoring.records,
  coordination_root)` for every record the run created, updated or left unchanged. It is filled before the
  problems check, so a refused run reports them too. An endpoint never refuses the run; with no root, every
  endpoint is reported `requirement-task-plane-unavailable`. The leaf route passes the contract's
  coordination root and the bootstrap wave the admitted authority's (`cli/knowledge_write_route.py`,
  `cli/knowledge_bootstrap.py`).
- **Reconsideration rows (MIK-R14 rule 4).** `WriteRequest.worklist` (optional) is the leaf's persisted worklist:
  `_reconsideration_items` keeps its `reconsideration_candidate` items by subject and hands them to `Authoring` as
  `reconsiderations`, so a `still_rejected` row refreshes the links whose trigger fired on its item; without it no
  link is refreshed. `WriteRequest.questions` (optional) is the leaf task document's `openQuestions` port, handed to
  `Authoring` as `questions`; without it a `raise` is refused. After validation passes and **before `_finish`**,
  `_append_raised` appends each queued `raise` question in a committing run; any refusal refuses the operation with
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
- `_writer_split` turns refusals of the rules the registry marks `writer_reports`
  (`writer_reported_rule_ids()`: today `R04.1-route-directory`, `R04.2-coverage`, `R04.2-non-empty`) into
  report-only violations **inside the writer**, so a leaf may place family routes over several runs
  (MIK-R04 rule 6). Every other refusal still refuses. `require_valid_commit` is not touched, so every
  commit route still refuses those rules (the L04 carry-over obligation, met at the L12 sync).
- `_finish`: without `commit` the state is `planned` and `written`/`removed` list what *would* change; with
  it, `MemoryState.write` writes and the state is `written`.
- `_render` validates a history document with `parse_history_document` and every other document with
  `parse_document`, then renders `canonical_text`; a model refusal is a `Problem` per pydantic error.
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
- **The worklist's items for a row's `items` (L37, MIK-R07 rule 1).** `_worklist_items` reads `(kind, subject, id)`
  of every well-formed item of `WriteRequest.worklist` (an ID must be `sha256:` plus 64 hex digits) and hands them
  to `Authoring` as `worklist_items`. Without a worklist no item is filled in.

### Conventions

- Report assembly uses `dataclasses.replace` on the frozen `WriteReport` at each stage.

### Invariants And Boundaries

- **All or nothing (rule 4):** a refused operation writes nothing and names every problem and every
  refusing violation. Report-only findings (family coverage among them) are carried and never refuse.
- A violation already present in the base still refuses a write unless the validator classes it as carried
  and report-only (architect ruling 6); the curator repairs such damage by direct edit first.
- Nothing is written before validation: `MemoryState.write` is reached only from `_finish` with
  `commit=True`.
- **The carry never edits authored fields or another owner's row (architect ruling 5, MIK-R08).** It never
  changes a locator kind, a name or `content`, and it leaves closed history files and other owners' rows
  alone; with this owner's own file closed, the history check then refuses the write ("closed and frozen").
- **An unresolved requirement endpoint is reported, never refused (MIK-R13 rule 4).** Resolution lives here, in the
  writer, not in the validator: `memory_quality` ranks below `memory` in `layers.toml`, and commit routes carry no
  coordination root (ruling 01:45:56 Q5/Q6; review F2 carried to L14 and L29). L14 reports the endpoints of
  `reconsider_on` links in the worklist's `reconsideration.links` summary; the reads remain L29's.
- **A `raise` puts the question in the task document before any knowledge file is written; on failure it writes
  nothing (MIK-R14 Failure And Recovery).** Candidate invariant. Realized by `_append_raised` between the
  validator and `_finish`, and by the dry-run check during authoring; proved by
  `test_raise_sets_the_status_and_appends_the_question_or_is_refused` (no task owner, a check refusal and an append
  refusal each leave the decision bytes unchanged and `written == ()`) and on real data by the worker's scratch
  answer (refused with exit 1 without task-document settings, then written with the question in the scratch task
  document).
- **Recorded limit (rulings 04:37:56 Q7/Q8 and 05:31:11 F7).** The question and the knowledge files are two
  stores: an `OSError` in `MemoryState.write` after the append, or a second `raise` whose append fails, leaves a
  question with no knowledge written. A rerun appends nothing twice (key prefix).

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

- One operation's inputs, including the authorization reference the report records and the task owner's decision resolver. [2]
- Read, author, check history, render, validate, then finish or refuse. [3]

- The worklist and the task document's questions, both optional (MIK-R14). [4]
- The questions reach the task document after validation and before any file. [5]
- The worklist's reconsideration items by subject; the append in a committing run. [6]
- The carry-forward call and its report field. [7]
- The carry itself. [8]
- The `writer_reports` rules become reports inside the writer; commit routes still refuse them. [9]
- Planned or written. [10]
- Model validation then canonical rendering of every touched document. [11]
- The registry side of the writer-reported rules. [12]
- A validator refusal writes nothing and names every violation. [13]
- Route rules are reports in the writer and refusals at a commit route. [14]
- The coordination root requirement endpoints resolve against; never a reason to refuse. [15]
- The report's requirement endpoints, resolved for every record the run touched. [16]

- The memory tree and its base, or why the writer cannot write it. [17]
- A crossing owner authors no entry, ruling or new record. [18]
- The writer compares an unconverted HEAD through its converted base. [19]
- A master line's crossing records its rows through the writer. [20]

- The worklist's well-formed items, for the rows' items. [21]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
