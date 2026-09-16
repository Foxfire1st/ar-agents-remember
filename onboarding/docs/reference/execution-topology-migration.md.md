# docs/reference/execution-topology-migration.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `docs/reference/execution-topology-migration.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-08T16:45:00+02:00 |
| lastVerifiedCommitHash | `e0820b04a499cbfb2079c78485346c50917a238a` |
| lastVerifiedCommitDate | 2026-09-13T18:02:04+02:00|
| governingOverview | `docs/reference/overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The read-only inventory the guide documents. | `inventory_execution_topology` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:917-979 |
| The graph-authoring batch (and graph-less bootstrap) the guide documents. | `author_execution_graph` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:193-261 |
| Fail-closed validation of a sprint's commanded membership and natures. | `validate_execution_topology` | mcp/src/agents_remember/tasks/document_refs.py:300-350 |
| Exact per-contract activation is the single runtime selection authority and archives malformed snapshots before replacement. | `observe_atomic_series`; `publish_atomic_series_selection` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:145-152; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:155-212 |
| Queue waiting reasons observe activation without owning its lifecycle; only reconciling waits. | `activation_waiting_reason` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:275-287 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned operator guide.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-13T15:03:18+02:00 — Removed the round-1 source-side-debt note: the guide was corrected this round, so the card now records the corrected text instead of flagging it. Re-read `docs/reference/execution-topology-migration.md` and confirmed the three corrected spots — the intro's "That default describes the sprint's shape and serializes nothing" with a graph-less sprint declaring no dependencies and "selecting one never pauses another" (lines 5-11), section 3's waiting reasons from "each contract's own strict activation snapshot (`active`, `reconciling`, or vacant)" (lines 62-68), and the release-notes bullet naming a missing graph "a sprint shape, not a serialization mechanism (nothing serializes a graph-less sprint)" (lines 122-125). Body updated with the ruling and the invariant that a missing graph is a shape, not a serialization mechanism; the retired phrases (the `paused by the selected master` waiting reason and "the source-pair-selected atomic-sequential default") no longer occur in the guide. Re-verified every citation row against the changed guide's cited sources: `inventory_execution_topology` task_execution_topology.py:917-979 (declaration at 966), `author_execution_graph` :193-261 (declaration at 202), `validate_execution_topology` tasks/document_refs.py:300-350 (declaration at 305), `observe_atomic_series`/`publish_atomic_series_selection` atomic_series_activation.py:145-152 and :155-212, and `activation_waiting_reason` :275-287; all anchors still resolve inside their ranges. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T14:19+02:00 — Per-contract activation curation: the card now describes the atomic-series activation record as keyed per series contract (not one selection per protected source pair), so selecting one master neither pauses nor clears another contract's record, and the queue's only waiting reason is `atomic-series-reconciling`. Rebound the observer/publisher citations to atomic_series_activation.py:145-152 and :155-212 and the waiting reason to :275-287. Recorded that the frozen documented guide's own text (lines 7-9, 61-65, 119) still carries the retired source-pair wording as source-side debt; no source-doc change is claimed. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ01 preparation rebound the operator-guide activation citations to the current observer, publisher, and waiting-reason definitions; no guide-content change or acceptance claim.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.

- 2026-08-26T08:45+02:00 — Restored the canonical Docs/Cross-Repo reference section shape after
  reconciling this changed guide.

- 2026-08-26T08:20+02:00 — Reconciled the operator doctrine card to the frozen source; only the
  future real-code-commit verification stamp remains closeout-owned.

- 2026-08-26T05:20+02:00 — Reconciled the graph-less operator guide with source-pair activation:
  switching selection pauses rather than retires, reconciliation precedes exposure, the queue is a
  disposable observer, selector failure is runtime-scoped, and task authoring remains upstream.
  Final citations and verification remain post-Dagger/closeout-owned.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the guide was retitled from migration to authoring —
  `migrate_execution_topology` is gone, the atomic-sequential default covers graph-less sprints,
  and `author_execution_graph` bootstraps the first graph; reworked the procedure, seams, and
  release-notes sections accordingly. Verification remains closeout-owned.

- 2026-08-18T12:00:00+00:00 — 260815-DAG-L9: created as the operator migration/rollback reference for the
  explicit execution-topology cutover. Verification remains closeout-owned.
