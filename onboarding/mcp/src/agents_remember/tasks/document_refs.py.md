# mcp/src/agents_remember/tasks/document_refs.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/tasks/document_refs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T15:04+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

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
Since 260815-DAG-L14 `validate_sprint_linkage` hard-fails NEW-shape sprint↔master linkage
drift on top of membership validation: every `subTasks` row carrying a typed `masterRef` must
resolve to exactly one master the sprint commands (same-repository), no two rows may type the same
master, and the target may not itself orchestrate. Legacy rows (seat-doc `file`, no `masterRef`)
are not checked here — `linkage_report`/`linkageFacts` surface them as drift facts instead (L14-R7
backward tolerance). The altitude role sets (`SPRINT_ROLES`/`MASTER_ROLES`/`LEAF_ROLES`) are
re-exported from `tasks/document.py`, their canonical home.

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

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Task document topology is centralized in one typed resolver. | `TaskDocumentTopology` | mcp/src/agents_remember/tasks/document_refs.py:82-575 |
| Structural seats consume this topology to qualify parent and child relations. | `StructuralSeatResolver` | mcp/src/agents_remember/serving/structural_seats.py:22-161 |
| The shared atomic segment-node-kind refusal used by the final validator and the authoring draft check (L15-R8 F6 / L15-FIX-1). | `refuse_segment_nodes_on_atomic_masters` | mcp/src/agents_remember/tasks/document_refs.py:42-59 |

## Cross-Repo References

The task documents live in the configured coordination root, but the resolver contract is implemented
inside agents-remember and has no sibling-repository code dependency.


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

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `TaskDocumentRefError`, `refuse_segment_nodes_on_atomic_masters`, `ResolvedTaskDocument` at this ownership boundary. | L34-L39; L42-L59; L63-L66 | `mcp/src/agents_remember/tasks/document_refs.py` |

## 260821-CLIVE Projection-Consumer Resolution

`projection_sprints_affected_by_master` resolves readable old/new consumers for post-publication
refresh without allowing an unrelated malformed task to veto the authoritative write. Override-only
new masters participate in the repository census. Exact commanded membership remains fail-closed
when the unreadable document is addressed by its directory alias, while unrelated unreadable
documents are skipped. This is one scoped resolver policy for disposable refresh, not a fallback
reader or relaxation of strict execution topology.

## Update History

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged override-aware, unrelated-failure-tolerant projection consumer resolution. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: extracted the shared atomic segment-node-kind refusal
  (`refuse_segment_nodes_on_atomic_masters`) consumed by the final validator and the authoring
  draft check; `nature_by_ref.get()` closes the L15-FIX-1 `KeyError` path. Verified at code commit
  de3a0fd9.

- 2026-08-20T04:16+02:00 — 260815-DAG-L14: `validate_sprint_linkage` hard-fails new-shape typed
  sprint↔master linkage drift (typed row must resolve to a same-repository commanded non-orchestrating
  master; no duplicate typed rows); legacy shapes stay facts. Altitude role sets now come from
  `tasks/document.py`. Verified at code commit 8071a644.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: a nature-less standalone master resolves at master
  altitude by default (only an explicit `organizational` standalone stays a dead-end); migration
  recovery strings re-point to `task_doc.author_execution_graph`; `commanded_masters` is public so
  the atomic-sequential default derives membership from aliases without re-resolving the sprint.
  Verification remains closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: topology validation compares resolved command membership
  against `graph.master_refs()`, refuses segment nodes on atomic masters, and gains
  `execution_leaf_placement` / `MasterLeafPlacement` reporting live unknown/unplaced leaf facts;
  `execution_waves` returns node waves. Verification remains closeout-owned.
- 2026-08-16T05:27+02:00 — L4 exact-review repair: exposed the existing canonical override
  resolver through `resolve_candidate`, preserving its root-confinement and repository-identity
  checks for live-leaf publication authority without adding a second validation route.
- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-15T03:20:17+02:00 — 260815-DAG-L1 independent-review repair: `execution_waves` now pins
  the first resolved sprint into topology validation before deriving its waves, closing the
  double-read race in which validation and return could observe different graph generations.
- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: forcing coverage now reaches
  non-sprint topology use plus override root-confinement and repository-identity refusals.
  `execution_waves` relies on the immediately preceding durable topology validation instead of
  carrying a second impossible missing-graph branch.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: added the affected-sprint census
  used to revalidate old and new folder/id/title aliases, preventing commanded-master identity
  drift or a new alias collision from bypassing exact execution-graph membership.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: canonical task topology now validates exact
  `orchestrates`/graph membership, rejects aliases and unresolved masters, requires every commanded
  nature explicitly, and exposes graph-derived waves without inference.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created as the real-document topology authority; absorbs canonical validation formerly described by `serving/leaf_ref_validation.py`.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: predecessor leaf-reference card was verified against the then-current worktree; stale moved-path references were repaired.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 curator: predecessor card rebound two onboarding citations to code authorities.
- 2026-08-02T16:55+02:00 — 260731-EFA-L6 curator: predecessor card repaired three repo-internal citation rows.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: predecessor leaf validation added bounded legacy role-suffix detection and canonical leaf-plus-role refusal guidance.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: predecessor card was created for terminal leaf-key normalization at serving and MCP write boundaries.
