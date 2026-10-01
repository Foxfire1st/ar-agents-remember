# mcp/src/agents_remember/application/task_docs

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/application/task_docs` |

## Governing Overview

[application overview](../overview.md)

## Purpose

The task-document authoring package (260815-DAG master full-gate repair): the operation-dispatched
`task_doc_tool` application entry point and its sibling modules — `task_ref` (the typed task
reference), `task_reopen` (leaf reopen), `task_doc_route_review` (candidate-bound route-review
authority), `task_doc_publication` (task-first exact publication plus projection refresh),
`task_doc_graph_titles` (zero-or-one graph-bearing batch authority),
`task_doc_section_scaffolding` (atomic raw-section shape boundary),
`task_execution_topology` (graph authoring/edits), `task_doc_steps` (the step plane: one exact
addressing rule plus `set_step`/`add_step`/`remove_step`/`skip_step` and the `read_steps`
projection), and `task_sprint_linkage`
(sprint↔master attach/detach/linkage facts). The modules moved here from `application/` (flat) so
the task-document authoring seam owns one package; `task_doc_steps` was added later
(260831-LOCR-L33) when keeping the step plane inline took `task_doc_tools.py` to 1,243 lines against
the armed 1,200-line hard limit.

## Hot Path Summary

`task_unstarted_evidence.py` determines commit evidence from actual code/memory-content and integrated output cells. Retired ledger commit cells no longer count as commit evidence; an existing enclosure remains independent started evidence, and task/lifecycle checks still apply.

## Detailed Route Context

Task-document authoring is the source-of-truth publication plane. An otherwise-valid mutation is
never subordinate to queue or per-contract atomic-series activation state. The exact transaction rechecks accepted source bytes, writes task
truth and invalidates every affected waiting projection under the task-publication lock, then
rebuilds each disposable projection independently from current closeout-door facts. The closed field-effect classifier excludes observation-only updates from invalidation;
semantic/planning changes invalidate their old/new affected sprint union. A planning
change therefore yields a clear invalidation/rebuild signal without freezing unrelated task-doc
authoring, changing activation state, or claiming lifecycle evidence for an operation already
underway. Per-contract activation and retained sync state are downstream worktree authorities that
re-evaluate
the changed plan at their next admission boundary.

`task_doc` MCP calls dispatch through `task_doc_tool` to one operation (create/replace/edits/special
ops); the special ops (sprint linkage + execution graph authoring) publish inside their own
functions and return raw operation payloads merged with the standard identity via
`_sprint_doc_identity`. Route review, topology enforcement, and master-row completion
checks run before any publication; exact route-review admission receives the selected
`ResolvedTaskDocument` and binds its semantic task-intent identity. Dry-run publication
also resolves the affected scope union through the same validation owner; everything validates against the strict `TaskDocResponse` wire
shape (the special-op fields declared in `models/task_doc.py`).

Graph-bearing writers share `task_doc_graph_titles`: pure batch cardinality is checked early and a
batch with more than one graph-bearing document refuses, while on-disk title reads remain inside the
locked publisher callback. Create/replace share `task_doc_section_scaffolding`: raw `sections` must
be a list of mappings before any missing canonical register scaffolds are appended.

Since 260913-LCA-L5 create/replace also share one fail-closed authoring guard:
`_require_bindable_leaf_authoring` refuses a leaf whose derived master link nothing would ever bind
(no series contract and no master document in the task root), while the ordinary planning order —
master first, then its leaves, before any start — remains allowed by the explicit guarantee that the
first start binds the fields.

## Conventions

- The package uses relative imports between its own modules (`from . import task_sprint_linkage`).
- The strict task-document writer authorities in `code_quality/single_owner.py` name these files.
- Shared contracts are explicit owners, not copied private helpers: graph cardinality/title context
  lives in `task_doc_graph_titles.py`, raw-section scaffolding in
  `task_doc_section_scaffolding.py`, and publication ordering in `task_doc_publication.py`.
- The step plane is one such contract owner: `task_doc_tools.py` registers the step operations and
  keeps thin `_apply_*` adapters, while `task_doc_steps.py` owns the addressing rule and the four
  operations. A second addressing rule must not appear in the dispatcher.

## Invariants And Boundaries

- Only these modules may author/render task documents; the application layer is the only writer.
- Since 260913-LCA-L5 authoring fails closed on a derived field it cannot bind: `_build_doc` refuses a
  leaf document authored under a task root with **no master document**, naming `seriesContractPath`, the
  missing `task.json` and the remedy. The planning case — a master document exists but the series
  contract is not bootstrapped yet — stays allowed, and only because the leaf's first
  `worktree_start`/`worktree_attach` is guaranteed to bind both derived fields; the guarantee is stated
  in the helper rather than left implicit. A leaf is therefore never authored under any task root: that
  earlier claim is now false.
- Task truth owns authoring; the waiting queue is a disposable scheduling projection and cannot
  freeze `task_doc` operations.
- Queue invalidation cannot erase claimed/running/commit lifecycle evidence; that durable evidence
  belongs outside the projection plane.
- Publication admits at most one graph-bearing document. Preview and apply use the same owner; no
  first-graph selector, catch-and-split retry, or silent title fallback is introduced.
- Raw section scaffolding validates the entire container/member shape before mutation and preserves
  typed errors; it does not coerce malformed input.
- Nothing here touches memory repos or the coordination ledger directly.

## Current Architecture After CLIVE And DAGQC L1

Task publication validates the complete accepted source set and current integration authority, then
writes task truth plus projection invalidation atomically or reports the exact conflict. Rebuild is
independent and derived from current task/door facts. DAGQC L1 centralizes graph-bearing batch
cardinality/title context and raw-section pre-model validation so all authoring routes share one
contract per concern.

### Reconciled Source Evidence

- Task-first transactional publication and independent projection refresh. [1]
- Zero-or-one graph-bearing publication batch and in-memory title context. [2]
- Atomic raw-section shape validation and missing-register scaffolding. [3]
- The extracted step plane owns one exact addressing rule and the four step operations. [4]

## 260824-PDLS Final Task-Recovery Boundary

Unstarted-task evidence and recovery routes now expose typed task facts without deriving authority
from queue state. Task mutations remain legal; affected closeout projections are invalidated and
rebuilt from current task truth instead of freezing authoring or carrying stale rows forward.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.


## Commanded-Master Completion Reads Terminal State

`task_execution_topology.py::require_commanded_masters_completed` no longer tests
`status != "Completed" or completion_blockers(...)`; it asks
`tasks/readiness.py::master_is_terminal` instead. That is the same judgement the task and worktree
planes consume, so a commanded master is incomplete only when it is neither `Completed` nor
`abandoned`. The route's refusal behavior is unchanged — it still names every incomplete master — but
abandonment now counts as a terminal decision here as it does everywhere else, from one definition
rather than a locally spelled-out set.

## 260831-LOCR-L33 Step Plane Extraction

The step plane left `task_doc_tools.py` for the new sibling `task_doc_steps.py` so the dispatcher
stayed under the armed 1,200-line hard limit (it had reached 1,243). The extraction is a size
decision with a semantic payoff: the operations are now split by intent — `set_step` updates exactly
one existing unit and never creates, `add_step` creates exactly one, `remove_step` deletes exactly
one with a mandatory reason, and `skip_step` keeps and resolves one — all sharing a single addressing
rule where `parent` selects the namespace and zero or multiple matches refuse. `read_steps` is the
read-only focused checklist read. Two developer rulings are in force: a reasoned `remove_step` may
remove a `done` unit and may operate on a `Completed` document, because the reason plus the appended
decision are the audited substitute for the guard and gating on document status would have forced a
full-document `replace`. `remove_step` ("this step should never have existed") and `skip_step`
("this planned unit was deliberately not done") remain distinct and are not interchangeable.

## 260928-MIK-L11 `set_field` Writes A Leaf's Declared Knowledge Effects

`task_doc_tools.py` adds `expectedKnowledgeEffects` (MIK-R11) to `_MUTABLE_FIELDS`, so `set_field` is the
route through which a leaf's task document declares, before implementation, the invariant and family effects
it expects (MIK-R11 rule 1: "written through `task_doc`"). The route's structure and operation set are
otherwise unchanged:

- the whole document is re-validated before the write, so a malformed declaration (a repeat of a subject and
  effect, a bad subject form, a label outside the vocabulary, a prose `requirementRef`, an empty list, an
  extra key, or the field on a master) is refused and nothing is written; `null` clears it;
- the field is `NORMATIVE`, so a `set_field` that declares or changes it is an `intent` mutation and changes
  the leaf's task-intent digest, while clearing it restores the former digest;
- `task_doc` never reads knowledge: an ID the memory does not hold is the worklist's `subject_unknown` fact;
- who may write the field (the architect, or the worker with the architect's approval) is procedural, since
  `task_doc` has no per-field role gate; the adversarial reviewer checks the declaration against the packet
  (ruling Q3, 2026-09-29T21:56:18+02:00);
- no real task document may carry the field before the L37 install, because the installed runtime refuses
  unknown task-document fields (ruling Q2).

- The settable flat fields, now including the declaration. [5]

## Evidence

### Repo-Internal References

The following current source owns the changed behavior; no external domain source is configured for this slice.

- Execution evidence checks real code and memory output cells. [6]
- None [7]
