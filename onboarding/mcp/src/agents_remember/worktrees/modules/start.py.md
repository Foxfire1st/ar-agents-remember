# mcp/src/agents_remember/worktrees/modules/start.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/start.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T18:40+02:00 |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063` |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
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
`argparse.Namespace`; `import argparse` is gone. `start_result()` resolves
context, builds the default contract, prepares code and optional memory
worktrees, runs the synchronous provider preflight, writes the contract for
real starts, and then LAUNCHES provider setup in the background (GitHub #53).
The ordering is deliberate: the contract is the durable anchor
`worktree_status` polls while the setup thread runs, so it must exist before
the launch. `plan_providers_for_start` is the sync preflight (skip /
enablement / settings checks — config-level failures still block the start
fast); `run_or_launch_provider_setup` keeps dry runs fully synchronous
(`planned`, unchanged shape) and otherwise delegates to
`provider_async.launch_provider_setup`, returning `starting` with the progress
file. The settings path transfers to the launcher's cleanup only when
`provider_setup_config.unlink_settings_after_setup` is set (the controller's
temp-file ownership handshake). `prepare_providers_for_start` remains as the
facade/CLI wrapper composing both halves in one call. `_build_start_contract`
asserts `args.task_name`/`args.worktree_name` are non-`None` and stamps
`args.lifecycle_id` into the contract (slice 2c — the observable-lifecycle
enclosure anchor, default `""`), and `_provider_start_paths` asserts
`args.provider_setup_config` is non-`None`, before use. Provider setup remains typed through `ProviderSetupRequest`; there is
no coordinator script or host-binary fallback path here. `provider_setup.load_settings`
and `provider_setup.settings_path` are now called with the settings path alone
(the `target_coordination_root` argument was dropped), and the dead
`_cgc_enablement_state` helper was removed in favour of the unified
`_provider_enablement_state`.

Slice 5e (§5.4) adds pre-contract start observability: `start_result` calls `_record_start_block` at
each of the three blocked early returns — stale-base (`stale-base-blocked`), external-memory
(`memory-blocked`), and provider-plan (`provider-blocked`) — writing a transient `start-progress.json`
(via `worktrees/start_progress.write_start_progress`) so a start gated *before* its contract exists is
visible to the dashboard; `_clear_start_block` removes it once `write_contract` lands (the contract
then anchors the enclosure). Slice 5f S6 (§9) closes the happy-path gap: `_record_start_progress`
(non-blocked, `blocked_reason` stays None) emits a beat at the two pre-contract success points —
`preflight` (after the preflights pass) and `code-worktree` (after `ensure_worktree`) — so the
enclosure is observable assembling rather than popping in at contract-write. All three helpers are
best-effort and skipped on dry runs, so the start flow never fails on observability.

When an existing contract is found on disk, `start_result` now checks its
`cleanup` field: if `cleanup == "abandoned"` the contract is a tombstone whose
worktrees and branches were already discarded, so start recreates fresh rather
than attaching to the dead binding. With `args.retry_provider_setup` set, an
existing live contract routes to `_retry_provider_setup_result` instead of
attaching: refused (exit 2, poll hint) while
`provider_async.provider_setup_running` reports a fresh heartbeat, otherwise
the preflight + launch re-run against the existing contract and the result is
`provider-setup-retried` — the recovery path for failed or stale background
setups.

The stale-base preflight (issue #54) runs after the existing-contract
short-circuit and before the long-path preflight: `_stale_base_preflight`
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
`start_result` rebuilds the contract so recorded base commits reflect the
recovered tips.

The **ledger-mapping gate** in `prepare_memory_for_start`: when `find_mapping(ledger,
code_base_commit)` is `None` (the code base is a SHA the ledger never recorded — e.g. two
code-only owner commits ahead of the last memory closeout), the recovery block now
consumes BOTH advertised choices (260703-L18 finding 7 / friction F-R; previously only
`disabled-memory` was wired and `reconciliation`/`custom` dead-ended). `disabled-memory`
drops external memory; `memory_choice="reconciliation"` calls `_reconcile_missing_mapping`,
which records the mapping the way closeout ledger syncs do — `prepend_mapping(ledger,
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
The result is returned as `mtimeSync` in the `prepare_memory_for_start` payload.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Defines the `WorktreeArgs` dataclass that types every start/attach/status input. | [args.py](agents-remember/mcp/src/agents_remember/worktrees/modules/args.py) |
| Provider setup requests are implemented by the providers package. | [provider_setup.py](agents-remember/mcp/src/agents_remember/providers/provider_setup.py) |
| Worktree tests cover memory compatibility, disabled-memory choices, and dirty external-memory blocking. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Launcher, ordering, retry, and guard coverage for the async path. | [test_provider_async.py](agents-remember/mcp/tests/test_provider_async.py) |
| Background launcher and status projection. | [provider_async.py](provider_async.py.md) |
| mtime-sync unit tests cover matching-file sync, target-only file preservation, `.git` skip, and dry-run no-op. | [test_worktree_mtime_sync.py](agents-remember/mcp/tests/test_worktree_mtime_sync.py) |
| Stale-base preflight and memory-branch auto-template coverage (block, both recoveries, diverged, offline, memory side). | [test_worktree_stale_base.py](agents-remember/mcp/tests/test_worktree_stale_base.py) |
| Branch freshness facts come from the shared kernel. | [git_freshness.py](agents-remember/mcp/src/agents_remember/kernel/git_freshness.py) |

## Series-Contract Notes

For master task starts, `start.py` creates or loads the root series contract, creates the integration branch from the protected/source branch, and then builds the leaf contract from that integration branch with `leaf_id` recorded. Both the root and leaf `memory_base_commit` come from `_memory_base_for_source` — the tip of the **memory source branch** the worktree is created off (mirroring the code base), **not** the memory repo's current HEAD, which may sit on an unrelated in-flight branch and would record a divergent base that breaks closeout's "memory source branch moved" preflight; it falls back to the repo HEAD only when external memory is off or the source branch is not present yet.

## Update History

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
