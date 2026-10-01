# mcp/src/agents_remember/worktrees/queue

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/queue` |

## Governing Overview

[worktrees overview](../overview.md)

## Purpose

Builds, invalidates, publishes, and serves the disposable sprint closeout scheduling projection.
Canonical task documents and closeout doors are its inputs; the root operation journal owns every
claimed lifecycle after admission.

## Hot Path Summary

`closeout_preview.py` describes only code and memory-content writes plus informational cache refresh. `closeout_recovery.py` proves the same two outputs from Git and journal evidence; it never reconstructs ledger commit authority.

Canonical changes invalidate affected sprint projections to invalid-empty. A complete rebuild is
computed off-side from current task topology, canonical waiting doors, and per-contract activation;
publication occurs only after an exact-current source recheck. `closeout_queue.py` exposes status,
rebuild, and the short first-ready claim-admission fence. Projection member and graph helpers own
only deterministic readiness and order.

## Conventions

- Projection errors and source problems are bounded and typed. A capacity refusal is `invalid`, not
  `unreadable`: the source was read and is past its bound, and the codes that say so are declared
  once with that classification in `closeout_queue_errors.py` so a raiser and the projection's
  classifier cannot drift apart.
- The projection is evictable; canonical task, door, register, and journal sources are not copied
  into permanent queue authority.

## Invariants And Boundaries

- Only waiting door generations may be projection members.
- Task authoring never waits on or seeks permission from projection state.
- Claim, certification, commit, blocker, integration, and lifecycle evidence never live here.
- Graph-less atomic-sequential topology is valid; a graph, when present, contributes bounded order.
- Activation is read-only input: each live series is read from its own contract-keyed record, and
  only a reconciling record makes that series wait. Vacant and active are never waits, another
  master's state is never this contract's reason to wait, and the queue cannot select, release, or
  repair that authority.

## Evidence

### Closeout Recovery Uses Git Output Evidence

`closeout_recovery.py` remains in this package location but owns journal recovery, not queue authority. Recovery reads exact current code/memory refs, compares them with accepted journal commits, proves substantive cleanliness and source ancestry, and reuses already-created outputs. A missing, unreadable, malformed or changed `memory.md` is irrelevant to those Git proofs. Refresh of the consumer cache is best effort after the actual output is proven.

### MCAR-L02 Structured Curator Evidence

The queue evidence adapter no longer parses a stable Markdown filename. It delegates curator
evidence to the closeout integration route's sole structured currentness validator, then converts
that exact evidence list into door/projection facts. Generated reports are evidence bytes only;
historical files cannot compete with the stable manifest.

### Repo-Internal References

The following current source owns the changed behavior; no external domain source is configured for this slice.

- Recovery proves the accepted code and memory outputs without a cache lookup. [1]

## IAS Per-Contract Activation Projection

Multiple live atomic-series contracts for one protected source pair are normal, and each contract
owns its own activation record keyed by `contract_fingerprint` (the digest of its resolved contract
path). The closeout projection is a read-only observer of those records: it derives only
`atomic-series-reconciling` as a waiting reason, treats vacant and active as normal rather than
waits, and never treats another master's state as this contract's reason to wait. A snapshot that is
not this exact contract, or is otherwise malformed, becomes a typed projection source problem with an
explicit selecting repair; rebuild does not infer a winner from prior queue rows, task ordering, a
contract census, or ambient Git. The projection never owns an activation transition — it cannot
publish, release, or archive a record.

This does not subordinate task authoring to selection. Task mutation publishes canonical truth; classified semantic/readiness changes
invalidate affected projections to empty, and causes a rebuild from that new truth. Selection
and sync lifecycle remain separate worktree authorities, so invalidation cannot destroy retained
conflicts, commit evidence, or an in-flight operation.

## 260821-CLIVE Final Disposable Projection Route

This route is a current scheduling projection, not a lifecycle subsystem. The canonical transaction
is intentionally simple:

```text
task or door mutation
  -> invalidate affected sprint projections to invalid-empty
  -> rebuild from current task topology + canonical waiting doors
  -> recheck the exact source fingerprint under the short task CAS
  -> publish valid-built, or remain invalid-empty
