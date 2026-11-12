# mcp/test_support/agents_remember_test_support/code_quality/causal_continuation.py

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

## Evidence

### Docs References

None. This behavior is repository-owned.

### Repo-Internal References

- The report has a closed three-state observation vocabulary. [1]
- Invalid or contradictory evidence chooses full-population safe mode. [2]

### Cross-Repo References

None.
