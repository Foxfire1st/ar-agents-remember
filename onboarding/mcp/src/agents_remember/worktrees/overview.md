# mcp/src/agents_remember/worktrees

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees` |

## Governing Overview

[mcp overview](../../../overview.md)

## 260928-MIK-L37 The Cutover Lock Joins This Route, And A Reopened Leaf Writes A New History Attempt

`260928-MIK-L37` (MIK-R37) adds one module and wires it at every memory route of this layer. What earlier sections of this overview call "inert until the cutover" is what the code does on converted memory: a
memory tree that holds `knowledge/layout.json`.

- **[`cutover_lock.py`](cutover_lock.py.md) (new): unconverted memory is read, never written, checked, synced or
  landed (MIK-R09 rule 6, second bullet; MIK-R24 rule 9).** A route that found its memory unconverted on every side
  asks `cutover_lock_refusal`. The lock holds once the memory repository holds converted memory anywhere (a local
  branch tip or a registered worktree's working tree with `knowledge/layout.json`); the refusal names the crossing
  sync. A repository that holds none is not locked and behaves as before this master. A probe Git cannot answer
  refuses by name. A converting candidate is gated, never locked. Decision record DEC-FCNRNT holds why the lock is
  this fact about the repository, and DEC-VMMJDN why the onboarding card writers stay unlocked.
- **Where it is asked.** [`knowledge_gate.py`](knowledge_gate.py.md) (`leaf_cutover_refusal`,
  `prepared_closeout_lock`, and inside `leaf_gate_refusal` and `landing_gate_refusal`),
  [`knowledge_crossing.py`](knowledge_crossing.py.md) (`unconverted_line_refusal`),
  [`direct_landing.py`](direct_landing.py.md), [`sync_transaction.py`](sync_transaction.py.md) (`_cutover_locked`,
  at admission), and the `modules/` routes (closeout, record landing, a leaf's integration).
- **A leaf that writes again after its closeout (decision record DEC-0AEQ28).** `knowledge_gate.latest_owner_history`
  finds the leaf's latest attempt file (`<leaf-id>-attempt-<n>.json`), and `close_owner_history` closes that one; the
  closed first file stays frozen. `knowledge_gate.closed_out_memory` names the memory commit of the leaf's recorded,
  completed closeout: its closed history files are frozen for the validator and the gate also while the parent line
  does not hold them. [`services.py`](services.py.md) carries those commits as `LeafPublication.frozen` and
  `LandingGateRequest.frozen`, and [`knowledge_validation.py`](knowledge_validation.py.md) passes them to the
  validator.
- **The stage copies of a knowledge conflict.** [`knowledge_conflict.py`](knowledge_conflict.py.md) materialises a
  settlement's three index stages in a temporary directory that is removed on every way out.
- **Cancel after a memory conflict.** [`sync_transaction_git.py`](sync_transaction_git.py.md)'s `rollback_side`
  restores a tracked `memory.md` before `git merge --abort`, so a conflicted memory sync can be cancelled on a line
  that still tracks the cache.

The lock is a stored invariant (INV-JT28KJ), realized in `cutover_lock.py` and at each route that asks it, in this
layer and in the application, memory and command-line layers, and proved by `mcp/tests/test_knowledge_cutover.py`.

- The lock's one question and its refusal. [65]
- The worktree layer's helper that names the leaf's line. [66]
- The managed sync asks the lock at admission. [67]
- The closeout closes a reopened leaf's latest attempt. [68]
- The rollback restores the cache before the merge abort. [69]

- The commit whose closed history files are frozen: the recorded, completed closeout's. [70]
- The memory trees of a commit that publishes a leaf. [71]


## Route Impact: Explicit Code-Object Retention (260921-ICR-L11)

This route's `modules/` gained **one member** this leaf: `modules/code_object_retention.py`, the explicit
Git-object retention a durable comparison generation needs because the candidate tree it binds exists in
**no commit**. The route-level facts a reader should carry are the ones that constrain the ref namespace
and the custody question:

- **`refs/ar/retained-code/` is a namespace of its own, not a branch.** Nothing fetches, pushes, merges,
  rebases or deletes it, which is precisely why `worktree remove`, `branch -D`, `worktree prune` and
  `gc --prune=now` leave a pin where it is — the module's own docstring states that property as the
  reason the namespace exists rather than as an observation.
- **One ref keeps both bound objects alive**, because the retention commit's parent is the **recorded base
  commit** rather than `HEAD`; and its commit id is a function of the two objects it keeps (identity and
  timestamps supplied, dated by the base commit), so re-creating a released pin reproduces the identical
  object and an exact re-freeze converges.
- **Custody is measured only over the history the caller names.** The consumer derives those names from
  the enclosure contract — the leaf's protected source branch plus the commits the task record landed —
  and the leaf's own disposable work branch is deliberately absent. A tree that no named history holds is
  `retained`, which keeps the pin: the safe direction to be wrong in, and the reason a custody
  measurement never releases anything by itself.
- **Release is explicit and refuses to delete what it did not bind.** A ref that no longer points at the
  recorded commit is refused, an already-absent ref converges, and the value returned carries the custody
  measured *before* deletion — the value a caller stores as the unavailable-history record.

**Open boundary, recorded rather than assumed safe.** Whether a landed integration or closeout operation
objects to the new ref namespace was not measured by this leaf, which cannot run those transactions.

- **The retention owner this route gained: one commit, one ref, the recorded base as parent.** [1]
- **Custody measured over named history, and the three-way observation that a record never stores.** [2]
- The commit identity that makes a re-created pin identical. [3]
- The explicit release, and the record it returns. [4]
- The contract-derived custody names the create-side consumer measures against. [5]
- The per-file detail for the new member: the module's own statement of the three properties — one commit and one ref, measured custody over named history only, explicit release with a record — and of what it does not decide. [6]
- The per-file detail for the new member. [7]

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

`series_closeout.py`, integration admission and synchronization use exact code/memory history. `ledger_projection.py` and `named_ref_memory.py` retain the consumer read surface, derived solely from committed attribution. Closeout and landing produce at most code plus one memory-content output; cache availability cannot gate them. `knowledge_validation.py` is the memory commit routes' gate to the MIK-R22 knowledge validator: a converted memory commit is validated before it is made, and today the sync's memory merge calls it.

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
| `services.py` | explicit provider, memory, citation, certification-continuation and knowledge ports (validation, crossing, worklist recompute) |

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
2. Resolve and stage the retained merge in the reported code or memory worktree. A **knowledge dataset** on
   the memory side is not the agent's to resolve by hand: the transaction settles it through the knowledge
   merge adapter before it reports the conflict, and only the paths the adapter declined are handed over.
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
| `sync_transaction_git.py` | Git proof | retains conflicts and proves exact operation-created history; validates a staged memory merge before committing it; routes a crossing sync's knowledge paths through the crossing plan | covered |
| `knowledge_validation.py` | knowledge-validator gate (MIK-R22) | probes the layout marker and, for converted memory, calls the validator through `KnowledgeValidationPort`; refuses when the validator or the paired code commit is missing | covered |
| `knowledge_crossing.py` | crossing sync and unconverted-line refusal (MIK-R24) | plans a crossing sync's structural merge through `KnowledgeCrossingPort` before Git runs, applies it with conflicted paths unmerged, writes the crossing report, closes a master line's crossing history file; refuses an unconverted leaf tree once its official line is converted | covered |
| `knowledge_conflict.py` | knowledge-conflict settlement (Git half) | settles a binary knowledge dataset through the merge adapter so the agent keeps only what the adapter will not decide | covered |
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

## The Contract Read Is Recorded

`load_contract` ([worktree_contract.py](worktree_contract.py.md)) is the one read entry of a series contract and of a leaf
enclosure contract for every worktree tool. It probes and reads the file through the kernel's read recorder
(`observed_exists`, `observed_text`), so inside a recording block the read leaves one row under the path it was given:
the SHA-256 of the exact bytes read, `absent` for a missing file, or `unreadable (...)` for a failed read. A caller that
keeps a result together with its recorded rows, such as the reviewer's leaf-wide view and the invariant gate, depends on
the contract's bytes as they were consumed. Outside a recording block nothing is recorded, and for every caller the
refusals of the read are the same: a missing file raises `ContractError`, and an error of the read itself is raised
unchanged.

- The contract is probed and read once through the read recorder. [72]
- A read is recorded with the identity of its exact bytes, or as absent or unreadable. [73]
- A missing file is recorded at the probe. [74]

## An Abandoned Row Is Outside A Master's Landing Chain

An atomic master's closeout proves a landing chain over the enclosures of its rows that are not `abandoned`
([series_leaf_contracts.py](series_leaf_contracts.py.md)). An abandoned row needs no enclosure or landing, and an enclosure it has whose
integration is not completed is ignored; an abandoned row whose enclosure records a completed integration refuses by name; a master whose rows are
all abandoned has an empty chain that still refuses a commit of its own on the master's line. Every refusal of
[series_closeout.py](series_closeout.py.md) and of `series_leaf_contracts.py` names the master, row, leaf or contract cell and the action that
clears it. [task_resolver.py](task_resolver.py.md) never archives a task that holds a series contract, so finalizing a master never archives
it; the skip names the commanding sprint or `task_doc.retire_master`. [task_retirement.py](task_retirement.py.md) holds the read-only readiness check
that `task_doc.retire_master` runs: actual open leaf work and unfinished or unreadable current enclosure operation authority refuse.
The master's own resources, recorded identity differences, pending cleanup without open work and historical document/report observations remain facts.
Lifecycle remedies require a live locator; otherwise the refusal gives the applicable manual action.

- Only non-abandoned rows need an enclosure, and a landed abandoned row refuses. [75]
- The chain proof is built from those enclosures. [76]

- A task holding a series contract is skipped with the commanding sprint or the retire route named. [77]

- Retirement readiness refuses actual open leaf work and unfinished or unreadable current operation authority, and returns evidence and retained facts. [78]

## Evidence

### Repo-Internal References

- Task observation, memory/finalization continuation, knowledge validation (since MIK-R22), the knowledge crossing (since MIK-R24), the worklist recompute (since MIK-R08), the review-artifact archive hook (since MIK-R25) and the mandatory invariant gate (since MIK-R09) use explicit service ports; `WorktreeServices` carries each as a field. [8]
- The activation record is a strict per-contract fingerprinted snapshot with explicit selection states. [9]
- The route's stop: release this contract's selection, refuse a non-series contract, report a released master as `paused` or a master that held no selection as `atomic-series-already-vacant`, and propose no next call in either success. [10]
- The child-admission seal is deleted: the parent-series helper is now resolution only and no lifecycle cell refuses a leaf. [11]
- The stop cannot reach a publication, asserted structurally over the module's import closure. [12]
- Selection observation treats absence as vacant and refuses a record that is not this exact contract rather than inferring from task or queue state; the record address is the contract's own digest. [13]
- Selecting admission publishes reconciling, delegates exact sync, and publishes active only after the current source pair is proven; the public admission explanation stays contract-grounded and never names a foreign master as a precondition. [14]
- The stable journal lives at `.lifecycle/sync-operation.json` and projects recovery without reading task text. [15]
- The sync driver retains conflicts for continuation, exposes explicit cancellation, and now carries the authored reconcile route through the same continuation. [16]
- Cancellation restores only operation-owned heads; malformed or missing journals recover only through explicit pinned-ref proof. [17]
- Every sync proof is Git state — the admitted head, the already-current decision, the staged resolution (validated by the MIK-R22 knowledge validator before its commit when the memory is converted, after a crossing sync's history file is closed), and the completed branch — and none of them reads a ledger row list. [18]
- A mid-flight selection reports the stuck contract and both exits, and a succeeding pass beside it never reports its own success state. [19]

Current working-candidate evidence for this route:

- Checkpoint captures the current code and memory branch tips without a ledger mapping prerequisite. [20]
- Consumer source rows are derived only from Git attribution. [21]
- Real memory source ancestry remains a landing requirement. [22]

### Cross-Repo References

No cross-repository source is configured for this memory root.

### Docs References

No Domain Documentation source is configured for this memory root.

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `modules/pause.py` | [`modules/pause.py.md`](modules/pause.py.md) | covered | the stop-only pause: release one selection, publish nothing |
| `cutover_lock.py` | [`cutover_lock.py.md`](cutover_lock.py.md) | covered | the cutover lock: unconverted memory is only read once the repository holds converted memory |
| `knowledge_conflict.py` | [`knowledge_conflict.py.md`](knowledge_conflict.py.md) | covered | Git half of the knowledge-dataset conflict settlement |
| `knowledge_crossing.py` | [`knowledge_crossing.py.md`](knowledge_crossing.py.md) | covered | the crossing sync in the managed sync, and the MIK-R24 rule 9 refusal |
| `knowledge_validation.py` | [`knowledge_validation.py.md`](knowledge_validation.py.md) | covered | memory commit routes' gate to the MIK-R22 knowledge validator |
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

## Route Impact: The Sync Settles A Knowledge-Dataset Conflict (260915-KS-L31)

The sync's retained-conflict flow gained one step, and the step is what makes the knowledge merge adapter a
driver rather than a callable seam. A knowledge database is **binary to Git**: an ordinary merge can only
declare the whole file conflicted, and no amount of staging resolves it. Before this change the transaction
handed that file to the agent as `sync-resolution-required` with `resolutionOwner: agent`, and the union was
obtainable only by calling `resolve_knowledge_merge_base` and `merge_resolved_knowledge_datasets` by hand —
not a composition seam an agent should have to discover.

`_continue_memory_merge` now calls `settle_knowledge_conflicts(Path(side.worktree), conflicts,
side.preSyncHead, side.sourceCommit)` before it returns that state, and the left/right pair it passes is
exactly the pair the adapter's request names: `ours` is the work branch tip the merge started from and
`theirs` is the source commit being merged in. Only the paths the settlement could not decide come back as
`resolution-required`, so the routing **narrows the agent's work rather than hiding any of it**.

The new module `knowledge_conflict.py` is the Git half and owns three facts:

- **Binary safety.** The three datasets are Git *index stages*, and `kernel.git_command.run_git` returns
  text, so reading a stage with `git show :1:<path>` would decode a SQLite file through a text layer and
  corrupt it before the adapter ever saw it — surfacing as a row-count mismatch rather than as corruption.
  The stages are materialised with `git checkout-index --stage=<n> --prefix`, where Git writes the bytes
  itself, one prefix directory per stage.
- **Refusal preserved.** A path the adapter will not decide — a schema disagreement above all — stays
  conflicted, and `settle_knowledge_conflicts` returns it to the caller, which is the tuple the transaction
  reports.
- **No compatibility verdict.** A structurally merged dataset says the union is valid, never that the
  combined knowledge is correct; nothing here may treat it as approval.

The layer contract is what splits the work across two modules rather than one, and the split is enforced
rather than documented: a module under `worktrees/` may not import `agents_remember.memory` at all, so the
dataset half — reading identities, proving the common base, publishing the union — lives in
`application/knowledge_merge.py` as `merge_conflicted_stages`, and this module hands it three paths and
receives one boolean. `SyncGitProofError` still owns every unproven Git transition, and the routing
introduces no new authority, no commit of its own, and no ledger row.

- The routing: knowledge conflicts settle in the transaction, what it will not decide is what the agent still gets, and the engine's reason travels out with it. [23]
- Binary-safe stage materialisation and the unique-common-base proof that refuses rather than guessing. [24]
- The dataset half this route may not host, and the commits the adapter's base claim needs together. [25]
- The layer rule that forces the split, enforced over the tree rather than asserted. [26]
- The integration case that drives a real divergent dataset through `sync()` and asserts the sync completes with both sides intact. [27]

## Route Impact: A Series At A Collected Address Is Re-Addressed, Not Refused (260915-KS-L34)

This route's `reopen.py` is the owner of `task_reopen`, and it grew a second arrival at the series
publication. The route-level fact a reader needs is **what decides a series reopen's ref rule**, because
the answer is not the cell the reader would look at first.

A completed series reaches terminal cleanup: its enclosure generation is collected after terminal
archive proof, its locator reads `terminal-archived`, and its enclosure root is gone. Reopening such a
series in place is now one journaled transition — contract tombstone, integration refs, master document,
successor enclosure generation. But a series can also arrive at that transition **already live**: reopened
by hand before the transition existed (the state D-49's own comment describes), or by a reopen whose
successor publication was interrupted and then forgotten. That state is `cleanup: pending`, every
progress cell virgin, both integration branches carrying the series' *own* landed work, and a locator
that is still `terminal-archived`. The old gates refused it on all three counts, and every operation on
the series refused with it (`terminal-archive-contract-mismatch`,
`operation-location-terminal-archived`), so the line could not be integrated by any route.

Three facts now decide instead of two, and each one replaces a cell that could not answer:

- **In flight, not `cleanup`.** `_series_in_flight` reads `closeout_status` and `integration_status`.
  `cleanup` is deliberately **not** the question: the reopen rewrites that cell as its own first durable
  step, so keying the ref rule on it would make the rule's answer depend on whether the reset had already
  been written — which is exactly the difference between a first attempt and its resume.
- **An advanced branch may be the series' own work, not a moved ref.** `_series_ref_recut` takes
  `in_flight` and accepts an integration branch that is **strictly ahead of its source on the same line**
  (the recorded source tip is an ancestor) as action `advance`: that branch is the line the series is
  landing on, there is nothing to re-cut, and it is never moved. A *completed* series, or a diverged or
  lagging branch, keeps exactly the refusal it had.
- **The locator separates "collected" from "mid-transition".** `_series_is_live_unaddressed` accepts the
  live-unaddressed state only when the generation at the contract's own address is `terminal-archived`
  **and** closeout and integration are both untouched, then publishes the successor generation alone —
  structured `mode: publish`, no reset and no ref move. The same predicate is what lets an interrupted
  reset be resumed rather than stranded: with the tombstone already durable and the locator still
  collected, the same call finishes the publication.

The review-counter half is the part that is easy to miss and expensive to get wrong. A reopened master
begins a **new review cycle**, so its counter must be zero: the rounds that ran belong to the completion
being reopened. `_review_state_carries_history` reports whether the counter carries anything at all
(round, pending, sealed baseline, residual, developer approval, additional rounds), and
`_plan_series_document_reset` writes a pristine `ReviewState()` when it does. Without it a master reopened
at round 3 keeps the counter, its next round reads as the fourth, and at the cap an ordinary first round
reads as one the developer had to authorize. The reset no longer returns early on a document that has
already left `Completed`, and a document whose counter is absent or all-zero is left untouched.

What this route therefore guarantees to every caller: **the reopen never moves an existing ref** — it
re-cuts an absent one, reports an advanced one as the series' own work, and refuses divergence — and a
successor generation always cites the exact archived predecessor. The series' own `cleanup` stays
`pending`, because `reopened` is itself a terminal series state and would leave the series unable to own
the lane.

- In flight is read from the progress cells a completion writes, never from `cleanup`. [28]
- A live series is unaddressed only when its own address is terminal-archived and both progress cells are untouched. [29]
- An advanced branch on an in-flight series is its own landed work: reported `advance`, never moved. [30]
- The reset clears a review counter that carries history, and leaves an all-zero one alone. [31]
- `reset` or `publish` is decided by the arrival, and the applied payload states which one ran. [32]
- The gathered case that drives all three arrivals at the publication, and the spent counter's clearance. [33]
- The already-live arrival re-addressed: successor cites the archived predecessor, branch unmoved, counter cleared from `round: 3`. [34]

## Route Impact: The Series Chain Admits The Reconciled Line A Step Merged With (260915-KS-L35)

This route owns the one proof that decides whether an atomic master's landing chain may be closed out.
`series_closeout.py::_require_exact_atomic_landing_chain` proves every canonical leaf landed, orders the
leaves by their own landed ancestry, and then walks each side of the pair from landing to landing proving
that **every step adds nothing but the series' own reconciled line**. This leaf changed what "nothing but"
means, and that change is the route-level fact a reader needs.

A step is measured by **enumeration**, never by subtraction: `_require_admitted_step` lists what the step
adds (`rev-list --no-merges --full-history <later> --not <earlier>`, the memory side additionally excluding
`. :(top,exclude)memory.md`) and admits a commit only when it is one of the official positions the chain's
own contracts recorded as synced, or when a recorded position lying **inside** that step reaches it.
Subtraction was the old shape and it removed a position's whole ancestry, so a single position descending
from a step erased the step and the check could pass vacuously; the enumeration is what closed that gap
(D-45).

The residual the enumeration left was the shape the rule exists to **allow**. When a step's endpoint is the
merge of the previous landing with a synced position, the whole step *is* that position's own line. On the
260915-KS master the step is L5's landing `7db50f8f` to L6's recorded base `8dfc11b8`; `8dfc11b8` is the
merge of `7db50f8f` with the synced super-line position `8dd62345`, and all 22 commits the step adds are
reachable from `8dd62345`. The rule admitted the position and refused the line it introduced, so the
master's own closeout refused `atomic-series-leaf-chain-invalid` naming those 22 commits (D-60), and the
master could neither complete its own closeout nor integrate.

Two predicates now decide, and the boundary between them is the point:

- **`_positions_inside_the_step`** — the recorded positions lying *inside* the step: strictly after its
  start (`is_ancestor(earlier, position)`) and at or before its end (`is_ancestor(position, later)`). The
  start is excluded deliberately and costs nothing, because the revision walk already removes everything
  the start reaches; a position *past* the step is excluded because it reaches the whole step and would
  erase a commit the step genuinely introduced.
- **`_reached_by_an_official_position`** — a commit is admitted when any position in that inside set
  reaches it. The admission therefore stays bounded to the positions the call was given, and a position
  that merely descends **from** the step is not inside it: the counter-case ("a position that descends
  from a step does not vacate it") still refuses, and its case still passes unchanged.

Nothing else about the chain proof moved. Origin, leaf-landing identity, the pair ordering, and the
refusal to create commits on a dirty integration checkout are all as this overview already describes; the
repair is one clause in the step rule and two helpers beside it.

One operational consequence belongs on this route, because it is a property of the check rather than of
this leaf. The rule is enforced by whatever revision of `series_closeout.py` the **running plane** loads,
not by the revision carried on the branch being closed out. The 260915-KS master's first promotion ran
under the pre-repair validator and admitted genuinely foreign history once, and nothing re-measured the
result; the second promotion ran the repaired validator against that history, which is what surfaced the
refusal. A chain admitted under an older validator has not been proved by the current one.

- Each landing is an ancestor of the ref, and each step is proved by enumeration against the positions the chain's own contracts record. [35]
- Inside means strictly after the step's start and at or before its end, so a position that only descends from the step is outside it. [36]
- Both directions of the step rule are pinned by one collected case, because both lanes sit at exactly their budget, and the descending-position counter-case is untouched. [37]
- The order the spine walk consumes: every leaf is proved landed first, then ordered by the pair predicate, refusing unless exactly one minimum exists. [38]

## Route Impact: The Diagnosis Reaches The Agent, And One Authored Decision Settles It (260915-KS-L40)

The L31 section above records the wiring: a conflicted knowledge dataset settles inside the transaction and only the undecided remainder reaches the agent. **This leaf changes what the agent receives and what it can do about it**, and both halves are public.

**The refusal stopped being a boolean.** `merge_conflicted_stages` (application) returns `KnowledgeStageSettlement(settled, conflict, refusal, detail)`; `knowledge_conflict.py` returns `RefusedKnowledgeStage` (path + the engine's `MergeConflict` + the typed `KnowledgeRefusal` + this layer's own detail + the decisions that conflict admits); `sync_transaction_git.SideMergeOutcome` carries it out of the merge. The engine's explanation was always produced — it used to be discarded one layer below the public response, which reported `sync-resolution-required` with `files: ["knowledge.sqlite"]` and nothing an agent could reconcile. The facts now travel **verbatim**: nothing on the path re-renders, summarises or re-keys the refused row, because a re-rendered diagnosis is a second implementation of it.

**The diagnosis is durable, not just returned.** `SyncSideRecord.knowledgeConflict` journals it, so `_active_sync_projection` re-states the exact row on every later call. Without that, a resumed sync would fall back to naming the unresolved file.

**There is a supported recovery, and the response advertises it.** The public sync (`worktree_sync`) gained a third flat argument, `knowledge_resolution`, carried with `resolution_action='reconcile'`; the response's `nextOperation`/`nextArgs` switch to `reconcile_knowledge_resolution` with the journaled `table`/`record_id` and the decision left as a placeholder, because choosing the side is the agent's act and not the projection's. The merge's own vocabulary decides which decisions a conflict admits (`expressible_decisions`), so the agent is never offered one the engine would refuse to apply.

**What the engine will and will not settle.** `apply_changeset` applies the caller's decision only where it names exactly the conflict in hand (table **and** rendered key), and lets the application continue to the next conflict — which is refused exactly as before. `keep-right` is reachable only with a named row. The row-less referential conflict admits `keep-left` alone and is settled by retracting a row the **arriving** delta inserted. Two consequences are stated as limits rather than as behaviour: the refusal's other named orientation (*restore the removed row*) is **not** expressible in this change and keeps its refusal, and a referential retraction is not itemised in the `synced` result. A schema disagreement still refuses explicitly and admits no decision at all, which the response says by publishing an empty `decisions` list and keeping the generic continuation.

**The disjoint path is untouched.** `sync(memory_sync_choice="merge-memory")` on a valid disjoint divergence still returns `synced` with exit 0, the union committed and the merge parents equal to the two admitted commits — measured identical before and after the change. The explicit schema-disagreement refusal is retained, and a structurally merged database is still not approval.

## 260915-KS-L43 The Recovery Journals Accepted Decisions, And A Returning Answered Row Is Refused

**This route's impact is the retained-knowledge recovery's progress property, and it has two halves that only work together.**
The L40 section above records the supported recovery: one authored decision, validated against the journaled diagnosis,
re-run through the merge. What it did not have was **progress**. A retained merge holding two conflicts alternated between
the same two rows forever, because each attempt carried only the newest decision and so re-refused the row the previous one
had already answered; the agent was offered a decision it had already made and that had already had its effect. Measured on
the same harness and the same public surface: **twelve** applications to the cap with `settled: false` before, **two**
applications and `state synced` after (`evidence/after-independent/recovery-progress-after.json` against
`recovery-progress-before.json`; the script drives only `fixture.sync` and the advertised `nextArgs`, so it runs unchanged
against both trees).

**Half one: accepted decisions persist.** `SyncSideRecord.knowledgeReconciliations` journals every decision this side has
already accepted, in acceptance order, and `_reconcile_knowledge_resolution` re-enters the merge with **all** of them —
`accepted = (*side.knowledgeReconciliations, args.knowledge_resolution)` — so each attempt starts from the conflict the
previous attempt actually reached. Each decision still answers only the row it named, and every conflict no decision names
is still refused, so this is not a policy. `_finish_retained_merge` clears the field with the conflict it belongs to.

**Half two: a returning answered row gets a bounded refusal.** If a row an already-accepted decision answered comes back
anyway, the retraction could not hold it — retracting the arriving change re-exposed another arriving change that needs the
same row — and `_reconcile_progress_refusal` returns `sync-resolution-cycling` naming the exact row and the two honest next
steps (resolve it in the worktree and continue, or cancel), rather than journaling the same decision a second time. The
merge guard is untouched: `_independent_insert_refusal` still refuses two independent insertions of one identity, and no
blanket equal-payload exception was introduced.

- The journaled decisions, and the continuation that clears them with the conflict. [39]
- The attempt that carries every accepted decision, and the bounded refusal that stops the cycling. [40]
- The Git half that hands the adapter the whole sequence. [41]

## 260915-KS-L42 The Unsettleable Conflict's Summary Names It And Says What To Do

**This route's impact is the sentence a caller reads when no authored decision can settle a retained knowledge conflict.** In `worktrees/sync_transaction_results.py`, `_unsettled_instruction` splits that summary on the merge's measured retraction precondition: a referential refusal whose `precondition` is `no_arriving_insertion` is the orientation where the arriving side removed a row the retained side still cites, so the response says to restore the removed row or retract the reference in the worktree, stage it and continue — while every other unsettled conflict keeps the shipped "resolve it in the worktree, stage it, then continue". `_resolution_guidance` needed no new branch: an empty decision list already falls through to `continue_sync_resolution` with `nextArgs.resolution_action=continue`, which is the route that actually exists, and `cancelArgs` is still carried beside it.

**The failure this replaces was measured, not argued.** The first response used to promise that the merge continues while advertising a `keep_left` the merge had not observed to work, and driving exactly that advertised call returned the identical response forever. The before/after captures are kept in the leaf's evidence — `notes/reports/2026-09-21-cycle-fix-verification/evidence/cycle02-orientation/summary-driven.json` (before) and `.../cycle02-orientation-fixed/summary-driven-after-fix.json` (after) — and the diagnosis in the two is byte-identical, which is the point: the explanation was preserved and only the false promise was removed.

**Open, not settled — named for the round-3 reviewer.** `cancelArgs` itself returns `sync-operation-refused` / `SyncGitProofError` in **both** orientations, including the INSERTED-row orientation round 2 verified as working; it is not introduced here, it is most likely the fixture's missing canonical enclosure locator chain, and the cancel half of the manual continuation therefore could not be proven to settle in that fixture.

## 260928-MIK-L22 The Memory Commit Routes' Gate To The Knowledge Validator

**This route gained the gate that keeps a converted memory commit from being made without a passing
validator run (MIK-R22 rule 8).** The validator itself lives in `memory_quality/knowledge_validator/`,
which ranks above this layer, so the route reaches it only through `services.KnowledgeValidationPort`,
bound by `application/worktree_services.py`. `knowledge_validation.memory_commit_refusal` is the one
entry point a route calls, with the exact candidate tree, its comparison bases and its paired code commit:

- It first probes each tree for `knowledge/layout.json` with `git ls-tree`. If no side has the marker,
  the memory is unconverted and the helper returns `None` before touching the validator, so every route
  commits unconverted memory exactly as before the cutover (MIK-R37). A tree Git cannot read is refused;
  it is never taken as unconverted.
- A converted commit with no paired code commit, or with no bound validator, is refused, never committed
  unchecked. There is no parameter that skips validation.

**The managed sync is the one route wired in this leaf.** `sync_transaction_git._finish_staged_memory_merge`
writes the staged merge as a tree and validates it against both parents and the code side's settled result
(`sync_transaction._paired_code`) before `git commit`. A refusal raises `SyncKnowledgeValidationError`; the
driver reports `sync-knowledge-validation-refused` with every violation and a recovery line, and it leaves
the merge staged and the phase unchanged, on both the automatic path and the retained-conflict `continue`.
Closeout, direct landing, record landing, and master and checkpoint landing are MIK-R09's routes by the
architect's ruling; they will call the same helper. Memory plans that are not a merge (fast-forward, skip,
already-current) are not validated at the sync.

- The route helper: marker probe, fail-closed on unreadable trees, refusal without a paired code commit or a bound validator. [42]
- The port the helper calls (since MIK-R09 with a `leaf_refusal` twin) and the bundle field that carries it (beside `knowledge_crossing`, since MIK-R24, `knowledge_worklist`, since MIK-R08, `review_artifact_cleanup`, since MIK-R25, and `knowledge_gate`, since MIK-R09). [43]

- The sync validates the staged memory merge before its commit, against a converted base when a parent is unconverted (MIK-R24 rule 7). [44]
- The driver maps the refusal to its own state with a recovery line. [45]
- The route never commits converted memory unvalidated, and an unreadable tree is refused. [46]

## 260928-MIK-L24 The Crossing Sync In The Managed Sync, And The Unconverted-Line Refusal

**This route gained the crossing sync (MIK-R24@v1 rule 8) and the rule 9 refusal.** A memory merge is a
crossing sync when one of its merge base, its own side and its incoming side lacks `knowledge/layout.json`
and another has it. The conversion itself lives in `memory/conversion/`, which ranks above this layer, so
the route reaches it only through the new `services.KnowledgeCrossingPort`, bound by
`application/worktree_services.py`.

- [`knowledge_crossing.py`](knowledge_crossing.py.md) (new) plans the structural merge through the port
  **before Git touches the worktree**, so a failing step leaves the line unchanged and names the step. It
  then replaces the started merge's `knowledge/` and `onboarding/` paths with the plan, leaving each
  conflicted path unmerged with its converted base, own and incoming versions as stages 1-3. It writes the
  durable crossing report into the worktree group's `reports/` and closes a master line's
  `<task-id>-crossing-<n>.json` in the merge commit. It also holds `unconverted_line_refusal`.
- [`sync_transaction_git.py`](sync_transaction_git.py.md): `start_side_merge` takes the crossing owner;
  `_crossing` is inert when all three trees are alike (every sync today); `_apply_crossing_merge` applies
  the plan; `_finish_staged_memory_merge` closes the crossing history file before the validator runs.
- [`sync_transaction.py`](sync_transaction.py.md) passes the owner (leaf, or the master line's task) and
  journals the report path. [`sync_transaction_state.py`](sync_transaction_state.py.md) omits an empty
  `crossingReport`, so ordinary journals keep the installed runtime's shape (ruling N2).
  [`sync_transaction_results.py`](sync_transaction_results.py.md) adds `resolution.crossing` and names the
  report.
- [`services.py`](services.py.md) declares `KnowledgeCrossingPort`, `CrossingRequest`, `CrossingPlanView`,
  `CrossingStepFailed` and the `knowledge_crossing` field.

**Rulings carried on the cards:**

- **Mechanical anchor fields never conflict.** An item only one side changed is taken whole, authored beats
  mechanical, and both-mechanical takes the incoming side.
- **A crossing conflict is never committed silently.** Conflicted JSON items hold a `crossing-conflict` marker
  the validator refuses, Markdown keeps Git markers, and a card's Markdown and sidecar must be resolved
  together.
- **Rule 9 refusals are inert until the official line is converted.**
- **Conversion and crossing are separate routes.** The crossing is only for lines that descend from a
  converted official line. The closeout refusal is L09's.

On the real ONT fork (`48b06d96b` against the scratch-converted sprint line), the conflicted cards were
exactly within the 46 cards both lines changed, and after mechanical resolution the merge validated clean.

- The plan before Git, and its application to the started merge. [47]
- The crossing branch of the memory merge. [48]
- The port and its request and view. [49]
- The rule 9 refusal. [50]
- The durable report and the master-line history file closed at commit. [51]

## 260928-MIK-L08 A Completed Sync Recomputes The Leaf's Worklist

**Route meaning extended (MIK-R08@v2 rule 8, architect ruling 1).** A completed managed sync moves the
leaf's base pair, so B and K_B move with it; the sync now recomputes the leaf's change-to-knowledge worklist:

- [`services.py`](services.py.md) declares `KnowledgeWorklistPort.recompute(contract)` and the optional
  `WorktreeServices.knowledge_worklist` field; the application binds `LeafWorklistRecompute` above this
  layer, as it binds the crossing port.
- [`sync_transaction_recovery.py`](sync_transaction_recovery.py.md): `finalize_sync` returns its completed
  result through `with_recomputed_worklist`, which adds `knowledgeWorklist` (the summary) when one applies.
  `recompute_knowledge_worklist` puts the port lookup, the contract reload and the recompute in one guard, so
  **the worklist recompute never fails a completed sync** (review R1 F2).
- [`sync_transaction_results.py`](sync_transaction_results.py.md): the `continue` replay of a completed
  generation recomputes too.

With no port bound, or no worklist applicable (both memory sides unconverted, every production leaf before
MIK-R37), the sync result is byte-for-byte unchanged. Closeout validation and landing pre-commit are the
other two triggers, and they are L09's.

- The port and the bundle field (which since MIK-R09 also carries `knowledge_gate`). [52]
- The completed result gains the summary; every failure leaves it unchanged. [53]
- The `continue` replay recomputes too. [54]

## 260928-MIK-L25 Archiving A Task Deletes Its Review Artifacts

**Archive-hook ownership (MIK-R25 rule 5, D17).** Review-artifact cleanup is bound through a service port.
Current series finalization retains the master folder and reports the archive skip, so it invokes no
review-artifact cleanup. Explicit `task_doc.retire_master` owns master archival and the applicable hook:

- [`services.py`](services.py.md) declares `ReviewArtifactCleanupRequest` (the task root as it is now, its
  directory name, the series contract's two repositories, `dry_run`) and `ReviewArtifactCleanupPort.cleanup`, and
  the optional `WorktreeServices.review_artifact_cleanup` field; the application binds
  `application/review_artifact_cleanup.ReviewArtifactCleanup` above this layer.
- [`modules/finalize.py`](modules/finalize.py.md): `_with_review_artifact_cleanup` runs right after
  `archive_completed_root_task` for an `archived` (or `would-archive`) task and carries the report as
  `taskArchive.reviewArtifacts`. An unbound port reports `not-bound`; any exception is a `failed` report — the task
  is already archived, so **the hook never fails finalize** (review F2, ruling 2026-09-29T23:15:34).

What the hook deletes, and why only that, is the application card's: the task's `refs/ar/review/<task-directory>/…`
refs (ruling 2026-09-30T02:32:42 (a): the directory name only), its own legacy `refs/ar/retained-code/…` pins (the
F1 exact rule and the trust line of ruling 02:32:42 (b)), and its legacy dataset copies by content, every path
physically confined to the task (rulings 00:08:39, 01:00:07, 01:37:42, 02:12:06; the TOCTOU window accepted). It is
not gated on conversion (ruling 22:22:37 Q4): once this build is installed, archival also deletes unconverted
tasks' legacy copies — including curator scratch copies — which L37's cutover notes state (F7).

- The archive hook's request and port. [55]
- The conditional finalizer helper acts only on archived or would-archive results; a series archive skip invokes no cleanup. [56]

## 260928-MIK-L38 A Leaf's Master Is Resolved By One Rule At Finalize And Reopen

**Route meaning extended (MIK-R38, developer direction D32: a completed leaf must show `Completed` on the master).**
The two terminal task-document writers in this route now find a leaf's master exactly as the task-document master
sync does, through `tasks/master_sync.folder_master_json_path`:

- [`modules/finalize.py`](modules/finalize.py.md) completes the listing master's row for a leaf that names no
  `master` (before, such a leaf finalized standalone and its row stayed `inProgress`; 15 MIK rows were repaired by
  resync writes). The folder master meets every named-master check; without one, or without the leaf's row, the leaf
  finalizes standalone as before.
- [`reopen.py`](reopen.py.md) drops its own copy of the fallback (ruling 2026-09-30T12:33:07 Q2); an unnamed
  `subTask` still resets its row, and a `light` document that is itself the folder's `task.json` no longer resolves
  to itself.
- Both refuse, before any write, a leaf or master whose read path differs from the store's write target for it,
  through `tasks/leaf_doc.require_task_document_in_place` (review R1 finding 1, rulings 13:11:32 and 13:35:32): a
  hand-made `light` leaf or master under another name would otherwise be written over the series `task.json`.

The rule lives below this layer, in the task domain, so this route imports it and owns none of it. It is not gated
on the memory conversion. The named-master resolution differences between the sync and these writers stay out of
scope (review R1 note 3).

- Finalize resolves a leaf naming none through the shared helper. [57]
- Reopen resolves a leaf naming none through the same helper. [58]
- Reopen's placement guard on the leaf and the master. [59]

## 260928-MIK-L09 Every Memory Commit And Landing Route Asks The Mandatory Invariant Gate

**Route meaning extended (MIK-R09@v2, D5: invariant work is mandatory, never report-only).** Every route in this area
that commits or lands a leaf's or a master's memory now asks the mandatory invariant gate before it moves anything.
The gate ranks above this layer (`application/knowledge_gate/`) and is reached only through the new
`services.KnowledgeGatePort`, bound by `application/worktree_services.py`. The new
[`knowledge_gate.py`](knowledge_gate.py.md) (carded, governed here) holds what the layer owns itself:

- **Applicability by the layout marker (rule 6).** Each route probes K_C or K_B (the candidate tree, the official
  line, the checkout's `HEAD`, a landed commit and its bases) with `has_layout_marker`; with no marker anywhere the
  route behaves exactly as before this master. A probe Git cannot answer refuses by name; it is never taken for
  unconverted memory (review R1 F9). MIK-R09 rule 6's second bullet (refuse unconverted trees and name the crossing
  sync) is **not** built: carried to L37 (ruling 14:38:47 gap 1).
- **No bypass (rule 5):** a converted route with no bound gate refuses (`GATE_UNBOUND`).
- **The closeout's own write (MIK-R07 rule 7):** `close_owner_history` sets `closed: true` in the leaf's history file
  (creating it with no rows when absent); `HistoryClosing.restore` undoes it on a refusal.
- **A direct landing's closing outlives the call:** per-generation receipts under the worktree group's `reports/`,
  settled when the generation lands (forgotten), is cancelled or was never created (restored, never over a later
  edit), with `git hash-object` recording the closed blob (R3-1) and an unreadable receipt refusing by name (R2-5).
- **The prepared path fails closed** on converted memory (`prepared_closeout_refusal`, gap 3).

The routes, each with a refusal test through its public entry point (`test_knowledge_gate_routes.py`, review R1 F5):

| Route | Where | What it checks |
| --- | --- | --- |
| Closeout validator | `integration/closeout/curator_coherence._require_knowledge_gate` | The full gate over the authority's exact candidate; `curator-coherence-knowledge-gate-refused`. |
| Closeout memory commit | `modules/closeout_external` | Closes the history file, validates the exact tree as a leaf publication against the parent tip, restores on refusal (F2). |
| Direct landing | [`direct_landing.py`](direct_landing.py.md) | Gate (the leaf is the one open history file's owner, gap 2), close, validate the exact tree, keep the closing until the generation is decided; an exact retry of an in-flight generation reaches it before the gate (F3). |
| Cancellation | `integration/lifecycle/control/cancellation` | Checks receipts before anything moves; restores a cancelled direct landing's closing. |
| Record landing | `modules/record_landing` | Probe first (F7); the landed memory commit validates against the task's memory base, and a leaf's history file is closed in it. |
| Master and checkpoint landing | `modules/integrate._knowledge_gate_block` | The validator on the master's memory commit and every entry at a path the net code diff changed `current` at its code commit (rule 4; F4: `unverifiable` refuses too). |
| Prepared closeout | `integration/closeout/certification/execution` | Refuses on converted memory (gap 3). |

[`knowledge_validation.py`](knowledge_validation.py.md) gains `leaf_publication` (the port's `leaf_refusal`, F1) and a
named refusal for a timed-out probe; [`services.py`](services.py.md) declares `KnowledgeGatePort`,
`LandingGateRequest` and `DirectGateVerdict`. **Candidate invariants (not ingested):** no memory reaches a
leaf-publication route without the recomputed worklist fully answered and the validator passing; on unconverted memory
every route behaves exactly as before the gate (the unconverted test; `unconverted.sh`, base `904e804b` against this
build: identical apart from the build label, including the real memory commit tree `20ccf39a…`, the record-landing
payload and the direct-landing preview). **Inert until the cutover.**

- The layer's probes, the unbound refusal and the closeout's own write. [60]

- The closeout validator's and the landings' gate. [61]

- The direct landing's closing, kept and settled per generation. [62]

- The port, the landing request and the direct verdict. [63]

- Direct landing's gate and closing. [64]

## Closed-leaf agent archive (MIK-R76)

`services.py` declares `LeafAgentArchivePort` and the optional `leaf_agent_archive` bundle field, so
the admitted terminal transactions reach the leaf archive service through the worktree layer's
existing port boundary. A bundle without the port reports `not-bound`; no fallback owner is
constructed.

