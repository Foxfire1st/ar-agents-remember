# mcp/src/agents_remember/worktrees/modules/start.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/start.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns worktree start, attach, status result construction, and startup preparation
for external memory and providers. Since L11 the existing-contract branch recreates
fresh for `cleanup in {abandoned, reopened}` (a reopened leaf keeps its exact leaf
id), and after writing a leaf contract start restamps the leaf doc's `lifecycleId`
via `tasks.leaf_doc` so the doc follows the enclosure's fresh lifecycle.

## Code Commentary

Every entry point and helper takes the typed `WorktreeArgs` dataclass (imported
from `agents_remember.worktrees.modules.args`), replacing the former
`argparse.Namespace`; `import argparse` is gone.

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
   plan providers, write the contract, and launch setup.

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
(the `target_coordination_root` argument was dropped), and the dead
`_cgc_enablement_state` helper was removed in favour of the unified
`_provider_enablement_state`.

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

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the `WorktreeArgs` dataclass that types every start/attach/status input. | `WorktreeArgs` | mcp/src/agents_remember/worktrees/modules/args.py:20-82 |
| Provider setup requests are implemented by the providers package. | `ProviderSetupRequest`, `run_provider_setup` | mcp/src/agents_remember/providers/provider_setup.py:57-120; mcp/src/agents_remember/providers/provider_setup.py:547-555 |
| Worktree tests cover memory compatibility, disabled-memory choices, and dirty external-memory blocking. | `test_memory_base_for_source_uses_source_branch_tip_not_head`, `test_start_reports_compatible_external_memory`, `test_start_reports_internal_memory_mode`, `test_start_blocks_dirty_external_memory_source` | mcp/tests/test_worktree_support_tests_1.py:155-172; mcp/tests/test_worktree_support_tests_1.py:692-731; mcp/tests/test_worktree_support_tests_1.py:733-765; mcp/tests/test_worktree_support_tests_1.py:767-789 |
| Launcher, ordering, retry, and guard coverage for the async path. | `test_successful_setup_writes_state_file_and_finishes_ok`, `test_contract_is_written_before_provider_launch`, `test_retry_refused_while_setup_is_running`, `test_retry_relaunches_after_failure`, `test_cleanup_blocks_while_setup_running`, `test_abandon_blocks_without_force_while_setup_running` | mcp/tests/test_provider_async.py:100-123; mcp/tests/test_provider_async.py:221-264; mcp/tests/test_provider_async.py:323-331; mcp/tests/test_provider_async.py:333-358; mcp/tests/test_provider_async.py:371-379; mcp/tests/test_provider_async.py:381-389 |
| Background launcher and status projection. | `ProviderSetupJob`, `launch_provider_setup`, `provider_setup_status`, `provider_setup_running` | mcp/src/agents_remember/application/provider_runtime.py:59-70; mcp/src/agents_remember/application/provider_runtime.py:73-121; mcp/src/agents_remember/application/provider_runtime.py:124-147; mcp/src/agents_remember/application/provider_runtime.py:150-155 |
| mtime-sync unit tests cover matching-file sync, target-only file preservation, `.git` skip, and dry-run no-op. | `test_syncs_matching_files_to_source_mtime`, `test_target_only_file_is_left_untouched`, `test_git_dir_is_skipped`, `test_dry_run_changes_nothing` | mcp/tests/test_worktree_mtime_sync.py:51-57; mcp/tests/test_worktree_mtime_sync.py:59-61; mcp/tests/test_worktree_mtime_sync.py:63-66; mcp/tests/test_worktree_mtime_sync.py:68-71 |
| Index-lifecycle tests pin the divergence exclusion (real git worktree fixtures: divergent files stay fresh, equal heads sync everything). | `test_divergent_files_keep_fresh_mtimes`, `test_equal_heads_sync_everything` | mcp/tests/test_provider_index_lifecycle.py:365-399; mcp/tests/test_provider_index_lifecycle.py:401-417 |
| Stale-base preflight and memory-branch auto-template coverage (block, both recoveries, diverged, offline, memory side). | `test_behind_code_source_branch_blocks_with_recovery_guidance`, `test_fast_forward_recovers_non_checked_out_branch`, `test_fast_forward_recovers_checked_out_branch`, `test_fast_forward_cannot_recover_diverged_branch`, `test_offline_fetch_reports_unknown_and_does_not_block`, `test_behind_memory_source_branch_blocks`, `test_missing_memory_source_branch_is_created_from_official_tip` | mcp/tests/test_worktree_stale_base.py:42-59; mcp/tests/test_worktree_stale_base.py:75-91; mcp/tests/test_worktree_stale_base.py:93-108; mcp/tests/test_worktree_stale_base.py:110-127; mcp/tests/test_worktree_stale_base.py:129-137; mcp/tests/test_worktree_stale_base.py:139-152; mcp/tests/test_worktree_stale_base.py:156-184 |
| Branch freshness facts come from the shared kernel. | `read_branch_freshness`, `freshness_to_packet` | mcp/src/agents_remember/kernel/git_freshness.py:98-112; mcp/src/agents_remember/kernel/git_freshness.py:158-169 |
| `recovery_guidance` and the `RecoveryOperation` vocabulary the three blocked starts belong to, plus `next_guidance`/`status_payload` for the phase side. | `RecoveryOperation`, `recovery_guidance`, `next_guidance`, `status_payload` | mcp/src/agents_remember/worktrees/modules/guidance.py:37-48; mcp/src/agents_remember/worktrees/modules/guidance.py:129-143; mcp/src/agents_remember/worktrees/modules/guidance.py:146-169; mcp/src/agents_remember/worktrees/modules/guidance.py:450-452 |
| `ContractCells` / `amend_contract`, the typed path every vocabulary-cell write takes. | `ContractCells`, `amend_contract` | mcp/src/agents_remember/worktrees/worktree_contract.py:181-196; mcp/src/agents_remember/worktrees/worktree_contract.py:199-227 |

