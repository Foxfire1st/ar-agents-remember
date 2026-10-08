# docs/reference/execution-topology-migration.md

## Governing Overview

[docs/reference/overview.md](overview.md)

## Purpose

Operator-facing guide for the explicit execution topology (`executionNature` on commanded masters,
`executionGraph` on orchestration sprints). It is an *authoring* procedure, not a runtime cutover.
A sprint without an `executionGraph` uses the graph-less atomic-sequential choice, which describes
the sprint's shape — every commanded master executes atomically — and serializes nothing: a
graph-less sprint declares no dependencies, so independent masters proceed concurrently and selecting
one master never pauses or excludes a sibling. Canonical commanded-master order is an equal-priority
tie-break, while exact per-contract activation keys one record per series contract, so two
sprint-commanded masters that share one protected source pair each own their own selection and
neither one's state is the other's reason to wait. Selecting one master does not clear, retire, or
pause another contract's record. Authoring a graph is the explicit opt-in to dependency-aware
scheduling; no separate migration operation remains.

## Code Commentary

### Logic

The guide documents: (1) a read-only inventory that proposes the explicit nature
(atomic when an `ar/<slug>` branch already backs the master, organizational otherwise) with
parallel edges pending a ruling; (2) graph authoring through `task_doc.author_execution_graph` —
one validated mutation batch per call whose first `add_node` batch on a graph-less sprint
bootstraps the graph (`bootstrapped: true`), with judgment-bearing mutations requiring a canonical
Judgment Register row and final validation requiring exact `orchestrates` membership plus explicit
natures; (3) the defaults and fail-closed seams — no graph selects the per-contract-activated
atomic-sequential default, while the queue projects only `atomic-series-reconciling` as a waiting
reason (vacant and active are never waits, and a foreign master's state is never named as this
contract's blocker); manager/worker dispatch and atomic start/attach select, but reviewer/curator
inspection does not; selection publishes `reconciling` before exact source sync and `active` only
after both recorded bases are current; a malformed selector invalidates only affected runtime
projection/admission and is archived/replaced by the next exact selecting operation; task-document
authoring never reads it; a nature-less commanded master under an authored graph remains a hard
refusal naming `set_nature`; and (4) snapshot-based rollback that restores the pre-authoring tree
rather than re-enabling a compatibility path.

### Invariants And Boundaries

- The inventory never infers edges from file order, names, or status.
- A branch recorded atomic is only reclassified by an accepted strategist/orchestrator ruling.
- Rollback restores the snapshot; it does not retain a dual-reader or feature-switch fallback.
- A missing graph is a scheduling default, not an error, and it is a sprint shape rather than a
  serialization mechanism: nothing serializes a graph-less sprint, which declares no dependencies.
  A missing nature under an authored graph remains a hard refusal.
- Contract presence never elects the selected master; each series contract owns its own
  `contract_fingerprint`-keyed activation record, and the closeout queue owns no activation or
  operation-lifecycle transition.
- Selector corruption is scoped to affected runtime admission/projection and cannot subordinate an
  otherwise-valid task-document mutation.

The guide's own text was corrected this round and now matches the per-contract runtime; the
source-side debt noted in round 1 is gone.

- The intro says the graph-less default "describes the sprint's shape and serializes nothing", with a
  graph-less sprint declaring no dependencies so "independent masters proceed concurrently, and
  selecting one never pauses another or requires it to integrate, retire its contract, or terminate
  its agent/worktree", and canonical commanded-master order only "the stable tie-break where priority
  is equal" (guide lines 5-11).
- Section 3 derives its waiting reasons from "each contract's own strict activation snapshot
  (`active`, `reconciling`, or vacant)", with contract presence never electing a master and the queue
  owning no activation transition or lifecycle operation (guide lines 62-68).
- The release-notes bullet names a missing graph "a sprint shape, not a serialization mechanism
  (nothing serializes a graph-less sprint)" (guide lines 122-125).

Read the guide for the operator procedure; its wording is now the same rule this card documents.

### Todos

Source claims are reconciled to the frozen implementation. Verification metadata remains pinned to
the previously verified commit until governed closeout can stamp the real new code commit.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- The read-only inventory the guide documents. [1]

- The graph-authoring batch (and graph-less bootstrap) the guide documents. [2]

- Fail-closed validation of a sprint's commanded membership and natures. [3]
- Exact per-contract activation is the single runtime selection authority and archives malformed snapshots before replacement. [4]
- Queue waiting reasons observe activation without owning its lifecycle; only reconciling waits. [5]

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned operator guide.
