# mcp/test_support/agents_remember_test_support/code_quality/causal_continuation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/test_support/agents_remember_test_support/code_quality/causal_continuation.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | overview.md |

## Governing Overview

[Python quality verification](overview.md)

## Purpose

Owns the safe reconciliation between the causal-preflight process result and its durable report.
It converts the pair into a typed decision used by the quality executor. Missing, malformed, or
contradictory evidence never suppresses tests.

## Code Commentary

inspect_causal_report validates the report through the canonical causal-report reader and folds
usage errors into an UNAVAILABLE observation. It does not repair or reinterpret malformed data.

evaluate_preflight_result accepts only two consistent pairs: exit zero plus a validated passed
report, or non-zero exit plus a validated failed report. Every other pair is evidence-unavailable
safe mode. Safe mode keeps the preflight result failing and runs the full selected pytest
population without suppression. A consistent causal failure may reduce only the graph-proven
dependent population through the execution facade.

The decision carries passed, causal_failure, and report_unavailable separately so callers cannot
mistake missing evidence for an observed causal relationship.

## Invariants And Boundaries

- Process exit alone never authorizes suppression.
- Report content alone never overrides a contradictory process exit.
- Missing, malformed, or inconsistent evidence selects full-population safe mode.
- This module classifies continuation; it does not derive dependency relationships.
- A failed preflight remains a quality failure even when dependent tests are skipped.
- No fallback report or compatibility reader is introduced.

## Docs References

None. This behavior is repository-owned.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The report has a closed three-state observation vocabulary. | `CausalReportState` | mcp/test_support/agents_remember_test_support/code_quality/causal_continuation.py:15-18 |
| Invalid or contradictory evidence chooses full-population safe mode. | `evaluate_preflight_result` | mcp/test_support/agents_remember_test_support/code_quality/causal_continuation.py:48-73 |

## Cross-Repo References

None.

## Update History

- 2026-08-28T04:48+02:00 — Created for PDLS remediation after adversarial review proved that
  unavailable causal evidence could not safely retain suppression authority.
