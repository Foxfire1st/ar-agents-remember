# dashboard/src/types/projection.ts

## Governing Overview

[dashboard/src/ overview](../overview.md)

## Purpose

Generated TypeScript mirror of the served workspace projection plus its enumerable runtime
vocabularies, one of which is the attention row's class: `ATTENTION_ITEM_CLASSES` (operational, action,
notice) beside the widened `ATTENTION_LANES` (repo, worktree, agent, task), with `AttentionItem` carrying a
required `itemClass` and `dismissible` and the optional task, agent, prompt, held-message and occurrence
identities a row may open. It carries canonical `TaskDocumentRef` values on native task entries/dependencies, not removed pickup/expectation DTOs, without
turning runtime session/lifecycle ids into work identity. Since 260831-CCR (commit `99dc249b`)
it also mirrors the canonical `TaskIntentIdentity` wire shape (`task-intent/v1` schema + 64-hex
digest) and attaches it optionally to the lifecycle operation projection.

## Code Commentary

### Task-reader wire fields

`TaskSummary` requires `form` (`sprint`/`master`/`task`), `type`, `headerNotes` and
`statusNoteTruncated`; `integrationBranch`, `statusNote`, `headerNotesTotal` and `reviewState`
remain optional. Its required reader fields also include `bodyRevision`, `codeExamples`,
`createdAt`, `decisions`, `executionWaves`, `kind`, `objective`, `openQuestions`, `orchestrates`,
`references`, `requirements`, `seats`, `sections` and `steps`; acceptance/design/completion,
direct-grant, discard, graph and dependency additions remain optional as declared.
`TaskStepNode` requires `noteTruncated` and `outcomeTruncated` beside optional `note`/`outcome`;
`TaskSubStepNode` has optional `note` without a note-truncation flag. A present
`TaskReviewStateNode` still requires whole-round `openFindings` and `totalFindings`, independently
of its findings preview. Supported older-recording recovery is not permission to invent a
malformed present review object missing those counts. `TaskEntry` separately owns key/id/title,
served stage, ordered membership, counts, major-step totals and worktrees; its `reference`,
`activity` and `summary` are optional. Optional `TaskListDisagreement[]` carries served list/record
discrepancies with required kind and record reference and optional row id, recordMaster reference,
original masterLiteral or actual parent key. It is neither a second task entry nor a
browser-authored membership edge. `TaskSummary` is reader content, not a second status authority.


The lifecycle phase vocabulary now includes `recovering-private-preparation`. This exposes the existing private-preparation recovery phase without granting publication or lifecycle authority to the dashboard. Evidence: dashboard/src/types/projection.ts:352-352.

### Logic

The generated `LifecycleOperationProjection.phase` union has no `ledger-commit` or
`direct-ledger-commit` member. It mirrors the Python lifecycle vocabulary: code and memory output
publication remain observable, while the downstream ledger cache creates no separate commit phase.

One TaskEntry/TaskCounts grammar replaces session lifecycle state constants and duplicate analytics document/series joins. The browser consumes stage/activity and counts rather than inferring them. TaskSummary is content, not a second task-status authority. TaskEntry retains eventAt but no longer declares task-event ageSeconds; the browser owns its event-age display. Other projection age fields are separate contracts.

`LifecycleOperationProjection` gains the optional `taskIntent?: TaskIntentIdentity` (line 349),
and the new `TaskIntentIdentity` interface (line 750-754) mirrors the JSON Schema refinements:
the required 64-hex `digest` and the closed `schema: "task-intent/v1"` union.

Since 260913-LCA-L6 the mirror carries no refinement comment on `CloseoutQueueNode.members`: the
candidate population is unbounded, so the generated interface declares the array as a plain
`members: CloseoutCandidateNode[]` (line 144). The 256-entry refinements that remain in this
generated file belong to other collections — `CloseoutCandidateNode.reasons` (line 130) and
`CloseoutQueueNode.sourceProblems` (line 149).

