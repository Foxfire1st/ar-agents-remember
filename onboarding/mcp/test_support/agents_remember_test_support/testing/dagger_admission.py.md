# mcp/test_support/agents_remember_test_support/testing/dagger_admission.py

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

## Evidence

### Repo-Internal References

- Nonce/file facts are validated as a total refusal. [1]
- Only the validator mints admission. [2]
- Downstream caller-shaped capabilities refuse. [3]
