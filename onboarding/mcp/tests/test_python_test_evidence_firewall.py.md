# mcp/tests/test_python_test_evidence_firewall.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_python_test_evidence_firewall.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Proves arbitrary non-certifying evidence cannot enter coverage, quality, retry, lifecycle,
closeout, integration, or Dagger report publication and that certifying evidence is bound to
verified immutable reports.

## Code Commentary

Tests exercise every accepting consumer, opaque admission forgery, explicitly non-accepting JSON,
candidate tree/digest mismatch, clean-executor publication, and Dagger-only result factories.
Retry forgery supplies the complete current cache/lane identity so the refusal cannot pass merely
because a required field was omitted.

## Invariants And Boundaries

- File serialization does not weaken altitude.
- Consumer tests cover the closed inventory rather than a hand-picked subset.
- Only verified schema-2 publication and exact candidate tree can mint certifying evidence.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Every accepting consumer refuses an arbitrary non-certifying object. | `test_diagnostic_evidence_is_rejected_by_every_accepting_consumer` | mcp/tests/test_python_test_evidence_firewall.py:34-43 |
| Coverage/retry require the opaque admission capability and copied non-accepting JSON cannot publish. | `test_coverage_and_retry_require_the_opaque_admission_capability`; `test_copying_or_renaming_diagnostic_output_cannot_create_publication_authority` | mcp/tests/test_python_test_evidence_firewall.py:45-103 |
| Published Dagger evidence is candidate-bound and digest-protected. | `test_verified_dagger_generation_mints_evidence_for_lifecycle_consumers` | mcp/tests/test_python_test_evidence_firewall.py:105-149 |

## Update History

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: removed the retired production diagnostic
  model from the firewall account. Arbitrary objects and explicit non-accepting JSON now exercise
  the same refusal boundary; retry forgery carries the complete cache/lane identity.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the common `evidence_payload` rename, quality-package relocation, and catalog-owned selection inputs; diagnostic evidence remains unreachable from every accepting consumer.

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