### Conventions


**L184 — INV-XZYGEB.** The client type is what the dashboard reads the projection as, so the fact's shape is declared here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## L126 Product-Record Wire Flag

`TaskDecisionNode` carries `product_record: boolean`: the server classifies legacy exact finalizer strings and remove/skip prefixes as product records, while the stored entry shape is unchanged. Existing finalizer-shaped records remain marked; current finalization does not emit a new decision. Authored-only preview numbering/counts exclude such records, and the whole-log page preserves them in the muted end disclosure. The type declaration itself does not call a writer or prove classification.

This file is generated from the Python projection schemas; edit the model/generator and resynchronize
rather than hand-maintaining parallel declarations.

### Invariants And Boundaries

- The task-document reference carries repository and path; task level/form is represented separately on task projections rather than as a field of TaskDocumentRef.
- Runtime ids remain projections/correlation, not structural seat identity.
- Generated TypeScript and schema artifacts must remain synchronized.
- Only refinements the producer's Python schema actually carries are emitted, so a collection the
  producer leaves unbounded (today `CloseoutQueueNode.members`) gets no bound comment here either;
  the dashboard never adds a limit the server does not enforce.
- The task-intent identity is observation-only: the dashboard never mints or mutates a digest.

### Todos

None.

## Optional direct grant display

TaskSummary carries optional directGrant giver/time evidence for display. Backend grant mutation and task authoring retain separate authority; generated declarations are not hand-maintained permission rules.

## Dependency Display Shape

TaskDependencyNode requires id/title; its canonical reference is optional. A file-less dependency has no reference to resolve, task-state word or navigation target. TaskSummary carries optional fixed prose/completion/dependencies; graph display nodes retain optional cycle. Default-null producer fields become optional non-null output properties under exclude_none serialization. These are declarations, not membership validation or scheduling functions.



- Core nullable properties are emitted as optional non-null output properties, except explicitly null-preserving models. [15] [15]
- Current CloseoutCandidateNode uses string classification/priority; queue members reference that interface. [16] [16]

## Evidence

- The generated TaskEntry wire type carries optional structured list disagreements beside its canonical membership and cached summary. [22]

- TaskSummary separates required reader fields from optional branch/note/review, content and graph additions. [19]
- TaskStepNode requires note/outcome truncation booleans beside optional prose; TaskSubStepNode has optional note without a truncation flag. [20]
- A present TaskReviewStateNode requires openFindings and totalFindings independently of its findings array. [21]

- A dependency keeps id/title without inventing a reference; TaskEntry event time is not a served age. [18]



### Docs References

No Domain Documentation source is configured.

No configured external domain-documentation source applies.

### Repo-Internal References

- The lifecycle phase union mirrors the code/memory-only vocabulary. Anchor: `refinements` [1]

- Execution nodes retain kind/leafIds/ref; display nodes add cycle?: boolean and retain graph-rendering fields. Shared DTO declarations are not order derivation. [4]

- An execution endpoint carries a task reference and optional leaf id. [5]
- Execution edges bind predecessor and successor endpoints with a reason and optional judgment id. [6]
- The graph contains typed node and edge arrays. [7]

- The optional canonical task-intent identity on lifecycle operations. [9]
- The generated `task-intent/v1` identity interface. Anchor: "task-intent/v1" [10]
- The generated closeout-queue node carries an unbounded `members` array beside its 256-bounded `sourceProblems`. Anchor: `string` [11]

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

The generated mirror gains the render-ready sprint graph wire shapes (L12-R4): `TaskExecutionGraphView` (nodes), `TaskExecutionNodeView` (kind `lump`/`segment`, masterRef + masterTitle, leafIds + leafTitles, waveIndex, frontierState, optional executionNature, predecessors), and `TaskExecutionPredecessorNode` (predecessorRef + predecessorTitle + reason + optional judgmentId); `TaskSummary` carries the optional `executionGraphView` field. Regenerated by `scripts/sync-projection-types.py`.


