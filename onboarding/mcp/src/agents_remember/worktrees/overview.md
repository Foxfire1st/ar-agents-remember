# mcp/src/agents_remember/worktrees

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-11T10:26:37+02:00 |
| lastVerifiedCommitHash | `5410fb07d0d3a73f4d81d57ed020bbfcdaaa2267` |
| lastVerifiedCommitDate | 2026-09-12T18:45:26+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## What This Area Is

This route owns the durable worktree-enclosure and protected-source coordination primitives beneath
the public lifecycle modules. The current architecture adds two related but distinct owners:
source-pair-scoped atomic-series activation decides which live master may expose implementation
work, while a contract-addressed sync transaction reconciles code and external-memory sources
without depending on a readable task document for its in-flight journal.

## Hot Path Summary

`activation/atomic_series_activation.py` is the single disposable selection authority for one
normalized source pair; its release and terminal siblings own exact vacancy. The selecting
transaction publishes `reconciling`, runs exact source sync, and publishes `active` only after both
required bases are current. Root-level `sync_transaction.py` drives the journaled state machine;
focused state, authority, Git, recovery, result, and source-refresh modules own their respective
proof and response boundaries.

Master-series bootstrap observes its transient root journal and durable series contract under the
same existing per-master bootstrap mutex on apply. A concurrent starter therefore sees either the
live journal or the published contract across that handoff; it cannot read before publication,
wait behind the winner, then treat the retired journal as an orphan. Dry-run remains unlocked and
write-free, and no retry, fallback reader, compatibility route, or second lock namespace is added.

## CCR-R25 Actionable Refusal Surface

The route-review owner now supplies one pure projection for observed review refusals. Application
start/admission and direct closeout reuse it to preserve the concrete status, expected/observed
facts, and exact contract-bound task-document address; the caller supplies any review payload. The
projection does not alter route altitude, create review records, or weaken candidate currentness.
The activation owner likewise exposes source-pair observations and bounded admission evidence while
leaving selector and sync mutation in their existing transaction owners.

## L30 Quality Publication Boundary

The child `modules/quality` route retains actual rail evidence and immutable selected certificate generations. Its host Dagger registry uses the neutral kernel file lock while checkout durable stores preserve their coordination guard. L33 composes journal-selected admission, original certificate readback and suffix execution through the existing lifecycle owners. Gate-5 observation/execution and finalization remain explicit continuation capabilities; the default application bundle installs `PreparedCloseoutContinuation`. See [the modules overview](modules/overview.md) for read/export/prune owners and [the integration overview](integration/overview.md) for operation-selected execution.

`services.py` is the downward service boundary for provider, citation and memory work. Its canonical task-observation method and separate memory/finalization continuation avoid imports from worktrees into higher-level memory implementations. Read [the service card](services.py.md) for explicit binding and absent-capability behavior.

## What Belongs Here

| Path | Role |
| --- | --- |
| `activation/` | source-pair selector, selecting transaction, exact release, and terminal bridge |
| `sync_transaction*.py` | resumable source synchronization, journal, Git proof, authority refs, and recovery |
| `worktree_contract.py` and enclosure helpers | canonical worktree/enclosure authority used by child lifecycle routes |
| `modules/` | public lifecycle command composition |
| `queue/` | disposable waiting-candidate scheduling projection |
| `integration/` | protected branch integration and lifecycle journals |
| `services.py` | explicit provider, memory, citation and certification-continuation ports |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| task-document authoring or publication permission | `tasks/` and `application/task_docs/` |
| closeout claim, commit, certification, integration, or recovery evidence | `worktrees/integration/lifecycle/` and closeout-door owners |
| public MCP schema/transport translation | `mcp/registration/` and `mcp/tools/` |

## Structures Found Here

- `AtomicSeriesSourcePair` and one fingerprint-addressed activation record per protected pair.
- `vacant`, `reconciling`, and `active` selector states; `unreadable` is an observation, not a
  selectable state.
- One stable `.lifecycle/sync-operation.json` record per worktree enclosure plus pinned
  `refs/agents-remember/sync/...` authority on participating repositories.
