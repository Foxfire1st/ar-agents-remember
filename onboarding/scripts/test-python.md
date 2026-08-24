# scripts/test-python

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `scripts/test-python` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
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
| The wrapper pins uv configuration, project, Python, and one module. | full script | scripts/test-python:1-7 |
| Direct-runner tests enforce the wrapper shape and executable bit. | `test_repository_wrapper_is_executable_and_pins_the_direct_route` | mcp/tests/test_direct_test_runner.py:202-213 |

## Update History

- 2026-08-24T20:55+02:00 — Created for 260824-PDLS.
