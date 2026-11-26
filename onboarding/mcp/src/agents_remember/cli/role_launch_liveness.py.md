# mcp/src/agents_remember/cli/role_launch_liveness.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Refreshes receipt facts from one native agent read and reconciles new starts with observed execution state.

## Code Commentary

The receipt liveness read skips unresolved or rejected launches. The options coordinator can read the agent outside the dispatch lock, then pass the observation to the liveness projection only when the saved receipt still matches. `_apply_reading` locks the receipt, preserves any existing `retiredBy`, routes host-confirmed `archived`/`gone` observations through `_observe_host_archive` (which defers when `retireIntent` or `_leaf_is_closing` is present and otherwise calls `settle_retirement(..., caller="host", reason="host archive", host_state=...)` to record host-archive attribution and settle the held store), and otherwise applies changed lifecycle fields via `_apply_status_row` without writing on unreachable reads (response-only unreachable detail preserves last known status). Revive republishes the saved receipt’s role identity through `resume_role_agent` before resuming only the same closed agent, persists answered refusal, and drops that refusal only after seeing the session open. New Start applies open-execution policy to current native facts. For non-leaf replacements (`_reconcile_non_leaf`), an open execution still refuses HTTP 409; for a closed non-rejected execution without `retiredBy`, it reserves `retireIntent` via `hold_retirement` before archiving the receipt so `finish_replacing_predecessor` records retirement after acknowledged archival. For a leaf seat, a finished turn or closed session does not free its unarchived holder. An ordinary new request must explicitly name that holder for replacement; non-step-up replacement authorizes by caller scope via `retirement_scope_refusal` (or the dashboard launcher), and interrupting an active turn or running subagents requires `replaces_interrupt_turn=true`. A step-up replacement (`replacement.step_up`) enforces starter-only authority (`parentAgentId`) and `_require_step_up_idle` always refuses active turns, pending permissions, or running subagents even with interruption requested. An unreadable holder fails closed rather than appearing free. Replacement reserves `retireIntent` via `_reserve_leaf_predecessor` before archiving the prior receipt and preserves predecessor report custody.

A held receipt keeps the product status `held` through an ordinary host idle reading. Only an archived or vanished holder frees that seat; an unreachable host leaves its saved held state intact. Ordinary revive and closing-mark behavior stays separate.


**L184 — INV-ECNV2S.** This module is where a seat's liveness is judged, so the word that guards a retirement is realized here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Current Contract — Scoped Launch And Settings Changes

Same-request reconciliation checks request digest first, reconciles its task step-up decision, then re-executes `starting`/`unknown`, or restarts via `_restart_closed_execution` when `status == "stopped"` (including host-observed archives, since `receipt_is_explicitly_retired` is False for `caller == "host"`) or `status == "rejected" and stepUp` with a saved `replayRequest`, neither explicitly retired nor `_leaf_is_closing`. Other resolved receipts continue through refresh. A missing recorded native Antigravity agent settles the refusal and drops the replay call, which closes this Retry path.

Ordinary leaf replacement requires a named holder and `retirement_scope_refusal` caller scope (or the dashboard launcher), with `replaces_interrupt_turn=true` for an active turn or running subagents. For a step-up replacement, only the original starter (`parentAgentId`) or launcher may authorize it, and `_require_step_up_idle` always refuses pending permission, active turns, or running subagents even when interruption was requested.

The saved-call executor renews predecessor liveness for a step-up receipt whose saved launch names an `archiveAgentId`, including Retry and recovery through that executor. An unreachable host refuses the call. A found, unarchived predecessor must be idle and prompt-free.

No finished turn accepts AR work or frees a live leaf holder. Held-state persistence, response-only unreachable refresh, revive refusal custody, predecessor reports and ordinary closing-mark behavior remain unchanged.

## Evidence


- Execution refresh reads the recorded agent and applies its observation. A receipt without a confirmed host agent is projected without a host read. [1]




- The current reading updates changed lifecycle fields or settles host-observed archives without overwriting `retiredBy` or pending `retireIntent`. An unreachable reading preserves the receipt and labels the response as last known. [2]





- Revive republishes the recorded role binding and resumes only the same eligible closed host agent. A recorded refusal remains until that session is observed open. [3]



- Checks bytes, inode and mtime unchanged on failed/unreadable state and response-only unreachable reason. [6]



- Refresh preserves the failed Revive status and reason. A second Revive refuses after agent-state without a resume call. [7]



- Observing the same session open clears prior resume refusal. [8]

- Checks unresolved/rejected receipts returned unchanged without host read. [9]

- Checks an idle finished native turn projects completed lifecycle status and its bounded last text; the test does not itself prove absence of every semantic/Git mutation. [10]



## Investigator scope and request identity

Selected-task Investigator starts reconcile their exact request instead of adopting another request for that role. Existing close/revive/refresh meanings stay receipt-derived: completed means the native agent is idle, and does not accept AR work. The capacity owner refreshes open requests before a new admitted turn; Projects retains its original single-open bound-row behavior.




- The current source implements this file’s stated Investigator and reconciliation boundaries. [13]

## Refreshed current evidence


- Changes task/capsule/prompt inputs and verifies repeat returns or replays saved receipt without new preparation. [4]






Past-epoch account (retained wording): - Pins delivered worker doctrine: freeze the candidate and hand it directly to the leaf's Reviewer; the Manager receives no routine report notice. A dashboard-started Worker has no parent, and a finished turn is not AR acceptance.

Custody: the preceding sentence is detached from live reference 11; its original target blob(s) were `74a051a27a76bfa2d21ab404b581911d5e391701`. The current clause below is separately bound.

- The Worker handover test requires a first freeze notice to the Manager to start the Reviewer, followed by direct complete freeze handover to that Reviewer; the Manager does not relay it or receive routine report notices. It also checks parentless Worker and turn-end-versus-acceptance wording, with mutation cases for every required route clause.


Past-epoch account (retained wording): - Composes delivered architect/manager/orchestrator capsule text, requires current diff/evidence inspection and owner acceptance clauses, and detects removal of manager inspection; this proves instruction delivery rather than runtime no-mutation.

Custody: the preceding sentence is detached from live reference 12; original target blob(s): `74a051a27a76bfa2d21ab404b581911d5e391701`.

- The test joins the shipped Architect/review, Manager/coordination and Orchestrator/coordination source texts, checks their candidate-evidence and owner-acceptance clauses, and detects removal of Manager inspection. This checks that source composition’s wording; it runs no capsule admission/compilation and proves no runtime no-mutation property.



- Digest-bound same-request replay reconciles decisions, restarts eligible non-explicitly-retired closed receipts, and reconciles empty successors. [14]
- Ordinary leaf replacement uses caller scope (`retirement_scope_refusal`) while step-up keeps starter-only authority and unconditional idle/prompt/subagent checks. [15]

- The saved-call executor rechecks the named step-up predecessor before archiving it. A found, unarchived predecessor must be idle and prompt-free. [16]






- Test source checks turn/prompt/unreachable recovery and no archive/create. [17]

- The Worker handover test requires a first freeze notice to the Manager to start the Reviewer, followed by direct complete freeze handover to that Reviewer; the Manager does not relay it or receive routine report notices. It also checks parentless Worker and turn-end-versus-acceptance wording, with mutation cases for every required route clause. [11]

- The test joins the shipped Architect/review, Manager/coordination and Orchestrator/coordination source texts, checks their candidate-evidence and owner-acceptance clauses, and detects removal of Manager inspection. This checks that source composition’s wording; it runs no capsule admission/compilation and proves no runtime no-mutation property. [12]
