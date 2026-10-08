# mcp/src/agents_remember/cli/role_launch_liveness.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Refreshes receipt facts from one native agent read and reconciles new starts with observed execution state.

## Code Commentary

_refresh_execution returns unresolved/rejected launches without an agent read. _apply_reading writes only changed lifecycle fields and never on unreachable reads; response-only unreachable detail preserves last known status. Revive resumes only the same closed agent, persists answered refusal, and drops that refusal only after seeing the session open. New Start applies open-execution policy to current native facts.

## Evidence

- Frozen implementation of _refresh_execution supporting the stated file behavior. [1]
- Frozen implementation of _apply_reading supporting the stated file behavior. [2]
- Frozen implementation of _revive_agent supporting the stated file behavior. [3]

- Checks repeated unresolved calls retain the minted agent. [5]
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