- Separate code and memory side records with admitted base/source/pre-sync heads, plan, retained
  conflict set, and exact result head.

## Operating Model

1. A selecting public start/attach/dispatch or sync operation identifies one canonical series
   contract and derives its normalized code/memory source pair.
2. Selection atomically replaces the pair's prior snapshot with this master in `reconciling`.
   Other live series remain intact and merely project as paused.
3. The sync transaction pins exact base, pre-sync, and source commits, journals admission below the
   enclosure root, and advances code then memory under repository integration authority.
4. A dirty moving side's candidate is parked into the transaction before the carry and returned
   after it (restore on the completed path, on resume, and on cancel); a genuine merge conflict is
   retained in the operation-owned worktree. The integration lock is released while an agent
   resolves and stages it; a later exact contract-addressed `continue` validates and commits it,
   while `cancel` restores all provably operation-owned heads and returns the parked candidate.
5. Finalization writes the new base pair and terminal journal before removing temporary worktrees
   and authority refs. If the official source moves again, the completed generation reports that
   fact and a new generation may be admitted.
6. Atomic implementation becomes visible only after exact current bases are proven and selection
   advances to `active`.
7. Terminal cleanup attempts to vacate only the exact selected terminal contract. A missing,
   unreadable, vacant, or different selection is preserved and cannot be cleared by the old master.
8. A fresh ordinary series integration has no leaf closeout door and records that authority as
   `not-applicable`; it is not direct execution. Direct landing remains the policy-gated delivery
   route for an explicitly selected leaf without an enclosure, while fresh leaf integration still
   requires its exact claimed closeout source.

## Parked Candidate And Closeout Auto-Carry

The sync transaction now parks a dirty moving side's uncommitted candidate instead of refusing it.
`sync_transaction._admit_participating_sides` runs the parkability preflight, returns the read-only
preview for `dry_run`, and otherwise parks each dirty non-temporary, actually-moving side with
`git stash push --include-untracked`; the stash identity, bounded path sample
(`WIP_PATH_SAMPLE_LIMIT = 128`) and true path count are journaled in the same admission write. The
candidate is restored on the completed path, on resume, and on cancel, and `finalize_sync` refuses
while any side still parks its candidate. Kept refusals are a worktree whose index already has
unmerged paths and an unprovable checkout; an unprovable restore keeps the stash and refuses with
`sync-git-proof-failed`. See the child cards for the exact primitives.

Supporting that, the closeout-family lineage guard self-heals a settleable stale break:
`modules/closeout_lineage.heal_current_source_lineage` carries a `behind > 0` edge (a leaf that owns
its own commit is normal) through this same sync transaction, refuses a `dry_run` without mutating,
escalates an unprovable projection to the human developer, and hands back a retained sync conflict
with both worktrees and their resolution duties. `replay` is untouched and remains the
memory-carryover vehicle.

## Main Flows

### Select And Admit An Atomic Master

1. Refresh remote-tracking evidence outside the integration lock.
2. Re-read the canonical contract under source-pair integration authority.
3. Publish exact selection as `reconciling`.
4. Complete or resume the source-pair sync transaction.
5. Publish `active` only when contract bases equal current admitted source tips.

### Resolve Or Cancel Retained Sync Conflict

1. Read the stable enclosure-root journal and pinned Git authority.
2. Resolve and stage the retained merge in the reported code or memory worktree.
3. Call the same contract-addressed sync with `resolution_action="continue"`, or call it with
   `resolution_action="cancel"` to restore the pinned pre-sync pair.
4. Fail closed for missing/malformed identity; explicit cancellation may recover from complete
   pinned refs and preserves incomplete authority for manual repair.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `activation/atomic_series_activation.py` | selector store | single source-pair activation authority and strict observation | covered |
