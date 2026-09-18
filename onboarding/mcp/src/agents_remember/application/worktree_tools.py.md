# mcp/src/agents_remember/application/worktree_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/application/worktree_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Owning overview](overview.md)

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

## CCR-R12@v5 Current Transaction Boundary

The public worktree adapters preview, admit, observe, and control task-addressed closeout and
integration operations. Their normal transaction path preserves explicit developer approval,
candidate/source identity, lease ownership, and ref safety, then delegates mutation to the
detached worker and worktree owners. The path does not automatically run strict code quality,
memory quality, selected certification, curator coherence, or independent review; full suites are
only an explicit developer request. Repository certification-profile fields that remain in generic
request plumbing are not a normal closeout/integration execution gate.

## Code Commentary

### Logic

Closeout and resume normalize only code and memory messages. Integration and checkpoint
landing accept the contract, strategy, and preview choice; they do not ask for a ledger subject.
PR landing records the actual code and optional memory-content commits. Cache contents do not
select the candidate or supply publication authority at this adapter.

### Parameter Objects (260731-EFA-L2)

The module consumes the concept objects its callers pack from the dedicated
`worktree_tool_requests.py` owner. Each retains a documented meaning rather than a keyword list:

| Type | Meaning | Shared default |
| --- | --- | --- |
| `TaskIdentity(repo_id, task_name, worktree_name, leaf_id, parent_task, workflow_kind)` | Who the task is. `worktree_name` is the on-disk directory; `leaf_id`/`parent_task` place it in the task tree; `workflow_kind` is its document format (`light-task`/`chat-task`). | — |
| `TaskBases(source_branch, work_branch, memory_mode, memory_choice, stale_base_choice)` | What a started task is cut from, plus the answers that clear a refused base. | `DEFAULT_TASK_BASES` |
| `StartExecution(dry_run, skip_provider_setup, retry_provider_setup)` | How the start itself runs, and what happens to background provider setup. | `DEFAULT_START_EXECUTION` |
| `CloseoutCommitMessages(code, memory)` | The two possible commit messages. | — |
| `CloseoutApproval(intent_note, dry_run)` | The approval-bearing half, deliberately separate so a preview cannot read as an approved apply. | `PREVIEW_ONLY` |
| `FinalizeTaskDocs(task_doc_path, master_doc_path, subtask_number)` | The documents finalize reconciles. | `NO_TASK_DOCS` |

Resulting signatures: `worktree_start_tool(config, identity, *, bases, execution)`;
`worktree_attach_tool(config, task: TaskRef, *, on_unsaved)`; `worktree_status_tool(config, task:
TaskRef)` — both attach and status resolve through the shared `_task_ref_namespace(config, task)`
helper; the closeout pair take `(config, contract_path, messages[, approval])`; and
`lifecycle_finalize_task_tool(config, contract_path, *, docs, dry_run, teardown_providers)`.
`TaskRef` itself lives in `application/task_ref.py` and is shared with `resolve_context_tool`.

The hard-limit repair moved definitions only. `worktree_tools.py` imports the exact classes and
defaults and keeps the same function annotations/default objects, so the behavior below remains the
same plumbing with its arguments named. No parallel model, legacy reader, or fallback path exists.

`_START_ELIGIBILITY` is a module-level fact, not a policy: `{"requiresCheck": "not-performed"}` plus
the reason, published as the `eligibility` key on **every** `worktree_start` result (including the
`would-start` preview) and on the `lifecycle-switch-required` refusal. It exists because the tool
cannot check a leaf's declared dependencies at all — the `Requires` set lives in the plan document's
prose, not in the addressed leaf document — and the honest response is to say what was *not* verified
rather than to let a `would-start` preview read as an eligibility verdict (D-17). Also note that the
`lifecycle-switch-required` refusal's `summary` states the condition the gate actually tests: the
session's own current lifecycle is already bound to another enclosure, and **no other leaf,
enclosure or session can block a start**.

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
`contract_path` through configured-contract admission and forwards typed
`MemorySyncChoice`, typed `SyncResolutionAction` (`continue`/`cancel`), and `dry_run` to
`git_worktree_manager.sync_result`. The contract path, not a public operation id, addresses a
retained generation.

