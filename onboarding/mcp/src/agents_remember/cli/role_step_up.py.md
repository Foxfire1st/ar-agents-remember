# mcp/src/agents_remember/cli/role_step_up.py

## Purpose

Select one user-owned role alternative from typed review facts without mutating a seat.

## Governing Overview

[MCP package overview](../../../overview.md)

## Current Contract

Only completed failing code review rounds count for Worker; only completed failing memory review rounds count for Curator. Record-only checks of the unchanged candidate do not add a try; no legacy mixed-code row is reinterpreted as a Curator round. The optional user alternative defaults to afterTries=3 for these roles, not to extra review authority.

select_step_up uses an explicit one-sentence reason, a prior selected step-up or a reached configured threshold. A reason requires a configured alternative; absent settings keep the role’s own choices, warning when a prior selection no longer has configuration. Reasons are trimmed, single-line, nonblank and at most 1000 characters.

Cross-provider/model selection clears omitted model/effort/tier/mode/features/notes, clears hostRole, and uses host-default mode when the alternative omits it; same scope may inherit unmentioned fields. An explicitly native service_tier feature suppresses the inherited tier alias. Origins remain tied to authored alternative keys.

stepUpSelection records source, tries, reason, role and sanitized predecessor note metadata. label_step_up_choices labels authored settings choices while preserving start-call/host-default provenance; step_up_note displays the selected/observed model and source. Host validation, actual predecessor rebinding and durable task publication belong to callers.

A prior selection is retained while an alternative remains configured, not an immutable lock on obsolete settings. Selection alone does not archive a busy seat, grant another round, replace the Reviewer or reset remaining findings.

## Evidence

- Threshold/manual/prior selection uses scoped choices and sanitized provenance. [1]
- The manual reason has an explicit bounded single-sentence shape. [2]
- Only settings-origin selections are relabeled. [3]
- Failed counts use role-specific typed lanes, not total record operations. [4]
- Incomplete typed history yields unknown, not an invented zero/count. [5]
- Test source keeps record-only checks and the memory sequence independent. [6]