| `activation/atomic_series_activation_release.py` | selector transition | exact cancellation and terminal vacancy | covered |
| `activation/atomic_series_activation_transaction.py` | admission state machine | binds selection to exact sync-before-exposure | covered |
| `activation/atomic_series_activation_terminal.py` | terminal bridge | prevents paused cleanup from clearing a newer selection | covered |
| `sync_source_refresh.py` | pre-lock evidence | shared bounded upstream refresh without local authority | covered |
| `sync_transaction.py` | transaction driver | public start/resume/continue/cancel routing | covered |
| `sync_transaction_state.py` | stable journal | state survives task/contract readability failures | covered |
| `sync_transaction_authority.py` | identity/admission | pins sources and validates official code-memory ledger pairing | covered |
| `sync_transaction_git.py` | Git proof | retains conflicts and proves exact operation-created history | covered |
| `sync_transaction_recovery.py` | finalization/recovery | terminal publication, rollback, and malformed/missing journal escape | covered |
| `sync_transaction_results.py` | public evidence | consistent previews, conflict guidance, and terminal replay | covered |

## Local Invariants And Traps

- Task authoring is upstream of scheduling and selection; neither activation nor queue state
  may veto it. Its exact source publication still uses the canonical task-publication lock.
- The activation snapshot is disposable selection, not a lifecycle journal or retirement record.
- Multiple live series contracts for one source pair are normal. Selection change auto-pauses old
  work without deleting or terminalizing it.
- Sync owns lifecycle evidence in the stable enclosure-root journal and Git refs; the queue owns
  none of it.
- Normal readers never infer selection or sync state from legacy files, task text, queue rows, or
  ambient Git. Missing/corrupt authority fails closed and is repaired only by explicit bounded
  selection/cancellation paths.
- External-memory ledgers are newest-first state history. Sync preserves every exact parent row and
  accepts repeated code commits; the newest matching row remains current authority.
- Cleanup may release only an exact selected terminal contract and must do so before deleting the
  canonical contract pointer needed to prove identity.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Task observation and memory/finalization continuation use explicit service ports. | `MemoryQualityPort`; `CertificationContinuationPort`; `WorktreeServices` | mcp/src/agents_remember/worktrees/services.py:111-128; mcp/src/agents_remember/worktrees/services.py:131-141; mcp/src/agents_remember/worktrees/services.py:144-151 |
| The activation record is a strict source-pair fingerprinted snapshot with explicit selection states. | `AtomicSeriesSourceRef`; `AtomicSeriesSourcePair`; `AtomicSeriesActivationRecord`; `AtomicSeriesActivationArchiveEvidence` | mcp/src/agents_remember/models/structural/atomic_series_activation.py:16-30; mcp/src/agents_remember/models/structural/atomic_series_activation.py:33-39; mcp/src/agents_remember/models/structural/atomic_series_activation.py:42-54; mcp/src/agents_remember/models/structural/atomic_series_activation.py:57-72 |
| Selection observation treats absence as vacant and validates the exact canonical series/source pair rather than inferring from task or queue state. | `atomic_series_source_pair`; `observe_atomic_series` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:131-153; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:196-213 |
| Selecting admission publishes reconciling, delegates exact sync, and publishes active only after the current source pair is proven. | `activate_atomic_series_contract`; `reconcile_selected_series_under_authority` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:55-100; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:103-121 |
| The stable journal lives at `.lifecycle/sync-operation.json` and projects recovery without reading task text. | `SyncOperationStore`; `observe_sync_operation` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:172-366; mcp/src/agents_remember/worktrees/sync_transaction_state.py:369-385 |
| The sync driver retains conflicts for continuation and exposes explicit cancellation. | `sync_contract_under_authority`; `_continue_resolution` | mcp/src/agents_remember/worktrees/sync_transaction.py:83-111; mcp/src/agents_remember/worktrees/sync_transaction.py:539-570 |
| Cancellation restores only operation-owned heads; malformed or missing journals recover only through explicit pinned-ref proof. | `cancel_sync`; `recover_unreadable_journal`; `recover_missing_journal` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:160-191; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:194-264; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:267-284 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `sync_source_refresh.py` | [`sync_source_refresh.py.md`](sync_source_refresh.py.md) | covered | shared pre-lock fetch evidence |
| `sync_transaction.py` | [`sync_transaction.py.md`](sync_transaction.py.md) | covered | transaction driver |
| `sync_transaction_authority.py` | [`sync_transaction_authority.py.md`](sync_transaction_authority.py.md) | covered | source/contract authority |
| `sync_transaction_git.py` | [`sync_transaction_git.py.md`](sync_transaction_git.py.md) | covered | exact Git mutation/proof |
| `sync_transaction_recovery.py` | [`sync_transaction_recovery.py.md`](sync_transaction_recovery.py.md) | covered | finalization and recovery |
| `sync_transaction_results.py` | [`sync_transaction_results.py.md`](sync_transaction_results.py.md) | covered | result and guidance construction |
| `sync_transaction_state.py` | [`sync_transaction_state.py.md`](sync_transaction_state.py.md) | covered | stable journal model/store |

