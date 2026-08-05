# mcp/src/agents_remember/models/application_requests.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/application_requests.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Wire request records consumed by application operations.

## Code Commentary

### Logic

Module-level surface:

- `LifecycleGateRequest` (class, lines 42-53) — The flat public lifecycle-gate request before domain record construction.
- `GateDecisionRequest` (class, lines 57-67) — One addressed gate verdict with its transport-owned attribution.
- `OperatorInboxPostRequest` (class, lines 71-86) — The flat inbox post before application-owned routing and record construction.
- `OrchestrationNudgeRequest` (class, lines 90-100) — The flat manager-nudge request before target/subject construction.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `LifecycleGateRequest` (lines 42-53) — The flat public lifecycle-gate request before domain record construction.. | `LifecycleGateRequest` | mcp/src/agents_remember/models/application_requests.py:41-53 |
| Defines the class `GateDecisionRequest` (lines 57-67) — One addressed gate verdict with its transport-owned attribution.. | `GateDecisionRequest` | mcp/src/agents_remember/models/application_requests.py:56-67 |
| Defines the class `OperatorInboxPostRequest` (lines 71-86) — The flat inbox post before application-owned routing and record construction.. | `OperatorInboxPostRequest` | mcp/src/agents_remember/models/application_requests.py:70-86 |
| Defines the class `OrchestrationNudgeRequest` (lines 90-100) — The flat manager-nudge request before target/subject construction.. | `OrchestrationNudgeRequest` | mcp/src/agents_remember/models/application_requests.py:89-100 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
