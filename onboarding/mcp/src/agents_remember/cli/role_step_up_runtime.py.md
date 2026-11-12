# mcp/src/agents_remember/cli/role_step_up_runtime.py

## Purpose

Wire task/receipt step-up selection, predecessor provenance and bounded immutable takeover material.

## Governing Overview

[MCP package overview](../../../overview.md)

## Current Contract

Only completed failing code review rounds count for Worker; only completed failing memory review rounds count for Curator. Record-only checks of the unchanged candidate do not add a try; no legacy mixed-code row is reinterpreted as a Curator round. The optional user alternative defaults to afterTries=3 for these roles, not to extra review authority.

For a non-taskless role with an effective task, selected_defaults prefers current receipt stepUp, then a recognized durable task decision. Architect and Investigator use TASKLESS_ROLES and do not probe a request-less singleton receipt even when the context has an effective master; their receipts remain request-scoped at the receipt owner. Unreadable or incomplete typed review count warns and uses base choices absent an explicit/prior selection; explicit or prior selection remains with an unknown count warning. With receipt loss, only a durably observed destination may be called an applied predecessor; an unconfirmed requested destination stays unknown.

step_up_request infers a base holder only after catalog validation and clears interruption authority. bind_step_up_predecessor uses actual prior applied/session choices and sanitized notes, not today’s base settings, and does not overwrite receipt-loss provenance.

successor_prompt preserves prior report paths and freezes from-model/provenance/source, last verdict, remaining finding IDs and uncommitted-files inventories beside the report. The primary handover names its path/hash and states that the worktree/candidate is retained and must be accounted for. Changing the model never changes the task’s Reviewer, fixed findings or round budget.

Inventory runs read-only git status --porcelain=v1 -z with optional locks and fsmonitor disabled, per code/memory root: 1.0-second read budget, 65536 captured bytes, 512 NUL records (rename paths count separately), 4096 diagnostic bytes and 0.2-second reap wait. Incomplete output drops the unfinished record, reports its reason/bytes and freezes an explicit outside-role_start full-read recovery instruction; this is not a complete-looking empty list.

Cleanup attempts process/group termination and waits up to the configured reap interval; `TimeoutExpired` can leave termination unconfirmed. Pipes close in the cleanup `finally` block. The inventory remains incomplete when a read or cleanup reason exists; `reason or cleanup` gives an earlier read diagnostic precedence over the cleanup diagnostic. These are advisory bounded inventories, not a guaranteed successful reap, descriptor-nonblocking setting, runtime time guarantee for the whole start, semantic diff, file-count census or permission to rewrite the frozen takeover material.

## Evidence

- Only non-taskless roles with an effective task inspect singleton receipt/prior decision; review-count warnings and explicit/prior choices remain qualified. [1]
- Per-root inventory constants explicitly bound capture time, bytes, NUL records, diagnostics and bounded reap wait. [8]
- Cleanup attempts process/group termination and bounded waiting, closes pipes and can return unconfirmed termination; an earlier read reason takes precedence. [11]

- The runtime reuses the owner's shared taskless set — `architect`, `investigator` and `bootstrap` — for receipt identity; effective-master presence is not that identity. [12]


- Unconfirmed task metadata cannot assert an applied predecessor. [2]
- Actual receipt choices supply the from record. [3]
- The handover names immutable takeover bytes and retains predecessor report paths. [4]
- Inventory starts a separate process group for bounded cleanup attempts, not a guaranteed successful reap. [5]

- Partial inventories expose recovery instead of pretending completeness. [6]

- Test source exercises bounded partial inventory without blocking later seat start. [7]


- Capture enforces aggregate bytes, diagnostics and NUL-record budgets. [9]
- Selector readiness precedes each descriptor read; the loop checks its monotonic remaining budget and rejects incomplete final records. No descriptor-nonblocking setting or universal OS-read timing bound is inferred. [10]

