# mcp/tests/test_python_runtime_contract.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_python_runtime_contract.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T16:10+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Pins one exact Python 3.13 runtime contract across package metadata, CI, release, Dagger, and the
interpreter that actually executes the test population.

## Code Commentary

### Logic

`_contract` reads the canonical runtime environment file. The metadata test requires 3.13.15 and
the bounded `>=3.13,<3.14` package range everywhere, while explicitly rejecting the old 3.11 and
3.12 classifiers. The Linux capability test invokes the canonical runtime probe with the current
test interpreter and requires both native pidfd APIs.

### Conventions

The test compares exact durable text at configuration boundaries and parses the probe's structured
JSON for runtime capabilities. A version string alone never counts as Linux compatibility proof.

### Invariants And Boundaries

- CI, release, Dagger, and package metadata cannot silently select different Python minors.
- Linux acceptance fails if either native pidfd API is absent.
- The test does not permit system Python, a compatibility wrapper, or a signaling fallback.
- Dagger owns certifying execution.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; repository configuration is the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is needed to verify internal runtime alignment. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One exact Python 3.13.15 contract is required across package, CI, release, and Dagger. | `test_runtime_contract_has_one_exact_supported_minor` | mcp/tests/test_python_runtime_contract.py:13-42 |
| The executing Linux interpreter must pass the canonical native-pidfd probe. | `test_current_test_interpreter_passes_the_canonical_capability_probe` | mcp/tests/test_python_runtime_contract.py:45-66 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The proof is confined to the Agents Remember candidate. | — | — |

## Update History

- 2026-08-29T16:10+02:00 — Created for the project-wide Python 3.13.15 cutover and native-pidfd
  acceptance boundary. Verification remains closeout-owned.
