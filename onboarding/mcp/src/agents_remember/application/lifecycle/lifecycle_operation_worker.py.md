# mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:15:00+02:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
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

Since CCR-R20 (L20, commit `ce7f10b5`) `OperationRuntime.fail` routes an outer worker
failure through the typed terminal rail-failure envelope
(`terminal_worker_failure_result` from `terminal_rail_failure.py`) whenever the durable
record exists and no organizational-repair or ledger-recovery pending payload applies, so an
available typed rail result is journaled instead of collapsing to the generic worker guard.

## Code Commentary

### Logic

The worker binds default services, starts/heartbeats/progresses the durable record, executes the
operation, records mutation and publication evidence, and writes a terminal result or typed
failure. `execute_operation` now loads `current_contract` once, resolves the profile reference
via `require_repo`, and passes `certification_profile` in the `common` args shared by
`closeout_result` and `integrate_result`.

`OperationRuntime.fail` (lifecycle_operation_worker.py:282-309) first consults the durable
record and the organizational-repair decision; when neither a pending repair nor a
`CloseoutLedgerRecoveryDecision` payload applies and the current record exists, it calls
`terminal_worker_failure_result` (lifecycle_operation_worker.py:288-295) with the operation
kind, generation, candidate tree, error, and reports directory, and only falls back to the generic
guard when no typed result was produced.

The process entrypoint parses contract address, operation kind, and worker lease, then declares
the lifecycle process before constructing and binding services. The worker derives its journal from
that contract; a cancelled or completed record returns without replaying the operation. Failure
publication goes through the durable store and typed terminal result, not a worker-authored queue
release or repair. This preserves the journal as the recovery authority.

cit:([`main`], mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:530-538)
cit:([`run_worker`], mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:486-519)
cit:([`fail`], mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:288-315)

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- One worker lease owns one generation; journal progress precedes external claims; cancellation and organizational-repair failures preserve durable evidence instead of exiting silently.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- An available typed terminal rail-failure result must never be replaced by the generic guard:
  `fail` routes through the envelope whenever a durable record exists and no pending
  organizational/ledger decision payload applies.

### Todos

None recorded.

### CCR private preparation boundary

The worker projects retained private preparation separately from consumed approval. Starting the retained generation uses `closeout_recovery_phase`; failure preserves `input-required` with `recovering-private-preparation` and directs inspection of the exact private output. Preparation alone does not justify an after-claim or contract-finalization label. Once approval/publication evidence exists, the ordinary claimed recovery phase applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The current `terminal_operation_record` boundary implements the preparation contract above. | "def terminal_operation_record" | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:388-460 |

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `HEARTBEAT_SECONDS` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:1-527 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `HEARTBEAT_SECONDS` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:1-527 |
| Profile resolution at execution and forwarding into closeout/integration common args. | `execute_operation` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:312-361 |
| `OperationRuntime.fail` routes an unclassified outer failure through the typed terminal rail-failure envelope when a durable record exists. | `fail`; `terminal_worker_failure_result` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:282-309; mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:288-295 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `HEARTBEAT_SECONDS` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:1-527 |

## Update History

- 2026-09-06T23:07:14+00:00 — History-format repair at the actual recorded repair time. The earlier reconciliation note recorded only a local calendar date; its time of day is unknown. Original note preserved verbatim: "- 2026-09-07 — Reconciled the preparation contract introduced by 245057 against surviving d361 source; retained prior history and verification pins."


- 2026-09-04T17:15+02:00 - 260831-CCR-L20 Gate-5 memory pass (code commit `ce7f10b5`):
  recorded CCR-R20 typed terminal rail-failure propagation in `OperationRuntime.fail` -
  unclassified outer Dagger/memory failures route through
  `terminal_worker_failure_result(...)` whenever the durable record exists and no
  organizational-repair or ledger-recovery pending payload applies. Re-anchored whole-file and
  `execute_operation` rows to the post-change layout. Verification stamp is the full leaf code
  commit `ce7f10b565f82bc41421d60ba914ee1d0abf61c4`.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the repository profile resolution at operation execution (require_repo + certification_profile forwarded in the common args) and the single contract load shared by closeout/integration branches.

- 2026-08-25T15:44+02:00 -- Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