## Child Overviews

| Route | Why It Has Its Own Overview |
| --- | --- |
| [`activation/overview.md`](activation/overview.md) | source-pair selector, reconciliation-bound admission, and exact vacancy |
| [`integration/overview.md`](integration/overview.md) | protected-source integration and lifecycle journals |
| [`modules/overview.md`](modules/overview.md) | public worktree command composition |
| [`queue/overview.md`](queue/overview.md) | disposable closeout scheduling projection |

## How To Use This Area

When changing worktree coordination:

1. Read this overview for selector/sync ownership.
2. Read the nearest child overview when editing `integration`, `modules`, or `queue`.
3. Read the exact file-level onboarding and the focused tests.
4. Keep task truth, disposable scheduling, selection, and lifecycle evidence in their separate
   authority planes.

## CCR Intent And Certification Composition

Route reviews, closeout doors and lifecycle candidates now share canonical task intent and
content-digested direct evidence dependencies. Direct landing refuses absent/stale intent;
contract publication rejects a door without current intent. Task publication classifies
semantic versus observational edits before deriving affected queue scopes.
`services.CertificationMemoryRailsPort` supplies the memory-domain registry contribution
without importing memory quality upward. The quality and integration routes now compose frozen
admission, journal-selected original certificates and R21 suffix execution.
`CertificationContinuationPort` separates current memory observation, Gate-5 execution and
finalization. The default application bundle installs `PreparedCloseoutContinuation`; an incomplete
custom composition without the required capability still refuses instead of completing.
Child overviews retain the precise execution and publication boundaries.

## Needs Verification

- Verification stamps record source review. Aggregate execution, final provenance publication,
  and acceptance require their separate closeout evidence.
- [CURATOR] Generated route indexes are refreshed from explicit frozen code/onboarding roots in
  this final pass; they are never hand-edited.

## MCAR-L02 Curator-Coherence Authority

The integration/closeout child route now owns one stable structured coherence manifest and
content-addressed generation per leaf. It captures the same isolated add-all future code tree used
by closeout, the paired memory tree, candidate-relevant task topology, and the exact structured
memory-quality attestation. Publication validates one agent judgment per candidate and writes the
stable selector last; all readiness consumers share its currentness validator.

## MCAR-L02 Candidate Observation Concurrency

Candidate-tree reads across status, dashboard, queue, memory, route review, and closeout now share
one low-level isolation contract: a caller supplies a scratch namespace, while
`worktree_candidate_tree` allocates a unique temporary index for each invocation. Concurrent
observers may therefore inspect one dirty candidate without mutating the real Git index or deleting
another observer's scratch state. Candidate identity remains the resulting Git tree; temporary
filesystem names carry no lifecycle or semantic authority.

## MCAR-L03 Exact Pair Resolver

`memory_candidate_pair.py` — relocated from `worktrees/integration/closeout/` to `memory_quality/` by
the de-entanglement cut (commit `0b63d6fc`) — is the sole read-only authority for worktree-backed
memory candidates. It proves requested contract/repository identity, live roots, Git repository
membership, checked out work branches, source/base equality, and base ancestry before emitting the
shared pair model. No queue, report, repo-id lookup, branch switch, or fallback participates.

## 260831-CCR-L01 Shared Leaf Identity Boundary

