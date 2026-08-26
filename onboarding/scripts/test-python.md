# scripts/test-python

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `scripts/test-python` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[repository overview](../overview.md)

## Purpose

Provides the single human/agent-facing command for bounded direct Python diagnostic feedback.

## Code Commentary

The executable shell wrapper resolves its own repository root and invokes Python 3.12 through
`uv --no-config` with `mcp/pyproject.toml`, the development extra, and exactly one
`agents_remember.testing.direct_runner` module entrypoint. All selector parsing, eligibility,
environment isolation, and evidence labeling remain in the typed Python owner.

## Invariants And Boundaries

- The wrapper does not call Dagger, raw pytest, coverage, or an alternate runner.
- It accepts exact node IDs only through the Python entrypoint; it adds no pass-through flags.
- A zero exit is useful local feedback, never acceptance.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wrapper pins uv configuration, project, Python, and one module. | "set -euo pipefail"; "exec uv --no-config run --project"; "--python 3.12 --extra dev"; "python -m agents_remember.testing.direct_runner" | scripts/test-python:2-2; scripts/test-python:6-6; scripts/test-python:7-7 |
| Direct-runner tests enforce the wrapper shape and executable bit. | `test_repository_wrapper_is_executable_and_pins_the_direct_route` | mcp/tests/test_direct_test_runner.py:253-262 |

## Update History

- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.