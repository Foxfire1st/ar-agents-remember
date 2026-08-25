# mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Application lifecycle overview](overview.md)

## Purpose

Runs one detached closeout or integration lifecycle generation under a canonical worker lease.

## Code Commentary

### Logic

The worker binds default services, starts/heartbeats/progresses the durable record, executes the operation, records mutation and publication evidence, and writes a terminal result or typed failure.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- One worker lease owns one generation; journal progress precedes external claims; cancellation and organizational-repair failures preserve durable evidence instead of exiting silently.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `HEARTBEAT_SECONDS` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:1-511 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `HEARTBEAT_SECONDS` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:1-511 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `HEARTBEAT_SECONDS` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:1-511 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