`worktree_status_tool` resolves the canonical locator before calling the legacy-shaped status
facade and independently observes the stable enclosure-root sync journal. When present it adds the
typed `syncOperation` projection even if contract reading later reports a missing or unreadable
contract. Lifecycle archive projection remains separate; neither task text nor closeout queue state
is used to reconstruct sync evidence.
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
CCR-R22@v1 (L22, commit `685f83c44055`) makes the repository certification profile part of the
typed plumbing: `worktree_integrate_tool` forwards
`require_repo(config, configured.contract.repo_name).certification_profile` into
`WorktreeArgs.certification_profile`, and `_worktree_closeout` plus `_worktree_namespace`
thread the same `repo.certification_profile` value, so the closeout and integration paths carry
the exact profile authority into `git_worktree_manager` without reading it from agentic settings
(the settings-level quality-gate executor was removed by the same commit).

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

## 260831-LOCR-L30/L34 Checkpoint Landing Entry Point

`worktree_checkpoint_landing_tool(config, *, contract_path, strategy="ff-only", dry_run=False)` cit:([`worktree_checkpoint_landing_tool`], mcp/src/agents_remember/application/worktree_tools.py:425-463) is the application entry point for the
partial-master landing route. It admits the configured contract, builds `WorktreeArgs` with
`approved=not dry_run` and the configured `gate_policy` (the same seam-guard pass-through
`worktree_integrate_tool` uses), and delegates to
`git_worktree_manager.checkpoint_landing_result(args, configured.contract)`.

The docstring was corrected by 260831-LOCR-L34, and the correction is the point rather than
cosmetics: it had said the route "drops only the two assumptions that the master is finished", which
was true of L30's intent and false of its behavior — the route also required the master to have
**closed out**, which is why it was unreachable from both directions. It now states that
`worktree_integrate` proves the master complete *and* that it has closed out, that an unfinished
master has none of those, that the checkpoint captures the master's own committed refs (the live
series code work branch tip and the live memory work branch tip), proves their source ancestry, lands exactly those, requires the same explicit developer approval (`dry_run=False`), and
keeps the master's worktrees, branches and enclosure.

**Residual naming collision this leaf could not clear (260831-LOCR-L37, recorded not fixed).** The
entry-point docstring above the code still reads "A master being paused has none of those" — the
pre-L36 sense of "paused", meaning an unfinished master. The **registered** description, which is what
an agent actually reads, was corrected by L36 and now says the route is a publication and that pausing
is a separate matter and is NOT this call; L37 then gave "paused" a real public meaning (a master whose
activation selection has been released). So the application docstring is the one surface still using
the retired word, and it sits in `mcp/src/`, which curation must not edit. Do not propagate its wording
here: an unfinished master is **unfinished**, a master landed at a checkpoint is **checkpointed**, and a
**paused** master is one stopped by `worktree_pause` with nothing published. Flagged for the code owner
rather than repaired by memory.

The entry point adds no behavior of its own beyond admission and argument building: whether the
master is eligible to land without being complete, which series authority runs, which refs are
captured and revalidated, and what state is recorded all live in
`worktrees/modules/integrate.py`'s `checkpoint_landing_eligibility`/`checkpoint_landing_result` and
`worktrees/series_closeout.py`'s `capture_series_checkpoint_refs`/`publish_series_checkpoint_under_authority`.
It does **not** run the
auto-land seat hook that follows a successful final `worktree_integrate_tool` call, because nothing
is being retired.

## 260831-LOCR-L37 Pause Entry Point

`worktree_pause_tool(config, *, contract_path)` is the application entry point for the stop-only
pause. It is the shortest adapter in this module on purpose: it admits the configured contract
through the shared `admit_configured_contract` gate (projecting a refusal with
`operation="worktree_pause"`), builds the same typed `WorktreeArgs` the other contract-addressed
entry points build — `contract_path` plus `config.orchestration.gate_policy` — and delegates to
`git_worktree_manager.pause_result(args, configured.contract)`.

It adds nothing else, and that is the contract: the entry point performs no Git, no ref move, no
commit, no landing and no ledger write, so reaching the stop cannot publish. It also runs no
auto-land seat hook, because nothing is being retired — the mirror of the checkpoint entry point
above, which skips that hook because nothing is finished.

The docstring carries the distinction an agent needs and states it in the route's own terms: the
stop publishes nothing and the master keeps its branches, worktrees, enclosure and unstarted
leaves; `worktree_checkpoint_landing` is the separate, explicitly requested **publication**, and
pausing never does that.

