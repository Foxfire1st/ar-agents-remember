# mcp/src/agents_remember/tasks/ — JSON-Primary Task Documents Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/tasks/`                 |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Current Structural Topology Contract

`document_refs.py` indexes real sprint/master/leaf task documents, validates canonical
repository-qualified references, and walks containment without synthesizing role anchors. This
topology supplies structural authorization and dashboard hierarchy; it does not inspect liveness or
select a runtime occupant. Since 260815-DAG-L13 a nature-less standalone master resolves at master
altitude by default (only an explicit `organizational` standalone stays a dead-end), migration
recovery strings name the `author_execution_graph` bootstrap, and the public `commanded_masters`
derives alias-commanded membership for the atomic-sequential default without re-resolving the
sprint from disk.

## Canonical consumed JSON bytes

The one canonical task reader records the exact original JSON bytes it parses through generic read observation. Existing task readers need no opt-in; maintenance scope and declared effects can therefore be compared against request inputs even across an A-to-B-to-A edit. This source observation changes neither JSON-primary authority nor write/rollback/publishability ownership.

## Purpose

`tasks/` owns the **JSON-primary task document**: the persisted `ar-task-document/v1`
record is the source of truth for a task's plan and progress, and `task.md` (or
`<slug>.md` for a sub-task) is a deterministic *render* of it. The JSON is never
produced by parsing markdown back. From L11 until 260731-EFA-L6 the route also owned leaf reopen
semantics; `reopen.py` has since moved to `worktrees/reopen.py`, because reopening rewrites the
leaf's enclosure contract and ranking it as a task operation made `tasks` and `worktrees` mutually
dependent (`layers.toml`). What stays here is `leaf_doc.py` (exact case-insensitive leaf-doc lookup,
the explicit `lifecycleId` restamp worktree start applies across restarts, and — since 260913-LCA-L5 —
the derived master link `seriesContractPath`/`enclosures[]` bound when a leaf document was authored
before its master's series contract existed) and the document
reset itself, which reopen still drives through this route's `store.py`. This is the work-content layer the observer projects as active
task documents, with lifecycle/enclosure bindings attached when available, so the dashboard can show
planned and running work from the same JSON source (slice 3c; closes note-03 gap #8).

## Hot Path Summary

Task JSON remains planning/source truth. The application publisher captures exact source snapshots,
serializes structural publication, commits task truth plus invalidation for semantic/readiness mutations (observational changes do not invalidate), and then
rebuilds each waiting projection from current closeout-door facts. Queue state is derived scheduling
output, so it cannot make an otherwise-valid task mutation unavailable.

The `task_doc` MCP tool authors documents: its application entry point
(`application/task_docs/task_doc_tools.py`) loads or creates the JSON, applies one operation,
and rewrites both the JSON and the rendered markdown through this package. Leaf writes
can also plan a same-root master-row update through `master_sync.py`, so the parent
master `subTasks[]` checklist follows deterministic leaf facts without overwriting
manual `scope` prose. Start at
`document.py` for the schema, `render.py` for the markdown shape (the
`w-02-light-task-workflow` `template.md` is the spec), and `store.py` for the atomic
JSON+md write/read, including batch writes when a leaf and master must be persisted
together.

## Route Model

- `document.py` — the `ar-task-document/v1` Pydantic schema (`TaskDocument` +
  `Step`/`SubStep`/`Decision`/`CodeExample`, plus `SubTaskRef`/`Section` for masters),
  the `DocKind` (`light`|`subTask`|`master`) and imported `DocStatus`/`StepStatus` from `models/task_document.py`,
  the progress helpers (`step_total`/`step_done`/`current_step` for leaves; `series_total`/`series_done`
  for a master's `subTasks` checkboxes — R1), the optional leaf-only `codeExamplesNote`
  (R3) plus the leaf header companions `statusNote`/`headerNotes` (`HeaderNote`) and freeform leaf
  `sections` (R4 — bespoke prose appended after the template), the master-only `orchestrates`
  list (L14 — the orchestration-command relation: a master with a non-empty list IS an
  orchestration task naming the masters it commands; additive, no new kind), and an after-validator
  that keeps the three kinds disjoint (master ⇒ `subTasks` + structured `sections`, no
  `steps`/`codeExamples`/`codeExamplesNote`/`lifecycleId`; light/subTask ⇒ no `subTasks`, no
  `orchestrates`, freeform-only
  `sections` (R4), and no `codeExamplesNote` alongside non-empty `codeExamples`). A persisted/served
  contract, **not** an MCP response model (peer of `observer.projection`). Leaf docs can name their root
  `seriesContractPath` and one or more `enclosures[]` leaf enclosure contracts. Its
  `SprintExecutionNode` equality/hash contract is structural node-to-node only; callers use the
  explicit `.ref` field when they mean the addressed task document. Legacy bare-reference JSON
  lifting/roundtrip is an independent wire contract.
- `document_field_effects.py` — the exhaustive schema-derived effect taxonomy. Every persisted
  root/nested field is classified by structural topology, normative intent, completion readiness,
  progress, evidence, lifecycle, and/or prose audit; missing, stale, and empty memberships refuse.
- `execution_graph_validation.py` — the schema's indexed intrinsic graph algorithm. One endpoint
  index and resolved-edge population feed uniqueness, ownership, DAG, waves, and named cycles while
  recording exact collection work.
- `leaf_binding.py` — the pure canonical composite master-row/leaf identity owner shared by
  lifecycle and semantic-topology consumers. Number, file, ref, directory, id, and stem must agree.
- `task_paths.py` — the on-disk task-root path vocabulary and the predicates over it
  (`SERIES_CONTRACT_FILENAME`, `ARCHIVE_DIR`, `ENCLOSURES_DIR`, `slugify`, `series_contract_path`,
  `leaf_enclosure_dir`, `leaf_enclosure_path`, `is_archived_path`, `is_enclosure_contract`,
  `iter_leaf_enclosure_contracts`). Task-domain rules, single definition, no import from `worktrees`:
  `worktrees/task_resolver.py` re-exports every name so the rules can live below `worktrees` where
  `layers.toml` requires them.
- `semantic_topology.py` — the strict `semantic-topology/v2` candidate identity: exact refs, one
  structural parent row, execution nature, and explicit DAG or atomic-sequential placement only.
- `semantic_topology_graph.py` + `semantic_topology_graph_binding.py` — compare authored/resolved
  graph bytes, refuse over-budget populations before admission, materialize one recursively immutable
  graph generation, and index all candidate placements and incident edges for bounded reuse.
- `render.py` — `render_markdown(doc)`: the only writer of the rendered markdown.
  Section helpers assemble lines from the model (mirroring
  `worktrees.worktree_contract.contract_to_text`); output is deterministic. A step renders a `### {id} — {title}`
  heading + a `- [ ] {outcome or title}` checkbox carrying the distinct `Step.outcome` (R2; a bare step with no
  outcome and no substeps is heading-only). An empty Proposed Code Examples section renders
  `codeExamplesNote` when set (a deferred slice) instead of the default "no code examples are
  needed" placeholder (R3). The header carries an optional `statusNote` suffix + the `headerNotes` lines
  (and, on an orchestration master, an `**Orchestrates:**` line listing the commanded names — L14),
  and a leaf appends its freeform `sections` after References (R4). A `master`
  dispatches to `_render_master`: an ordered `sections` walk where `freeform` bodies
  render verbatim and `subTasks`/`sharedDecisions` render the generated list/table. Execution-graph
  Mermaid declarations and endpoints use one declaration-order ordinal identity map; ref/leaf
  strings remain human labels and never become private ids.
- `execution_graph_titles.py` — owns the title join. Master titles use `ref.key`; leaf titles use
  `(owning TaskDocumentRef, leaf id)`, so equal local row numbers under different masters cannot
  overwrite or borrow from one another.
- `store.py` — `read_task_doc` / `write_task_doc` (atomic JSON source + rendered
  `.md`), `write_task_docs` (batch prepare-all-then-write persistence for coupled
  leaf/master edits), and `doc_stem` (`task` for a light **or master** doc, `<slug>` for a sub-task).
- `master_sync.py` — the leaf-to-master row planner used by `task_doc`: same-root
  master discovery (a leaf naming no master resolves through the public `folder_master_json_path`,
  the one rule the finalizer and reopen also use since MIK-R38), `SubTaskRef` derivation from leaf id/title/rendered filename/status, manual
  `scope` preservation, strict parent-master validation, and the step/substep status collapse that
  maps any active/blocked/done progress to master `inProgress` and all-done progress to `Completed`.

## Current Normative Intent And Evidence Publication

`task_intent.py` derives `task-intent/v1` from the exhaustive field-effect taxonomy. Exact requirement text stays normative; typed approved packet references supplement that text and are checked for task-relative containment and matching packet identity/version. Packet references alone require an explicit v2 cutover. Typed acceptance-obligation questions contribute to the digest; ordinary progress/audit prose does not. The renderer presents both structured forms without converting them back into authority from Markdown.

Route reviews now bind task intent, content digests and declared direct dependencies. Partial content-addressing fields refuse validation, and publication rejects a review with missing task intent. This publication check does not independently recompute every accepted review from source. Mutation classification projects actual before/after field changes into topology, intent, readiness, evidence and operational-audit classes; schema additions cannot silently escape classification.

- Canonical task intent is hashed from the validated normative projection. [1]
- Exact task text remains mandatory alongside supplemental packet references. [2]
- Task-document publication rejects a route review missing intent identity. [3]
- Mutation classification consumes the accepted/candidate field delta. [4]

## Invariants And Boundaries

- **JSON is the source of truth; markdown is generated.** The renderer is the only
  writer of the `.md`; nothing parses the markdown back into a document. A re-render
  fully regenerates the body, so any prose not in the model is dropped. Series *master*
  files (with bespoke sections) are covered too: a master keeps its prose in ordered
  `freeform` `sections` (rendered verbatim) and its machine-readable parts in
  `subTasks` + `decisions`, so the round-trip is lossless. The shipped `task_doc` runtime
  authors the JSON source and regenerates its markdown view; hand-editing the rendered
  markdown is outside the contract and is overwritten by the next write.
- The fold is pure data: the renderer takes an already-validated model; all I/O lives
  in `store.py`, and reads go through `model_validate_json`.
- Step/substep status carries dashboard granularity (4-state); the markdown checkbox
  is binary (`done` → `[x]`), so the richer state lives only in the JSON.
- Lifecycle binding is optional runtime context. A leaf/light document may carry a direct
  `lifecycleId` or matching `enclosures[].enclosurePath`; worktree-backed durable tasks store their
  leaf contract under `enclosures/<leaf-id>/series-contract.md`, while a master/root task may also name
  `seriesContractPath`. The document remains readable before those bindings exist.
- Master-row sync is same-root only. Cross-series `master` refs remain navigation metadata; automatic
  writes never cross into another task folder. Existing master `scope` text is manual and preserved.
- Coupled leaf/master writes prepare every JSON and rendered markdown payload before replacing files,
  and reject duplicate output targets up front; that guard is necessary because a coupled operation
  would otherwise silently let one document target overwrite another.
- Graph node identity, addressed document identity, Mermaid private identity, and human labels are
  separate contracts: structural nodes compare to nodes, callers project `.ref`, Mermaid ids are
  ordinal, and leaf titles are master-qualified.
- **`cleanup: reopened` is no longer written in this route.** Its sole producer, `reopen.py`, moved
  to `worktrees/reopen.py` in 260731-EFA-L6 — see that file's sidecar for the current account. The
  history below is kept because the failure it describes was this route's, and because the reader
  reset it documents still runs through this route's `store.py`. `reopen.py` (now line 94) remains
  the package's only producer of that contract cell; `worktrees/modules/start.py` (line 482) and
  `observer/reducer.py` (line 319) only read it, both pairing it with `abandoned` as
  recreate-fresh. That made this route the sole cause of a wire failure until 260731-EFA-L4:
  `models/worktree.py` hand-wrote `CleanupStatus = Literal["pending", "completed", "abandoned"]`,
  so a context packet for a reopened task raised a pydantic `ValidationError` **inside an MCP
  tool handler that has no `except` for one** — for a value only this file writes. The fix is at
  both ends. The reader now imports the contract's own `CleanupStatus`, which includes
  `reopened`; and the four vocabulary cells `reopen_task` moves (`human_review_status`,
  `closeout_status`, `integration_status`, `cleanup`) go through
  `worktree_contract.ContractCells` + `amend_contract` (now line 71) instead of being
  `dataclasses.replace` keywords, because typeshed declares `replace(obj, /, **changes: Any)` and
  pyright therefore checked none of them. The free-text resets (`code_commit`,
  `memory_content_commit`, `ledger_commit`, `commit_approval_note`, `integration_strategy`, the
  three `integrated_*` commits, `lifecycle_id`, `memory_state`, `approved_for_commit`) stay on
  the inner `replace`, since they have no vocabulary to be checked against. The contract this
  writes is byte-identical to before; what changed is that the writer is now checked against the
  vocabulary the reader publishes.

## Evidence

### Repo-Internal References

- The `task_doc` application entry point authors documents through this package. [5]
- Leaf writes keep same-root master rows synchronized through the dedicated planner. [6]
- The task-document renderer regenerates markdown from the validated `TaskDocument`. [7]
- The persisted worktree contract is the analogous model-to-text precedent. [8]
- The persisted-contract peer this schema mirrors. [9]

## 260718-CHATS-L5I Current Route Impact

Task reopening now clears the completed landing-final artifact as part of restoring live task state and exposes a clearing failure, so a historical completed landing projection does not survive as the current truth for reopened work. Since 260731-EFA-L6 that clearing lives in `worktrees/reopen.py`, not in this route; the document half of the same reset still runs through this route's `store.py`.

Route indexes remain parent-owned for one aggregate refresh after disjoint curation. This overview records the cumulative frozen-source review; index regeneration and aggregate acceptance are separate work.

## 260731-EFA-L9 Route Impact — Vocabulary Moved

The task-document vocabulary (`StepStatus`/`DocStatus`/`CompletionBlocker`) moved to `models/task_document.py` by L9; tasks modules now import it from there. Task-document behavior is unchanged.

## L23 Final Candidate Route Disposition

Task documents are the canonical sprint/master/leaf identity for source lineage, route review, and
durable lifecycle addressing. A cleaned completed leaf is first converted into an exact task-reopen
plan, before deliberately removed descendant branches can be mistaken for lineage failure.

## Current Task-First Task-Fact Publication

Sprint, master, and leaf documents are planning truth, not queue-owned records. Publication rechecks
the accepted source bytes, writes the task batch and invalidates every affected waiting projection
under one short task-publication lock, then rebuilds each projection independently from current
door facts. Claimed/running lifecycle and commit evidence remains outside that disposable queue
projection, so invalidation cannot erase an operation already underway.

## 260815-DAG-L4 L4 Topology Publication Authority

Task-document execution-topology edits are validated under the same repository authority as Git mutation. Candidate graphs cannot promote live leaf work branches into protected supers/atomic refs, detach live owners, or contradict an existing atomic series edge.

## 260815-DAG-L14 Task-Document Route

The `ar-task-document/v1` schema gains `SprintSeat`/`seats` (sprint-only, unique among
non-retired roles) and typed `SubTaskRef.masterRef` rows; the renderer emits real relative
master links, the generated Master Index for sprints, and the `**Seats:**` header block;
`validate_sprint_linkage` hard-fails new-shape drift.

## 260913-LCA-L5 Route Impact — The Derived Master Link, And A Recorded Layer Inversion

`leaf_doc.py` now binds the two derived fields (`seriesContractPath`, `enclosures[]`) that a leaf
document cannot carry when it is authored before its master's series contract exists — the normal
planning order. Both planning paths bind only the ABSENT fields, so an existing binding is never
rewired, and `plan_leaf_doc_enclosure_registration`'s exact no-op now requires the link to be present
(new `master-link-missing` state). `restamp_leaf_doc_lifecycle` gained the same binding in its
docstring's corrected premise, but it remains **uncalled** anywhere in `mcp/src`; the live publisher is
the start/attach path.

Route-level consequence, and the reason this is recorded at route altitude rather than only on the
file card: the **first revision** of this change set imported those two helpers from
`worktrees.task_resolver`, which inverted the declared package order (`tasks` is rank 9, `worktrees`
rank 10, and `layers.toml` declares no baseline and no exception) and produced a `tasks <-> worktrees`
package cycle. The repository's own layering fitness function reported
`tasks -> worktrees (tasks/leaf_doc.py:32)` plus that cycle, and exited 1 — 17 violations and 2 cycles
against 16 and 1 for the same tree with only those import lines deleted. The route's charter —
"Document state only -- an operation that also rewrites an enclosure contract is a worktree operation
and is ranked accordingly" — was not violated by what the module *does* (it writes only the document),
but the dependency pointed the wrong way across the two packages' boundary, and the rail is armed
(`quality_plan.py` inserts a `layering` step).

**Resolved by moving the rules down, not by having `tasks` reach up.** The task-layout path vocabulary
now has its single definition in the new route module `task_paths.py`, and `worktrees/task_resolver.py`
imports and re-exports it so its existing callers are unchanged. `leaf_doc.py` imports from
`tasks.task_paths`, no `tasks -> worktrees` import remains anywhere under `tasks/`, and the same checker
reports 16 violations and 1 cycle (the pre-existing `memory_quality <-> worktrees` cycle) with no
tasks-related finding — the base state, since the rail was already red before this change set on
pre-existing `worktrees -> memory_quality` edges. `layers.toml` is untouched.

## 260815-DAG-L16 Route Impact

`tasks/leaf_doc.py` blank-id refusal now names the missing binding and the recovery (L16-R9:
re-stamp the series contract / use branch-addressed mode for direct execution). The
`record_route_review` binding machinery moved to `application/task_doc_route_review.py` (facade
re-export); the task route's model is unchanged.

## 260815-DAG-L12 Route Impact

The execution graph renders as a deterministic Mermaid `flowchart TD` diagram (L12-R1):
`render.py` emits subgraph-per-master boxes (title-labeled, truncated leaf nodes, atomic lumps,
labeled edges) ordered by derived wave then declaration order, with the machine lists alongside.
DAGQC L1 hardens private identity to collision-free ordinal ids shared by declarations and edge
endpoints; no sanitizer-derived id remains. `execution_graph_titles.py` owns the shared title join
(`SprintGraphTitles`, `build_graph_titles`, `read_graph_titles`), with leaf keys qualified by the
owning `TaskDocumentRef`, and is threaded through `store.py` batch writes and application writers.


## 260815-DAG-L15 Route Impact

New `tasks/serving_preflight.py`: the served-build preflight gate (model self-probe + non-editable wheel floor 3.0.0rc8, fail-closed, L15-R4) wired before every topology-schema write. `document.py` acyclicity refusals now name the exact cycle members (F4); `document_refs.py` hosts the shared atomic node-kind rule with the L15-FIX-1 `KeyError` closure.

## Current Architecture After CLIVE And DAGQC L1

Task writes capture and validate their before-state and publish task truth plus projection
invalidation atomically under the short authority needed for structural/integration races. Waiting
projection rebuild follows independently. DAGQC L1 makes execution-graph identities explicit:
structural node equality/hash, `.ref` for document ownership, ordinal Mermaid ids, and
master-qualified leaf-title keys.

### Reconciled Source Evidence

- Task source snapshots and publication. [10]
- Application publication transaction. [11]
- Structural execution-node equality/hash and explicit reference ownership. [12]
- Qualified leaf-title join. [13]
- Ordinal Mermaid identity allocation and rendering. [14]

## 260821-DAGQC-L2 Total Serving-Preflight Boundary

`serving_preflight.py` now translates each expected distribution discovery, metadata iteration,
read, stat, and version failure at one explicit typed boundary, reads version once, and preserves
the existing topology floor/editable-install policy. Programmer defects are not swallowed by a
broad fallback.

## Repository Census Ownership

Repository-wide master discovery is exposed once as the module-level
`repository_master_documents(topology, repository)` query in `document_refs.py`. Execution
topology, sprint linkage, and topology-internal consumer scans all call that seam. The topology
object no longer carries parallel public/private master-census methods, so branch-authority checks
cannot drift across competing APIs.

## 260831-CCR-L01 Stable Semantic Topology Identity

Closeout topology currentness is now a task-domain semantic projection rather than a queue-private
whole-document digest. The exhaustive field-effect taxonomy makes schema growth explicit;
`semantic-topology/v2` includes only sprint/master/leaf refs, the uniquely bound structural parent
row, effective execution nature, and candidate-applicable placement. One bounded immutable graph
index is shared across the candidate population. The existing task-document schema remains the
canonical persisted authority, and its intrinsic graph validation is now one indexed analysis
reused by admission and wave/cycle reads.

## Master Abandonment: Terminal Status And Resolved Rows

`DocStatus` gained `abandoned` as a second terminal value, and this route owns the judgement that
consumes it. `readiness.py::master_is_terminal` is the single definition: `Completed`, or
`abandoned`. It is deliberately not `status == "Completed" and not completion_blockers(doc)` —
abandonment does *not* resolve a master's rows: on an atomic master whose remaining leaves were
never started those rows stay `planning` on purpose. The shared
`RESOLVED_MASTER_ROW_STATUSES = {"Completed", "abandoned"}` lives beside the vocabulary in
`models/task_document.py`, so the task, worktree and observer planes consume one set instead of each
spelling it out and drifting.

Within this route: `completion_blockers` and `missing_unresolved_master_rows` read that shared set;
`master_sync.py::derived_master_status` projects an abandoned leaf straight to `abandoned` (otherwise
the rollup collapses it back to `inProgress` and a later sync silently reopens it); `render.py`'s
`_MARKER` is a direct lookup covering every status, so a new status without a marker raises at render
time instead of drawing a wrong glyph; `document.py::derived_leaf_placement` chooses a segment by
resolved (terminal) predecessors rather than completed ones; and `__init__.py` re-exports
`master_is_terminal` on the route's public surface.

## 260831-LOCR-L33 Step Notes And Their Render

`Step` gained an optional `note` (`document.py`), the same free prose `SubStep` already carried and
`None`-defaulted for the same `exclude_none` byte-identity reason. **The field is a root-cause fix,
not a convenience**: before it existed the schema had nowhere to put a top-level note, so
`task_doc`'s `set_step` accepted a caller's `note` and silently discarded it whatever the update key
set did. Any future report that a caller's field vanished should first ask whether the field is
declared in this schema at all.

`Step.note` is classified `AUDIT` in `document_field_effects.py` — the taxonomy is exhaustive and
fails closed, so adding a persisted field without a classification refuses before write — and the
renderer (`render.py::_step_lines`) now suffixes a top-level note onto the step's checkbox line
exactly as a substep's, **and** counts `step.note` among the reasons to draw that line: a step
carrying only a note would otherwise render as a bare heading and lose the note a second time.
Persisting a field the renderer cannot show still leaves it invisible.

## 260928-MIK-L08 The `knowledgeMaintenanceScope` Field

`document.py`'s `TaskDocument` gained the optional boolean `knowledgeMaintenanceScope` (MIK-R08 definition
5): a leaf that sets it has its worklist classify every entry of its memory base.
`document_field_effects.py` classifies it `LIFECYCLE`, not `NORMATIVE` (**architect ruling 4**), so it
stays outside the intent digest and a change to it is an `operational-audit` mutation; `render.py` draws
a `**Knowledge maintenance scope:**` header line when it is true. Every existing document loads unchanged.

- The field. [15]
- Its classification. [16]
- Its header line. [17]

## 260928-MIK-L11 The `expectedKnowledgeEffects` Declaration And The Task Owner's Answers

MIK-R11 lets a leaf's task document declare, before implementation, the invariant and family effects it
expects; the worklist then marks every invariant and family item `planned` or `unplanned` and raises a
`planned_untouched` item for each declaration no history row delivers. The task plane's part:

- [`document.py`](document.py.md): `TaskDocument.expectedKnowledgeEffects: list[ExpectedKnowledgeEffect] |
  None` (`subject`, `effect`, `requirementRef`). The model refuses a malformed entry, the field on a master,
  an empty list, and two declarations with the same subject and effect. The task plane checks shape only and
  never reads knowledge; the patterns come from `models/knowledge_files/planned.py`.
- [`document_field_effects.py`](document_field_effects.py.md) classifies the field and its three nested
  fields `NORMATIVE` (the packet's `NORMATIVE_INTENT`), unlike L08's `LIFECYCLE` flag, and
  [`task_intent.py`](task_intent.py.md) carries it as an optional `task-intent/v1` slot whose key is dropped
  when absent (and from a master's projection). **An absent field leaves every existing task-intent digest
  unchanged**: the worker (597 documents) and the reviewer (889 documents) found every real digest, render
  and stored JSON byte-identical. A declaration changes the leaf's intent digest; clearing it restores it.
- [`render.py`](render.py.md) draws an `**Expected knowledge effects:**` header block when declared.
- [`leaf_decisions.py`](leaf_decisions.py.md) (new) is the task owner's answer for MIK-R11, through one strict
  leaf lookup (`strict_leaf_doc`: `resolve_terminal_leaf_doc` plus a refusal of any unreadable document that
  still names the leaf). The worklist reads the declaration through it, so **an unreadable leaf document
  never reads as "nothing declared"** — it makes the run `incomplete` (ruling F2); and
  `leaf_decision_refusal` answers whether a planned `dropped` row's cited decision (`at`) resolves to exactly
  one decision entry — ambiguity refuses (ruling F1, 2026-09-29T22:35:34+02:00).
- **Transition (ruling Q2, 2026-09-29T21:56:18+02:00).** The installed runtime's `TaskDocument` forbids
  unknown fields, so no real task document may declare `expectedKnowledgeEffects` before the L37 install.
  Who writes the field is procedural (`task_doc` has no per-field role gate); the reviewer checks the
  declaration against the packet (ruling Q3). `leaf_maintenance_scope` keeps the fail-soft `find_leaf_doc`,
  carried to L09 (ruling F2).

- The declaration model and its refusals. [18]
- The field on the task document. [19]
- Its normative classification. [20]
- The optional intent slot, absent when undeclared. [21]
- The header block. [22]
- The strict lookup and the decision answer. [23]

## 260928-MIK-L38 The Master Sync's Fallback Becomes The One Rule, And A Placement Guard

Developer direction D32 (MIK-R38): a completed leaf must show `Completed` on the master that lists it. Two tools had
resolved a leaf's master differently: this route's master sync fell back to the folder's `task.json` for a leaf
naming no master, while the finalizer (`worktrees/modules/finalize.py`) called that leaf standalone, so the master
row the sync kept current stayed `inProgress` after the leaf landed (260928-MIK: 15 rows, repaired by resync
writes). This route now owns the rule and one guard, both used by the worktree layer above it:

- [`master_sync.py`](master_sync.py.md): the public `folder_master_json_path(task_root, leaf)` is the whole rule
  for a leaf naming no master: `None` for a named master or a non-`subTask` (a `light` or master document *is* the
  folder's `task.json`), else the folder's `task.json` when it exists. `_master_json_path` calls it and returns the
  same unresolved path as before, so the sync's behaviour and `masterDocPath` are unchanged. The finalizer and
  reopen (`worktrees/reopen.py`, ruling 2026-09-30T12:33:07 Q2) call it too.
- [`leaf_doc.py`](leaf_doc.py.md): `require_task_document_in_place(json_path, doc, refusal)` raises the caller's
  refusal when the store's write target for a document (`json_path_for`, by kind and slug) differs from the path it
  was read from. Finalize and reopen call it on the leaf and on the master before any write, so a hand-made `light`
  leaf or master under another name can never be written over the series `task.json` (review R1 finding 1, rulings
  13:11:32 and 13:35:32). Review R2's read-only sweep of the real task folders (557 sub-tasks, 39 masters) refused
  none.

No task-document format, render or sync behaviour changed, and no document was migrated (the packet's Exclusions).

- The one rule for a leaf naming no master, and the sync's own call. [24]
- The placement guard. [25]