## 260821-CLIVE-L2 Lifecycle Operation Projection Contract

The generated TypeScript mirror now carries optional lifecycle-operation `generation`, the
`direct-landing` kind, required opaque `legalControls`, and the termination-required/unreadable
status vocabulary. These fields describe root-journal-owned operation state to dashboard consumers;
they do not make the dashboard or disposable closeout projection an operation authority.


## 260821-CLIVE Disposable Queue And Discard Audit Mirror

The generated mirror removes `AtomicBlockerNode` and the old mutable queue candidate fields.
`CloseoutQueueNode` now exposes exact-current service/source condition, bounded problems, and
generation-keyed `CloseoutCandidateNode` rows; the current generated declaration types
`classification` and `priority` as `string`, not a closed `ready | waiting | blocked` union. These interfaces describe a disposable producer view
only and transfer no scheduling or operation authority to the browser. The `members` array itself
carries no item ceiling since 260913-LCA-L6 — see that section below — while `sourceProblems` and
each row's `reasons` keep their 256-entry refinements.

`DiscardUnstartedProofNode` and `DiscardedSubTaskNode` expose audited discard-before-start evidence.
TaskSummary discard count/history remains distinct from live child membership/counts and completed progress. Supported runtime-only schema constraints are emitted immediately
above their TypeScript properties as stable `JSON Schema refinements` comments, including nested item
constraints; TypeScript shape alone is not runtime validation.

## 260913-LCA-L6 Unbounded Closeout Queue Members

The regenerated mirror no longer documents a `maxItems` refinement on `CloseoutQueueNode.members`:
`members: CloseoutCandidateNode[]` is emitted with no refinement comment because the producer's
Python schema dropped the candidate cap, and a sprint may now declare any number of leaves. The
neighbouring refinements are untouched — `CloseoutCandidateNode.reasons` keeps
`{"maxItems":256}` and `CloseoutQueueNode.sourceProblems` keeps its own. No dashboard-side behaviour
changes: the panel still renders whatever rows the producer serves.


## 260824-PDLS Invalidation Outcome Mirror

`ProjectionInvalidationResult.outcome` no longer includes `not-created`. The producer always
materializes invalid-empty state when invalidating a projection, so dashboard consumers receive an
explicit non-admitting result rather than interpreting file absence as lifecycle or queue evidence.

## 260831-LOCR-L17 Terminal-Observer-Health Mirror

The served-only tail declares servingBuild and watcherHealth. TerminalObserverHealth and the old notifier/supervisor heartbeat fields are absent; their former declarations are not current fixture gaps.

The current served-only diagnostics retain their own generated vocabularies and optional-field semantics. Native task state/activity and landing-operation phase/status remain separate contracts.

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

- The lifecycle phase union mirrors the code/memory-only vocabulary. Anchor: `refinements` [1]
- Execution nodes retain kind/leafIds/ref; display nodes add cycle?: boolean and retain graph-rendering fields. Shared DTO declarations are not order derivation. [4]
- An execution endpoint carries a task reference and optional leaf id. [5]
- Execution edges bind predecessor and successor endpoints with a reason and optional judgment id. [6]
- The graph contains typed node and edge arrays. [7]
- The optional canonical task-intent identity on lifecycle operations. [9]
- The generated `task-intent/v1` identity interface. Anchor: "task-intent/v1" [10]
- The generated closeout-queue node carries an unbounded `members` array beside its 256-bounded `sourceProblems`. Anchor: `string` [11]
- The lifecycle operation wire type keeps generation optional, controls opaque, and kind/status vocabularies closed. Anchor: `string` [12]
- The queue members remain unbounded while sourceProblems and candidate reasons retain their bounds. Anchor: `string`; "sourceProblems: CloseoutProjectionProblemNode[]" [13]

- Generated TaskEntry retains stage/activity and eventAt without a task-event ageSeconds field. [17]
