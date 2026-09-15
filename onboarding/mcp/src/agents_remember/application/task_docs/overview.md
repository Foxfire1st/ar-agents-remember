# mcp/src/agents_remember/application/task_docs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/application/task_docs` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-15T00:56:17+00:00 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935` |
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| reviewedWorkingCandidate | `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| governingOverview | `../overview.md` |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| Task-first transactional publication and independent projection refresh. | `publish_task_doc_set`; `publish_prepared_task_documents`; `publish_task_doc_transaction_and_refresh`; `preview_task_doc_projection_effects`; `preview_task_doc_transaction_projection_effects` | mcp/src/agents_remember/application/task_docs/task_doc_publication.py:81-85; mcp/src/agents_remember/application/task_docs/task_doc_publication.py:88-127; mcp/src/agents_remember/application/task_docs/task_doc_publication.py:130-145; mcp/src/agents_remember/application/task_docs/task_doc_publication.py:148-155; mcp/src/agents_remember/application/task_docs/task_doc_publication.py:158-173 |
| Zero-or-one graph-bearing publication batch and in-memory title context. | `require_single_graph_document`; `build_publication_batch_graph_titles` | mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py:16-33; mcp/src/agents_remember/application/task_docs/task_doc_graph_titles.py:36-48 |
| Atomic raw-section shape validation and missing-register scaffolding. | `scaffold_register_sections`; `_validated_section_list`; `_requires_register_scaffolding` | mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py:17-37; mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py:40-51; mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py:54-55 |
| The extracted step plane owns one exact addressing rule and the four step operations. | `exact_step_target`; `set_step`; `add_step`; `remove_step`; `step_payloads` | mcp/src/agents_remember/application/task_docs/task_doc_steps.py:97-124; mcp/src/agents_remember/application/task_docs/task_doc_steps.py:153-165; mcp/src/agents_remember/application/task_docs/task_doc_steps.py:168-190; mcp/src/agents_remember/application/task_docs/task_doc_steps.py:193-223; mcp/src/agents_remember/application/task_docs/task_doc_steps.py:264-275 |

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

## Repo-Internal References

The following current source owns the changed behavior; no external domain source is configured for this slice.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Execution evidence checks real code and memory output cells. | L247-L297 | [mcp/src/agents_remember/application/task_docs/task_unstarted_evidence.py](mcp/src/agents_remember/application/task_docs/task_unstarted_evidence.py) |

## Update History

- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Documented unstarted-task evidence after removal of ledger commit fields. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.

- 2026-09-14T07:05+02:00 — 260913-LCA-L5 route impact (curator, uncommitted change set on
  `ar/260913-lca-l5-ar`, base `52875e7a`): recorded the fail-closed authoring guard on the route.
  `_require_bindable_leaf_authoring` refuses a leaf document authored under a task root with no master
  document — the case where the derived `seriesContractPath`/`enclosures[]` would have nothing that could
  ever bind them — while the planning order (master document present, series contract not yet
  bootstrapped) stays allowed by the explicit guarantee that the leaf's first start binds both fields.
  Corrected the invariant that implied a leaf could be authored under any task root. Route documentation
  only: verification metadata remains closeout-owned and no execution or acceptance claim is made.
- 2026-09-13T14:24:00+02:00 — 260831-LOCR-L36 activation re-keying: corrected this route's
  remaining source-pair/selector phrasing to per-contract activation — an otherwise-valid task
  mutation is never subordinate to queue or per-contract activation state, and per-contract
  activation plus retained sync state are the downstream worktree authorities that re-evaluate the
  changed plan at their next admission boundary. The dated history entry below that names
  "source-pair activation" is retained as superseded history, not as a current claim. Source
  documentation only; verification metadata remains closeout-owned and no acceptance or test claim
  is made.
- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded the new `task_doc_steps` sibling in the
  route purpose and conventions (the step plane is a shared-contract owner, and the dispatcher must
  not grow a second addressing rule), added the step-plane source-evidence row, and added this
  section describing the extraction, the operations split by intent, and the two developer rulings
  for a reasoned `remove_step`. Route ownership, publication, and queue semantics are unchanged.
- 2026-09-11T23:05:00+00:00: Master abandonment curation: `require_commanded_masters_completed` now resolves commanded masters through `master_is_terminal` instead of a local `!= "Completed"` test, so an abandoned commanded master counts as terminal. Content change, not a range repoint.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `preview_task_doc_projection_effects`, `preview_task_doc_transaction_projection_effects`, `publish_prepared_task_documents`, `publish_task_doc_set`, `publish_task_doc_transaction_and_refresh` repointed to mcp/src/agents_remember/application/task_docs/task_doc_publication.py:130-145, mcp/src/agents_remember/application/task_docs/task_doc_publication.py:148-155, mcp/src/agents_remember/application/task_docs/task_doc_publication.py:158-173, mcp/src/agents_remember/application/task_docs/task_doc_publication.py:81-85, mcp/src/agents_remember/application/task_docs/task_doc_publication.py:88-127. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-10T02:27:58+02:00 — CCR-L42 parity curation: No route impact: curator preparation and closeout now run the shared sidecar and route body/history validators independently; this route's ownership and source semantics remain unchanged. No acceptance claim is made.

- 2026-09-05T07:05+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Recorded field-classified invalidation, exact resolved task intent for route review, and dry-run scope preflight. Current route claims were checked against the frozen candidate; this stamp records source verification, not execution or certification.

- 2026-08-29T18:29+02:00 — Reconciled the graph-title citation coordinate after the runtime and
  coherence refactor moved the cited symbol; task-publication behavior is unchanged.

- 2026-08-26T08:30+02:00 — Rebounded the graph-title source range after the frozen structural
  split; the task-first, always-unlocked authoring contract is unchanged.

- 2026-08-26T02:55+02:00 — Direct IAS architecture refresh: made explicit that task authoring is
  upstream of both queue projection and source-pair activation. Planning changes invalidate/rebuild
  scheduling and are re-evaluated by later worktree admission; they never mutate in-flight journal
  evidence. Verification remains frozen-candidate owned.

- 2026-08-25T17:21+02:00 — Reconciled typed unstarted-task recovery with projection invalidation.
  Verification remains closeout-owned.

- 2026-08-24T13:43+02:00 — 260821-DAGQC-L1: made the task-first publication ownership current,
  added the shared graph-cardinality/title and raw-section-scaffolding route owners, and removed the
  stale queue-subordinate transitional account. Verification metadata remains pinned until
  architect-owned closeout stamps the real code commit.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `application/task_docs`
  route — seven modules moved from `application/` (flat); `task_doc_tools` gained
  `_sprint_doc_identity`. Verified at code commit e5cb139f.