`task_leaf_binding.py` now delegates row/source identity to the pure task-domain
`tasks/leaf_binding.py` owner used by semantic topology. Lifecycle start/discard and closeout
topology therefore require the same composite facts: exact parent row number and file, canonical
direct-child JSON ref, repository/directory, child id, and stem. Stem-only or split identities fail
with typed status/detail; no worktree-local fallback remains.


## Integrated IAS Recovery Contract

The default application bundle installs `PreparedCloseoutContinuation`, composing the memory-certification producer and prepared finalizer through the existing downward port. The closeout child owns resumption of selected private outputs and original C/M/L publication. Source-pair selection, synchronization, ledger authority and coordinator isolation are unchanged; an absent capability in an incomplete custom composition still refuses.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.


## CCR-R12@v5 Current Worktree Delivery Boundary

Worktree delivery preserves exact task/contract/source identity, explicit approval and handover
controls, leases, recovery evidence, and protected ref safety. Normal closeout commits code,
mechanically refreshes and commits external memory, and records the ledger; normal integration
publishes the prepared pair with ref/tree movement and no merge commit. Strict code quality, memory
quality, selected certification, curator coherence, independent review, and full suites are not
automatic transaction steps; full suites require an explicit developer request.

## Route Impact: Landing Record And Terminal Master State

This route's public surface grew by one entry point and one re-export. `git_worktree_manager.py`
re-exports `record_landing_result` from `modules/record_landing.py` and lists it in `__all__`, so the
pull-request landing tool and the local `worktree_integrate` path reach the same writer in
`modules/landing_record.py`; the terminal `integration` cell therefore has exactly one definition.
`modules/start.py` gained the matching CLI adapter wiring. Retiring a series' integration branch now
requires the master's own terminal task state through
`integration/integration_branch_authority.py::_require_series_task_terminal`, with `worktree_cleanup`
requiring `Completed` exactly and `worktree_abandon` accepting `Completed` or `abandoned`;
`series_closeout.py` keeps its `!= "Completed"` test and names abandonment distinctly
(`atomic-series-closeout-master-abandoned`) because closeout proves a completion fact and abandonment
is reclaimed through `worktree_abandon`.

## Route Impact: Checkpoint Landing (260831-LOCR-L30)

This route gained the partial-master landing verb, and it is the first way a series' integration refs
can move without the master being complete. `series_closeout.py::publish_series_checkpoint_under_authority`
keeps every authority that protects other owners' refs and drops only the two completion assumptions
the final series route proves; it refuses an already-`Completed` master
(`atomic-series-checkpoint-master-complete`), so a checkpoint can never downgrade a finished
integration. `modules/integrate.py::checkpoint_landing_result` threads a keyword-only
`checkpoint` flag through the shared preflight and ref move, and
`modules/landing_record.py::record_landed_integration` now writes either `checkpointed` (cleanup
untouched) or `completed` + `cleanup="pending"` from that flag, so the terminal `integration` cell
still has exactly one writer. The facade re-exports `checkpoint_landing_result`, and the public
`worktree_checkpoint_landing` tool exposes it.

The same leaf widened the series abandon guard: `worktree_abandon` now refuses a master whose
integration cell records **any** landed line — `completed` or `checkpointed` — because abandoning
asserts that none of the work was taken.

A checkpointed contract projects as **still working**, and the projection is deliberate.
`worktrees/modules/guidance.py::_post_integration_phase` gained a `checkpointed` branch that returns
phase `worktree-started` with `nextOperation: "continue_work"` / `nextTool: "worktree_status"`, and a
summary stating that the series has landed into its source branch but remains open and that cleanup
is deliberately not pending. No new `WorktreePhase` member was added: `WorktreePhase` is a closed
`Literal` in `models/worktree.py` mirrored by the dashboard at five files / six sites —
`EngineRoom.tsx:59-66` (`LIFECYCLE_PHASES`, `"integration-pending"` at `:63`), `BootTimeline.tsx:88`
and `:110`, `useEngineTimeline.ts:41`, `buildEngineRoomModel.ts:16` (`PHASE_ORDER`) and
`geometry.ts:218` (`LANDING_PHASES`) — so a new member would be a cross-codebase change, and
`worktree-started` is the honest phase for a series that is still working — the summary carries the
checkpoint truth. The full list is maintained in the `guidance.py` card. Before this branch existed
the contract fell through to the pre-integration
`integration-pending` phase, which points at `worktree_integrate`, a tool that refuses while the
series is open.

