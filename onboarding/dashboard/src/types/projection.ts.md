# dashboard/src/types/projection.ts

## Governing Overview

[dashboard/src/ overview](../overview.md)

## Purpose

Generated TypeScript mirror of the served workspace projection plus its enumerable runtime
vocabularies. It carries canonical `TaskDocumentRef` values on task-aware analytics without
turning runtime session/lifecycle ids into work identity. Since 260831-CCR (commit `99dc249b`)
it also mirrors the canonical `TaskIntentIdentity` wire shape (`task-intent/v1` schema + 64-hex
digest) and attaches it optionally to the lifecycle operation projection.

## Code Commentary

The lifecycle phase vocabulary now includes `recovering-private-preparation`. This exposes the existing private-preparation recovery phase without granting publication or lifecycle authority to the dashboard. Evidence: dashboard/src/types/projection.ts:352-352.

### Logic

The generated `LifecycleOperationProjection.phase` union has no `ledger-commit` or
`direct-ledger-commit` member. It mirrors the Python lifecycle vocabulary: code and memory output
publication remain observable, while the downstream ledger cache creates no separate commit phase.

The generator emits lifecycle, task, attention, engine, and metrics wire shapes together with checked
state vocabularies. Structural additions share one `TaskDocumentRef` interface. Task documents
remain the hierarchy authority; lifecycle and hosted-occupant fields are optional runtime
attachments.

`LifecycleOperationProjection` gains the optional `taskIntent?: TaskIntentIdentity` (line 349),
and the new `TaskIntentIdentity` interface (line 750-754) mirrors the JSON Schema refinements:
the required 64-hex `digest` and the closed `schema: "task-intent/v1"` union.

Since 260913-LCA-L6 the mirror carries no refinement comment on `CloseoutQueueNode.members`: the
candidate population is unbounded, so the generated interface declares the array as a plain
`members: CloseoutCandidateNode[]` (line 144). The 256-entry refinements that remain in this
generated file belong to other collections — `CloseoutCandidateNode.reasons` (line 130) and
`CloseoutQueueNode.sourceProblems` (line 149).

### Conventions

This file is generated from the Python projection schemas; edit the model/generator and resynchronize
rather than hand-maintaining parallel declarations.

### Invariants And Boundaries

- The task-document reference is repository-qualified and level-explicit.
- Runtime ids remain projections/correlation, not structural seat identity.
- Generated TypeScript and schema artifacts must remain synchronized.
- Only refinements the producer's Python schema actually carries are emitted, so a collection the
  producer leaves unbounded (today `CloseoutQueueNode.members`) gets no bound comment here either;
  the dashboard never adds a limit the server does not enforce.
- The task-intent identity is observation-only: the dashboard never mints or mutates a digest.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

No configured external domain-documentation source applies.

### Repo-Internal References

- The lifecycle phase union mirrors the code/memory-only vocabulary. [1]
- Structural analytics fields use the shared task-document reference. [2]
- Generated task documents carry real hierarchy and optional runtime attachment. [3]
- Execution nodes name their kind, leaf-id segment and task reference. [4]
- An execution endpoint carries a task reference and optional leaf id. [5]
- Execution edges bind predecessor and successor endpoints with a reason and optional judgment id. [6]
- The graph contains typed node and edge arrays. [7]
- Workspace projection remains the generated top-level wire contract. [8]
- The optional canonical task-intent identity on lifecycle operations. [9]
- The generated `task-intent/v1` identity interface. [10]
- The generated closeout-queue node carries an unbounded `members` array beside its 256-bounded `sourceProblems`. [11]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

No separate external implementation source applies to this file.

## L23 Source-Lineage Mirror

The frontend projection declares strict edge, recovery, and aggregate lineage
shapes and attaches the aggregate optionally to each Engine Process. Its closed
relations, sides, states, and `worktree_sync` tool mirror the server model; the
dashboard does not accept an open-ended string vocabulary here.

## 260815-DAG-L4 Projection Contract

The L4 delta keeps the generated dashboard contract aligned with the backend's organizational `super-to-leaf` lineage and lifecycle-operation guidance. The dashboard remains a projection consumer: it does not gain branch-mutation authority.


## 260815-DAG-L12 Render-Ready Graph View Types

The generated mirror gains the render-ready sprint graph wire shapes (L12-R4): `TaskExecutionGraphView` (nodes), `TaskExecutionNodeView` (kind `lump`/`segment`, masterRef + masterTitle, leafIds + leafTitles, waveIndex, frontierState, optional executionNature, predecessors), and `TaskExecutionPredecessorNode` (predecessorRef + predecessorTitle + reason + optional judgmentId); `TaskDocNode` gains the optional `executionGraphView` field. Regenerated by `scripts/sync-projection-types.py`.


## 260821-CLIVE-L2 Lifecycle Operation Projection Contract

