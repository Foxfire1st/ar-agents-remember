# mcp/src/agents_remember/application/worktree_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/application/worktree_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-24T15:04+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`worktree_tools.py` is the application entry point surface for worktree start, attach,
status, closeout preview/apply, integration, cleanup, and lifecycle finalization
tools. The direct
closeout preview/apply application entry points (and the `_direct_closeout` helper) were
removed with the direct-closeout tool surface (issue #62): closeout is
worktree-only. Since L11 `worktree_abandon_tool` also ends the session's ambient
lifecycle when it anchors the abandoned worktree (an owner-written `lifecycle.ended`);
a lifecycle whose owner is gone is terminalized by the reducer from the contract's
`cleanup: abandoned` instead, honoring the event store's single-writer invariant.

## Code Commentary

### Parameter Objects (260731-EFA-L2)

The module now defines the concept objects its callers pack, each with a documented meaning rather
than a keyword list:

| Type | Meaning | Shared default |
| --- | --- | --- |
| `TaskIdentity(repo_id, task_name, worktree_name, leaf_id, parent_task, workflow_kind)` | Who the task is. `worktree_name` is the on-disk directory; `leaf_id`/`parent_task` place it in the task tree; `workflow_kind` is its document format (`light-task`/`chat-task`). | — |
| `TaskBases(source_branch, work_branch, memory_mode, memory_choice, stale_base_choice)` | What a started task is cut from, plus the answers that clear a refused base. | `DEFAULT_TASK_BASES` |
| `StartExecution(dry_run, skip_provider_setup, retry_provider_setup)` | How the start itself runs, and what happens to background provider setup. | `DEFAULT_START_EXECUTION` |
| `CloseoutCommitMessages(code, memory, ledger)` | The three commit messages. | — |
| `CloseoutApproval(intent_note, dry_run)` | The approval-bearing half, deliberately separate so a preview cannot read as an approved apply. | `PREVIEW_ONLY` |
| `FinalizeTaskDocs(task_doc_path, master_doc_path, subtask_number)` | The documents finalize reconciles. | `NO_TASK_DOCS` |

Resulting signatures: `worktree_start_tool(config, identity, *, bases, execution)`;
`worktree_attach_tool(config, task: TaskRef, *, on_unsaved)`; `worktree_status_tool(config, task:
TaskRef)` — both attach and status resolve through the shared `_task_ref_namespace(config, task)`
helper; the closeout pair take `(config, contract_path, messages[, approval])`; and
`lifecycle_finalize_task_tool(config, contract_path, *, docs, dry_run, teardown_providers)`.
`TaskRef` itself lives in `application/task_ref.py` and is shared with `resolve_context_tool`.

The behaviour below is unchanged — this is the same plumbing with its arguments named.

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
`WorktreeArgs` for the stale-base preflight recovery; the application entry point adds no
behavior of its own. `worktree_sync_tool` (GitHub #54 sub-task D) is the
contract-path-based application entry point for the mid-task base sync: it confines
`contract_path` via `require_within_coordination` and forwards
`memory_sync_choice`/`dry_run` to `git_worktree_manager.sync_result`.
`lifecycle_finalize_task_tool` confines the contract and optional task-document
paths under the coordination root, builds `git_worktree_manager.FinalizeArgs`,
and delegates final readiness, cleanup, and task-document reconciliation to the
worktree finalizer.
260703-L4 also threads `config.orchestration.gate_policy` into closeout
`WorktreeArgs`, keeping the application entry point as typed plumbing while the closeout
module and controlplane enforce the policy. L9 cycle 6 extends the same
pass-through to `worktree_integrate_tool`: integrate `WorktreeArgs` now carry
the configured policy too (the dataclass default is all-human, which would
refuse the exact delegated master-handover approval the seam channel produces),
so both gate consumers evaluate the deployment's policy, not the default.

260707-HFX2-L11 changes the completion-edge hook from auto-retire to auto-land. After a successful
non-dry-run `worktree_integrate_tool` call (`result["ok"]` true), the application entry point — gated by
`config.retirement.auto_land_on_integration` (default ON) — calls
`_auto_land_completed_seats(config, confined_contract, roles=frozenset({"worker", "reviewer"}),
reason="leaf integrated into master", edge="leaf-integration")` and stores its return into
`result["autoLandedSeats"]`. `lifecycle_finalize_task_tool` does the analogous thing on its own
success, gated by `config.retirement.auto_land_on_finalize`, with
`roles=frozenset({"manager", "reviewer"})`, `reason="master finalized into super"`,
`edge="master-finalization"`. `worktree_integrate_tool` was refactored to bind
`confined_contract = require_within_coordination(...)` once (previously inlined directly into
`WorktreeArgs(...)`) so the same confined path is reused by the auto-land call without
re-deriving it.

`_auto_land_completed_seats(config, contract_path, *, roles, reason, edge) -> list[str]`
resolves the contract's own qualified leaf key
(`f"{contract.repo_name}/{contract.task_root.name}/{contract.task_id}"` via
`worktree_contract.load_contract`), builds a `TerminalCatalog` at
`terminal_catalog_path(config.coordination_root)`, calls
`landing.land_seats_for_leaf(catalog, leaf_key=..., roles=roles, reason=reason, edge=edge,
at=now_iso())`, logs each landed entry via `seat_events.log_landed_event(config, entry)`, and returns
the landed session ids. The helper does not construct `TerminalHost` and does not kill tmux:
successful completion is an archive classification, not cleanup.

**F1 fix round (260707-HFX-L9, reviewer finding F1, LOW/MEDIUM):** the FIRST build round only
wrapped `load_contract` in a narrow `try/except (ContractError, OSError)`, leaving
the catalog file I/O (the `_read`/`_write` calls inside the seat-classification helper can raise
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
  `dry_run=False` (act-by-default); the `*_closeout_apply` application entry points keep
  `dry_run=False` paired with their `*_preview` tools. `dry_run=true` previews.
- Provider setup inside worktree start launches only under the live on-disk
  providers authority (containment R1): a disk-disabled or unreadable
  authority skips setup fail-closed and is surfaced via the
  `providersAuthority` result block; worktree creation itself is never blocked
  by the provider gate.
- Completion-seat classification must NEVER be able to fail a completion edge that has already
  succeeded (260707-HFX-L9 F1 doctrine, carried into HFX2-L11): `_auto_land_completed_seats` wraps
  its ENTIRE body — contract load, catalog construction, `land_seats_for_leaf`, and the
  `log_landed_event` loop — in one `try: ... except Exception: return []`. Landing is an archive
  courtesy that rides the `worktree_integrate`/`lifecycle_finalize_task` edge; it is never itself a
  gate on that edge, and the current code achieves this by construction (guard wraps everything,
  catches everything, always returns `[]` on any failure rather than raising).

## Repo-Internal References
`worktree_start_tool` marks the temp lifecycle settings file with
`unlink_settings_after_setup=True` and skips its own `finally` unlink when
`_settings_owned_by_background(result)` sees a providers state of `starting` —
the background setup thread reads the file and owns the unlink (GitHub #53).
The new `retry_provider_setup` flag is forwarded to the worktree layer, and the
provider timeout is `config.timeout_caps["providerSetupSeconds"]` (default
`DEFAULT_PROVIDER_SETUP_SECONDS`, 1800) instead of the docker-control 120 —
the documented setup cap now actually governs the worktree flow.


| Finding | Anchor | Source |
| --- | --- | --- |
| Worktree service behavior is owned by the worktree manager and modules. | "from agents_remember.worktrees.modules.finalize import FinalizeArgs" | mcp/src/agents_remember/worktrees/git_worktree_manager.py:31-37 |
| Worktree response models define the public tool envelopes and context summary. | `WorktreeSummary`, `WorktreeCommandResponse` | mcp/src/agents_remember/models/worktree.py:101-150; mcp/src/agents_remember/models/worktree.py:153-178 |
| Shared repo/path authority guards (`require_repo`, `require_within_coordination`). | `require_repo`, `require_within_coordination` | mcp/src/agents_remember/kernel/authority.py:20-28; mcp/src/agents_remember/kernel/authority.py:31-39 |
| Lifecycle finalization behavior is delegated to the worktree finalizer module. | `finalize_result` | mcp/src/agents_remember/worktrees/modules/finalize.py:58-157 |
| The on-disk provider authority reload consumed before provider setup (containment R1). | "def reload_provider_authority(config: McpRuntimeConfig) -> ProviderAuthority:", "def worktree_start_tool(" | mcp/src/agents_remember/application/worktree_tools.py:108-108; mcp/src/agents_remember/kernel/primitives/runtime_config.py:188-188 |
| Containment tests pin the worktree-start veto and the armed-path live-map launch. | "test_stale_armed_snapshot_is_vetoed_by_disk", "test_disk_armed_snapshot_launches_with_live_map" | mcp/tests/test_provider_containment.py:125-177 |
| `land_seats_for_task`, the document-owned seat-landing domain function the auto-land hook calls. | `land_seats_for_task` | mcp/src/agents_remember/serving/landing.py:13-32 |
| Manual retire eligibility/role policy remains owned by `retire_policy.py`. | `check_retire_authority` | mcp/src/agents_remember/serving/retire_policy.py:34-65 |
| `log_landed_event`, called once per landed entry after a successful auto-land. | `log_landed_event` | mcp/src/agents_remember/serving/seat_events.py:56-80 |
| `TerminalCatalog`/`terminal_catalog_path`, the seat catalog the auto-land hook reads and writes. | `terminal_catalog_path`, `TerminalCatalog` | mcp/src/agents_remember/serving/terminal_catalog.py:45-48; mcp/src/agents_remember/serving/terminal_catalog.py:51-408 |
| `RetirementSettings`/`config.retirement` gating the two auto-land hooks. | `RetirementSettings` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:110-120 |

## Series-Contract Notes

Worktree start/attach/status application entry points accept `parent_task` and `leaf_id` and report lifecycle attribution against `enclosure_path`, with `contract_path` retained only as the existing wire-compatible field.

## L23 Attach Attribution Guard

Ambient lifecycle attribution now occurs only when the worktree result is
actually `attached`. A source-lineage refusal can therefore return its blocked
evidence without being recorded as a successful attachment.

## L23 Lifecycle Model Package Review

The worktree application facade now imports lifecycle operation DTOs and policy snapshots from
`models.lifecycles.operation`. The facade's task-addressed arguments, attribution guard, and calls
into closeout/integration/finalization remain unchanged by that ownership move.

## 260815-DAG-L3 Generic Integration Boundary

`worktree_integrate_tool` remains a task-addressed operation launcher, not a scheduler. The
orchestrator may rank a disposable projection member, but the lifecycle plane binds the exact claimed
door/source journal before launch. This generic boundary cannot select or substitute a candidate,
and the detached worker revalidates the exact durable operation immediately before moving source
history.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-CLIVE-L1 Admission Boundary

Public closeout messages remain raw optionals only until the shared normalizer resolves the stable candidate and enabled/not-applicable plan. Preview and apply both return typed refusals; apply hands `start_or_observe_closeout_operation` only validated admission, while preview carries the same `effectiveInput`. Validation occurs before integration-authority observation, journal creation, worker launch, or Git. Projection selection remains independent and has no message-input authority.

## 260821-CLIVE-L2 Current Contract

The current source seams include `TaskIdentity`, `TaskBases`, `StartExecution`. Public worktree consumers branch on accepted versus refused configured-contract admission and pass the exact admitted contract onward. Mutation owners retain their existing authoritative reread and serialization; callers no longer enumerate lower reader exception families.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `TaskIdentity`, `TaskBases`, `StartExecution` at this ownership boundary. | L100-L113; L117-L131; L135-L142 | `mcp/src/agents_remember/application/worktree_tools.py` |

## 260821-CLIVE Final Public Worktree Boundary

`worktree_status` now has two strict routes: live locator→manifest→journal authority, or an exact
terminal locator→external archive/receipt plus surviving contract truth. Terminal status reports
archive-ready versus cleanup-completed and returns the original typed cleanup/abandon arguments as
the executable retry; a different retry input refuses. Cleanup and abandon use this same admission
instead of scanning a deleted enclosure. Closeout requests carry the shared grade/admission models,
but the task-addressed worker never makes the scheduling decision or claims a door: its enclosing
operation revalidates the journal, contract, and protected-ref authority.

## Update History

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: merged terminal archive status/retry and journal-owned closeout authority into the existing worktree-tool contract. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16 curator: re-anchored citation range(s) to current source after the L16 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: clarified the task-addressed integration launcher's
  non-scheduling role and final worker revalidation; verification remains closeout-owned.
- 2026-08-14T06:30+02:00 — L23 final candidate review: worktree application calls start or observe
  durable closeout/integration by canonical task identity and preserve candidate-bound route-review,
  lineage, and landing boundaries. Verification remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 curator: reviewed and recorded the lifecycle-operation package import
  move; application behavior is unchanged and final provenance remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented the state-qualified attach attribution boundary; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:59:59+02:00 — Curated 16 citation claims (8 table rows, 8 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: introduced `TaskIdentity`, `TaskBases`, `StartExecution`,
  `CloseoutCommitMessages`, `CloseoutApproval` and `FinalizeTaskDocs` (plus their shared defaults)
  and moved every controller's keyword list onto them; attach/status now take the shared `TaskRef`
  and resolve through one `_task_ref_namespace` helper. Behaviour, guards and result shapes are
  unchanged. Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-07-09T13:07+02:00 — 260707-HFX2-L11 (landed chat archive): successful
  `worktree_integrate_tool`/`lifecycle_finalize_task_tool` edges now auto-land matching seats into
  `result["autoLandedSeats"]` instead of auto-retiring them. The helper calls
  `serving/landing.py` + `log_landed_event`, does not create a `TerminalHost`, does not terminate tmux,
  and keeps the all-exceptions best-effort guard so completion cannot fail after the branch/task edge
  succeeded. Verification metadata remains pinned until closeout stamps the HFX2-L11 commit.

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

## Governing Overview

[governing overview](overview.md)
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.


## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