The pull-request landing route keeps the same guarantee from its side: `record_landing.py`'s
`already-recorded` short-circuit now covers `{"completed", "checkpointed"}`, so a checkpointed series
cannot be re-recorded into `completed` + `cleanup="pending"` — the state `worktree_cleanup` requires.
Completion still travels through `worktree_integrate`, which reaches it only once the series is
genuinely terminal.

## Update History
- 2026-09-12T05:05+02:00 — 260831-LOCR-L30 mirror-list completeness: the checkpoint projection note
  named three dashboard mirrors of `WorktreePhase` where there are six; it now lists all five files /
  six sites and defers to the `guidance.py` card as the maintained list. Content change, not a range
  repoint; verification metadata remains closeout-owned.
- 2026-09-12T04:10+02:00 — 260831-LOCR-L30 follow-up: replaced the recorded checkpoint guidance gap
  with the implemented behavior — `_post_integration_phase` now has a `checkpointed` branch projecting
  `worktree-started` + `continue_work`/`worktree_status`, with the closed-`WorktreePhase` rationale —
  and recorded the widened `already-recorded` guard on the pull-request route. Verification metadata
  remains closeout-owned; no acceptance claim.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: recorded the non-final series exit on this route,
  the single-writer cell that now carries two landing outcomes, the widened series abandon guard, and
  the guidance phase gap for `checkpointed`. Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-11T23:05:00+00:00: Route-impact curation for this route: recorded the new `record_landing_result` facade export and shared landed-integration writer, the terminal-task-state requirement for integration-branch retirement with its cleanup/abandon asymmetry, and the named abandoned-master closeout refusal. Content change, not a range repoint.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `SyncOperationStore`, `activate_atomic_series_contract`, `observe_sync_operation`, `reconcile_selected_series_under_authority` repointed to mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:103-121, mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:55-100, mcp/src/agents_remember/worktrees/sync_transaction_state.py:172-366, mcp/src/agents_remember/worktrees/sync_transaction_state.py:369-385. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: repaired the exact-pair resolver reference, which now lives at `memory_quality/memory_candidate_pair.py` after commit `0b63d6fc` relocated it out of `closeout/`. Only this cut-affected claim was reconciled; the rest of this route was not re-read in this pass, so verification metadata remains pinned. Source documentation only; no acceptance or certification claim.
- 2026-09-10T15:06+02:00 — No content impact: mechanical citation re-derivation of pre-existing stale anchors in this route overview against the current working tree; the cited symbols and route meaning are unchanged.
- 2026-09-10T15:06+02:00 — Closeout auto-carry and parked candidate: recorded that the sync transaction parks and returns a dirty moving side's candidate (park, journal, restore on completed/resume/cancel, finalize refusal), and that the closeout-family lineage guard self-heals a settleable stale break through that transaction. Re-derived the sync anchors against the current working tree. Verification metadata remains closeout-owned.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-10T02:27:58+02:00 — CCR-L42 parity curation: No route impact: curator preparation and closeout now run the shared sidecar and route body/history validators independently; this route's ownership and source semantics remain unchanged. No acceptance claim is made.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ01 preparation rebound the worktrees overview's activation observer citations to current source ranges; source-pair ownership is unchanged and no acceptance claim is made.
- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: recorded the route-review refusal projection and activation/admission observation boundaries under the worktrees route. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.

- 2026-09-06T21:58:28+00:00 — Reconciled this route against the source delta from `245057ab16e19afdaabd5c188c9576b22e0c0870` to `d36109038b3f2b500c138f9dc1ea9c9f9a247489`. Updated current ownership and policy claims; prior verification commit/date and history remain unchanged. Source inspection only; no test, review or acceptance claim.


