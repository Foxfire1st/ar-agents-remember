# mcp/tests/test_python_test_evidence_firewall.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_python_test_evidence_firewall.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Proves arbitrary non-certifying evidence cannot enter coverage, quality, retry, lifecycle,
closeout, integration, or Dagger report publication and that certifying evidence is bound to
verified immutable reports. L19 bound the exact selection identity into the retry-firewall forgery
so a forged proof must carry the current immutable selection digest too.

## Code Commentary

Tests exercise every accepting consumer, opaque admission forgery, explicitly non-accepting JSON,
candidate tree/digest mismatch, clean-executor publication, and Dagger-only result factories.
Retry forgery supplies the complete current cache/lane identity — including, after L19, a valid
`selection_digest` — so the refusal cannot pass merely because a required field was omitted.

## Invariants And Boundaries

- File serialization does not weaken altitude.
- Consumer tests cover the closed inventory rather than a hand-picked subset.
- Only verified schema-2 publication and exact candidate tree can mint certifying evidence.
- Retry-forgery inputs must be complete under the current retry contract (including the immutable
  selection digest) for the refusal to be meaningful.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Every accepting consumer refuses an arbitrary non-certifying object. | `test_diagnostic_evidence_is_rejected_by_every_accepting_consumer` | mcp/tests/test_python_test_evidence_firewall.py:34-43 |
| Coverage/retry require the opaque admission capability and copied non-accepting JSON cannot publish. | `test_coverage_and_retry_require_the_opaque_admission_capability`; `test_copying_or_renaming_diagnostic_output_cannot_create_publication_authority` | mcp/tests/test_python_test_evidence_firewall.py:45-103 |
| Published Dagger evidence is candidate-bound and digest-protected. | `test_verified_dagger_generation_mints_evidence_for_lifecycle_consumers` | mcp/tests/test_python_test_evidence_firewall.py:105-149 |
| Retry forgery carries the complete current identity including the selection digest. | `test_coverage_and_retry_require_the_opaque_admission_capability` | mcp/tests/test_python_test_evidence_firewall.py:46-81 |

## Docs References

No configured Domain Documentation source applies to this repository-local firewall suite.

## Cross-Repo References

No meaningful cross-repository boundary is exercised; the firewall proof is repository-local.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): recorded the L19 addition of the
  `selection_digest` to the retry-forgery inputs so the firewall exercises the complete current
  retry identity. Verification is pinned to the owning commit.

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: removed the retired production diagnostic
  model from the firewall account. Arbitrary objects and explicit non-accepting JSON now exercise
  the same refusal boundary; retry forgery carries the complete cache/lane identity.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the common `evidence_payload` rename, quality-package relocation, and catalog-owned selection inputs; diagnostic evidence remains unreachable from every accepting consumer.

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
