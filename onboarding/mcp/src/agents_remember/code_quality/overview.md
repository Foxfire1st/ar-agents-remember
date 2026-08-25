# Python Quality System Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/code_quality` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[MCP overview](../../overview.md)

## What This Area Is

The certifying Python quality system. It owns Dagger-executed static rails, product CRAP and
changed-code coverage, dependency-attributed selection/retry, causal prerequisite checks, and
machine-readable reports.

## Hot Path Summary

Use `check.py` for orchestration, `dependency_ownership.py` for affected-consumer truth,
`causal_preflight.py` for owner-first failure localization, and `diff_coverage.py` /
`crap_calculator.py` for product release metrics.

## Operating Model

One dependency graph explains selection reasons and retry invalidation. Owner preflights run before
pytest and may account for dependent groups only through explicit edges. The Dagger wrapper remains
the acceptance authority; direct diagnostics and scheduled cadence cannot mint quality evidence.

## Local Invariants And Traps

- Production thresholds stay intact; test support remains linted and typed without recursive
  product-coverage obligations.
- Unknown or ambiguous ownership fails to a fresh safe plan, never optimistic proof reuse.
- One failed owner may classify proven dependents, but independent failures remain visible.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `causal_preflight.py` | [causal_preflight.py.md](causal_preflight.py.md) | covered |
| `dependency_ownership.py` | [dependency_ownership.py.md](dependency_ownership.py.md) | covered |

## Docs And Boundary References

No Domain Documentation or cross-repository source is configured. The canonical implementation
and Dagger reports are same-repository evidence.

## Update History

- 2026-08-25T15:44+02:00 — Created for PDLS quality-scope, dependency-ownership, and causal
  preflight reconciliation. Verification remains closeout-owned.
