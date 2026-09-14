# mcp/src/agents_remember/worktrees/modules/integrate.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/integrate.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Owns integration of completed worktree task branches back into their source
branches. Since 260831-LOCR-L30 it also owns the **checkpoint** route
(`checkpoint_landing_result`), which lands an unfinished atomic master's accumulated line into its
super branch without closing the master. Since 260831-LOCR-L34 that route captures and revalidates
its own candidate refs (`checkpoint_landing_eligibility` / `CheckpointLanding`) instead of reading
closeout cells it cannot have, and proves its ledger projection on the preview as well as the apply.

## CCR-R12@v5 Current Transaction Boundary

Normal integration validates the prepared code/external-memory pair, explicit handover approval,
source identity, and compare-and-swap/ref safety before protected publication. It does not run
strict code quality, memory quality, selected certification, curator coherence, or independent
review as part of the transaction; full suites are only an explicit developer request. Publication
uses the existing integration ref move (`update-ref`/tree publication through
`merge_integrated_commits`) and records the resulting pair; it creates no merge commit and hence
has no merge-hook path. Source movement refuses before protected refs move. The quality-altitude
material below is historical pre-R12 context.

## Code Commentary

The module validates closeout state, checks fast-forward eligibility, reports
blocked non-fast-forward cases, optionally replays code and memory content for
reviewed parallel changes, merges integrated commits, verifies the memory
ledger mapping, and updates integration fields in the contract.

**Historical pre-CCR-R12 quality altitude ladder (260731-EFA-L17/L24/L23 reopen).** Integration owned acceptance only at
master altitude. A leaf integration returns `certified-at-leaf-closeout` and lands the exact
closeout commit without calling the quality decider, settings loader, or Dagger executor again.
`quality_gate_mode` refuses leaf use and returns `GATE_FULL` only for series/master contracts.
`_run_integration_quality_gate` therefore runs `run_strict_code_quality_gate` once for master
integration, with the optional settings-owned memory cap and `master-integration` invocation.
Since CCR-R22@v1 (L22, commit `685f83c44055`) the quality preview and the full gate forward
`profile_reference=args.certification_profile` (the configured repository certification profile)
into `integration_quality`, so the master gate admits the exact repository-owned profile instead
of a settings executor; the old `requires_integrated_acceptance` repo-name policy was removed.
Dry-run reports the same ownership without executing it. A full-gate refusal returns
`blocked-quality-gate` before any source ref moves. `memory_quality_check` remains leaf-closeout
owned and is not repeated here. **`integration_quality.py` itself was deleted by the closeout-door cut
(commit `fad9808e`), so this entire ladder is now history with no live module behind it.**

**Two frozen parameter objects and one extracted phase (260731-EFA-L2):**

- **`IntegrationSources(current_code_source, current_memory_source, code_replay_required,
  memory_replay_required)`** — where each side's source branch stands when integration starts: its
  current head, and whether that head has already moved past the commit closeout landed (which is
  exactly what makes a fast-forward impossible and `--strategy replay` necessary). Head and verdict
  are read in the same breath per side and every consumer needs both.
  `IntegrationSources.replay_required` is a property (`code_replay_required or
  memory_replay_required`) — the ff-only block now reads `sources.replay_required` rather than
  re-OR-ing at the call site. `_integration_replay_requirements` returns it;
  `_blocked_non_ff_result` and `_dry_run_result` consume it.
- **`IntegratedCommits(code, memory_content, ledger)`** — the three commits one integration lands.
  Every step past the replay decision — the merge, the contract rewrite, the result payload —
  consumes all three or none, so `_merge_integrated_commits(contract, commits)` and
  `_integrated_result(contract, args, commits, *, handover_warning)` take the triple.
- **`_apply_integration(contract, args, sources, *, handover_warning, checkpoint=False)`** — the real
  (non-dry-run) path lifted out of `integrate_result`: land the code commit, then the memory commits,
  then merge both into their sources. `integrate_result` now reads as guard, replay decision,
  dry-run branch, delegate. Since 260831-LOCR-L30 it also selects the series authority and the
  recorded state from `checkpoint`.

The merge of integrated commits is all-or-nothing: both the code and memory
fast-forwards are pre-validated as ancestors before either branch is mutated,
and if the memory-side merge or ledger-mapping check fails after the code
branch has advanced, both branches are reset hard to their pre-merge heads
before the failure re-raises, so integration never leaves a half-integrated
state.

**Lineage and source-tip gate.** `integrate_result` refuses stale or unavailable transitive
super→master→leaf code/external-memory ancestry during preflight. `_apply_integration` then
re-proves that lineage and the exact code/memory source tips after the potentially long quality
gate, before replaying memory, and once more immediately before `source-merge`. Movement returns
`source-moved-during-quality` with a retry preview and performs no source ref movement; the quality
result therefore cannot certify a candidate assembled from older source tips.

**Contract writes go through `ContractCells` (260731-EFA-L4), and the landing cells through one
shared writer (260831-LOCR-L29/L30).** This module reaches the persisted vocabulary cells on two
paths:

- `blocked_integration_payload` via `integration/master_review_gate.py` —
  `amend_contract(contract, ContractCells(integration_status="blocked"))`
  cit:(["def blocked_integration_payload("], mcp/src/agents_remember/worktrees/integration/master_review_gate.py:14-14).