```

`closeout_projection.py` captures the bounded canonical census;
`closeout_projection_members.py` recomputes readiness and deterministic priority/graph order; and
`closeout_projection_publication.py` owns invalidation, preview, off-side rebuild, and exact-current
publication. `closeout_queue.py` exposes status/rebuild and the short first-ready claim admission
check. `closeout_queue_graph.py` owns the queue adapter around the task domain's one bounded,
deep-immutable semantic graph index, while
`closeout_queue_evidence.py` retains canonical grade/admission source parsing.

`closeout_projection_source_facts.py` makes currentness inputs explicit: one source plane contains
task address plus only fields classified as completion readiness, and a second contains the
`semantic-topology/v2` fingerprint. The member source census additionally binds canonical
`taskIntent`; missing or changed door intent becomes a typed blocker. `closeout_projection_snapshot.py` freezes one exact readable,
classified census before publication. Whole task documents, private v1 topology tables, and old
projection rows are not source inputs.

Prior projection rows are never rebuild input. Only waiting door generations may be members.
Projection state cannot claim, certify, consume, block, release, abort, carry commits, or own
integration/lifecycle evidence. Task authoring is never subordinate to projection state. The five
deleted mutable-queue modules have no tombstones: still-current evidence moved to door source and
evidence owners; claim/cancel/supersede moved to the root operation journal; protected-ref exclusion
moved to atomic landing authority; and mutable blocker, `QueueBinding`, certification, consumption,
and action-driven initial-state contracts were retired rather than preserved as compatibility code.

## 260824-PDLS Final Projection Boundary

Queue construction, membership, evidence parsing, and publication now operate only on current task
truth and waiting door generations. Invalidation publishes invalid-empty state, rebuild derives a
fresh valid-built projection, and no queue row owns retry, claim, commit, certification, terminal,
or compatibility evidence.

## 260831-CCR-L01 Semantic Source Planes

Member readiness now receives one already-computed task-domain topology fingerprint. Queue adapters
translate typed topology refusals without changing status/detail and never maintain a parallel
identity algorithm. Graph-backed rebuild resolves and compares the authored graph once, substitutes
the sole immutable bound graph into the sprint context, and reuses its indexes for every candidate.
Graphless atomic-sequential mode remains explicit and valid.

## Current Landed Composition

The transitional `closeout_staged_quality.py` helper separates `prepare_staged_code` from fresh gate execution. Its returned tree and hook outcome feed certification admission after strict hooks settle; this helper location does not give scheduling projection state any certification or mutation authority.

## CCR-R12@v5 Current Queue Boundary

Queue/projection helpers describe and recover transaction state; they do not own normal quality or
certification acceptance. Closeout preview presents candidate/source checks, code commit, raw memory
metadata/entity/index refresh, one attributed memory-content commit when content changed, cache refresh, and finalization. Recovery proves
already-created outputs and uses the staged-index commit helper without repository hooks. Integration
publication moves the prepared pair under ref safety and creates no merge commit. Strict code or
memory checks, selected certification, curator coherence, independent review, and full suites are
explicit developer actions rather than automatic queue steps.

## Resolved Masters Stop Blocking Their Successors

Queue scheduling and projection now resolve masters on *terminal state* rather than completion.
`closeout_queue_graph.py::graph_context` and `incomplete_predecessor_map` build their blocking set
with `tasks/readiness.py::master_is_terminal`, so a predecessor master that was `abandoned` resolves
exactly like a `Completed` one and stops blocking its successors. The reason is stated in the source
and is a scheduling invariant, not a courtesy: an abandoned master is never going to produce the work
its dependents wait on, so leaving them blocked forever would make abandonment worse than doing
nothing. `closeout_projection.py::capture_projection_source` uses the same judgement to classify a
sprint source as `terminal`. Master-granular resolution is unchanged; only the terminal set widened.