**The pause and the publication are two verbs with two entry points.** `worktree_checkpoint_landing_tool`
above lands a partial master's committed refs under an explicitly required developer approval;
`worktree_pause_tool` releases the master's atomic-series activation selection and hands the turn
back. Neither is reachable from the other, and no surface may present the stop as the publication
or the publication as the stop.

### Conventions

Application adapters admit configured contract addresses and pass typed requests to their operation owners. Publication and recovery decisions stay with those owners.

### Invariants And Boundaries

- Repo IDs must resolve through MCP settings; disallowed IDs and paths escaping
  `coordination_root` raise `AuthorityError` (via the `_guards` helpers).
- Contract paths and memory/source paths must stay under the configured
  coordination root unless a specific tool owns a setup target.
- Worktree operations call package services directly; CLI entrypoints remain
  print adapters.
- Sync status and control are contract-addressed. `resolution_action` is typed and the application
  facade must not invent a public operation-id selector or queue-derived lifecycle fallback.
- Stable sync journal evidence remains observable across contract read failure once the canonical
  lifecycle locator establishes the enclosure root.
- `worktree_start_tool`/`worktree_integrate_tool`/`worktree_cleanup_tool`/`lifecycle_finalize_task_tool` default
  `dry_run=False` (act-by-default); the `*_closeout_apply` application entry points keep
  `dry_run=False` paired with their `*_preview` tools. `dry_run=true` previews.
- Provider setup inside worktree start launches only under the live on-disk
  providers authority (containment R1): a disk-disabled or unreadable
  authority skips setup fail-closed and is surfaced via the
  `providersAuthority` result block; worktree creation itself is never blocked
  by the provider gate.
- `worktree_start` reports the eligibility check it does **not** perform
  (`eligibility.requiresCheck == "not-performed"`) on every result and on the
  `lifecycle-switch-required` refusal. A caller must not read a `would-start` preview as proof that a
  declared dependency has landed; the `Requires` lines are the owning seat's check.
- A lifecycle hint attached to a response must agree with that response's own address. The binder
  derives the hint from the addressed contract and **omits** a hint whose `nextArgs` paths name a
  different contract, rather than forwarding guidance that would send an operator to another
  enclosure.
- Completion-seat classification must NEVER be able to fail a completion edge that has already
  succeeded (260707-HFX-L9 F1 doctrine, carried into HFX2-L11): `_auto_land_completed_seats` wraps
  its ENTIRE body — contract load, catalog construction, `land_seats_for_leaf`, and the
  `log_landed_event` loop — in one `try: ... except Exception: return []`. Landing is an archive
  courtesy that rides the `worktree_integrate`/`lifecycle_finalize_task` edge; it is never itself a
  gate on that edge, and the current code achieves this by construction (guard wraps everything,
  catches everything, always returns `[]` on any failure rather than raising).

### Todos

No additional file-local TODO is established by this candidate review.

## Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source applies. | — | — |