- The final and checkpoint integration cells via
  `modules/landing_record.py::record_landed_integration`, which owns the `ContractCells` amendment
  itself: `_integrated_result` passes `LandedIntegration(...)` alone (which selects
  `integration_status="completed", cleanup="pending"`) and `_checkpoint_result` passes the same
  record with `checkpoint=True` (which selects `checkpointed` and leaves `cleanup` untouched)
  cit:([`record_landed_integration`], mcp/src/agents_remember/worktrees/modules/landing_record.py:37-68).
  This module no longer amends those two cells inline — the writer is the single definition of
  "landed", and the commit triple, the strategy string and the checkpoint/final distinction all
  travel through it.

The typed record remains the reason the cells are safe to write: typeshed declares
`dataclasses.replace` as `**changes: Any`, so an off-vocabulary literal such as
`integration_status="bloqued"` was zero pyright errors even though the wire model rejects it. The
persisted contract is byte-identical either way. `replace` is still used for the free-text fields
(`integration_strategy` and the three commits), which have no vocabulary to be checked against —
now inside `landing_record.py` rather than here.

**Landing publishes the integration cell and stops (260831-LOCR-L31).** `_integrated_result`
cit:([`_integrated_result`], mcp/src/agents_remember/worktrees/modules/integrate.py:600-635) writes
the landed facts through the shared writer — `record_landed_integration` records
`integration_status="completed", cleanup="pending"` — reloads the contract so the payload's status
facts come from disk, and returns. It reclaims nothing, and the integrated payload no longer carries
a `"cleanup"` report key at all: the writer's return value is deliberately not bound, because
nothing downstream of it needed the amended contract.

**That ownership move is the fix, not a tidy-up.** Reclamation used to run here, inline, through
`automatic_cleanup.run_automatic_cleanup`. Because cleanup had already reached `completed` by the time
this function returned, the one guard that routes a landed leaf onward to `lifecycle_finalize_task`
(`next_step.py::_gate_after`, keyed on `contract.cleanup != "completed"`) could never fire. A real
landing therefore reported `nextOperation: "done"` while the leaf's task document stayed `planning`
and its master row stayed `inProgress` — and it did so silently, on leaves L29 and L30.
`lifecycle_finalize_task` now owns terminal reclamation and is the **only** route that reaches it;
`worktree_integrate` lands the refs and hands the task edge on.

Two wire-visible surfaces were re-worded to match, and neither is cosmetic:

- the dry run's `cleanup_reminder` now reads "On apply, the integration lands the refs; the code and
  memory worktrees are reclaimed when the task edge is finalized."
- the integrated payload's `summary` now reads "Integration completed; the refs are landed and the
  code and memory worktrees are reclaimed when the task edge is finalized."

The `cleanup` key on an integrated payload is now the untouched contract cell (`"pending"`), not a
report, so a caller cannot mistake a landing for a reclamation — and a refused or partial integration
still changes nothing, which is exactly when the enclosure evidence is still needed. The retired
`cleanup_question` key stays gone from both payloads.

## Current Source-Moved Guidance

