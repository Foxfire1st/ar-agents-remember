# Python Test Infrastructure Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/testing` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[MCP overview](../../overview.md)

## What This Area Is

Owned Python test-infrastructure contracts: Dagger admission, hermetic setup, evidence lanes and
lifecycle, sealed direct-diagnostic eligibility, dependency-aware causal reporting, and pytest
plugins. The package initializer deliberately exports no public facade.

## Hot Path Summary

Use `dagger_admission.py` for certifying authority, `certifying_bootstrap.py` and
`hermetic_bootstrap.py` for setup, `cohort_manifest.py`/`eligibility.py` for the sealed direct
cohort, `evidence_lifecycle.py` for durable proof metadata, and `causal_failures.py` for pytest-side
classification.

## Operating Model

Certifying pytest admits Dagger before collection, then composes shared hermetic setup. The direct
route uses an exact content-sealed cohort and produces only diagnostic evidence. Durable fixtures
and support are catalogued with authority, fidelity, cadence, lifetime, and replacement.

## Local Invariants And Traps

- Import leaf owners directly; adding package-level re-exports recreates bootstrap import fan-out.
- Diagnostic evidence cannot satisfy coverage, retry, closeout, integration, or quality consumers.
- Unknown effects or dependencies refuse direct execution; there is no route fallback.
- Causal suppression requires an explicit dependency edge and never hides independent failures.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | covered |
| `causal_failures.py` | [causal_failures.py.md](causal_failures.py.md) | covered |
| `cohort_manifest.py` | [cohort_manifest.py.md](cohort_manifest.py.md) | covered |
| `evidence_lifecycle.py` | [evidence_lifecycle.py.md](evidence_lifecycle.py.md) | covered |

## Docs And Boundary References

No configured Domain Documentation or cross-repository source applies. The PDLS task rationale
and Dagger reports are planning/evidence artifacts, while durable behavior is cited from source.

## Update History

- 2026-08-25T15:44+02:00 — Created for the PDLS evidence-lane and bootstrap-import ownership
  model. Verification remains closeout-owned.