## Repo-Internal References
`worktree_start_tool` marks the temp lifecycle settings file with
`unlink_settings_after_setup=True` and skips its own `finally` unlink when
`_settings_owned_by_background(result)` sees a providers state of `starting` —
the background setup thread reads the file and owns the unlink (GitHub #53).
The new `retry_provider_setup` flag is forwarded to the worktree layer, and the
provider timeout is `config.timeout_caps["providerSetupSeconds"]` (default
`DEFAULT_PROVIDER_SETUP_SECONDS`, 1800) instead of the docker-control 120 —
the documented setup cap now actually governs the worktree flow.

## CCR-R25 Route-Review Refusal Projection

The start/admission seam and direct closeout seam now translate the existing typed
`RouteReviewError` through the shared `route_review_refusal_fields`/`route_review_refusal_projection`
owner. An exact configured contract adds the contract-bound `task_doc` operation and arguments;
the required `review` payload remains caller-supplied in `nextRequiredArgs` and is never invented.
Certification refusals use the same projector when a `routeReview` finding is present, preserving
all original findings and gate-start facts. The catches remain narrow (`RouteReviewError` and
`CertificationContractError`); no broad fallback or task-document mutation occurs in this adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| Integration, checkpoint, landing recording, and resume normalize code/memory authority without ledger subjects. | `worktree_integrate_tool`; `worktree_checkpoint_landing_tool` | mcp/src/agents_remember/application/worktree_tools.py:371-422; mcp/src/agents_remember/application/worktree_tools.py:425-463 |
| Public status observes the stable journal through the canonical locator and preserves it in the result. | `worktree_status_tool` | mcp/src/agents_remember/application/worktree_tools.py:305-328 |
| Public sync forwards typed memory choice and continue/cancel control after configured-contract admission. | `worktree_sync_tool`; `_configured_control_refusal` | mcp/src/agents_remember/application/worktree_tools.py:347-364; mcp/src/agents_remember/application/worktree_tools.py:616-640 |
| The checkpoint landing entry point admits the contract and delegates the whole decision to the worktree layer. | `worktree_checkpoint_landing_tool` | mcp/src/agents_remember/application/worktree_tools.py:425-463 |
| The pause entry point admits the contract, builds the typed args with the configured gate policy, and delegates to the stop route; it performs no publication work of its own. | `worktree_pause_tool`; `_gate_policy_snapshot` | mcp/src/agents_remember/application/worktree_tools.py:466-495; mcp/src/agents_remember/application/worktree_tools.py:798-806 |
| Stable sync projection is read from the enclosure-root journal. | `observe_sync_operation`; `SyncJournalReadError` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:108-115; mcp/src/agents_remember/worktrees/sync_transaction_state.py:369-385 |
| Worktree service behavior is owned by the worktree manager and modules. | `agents_remember` | mcp/src/agents_remember/worktrees/git_worktree_manager.py:34 |
| Worktree response models define the public tool envelopes and context summary, including activation/admission fields and the checkpoint-landing envelope. | `WorktreeSummary`; `WorktreeCheckpointLandingResponse` | mcp/src/agents_remember/models/worktree.py:240-294; mcp/src/agents_remember/models/worktree.py:466-470 |
| Route-review refusals are projected once with exact contract guidance at start/admission and closeout. | `_worktree_closeout`; `route_review_refusal_projection` | mcp/src/agents_remember/application/worktree_tools.py:914-956; mcp/src/agents_remember/worktrees/route_review.py:183-250; mcp/src/agents_remember/worktrees/route_review.py:549 |
| Shared repo/path authority guards (`require_repo`, `require_within_coordination`). | `require_repo` | mcp/src/agents_remember/kernel/authority.py:20-28 |
| Lifecycle finalization behavior is delegated to the worktree finalizer module. | `finalize_result` | mcp/src/agents_remember/worktrees/modules/finalize.py:68-141 |
| The on-disk provider authority reload consumed before provider setup (containment R1). | `worktree_start_tool`; `reload_provider_authority`; `provider_setup_config` | mcp/src/agents_remember/application/worktree_tools.py:121-228; mcp/src/agents_remember/kernel/primitives/runtime_config.py:103-200; mcp/src/agents_remember/kernel/primitives/runtime_config.py:193-218 |
| `land_seats_for_task`, the document-owned seat-landing domain function the auto-land hook calls. | `land_seats_for_task` | mcp/src/agents_remember/serving/landing.py:13-32 |
| Manual retire eligibility/role policy remains owned by `retire_policy.py`. | `check_retire_authority`; `RetirePolicyError` | mcp/src/agents_remember/serving/retire_policy.py:21-22; mcp/src/agents_remember/serving/retire_policy.py:36-85 |
| `log_landed_event`, called once per landed entry after a successful auto-land. | `log_landed_event` | mcp/src/agents_remember/serving/seat_events.py:56-80 |
| `TerminalCatalog`/`terminal_catalog_path`, the seat catalog the auto-land hook reads and writes. | `TerminalCatalog` | mcp/src/agents_remember/serving/terminal_catalog.py:65-431 |
| `RetirementSettings`/`config.retirement` gating the two auto-land hooks. | `RetirementSettings` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:111-121; mcp/src/agents_remember/kernel/primitives/runtime_config.py:114-125 |
| None | `worktree_status_tool` | mcp/src/agents_remember/application/worktree_tools.py:305-328 |
| None | `finalize_result` | mcp/src/agents_remember/worktrees/modules/finalize.py:68-141 |
| Worktree service behavior is owned by the worktree modules, which this manager module re-exports. | `__all__` | mcp/src/agents_remember/worktrees/git_worktree_manager.py:99-173 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The facade's start entry point consumes the extracted task-start request types at this boundary. | `worktree_start_tool` | mcp/src/agents_remember/application/worktree_tools.py:121-228 |
| None | `worktree_start_tool` | mcp/src/agents_remember/application/worktree_tools.py:121-228 |

## 260821-CLIVE Final Public Worktree Boundary

`worktree_status` now has two strict routes: live locator→manifest→journal authority, or an exact
terminal locator→external archive/receipt plus surviving contract truth. Terminal status reports
archive-ready versus cleanup-completed and returns the original typed cleanup/abandon arguments as
the executable retry; a different retry input refuses. Cleanup and abandon use this same admission
instead of scanning a deleted enclosure. Closeout requests carry the shared grade/admission models,
but the task-addressed worker never makes the scheduling decision or claims a door: its enclosing
operation revalidates the journal, contract, and protected-ref authority.

## MCAR-L03 Closeout Application Boundary

Initial closeout apply now re-proves the external leaf pair before lifecycle admission and includes
that identity in its acknowledgement. Preview converts pair/coherence failure through the typed
domain projector, including the named field and exact repair route. The detached worker still
revalidates independently before mutation.

## 260915-KS-L23 Start Eligibility And The Response's Own Address

**The start gate now says what it checks, and what it does not (D-17).** The `lifecycle-switch-required`
refusal used to read *"worktree_start refuses to repoint the active persistent lifecycle"*, which
described a protection the tool does not implement and left a reader thinking one enclosure could
block another; it now names the real condition — a start binds the session's current lifecycle to the
new enclosure and leaves it non-fleeting, so the next start in that session refuses — and states
explicitly that no other leaf, enclosure or session can block a start. The unchecked half is
disclosed rather than implied: the module-level `_START_ELIGIBILITY` fact
(`requiresCheck: "not-performed"`) rides every start result and the refusal, because the `Requires`
set lives in the plan document's prose and nothing in the addressed leaf document carries it in
machine-readable form. The tool therefore does **not** gain a dependency check; it stops implying
that eligibility was part of what it verified.

**A response's next-step hint is bound to the response's own address (D-13).** `worktree_status`
answers an *addressed* contract, and the hint attached to its envelope must be that contract's: the
hint is derived from the addressed contract (`application/next_step.compute_next_step`) rather than
from a global "most recently published enclosure" cursor, and `application/tool_response.bound_next_step`
omits a hint whose `nextArgs` path fields contradict the response's own `contractPath` /
`enclosurePath`. Two contracts addressed in sequence therefore receive two different hints, and a
hint naming another contract is dropped rather than forwarded. The boundary is worth stating here
because it is the caller's carrier that decides: the binder only checks a response model that
declares an address, and `TaskDocResponse` declares neither field, so a hint on that carrier passes
through unchecked — a deliberate, pinned boundary rather than a silent one.

## Current Landed Composition

Status now delegates its contract/terminal projection to `application.worktree_status.project_contract_status`. Closeout apply forwards typed `corrective_dispositions` into durable admission, and certification contract refusals are translated through the shared certification refusal owner. Preview does not launch the operation.


## Cross-Repo References

No separate cross-repository implementation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external implementation source applies. | — | — |

## Update History
- 2026-09-18T18:04:10+00:00: 260915-KS-L23 residue clearance (seat A, follow-up): the three cells that name `worktree_start_tool` -- the containment-R1 provider-authority row, the L23-era "facade's start entry point" row and its duplicated `None` row -- were re-cited from `mcp/src/agents_remember/application/worktree_tools.py:103-200` to `:121-228`, the function's own extent. The retired span began inside the `_START_ELIGIBILITY` constant block (102-118) and stopped 28 lines short of the body's end; this card's own L23 history already named `121-228` as the live extent. This is the explicit disposition the two mechanically-projected reopen items ask for. Question (1): yes -- the construct at 121-228 supports each claim's words (`worktree_start_tool` is declared at 121-127 and consumes the on-disk provider authority at 164, before the provider setup config is built at 170-176). Question (2): the retired ranges arrived by mechanical anchor-range projection, and the two generated repair bullets that record them are deliberately **left in this history** rather than retired by hand, because retiring them would delete provenance this pass was told not to delete; those items therefore remain enforced until the closing commit's stamp makes the change invisible (D-29), and this entry is the curator's reading they asked for. No anchor, row or claim was deleted or reworded. Verification stamp not advanced.
- 2026-09-18T17:55:32+00:00: 260915-KS-L23 residue clearance (seat A): re-read the three reopened rows whose cited module is this card's own source and repointed the stale range; every claim's wording, anchor set and range shape kept. `worktree_sync_tool` from `mcp/src/agents_remember/application/worktree_tools.py:319-336` to `:347-364` (the entry point's own definition) and `_configured_control_refusal` from `:588-612` to `:616-640` (the refusal helper's own definition); `worktree_pause_tool`'s `_gate_policy_snapshot` from `:770-778` to `:798-806`; and `WorktreeSummary` from `mcp/src/agents_remember/models/worktree.py:233-287` to `:240-294` with `WorktreeCheckpointLandingResponse` from `:459-463` to `:466-470`. The paired halves that already held their anchors are unchanged (`worktree_pause_tool` at `:466-495`; the `worktree_integrate_tool`/`worktree_checkpoint_landing_tool` rows at `:371-422`/`:425-463`, whose ranges the L23 section's added lines did not move). Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `worktree_status_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:305-328. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `worktree_status_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:305-328. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:20+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded two response-surface corrections in this adapter. (1) **Item 8 (D-17):** `worktree_start`'s `lifecycle-switch-required` refusal no longer says it "refuses to repoint the active persistent lifecycle" — it states the condition it actually tests (a start binds the session's current lifecycle to the new enclosure, and *this session's* lifecycle is already bound to another one) and says plainly that no other leaf, enclosure or session can block a start; the tool also publishes `_START_ELIGIBILITY` (`requiresCheck: "not-performed"`) as `eligibility` on every start result and on the refusal, so a `would-start` preview no longer reads as a dependency verdict. The tool deliberately gains **no** `Requires` check, because that set is plan-document prose and is not machine-readable in the addressed leaf document. (2) **Item 3 (D-13):** documented that the hint attached to an addressed response is derived from that contract (`application/next_step.compute_next_step`) and that `application/tool_response.bound_next_step` omits a hint whose `nextArgs` path fields contradict the response's own `contractPath`/`enclosurePath`; also recorded the boundary — the binder can only check a carrier that declares an address, and `TaskDocResponse` declares neither, which is why that carrier's hint passes through unchecked. **No pre-existing claim in this card was falsified by either change** — the `providersAuthority` containment rule, the auto-land hooks, the checkpoint/pause entry points and the closeout/CILE boundaries are untouched — so the existing body above stands and the two new subjects were added as their own section plus three invariants. Existing citation ranges were left for the citation pass; noted drift from this change: `worktree_start_tool`'s module-level constant now sits at `102-118` and the function spans `121-228`, so every card range that begins at `103` is stale by the size of the inserted block.
- 2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): clamped mcp/src/agents_remember/worktrees/route_review.py:550 to mcp/src/agents_remember/worktrees/route_review.py:549, the range the cited construct now occupies
- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Aligned closeout, control, integration, checkpoint, and PR-recording adapters with code/memory outputs only. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.

