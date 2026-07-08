# mcp/src/agents_remember/controllers/worktree_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/controllers/worktree_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-08T02:43+02:00                     |
| lastVerifiedCommitHash | `2322ffc15ef803ea29bf900beeae84de19b43019` |
| lastVerifiedCommitDate | 2026-07-08T03:14:39+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`worktree_tools.py` is the controller surface for worktree start, attach,
status, closeout preview/apply, integration, cleanup, and lifecycle finalization
tools. The direct
closeout preview/apply controllers (and the `_direct_closeout` helper) were
removed with the direct-closeout tool surface (issue #62): closeout is
worktree-only. Since L11 `worktree_abandon_tool` also ends the session's ambient
lifecycle when it anchors the abandoned worktree (an owner-written `lifecycle.ended`);
a lifecycle whose owner is gone is terminalized by the reducer from the contract's
`cleanup: abandoned` instead, honoring the event store's single-writer invariant.

## Code Commentary

The module resolves allowed repositories and coordination-contained paths from
`McpRuntimeConfig`, builds typed `git_worktree_manager.WorktreeArgs`, and
delegates lifecycle work to `worktrees.git_worktree_manager`. Repo resolution
and path confinement use the shared `_guards` helpers (`require_repo`,
`require_within_coordination`) so the security boundary lives in one place.
Worktree start can include provider setup by writing MCP-derived lifecycle
settings and handing a package-local provider setup config to the worktree
manager. Since 260707-HFX-L1 (containment R1) the boot-snapshot config is NOT
launch authority for that setup: `worktree_start_tool` calls
`reload_provider_authority(config)` first and writes the lifecycle settings
from the LIVE providers map (`authority.apply(config)`) only when the on-disk
map is readable and non-empty. An empty or unreadable (fail-closed) live map
skips provider setup outright — no settings file, no setup config — while the
worktree itself is still created. When the disk vetoed an armed boot snapshot
or the read failed, the result carries a `providersAuthority` block
(`source`, `bootSnapshotProviders`, and `error` when the read failed) so a
stale-snapshot session sees WHY setup was skipped instead of silently
diverging from its boot config. `worktree_start_tool` forwards
`stale_base_choice` (GitHub #54) into
`WorktreeArgs` for the stale-base preflight recovery; the controller adds no
behavior of its own. `worktree_sync_tool` (GitHub #54 sub-task D) is the
contract-path-based controller for the mid-task base sync: it confines
`contract_path` via `require_within_coordination` and forwards
`memory_sync_choice`/`dry_run` to `git_worktree_manager.sync_result`.
`lifecycle_finalize_task_tool` confines the contract and optional task-document
paths under the coordination root, builds `git_worktree_manager.FinalizeArgs`,
and delegates final readiness, cleanup, and task-document reconciliation to the
worktree finalizer.
260703-L4 also threads `config.orchestration.gate_policy` into closeout
`WorktreeArgs`, keeping the controller as typed plumbing while the closeout
module and controlplane enforce the policy. L8 cycle 6 extends the same
pass-through to `worktree_integrate_tool`: integrate `WorktreeArgs` now carry
the configured policy too (the dataclass default is all-human, which would
refuse the exact delegated master-handover approval the seam channel produces),
so both gate consumers evaluate the deployment's policy, not the default.

260707-HFX-L8 adds a completion-edge auto-retire hook to both success paths. After a successful
non-dry-run `worktree_integrate_tool` call (`result["ok"]` true), the controller — gated by
`config.retirement.auto_retire_on_integration` (default ON) — calls the new
`_auto_retire_completed_seats(config, confined_contract, roles=frozenset({"worker", "reviewer"}),
reason="leaf integrated into master", edge="leaf-integration")` and stores its return into
`result["autoRetiredSeats"]`. `lifecycle_finalize_task_tool` does the analogous thing on its own
success, gated by `config.retirement.auto_retire_on_finalize`, with
`roles=frozenset({"manager", "reviewer"})`, `reason="master finalized into super"`,
`edge="master-finalization"`. `worktree_integrate_tool` was refactored to bind
`confined_contract = require_within_coordination(...)` once (previously inlined directly into
`WorktreeArgs(...)`) so the same confined path is reused by the auto-retire call without
re-deriving it.

`_auto_retire_completed_seats(config, contract_path, *, roles, reason, edge) -> list[str]`
resolves the contract's own qualified leaf key
(`f"{contract.repo_name}/{contract.task_root.name}/{contract.task_id}"` via
`worktree_contract.load_contract`), builds a `TerminalCatalog` (at
`terminal_catalog_path(config.coordination_root)`) and a `TerminalHost`, calls
`retire.retire_seats_for_leaf(catalog, host, leaf_key=..., roles=roles, reason=reason, edge=edge,
at=now_iso())`, logs each retired entry via `seat_events.log_retire_event(config, entry)`, and
returns the retired session ids.

**F1 fix round (260707-HFX-L8, reviewer finding F1, LOW/MEDIUM):** the FIRST build round only
wrapped `load_contract` in a narrow `try/except (ContractError, OSError)`, leaving
`retire_seats_for_leaf`'s catalog file I/O (the `_read`/`_write` calls inside it can raise
`OSError`/JSON-decode errors) and the `log_retire_event` loop OUTSIDE any guard. That let a rare
catalog I/O fault propagate out of `worktree_integrate_tool`/`lifecycle_finalize_task_tool` and
make the TOOL report failure for an edge (branch integration / task-doc reconciliation) that had
already landed successfully. The fix, now in the code, widens the guard to wrap the ENTIRE helper
body — contract load through the `log_retire_event` loop — in a single `try: ... except Exception:
return []`, so nothing inside the helper can ever raise out of it.

Slice 2c wires the observable lifecycle here while the git module stays
observer-free: `worktree_start_tool` resolves a `lifecycle_id` (the active
lifecycle's id, or a fresh `new_ulid()` when none is active), threads it into
`WorktreeArgs`, and after `start_result` calls `_attribute_start` — promoting the
active lifecycle into the contract (`ambient().promote`) on a `started` result, or
adopting the minted id when none was active. `worktree_attach_tool` gains
`on_unsaved` and calls `_attribute_attach`, which drives `ambient().attach` (the
§1.3 resume table: adopt when none is active, no-op on the same id, auto-pause a
persistent current, route an unsaved fleeting through the save gate —
`SaveGateRequired` when `on_unsaved` is absent). Both helpers no-op when no
ambient is installed (CLI/tests).

## Invariants And Boundaries

- Repo IDs must resolve through MCP settings; disallowed IDs and paths escaping
  `coordination_root` raise `AuthorityError` (via the `_guards` helpers).
- Contract paths and memory/source paths must stay under the configured
  coordination root unless a specific tool owns a setup target.
- Worktree operations call package services directly; CLI entrypoints remain
  print adapters.
- `worktree_start_tool`/`worktree_integrate_tool`/`worktree_cleanup_tool`/`lifecycle_finalize_task_tool` default
  `dry_run=False` (act-by-default); the `*_closeout_apply` controllers keep
  `dry_run=False` paired with their `*_preview` tools. `dry_run=true` previews.
- Provider setup inside worktree start launches only under the live on-disk
  providers authority (containment R1): a disk-disabled or unreadable
  authority skips setup fail-closed and is surfaced via the
  `providersAuthority` result block; worktree creation itself is never blocked
  by the provider gate.
- Auto-retire must NEVER be able to fail a completion edge that has already succeeded (260707-HFX-L8,
  F1 doctrine): `_auto_retire_completed_seats` wraps its ENTIRE body — contract load, catalog
  construction, `retire_seats_for_leaf`, and the `log_retire_event` loop — in one
  `try: ... except Exception: return []`. Retirement is a cleanup courtesy that rides the
  `worktree_integrate`/`lifecycle_finalize_task` edge; it is never itself a gate on that edge, and
  the current code achieves this by construction (guard wraps everything, catches everything,
  always returns `[]` on any failure rather than raising).

## Repo-Internal References
`worktree_start_tool` marks the temp lifecycle settings file with
`unlink_settings_after_setup=True` and skips its own `finally` unlink when
`_settings_owned_by_background(result)` sees a providers state of `starting` —
the background setup thread reads the file and owns the unlink (GitHub #53).
The new `retry_provider_setup` flag is forwarded to the worktree layer, and the
provider timeout is `config.timeout_caps["providerSetupSeconds"]` (default
`DEFAULT_PROVIDER_SETUP_SECONDS`, 1800) instead of the docker-control 120 —
the documented setup cap now actually governs the worktree flow.


| Finding | Source Path |
| --- | --- |
| Worktree service behavior is owned by the worktree manager and modules. | [git_worktree_manager.py](agents-remember/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Worktree response models define the public tool envelopes and context summary. | [worktree.py](agents-remember/mcp/src/agents_remember/models/worktree.py) |
| Shared repo/path authority guards (`require_repo`, `require_within_coordination`). | [_guards.py](agents-remember/mcp/src/agents_remember/controllers/_guards.py) |
| Lifecycle finalization behavior is delegated to the worktree finalizer module. | [finalize.py](agents-remember/mcp/src/agents_remember/worktrees/modules/finalize.py) |
| The on-disk provider authority reload consumed before provider setup (containment R1). | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| Containment tests pin the worktree-start veto and the armed-path live-map launch. | [test_provider_containment.py](agents-remember/mcp/tests/test_provider_containment.py) |
| `retire_seats_for_leaf`, the seat-retirement domain function the auto-retire hook calls. | [retire.py](agents-remember/mcp/src/agents_remember/serving/retire.py) |
| Retirement eligibility/role policy consumed by `retire_seats_for_leaf`. | [retire_policy.py](agents-remember/mcp/src/agents_remember/serving/retire_policy.py) |
| `log_retire_event`, called once per retired entry after a successful auto-retire. | [seat_events.py](agents-remember/mcp/src/agents_remember/serving/seat_events.py) |
| `TerminalCatalog`/`terminal_catalog_path`, the seat catalog the auto-retire hook reads and writes. | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |
| `RetirementSettings`/`config.retirement` gating the two auto-retire hooks. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |

## Series-Contract Notes

Worktree start/attach/status controllers accept `parent_task` and `leaf_id` and report lifecycle attribution against `enclosure_path`, with `contract_path` retained only as the existing wire-compatible field.

## Update History

- 2026-07-08T02:43+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity + turn-state),
  INCLUDING the R2/F1 fix round: `worktree_integrate_tool` and `lifecycle_finalize_task_tool` now
  call the new `_auto_retire_completed_seats` helper on their own success (gated by
  `config.retirement.auto_retire_on_integration` / `auto_retire_on_finalize`), storing retired
  session ids into `result["autoRetiredSeats"]`; `worktree_integrate_tool` binds
  `confined_contract` once for reuse. The F1 fix round widened the helper's guard from just
  `load_contract` to the ENTIRE body (contract load through the `log_retire_event` loop) under one
  `try/except Exception: return []`, closing a gap where `retire_seats_for_leaf`'s catalog I/O or
  the event-log loop could otherwise raise out of an already-succeeded completion edge. Verification
  metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-07T16:30+02:00 — 260707-HFX-L1 (provider containment R1): `worktree_start_tool` now
  re-reads the on-disk authority (`reload_provider_authority`) before provider setup, writes the
  lifecycle settings from the LIVE providers map only when armed, skips setup fail-closed on an
  empty/unreadable live map (the worktree is still created), and attaches a `providersAuthority`
  veto block when the disk vetoed an armed boot snapshot or the read failed. Verification
  metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: `worktree_integrate_tool` now passes `gate_policy=config.orchestration.gate_policy` into `WorktreeArgs`, mirroring the closeout path (AR3-1(a)). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T12:32+02:00 — No route impact: 260703-L4 only forwards the parsed
  gate delegation policy from MCP config into worktree closeout args; controller
  domain boundaries and public tool surface are unchanged. Verification metadata
  pinned until closeout stamps the L4 commit.
- 2026-07-03T00:30+02:00 — L11: worktree_abandon ends its anchored ambient lifecycle via `_end_ambient_lifecycle_if_anchored`; the short-lived task_reopen controller moved out to task_doc_tools (task domain).
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: worktree start/attach/status controllers now accept `leaf_id` and `parent_task`, and lifecycle attribution prefers `enclosure_path` while keeping `contract_path` as a compatibility payload field. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Added `lifecycle_finalize_task_tool`: coordination-confined contract/task-doc paths are converted into `FinalizeArgs` and delegated to `git_worktree_manager.finalize_result`. The controller remains a path-authority and typed-argument facade; finalization behavior lives in `worktrees/modules/finalize.py`. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-13T18:45+02:00 — Slice 2c: wired the observable lifecycle. `worktree_start_tool` resolves + threads a `lifecycle_id` (active id or fresh mint) and `_attribute_start` promotes/adopts it after start; `worktree_attach_tool` gains `on_unsaved` and `_attribute_attach` drives the `ambient().attach` §1.3 resume table (adopt / no-op / pause+adopt / save gate). The git module stays observer-free; both helpers no-op without an ambient. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-11T06:47+02:00 — Removed `direct_closeout_preview_tool` / `direct_closeout_apply_tool` and the `_direct_closeout` helper (issue #62 worktree-only closeout); the controller surface is now start, attach, status, sync, closeout preview/apply, integrate, cleanup, abandon.
- 2026-06-10T09:56+02:00 — Added `worktree_sync_tool` (contract-path confinement + `memory_sync_choice`/`dry_run` forwarding to `sync_result`) for the GitHub #54 mid-task base sync.
- 2026-06-10T09:30+02:00 — `worktree_start_tool` forwards the new `stale_base_choice` recovery selector into `WorktreeArgs` (GitHub #54 stale-base preflight); plumbing only.
- 2026-06-10T07:30+02:00 — worktree_start async support (GitHub #53): the provider setup config now carries `unlink_settings_after_setup=True` and the controller skips its `finally` unlink when the result's providers state is `starting` (`_settings_owned_by_background`) — the background thread reads the temp settings file and owns the unlink. New `retry_provider_setup` flag forwarded to the worktree layer. The provider timeout switched from the hardcoded `DEFAULT_DOCKER_CONTROL_SECONDS` (120) to `config.timeout_caps['providerSetupSeconds']` (default `DEFAULT_PROVIDER_SETUP_SECONDS`, 1800) — the documented setup cap now actually governs the worktree flow (GitHub #58 evidence showed the 120s bound on seed exports).
- 2026-06-01T20:45+02:00 — Added `worktree_abandon_tool` to the controller surface and threaded the `teardown_providers` flag through `worktree_cleanup_tool` (behavior detail lives in `provider_tools.py.md`, `abandon.py.md`, `cleanup.py.md`).
- 2026-05-31T12:30+02:00 — Repo/path guards moved to shared `_guards` (require_repo/require_within_coordination) raising AuthorityError, and namespaces are now typed `git_worktree_manager.WorktreeArgs` instead of `argparse.Namespace` (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Re-verified against `825a172` after the 0.9.x provider/worktree run; the controller surface (start, attach, status, closeout preview/apply, direct closeout preview/apply, integrate, cleanup), its coordination-containment rules, and the act-by-default `dry_run` behavior still match the source. References (`git_worktree_manager.py`, `models/worktree.py`) verified present.
- 2026-05-28T19:52+02:00: Created when worktree MCP controllers moved into their own domain module.
