# mcp/test_support/agents_remember_test_support/testing/evidence_provenance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/evidence_provenance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Captures one shared exact-candidate and machine identity for non-accepting Dagger evidence.

## Code Commentary

### Logic

`capture_provenance` combines the complete `candidate_snapshot` payload with Python implementation,
platform, machine, pytest, logical CPU count, and executable. A deterministic environment digest
binds those machine facts while the timestamp records observation time. The CLI requires Dagger
admission before publishing the JSON artifact.

### Conventions

This schema describes provenance only. It cannot elevate a cadence, retry, causal, or measurement
artifact into acceptance evidence.

### Invariants And Boundaries

- Candidate identity includes HEAD, HEAD tree, staged candidate tree, and working-path digest.
- Machine identity is explicit rather than inferred from a Dagger image tag.
- Host invocation refuses through the shared Dagger admission boundary.
- Consumers add their own population, topology, phase, repetition, and limitation fields.

### Todos

None recorded.

## Docs References

No external domain documentation governs this repository-owned evidence schema.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate and machine facts form one content-bound provenance payload. | `capture_provenance` | mcp/test_support/agents_remember_test_support/testing/evidence_provenance.py:23-43 |
| The CLI refuses without Dagger admission before publication. | `main` | mcp/test_support/agents_remember_test_support/testing/evidence_provenance.py:46-58 |

## Cross-Repo References

No cross-repository boundary applies.

## Update History

- 2026-08-28T04:37+02:00 — Created for shared candidate/machine provenance across Dagger evidence.
