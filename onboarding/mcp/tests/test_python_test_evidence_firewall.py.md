# mcp/tests/test_python_test_evidence_firewall.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_python_test_evidence_firewall.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Proves diagnostic evidence cannot enter coverage, quality, retry, lifecycle, closeout, integration,
or Dagger report publication and that certifying evidence is bound to verified immutable reports.

## Code Commentary

Tests exercise every accepting consumer, strict payload altitude, candidate tree/digest mismatch,
caller-shaped evidence, clean-executor publication, quality-gate recovery, and Dagger-only result
factories. The route-neutral phase report is checked as an exported observation, never as authority.

## Invariants And Boundaries

- File serialization does not weaken altitude.
- Consumer tests cover the closed inventory rather than a hand-picked subset.
- Only verified schema-2 publication and exact candidate tree can mint certifying evidence.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Every accepting consumer refuses diagnostics. | `test_diagnostic_evidence_is_rejected_by_every_accepting_consumer` | mcp/tests/test_python_test_evidence_firewall.py:41-50 |
| Published Dagger evidence is candidate-bound. | `test_verified_dagger_generation_mints_evidence_for_lifecycle_consumers` | mcp/tests/test_python_test_evidence_firewall.py:102-146 |

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the common `evidence_payload` rename, quality-package relocation, and catalog-owned selection inputs; diagnostic evidence remains unreachable from every accepting consumer.

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
