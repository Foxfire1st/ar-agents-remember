# mcp/src/agents_remember/cli/paseo_status.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns ordered native observation-to-execution status and resume projection.

## Code Commentary

Live listing includes an authoritative host process-start identity: PID, kernel birth ticks and OS boot identity, confirmed during one observation. Unavailable identity stays explicit and retries; serverId alone and temporary reachability loss do not establish a new start.


STATUS_TABLE applies its first matching row: unreadable host preserves receipt facts; found closed/open/native permission/error/idle states retain distinct lifecycle meanings. read_agent/resume_agent report native observations; completed means last turn finished, not AR acceptance. An answered still-closed resume is a refusal, while unreachable remains unconfirmed.

`read_live_agents` makes one read-only `agents-live` bridge call and validates a string-ID list plus a boolean completeness flag. Bridge failures and malformed answers become unreachable readings with a reason; a valid incomplete listing keeps its known IDs and cannot classify an absent recorded agent as gone. The existing per-agent first-match status table and explicit resume path remain unchanged.

## Evidence

- Checks bytes, inode and mtime unchanged on failed/unreadable state and response-only unreachable reason. [5]
- Answered refusal persists as failed across refreshes without rewrite and blocks another Revive. [6]
- Observing the same session open clears prior resume refusal. [7]
- Checks unresolved/rejected receipts returned unchanged without host read. [8]
- Checks an idle finished native turn projects completed lifecycle status and its bounded last text; the test does not itself prove absence of every semantic/Git mutation. [9]

- Pins delivered worker doctrine: freeze the candidate and hand its report file directly to the leaf's Reviewer, not to the Manager for relay; dashboard-started workers need no parent. A finished turn is not AR acceptance.  Anchor: `AgreementAcrossTheRoleSetTests.test_a_worker_tells_only_a_parent_agent_and_only_once_that_its_report_is_written` [10]

- Composes delivered architect/manager/orchestrator capsule text, requires current diff/evidence inspection and owner acceptance clauses, and detects removal of manager inspection; this proves instruction delivery rather than runtime no-mutation. [11]

## Current contract evidence

- Frozen implementation of STATUS_TABLE supporting the stated file behavior. [1]
- Frozen implementation of status_row supporting the stated file behavior. [2]
- Frozen implementation of read_agent supporting the stated file behavior. [3]
- Frozen implementation of resume_agent supporting the stated file behavior. [4]
- `read_live_agents` makes one read-only `agents-live` bridge call and validates a string-ID list plus a boolean completeness flag. Bridge failures and malformed answers become unreachable readings with a reason; a valid incomplete listing keeps its known IDs and cannot classify an absent recorded agent as gone. The existing per-agent first-match status table and explicit resume path remain unchanged. [12]
