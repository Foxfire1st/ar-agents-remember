# mcp/src/agents_remember/worktrees

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-15T00:56:17+00:00 |
| lastVerifiedCommitHash | `67b21aeb66df96a971a33ae431a13992f2528b45` |
| lastVerifiedCommitDate | 2026-09-15T06:37:48+02:00|
| reviewedWorkingCandidate | `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## What This Area Is

This route owns the durable worktree-enclosure and protected-source coordination primitives beneath
the public lifecycle modules. The current architecture adds two related but distinct owners:
contract-scoped atomic-series activation decides whether each live master may expose implementation
work, while a contract-addressed sync transaction reconciles code and external-memory sources
without depending on a readable task document for its in-flight journal. Scheduling itself carries no
cross-master exclusion: a graph-less sprint's `atomic-sequential` default describes the sprint's
shape — every commanded master executes atomically — and serializes nothing, because such a sprint
declares no dependencies, and per-contract activation never pauses or excludes a sibling.
Since 260831-LOCR-L37 the route also owns the **stop**: `modules/pause.py` releases one master's
activation selection, publishes nothing, and hands the turn back.

## Hot Path Summary

`series_closeout.py`, integration admission and synchronization use exact code/memory history. `ledger_projection.py` and `named_ref_memory.py` retain the consumer read surface, derived solely from committed attribution. Closeout and landing produce at most code plus one memory-content output; cache availability cannot gate them.

## Detailed Route Context

`activation/atomic_series_activation.py` is the single disposable selection authority, keyed per
series contract by `contract_fingerprint`; its release and terminal siblings own exact vacancy. The
selecting transaction publishes `reconciling`, runs exact source sync, and publishes `active` only
after both required bases are current. Two sprint-commanded masters that share one protected source
pair therefore hold independent records, and neither one's state is the other's reason to wait; the
graph-less `atomic-sequential` default adds no dependency between them and serializes nothing.
Root-level `sync_transaction.py` drives the journaled state machine; focused state, authority, Git,
recovery, result, and source-refresh modules own their respective proof and response boundaries.

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
The activation owner likewise exposes per-contract observations and bounded admission evidence while
leaving selector and sync mutation in their existing transaction owners.

## L30 Quality Publication Boundary

The child `modules/quality` route retains actual rail evidence and immutable selected certificate generations. Its host Dagger registry uses the neutral kernel file lock while checkout durable stores preserve their coordination guard. L33 composes journal-selected admission, original certificate readback and suffix execution through the existing lifecycle owners. Gate-5 observation/execution and finalization remain explicit continuation capabilities; the default application bundle installs `PreparedCloseoutContinuation`. See [the modules overview](modules/overview.md) for read/export/prune owners and [the integration overview](integration/overview.md) for operation-selected execution.

`services.py` is the downward service boundary for provider, citation and memory work. Its canonical task-observation method and separate memory/finalization continuation avoid imports from worktrees into higher-level memory implementations. Read [the service card](services.py.md) for explicit binding and absent-capability behavior.

## What Belongs Here

| Path | Role |
| --- | --- |
| `activation/` | contract-scoped selector, selecting transaction, exact release, and terminal bridge |
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

- One `contract_fingerprint`-addressed activation record per series contract, so masters that share
  one protected source pair stay independent.
- `vacant`, `reconciling`, and `active` selector states; `unreadable` is an observation, not a
  selectable state.
- One stable `.lifecycle/sync-operation.json` record per worktree enclosure plus pinned
  `refs/agents-remember/sync/...` authority on participating repositories.
- Separate code and memory side records with admitted base/source/pre-sync heads, plan, retained
  conflict set, and exact result head.

## Operating Model

1. A selecting public start/attach/dispatch or sync operation identifies one canonical series
   contract and derives its normalized code/memory source pair.
2. Selection atomically replaces this contract's own activation record with this master in
   `reconciling`. Another contract's record is untouched, and only this contract's reconciling
   state makes it wait.
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
6. Atomic implementation becomes visible only after exact current bases are proven and this
   contract's selection advances to `active`.
7. Terminal cleanup attempts to vacate only this exact contract's own record. A missing, unreadable,
   vacant, or non-matching record is preserved and cannot be cleared by another master.
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
3. Publish this contract's exact selection as `reconciling` in its own fingerprinted record.
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
| `activation/atomic_series_activation.py` | selector store | single per-contract activation authority and strict observation | covered |
| `activation/atomic_series_activation_release.py` | selector transition | exact cancellation and terminal vacancy | covered |
| `activation/atomic_series_activation_transaction.py` | admission state machine | binds selection to exact sync-before-exposure | covered |
| `activation/atomic_series_activation_terminal.py` | terminal bridge | releases only this exact contract's record | covered |
| `modules/pause.py` | stop-only pause | the developer's stop verb: releases this contract's selection, publishes nothing, proposes no next call | covered |
| `sync_source_refresh.py` | pre-lock evidence | shared bounded upstream refresh without local authority | covered |
| `sync_transaction.py` | transaction driver | public start/resume/continue/cancel routing | covered |
| `sync_transaction_state.py` | stable journal | state survives task/contract readability failures | covered |
| `sync_transaction_authority.py` | identity/admission | pins exact code and memory source refs and admits their Git history | covered |
| `sync_transaction_git.py` | Git proof | retains conflicts and proves exact operation-created history | covered |
| `sync_transaction_recovery.py` | finalization/recovery | terminal publication, rollback, and malformed/missing journal escape | covered |
| `sync_transaction_results.py` | public evidence | consistent previews, conflict guidance, and terminal replay | covered |

## Local Invariants And Traps

- Task authoring is upstream of scheduling and selection; neither activation nor queue state
  may veto it. Its exact source publication still uses the canonical task-publication lock.
- The activation snapshot is disposable per-contract selection, not a lifecycle journal or
  retirement record; `reconciling` is the only waiting reason, and vacant/active records are normal
  rather than waits.
- Multiple live series contracts for one protected source pair are normal, and each owns its own
  activation record. Selecting one master neither pauses, deletes, nor terminalizes another.
- A graph-less sprint carries no serialization authority: `atomic-sequential` describes the sprint's
  shape (every commanded master executes atomically) and declares no dependency, so nothing
  serializes its masters. Source-pair wording on this route belongs to the sync/integration plane,
  which genuinely remains per pair.
- Sync owns lifecycle evidence in the stable enclosure-root journal and Git refs; the queue owns
  none of it.
- Normal readers never infer selection or sync state from legacy files, task text, queue rows, or
  ambient Git. Missing/corrupt authority fails closed and is repaired only by explicit bounded
  selection/cancellation paths.
- Code and memory refs, substantive trees, ancestry and admitted operation identity decide Git mutations. A consumer ledger is computed from memory commit attribution and never supplies a missing Git proof.
- `read_ledger_source` derives rows only from reachable `Code-Commit:` trailers; it does not union the cached table into history. Missing or malformed cached bytes are a cache miss. Invalid code attributions are reported by the reader, separately from transaction admission.
- Memory candidate/status/index comparisons exclude root `memory.md`; code repositories keep their ordinary file semantics. Real content conflicts, branch movement, source ancestry and compare-and-swap publication checks remain enforced.
- Cleanup may release only an exact selected terminal contract and must do so before deleting the
  canonical contract pointer needed to prove identity.
- **The stop is not a publication (260831-LOCR-L37), and a master is not sealed by its own landing
  (260831-LOCR seal removal).** The pause releases this contract's activation selection — or reports
  `atomic-series-already-vacant` when it holds none — and writes nothing else; it moves no ref,
  creates no commit, lands nothing, writes no ledger row and advances no unstarted leaf, and the result
  proposes no continued execution. Publishing a partial master is the separate
  `worktree_checkpoint_landing` route, which lands refs under explicitly required developer approval.
  The two must never be presented or reached as each other. No closeout, integration or cleanup cell
  refuses a leaf either: the deleted `atomic_series_seal.py` predicate that read those cells as a
  child-admission seal is gone, so a master that took a checkpoint landing
  (`integration_status="checkpointed"`) still admits the next leaf.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Task observation and memory/finalization continuation use explicit service ports. | `MemoryQualityPort`; `CertificationContinuationPort`; `WorktreeServices` | mcp/src/agents_remember/worktrees/services.py:111-128; mcp/src/agents_remember/worktrees/services.py:131-141; mcp/src/agents_remember/worktrees/services.py:144-151 |
| The activation record is a strict per-contract fingerprinted snapshot with explicit selection states. | `AtomicSeriesActivationRecord`; `AtomicSeriesActivationArchiveEvidence` | mcp/src/agents_remember/models/structural/atomic_series_activation.py:16-27; mcp/src/agents_remember/models/structural/atomic_series_activation.py:30-45 |
| The route's stop: release this contract's selection, refuse a non-series contract, report a released master as `paused` or a master that held no selection as `atomic-series-already-vacant`, and propose no next call in either success. | `pause_result`; `_already_stopped_result`; `_already_vacant_payload`; `_paused_payload`; `_refusal_payload` | mcp/src/agents_remember/worktrees/modules/pause.py:80-128; mcp/src/agents_remember/worktrees/modules/pause.py:131-151; mcp/src/agents_remember/worktrees/modules/pause.py:153-171; mcp/src/agents_remember/worktrees/modules/pause.py:173-191; mcp/src/agents_remember/worktrees/modules/pause.py:193-209 |
| The child-admission seal is deleted: the parent-series helper is now resolution only and no lifecycle cell refuses a leaf. | `require_parent_series` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:309-330 |
| The stop cannot reach a publication, asserted structurally over the module's import closure. | `PUBLICATION_MODULES`; `test_the_pause_cannot_reach_any_publication_module` | mcp/tests/test_pause_is_not_publication.py:37-52; mcp/tests/test_pause_is_not_publication.py:165-202 |
| Selection observation treats absence as vacant and refuses a record that is not this exact contract rather than inferring from task or queue state; the record address is the contract's own digest. | `observe_atomic_series`; `_require_record_identity`; "def contract_fingerprint("; "def activation_path(" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:145-152; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:360-372; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-134; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:137-142 |
| Selecting admission publishes reconciling, delegates exact sync, and publishes active only after the current source pair is proven; the public admission explanation stays contract-grounded and never names a foreign master as a precondition. | `activate_atomic_series_contract`; `reconcile_selected_series_under_authority`; "def atomic_series_admission_projection(" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:55-100; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:103-121; mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:33-74 |
| The stable journal lives at `.lifecycle/sync-operation.json` and projects recovery without reading task text. | `SyncOperationStore`; `observe_sync_operation` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:172-366; mcp/src/agents_remember/worktrees/sync_transaction_state.py:369-385 |
| The sync driver retains conflicts for continuation and exposes explicit cancellation. | `sync_contract_under_authority`; `_continue_resolution` | mcp/src/agents_remember/worktrees/sync_transaction.py:82-110; mcp/src/agents_remember/worktrees/sync_transaction.py:540-571 |
| Cancellation restores only operation-owned heads; malformed or missing journals recover only through explicit pinned-ref proof. | `cancel_sync`; `recover_unreadable_journal`; `recover_missing_journal` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:159-190; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:193-263; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:266-283 |
| Every sync proof is Git state — the admitted head, the already-current decision, the staged resolution, and the completed branch — and none of them reads a ledger row list. | `_finish_staged_memory_merge`; `_already_current_result`; `_require_completed_branches` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:304-326; mcp/src/agents_remember/worktrees/sync_transaction.py:336-362; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:516-536 |
| A mid-flight selection reports the stuck contract and both exits, and a succeeding pass beside it never reports its own success state. | `_reconciling_result`; `_mid_flight_summary` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:280-294; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:297-335 |

Current working-candidate evidence for this route:

| Finding | Citations | Source Path |
| --- | --- | --- |
| Checkpoint captures the current code and memory branch tips without a ledger mapping prerequisite. | L104-L122 | [mcp/src/agents_remember/worktrees/series_closeout.py](mcp/src/agents_remember/worktrees/series_closeout.py) |
| Consumer source rows are derived only from Git attribution. | L222-L249 | [mcp/src/agents_remember/worktrees/ledger_projection.py](mcp/src/agents_remember/worktrees/ledger_projection.py) |
| Real memory source ancestry remains a landing requirement. | L235-L250 | [mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py](mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py) |

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
| `modules/pause.py` | [`modules/pause.py.md`](modules/pause.py.md) | covered | the stop-only pause: release one selection, publish nothing |
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
| [`activation/overview.md`](activation/overview.md) | contract-scoped selector, reconciliation-bound admission, and exact vacancy |
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

## 260913-LCA-L5 Missing Master Link Refuses By Name

`task_leaf_binding.py`'s `require_current_leaf_enclosure_binding` reads the enclosure-registration
plan's state and, when the plan carries a candidate in state `master-link-missing`, raises
`TaskLeafBindingError` with status `task-enclosure-binding-master-link-missing` and the route that
actually binds the field — re-run `worktree_start`/`worktree_attach` so the start binding publisher
writes `seriesContractPath`, then retry closeout. It deliberately does not reuse the `mismatched`
recovery (`task_doc.replace` against the exact leaf contract), which could not have written a derived
field.

This is a real behaviour change on the route, and an intended one: a leaf document with an exact
enclosure address but no `seriesContractPath` used to read as `present` and pass silently, so closeout
would proceed on a document whose master link was never bound. Two shared closeout fixtures
(`test_closeout_queue._leaf`, `test_transaction_only_worktree_delivery._bind_task_without_review`) had
been modelling exactly that damage state and now bind the field. The publisher that repairs the
document is `plan_leaf_doc_enclosure_registration` in the task route, reached from
`_publish_leaf_task_enclosure_binding`; the worktrees route only names it.

The same change set also moved this route's task-layout path vocabulary down a layer:
`task_resolver.py` no longer defines `series-contract.md`, `0_archive`, `enclosures/`, `slugify`, the two
path builders or the two predicates — it imports them from the new `tasks/task_paths.py` and re-exports
them under an explicit `__all__`, so `layers.toml`'s `tasks`(9) < `worktrees`(10) order holds and every
existing caller is unchanged. What this route still owns in that module is task-name resolution,
active-series discovery, leaf-enclosure contract resolution and root-task archival.

## 260831-CCR-L01 Shared Leaf Identity Boundary

`task_leaf_binding.py` now delegates row/source identity to the pure task-domain
`tasks/leaf_binding.py` owner used by semantic topology. Lifecycle start/discard and closeout
topology therefore require the same composite facts: exact parent row number and file, canonical
direct-child JSON ref, repository/directory, child id, and stem. Stem-only or split identities fail
with typed status/detail; no worktree-local fallback remains.


## Integrated IAS Recovery Contract

The default application bundle installs `PreparedCloseoutContinuation`, composing the memory-certification producer and prepared finalizer through the existing downward port. The closeout child owns resumption of selected private outputs and original code/memory publication. Per-contract activation selection, synchronization and coordinator isolation remain; the ledger is a disposable consumer cache; an absent capability in an incomplete custom composition still refuses.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.


## CCR-R12@v5 Current Worktree Delivery Boundary

Worktree delivery preserves exact task/contract/source identity, explicit approval and handover
controls, leases, recovery evidence, and protected ref safety. Normal closeout commits code,
mechanically refreshes and commits substantive external memory when needed, then refreshes its consumer cache; normal integration
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
keeps every authority that protects other owners' refs and drops only the completion assumptions the
final series route proves; it refuses an already-`Completed` master
(`atomic-series-checkpoint-master-complete`), so a checkpoint can never downgrade a finished
integration. **The L30 text below is superseded by the L34 section above**: the `checkpoint` flag it
describes is now the `CheckpointLanding` value carrying the route's own captured refs, and the
closeout requirement L30 silently also demanded is now stated and evaluated on the preview too.
`modules/landing_record.py::record_landed_integration` still writes either `checkpointed` (cleanup
untouched) or `completed` + `cleanup="pending"` from that route's landing shape, so the terminal
`integration` cell still has exactly one writer. The facade re-exports `checkpoint_landing_result`,
and the public `worktree_checkpoint_landing` tool exposes it.

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

## Historical milestone context: Route Impact: Preview/Apply Parity And The Checkpoint Reachability Repair (260831-LOCR-L34)

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

**The invariant: a preview that plans an operation does not enforce it, and the two surfaces must be
maintained as one.** A dry run is read as a promise — by a human deciding what to do next and by an
agent composing the next call — but it is only a *plan*. When the preview and the apply are two
implementations of the same eligibility decision, the plan can promise an operation the apply will
refuse, and nothing in the system notices. Six instances were found, **every one of them by
exercising an operation rather than by reading it**, plus one adjacent shape.

### The instance inventory

| # | Surface | The divergence | Status |
| --- | --- | --- | --- |
| 1 | series **closeout** | `closeout_preview_payload` answered `would-closeout` while the apply refused on master completion — 19 blockers on LOCR. This is the original, and it misled a human into writing a false note. | **Fixed** (L34): the gate is `series_closeout.require_closeout_publication_authority`, one definition with two callers. |
| 2 | `worktree_checkpoint_landing` | preview vs apply eligibility were computed separately. | **Fixed** (L34): both read `checkpoint_landing_eligibility` / `CheckpointLanding`. |
| 3 | `integration-ref-race` payload | `nextTool` was the hardcoded literal `"worktree_integrate"`, so a checkpoint losing the compare-and-swap told the operator to re-run the **wrong tool**. | **Fixed** (L34): `_publish_integration_edge` takes a required `operation` name threaded from the route. |
| 4 | the checkpoint's ledger projection | the preview said `would-checkpoint`; the apply refused on the projection. | **Fixed** (L34): `_require_ledger_projection` runs before the dry-run branch. |
| 5 | the ordinary `worktree_integrate` dry run | it did not evaluate the ledger projection at all. | **Fixed** (L34): the same shared call covers both routes. |
| 6 | `worktree_start` | its dry run skips `require_current_start_task_binding` and `require_current_leaf_enclosure_binding`. | **Reported, not fixed.** This is deliberately a reservation compare-and-swap, **not safely separable** into a preview-side evaluation; recorded with that reasoning so it is not "fixed" blindly. |
| 7 | `memory_carryover_plan` / `memory_carryover_apply` | the plan evaluates its own authority while the apply additionally enforces `require_ordinary_repository_checkout` and `ensure_clean`. | **Reported, not fixed.** Outside this leaf. |
| — | `worktree_abandon` / `worktree_cleanup` | an **adjacent shape**: the gate IS evaluated on the dry run and blockers *are* reported, but the dry run returns `ok=true, state="would-abandon"` / `"would-cleanup"` where the apply returns `ok=false, state="abandon-blocked"` / `"blocked"`; `worktree_cleanup`'s summary is also generic and does not mention the blockers, unlike abandon's. | **Reported, not fixed.** A verdict/state-string difference, not a missing evaluation, on two routes outside this leaf; turning them into refusals is a public state-vocabulary change. |

Instances 1-5 are fixed in this leaf; 6, 7 and the adjacent shape are recorded so the next reader has
the inventory instead of rediscovering it one operation at a time. This matters especially because the
planned ledger migration is a bulk mechanical pass over exactly these surfaces.

### What L34 changed on this route

The checkpoint route written by L30 was **unreachable in both directions**: it required
`closeout_status == "completed"`, while the only operation producing that cell (the series closeout)
requires the master complete and every atomic leaf landed, and the checkpoint in turn refused an
already-`Completed` master. L30's own note admitted the real ref move was never proven end to end,
which is how it survived.

- `worktrees/series_closeout.py` gained `SeriesCheckpointRefs` / `capture_series_checkpoint_refs`
  (the live code and memory work-branch tips plus their proved ledger mapping, proved through
  `exact_series_memory_closeout`, the exact-mapping reader) and `require_series_checkpoint_authority`
  (the master-complete refusal, one definition with two callers). `publish_series_checkpoint_under_authority`
  now **requires** `expected` and revalidates it against the live tips at publication
  (`atomic-series-checkpoint-candidate-moved`), so a candidate that moves between preview and apply
  refuses instead of landing a pair the preview never showed. This route is a partial **publication**,
  not a pause: the ref move puts the master's committed line on the protected source branch under
  explicit developer approval, while pausing a master publishes nothing and moves no ref
  (260831-LOCR-L36).
- `worktrees/modules/integrate.py` gained `CheckpointLanding` and
  `checkpoint_landing_eligibility` — **the ONE eligibility decision both the preview and the apply
  read** — plus `_checkpoint_dry_run_result`, the shared `_require_ledger_projection`, `_route_commits`,
  `_landing_admission`, and the required `operation` name on `_publish_integration_edge`. The
  checkpoint path no longer calls `validate_integrate_contract`, whose series arm is byte-identical to
  the two ref-shape checks the capture already makes.
- `worktrees/integration/integration_ref_transaction.py` gained `LandingAdmission` in place of a
  single keyword-only prefix argument, and `_require_preserved_ledger_history` took the leaf
  **projection** form for an unfinished master — a smaller promise, not a dropped one, because the
  completed leaf-chain census is exactly one of the completion facts the checkpoint route does not
  require. **Both that function and `LandingAdmission.expected_series_ledger_prefix` were removed by
  260913-LCA-L11** (see the L11 section below), so this paragraph records the L34 shape as history.
  The transaction's own boundary read remains authoritative, re-taken under the transaction
  immediately before the irreversible ref move.
- `worktrees/modules/closeout.py`'s `closeout_preview_payload` now calls the extracted
  `require_closeout_publication_authority`, closing instance 1 (see the `closeout.py` card).
- `models/worktree.py`'s `NextTool` gained `worktree_checkpoint_landing`; `NextOperation` was
  deliberately not widened (see the `models/worktree.py` card).
- `application/worktree_tools.py` and `mcp/registration/closeout.py` corrected the published
  docstrings, which had described the route as dropping only two of the three completion assumptions
  — a client-facing promise that was false.

### Where this is tested

The new `mcp/tests/test_checkpoint_landing_end_to_end.py` (integration lane) drives the **public**
operations over real temporary Git repositories: an unfinished master with `closeout_status` still
`not-started` checkpoints end to end (both destination refs and the ledger verified), retry is
idempotent, continued work advances the refs again, a hand-edited ledger is refused at **both**
surfaces, a divergent ledger on the ordinary leaf route is refused at **both** surfaces, the ref race
names the checkpoint as the tool to re-run, and the closeout preview/apply parity case. See its card
for the recorded `UNREPRODUCED FLAKE` note above
`test_checkpoint_landing_requires_explicit_developer_approval`.

## Route Impact: Stop-Only Pause (260831-LOCR-L37)

This route gained the developer's **stop**. `worktrees/modules/pause.py::pause_result` is the entire
route: it asserts the addressed contract is the one it was given, refuses any contract whose `kind` is
not `series` (`pause-requires-atomic-master` — an ordinary leaf owns no selection of its own), delegates
the actual release to the existing `release_atomic_series_selection` authority, and returns a payload
whose `state`/`status` are `paused`, whose `paused` is `True`, whose `atomicSeriesActivation` echoes the
released record, and whose `nextStep` carries a summary and **no** `nextTool`/`nextArgs`/`nextOperation`.
The application entry point, payload builder, registrar declaration, `PUBLIC_TOOLS` entry and
`WorktreePauseResponse` row are its five public edges; `git_worktree_manager` re-exports `pause_result`
so the stop reaches the route through the same stable facade as its siblings.

**Why the boundary is the feature.** The activation selection is the one durable fact that says this
master is the one exposing implementation work, so releasing it is what makes the stop real — marking
the master without releasing it would stop nothing. And because the record is addressed per contract by
`activation_path(...)`, releasing one master leaves every other master's record byte-identical: the
pause cannot make a sibling ineligible, and the retired cross-master waiting vocabulary has nothing to
say about it.

**The pause cannot publish, and that is structural.** `modules/pause.py` imports and calls none of the
integration, landing, closeout or ledger planes and runs no Git; the activation snapshot it writes while
releasing is its one legitimate write and is not a publication. `mcp/tests/test_pause_is_not_publication.py`
builds the module's static source-level import graph and asserts it is disjoint from all twelve
publication modules. Measured on this candidate: the closure holds **60** modules including the root,
the pause's **5** direct imports, **54** modules beyond them, and **0 of 12** publication modules; the
case adds non-vacuity checks and named witnesses so a walker that stopped at the direct imports would
fail instead of pass. The guard is a static AST reading — dynamic imports are not followed and it is
per-module rather than process-wide, which the test states and which a future reader must not read as
completeness. See that test's card.

**The checkpoint is the separate publication, and L30/L34's route is untouched by this leaf.**
`worktree_checkpoint_landing` still lands a partial master's accumulated line onto its super branch under
explicit developer approval and records `checkpointed`. The pause must never be routed through it, and
no pause surface may describe it as the pause. Its registered description already says it is a
publication and denies being the pause (L36); L37 adds the stop the description points at.

`mcp/tests/test_pause_stop_only_end_to_end.py` (integration lane) is the boundary proof over one real
temporary Git world holding two atomic masters: it measures both repositories' refs and complete object
databases, the coordination tree, both worktrees and every task document before and after the public
pause, and covers the hand-back payload, the already-stopped success a never-selected master produces,
the leaf and foreign-record refusals, leave-idempotence, per-contract record isolation and resume.

## Route Impact: Child-Admission Seal Removal And The Already-Vacant Stop (260831-LOCR)

**The seal is deleted, and a master is no longer locked by its own landing.** L37 added a test in its
own boundary suite. This pass removed the guard it revealed:
`mcp/src/agents_remember/worktrees/atomic_series_seal.py` (the whole module, including its zero-caller
`require_series_path_accepting_leaves`) was the "one irreversible child-admission seal for an atomic
series". `require_series_accepting_leaves` refused a new or reopened atomic child leaf whenever the
parent series' `(closeout_status, integration_status, cleanup)` was not
`("not-started", "not-started", "pending")`. When `checkpointed` joined the integration vocabulary,
that same predicate also sealed every master that took a checkpoint landing — so after its first
landing a master could never admit another leaf, and a paused master was a dead master. The developer
ruled the seal out entirely: a master is meant to be paused and resumed, never locked by its own
landing. Its call sites in `start_contract.py` (`ensure_master_series_contract`'s dry-run and locked
apply arms, and `_parent_series_contract`), `start.py`, `reopen.py` and
`integration_branch_authority.py` are gone; the helper formerly named
`require_parent_series_accepting_leaves` is now `require_parent_series` and resolves and validates the
exact parent series without deciding whether it accepts leaves. `leaf_admission_operation` survives as
the refusal label.

**The pause now succeeds when the master holds no selection.** `worktrees/modules/pause.py` answers
`atomic-series-activation-selection-missing` itself: after `observe_atomic_series` confirms the record
is `vacant` (the ordinary state of a master between landings, and the state a release leaves behind),
it returns `state`/`status` `atomic-series-already-vacant`, `paused: true`, the same stop next step,
and publishes nothing — explicitly, never silently. An unreadable record and a record naming another
master stay refusals, because neither proves the master is inactive, and
`release_atomic_series_selection` is unchanged because explicit sync cancellation still requires an
existing exact selection.

**`mcp/tests/test_lifecycle_playthrough_end_to_end.py` (integration lane) is the regression proof.**
It plays the lifecycle in order on one real temporary Git world — master open and unselected → leaf
commanded and started → leaf closed out → leaf landed through the public `worktree_integrate` →
unfinished master checkpointed through the public `worktree_checkpoint_landing` → master paused through
the public `worktree_pause` with both repositories' ref maps unchanged → master resumed through the
ordinary attach route → a leaf commanded *after* the landing still starts on a new base. Step 8 is the
regression: no single-boundary case could have seen it, because every operation was correct on its
own. Leaf start and closeout use the fixture's structural equivalents, which the module docstring
states; the master-level beats are the registered tools.

## Historical milestone context: Route Impact: The Ledger's Source Is The Attribution (260913-LCA-L2)

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

`ledger_projection.read_ledger_source` no longer reads the complete source ledger out of the blob at
`commit:memory.md` alone. It merges two records: the new kernel module
`mcp/src/agents_remember/kernel/memory_attribution.py` walks the whole ancestry from the exact source
commit it is given and turns every `Code-Commit:` trailer into one row, and the reader separately
takes the rows **that commit's own table recorded**, keeping the table's order and each mapping once.
The reader's original L2 form returned the trailers *alone* as soon as the history carried a single
one, which made the blob reachable only for a history with no trailer at all; **260913-LCA-L11
corrected that** and made the union the rule, with a row the exact source commit cannot prove
excluded at the read and reported with its reason rather than dropped in silence. A source that
resolves and carries neither record contributes no rows, which is the bootstrap state the
ledger-creation paths start from; a history that cannot be walked and a blob that exists and cannot
be parsed both still refuse with their remedy. `ledger_projection.code_commit_exists` is a delegation
to the attribution module's single `cat-file -e` definition rather than a second copy of that test.

**The walk is the whole ancestry because a memory line merges.** Measured on the real memory
repository at tip `5e4899ea` with `git merge-base --is-ancestor` (the projection's own truth test,
which resolves object names): the tracked table's 476 rows name 442 memory commits on the tip's
first-parent line and 34 that are not on it, and 21 of those 34 are still ancestors of the tip — so
a first-parent-only walk would silently drop 21 mappings the full walk reaches, which is the
"partial coverage looks like a gap" failure the trailer rule exists to prevent. 463 of the 476 rows
name an ancestor in total (the 442 on the line plus the 21 off it), and the remaining 13 name a
memory commit that is not an ancestor at all; those cannot appear in the projection by its own rules,
which is "a row the history does not carry is not a row" rather than something a hand edit fixes. The
older figures in the module's own docstring — 35 rows off the line, 441 on it, 462 reachable, 14 not —
came from comparing the table's written cells against `git rev-list` output as TEXT; the whole
difference is the table's single truncated memory-commit cell (`684c33b2`), which resolves to a real
ancestor on the first-parent line but never matches a full object name as text.

**What did not change, and must not be described as changed.** The tracked ledger commit is **not**
retired. `memory.md` is still written, committed and proved by this route's closeout family, its
ledger leg is still one of a closeout's three commit legs, and the named-ref readers on this route —
`sync_transaction_authority`, `series_closeout`, `integration_ref_transaction`,
`organizational_completion`, the queue's `closeout_recovery`, and the closeout preparation's
`memory_output` and `finalization` — still read, inject and validate the ledger blob exactly as
before. The ledger commit's tree is built by **injecting the ledger blob as an index entry**
(`preparation/memory_output.py::_ledger_tree` runs
`update-index --add --cacheinfo 100644,<blob>,memory.md` against a temporary index and writes the
tree) rather than by writing a file
someone edits, which is why the tracked form is a commit shape: retiring it means retiring the
ledger-commit leg across worktree closeout, direct landing, queue recovery, series closeout,
integration and sync, and that is a separate leaf of this master, deliberately not half-landed here.

**On the real repository the L2 measurement and the L11 measurement are different states of the same
line, and both are recorded with their method.** At `5e4899ea` the L2 pass measured 0 of the 958
reachable memory commits carrying the trailer, so the projection returned the table's 476 rows
through the blob read. At `f5edc613` (this leaf's memory base) the 260913-LCA-L11 worker measured
that the table records 479 rows of which exactly ONE commit carries a trailer; the curator
re-verified both halves against the official memory repository (`git show f5edc613:memory.md` parsed
as the ledger parser does → 479 data rows; `git log --format=%(trailers:key=Code-Commit,valueonly)
f5edc613` → one non-empty value, `02ed1fbc` trailing `4214d7a1`) and re-derived the read's split with
`git merge-base --is-ancestor` row by row → 466 kept + 13 excluded, the worker's own figures. The
attribution path itself is proved by `mcp/tests/test_memory_ledger.py`'s attributed fixture line, and
making the real history fully carry it is the master's backfill leaf.

## Historical milestone context: Route Impact: The Rebuild Outranks The Ledger File (260913-LCA-L11)

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

**The developer's ruling of 2026-09-14T08:15+02:00, and what this route had to give up for it.** The
integration-side check that enforced "preserve the complete source ledger history: no source row
dropped, reordered or replaced" protected the tracked `memory.md`, and `memory.md` is derived state —
the projection recomputes it from the memory commits' own attribution. A table that differs from the
file it replaced is therefore the *normal* result of a rebuild, not damage, and a rule that refuses it
is a rule that keeps a derived file authoritative. **The rebuild takes priority: the check is removed,
not weakened** — no flag, no opt-out, no compatibility path. The trigger was concrete: leaf L10's
ledger repair reported added 1, removed 13, reordered 455 (479 → 467) and its integration was refused
by that check while naming the 13 missing rows and the ~455 out-of-order ones, even though the start
point was current (the master records memory base `7317108b` and the source branch tip *is*
`7317108b`). The asymmetry settled it: the **checkpoint** route already tolerated merge-produced
interleaving while the **leaf** route did not, so the same table was accepted on one road and refused
on the other. (The master's decision attributes the checkpoint half of that asymmetry to `L35`; this
route's own record attributes the checkpoint's interleaved-projection acceptance to the L34 work
above. The two labels are not reconciled here — what matters is that the asymmetry was real and is
now gone.)

**Removed, across three modules, so no producer is left without a consumer.**
`integration_ref_transaction.py` lost `_require_preserved_ledger_history` (both the series leaf-chain
prefix branch and the projection fixed point), its evidence renderers `_ledger_projection_refusal` /
`_landing_ledger_rule` / `_projection_divergence_evidence` / `_ledger_row_list` / `_ledger_row_text`,
the `_LedgerLanding` carrier, `_integrated_ledger_pair` and its source-blob read, and
`LandingAdmission.expected_series_ledger_prefix`. `series_closeout.py` lost the now-orphaned
`atomic_series_ledger_prefix` with `_reconciled_ledger_prefix` and `_is_reconciliation_row`.
`modules/integrate.py`'s `_landing_admission` no longer takes the contract, because there is no series
ledger prefix left to derive, and `_require_ledger_projection` no longer receives a history form.

**What survives, and it is not nothing.** Four protections the file rule never carried all still fire,
and each was proven by its own mutation: the landed code commit **is** mapped to the landed memory
content (`find_mapping`, so a table naming that commit with different content refuses too); every row
of the landed table is **true** against the two repositories (`_require_true_rows`, naming the
offending row); the landed memory content descends from the exact memory source, now asked exactly
while the source is still behind the landing so an idempotent retry converges; and the header names
its own first row, through a validated read of the landed ledger with its own closeout-re-run remedy.
The final **series closeout's** reconciled-pair recording still requires the landed table to be the
fixed-point projection (`series_closeout._require_series_ledger_projection`) — a different route, on
purpose, and not something this leaf touched.

**The cost is recorded, not hidden.** With the file rule gone, a reordering that moves an OLDER row
above a NEWER one **for the same code commit** can now land, and nothing at the landing reports it:
`find_mapping` resolves the first row naming a commit, so the reversal silently changes what that code
commit resolves to. The landed code commit's own pair is still safe — that is the mapping clause — so
the exposure is every *other* code commit the table names. The worker briefly added a "resolution
preservation" rule, found it refused a correct ledger (re-establishing the file as authority by the
back door), and removed it. This is a **known gap pending a decision**, and no card or comment may
describe it as blocked.

**The rebuilder's second, independent defect — the expensive shape of "no attribution exists".** The
ruling did not name it; the worker found it while reproducing the ruling. `read_ledger_source`
returned the trailers ALONE as soon as the history carried one, so a line whose table records 479 rows
and whose history carries one trailer read as a **one-row source** and every pre-rule row vanished
from its tail. The blob is now the common case and the trailers merge into it; rows the exact source
commit cannot carry are excluded at the read with a recorded reason and operator-visible counts
(`sourceRowsExcluded`, `sourceExcludedRows`, `sourceExcludedReasons`, `sourceTraileredCommits`), and
abbreviated object names are resolved by ancestry rather than string-compared. See the
`ledger_projection.py` card for the measurement and its re-verification.

**Where this is tested.** `mcp/tests/test_checkpoint_landing_end_to_end.py` is the behavioural proof
and three of its cases changed direction: a reordered source region, a reversed superseding pair, and
the interleaved projection on the leaf route all **land** now, each asserting the acceptance (and, for
the leaf case, that the destination refs really moved) rather than dropping the scenario.
`mcp/tests/test_integration_branch_authority.py` carries the clause inventory, including the dropped
and duplicated source rows it now asserts as accepted, and the two new module-level cases that drive
`_require_true_rows` directly. `mcp/tests/test_memory_ledger.py` gained the exclusion case and the
partially-trailered-source case. No new test module was added and none was deleted.

## Historical milestone context: Route Impact: A Dropped Ledger Row Is Reported, Not Refused By The Sync

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

**The same ruling that removed the integration gate removed the sync gate.** The resumable sync
transaction was the file rule's second keeper: a descendant or merged `memory.md` had to contain
every row its source carried, and anything else refused with the state `sync-work-branch-invalid` and
`resolved memory ledger dropped parent mapping(s): ...`. Measured on this master: thirteen
unresolvable rows (eleven stale duplicates whose code commits map to a different memory commit, two
naming memory commits that exist nowhere) had been dropped from the ledger by the master's own
closeouts, so the same rows refused the integration gate and this one, and every later leaf start of
that master refused permanently while both sides were already current — there was no merge left to
resolve and nothing the operator could do. `sync_transaction_git.py` lost
`validate_current_memory_side`, `validate_completed_side`, `_validate_parent_ledgers`,
`_validate_required_ledger_rows` and `_ledger_rows` together with their call sites in
`sync_transaction.py` (`_already_current_result`) and `sync_transaction_recovery.py`
(`_require_completed_branches`), and the refusal state `sync-work-branch-invalid` no longer exists
anywhere in the repository. Every sync proof is now about Git state — the admitted fast-forward or
the exact two-parent commit, and the staged resolution — so both routes answer the same way and no
surface restates the projection's judgement where it can drift from the reasons it classifies.

**A selection left mid-flight now says so.** `_reconciling_result` rewrites a pass that itself
returned `synced` or `already-current` to `atomic-series-reconciling` rather than presenting that
pass's success beside a mid-flight record, and its new `_mid_flight_summary` leads with the stuck
master's task-document ref and contract path, when its record was published, its revision, the
incomplete source reconciliation, and both exits (`worktree_sync(contract_path=..., dry_run=false)`,
or `worktree_sync(..., resolution_action='cancel', dry_run=false)`), keeping the refused pass's own
message last. Before this the only thing said about that state was the refused pass's branch
complaint, which named neither the stuck contract nor what it was doing.

## Update History

- 2026-09-15 — Preserved the following dated pre-takeover review notes from the parent working tree. They describe that earlier candidate; current behavior is documented above. Exact original files and patches are retained in the master cutover report.

- 2026-09-14T23:55+02:00 — 260913-LCA completed-master review follow-up (same uncommitted change set,
  `ar/260913_ledger-commit-attribution`, base `bb65a207`): added the completed-master review's half of
  the ledger exclusion channel to this route's L11 record. The read still decides the memory half of a
  source row and holds no code repository; `project_ledger` now asks the code half of those same rows
  at the one boundary where the code repository is in hand (`_kept_true_source_rows`), excluding with
  `code-commit-missing` any source row the repository cannot prove and reporting it through the same
  `sourceRowsExcluded`/`sourceExcludedRows`/`sourceExcludedReasons` payload. The reviewed defect: the
  rebuild appended the source's rows unchanged, so an invalid source row survived the recompute that
  exists to repair it. Recorded the deliberate widening `LedgerWorld.code_repository: Path | None =
  None` — a world naming no code repository cannot refute a code claim and keeps its rows, where a
  `None` in the previously required field died inside the object test — and the two cases that pin
  both halves. Detail lives on the `worktrees/ledger_projection.py` card and on `mcp/overview.md`.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp
  advanced.

- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Replaced source-table union and ledger-based admission invariants; historical milestone accounts are explicitly superseded. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees` carries local unstaged changes not represented in HEAD.
  Re-read the card against the frozen on-disk source and re-checked its claims and cited ranges:
  nothing this card asserts is falsified by the change, so no wording changed. Verification metadata
  remains closeout-owned; no verification stamp advanced.