- 2026-09-13T17:20:55+00:00: Generated citation repair: "def route_review_refusal_fields("; "def _worktree_closeout(" repointed to mcp/src/agents_remember/worktrees/route_review.py:253-253; mcp/src/agents_remember/application/worktree_tools.py:921-921. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: recorded the new `worktree_pause_tool` application entry
  point — configured-contract admission with `operation="worktree_pause"`, typed `WorktreeArgs` with
  the configured gate policy, delegation to `git_worktree_manager.pause_result`, no auto-land hook
  because nothing is retired, and no Git/ref/commit/landing/ledger work of its own — and stated that
  the stop and the checkpoint publication are two verbs with two entry points, neither reachable from
  the other. Added the entry point's reference row. Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-13T14:32+02:00 — Curator citation repoint after the contract-scoped atomic-series activation re-keying shrank `models/worktree.py`: the public envelope/context-summary row was rebound to `models/worktree.py:232-286`, `289-352` and `458-463`. Claim wording unchanged.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:50+00:00 — 260831-LOCR-L34: recorded the corrected entry-point docstring. It had
  claimed the route drops only the two "master is finished" assumptions, which omitted the
  **completed-closeout** requirement that made the route unreachable in both directions; it now
  states that `worktree_integrate` proves completion *and* a completed closeout, that a paused master
  has none of those, that the checkpoint captures the master's own committed refs and proves their
  ledger mapping, and that the explicit developer approval is unchanged. Also named the new owners
  (`checkpoint_landing_eligibility`, `capture_series_checkpoint_refs`) and re-derived the reference
  range (427-465 → 427-469). No behavior change in this file: docstring only. Verification metadata
  remains closeout-owned; no acceptance claim.
