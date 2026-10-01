# mcp/src/agents_remember/application/worktree_tools.py

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

`worktree_checkpoint_landing_tool(config, *, contract_path, strategy="ff-only", dry_run=False)` cit:([`worktree_checkpoint_landing_tool`], mcp/src/agents_remember/application/worktree_tools.py:474-512) is the application entry point for the
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

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

No configured external domain source applies.

### Repo-Internal References
`worktree_start_tool` marks the temp lifecycle settings file with
`unlink_settings_after_setup=True` and skips its own `finally` unlink when
`_settings_owned_by_background(result)` sees a providers state of `starting` —
the background setup thread reads the file and owns the unlink (GitHub #53).
The new `retry_provider_setup` flag is forwarded to the worktree layer, and the
provider timeout is `config.timeout_caps["providerSetupSeconds"]` (default
`DEFAULT_PROVIDER_SETUP_SECONDS`, 1800) instead of the docker-control 120 —
the documented setup cap now actually governs the worktree flow.

### Cross-Repo References

No separate cross-repository implementation claim is made.

No external implementation source applies.

### Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

### Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.

## CCR-R25 Route-Review Refusal Projection

The start/admission seam and direct closeout seam now translate the existing typed
`RouteReviewError` through the shared `route_review_refusal_fields`/`route_review_refusal_projection`
owner. An exact configured contract adds the contract-bound `task_doc` operation and arguments;
the required `review` payload remains caller-supplied in `nextRequiredArgs` and is never invented.
Certification refusals use the same projector when a `routeReview` finding is present, preserving
all original findings and gate-start facts. The catches remain narrow (`RouteReviewError` and
`CertificationContractError`); no broad fallback or task-document mutation occurs in this adapter.

- Integration, checkpoint, landing recording, and resume normalize code/memory authority without ledger subjects. [1]
- Public status observes the stable journal through the canonical locator and preserves it in the result. [2]
- Public sync forwards typed memory choice and continue/cancel control after configured-contract admission. [3]
- The checkpoint landing entry point admits the contract and delegates the whole decision to the worktree layer. [4]
- The pause entry point admits the contract, builds the typed args with the configured gate policy, and delegates to the stop route; it performs no publication work of its own. [5]
- Stable sync projection is read from the enclosure-root journal. [6]
- Worktree service behavior is owned by the worktree manager and its worktree modules, which this manager module re-exports. [7]
- Worktree response models define the public tool envelopes and context summary, including activation/admission fields and the checkpoint-landing envelope. [8]
- Route-review refusals are projected once with exact contract guidance at start/admission and closeout. [9]
- **The closeout preview and closeout apply return paths now carry this leaf's final-output projection (ICR-R21@v1): the preview is decorated with the selected comparison generation and `prepared_is_reviewed_candidate`, the apply with the recorded receipt, and integration with the refs it landed — all attached after the Git transaction, so none of them can gate it.** [10]
- Worktree service behavior is owned by the worktree manager and modules. [11]
- Shared repo/path authority guards (`require_repo`, `require_within_coordination`). [12]
- Lifecycle finalization behavior is delegated to the worktree finalizer module. [13]
- The on-disk provider authority reload consumed before provider setup (containment R1). [14]
- `land_seats_for_task`, the document-owned seat-landing domain function the auto-land hook calls. [15]
- Manual retire eligibility/role policy remains owned by `retire_policy.py`. [16]
- `log_landed_event`, called once per landed entry after a successful auto-land. [17]
- `TerminalCatalog`/`terminal_catalog_path`, the seat catalog the auto-land hook reads and writes. [18]
- `RetirementSettings`/`config.retirement` gating the two auto-land hooks. [19]
- None [20]
- None [21]
- Worktree service behavior is owned by the worktree modules, which this manager module re-exports. [22]
- **The sync measures its own rebinding after the Git transaction and its contract write, so no review obligation can gate or refuse a completed sync (`ICR-R22@v1`); what it measured is a carrying sync's own resolved pair, published additively on the result.** [23]

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

- The facade's start entry point consumes the extracted task-start request types at this boundary. [24]
- None [25]

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

## 260921-ICR-L22 The Sync Measures Its Own Rebinding After The Transaction And Can Never Gate It

`260921-ICR-L22` (`ICR-R22@v1`) changes this adapter in two places and adds no measurement logic of its
own: one import (`:14`) and the sync entry point's final return. `worktree_sync_tool` (`:353-375`) now
builds the delegated result into `payload` (`:371`) and returns
`rebinding_result_block(configured.contract, payload)` (`:375`) instead of returning that result
directly; the module is **1030 → 1035 lines**.

**The order is the contract.** The block runs *after* the sync has finished its Git work and written
its contract, so the measurement never participates in the transaction's admission: a completed sync is
returned unchanged, and a review obligation can never become a gate on the Git transaction it
describes. Every failure is a state on the payload rather than a refusal — a capture the worktree
refused (`source-unmeasured`), an unreadable generation record, a filesystem that refuses the write,
and a payload that is not a carrying sync at all — because the owner,
`application/review_sync_rebinding.py`'s `rebinding_result_block` (`:316-323`), reports each of them as
a `state` and never raises.

**What is measured is a finished sync that carried the official line.** `resolved_pair_completed`
(`:196-220`) requires the operation, a successful result and one of the three carrying states, so a
preview (`would-sync`) and an `already-current` leaf are told apart by name rather than by a payload key
happening to be absent; and `record_review_sync_rebinding` (`:271-313`) measures the sync's own result
payload rather than re-reading the journal, re-running a merge or touching the parked candidate. A
published rebinding writes `review_rebinding` onto the result — the measured state, the generation it
supersedes with its binding and manifest digests, the reviewed and resolved candidate trees with the
code match fact, the knowledge state and digest on both sides, the successor action, and the durable
evidence reference with its read-back — while a sync with nothing to bind states that instead. The
field is additive: a caller that does not read it sees the sync result it always saw.


## Governing Overview

[governing overview](overview.md)
