# mcp/src/agents_remember/worktrees/modules/start.py

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Owns worktree start, attach, status result construction, and startup preparation
for external memory and providers. Attach now reselects and reconciles an atomic leaf's parent
series before it exposes the existing workbench. Since L11 the existing-contract branch recreates
fresh for `cleanup in {abandoned, reopened}` (a reopened leaf keeps its exact leaf
id), and after writing a leaf contract start restamps the leaf doc's `lifecycleId`
via `tasks.leaf_doc` so the doc follows the enclosure's fresh lifecycle.

## Code Commentary

Every entry point and helper takes the typed `WorktreeArgs` dataclass (imported
from `agents_remember.worktrees.modules.args`), replacing the former
`argparse.Namespace`; `import argparse` is gone.

`attach_result` rejects a series contract as a workbench, admits the ordinary leaf contract and its
exact lifecycle location, then resolves any parent series. The series branch itself now lives in
`startup/series_attach.py` as `series_attach_result`, moved there verbatim under the size rail, and
this module calls it (`:174-175`): it resumes a live series whose integration branch still exists and
otherwise refuses with `series-terminal` (the contract's cleanup is already terminal) or
`series-branch-missing` (the work branch is gone locally). When a parent exists it calls
`activate_atomic_series_contract` before source-lineage projection: that call transitions the
requested parent's OWN activation record (`reconciling`, reconcile its pinned source pair, then
`active`) because the record is keyed per series contract, not per protected source pair. No other
master is named, selected, or paused on this contract's behalf, and attach returns the selecting
transaction's conflict/refusal rather than exposing stale implementation.
Only an active/current parent reaches the existing lineage check and `attached` result. Dry-run
activation remains observation-only.

**260831-LOCR-L36 re-keyed the activation record from per protected source pair to per series
contract.** Start/attach/dispatch/sync still share one selecting transaction, but the record it
writes is addressed by `contract_fingerprint(contract)`; a foreign master's record is read only by
that foreign contract, so two atomic masters that share one sprint's code/memory source branches
hold independent records and both may be `active`. `activation_waiting_reason(observation)` now
takes the observation alone and returns only `atomic-series-reconciling`; a vacant record, an
`active` record, and a foreign master are all explicitly not waiting reasons. Genuine wave
dependencies remain with the sprint execution graph's own `predecessor-incomplete:` reasons.

**The child-admission seal is gone, so this module's parent-series guards are resolution only
(260831-LOCR seal removal).** Both call sites — `attach_result` (code line 177) and the apply-time
start preflight inside `_plan_start_enclosure` (code line 703) — now import and call
`require_parent_series` cit:([`require_parent_series`], mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:309-330)
instead of `require_parent_series_accepting_leaves`. The helper still resolves and validates the
leaf's exact parent series (organizational direct-super work under a sprint graph returns `None`;
`_require_atomic_master` refuses a non-atomic master; a missing parent contract and a stale series
identity still raise), but it no longer decides whether that series accepts leaves. The guard it
used to call, `worktrees/atomic_series_seal.py::require_series_accepting_leaves`, is deleted with its
module: it read the parent's `(closeout_status, integration_status, cleanup)` cells as a seal, which
once `checkpointed` existed also sealed every master that took a checkpoint landing. A master is
meant to be paused and resumed, never locked by its own landing, so neither `worktree_attach` nor
`worktree_start` refuses a leaf because of a lifecycle cell.

`mcp/tests/test_lifecycle_playthrough_end_to_end.py` is the regression proof: it walks master open →
leaf start → leaf closeout → leaf landing → checkpoint → pause → attach, then starts a leaf commanded
*after* the landing.

**`start_result()` is now four lines (260731-EFA-L2)** — resolve context, build the contract, then
three stages, each of which owns one decision and can return early:

1. `_existing_contract_result(context, contract, args) -> WorktreeCommandResult | None` — attach to
   a live contract at this path instead of recreating its worktrees. Returns `None` (recreate
   fresh) when no contract exists, or when the one on disk is `abandoned` (a tombstone) or
   `reopened` (a reset) — either way its worktrees and branches are gone. With
   `args.retry_provider_setup` a live contract routes to `_retry_provider_setup_result`.
