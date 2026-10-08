# mcp/src/agents_remember/tasks/document_refs.py

## Governing Overview

[Tasks overview](overview.md)

## Purpose

Resolves canonical sprint/master/leaf document references and their containment from the actual task
files. This is the topology authority behind structural seat qualification and replaces leaf-key
parsing as an identity model.

## Code Commentary

### Logic

`TaskDocumentTopology` indexes real task documents, normalizes repository-qualified references,
checks level and containment, and walks leaf→master→sprint without synthesizing anchors. Typed
`TaskDocumentRefError` failures distinguish malformed, missing, mismatched, and ambiguous topology.

For execution topology, `validate_execution_topology` resolves every sprint `orchestrates` alias to
exactly one commanded master, requires graph *master* membership (`graph.master_refs()`) to equal
that resolved set, refuses a missing graph or nature as migration-required — since 260815-DAG-L13
the refusal names the `task_doc.author_execution_graph` bootstrap/`set_nature` seam rather than a
removed migration operation — and — since
260815-DAG-L11 — refuses a segment node on an `atomic`-nature master (atomic masters admit lump
nodes only). Candidate overrides let task-doc authoring validate before publication. Since
260815-DAG-L13 a nature-less standalone master resolves at master altitude by default
(L13-R5e — only an explicit `organizational` standalone master stays a dead-end), and the public
`commanded_masters` derives a sprint's exact alias-commanded masters without re-resolving the
sprint from disk, so unpublished candidate sprints work.
Readers that reach `_commanded_masters_exact` share `missing_master_detail` for an alias with no live master.
The message names the sprint, master and archive or missing-folder location, and asks for restoration followed
by `task_doc.retire_master`. Admission differs: linkage validation returns without exact resolution when no
typed rows exist; active execution-topology validation can refuse a missing graph first. A retired-only
graphless sprint has no commanded membership to resolve.

An ambiguous alias is repaired with `task_doc.set_field`: give the unintended master its own id and title,
or replace the sprint entry with the intended master's canonical folder name. Reverse membership discovery
belongs to `tasks.sprint_rows.sprint_census`, which returns commanding, recording and unreadable populations.
Finalization refuses unreadable documents whose text names the master; retirement refuses every unreadable
document. There is no `commanding_sprints` method on `TaskDocumentTopology`.

Since 260815-DAG-L14 `validate_sprint_linkage` hard-fails NEW-shape sprint↔master linkage
drift on top of membership validation: every `subTasks` row carrying a typed `masterRef` must
resolve to exactly one master the sprint commands (same-repository), no two rows may type the same
master, and the target may not itself orchestrate. Legacy rows (seat-doc `file`, no `masterRef`)
are not checked here — `linkage_report`/`linkageFacts` surface them as drift facts instead (L14-R7
backward tolerance). The altitude role sets (`SPRINT_ROLES`/`MASTER_ROLES`/`LEAF_ROLES`) and
`REVIEWER_ALTITUDES` are re-exported from `tasks/document.py`, their canonical home.
`validate_role` treats reviewer as the deliberate exception to single-altitude roles: the same role
may bind leaf, master, or sprint documents, while unsupported roles and every other altitude
mismatch retain typed refusals. Reviewer ownership is not decided here; generation-bound parent
validation belongs to the structural seat plane.

Since 260815-DAG-L15 the atomic segment node-kind rule lives here once as the shared
`refuse_segment_nodes_on_atomic_masters(nodes, nature_by_ref)`, consumed by both the final
topology validator and the graph-authoring draft check (`_require_draft_node_kinds` in
`application/task_execution_topology.py`) so the refusal dialect has one home (L15-R8 F6). The
helper reads `nature_by_ref.get(node.ref)` — a missing key (an unresolvable draft ref) is never a
raw `KeyError`; the draft scan records an explicit `None` and the later membership validation names
the ref (L15-FIX-1).