The generated TypeScript mirror now carries optional lifecycle-operation `generation`, the
`direct-landing` kind, required opaque `legalControls`, and the termination-required/unreadable
status vocabulary. These fields describe root-journal-owned operation state to dashboard consumers;
they do not make the dashboard or disposable closeout projection an operation authority.

- The lifecycle operation wire type keeps generation optional, controls opaque, and kind/status vocabularies closed. [12]

## 260821-CLIVE Disposable Queue And Discard Audit Mirror

The generated mirror removes `AtomicBlockerNode` and the old mutable queue candidate fields.
`CloseoutQueueNode` now exposes exact-current service/source condition, bounded problems, and
generation-keyed `CloseoutProjectionMemberNode` rows; member classification is the closed
`ready | waiting | blocked` display vocabulary. These interfaces describe a disposable producer view
only and transfer no scheduling or operation authority to the browser. The `members` array itself
carries no item ceiling since 260913-LCA-L6 — see that section below — while `sourceProblems` and
each row's `reasons` keep their 256-entry refinements.

`DiscardUnstartedProofNode` and `DiscardedSubTaskNode` expose audited discard-before-start evidence.
Required series and optional task-document discard count/history fields remain distinct from live
subtasks and completed progress. Supported runtime-only schema constraints are emitted immediately
above their TypeScript properties as stable `JSON Schema refinements` comments, including nested item
constraints; TypeScript shape alone is not runtime validation.

## 260913-LCA-L6 Unbounded Closeout Queue Members

The regenerated mirror no longer documents a `maxItems` refinement on `CloseoutQueueNode.members`:
`members: CloseoutCandidateNode[]` is emitted with no refinement comment because the producer's
Python schema dropped the candidate cap, and a sprint may now declare any number of leaves. The
neighbouring refinements are untouched — `CloseoutCandidateNode.reasons` keeps
`{"maxItems":256}` and `CloseoutQueueNode.sourceProblems` keeps its own. No dashboard-side behaviour
changes: the panel still renders whatever rows the producer serves.

- The queue members remain unbounded while sourceProblems and candidate reasons retain their bounds. [13]

## 260824-PDLS Invalidation Outcome Mirror

`ProjectionInvalidationResult.outcome` no longer includes `not-created`. The producer always
materializes invalid-empty state when invalidating a projection, so dashboard consumers receive an
explicit non-admitting result rather than interpreting file absence as lifecycle or queue evidence.

## 260831-LOCR-L17 Terminal-Observer-Health Mirror

The regenerated mirror gains the `TerminalObserverHealth` interface — the exact
`ar-terminal-observer-health/v1` record plus the four serve-time computed fields
(`ageSeconds`, `lastSuccessAgeSeconds`, `staleCutoffSeconds`, `status`) — and the optional
`terminalObserverHealth?` property on `WorkspaceProjection`, beside `servingBuild?` and the two
heartbeat names. Three properties of the mirror matter to a dashboard reader:

- Its **five literal unions are CLOSED** (`status`, `schemaVersion`, `activeFailureCategory`,
  `activeFailureSummary`, `activeFailureType`), so `test/contract.test.ts` walks them and the
  served sample must carry a value for each — the residue allowlist cannot absorb them.
- Its **nulls are meaningful**: the payload is declared in `NULL_PRESERVING_MODELS`, so its
  nullable properties stay required `T | null` instead of becoming optional. `lastAttemptAt: null`
  is how "no observer attempt has completed in this serving lifetime" is served, and the dashboard
  distinguishes that from a server that reports no observer health at all (the key is then absent).
- Its **counter ceiling is a refinement comment**, `{"maximum":4294967295,"minimum":0}`, beside
  both serving-lifetime counters, because TypeScript cannot enforce it structurally.

The file remains generated by `scripts/sync-projection-types.py` and drift-checked; nothing in it is
hand-edited, and adding a serve-time key here implies the companion updates described in
[the dashboard overview](../overview.md) and in the `contract.test.ts` card.

## ARSPAWN-L4 Serving-Build Mirror

The generated `ServingBuild` interface now includes optional `sourceDigest`, `pythonExecutable`, and
`packageRoot` beside the existing version, boot, checkout, dashboard, and dirtiness fields. These
are serve-time diagnostic facts, not persisted projection authority. They let dashboard and MCP
evidence distinguish equal-version candidates and name the runtime that actually answered.

## 260831-CCR-R02 Task-Intent Mirror

The generated mirror adds the `TaskIntentIdentity` interface (closed `task-intent/v1` schema plus
64-hex digest) and attaches it optionally to `LifecycleOperationProjection`. Dashboard consumers
observe the exact identity a door/journal/operation binds; no intent authority transfers to the
browser.

## 260831-CCR-L15 Meaningful Revision Wire Field

The generated `LifecycleOperationProjection` interface gains the optional
`meaningfulRevision?: number` field (JSON Schema refinement `minimum: 1`), the
dashboard mirror of the durable CCR-R15 wait cursor that the lifecycle status-change wait tool
returns on snapshots.