2. `_preflighted_contract(context, contract, args) -> WorktreeContract | WorktreeCommandResult` —
   the pre-creation preflights: stale base (records a `stale-base-blocked` beat, then refuses), the
   fast-forward rebuild, and the Windows long-path check. **The returned contract is the one the
   caller must use** — a `fast-forward` recovery may have moved the source branches, so the
   contract is rebuilt inside this stage and the fresh one is returned.
3. `_create_start_enclosure(context, contract, args)` — create the code worktree, prepare memory,
   plan providers, write the contract, and launch setup. Apply holds repository integration
   authority across its final exact source-lineage, parent-series, and workbench rechecks and every mutation. Preview runs
   those same read-only guards without opening the filesystem lock (which would itself violate
   dry-run byte preservation); apply always revalidates under the lock before acting.

**The three blocked returns use `recovery_guidance`, not `next_guidance` (260731-EFA-L4).**
`_blocked_memory_start_result` (`choose_memory_recovery`), `_blocked_provider_start_result`
(`choose_provider_setup_recovery`) and `_stale_base_preflight` (`choose_stale_base_recovery`) are
three of the five `RecoveryOperation` members, and all three pass `tool="worktree_start"`. The keys
they emit and their order are unchanged, so nothing on the wire moved; the split is in the type.
`next_guidance` is now narrowed to the phase machine's `NextOperation`/`NextTool` `Literal`s, which
`models.worktree.WorktreeSummary` imports — and none of these three payloads is a lifecycle phase.
They are blocks, rendered as a `FlexibleToolResponse`, so widening the phase vocabulary to hold
"blocked on a stale base" would have put it into the set the context packet's `nextOperation` claims
to be. `start.py` imports **both** builders: `status_result` still goes through the phase machine.

`status_result` returns `WorktreeCommandResult(0, dict(status_payload(contract)))` — `status_payload`
now returns the `WorktreeStatusPayload` `TypedDict`, and `WorktreeCommandResult.payload` is a plain
`dict[str, object]`, which a `TypedDict` is not assignable to; the `dict(...)` is that widening,
performed as a shallow copy.

CCR-R25 keeps the status entry point read-only while adding the series activation fact: when the
loaded contract is a series, `status_result` attaches `atomic_series_status_projection`; leaves
remain on the ordinary worktree status payload. Attach and start continue to delegate activation
and source synchronization to the selecting transaction, so this facade does not publish, repair,
or infer a live process from selector state.

`_contract_after_memory_start`'s disabled-memory branch now writes `memory_mode` through the typed
record: `amend_contract(replace(contract, memory_repo_path=None, …, memory_state="disabled"),
ContractCells(memory_mode="disabled"))`. The two look alike in the front matter and are not alike in
the type system — `memory_state` is free text, `memory_mode` is one of the six persisted
vocabularies — and `dataclasses.replace` types `**changes` as `Any`, so it checked neither. The
resulting contract is identical.