`execution_leaf_placement` returns each commanded master's live leaf-to-segment `LeafPlacement`
(`MasterLeafPlacement`): computed against the master's live `subTasks` rows, so a leaf set that
changed after graph authoring surfaces as unknown/unplaced facts on read paths; only the
graph-authoring write path refuses an incomplete partition.
`execution_sprints_affected_by_master` inventories old and new folder/id/title
aliases so identity edits and same-path kind replacement cannot silently detach or collide a
commanded master; `execution_waves` exposes only the graph-derived node order after validating the
exact sprint snapshot it will dereference, so a concurrent migration cannot split validation from the
returned graph. Override resolution retains independent root-confinement and repository-identity
guards for pre-publication candidates.
`resolve_candidate` exposes that same canonical override resolver to other task-authority owners;
callers do not duplicate the root and repository checks when inspecting a document that has not
yet been written.

### Conventions

Canonical paths are coordination-root-relative and remain tied to the actual task document.

### Invariants And Boundaries

- Task files, not session ancestry, define containment.
- Every resolved reference names one real document at one verified level.
- Ambiguity and scope loss fail closed.
- This module does not inspect terminal liveness or choose occupants.
- The atomic node-kind rule is centralized here (single source of truth); the shared helper must
  never raise a raw `KeyError` on a missing nature mapping (L15-FIX-1).
- **Leaf placement resolves masters on terminal state, not completion:** `execution_leaf_placement`
  collects the placement-blocking set with `tasks/readiness.py::master_is_terminal`, so an
  `abandoned` master counts as resolved exactly like a `Completed` one and stops gating the segment
  that waited on it. This module still does not inspect terminal liveness itself; that judgement
  stays in `readiness.py`.

### Todos

None.

## Evidence

### Docs References


### Repo-Internal References

- Task document topology is centralized in one typed resolver. [1]
- Structural seats consume this topology to qualify parent and child relations. [2]
- The shared atomic segment-node-kind refusal used by the final validator and the authoring draft check (L15-R8 F6 / L15-FIX-1). [3]
- Leaf placement builds its blocking set from terminal masters (`Completed` or `abandoned`) through the shared readiness judgement. [4]

### Cross-Repo References

The task documents live in the configured coordination root, but the resolver contract is implemented
inside agents-remember and has no sibling-repository code dependency.

- An alias that resolves to no master is refused with the shared missing-master message; one that resolves to several is refused with a duplicate-alias message. [6]
- Shared sprint census reports commanding, recording and unreadable populations with caller-specific refusal policy. [7]

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260815-DAG-L15 Shared Node-Kind Rule

L15 extracted the atomic segment-node-kind refusal from `validate_execution_topology` into the
module-level `refuse_segment_nodes_on_atomic_masters` shared with the authoring draft check
(`_require_draft_node_kinds` in `application/task_execution_topology.py`), giving the node-kind
rule one home and one refusal dialect (playthrough F6). The helper uses `nature_by_ref.get()`, so
an unresolvable draft ref (typo'd `add_node` ref, or a master deleted after graph authoring)
defers to membership validation instead of raising a raw `KeyError` (L15-FIX-1).

## 260821-CLIVE Final Reference/Topology Contract

The current source seams include `TaskDocumentRefError`,
`refuse_segment_nodes_on_atomic_masters`, and `ResolvedTaskDocument`. These helpers own canonical
reference/topology resolution, including the projection-consumer query described below. They do not
publish tasks, invalidate/rebuild projections, or grant lifecycle authority; effect owners consume
their exact resolved refs.

### Reconciled Source Evidence

- The current module exposes `TaskDocumentRefError`, `refuse_segment_nodes_on_atomic_masters`, `ResolvedTaskDocument` at this ownership boundary. [5]

## 260821-CLIVE Projection-Consumer Resolution

`projection_sprints_affected_by_master` resolves readable old/new consumers for post-publication
refresh without allowing an unrelated malformed task to veto the authoritative write. Override-only
new masters participate in the repository census. Exact commanded membership remains fail-closed
when the unreadable document is addressed by its directory alias, while unrelated unreadable
documents are skipped. This is one scoped resolver policy for disposable refresh, not a fallback
reader or relaxation of strict execution topology.

## Repository-Wide Master Census API

`repository_master_documents(topology, repository)` is the public query for the complete canonical
master set used by repository-global branch-authority and linkage checks. The query is module-level
because it composes topology primitives without making repository census another mutable
responsibility of `TaskDocumentTopology`; topology methods and application callers use the same
function. The former public `repository_masters` method and private `_master_documents` duplicate
route are removed rather than retained as compatibility readers.