## Series-Contract Notes

For master task starts, `start_contract.py` creates or loads the root series contract, creates the integration branch from the protected/source branch, and then builds the leaf contract from that integration branch with the canonical doc-id `leaf_id` recorded. Both the root and leaf `memory_base_commit` come from `memory_base_for_source` — the tip of the **memory source branch** the worktree is created off (mirroring the code base), **not** the memory repo's current HEAD, which may sit on an unrelated in-flight branch and would record a divergent base that breaks closeout's "memory source branch moved" preflight; it falls back to the repo HEAD only when external memory is off or the source branch is not present yet.

## L23 Pre-Mutation Lineage Gate

Attach, existing-contract reuse, and leaf start now prove applicable ancestry
before stale context is resumed or start state is mutated. Parent lineage runs
before the separate stale-base preflight, so `proceed-stale` cannot override a
super-to-master structural gap; blocked progress is recorded as
`source-lineage-blocked`.

## Update History
- 2026-08-14T06:36+02:00 — L23 final candidate review: start admission proves transitive lineage
  before mutation, routes cleaned completed leaves through task-reopen planning, and delegates
  result projection to `start_result.py`. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented fail-closed ancestry admission before attach/start state changes; verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 20 initial citation findings (10 anchor, 0 prose, 10 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:47+02:00 — 260731-EFA-L4 curator: unlike L3's one-import diff, this leaf changed
  three things in the file and the card described none. (1) All three blocked returns —
  `_blocked_memory_start_result`, `_blocked_provider_start_result`, `_stale_base_preflight` — now
  call `recovery_guidance` instead of `next_guidance`; the module imports both, because
  `status_result` still goes through the phase machine. Recorded why the split exists: identical
  keys on the wire, but `next_guidance` is now narrowed to the vocabulary `WorktreeSummary`
  publishes, and these three payloads are blocks rendered as a `FlexibleToolResponse`, never
  lifecycle phases. (2) `status_result` wraps its payload in `dict(...)` because `status_payload`
  now returns a `TypedDict` and `WorktreeCommandResult.payload` is `dict[str, object]`, which a
  `TypedDict` is not assignable to. (3) `_contract_after_memory_start` writes `memory_mode` through
  `amend_contract(replace(contract, …), ContractCells(memory_mode="disabled"))` while `memory_state`
  stays on `replace` — the two look alike in the front matter, but only one has a vocabulary, and
  `replace` types `**changes` as `Any`. The contract produced is identical. Everything else — the
  three L2 stages, the stale-base recoveries, the ledger-mapping gate and reconciliation, the mtime
  sync and its divergence guard — was re-read against the current file and is unchanged. Added two
  reference rows. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T21:01+02:00 — 260731-EFA-L3 curator: No content impact: the leaf's whole diff to
  `start.py` is one import line — `run_git` moved out of the `modules.git` import block to
  `agents_remember.kernel.git_command`; `current_branch`, `head_commit`,
  `longest_tracked_path_length` and `require_git` still come from `modules.git`. This sidecar names
  no runner, subprocess style or timeout, so nothing in it became false. I re-verified the two body
  claims that do name git commands against the current file: `_fast_forward_stale_branches` still
  does `merge --ff-only` for the checked-out branch and `branch -f` for a parked one, still
  collecting a non-zero return into `staleBases` as `recovery_error`; and
  `_memory_divergence_paths` still computes the changed-path set with
  `run_git(source, ["diff", "--name-only", source_head, target_head])` in the source repo. Both
  still describe the code exactly.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0912`/`PLR0915`/`PLR0913`
  armed with no exemptions): `start_result` was split into `_existing_contract_result` (attach vs
  recreate), `_preflighted_contract` (stale-base, fast-forward rebuild, long-path — returns the
  possibly-rebuilt contract) and `_create_start_enclosure` (worktrees, memory, contract write,
  provider launch). `prepare_memory_for_start` gained `_memory_source_state` (the pre-ledger
  settling states) and `_rebased_on_mapped_commit` (the missing-mapping recovery).
  `_record_start_block` / `_record_start_progress` now take a `StartBeat`, with the enclosure half
  built once by the new `_starting_enclosure` helper; `run_or_launch_provider_setup` passes a
  `provider_async.ProviderSetupJob`. Every blocked payload, recovery choice and start-progress beat
  is unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-07T23:45+02:00 — 260707-HFX-L4R2: `start.py` now imports the public
  `start_contract.memory_base_for_source` helper for the reconciliation path instead of reaching across
  modules for a private helper. Verification metadata pinned until closeout stamps the 260707-HFX-L4
  commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: refactored worktree-start contract construction and
  leaf-ref normalization out of `start.py` into `start_contract.py`/`leaf_ref_start.py`; `start.py`
  now only calls the extracted builder and returns its leaf-ref refusal payloads. The file shrank rather
  than grew. Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T20:45+02:00 — 260707-HFX-L2 review follow-up: the mtime-sync narration makes the
  guard's HEAD-vs-HEAD scope explicit — uncommitted SOURCE-checkout changes sit outside it and
  can only over-embed (their copied mtimes are at least as new as their content), never go
  silently stale. Documentation nuance on the source docstring; behavior unchanged from the
  19:30 entry.
- 2026-07-07T19:30+02:00 — 260707-HFX-L2 (index lifecycle): `_sync_worktree_memory_mtimes` now
  leaves DIVERGENT-content files with their fresh checkout mtimes (new
  `_memory_divergence_paths` via git diff of the two heads in the source repo; `None` →
  sync-all fallback with a `divergenceState` note; payload gains `divergentLeftFresh`) — stamping
  old mtimes onto changed content made the watcher skip exactly the delta (silent staleness);
  fresh mtimes make grepai re-embed precisely the divergence. Verification metadata pinned until
  closeout stamps the HFX-L2 commit.
- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, finding 7 / friction F-R): implemented the
  missing-mapping recovery `memory_choice="reconciliation"` (`_reconcile_missing_mapping`) — records
  the unmapped code base -> the ledger's memory content tip in the OFFICIAL memory repo the same way
  closeout ledger syncs do (header advance + newest-first row + a `Ledger sync` commit in the memory
  source repo; mirrors the owner's hand precedent `af50a05`), advances the contract's
  `memory_base_commit` (via `reconciledMemoryBaseCommit` → `_contract_after_memory_start`), and
  proceeds to a started worktree. The missing-mapping block now also consumes `disabled-memory` and
  advertises ONLY those two executable choices (`custom`, wired nowhere, removed). Tests: every
  advertised choice is consumable; reconciliation produces a valid mapping + a started worktree.
  Verification metadata pinned until closeout stamps the L18 commit.
- 2026-07-07T06:10+02:00 — PR #100 review fix (Codex P1, merge `e358c4a`): `_reconcile_missing_mapping`
  gained a memory-source-branch guard — reconciliation refuses (`LedgerError` naming both branches)
  when the official memory repo is checked out on a branch other than the contract's memory source
  branch, instead of committing the mapping to the wrong branch. Body updated; post-merge onboarding
  refresh (developer-approved) verified against main @ e358c4a.
- 2026-07-03T00:30+02:00 — L11: recreate-fresh admits `cleanup: reopened` beside `abandoned`, and a post-write hook restamps the existing leaf doc's lifecycleId with the newly minted lifecycle (explicit linkage across restarts).
- 2026-06-29T23:18+02:00 — Memory-base fix (L3): `start.py` now derives both the root and leaf `memory_base_commit` from the memory source branch tip via `_memory_base_for_source` (mirroring the code base) instead of the memory repo HEAD, so a memory repo checked out on an unrelated branch no longer records a divergent base that breaks closeout's "memory source branch moved" preflight. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: start now creates or loads a root series contract for master tasks, creates the integration branch from the protected/source branch, starts each leaf from that integration branch, writes leaf contracts under `enclosures/<leaf-id>/series-contract.md`, and reports `enclosure_path`/`leaf_id`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-16T03:25 — Slice 5f S6 (§9): added `_record_start_progress` and called it at the two happy-path pre-contract success points (`preflight`, `code-worktree`) so a non-blocked start emits start-progress (previously only blocked early returns did); best-effort, dry-run-skipped, cleared by the existing `_clear_start_block` on contract write. Verification metadata pinned until closeout stamps the S6 code commit.
- 2026-06-15T19:35 — Slice 5e (§5.4): `start_result` records a transient start-progress file at the three pre-contract blocked returns (stale-base / memory / provider) via `_record_start_block`, and clears it on contract write via `_clear_start_block` — best-effort, dry-run-skipped — so a start gated before its contract is observable. Verification metadata pinned until closeout stamps the 5e code commit.
- 2026-06-13T18:45+02:00 — Slice 2c: `_build_start_contract` stamps `args.lifecycle_id` into the built contract (the observable-lifecycle enclosure anchor; `worktree_start_tool` resolves it and the controller promotes/adopts after start). Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-10T09:30+02:00 — Issue #54 sub-task B: added `_stale_base_preflight` (+ `_branch_freshness_findings`, `_fast_forward_stale_branches`) blocking starts on behind/diverged source branches with `stale_base_choice` recoveries, contract rebuild after fast-forward recovery, and `_ensure_memory_source_branch` auto-creating a missing memory source branch at the official tip.
- 2026-06-10T07:30+02:00 — GitHub #53: provider setup moved to a background launch. `prepare_providers_for_start` split into `plan_providers_for_start` (sync preflight) + `run_or_launch_provider_setup` (dry-run sync / real launch via `provider_async`); the contract write moved BEFORE the launch; `_run_provider_setup` became the request builder `_provider_setup_request`; `_started_result` summary names the background poll loop; added the `retry_provider_setup` path on existing contracts.
- 2026-06-10T00:40+02:00 — Added the Windows long-path preflight: on hosts with `LongPathsEnabled=0`, `start_result` blocks (exit 2) before creating worktrees when the projected worktree path plus the longest tracked path in the code or external-memory repo exceeds `WINDOWS_MAX_PATH_BUDGET` (250). The block payload reports the computed lengths and both remedies (enable long paths / shorter worktree name). `long_path_block_payload` is the pure, platform-independent decision; `_windows_long_paths_enabled` reads the registry and returns True off-Windows. Existing-contract attach still short-circuits before the preflight.
- 2026-06-02T16:24+02:00: Normalized skill references in this module to full lowercase skill names; the missing-external-memory guidance names `c-00-initialize-memory-repo` (confirmed in source `_missing_memory_repo_state`). Reference-style normalization; behavior unchanged.
- 2026-06-01T00:00+02:00 — `start_result` now detects abandoned contracts and recreates instead of reattaching. `prepare_memory_for_start` calls `_sync_worktree_memory_mtimes` to mirror source-repo file mtimes onto the freshly checked-out memory worktree, enabling GrepAI clone reuse. Updated Code Commentary.
- 2026-05-31T12:50+02:00 — Re-typed every `args` param from `argparse.Namespace` to the new `WorktreeArgs` dataclass (dropping `import argparse`), added `task_name`/`worktree_name`/`provider_setup_config` non-`None` asserts, switched `provider_setup.load_settings`/`settings_path` to the path-only signature, and removed the dead `_cgc_enablement_state` helper; corrected Code Commentary and added the args.py reference (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: `_load_memory_ledger` returns `MemoryLedger | dict[str, object]` so `prepare_memory_for_start` narrows the ledger before `find_mapping`/attribute access; behavior-preserving (commit `0549b28`).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
