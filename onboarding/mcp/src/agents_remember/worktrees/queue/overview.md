# mcp/src/agents_remember/worktrees/queue

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/queue` |

## Governing Overview

[worktrees overview](../overview.md)

## Purpose

Builds, invalidates, publishes, and serves the disposable sprint closeout scheduling projection. Canonical task documents and closeout doors supply its scheduling inputs. Synchronous closeout keeps its transaction authority in the worktree closeout owner. The directory also houses closeout preview, Git-output recovery, and staged-quality helpers. Their location does not give scheduling projection state lifecycle, commit, or certification authority.

## Hot Path Summary

Canonical changes classified as affecting semantic topology or completion readiness invalidate affected sprint projections to invalid-empty. Rebuild derives a fresh projection from current task topology, canonical waiting doors, candidate evidence, planning registers, and per-contract activation. Publication rechecks the exact current source identity before publishing valid-built. The queue exposes status and rebuild. Member and graph helpers compute readiness and deterministic order.

Closeout preview describes code and memory-content writes plus informational cache refresh. Ordinary closeout recovery checks exact Git refs and accepted output identities. The direct-landing owner settles the kept history-closing receipt for its generation. Ledger refresh stays informational.

If recovered memory history was closed without a review fact, the success response can explain that the leaf’s revisions stay proposed. Recovery reads the owner history from the memory commit it already proved.

## Construction

### Canonical source census and publication

`closeout_projection.py` captures the canonical task, enclosure, door, and series census. Only waiting door generations enter membership. `closeout_projection_members.py` derives blockers, waiting reasons, and graph order; the census sorts members by classification, priority, order, and task identity. `closeout_projection_publication.py` owns invalidation, preview, off-side rebuild, and publication through the projection store. Previous projection rows are never rebuild inputs.

The transaction is:

```text
task or door mutation
  -> invalidate affected sprint projections to invalid-empty
  -> rebuild from current canonical sources
  -> recheck exact source identity under the projection store lock
  -> publish valid-built, or retain invalid-empty
