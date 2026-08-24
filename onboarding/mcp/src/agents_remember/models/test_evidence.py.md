# mcp/src/agents_remember/models/test_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/test_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[response contract models](overview.md)

## Purpose

Defines the typed evidence-altitude firewall between local Python diagnostic feedback and
candidate-bound Dagger acceptance.

## Code Commentary

`CandidateBinding` identifies direct evidence by classifier policy, exact closure/configuration
digest, and configuration paths. `DiagnosticTestEvidence` carries exact nodes and exit code.
`CertifyingTestEvidence` has no public constructor and can be minted only by the verified Dagger
publication adapter's private authority. `require_certifying_evidence` refuses diagnostics for
coverage, quality, retry, route review, lifecycle, closeout, and integration. Strict serialization
and loading preserve altitude across a file boundary and reject unknown fields.

## Invariants And Boundaries

- A passing diagnostic exit code never becomes acceptance.
- Payload names, paths, booleans, or caller-supplied dictionaries cannot elevate altitude.
- Only verified immutable Dagger publication mints certifying evidence.
- Local feedback is the only consumer allowed to receive diagnostics.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Altitudes and consumers are closed enums. | `EvidenceAltitude`; `EvidenceConsumer` | mcp/src/agents_remember/models/test_evidence.py:14-31 |
| Certifying evidence has a private factory authority. | `CertifyingTestEvidence`; `_certifying_evidence_from_verified_dagger` | mcp/src/agents_remember/models/test_evidence.py:60-91 |
| Accepting consumers reject diagnostic altitude. | `require_certifying_evidence` | mcp/src/agents_remember/models/test_evidence.py:143-174 |

## Cross-Repo References

No external repository may mint or reinterpret this evidence vocabulary.

## Update History

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
