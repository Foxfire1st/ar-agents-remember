# mcp/src/agents_remember/application/lifecycle/terminal_rail_failure.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/terminal_rail_failure.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:15:00+02:00 |
| lastVerifiedCommitHash | `ce7f10b565f82bc41421d60ba914ee1d0abf61c4` |
| lastVerifiedCommitDate | 2026-09-04T17:04:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Application lifecycle overview](overview.md)

## Purpose

CCR-R20 typed terminal rail-failure propagation at the detached worker boundary (260831-CCR-L20,
code commit `ce7f10b5`). When an enforcing closeout rail fails and the outer lifecycle worker
then crashes, the authoritative terminal journal must preserve the exact failed rail
IDs/versions, stable failure codes, corrective owner classes, candidate/plan identities,
dependency-blocked or skipped rails, and bounded evidence references. An available typed rail
result must never be replaced by a generic worker exception. This module owns the bounded
`terminal-rail-failure-envelope/v1` envelope and the census that
`OperationRuntime.fail` applies to outer Dagger/memory exception families, publishing exactly
three closed classes: `gate-result`, `terminal-rail-result-unavailable`, and
`worker-execution-unclassified`.

## Code Commentary

### Logic

`terminal_worker_failure_result` (terminal_rail_failure.py:146-194) is total: it always
returns a bounded, JSON-serializable envelope and never raises, so the worker boundary can never
fall back to an untyped generic wrapper when typed rail evidence exists. It reads the current
valid published rail report (`_read_published_report`, terminal_rail_failure.py:197-255),
censuses the outer error (`_worker_error_census`, terminal_rail_failure.py:797-843), and
dispatches on the read state: a published candidate-matched schema-3.1 quality manifest becomes a
`gate-result` envelope (`_gate_result_envelope`, terminal_rail_failure.py:283-340) whose
typed rail catalog is copied into the journal; missing/unreadable/mismatched rail evidence becomes
`terminal-rail-result-unavailable` (`_unavailable_envelope`,
terminal_rail_failure.py:343-367) without fabricating any rail outcome; and no current valid rail
report becomes `worker-execution-unclassified` (`_unclassified_envelope`,
terminal_rail_failure.py:370-396). `_with_terminal_identity`
(terminal_rail_failure.py:890-901) stamps a content digest `terminalId` over every other
envelope member so journal, status, wait, and telemetry mirrors share one result identity.
`telemetry_terminal_facts` (terminal_rail_failure.py:904-928) projects the CCR-R16
terminal-event view and `worker_failure_result_class` (terminal_rail_failure.py:931-951)
classifies an existing journal result only when it is a real envelope.

### Conventions

- The envelope is the only thing this module writes; raw command output, secrets, prompts,
  transcripts, and environment values are never copied into it (`_FORBIDDEN_PUBLIC_KEYS`,
  terminal_rail_failure.py:85-109) and all text fields are bounded.
- The closed class vocabulary is shared with the CCR-R16 telemetry mirror
  (`TERMINAL_RESULT_CLASSES`, terminal_rail_failure.py:62-67); a new class must be added to
  both or it is not publishable.

### Invariants And Boundaries

- Failure facts never collapse to `RuntimeError`: typed rail catalogs reach the journal intact.
- No rail outcome is fabricated when evidence is missing, unreadable, or candidate-mismatched.
- The census preserves the exact error type and typed profile/executor family facts instead of
  collapsing them.
- Envelope writing is total; the worker boundary cannot escape through an untyped fallback.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made;
CCR-R20 and the 260831-CCR-L20 delivery record are the governing artifacts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required for this repository-owned terminal envelope. | `TERMINAL_RAIL_FAILURE_SCHEMA_VERSION` | mcp/src/agents_remember/application/lifecycle/terminal_rail_failure.py:56-56 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, envelope contract, and bounded census are implemented here. | `terminal_worker_failure_result`; `__all__` | mcp/src/agents_remember/application/lifecycle/terminal_rail_failure.py:1-951 |
| A published candidate-matched rail report becomes a typed gate-result envelope with its full rail catalog. | `_gate_result_envelope` | mcp/src/agents_remember/application/lifecycle/terminal_rail_failure.py:283-340 |
| Missing, unreadable, or candidate-mismatched rail evidence becomes a typed unavailable envelope without fabricated outcomes. | `_unavailable_envelope` | mcp/src/agents_remember/application/lifecycle/terminal_rail_failure.py:343-367 |
| A worker crash before rail publication is censused, never collapsed to a generic exception. | `_worker_error_census`; `_unclassified_envelope` | mcp/src/agents_remember/application/lifecycle/terminal_rail_failure.py:797-843; mcp/src/agents_remember/application/lifecycle/terminal_rail_failure.py:370-396 |
| The terminal identity and closed class mirror the CCR-R16 operation-terminal payload. | `telemetry_terminal_facts`; `worker_failure_result_class` | mcp/src/agents_remember/application/lifecycle/terminal_rail_failure.py:904-951 |
| `OperationRuntime.fail` routes an unclassified worker failure through the envelope when a durable record exists. | `terminal_worker_failure_result` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:288-295 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `TERMINAL_RAIL_FAILURE_SCHEMA_VERSION` | mcp/src/agents_remember/application/lifecycle/terminal_rail_failure.py:56-56 |

## Update History

- 2026-09-04T17:15+02:00 - 260831-CCR-L20 Gate-5 memory pass: created for CCR-R20 typed terminal
  rail-failure propagation at the detached worker boundary (code commit `ce7f10b5`): bounded
  `terminal-rail-failure-envelope/v1` envelope, closed three-class vocabulary shared with the
  CCR-R16 telemetry mirror, and the census that `OperationRuntime.fail` applies to outer
  Dagger/memory exception families. Verification stamp is the full leaf code commit
  `ce7f10b565f82bc41421d60ba914ee1d0abf61c4`.