```

Task publication validates its canonical sources, publishes task truth, and then invalidates and rebuilds affected projections. A projection failure is returned as a typed effect rather than permission to reject already-published task truth. Door publication similarly proves the canonical door write before refreshing its projection. Effective reads also treat a stored projection as invalid-empty when its current source fingerprint, classification, or members differ.

`closeout_queue.py` exposes status and rebuild and retains a first-ready helper. The current synchronous closeout entry calls its worktree owner directly. Queue rows remain planning observations.

### Readiness, topology, and evidence

`closeout_projection_source_facts.py` separates task address and fields classified as completion readiness from the task-domain `semantic-topology/v2` fingerprint. Member source facts additionally bind canonical task intent and candidate evidence. Missing or changed door intent becomes a blocker. Whole task documents and private v1 topology tables are not serialized as these source planes. `closeout_projection_snapshot.py` freezes one readable, classified census before constructing a publication build.

`closeout_queue_graph.py` adapts the task domain's bounded, deep-immutable semantic graph index. Graph construction validates the authored graph, binds the sole immutable graph into the sprint context, and reuses its indexes for candidates. Topology adapters preserve typed refusal status and detail instead of defining a second topology identity algorithm. This queue graph route requires an executionGraph and refuses its absence with task-execution-topology-migration-required. Its refusal text preserves the wider atomic-sequential concurrency intent; that text does not admit a graph-less candidate to this queue.

Dependency resolution is master-granular. The graph's resolved-master set uses the task-domain terminal predicate: an abandoned master resolves immediately; a Completed master resolves only when it has no completion blockers. A resolved predecessor stops blocking successors. Abandonment does not require unfinished child rows to become completed, because that master will never produce their work. The source census uses the same predicate to classify a terminal sprint and publish empty membership.

`closeout_queue_evidence.py` parses canonical scheduling grades and planning registers. Its curator adapter delegates to the closeout integration route's single structured currentness validator and returns that validator's exact evidence list. Door evidence converts that list into candidate provenance consumed by the projection. Generated reports are evidence bytes; the stable structured authority identifies the current immutable generation, so historical files do not independently compete for current authority.

### Per-contract activation

Each live atomic-series contract is observed through its own activation record, keyed by the digest of its resolved contract path. The projection derives `atomic-series-reconciling` only from that contract's reconciling observation. Vacant and active are not activation waits, and another master's state is never this contract's reason to wait.

A malformed or mismatched activation snapshot becomes a typed source problem with an explicit selecting repair. Rebuild observes activation; it does not infer a winner from previous queue rows, task ordering, a contract census, or ambient Git. Selection, source sync, release, and archival remain activation and worktree authorities.

### Preview, output recovery, and quality helpers

`closeout_preview.py` describes the ordinary closeout sequence: candidate/source checks, code commit, onboarding and entity metadata refresh, route overview metadata and index refresh, memory-content commit, derived cache refresh, and contract finalization. Series closeout instead reads exact named code and memory refs and records already-created commits. Ordinary external-memory closeout creates one attributed memory-content commit when content changed and otherwise records the existing output.

`closeout_recovery.py` owns Git-output recovery rather than queue authority. It compares actual code and memory refs with the accepted commit identities when recovery input is supplied, checks leaf worktree cleanliness with the memory cache excluded, and proves memory-source ancestry. The optional progress callback can record evidence for an owning operation. Ordinary synchronous closeout supplies no operation journal callback. Series recovery reads named work-branch refs rather than requiring leaf worktree cleanliness. Missing, unreadable, malformed, or changed `memory.md` does not decide these Git proofs. Cache refresh follows the proven memory output and reports availability separately.

The ordinary commit helper calls the shared tree publisher. The publisher runs the configured pre-commit check explicitly before `commit-tree` creates the object and the ref moves. Integration publication separately checks source refs, ancestry, checkout state, and landing authority, then moves the prepared code and memory refs by compare-and-swap without creating a merge commit.

`closeout_staged_quality.py` retains explicitly invoked staged preparation and quality execution. Preparation refuses a non-linked or conflicted worktree before staging, checks an optional candidate before/after staging and after a configured pre-commit hook, and returns the actual tree/hook result. Requested certification freezes its profile/admission through `quality/certification_records.py`; the old closeout certification admission consumer is removed. None of these helpers grants scheduling projection state mutation or certification authority.

## Invariants And Boundaries

- The projection is evictable. Canonical task, door, register, and journal sources remain outside permanent queue authority.
- Only waiting door generations may be members. Projection rows never own retry, claim, cancellation, supersession, certification, consumption, commit, blocker, terminal, or integration evidence.
- Task authoring never waits on or seeks permission from projection state. Classified canonical changes drive invalidation and rebuild; projection invalidation cannot destroy retained lifecycle conflicts, commit evidence, or an in-flight operation.
- Activation is read-only input. The queue cannot select, publish, release, archive, or repair an activation record.
- Projection source problems and readiness reasons are bounded and typed. Capacity refusals are classified as invalid rather than unreadable because their sources were read but exceeded a bound. Their codes and shared classification are declared together in `closeout_queue_errors.py`.
- Mutable blocker, QueueBinding, certification, consumption, and action-driven initial-state contracts are not operative scheduling-projection contracts. Canonical door sources and protected-ref landing authority have their own owners. The retained first-ready helper checks a projection member when explicitly called. The ordinary closeout tool goes directly to its synchronous transaction owner.

### Quality-action intent and current enforcement

The standing intent recorded here is that strict code and memory quality checks, selected certification, curator coherence, independent review, and full suites are explicit developer actions rather than automatic queue steps. The scheduling projection does not execute or accept those checks; it reads their canonical evidence.

That intent must not be read as a promise that ordinary closeout has no automatic enforcement. For converted leaf memory, the current closeout route automatically checks the mandatory invariant gate before claiming approval, validates and gates the exact memory output before publication, and applies those checks to recovered memory output as well. These checks belong to the closeout transaction, not projection state. The staged-quality helper and requested-certification record preparer remain; the old closeout certification-admission helper is removed. Remaining helper presence alone does not establish that normal queue actions invoke certification.

### Lifecycle metadata boundary

Historical labels such as final, landed, and resolved describe earlier curation framing, not a current task lifecycle status or acceptance promise. No current lifecycle status is asserted by this overview; establishing one requires canonical lifecycle authority outside this assigned card.

## Evidence

- Recovery derives the no-pass sentence only after finding the exact recorded memory output. [8]


- Canonical census, readiness, source planes, and immutable snapshots construct fresh membership. [2]



- Canonical task and door publication precedes projection refresh. The retained first-ready helper can check projection readiness. The synchronous closeout owner separately admits and executes its transaction. [3]



- Graph resolution uses the task terminal predicate; activation and capacity classifications retain their own deciding owners. [4]





- Curator evidence comes from the structured currentness validator and is consumed as door candidate provenance. [5]

- Preview, exact Git-output recovery, cache handling, explicitly selected staged quality, ordinary invariant-gated memory publication and protected-ref integration have separate owners; disposable scheduling projection grants none of their publication or certification authority. [6]
- Recovery proves the accepted code and memory outputs without a cache lookup. [1]
