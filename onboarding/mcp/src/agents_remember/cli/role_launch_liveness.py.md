# mcp/src/agents_remember/cli/role_launch_liveness.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Refreshes receipt facts from one native agent read and reconciles new starts with observed execution state.

## Code Commentary

_refresh_execution returns unresolved/rejected launches without an agent read. _apply_reading writes only changed lifecycle fields and never on unreachable reads; response-only unreachable detail preserves last known status. Revive republishes the saved receipt’s role identity through `resume_role_agent` before resuming only the same closed agent, persists answered refusal, and drops that refusal only after seeing the session open. New Start applies open-execution policy to current native facts. For a leaf seat, a finished turn or closed session does not free its unarchived holder. An ordinary new request must explicitly name that holder for replacement; only the recorded starter or the dashboard launcher may authorize it, and interrupting an ordinary active replacement requires the explicit flag. A catalog-validated step-up can infer the current base holder, but still applies that caller authority and always requires idle/no pending permission; its replacement never interrupts an active turn. An unreadable holder fails closed rather than appearing free. The replacement records retirement before archiving the prior receipt and preserves predecessor report custody.

A held receipt keeps the product status `held` through an ordinary host idle reading. Only an archived or vanished holder frees that seat; an unreachable host leaves its saved held state intact. Ordinary revive and closing-mark behavior stays separate.


**L184 — INV-ECNV2S.** This module is where a seat's liveness is judged, so the word that guards a retirement is realized here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Current Contract — Scoped Launch And Settings Changes

Same-request reconciliation checks request digest first, reconciles its task step-up decision, then re-executes starting/unknown or a rejected stepped-up receipt that still has replayRequest. Other resolved receipts continue through refresh; this adds a narrow rejected-successor retry, not a general retry for every refusal.

Ordinary leaf replacement still requires a named holder and starter/launcher authority, with explicit permission to interrupt a normal active replacement. For a validated step-up, runtime wiring can infer that holder but _require_step_up_idle always refuses pending permission or active/running turns even when interruption was requested.

require_step_up_archive_idle re-reads archiveAgentId immediately before every saved step-up call, including retries and history recovery. Unreachable facts refuse; an extant unarchived predecessor must again be idle and prompt-free. A prior reservation or settled archive flag is not a liveness lease.

No finished turn accepts AR work or frees a live leaf holder. Held-state persistence, response-only unreachable refresh, revive refusal custody, predecessor reports and ordinary closing-mark behavior remain unchanged.

## Evidence

- Frozen implementation of _refresh_execution supporting the stated file behavior. [1]

- Frozen implementation of _apply_reading supporting the stated file behavior. [2]


- Frozen implementation of _revive_agent supporting the stated file behavior. [3]


- Checks bytes, inode and mtime unchanged on failed/unreadable state and response-only unreachable reason. [6]

- Answered refusal persists as failed across refreshes without rewrite and blocks another Revive. [7]

- Observing the same session open clears prior resume refusal. [8]
- Checks unresolved/rejected receipts returned unchanged without host read. [9]
- Checks an idle finished native turn projects completed lifecycle status and its bounded last text; the test does not itself prove absence of every semantic/Git mutation. [10]


## Investigator scope and request identity

Selected-task Investigator starts reconcile their exact request instead of adopting another request for that role. Existing close/revive/refresh meanings stay receipt-derived: completed means the native agent is idle, and does not accept AR work. The capacity owner refreshes open requests before a new admitted turn; Projects retains its original single-open bound-row behavior.



- The current source implements this file’s stated Investigator boundary. [13]



## Refreshed current evidence


- Changes task/capsule/prompt inputs and verifies repeat returns or replays saved receipt without new preparation. [4]


- Pins delivered worker doctrine: one parent role_message after report, none for dashboard-started worker, and a finished turn is not AR acceptance. [11]


- Composes delivered architect/manager/orchestrator capsule text, requires current diff/evidence inspection and owner acceptance clauses, and detects removal of manager inspection; this proves instruction delivery rather than runtime no-mutation. [12]


- Digest-bound same-request replay reconciles decisions and empty successors. [14]


- Replacement authority remains while step-up adds unconditional idle/prompt checks. [15]



- Every saved archival call renews host liveness. [16]


- Test source checks turn/prompt/unreachable recovery and no archive/create. [17]