This stage split is why the memory/provider blocked returns and their start-progress beats all sit
in stage 3 while the stale-base beat sits in stage 2. `start_result()` itself
resolves context, asks `start_contract.build_start_contract` for the normalized contract, and then
runs the three stages: prepare code and optional memory
worktrees, run the synchronous provider preflight, write the contract for
real starts, and then LAUNCH provider setup in the background (GitHub #53).
The ordering is deliberate: the contract is the durable anchor
`worktree_status` polls while the setup thread runs, so it must exist before
the launch. `plan_providers_for_start` is the sync preflight (skip /
enablement / settings checks — config-level failures still block the start
fast); `run_or_launch_provider_setup` keeps dry runs fully synchronous
(`planned`, unchanged shape) and otherwise delegates to
`provider_async.launch_provider_setup`, passing a
`provider_async.ProviderSetupJob(request=…, contract=…, write_state_file=…, settings_cleanup=…)`
and returning `starting` with the progress
file. The settings path transfers to the launcher's cleanup only when
`provider_setup_config.unlink_settings_after_setup` is set (the application entry point's
temp-file ownership handshake). `prepare_providers_for_start` remains as the
facade/CLI wrapper composing both halves in one call. Contract construction moved
out to `start_contract.py`: it validates `args.leaf_id or args.worktree_name`
through the shared leaf-ref resolver, persists the canonical task doc id into
the leaf contract, and returns a loud `leaf-ref-not-found` / `leaf-ref-ambiguous`
`WorktreeCommandResult` before any worktree write when the ref cannot resolve.
`_provider_start_paths` asserts
`args.provider_setup_config` is non-`None`, before use. Provider setup remains typed through `ProviderSetupRequest`; there is
no coordinator script or host-binary fallback path here. `provider_setup.load_settings`
and `provider_setup.settings_path` are now called with the settings path alone
(the `target_coordination_root` argument was dropped). CLIVE L2 moves provider enablement and
settings-readability classification to
`start_provider_preflight.provider_enablement_state`; `start.py` consumes that focused result
instead of retaining a private enablement helper.

Slice 5e (§5.4) adds pre-contract start observability: the start path calls `_record_start_block` at
each of the three blocked early returns — stale-base (`stale-base-blocked`), external-memory
(`memory-blocked`), and provider-plan (`provider-blocked`) — writing a transient `start-progress.json`
(via `worktrees/start_progress.write_start_progress`) so a start gated *before* its contract exists is
visible to the dashboard; `_clear_start_block` removes it once `write_contract` lands (the contract
then anchors the enclosure). Slice 5f S6 (§9) closes the happy-path gap: `_record_start_progress`
(non-blocked, `blocked_reason` stays None) emits a beat at the two pre-contract success points —
`preflight` (after the preflights pass) and `code-worktree` (after `ensure_worktree`) — so the
enclosure is observable assembling rather than popping in at contract-write. All three helpers are
best-effort and skipped on dry runs, so the start flow never fails on observability.

Since 260731-EFA-L2 both recorders take a `StartBeat` (from `worktrees.start_progress`) instead of
loose `phase`/`reason`/`completed`/`choices` keywords —
`_record_start_block(context, contract, args, beat)` and
`_record_start_progress(context, contract, args, beat)` — and the enclosure half of the payload is
built once by `_starting_enclosure(contract, worktree_name) -> StartingEnclosure`, the contract's
own front-matter facts for a start that has not written a contract yet. A blocked beat is a
`StartBeat` whose `blocked_reason` is set; a happy-path beat leaves it `None`. The two recorders
are otherwise identical, which is exactly what the shared beat type makes visible.

When an existing contract is found on disk, `_existing_contract_result` checks its
`cleanup` field: if `cleanup` is `abandoned` (a tombstone) or `reopened` (a reset) its
worktrees and branches were already discarded, so start recreates fresh rather
than attaching to the dead binding. With `args.retry_provider_setup` set, an
existing live contract routes to `_retry_provider_setup_result` instead of
attaching: refused (exit 2, poll hint) while
`provider_async.provider_setup_running` reports a fresh heartbeat, otherwise
the preflight + launch re-run against the existing contract and the result is
`provider-setup-retried` — the recovery path for failed or stale background
setups.

The stale-base preflight (issue #54) runs inside `_preflighted_contract`, after the
existing-contract short-circuit and before the long-path preflight: `_stale_base_preflight`
reads `kernel.git_freshness` for the code source branch and (external mode)
the memory source branch, and blocks (exit 2,
`choose_stale_base_recovery`, required arg `stale_base_choice`) when either is
`behind` or `diverged` from its upstream — a stale base produces wrong code
and silently defeats the CGC seed fast-path. `unknown` (offline fetch) and
`no-upstream` never block. Recoveries: `proceed-stale` skips the check;
`fast-forward` routes through `_fast_forward_stale_branches` (checked-out
branch → `merge --ff-only`; parked branch → `branch -f`, safe because state
`behind` proves ancestry; diverged or worktree-pinned branches land back in
`staleBases` with a `recovery_error`). After a fast-forward recovery
`_preflighted_contract` rebuilds the contract so recorded base commits reflect the
recovered tips, and returns the rebuilt one.

`prepare_memory_for_start` opens with `_memory_source_state(contract, args)` (260731-EFA-L2) — the
state that settles the memory side **before its ledger is ever read**: either there is no external
memory repo to prepare (`internal` / `disabled`), or the one configured cannot be started from
(absent → `_missing_memory_repo_state`, or dirty in its official checkout →
`_dirty_memory_source_state`). A non-`None` return is the whole result; `None` means proceed to the
ledger.

The **ledger-mapping gate** in `prepare_memory_for_start`: when `find_mapping(ledger,
code_base_commit)` is `None` (the code base is a SHA the ledger never recorded — e.g. two
code-only owner commits ahead of the last memory closeout), `_rebased_on_mapped_commit(contract,
ledger, args)` owns the recovery and returns either the rebound `(contract, ledger)` pair or the
`dict` state that blocks the start. It
consumes BOTH advertised choices (260703-L18 finding 7 / friction F-R; previously only
`disabled-memory` was wired and `reconciliation`/`custom` dead-ended). `disabled-memory`
drops external memory; `memory_choice="reconciliation"` calls `_reconcile_missing_mapping`,
which FIRST requires the official memory repo's checked-out branch to BE the contract's memory
source branch (PR #100 review, Codex P1: the worktree is created FROM that branch, so committing
to whatever is checked out would leave the source branch unmapped while start reports compatible —
it refuses loudly with a `LedgerError` naming both branches), then records the mapping the way
closeout ledger syncs do — `prepend_mapping(ledger,
code_base_commit, ledger.last_memory_content_commit)` (memory CONTENT tip unchanged; header
`lastVerifiedCodeCommit` advances) written to the OFFICIAL memory repo's `memory.md`, `git
add` + a `[<task_id>] Ledger sync: <code> -> <memory>` commit in the memory SOURCE repo
(mirroring `memory/carryover.py` and the owner's hand precedent, memory commit `af50a05`) —
then advances the contract's `memory_base_commit` to the post-reconciliation tip (threaded
back via `reconciledMemoryBaseCommit` → `_contract_after_memory_start`) and PROCEEDS to a
started worktree on the now-present mapping. `_missing_mapping_state` advertises only the two
executable choices (`custom`, wired nowhere, was removed). A dry-run reconciliation records
nothing and just reports `compatible`.

`_ensure_memory_source_branch` (issue #54) runs inside
`prepare_memory_for_start` after the ledger mapping gate: a missing external
memory source branch is auto-created at the validated official checkout tip
(`memory_base_commit`) using the code source branch name as template,
reported as `memorySourceBranch` (`existing` /
`created-from-official-tip` / dry-run `would-create-from-official-tip`) —
previously agents had to create that branch by hand or `ensure_worktree`
raised.

`prepare_memory_for_start` now also calls `_sync_worktree_memory_mtimes` after
preparing the memory worktree. `git checkout` stamps every file with the current
time; GrepAI's watcher skips unchanged files by `ModTime`, so brand-new mtimes
make every file look modified and force a full re-embed — defeating the DB clone.
`_sync_worktree_memory_mtimes` walks the freshly checked-out memory worktree,
finds each file's counterpart in the source memory repo, and calls `os.utime` to
copy the source mtime onto the worktree file. Files absent in the source are left
untouched and counted as `filesMissingInSource`. The `.git` subtree is skipped.
Since 260707-HFX-L2 files whose CONTENT diverges between the worktree checkout
and the source checkout are deliberately LEFT with their fresh checkout
mtimes: stamping the source's old mtime onto changed content made the watcher
skip exactly the delta — silent staleness — while fresh mtimes make GrepAI's
incremental scan re-embed precisely the divergence (a small diff becomes an
index UPDATE, never a full re-embed and never silent staleness).
`_memory_divergence_paths(source, target)` computes that changed-path set via
`git diff --name-only` of the two HEADs run in the source repo (worktrees
share its object database); equal heads yield the empty set, and `None`
(unrelatable heads) falls back to syncing everything — the pre-L2 behavior —
with a `divergenceState` note in the result rather than guessing. The guard's
scope is deliberately HEAD vs HEAD: uncommitted changes in the SOURCE
checkout sit outside it, and the mtime copied from such a dirty file is at
least as new as its content, so the watcher still re-embeds it —
over-embedding, never silent staleness. The payload
counts `divergentLeftFresh` beside `filesSynced`/`filesMissingInSource` and is
returned as `mtimeSync` in the `prepare_memory_for_start` payload.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- Attach activates and reconciles an atomic leaf's exact parent before returning the workbench. [1]
- The renamed parent-series resolver both start-side guards now call (attach at code line 177, the `_plan_start_enclosure` preflight at code line 703); it resolves and validates the exact parent series and no longer accepts or refuses leaves. [2]
- The end-to-end playthrough that proves a leaf commanded after a checkpoint landing still starts. [3]
- Series status carries a read-only activation observation while the facade leaves selection mutation to the transaction. [4]
- The selecting transaction owns the per-contract reconciling-to-active transition rather than this public facade. [5]
- Defines the `WorktreeArgs` dataclass that types every start/attach/status input. [6]
- Provider setup requests are implemented by the providers package. [7]
- Background launcher and status projection. [8]
- Branch freshness facts come from the shared kernel. [9]
- `recovery_guidance` and the `RecoveryOperation` vocabulary the three blocked starts belong to, plus `next_guidance`/`status_payload` for the phase side. [10]
- `ContractCells` / `amend_contract`, the typed path every vocabulary-cell write takes. [11]

### Cross-Repo References

No meaningful cross-repository reference applies beyond the explicitly configured code/memory
pair already documented by the repository-owned contract.

## Series-Contract Notes

For master task starts, `start_contract.py` creates or loads the root series contract, creates the
integration branch from the protected/source branch, selects and reconciles that exact series, and
only then builds the leaf contract from the integration branch with canonical doc-id `leaf_id`
recorded. Multiple root series contracts may remain live; selection is that one contract's own
`reconciling -> active` activation transition — never a global contract census, and never a claim on
a shared protected source pair. Both root and leaf `memory_base_commit` values come from
`memory_base_for_source` — the tip of the **memory source branch** the worktree is created from, not
the memory repo's ambient HEAD.

## L23 Pre-Mutation Lineage Gate

Attach, existing-contract reuse, and leaf start now prove applicable ancestry
before stale context is resumed or start state is mutated. Parent lineage runs
before the separate stale-base preflight, so `proceed-stale` cannot override a
super-to-master structural gap; blocked progress is recorded as
`source-lineage-blocked`.

## 260815-DAG-L3 Start Publication, Replaced By Task CAS

Leaf start still restamps the current lifecycle id, but CLIVE removed the queue-bound publisher.
Start now competes only with task-plane mutations such as discard-unstarted under the short task CAS;
after accepted task truth publishes, affected projections are refreshed independently.

## 260815-DAG-L4 Integration-Authority Impact

Task-derived integration refs remain mechanically non-ordinary. The exact configured locator and
task CAS remain the leaf publication boundary; the parent atomic series is separately selected and
reconciled under repository integration authority in its own contract-keyed activation record before
start/attach exposes the leaf. A mutable queue lane is absent from both decisions.

## 260821-CLIVE-L2 Current Contract

The current source seams include `ProviderStartPaths`, `load_contract_from_args`, `contract_path_from_args`. New enclosures publish the strict root manifest, canonical journal directory, and locked address-only locator before exposure or operation admission. Pre-existing readable enclosures require the explicit adoption route; start never infers or falls back.

### Reconciled Source Evidence

- The current module exposes `ProviderStartPaths`, `load_contract_from_args`, `contract_path_from_args` at this ownership boundary. [12]

## 260821-CLIVE Start Reservation And Task-CAS Boundary

Leaf publication still competes with discard-unstarted under the short task-publication CAS. It proves the exact
current parent/leaf binding and reserves the configured contract locator before code, memory,
provider, or lifecycle task mutation. Parent-series selection is a preceding contract-keyed activation
operation, not part of this task-authoring CAS.
Memory preparation must reproduce the reserved contract bytes or refuse. Lifecycle task restamping
uses the shared task-fact publisher and returns independent projection effects. Retry converges on
the same reservation; conflicts name task-authority or recovery actions. A successor start requires
the exact restartable terminal predecessor, never an inferred missing root.
