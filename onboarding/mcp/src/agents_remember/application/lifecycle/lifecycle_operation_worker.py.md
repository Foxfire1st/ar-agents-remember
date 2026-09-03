# mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Application lifecycle overview](overview.md)

## Purpose

Runs one detached closeout or integration lifecycle generation under a canonical worker lease.
Since CCR-R22@v1 (L22, commit `685f83c44055`) the worker resolves the configured repository
certification profile (`require_repo(config, contract.repo_name).certification_profile`) once per
operation and forwards it in the shared `common` dict as `certification_profile`, so both
closeout and integration executions admit the exact repository-owned profile instead of reading a
settings executor. The contract is loaded once into `current_contract` and reused by the
closeout and integration branches.

## Code Commentary

### Logic

The worker binds default services, starts/heartbeats/progresses the durable record, executes the
operation, records mutation and publication evidence, and writes a terminal result or typed
failure. `execute_operation` now loads `current_contract` once, resolves the profile reference
via `require_repo`, and passes `certification_profile` in the `common` args shared by
`closeout_result` and `integrate_result`.

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
| Profile resolution at execution and forwarding into closeout/integration common args. | `execute_operation` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:301-350 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `HEARTBEAT_SECONDS` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:1-511 |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the repository profile resolution at operation execution (require_repo + certification_profile forwarded in the common args) and the single contract load shared by closeout/integration branches.

- 2026-08-25T15:44+02:00 -- Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