- 2026-09-14T13:20+02:00 — A dropped ledger row is reported, not refused by the sync (curator on the
  landed `ab47182` change set of the 260913 ledger line): the sync-side row-preservation rule is
  removed — `validate_current_memory_side`, `validate_completed_side`, `_validate_parent_ledgers`,
  `_validate_required_ledger_rows` and `_ledger_rows`, with their call sites in
  `sync_transaction.py::_already_current_result` and
  `sync_transaction_recovery.py::_require_completed_branches` — so every sync proof is about Git
  state and one answer applies on both routes. Recorded the measured thirteen-row trigger and the
  permanently-unsyncable master it produced, the mid-flight reporting rewrite
  (`_reconciling_result` → `atomic-series-reconciling` with `_mid_flight_summary` naming the stuck
  contract, its publication time, its revision and both exits), and corrected the false local
  invariant that had stated the file rule. Re-derived the sync/activation reference anchors on this
  route. Verification metadata remains closeout-owned; no execution or acceptance claim and no
  verification stamp advanced.
- 2026-09-14T11:58+02:00 — 260913-LCA-L11 route impact (curator, uncommitted change set on
  `ar/260913-lca-l11-ar`, base `4214d7a1`): recorded the developer's 2026-09-14T08:15+02:00 ruling
  that the rebuild outranks the tracked ledger file, and the removal it ordered — the
  ledger-preservation check and its whole surface across `integration_ref_transaction.py` and
  `series_closeout.py`, with `integrate.py`'s admission losing its ledger-history dimension. Stated
  the four surviving promises, the surviving series-closeout projection gate as a different route,
  the measured trigger (L10's 13 dropped / 455 reordered repair refused at a current start point),
  and the asymmetry between the checkpoint and leaf routes that the master's decision attributes to `L35`. Recorded the removal's **cost** — a
  same-code-commit row reversal can now land unreported for any code commit other than the landed
  one, the "resolution preservation" rule that would have closed it refused a correct ledger and was
  removed, and it is a known gap pending a decision. Recorded the rebuilder's second defect and the
  direction of its fix, with both the worker's measurement and this curator's independent
  re-verification (479 rows, 1 trailered commit, 466 kept + 13 excluded at `f5edc613`). Corrected
  the two body passages the change falsifies — the L2 reader paragraph's "fallback" framing and the
  L34 paragraph's `LandingAdmission`/`_require_preserved_ledger_history` account — and added the
  matching local invariant. Verification metadata remains closeout-owned; no execution or acceptance
  claim and no verification stamp advanced.
- 2026-09-14T07:05+02:00 — 260913-LCA-L5 route impact (curator, uncommitted change set on
  `ar/260913-lca-l5-ar`, base `52875e7a`): recorded the new `task-enclosure-binding-master-link-missing`
  refusal on `require_current_leaf_enclosure_binding` — a leaf document with an exact enclosure address
  but no `seriesContractPath` now refuses by name with the start/attach remedy instead of reading as
  `present`, and the reason it does not reuse `mismatched`'s `task_doc.replace` recovery is that a replace
  cannot write a derived field. Stated that two shared closeout fixtures were corrected because they had
  been modelling the damage state, and that the repairing publisher lives on the task route. Also recorded
  that this route's `task_resolver.py` lost ownership of the task-layout path vocabulary to the new
  `tasks/task_paths.py` (it now re-exports it), which is what keeps `layers.toml`'s
  `tasks`(9) < `worktrees`(10) order intact. Route
  documentation only: verification metadata remains closeout-owned and no execution or acceptance claim is
  made.
- 2026-09-13T23:26+02:00 — 260913-LCA-L2 follow-up (same uncommitted change set): corrected the
  ancestry census in the route-impact section below to name its method and carry the full figures —
  `git merge-base --is-ancestor` at tip `5e4899ea` gives 442 rows on the first-parent line, 34 off it,
  21 of those 34 still ancestors, 463 rows naming an ancestor in total and 13 naming none — and
  stated that the module docstring's older 35/441/462/14 figures came from comparing the table's
  written cells against `git rev-list` output as text, the whole difference being the table's single
  truncated memory-commit cell `684c33b2`. No claim about the projection, the fallback or the
  unretired ledger commit changed. Verification metadata remains closeout-owned; no acceptance claim
  and no verification stamp advanced.
- 2026-09-13T23:10+02:00 — 260913-LCA-L2 curator (uncommitted change set on `ar/260913-lca-l2-ar`):
  recorded that this route's source-ledger reader now projects the complete source ledger from the
  memory commits' own `Code-Commit:` attribution through the new `kernel/memory_attribution.py`,
  with the per-commit blob read kept only for a commit whose whole walk attributes nothing; stated
  the measured reason the walk is the full ancestry (476 rows, 442 on the first-parent line, 34 off
  it, 21 of those still ancestors, 13 not ancestors at all), the real-repository state that the
  fallback is the live path at `5e4899ea` (0 of 958 commits trailered), and the boundary the change
  did not cross — the tracked ledger commit and every named-ref reader of it are unchanged and their
  retirement is a separate leaf. Added the matching local invariant. Verification metadata remains
  closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T20:42+02:00 — Recorded the child-admission seal removal and the already-vacant stop on this
  route (uncommitted 260831-LOCR change set on `ar/260831_lifecycle-owned-completion-relay`): the
  deleted `atomic_series_seal.py` and its call sites, the `require_parent_series` rename, the pause's
  `atomic-series-already-vacant` success for a master holding no selection (with the unreadable/foreign
  refusals kept and `release_atomic_series_selection` unchanged), and the new ordered playthrough as
  the regression proof. Widened the stop invariant to state that no lifecycle cell refuses a leaf,
  updated the load-bearing reference rows (`pause_result` and friends to `pause.py:80-128`/`173-191`/`193-209`
  after the module grew to 209 lines, plus a `require_parent_series` row), and corrected the
  `test_pause_stop_only_end_to_end.py` description. Verification metadata remains closeout-owned; no
  acceptance claim and no verification stamp advanced.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: recorded the stop-only pause on this route — the
  `modules/pause.py` delegation to the existing release authority, the paused payload and its
  proposal-free `nextStep`, the per-contract isolation that leaves a sibling's record byte-identical, the
  structural exclusion of publication (measured closure 60 modules including the root, 5 direct
  imports, 54 beyond them, 0 of 12 publication modules reached, with non-vacuity checks and named
  witnesses so a depth-1 walker fails), and the explicit statement that
  `worktree_checkpoint_landing` remains the separate publication. Added the load-bearing
  file row, the local invariant, the reference row, and the route-impact section. Verification metadata
  remains closeout-owned; no acceptance claim.
- 2026-09-13T17:56+02:00 — 260831-LOCR-L36: corrected the checkpoint-route paragraph and recorded
  the reconciled series completion. The checkpoint is a partial **publication** (it moves the master's
  committed code and memory refs onto the protected source branch under explicit developer approval),
  not a pause, and the checkpoint capture proves its ledger mapping through
  `exact_series_memory_closeout`, the exact-mapping reader, while the final series route may accept the
  reconciled pair through `series_memory_closeout`. Recorded that the atomic completion proof no longer
  anchors the leaf chain at the recorded base pair — `worktree_sync` advances that pair, so the chain
  is ordered by the leaves' own landed ancestry and each step is admitted only when it adds nothing
  beyond the previous landing and the official positions this contract synced with — and that a
  master's own reconciliation merges enter `atomic_series_ledger_prefix` as proved rows. The recorded
  pair for a reconciled master is the reconciled code tip against the memory ref the same sync landed,
  accepted only when the landed table is the exact projection of its source plus this line's own true
  rows; recording that row is an agent-owned `memory.md` write with no public tool. Verification
  metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T15:03:18+02:00 — 260831-LOCR-L36 round 2: stated the developer ruling on this route. "What This Area Is", the Hot Path Summary, and the local invariants now say that a graph-less sprint's `atomic-sequential` default describes the sprint's shape (every commanded master executes atomically) and serializes nothing, because such a sprint declares no dependencies, and that per-contract activation never pauses or excludes a sibling; the same ruling is recorded on the sibling `modules/overview.md` route. Source-pair wording was kept only where the sync/integration plane is genuinely per pair (the `Select And Admit An Atomic Master` flow steps and the sync-transaction paragraphs). The per-contract activation account itself is unchanged. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T14:19+02:00 — Per-contract activation curation on this route: rewrote the area purpose, hot path, R25 observation boundary, structures, operating model steps 2/6/7, main-flow selection step, load-bearing rows, invariants, child-overview row and the Integrated-IAS sentence so atomic-series activation is described as one `contract_fingerprint`-keyed record per series contract rather than one selection per protected source pair — selecting one master no longer pauses, clears, or terminalizes another, and `reconciling` is the only waiting reason. Replaced the retired `AtomicSeriesSourceRef`/`AtomicSeriesSourcePair`/`atomic_series_source_pair` rows with the `AtomicSeriesActivationRecord`/`AtomicSeriesActivationArchiveEvidence` and `observe_atomic_series`/`_require_record_identity`/`contract_fingerprint`/`activation_path`/`atomic_series_admission_projection` citations at models/structural/atomic_series_activation.py:16-27 and :30-45 and atomic_series_activation.py:145-152, :360-372, :130-134, :137-142, and atomic_series_admission.py:33-74. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:00+00:00 — 260831-LOCR-L34: recorded the preview/apply parity invariant on this route
  with its full instance inventory (five fixed; `worktree_start` and the memory-carryover pair
  reported-not-fixed with their reasons; and the `worktree_abandon`/`worktree_cleanup`
  verdict/state-string adjacent shape), and the checkpoint reachability repair that produced it — the
  captured `SeriesCheckpointRefs` candidate with its required, revalidated `expected` argument, the one
  `checkpoint_landing_eligibility` decision both surfaces read, the shared ledger proof, the required
  `operation` name on the protected-ref edge, and the closeout preview gate extraction. Content change,
  not a range repoint; verification metadata remains closeout-owned and no acceptance claim is made.
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