- 2026-09-06T13:51:59+00:00 — L33 candidate curation: Routed canonical task observation and selected certification through the existing service/integration owners; distinguished implemented admission/execution from absent default continuation. Reviewed uncommitted source; prior verification commit/date remain unchanged. This is source documentation, not gate or acceptance evidence.


- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:23+00:00 — L30 route-impact review against `6e4ab81f6ae52bce35003377bb3aec7877554ed7`: Reviewed the seven changed child quality sources; routed the new publication and host-lock behavior without changing lifecycle or source-pair ownership.

- 2026-09-05T07:14+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Corrected scheduling independence versus publication locking and added current intent/certification composition. Verification records source review, not execution or acceptance.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: unified lifecycle and semantic-topology leaf
  identity on the canonical composite task-domain binding. Verification remains closeout-owned.

- 2026-08-31T20:30+02:00 — 260831-DER: restored the ordinary series no-door integration state and
  recorded the strict separation from policy-gated leaf-without-enclosure direct landing. Existing
  leaf door and retained-journal recovery boundaries remain unchanged.

- 2026-08-31T12:27+02:00 — No route impact: A005 changes only the already-documented quality
  executor and publication child route; the root worktree ownership, lifecycle boundaries, and
  hot-path routing remain unchanged. Verification remains closeout-owned.

- 2026-08-29T21:46+02:00 — MCAR-L03: added the canonical exact code/memory pair resolver to the
  worktree route. Verification remains closeout-owned.

- 2026-08-29T12:52+02:00 — MCAR-L02 C009 recovery: recorded the invocation-owned
  candidate-index boundary after queue and dashboard observers exposed a shared-scratch deletion
  race. Verification remains closeout-owned.

- 2026-08-29T10:40+02:00 — Moved the exact future-code candidate identity into
  `integration/closeout/`, its consuming lifecycle boundary, to restore the root package cap.

- 2026-08-29T08:52+02:00 — Added the structured curator-coherence child route and shared
  admission boundary. Verification remains closeout-owned.

- 2026-08-29T05:17+02:00 — A003 self-review repair: recorded immutable identity and
  collision-free concurrent candidate observations.

- 2026-08-29T04:55+02:00 — Added the strict future-code candidate owner and documented the
  separation between tree-bound semantic acceptance and journal-bound Git-operation recovery.
  Verification metadata remains pinned until closeout.

- 2026-08-28T14:15+02:00 — PDLS closeout: re-read the accepted quality-gate and integration
  changes against the landed candidate. Existing route ownership already places test authority in
  the quality owner and recovery evidence in the root journal; stamped committed provenance.

- 2026-08-26T19:34+02:00 — Reconciled the master-series bootstrap handoff at the parent route:
  apply-time journal/contract observation shares the existing per-master mutex, while dry-run
  remains unlocked and write-free. This closes the concurrent split read without a retry, fallback
  reader, compatibility route, or new lock namespace.

- 2026-08-26T14:32+02:00 — Corrected source-pair sync's ledger boundary from global code-key
  uniqueness to newest-first current authority plus exact parent-history preservation.

- 2026-08-26T08:55+02:00 — Promoted the activation and sync units from provisional to frozen
  covered status after pass 13.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of 5 activation package units, 7 root
  sync units, and their queue/module/integration boundaries; commit-derived stamps remain
  closeout-owned.

- 2026-08-26T06:25+02:00 — Reconciled current coverage after the consolidation: five activation
  package units and seven root sync units have strict provisional sidecars; final citations and
  verification remain post-Dagger owned.

- 2026-08-26T06:05+02:00 — Reconciled the structural-limit move: activation is now one focused
  child route with five strict sidecars, while resumable sync remains at the worktrees root. No
  compatibility readers or old-path cards remain.

- 2026-08-26T02:55+02:00 — Created for the direct IAS source-pair coordination repair. Recorded
  approved activation, resumable-sync, task-authoring, queue-ownership, cleanup, and no-fallback
  boundaries against the moving candidate; verification remains frozen-candidate owned.