`_blocked_non_ff_result`'s `source branch moved` guidance no longer points at
`--strategy replay`. It now routes the operator through `worktree_sync` for the owning contract,
then a retained code-or-memory conflict settlement (re-running the targeted test utility after code
resolutions), then a re-run of the closeout before retrying the integration. `replay` itself remains
a supported strategy and the memory-carryover vehicle; only this prompt moved. The sibling
integration-resolution handoff wording moved the same way — see
[`integration_resolution_handoff.py`](../integration/integration_resolution_handoff.py.md).

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wire vocabulary declares integration and cleanup states, including the `checkpointed` member this route's checkpoint path records. | "IntegrationStatus = Literal["; "CleanupStatus = Literal[" | mcp/src/agents_remember/models/worktree.py:38-39 |
| The typed contract amendment record holds the six optional vocabulary cells. | "class ContractCells:" | mcp/src/agents_remember/worktrees/worktree_contract.py:180-180 |
| The typed amendment helper preserves unspecified cells and applies supplied vocabulary values. | "def amend_contract(" | mcp/src/agents_remember/worktrees/worktree_contract.py:197-197 |
| This module reaches the persisted vocabulary writes through two owners: the blocked cell here and the landing cells in the shared writer the final and checkpoint results both call. | "def blocked_integration_payload("; `_integrated_result`; `_checkpoint_result` | mcp/src/agents_remember/worktrees/integration/master_review_gate.py:14-14; mcp/src/agents_remember/worktrees/modules/integrate.py:600-635; mcp/src/agents_remember/worktrees/modules/integrate.py:923-962 |
| Landing publishes the integration cell and stops: the refs are landed, no removal inventory is produced, and the payload's `cleanup` key is the untouched contract cell. Reclamation belongs to `lifecycle_finalize_task`, whose `_run_or_verify_cleanup` runs the same terminal procedure and shapes its report. | "def _integrated_result("; "are reclaimed when the task edge is finalized." | mcp/src/agents_remember/worktrees/modules/integrate.py:600-600; mcp/src/agents_remember/worktrees/modules/integrate.py:626-626; mcp/src/agents_remember/worktrees/modules/finalize.py:277-311 |
| A checkpoint landing records `checkpointed` through the same writer and reclaims nothing either, so the open master keeps its worktrees, branches and enclosure; an unfinished master landed at a checkpoint is never finalized. | `_checkpoint_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:923-962 |
| The checkpoint's one eligibility decision: it captures the master's own live refs, proves their ledger mapping, and is read by both the preview and the apply. | `CheckpointLanding`; `checkpoint_landing_eligibility`; `_route_commits` | mcp/src/agents_remember/worktrees/modules/integrate.py:388-421; mcp/src/agents_remember/worktrees/modules/integrate.py:424-469; mcp/src/agents_remember/worktrees/modules/integrate.py:510-521 |
| The landing proof is evaluated on the preview as well as the apply, for both routes, from one derived admission record. Since 260913-LCA-L11 the admission carries only the checkpoint's captured candidate: the route no longer selects a ledger-history form, because the landing no longer judges the tracked table. | `_require_ledger_projection`; `_landing_admission` | mcp/src/agents_remember/worktrees/modules/integrate.py:484-507; mcp/src/agents_remember/worktrees/modules/integrate.py:472-481 |
| The protected-ref edge names the operation it performs, so a checkpoint's ref-race payload routes the operator back to the checkpoint rather than to `worktree_integrate`. | `_publish_integration_edge`; `"nextTool": operation` | mcp/src/agents_remember/worktrees/modules/integrate.py:847-920 |
| The checkpoint preview reports the same eligibility the apply enforces. | `_checkpoint_dry_run_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:524-569 |
| The checkpoint route's series authority keeps every ref guard and drops only the completion assumptions, refusing an already-completed master and revalidating the captured candidate against the live refs. | `publish_series_checkpoint_under_authority`; `require_series_checkpoint_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:144-163; mcp/src/agents_remember/worktrees/series_closeout.py:166-197 |
| The source-moved refusal now routes recovery through `worktree_sync` plus a new targeted closeout, never through `--strategy replay`. | `_blocked_non_ff_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:319-336 |
| Historical/removed: leaf integration reused its closeout proof without calling a gate, and series/master integration alone ran the profile-declared full adapter, with an optional settings-owned cap and enclosure-owned reports. The cited `integration_quality.py` was deleted by the closeout-door cut (commit `fad9808e`). | — | — |


As of cycle 6 the master-exit seam consumer is re-addressed by MASTER identity: the pure `handover_gate_guard` helper folds EVERY gate log (`GateStore.all_current()` — the raiser's lifecycle differs from the integrating contract's) and selects `master-handover-approval` gates whose `enclosure` matches the contract's `task_name` or `parent_task_name`; the latest matching gate must be policy-valid-approved under the CONFIGURED policy (`args.gate_policy`, now threaded from the application entry point) or the non-dry run returns handover-gate-blocked. Gateless — no gate addressed to this master — stays additive. Cycle 7 makes the exact-string address and the preview honest (AR4-1b/AR4-2): the pure sibling `unmatched_handover_gate_warning` reports, when NO gate addresses this contract but open `master-handover-approval` gates exist in the fold, a `handover_gate_warning` payload field (`unmatched_open_gates` + a verify-the-enclosure-spelling note) on the dry-run and integrated results, so a typo'd enclosure is loud instead of silently gateless; and the guard is now EVALUATED on the dry-run path too — enforced only on the real run — with the preview carrying `handover_gate` (`permitted`/`gateId`/`reason`) and a summary naming `handover-gate-blocked` when the real run would refuse, while the dry-run path persists no contract mutation.

## R39 Integration Altitude

Leaf integration returns certified-at-leaf-closeout and never invokes the gate runner.
Series/master integration owns the single full Dagger acceptance before merge, passes the
self-repository required-wrapper policy, and revalidates lineage/source tips after the long run.
A missing Agents Remember wrapper or failed full result blocks before merge.

## 260815-DAG-L3 Integration Seam, Replaced By Journal Transfer

The final integration path does not claim, certify, or consume a mutable queue row. Since the
closeout-door cut this admission no longer binds a claimed closeout door or a source journal into an
integration intent — those modules were deleted. Admission is the request plus the branch/ref
authority checks, and the mutation
re-proves lineage, commit identity, and protected refs immediately before
publication. Recovery resumes the same journaled operation generation only from mechanically proven
evidence; a generic request cannot select or substitute another leaf. Projection refresh after the
canonical transition is downstream and disposable.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers,
and active atomic-series refs are censused across code and external memory. CLIVE narrows the live
integration boundary to exact journal/door authority, protected-ref CAS, and (for an atomic series)
the short landing lock; mutable queue serialization is not publication authority.

The final reversible preparation checks the accepted code/external-memory source-tip snapshot before
the broader lineage diagnostic. A concurrent protected-ref move therefore returns the structured
`source-moved-during-quality` refusal expected by the retry protocol, before irreversible progress;
the lineage check still follows when the exact snapshot remains current.

Fresh journaled integrations now enter the normal claim-and-publication path. Recovery publication
is attempted only when the durable operation carries recovery commits that exactly match the worker
input. A completed contract without that durable tuple may still be previewed read-only, but apply
refuses before protected publication; immutable integration authority or self-asserted completed
fields alone are not recovery evidence.

## 260821-CLIVE-L2 Current Contract

The current source seams include `handover_gate_guard`, `unmatched_handover_gate_warning`,
`blocked_integration_payload`. A waiting projection is admission evidence only. Since the
closeout-door cut the exact claimed door and source journal no longer transfer authority into the
integration journal here — that transfer module was deleted; the integration journal still owns its
own operation generation, and no door claim is matched on this path. The mutation boundary revalidates
configured contract and protected refs and records publication evidence. Source-ref movement must
reconcile or complete the same generation.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `handover_gate_guard`, `unmatched_handover_gate_warning`, `blocked_integration_payload` at this ownership boundary. | `handover_gate_guard`; `unmatched_handover_gate_warning`; "def blocked_integration_payload(" | mcp/src/agents_remember/worktrees/modules/integrate.py:83-109; mcp/src/agents_remember/worktrees/modules/integrate.py:112-148; mcp/src/agents_remember/worktrees/integration/master_review_gate.py:14-14 |

## 260821-CLIVE Live Atomic Landing Authority

Before an atomic protected-ref publication, integration now calls
`require_atomic_landing_authority` against current repository/series truth. Conflicting nonterminal
series targets return the typed atomic-landing blocked result; no durable queue blocker is acquired
or released. The integration authority lock is held only around the protected publication edge and
the current contract is re-proved inside it. Completed integrations remain idempotent; organizational
completion continues through its journaled publication transaction.

## PDLS Reconciliation

Integration recovery now rejects external-memory commit evidence on internal-memory contracts and preserves exact candidate/ref state before invoking the canonical recovery route.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.

## Current Landed Composition

This module contains no quality reference at all. The integration quality call, `args.integration_certification_owner`, `run_integration_quality_gate` and the configured-profile forwarding described in earlier revisions of this section were deleted with `integration_quality.py` by the closeout-door cut (commit `fad9808e`). Integration lands the prepared pair under the existing authority and ref-safety controls and runs no acceptance gate of its own.

## Closeout-Door Cut: Boundary Facts, Publication Intent And Claim Transfer Removed

The closeout-door cut (commit `fad9808e`) removed three imports from this module and the code that used
them: `transfer_and_publish_integration_claim` (from `integration_claim_transfer.py`),
`IntegrationDoorAuthorityConflict` / `integration_door_decision_payload` (from
`integration_publication_fence.py`), and `IntegrationBoundaryFacts` /
`prepare_integration_publication_intent` / `preview_integration_boundary` (from
`organizational_completion_integration.py`). All three modules were deleted.

`_apply_integration` no longer builds boundary facts, a publication intent, or a claim transfer. It
takes the prepared commit pair straight to publication. Admission for the ordinary integration path is
therefore the request plus the existing branch/ref authority checks — no door-claim match is performed,
and `prepared_integration_recovery` was dropped from the preflight results with it. `IntegrationPublication`
lost its `intent` field for the same reason.

## 260831-LOCR-L30 Checkpoint Landing (The Partial-Master Verb)

`integrate_result` closes a finished master. `checkpoint_landing_result(args, current_contract)` cit:([`checkpoint_landing_result`], mcp/src/agents_remember/worktrees/modules/integrate.py:664-696) partially publishes an unfinished one: it lands that master's accumulated line into its super branch
and keeps the master open — a publication, not a pause. Before it existed a partial master could not land at all, because
`publish_series_integration_under_authority` structurally proves the master is complete — its task
document `Completed` and one landed enclosure per canonical leaf — and an unfinished master has neither.

It shares the entire preflight and the ref move with the final route. As L30 wrote it, it differed in
exactly two places; **the first of those is superseded by 260831-LOCR-L34** (see the section below),
which replaced the closeout-cell read and the `checkpoint: bool` flag with the captured
`CheckpointLanding` value:

- ~~Its series authority is `publish_series_checkpoint_under_authority`, which keeps the series
  contract binding, the atomic landing authority, the integration targets, **the contract
  validation**, the replay/ff source-state gate, the source-lineage proof and the master-handover
  gate, and drops only the two completion assumptions.~~ Superseded: the contract validation is no
  longer run on this path, and the completion gate it dropped is now also what the closeout preview
  refuses on. A master that is already `Completed` is still refused there with
  `atomic-series-checkpoint-master-complete`, and since L34 the captured refs are revalidated against
  the live tips before the move.
- Its recorded state comes from `_checkpoint_result` cit:([`_checkpoint_result`], mcp/src/agents_remember/worktrees/modules/integrate.py:923-962) instead of `_integrated_result`
  cit:([`_integrated_result`], mcp/src/agents_remember/worktrees/modules/integrate.py:600-635).
  `_checkpoint_result` writes `checkpointed` through the shared writer and reclaims nothing, so the
  master keeps its worktrees, its branches and its enclosure, and the integration cell never claims a
  completion that has not happened. Since 260831-LOCR-L31 that "reclaims nothing" clause is the
  property of **both** landing routes rather than the checkpoint's distinguishing feature — its
  docstring was corrected accordingly, because the old phrasing ("does not run the automatic
  cleanup") had become vacuous once no landing route reclaims. An unfinished master landed at a
  checkpoint is never finalized, so
  it is never reclaimed. Its payload summary states this in operator language: the line landed, the
  master stays open, nothing was retired and no cleanup ran.

The `checkpoint` value is threaded, keyword-only and defaulted to `None` at every step, so the final
route's behavior is byte-identical: `_continue_integration(checkpoint=…)` →
`_handover_or_apply_integration(checkpoint=…)` → `_apply_integration(checkpoint=…)` →
`_publish_integration_edge(..., checkpoint=…)` → `_checkpoint_result`. `checkpoint_landing_result`
also refuses a non-`series` contract outright (an ordinary leaf lands through `worktree_integrate`)
and requires explicit approval on a non-dry-run.

`checkpoint_landing_result` is re-exported from the `worktrees/git_worktree_manager.py` facade and
reached by the public `worktree_checkpoint_landing` tool; the payload builder and application entry
point are documented on their own cards.

## 260831-LOCR-L34 The Checkpoint Captures Its Own Refs (The Reachability Repair)

L30 wrote the checkpoint route but left it **unreachable in both directions**. It required
`closeout_status == "completed"` (through `validate_integrate_contract`, which it called), while the
only operation that produced that cell — the series closeout — requires the master complete and every
atomic leaf landed. A partial master therefore could not reach the route, and a complete one was
refused by the master-complete guard. L30's own note admitted the real ref move was never proven end
to end, which is how it survived.

The `checkpoint: bool` flag is gone, replaced by a `CheckpointLanding` value
cit:([`CheckpointLanding`], mcp/src/agents_remember/worktrees/modules/integrate.py:388-421) built by
`checkpoint_landing_eligibility(contract)`
cit:([`checkpoint_landing_eligibility`], mcp/src/agents_remember/worktrees/modules/integrate.py:424-469) — **the one eligibility decision both the preview and the apply read**. It captures the
master's own committed refs (`series_closeout.capture_series_checkpoint_refs`, the live code and
memory work-branch tips plus their proved ledger mapping), the `IntegratedCommits` triple, and the
`IntegrationSources` replay verdict, and raises when the captured ledger is not the live memory work
ref. It replaces the ordinary route's closeout cells — the state this route exists to make reachable
is exactly their absence — while every other condition is unchanged and proven either here or on the
shared path both routes still walk: the series contract binding, the integration targets, the atomic
landing authority, the source-lineage proof, the replay/ff source-state gate, the master-handover gate
and the compare-and-swap. `checkpoint_landing_result` no longer calls `validate_integrate_contract`
(whose series arm is byte-identical to the two ref-shape checks here); it uses the captured value
instead.

Three parity repairs ride with it, and all three are instances of the invariant recorded on the
`worktrees/overview.md` route:

- **`_checkpoint_dry_run_result`** cit:([`_checkpoint_dry_run_result`], mcp/src/agents_remember/worktrees/modules/integrate.py:524-569) is the checkpoint's preview: it reports the eligibility record
  (`eligibility`), the replay verdicts, the handover gate and the strategy, and moves nothing. It
  reads the same `CheckpointLanding` the apply lands. **Instance 2.**
- **The shared landing proof is now a proof about the landed commits only (260913-LCA-L11).**
  `_require_ledger_projection(...)`
  cit:([`_require_ledger_projection`], mcp/src/agents_remember/worktrees/modules/integrate.py:484-507) runs in `_handover_or_apply_integration` **before the dry-run branch**, for both routes, on
  the commits `_route_commits(contract, checkpoint)`
  cit:([`_route_commits`], mcp/src/agents_remember/worktrees/modules/integrate.py:510-521) selects. Before this the
  checkpoint's preview said `would-checkpoint` while its apply refused on the projection
  (**instance 4**), and the ordinary `worktree_integrate` dry run did not evaluate the projection at
  all (**instance 5**). The protected boundary inside the transaction still re-takes the read; this
  one exists only so the preview refuses exactly what the apply refuses. It runs after the replay/ff
  gate and the lineage block so those keep returning their own payload and remedy. Since
  260913-LCA-L11 it passes no ledger-history form: the file-preservation rule the preview used to
  share is gone (see the transaction card), and the preview therefore refuses exactly what the apply
  refuses **by construction rather than by a shape both had to agree on**.
- **The ref-race payload names the route's own tool.** `_publish_integration_edge` now takes a
  **required** `operation: str`
  cit:([`_publish_integration_edge`], mcp/src/agents_remember/worktrees/modules/integrate.py:847-920) threaded from the caller, and the `integration-ref-race` payload's `nextTool` is that
  name. It used to be the hardcoded literal `"worktree_integrate"`, so a checkpoint that lost the
  compare-and-swap told the operator to re-run the **wrong tool** (**instance 3**). The name is
  required rather than inferred from `checkpoint` so every route has to name itself, and a route added
  later cannot silently inherit the wrong name.

`_landing_admission(*, checkpoint)`
cit:([`_landing_admission`], mcp/src/agents_remember/worktrees/modules/integrate.py:472-481) is the one place the route's admission facts are derived, and `_apply_integration` routes
the checkpoint through `publish_series_checkpoint_under_authority(..., expected=checkpoint.refs)` so
the captured candidate is revalidated against the live tips before the single ref move. Since
260913-LCA-L11 it takes no contract: with the file-preservation rule gone there is no series ledger
prefix left to read, so the finished-master census (`atomic_series_ledger_prefix`) is no longer part
of the route's admission at all. The
`_publish_integration_edge` docstring is explicit that both literals it can receive are registered
public tools, which is what the wire's `nextTool` validator requires.

The `integration-ref-race` case is covered end to end by the new
`mcp/tests/test_checkpoint_landing_end_to_end.py::test_a_ref_race_names_the_checkpoint_as_the_tool_to_rerun`.

## Update History

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 19 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T11:58+02:00 — 260913-LCA-L11 curator (uncommitted change set on `ar/260913-lca-l11-ar`,
  base `4214d7a1`): the route's admission lost its ledger-history dimension. `_landing_admission`
  now takes only `checkpoint` — the contract argument is gone, because with the developer's ruling
  that the rebuild outranks the tracked ledger file there is no series ledger prefix left to read
  (`atomic_series_ledger_prefix` was deleted with its only consumer). `_require_ledger_projection`
  likewise no longer receives `expected_series_prefix`/`checkpoint`. The preview/apply parity the
  L34 section records is unchanged and is now stronger by construction: the preview refuses exactly
  what the apply refuses because both run the same proof with nothing route-shaped to agree on.
  Repointed the three reference ranges this card carried into `integrate.py` after the module shifted
  by roughly 20 lines, and recorded the fact on the reference row and in the L34 parity bullet.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp
  advanced.
- 2026-09-13T18:02+02:00 — 260831-LOCR-L36 terminology: `checkpoint_landing_result` partially
  publishes an unfinished master; the card no longer says it "pauses" one or calls the route's subject
  a "paused master". The mechanism is unchanged (it lands the accumulated line, keeps the master open,
  records `checkpointed`, retires nothing), and pausing remains a separate matter that moves no ref.
  Wording only; no verification stamp advanced.
- 2026-09-13T14:32+02:00 — Curator citation repoint after the contract-scoped atomic-series activation re-keying shrank `models/worktree.py`: rebound the wire-vocabulary row to `mcp/src/agents_remember/models/worktree.py:38-39`, `_blocked_non_ff_result` to `integrate.py:320-338`, the checkpoint eligibility row (`CheckpointLanding`, `checkpoint_landing_eligibility`, `_route_commits`) to `integrate.py:390-424`, `425-461` and `527-539`, the `_route_commits` mention to `527-539`, and the `are reclaimed when the task edge is finalized.` quote to `integrate.py:643`. Claim wording unchanged; the cited declarations moved without changing what each claim states.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:45+00:00 — 260831-LOCR-L34 reachability repair: recorded the `CheckpointLanding`
  value and `checkpoint_landing_eligibility` as the one eligibility decision both surfaces read, the
  removal of `validate_integrate_contract` from the checkpoint path, and the three parity repairs —
  `_checkpoint_dry_run_result` (instance 2), the shared `_require_ledger_projection` before the
  dry-run branch for both routes (instances 4 and 5), and the required `operation` name on
  `_publish_integration_edge` fixing the hardcoded `nextTool` on `integration-ref-race` (instance 3).
  Superseded the L30 section's claim that the checkpoint "differs in exactly two places" and that it
  runs the contract validation. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "IntegrationStatus = Literal["; "CleanupStatus = Literal[" repointed to mcp/src/agents_remember/models/worktree.py:39-39; mcp/src/agents_remember/models/worktree.py:40-40. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:57:35+00:00: Generated citation repair: `_blocked_non_ff_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:278-295. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T19:50+02:00 — 260831-LOCR-L31 root integration to `lifecycle_finalize_task`:
  `_integrated_result` no longer reclaims. Replaced the "Automatic post-integration cleanup" section
  with the landed-and-stop boundary, and recorded **why the removal is the fix**: because cleanup ran
  inline and had already reached `completed` when the function returned, the one guard that routes a
  landed leaf to `lifecycle_finalize_task` (`next_step.py::_gate_after`, keyed on
  `contract.cleanup != "completed"`) could never fire — a real landing reported `nextOperation: "done"`
  while the leaf document stayed `planning` and its master row stayed `inProgress`, silently, on L29
  and L30. Recorded that the payload no longer carries a `"cleanup"` report key (the key is now the
  untouched contract cell), the two re-worded wire surfaces (`cleanup_reminder` and the integrated
  `summary`), and the corrected `_checkpoint_result` docstring clause that had become vacuous once no
  landing route reclaims. Re-pointed the shifted `_integrated_result` (373-408 → 375-410),
  `_checkpoint_result` (674-714 → 678-717) and `_dry_run_result` ranges. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: added `checkpoint_landing_result` and
  `_checkpoint_result`, the keyword-only `checkpoint` flag threaded through
  `_continue_integration`/`_handover_or_apply_integration`/`_apply_integration`/`_publish_integration_edge`,
  and the `publish_series_checkpoint_under_authority` selection; recorded that the checkpoint path
  records `checkpointed` and runs no cleanup, and corrected the `ContractCells` section, which still
  described `_integrated_result` amending the landing cells inline after the L29 extraction moved
  those writes into `landing_record.py` (the L30 change then widened that writer to take
  `LandedIntegration`). Re-derived the shifted reference ranges. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-11T23:05:00+00:00: The completed-integration row anchored the bare symbol `run_automatic_cleanup`, which now resolves three times across the two cited files (import and call in `integrate.py`, definition in `automatic_cleanup.py`), so the claim's provenance could not be compared. The anchor is now the exact call text `cleanup = run_automatic_cleanup(updated)` at `integrate.py` line 386, which occurs once in the cited sources; the claim's wording and both cited extents are unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "class ContractCells:" repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:180-180. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def amend_contract(" repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:197-197. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_integrated_result`; "def blocked_integration_payload(" repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:369-400; mcp/src/agents_remember/worktrees/integration/master_review_gate.py:14-14. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_blocked_non_ff_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:275-292. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-11T14:52+02:00 — Automatic post-integration cleanup at code commit `76ce662a`: `_integrated_result` now calls `run_automatic_cleanup` on the successful path after writing `integration_status=completed`, reloads the contract so the payload reflects the post-cleanup cell, nests the cleanup report as a top-level `cleanup` key, and reports a cleanup refusal without failing the landing; a refused or partial integration cleans up nothing. Repointed the stale `_integrated_result` ranges (420-450 → 372-407). Verification metadata remains pinned because this is a targeted single-claim repair; source documentation only, no acceptance claim.
- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: retired the evidence row citing the deleted `integration_quality.py` and recorded the module has no quality reference at all; corrected the L3 seam and CLIVE-L2 admission wording, which had this module binding a claimed closeout door and source journal into an integration intent — that module was deleted and no door claim is matched on this path; added the boundary-facts/publication-intent/claim-transfer removal section. Verification metadata remains pinned because only the cut-affected claims were reconciled; source documentation only, no acceptance claim.
- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: retired the evidence row citing the deleted `test_worktree_integrate_quality_gate.py` altitude matrix. Verification metadata remains pinned because only the cut-affected reference was reconciled; source documentation only, no acceptance claim.

- 2026-09-10T15:06+02:00 — Integration guidance curation: the `blocked-non-ff` / `source branch moved` refusal now routes through `worktree_sync` plus a new targeted closeout instead of `--strategy replay`; recorded that `replay` remains supported and is the carryover vehicle. Re-derived the integrate.py anchors against the current working tree. Verification metadata remains closeout-owned.

- 2026-09-10T07:41:10+00:00: Generated citation repair: `_integrated_result`; "def blocked_integration_payload(" repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:418-448; mcp/src/agents_remember/worktrees/integration/master_review_gate.py:25-25. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.

- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 1 declined citation claim against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Separated wire state vocabulary from the typed amendment record and helper. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.
- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile_reference forwarding for the master full gate and removal of the requires_integrated_acceptance repo-name policy; refreshed integration_quality citations to the post-cutover ranges.
| The planned gate is carried in the typed dry-run payload without executing publication. | `IntegratePreview`; `_dry_run_result` | mcp/src/agents_remember/worktrees/modules/integration_publication.py:30-35; mcp/src/agents_remember/worktrees/modules/integrate.py:321-369 |
| The integrated result records the completed publication outcome and promises only the landing. | `_integrated_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:600-637 |
| The altitude-proof module this row cited was deleted with the removed closeout fixture chain (commit `9e1743c1`); the altitude matrix it described is no longer retained as test coverage. | — | — |
| Historical/removed: the direct-legacy-integration cases named here lived in `test_worktree_support_tests_2.py` / `_3.py`, which no longer exist. Journaled production-path suites own successful movement and recovery; this row records the earlier coverage rather than a current test. | N/A | N/A |


- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: replaced persistent blocker assumptions with live atomic protected-ref authority at the landing edge. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the queue-consume return (stale-by-evidence sibling
  facts) now lands on the fresh and completed-recovery integration payloads as
  `staleByEvidence`, each naming `worktree_sync` as recovery. Verification remains closeout-owned.

- 2026-08-17T12:09+02:00 — 260815-DAG-L5: the quality altitude ladder (`quality_gate_mode`, `quality_gate_preview`, `run_integration_quality_gate`) moved to `integration_quality.py` and `IntegratePreview`/`IntegrationPublication` to `modules/integration_publication.py`; re-pointed the two cited rows to the new owners. Verification remains closeout-owned.

- 2026-08-16T08:12+02:00 — Dagger repair: reordered final source-state diagnostics so the exact accepted-tip race owns the structured pre-CAS refusal before persisted lineage diagnostics.

- 2026-08-16T07:05+02:00 — L4 review repair: completed apply/recovery now requires the operation's exact durable recovery tuple before descendant, ledger, or queue-completion publication.

- 2026-08-16T06:15+02:00 — Dagger repair: separated fresh integration from durable recovery admission so a newly queued graph candidate is claimed before queue-owned publication rather than being misclassified as torn recovery.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: recorded the certified claim, final irreversible
  revalidation, exact consume, and completed-integration recovery path; verification remains
  closeout-owned.

- 2026-08-14T11:25+02:00 — R39 curator: replaced leaf targeted reruns with certified-commit reuse
  and retained full acceptance solely at master integration. Verification remains closeout-owned.
- 2026-08-14T09:37+02:00 — Reopened L23 acceptance ownership: leaf integration now lands the exact
  closeout-certified commit without Dagger; master integration remains the only full accepting run.
  PR, push, tag, and publish paths do not become alternate integration acceptance owners.
- 2026-08-14T06:36+02:00 — L23 final candidate review: integration rechecks complete code and
  external-memory lineage before/after quality and before merge, pins source tips, runs targeted
  leaf or full master Dagger authority, and stays failure-atomic before refs move.
- 2026-08-13T08:40+02:00 — L23 integration-gate repair: documented fail-closed transitive-lineage admission, exact source-tip pinning across quality, and the two post-quality checks that prevent memory replay or source merge after in-flight movement. Verification metadata remains closeout-owned.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: made the
  integration-time memory cap optional; master integration now runs
  host-managed by default and forwards an explicit cap only when configured.
  Verification metadata remains pinned until closeout stamps L24.

- 2026-08-11T17:50+02:00 — 260731-EFA-L19 curator: recorded enclosure-targeted,
  atomically replaced test/quality transcripts for leaf and master integration gates. Verification
  metadata remains pinned until governed closeout.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the quality
  altitude ladder at the integration seam (kind-based mode routing, settings-owned
  cap, gate run before any merge, dry-run planned-gate payload, altitude
  invocation labels) and refreshed the persisted-write rows to the post-L17
  ranges. Verification metadata stays pinned until closeout stamps the
  260731-EFA-L17 commit.

- 2026-08-04T03:26:26+02:00 — 260731-EFA-L6 S18-SR3-B06 curator: generated and source-inspected the two persisted integration-write ranges (1 repair, 0 normalisations, 0 declines); the locked immediate recheck was clean with frozen zero source/tokenize/parse/build telemetry.
- 2026-08-04T03:03:23+02:00 — 260731-EFA-L6 S18-SR3-B06 worker: replaced the
  underbound function-header/assignment fragments with both complete integration-write owners,
  retaining the blocked and completed-plus-cleanup-pending meanings. The changed binding is a
  provisional `:1-1` input for the fresh Luna curator; no citation mechanics ran.
- 2026-08-04T02:20:03+02:00 — 260731-EFA-L6 S18-B06 curator delta: repaired the scoped citations against the frozen source snapshot; generated ranges were inspected and the managed index remained warm/frozen with zero source reads, tokenization, parsing, and build.

- 2026-08-04T01:24:49+02:00 — 260731-EFA-L6 S18-SR2-B06 worker: source-first separated the
  worktree-contract type/helper definitions from this module's two actual `amend_contract` call
  sites. Preserved every generated definition range and added one honest `:1-1` binding for the
  blocked and completed writes; no citation mechanics ran.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the scoped worktree-integration citation claims; final exact frozen-snapshot check is clean.
- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 2 citation entries (4 findings); no Tier-3 findings.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:50+02:00 — 260731-EFA-L4 curator: this leaf's diff here is not an import move — both
  of the module's contract writes changed shape. `blocked_integration_payload` went from
  `replace(contract, integration_status="blocked")` to
  `amend_contract(contract, ContractCells(integration_status="blocked"))`, and `_integrated_result`
  from one seven-keyword `replace` to `amend_contract(replace(contract, <four commit/strategy
  fields>), ContractCells(integration_status="completed", cleanup="pending"))`. Documented both, and
  the rule behind them: typeshed types `dataclasses.replace`'s `**changes` as `Any`, so an
  off-vocabulary literal at either of these two cells was zero pyright errors; the typed record puts
  them back in front of the checker. The persisted contract is byte-identical, so no payload,
  ordering or blocking claim in this card changed — I re-verified the all-or-nothing merge, the
  `IntegrationSources` / `IntegratedCommits` / `_apply_integration` L2 structure, and the
  master-handover gate section against the current file, and all still hold. Extended the
  `worktree_contract.py` reference row. Verification metadata pinned until closeout stamps the L4
  commit.
- 2026-07-31T21:00+02:00 — 260731-EFA-L3 curator: No content impact: the leaf's whole diff to
  `integrate.py` is one import line — `run_git` moved out of the `modules.git` import block to
  `agents_remember.kernel.git_command` — and this sidecar names no runner, subprocess style or
  timeout. I specifically re-checked the one claim the shared runner's new 300s bound could have
  broken, the all-or-nothing merge: `_merge_integrated_commits` still wraps the memory-side
  `merge --ff-only` and the ledger-mapping check in `except Exception`, and
  `subprocess.TimeoutExpired` is an `Exception`, so even a merge that outruns the bound still hits
  `run_git(..., ["reset", "--hard", code_head_before])` and the memory equivalent before re-raising
  — integration still cannot leave a half-integrated state. `IntegrationSources` (with
  `replay_required`), `IntegratedCommits`, `_apply_integration` and the `rebase` /
  `rebase --onto` replay call sites are untouched.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0913` armed with no
  exemptions): added the frozen `IntegrationSources` (with its `replay_required` property) and
  `IntegratedCommits`, re-signed `_integration_replay_requirements` / `_blocked_non_ff_result` /
  `_dry_run_result` / `_merge_integrated_commits` / `_integrated_result` onto them, and lifted the
  real integration path into `_apply_integration`. The all-or-nothing merge, the replay decision
  and every payload field are unchanged. Verification metadata pinned until closeout stamps the L2
  commit.
- 2026-07-05T19:55+02:00 - L8 builder cycle 7: added pure `unmatched_handover_gate_warning` (the enclosure spelling-check on gateless integrates, AR4-1b) and the dry-run now evaluates-but-does-not-enforce the seam guard, carrying `handover_gate` + the warning in the preview with no contract mutation (AR4-2). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: extracted `handover_gate_guard` (pure, testable) — cross-lifecycle fold + enclosure addressing replaces the inert `contract.lifecycle_id` lookup (AR3-1(b)). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): master-handover-approval enforcement consumer added at the integrate edge. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-05-31T12:30+02:00 — Documented all-or-nothing merge: pre-validate both fast-forwards and roll both branches back on memory-side failure (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