- 2026-09-13T08:49:05+00:00: Generated citation repair: "def route_review_refusal_fields("; "def _worktree_closeout(" repointed to mcp/src/agents_remember/worktrees/route_review.py:253-253; mcp/src/agents_remember/application/worktree_tools.py:889-889. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: added `worktree_checkpoint_landing_tool`, the
  application entry point that admits the configured contract, builds the arguments with the
  configured gate policy, and delegates to `checkpoint_landing_result`; recorded that it runs no
  auto-land seat hook because nothing is retired, and re-derived the shifted reference ranges.
  Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `worktree_status_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:277-300. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `worktree_sync_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:319-336. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `observe_sync_operation` repointed to mcp/src/agents_remember/worktrees/sync_transaction_state.py:369-385. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def route_review_refusal_fields("; "def _worktree_closeout(" repointed to mcp/src/agents_remember/worktrees/route_review.py:253-253; mcp/src/agents_remember/application/worktree_tools.py:846-846. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def reload_provider_authority(config: McpRuntimeConfig) -> ProviderAuthority:"; "def worktree_start_tool(" repointed to mcp/src/agents_remember/kernel/primitives/runtime_config.py:189-189; mcp/src/agents_remember/application/worktree_tools.py:103-103. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `worktree_start_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:103-200. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T15:06+02:00 — No content impact: mechanical citation re-derivation after the closeout auto-carry change shifted lines in `sync_transaction.py` / `sync_transaction_state.py`; the cited symbols and their meanings are unchanged.

- 2026-09-10T07:41:10+00:00: Generated citation repair: `worktree_status_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:285-308. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `worktree_sync_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:327-344. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "def route_review_refusal_fields("; "def _worktree_closeout(" repointed to mcp/src/agents_remember/worktrees/route_review.py:255-255; mcp/src/agents_remember/application/worktree_tools.py:927-927. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "def reload_provider_authority(config: McpRuntimeConfig) -> ProviderAuthority:"; "def worktree_start_tool(" repointed to mcp/src/agents_remember/kernel/primitives/runtime_config.py:189-189; mcp/src/agents_remember/application/worktree_tools.py:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `worktree_start_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:111-208. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "def route_review_refusal_fields("; "def _worktree_closeout(" repointed to mcp/src/agents_remember/worktrees/route_review.py:255-255; mcp/src/agents_remember/application/worktree_tools.py:972-972. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.
- 2026-09-08T16:24:06+02:00 — CCR-L38 preparation range refresh: narrowed the route-review refusal anchors to their current unique definitions and repointed the shifted start-tool coordinate. This is a mechanical source-range correction; verification metadata remains closeout-owned.
- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: recorded the narrow route-review refusal projection at start/admission and direct closeout, with exact-contract task guidance and no mutation. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `worktree_sync_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:339-356. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-06T22:41:21+00:00: Generated citation repair: "def reload_provider_authority(config: McpRuntimeConfig) -> ProviderAuthority:"; "def worktree_start_tool(" repointed to mcp/src/agents_remember/kernel/primitives/runtime_config.py:189-189; mcp/src/agents_remember/application/worktree_tools.py:123-123. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the certification_profile plumbing into WorktreeArgs from the repository scope (require_repo) across integrate/closeout/namespace helpers -- profile authority now travels with the typed args instead of a settings executor.


- 2026-08-30T05:55+02:00 — MCAR-L03 A005: closeout apply now reuses the canonical admission
  normalizer before exact-pair resolution, so omitted, empty, and whitespace-only enabled commit
  messages refuse before pair or competing-lifecycle state can obscure the input defect. The
  lease-owned admission repeats the same validation against current state.

- 2026-08-29T21:46+02:00 — MCAR-L03: exposed and prevalidated the exact pair at closeout apply
  admission while preserving worker revalidation. Verification remains closeout-owned.

- 2026-08-26T03:37+02:00 — Added typed contract-addressed sync continuation/cancellation and
  stable sync-journal status projection across contract read failure. Recorded the separation from
  queue and task planes. Verification remains post-Dagger/closeout-owned.

- 2026-08-24T21:43+02:00 — File-size repair: moved the seven request/default concepts to the single
  `application/worktree_tool_requests.py` owner. This facade still consumes the exact types and
  retains all worktree operation behavior; verified at source commit `23d35f77`.

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
