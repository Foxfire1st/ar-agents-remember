# mcp/src/agents_remember/testing/dagger_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/dagger_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns the Dagger nonce/file route guard and mints the opaque capability required by certifying
pytest planning and evidence publication.

## Code Commentary

`dagger_admission_refusal` validates an exact 32-hex nonce and byte-identical attestation file.
`require_dagger_admission` raises before certifying bootstrap on any absent, malformed, unreadable,
or mismatched fact. `DaggerAdmission` has no public constructor; downstream boundaries accept only
an instance carrying this module's private authority object.

## Invariants And Boundaries

- The capability cannot be caller-shaped from a dictionary or boolean.
- Validation happens before certifying planning, collection, execution, or publication.
- The handshake is a wrong-route guard, not hostile-host authentication; the durable
  candidate-bound Dagger report generation establishes acceptance authority.
- No old `code_quality.dagger_environment` compatibility reader remains.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Nonce/file facts are validated as a total refusal. | `dagger_admission_refusal` | mcp/src/agents_remember/testing/dagger_admission.py:55-70 |
| Only the validator mints admission. | `require_dagger_admission` | mcp/src/agents_remember/testing/dagger_admission.py:73-90 |
| Downstream caller-shaped capabilities refuse. | `require_dagger_admission_capability` | mcp/src/agents_remember/testing/dagger_admission.py:93-101 |

## Update History

- 2026-08-24T20:55+02:00 — Moved and narrowed the former code-quality environment validator into
  the testing route; clarified route guard versus durable acceptance authority.
