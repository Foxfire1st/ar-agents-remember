# mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python quality verification overview](overview.md)

## Purpose

Repository-owned executable adapters for the certification-profile Python rails: it translates one
`quality-config` / `selection-ownership` / `python-suite` / `python-crap` /
`python-diff-coverage` / `verify-teardown` rail invocation into the check.py config and
execution surface, and L19 binds the exact repository selector result into every rail config.

## Code Commentary

### Logic

`build_parser` exposes the six rail subcommands. `_profile_config` rebuilds check.py argv from
the rail arguments, derives the config via `check.config_from_args`, and
`_require_exact_scope` validates the selector's published `repository-selector-result/v2`
JSON against the exact repository-owned derivation (`profile_selection.selection_payload`) and
against the derived executable rail scope; the validated `selection.selectionDigest` is stamped
back into the config via `dataclasses.replace(config, selection_digest=...)`. The
`selection-ownership` and `quality-config` rails run the same exact-scope proof without
executing tests. `_run_python_suite` runs the pytest rail (with retry/causal continuation),
and `_run_post_coverage` dispatches CRAP or diff-coverage from the exact suite artifacts.
`_verify_teardown` requires the clean-room summary schema and a passing teardown checkpoint.

### Invariants And Boundaries

- Every rail requires the Dagger admission capability; refusals surface as
  `repository certification rail refused: ...` with exit 1.
- The selector contract must match the repository-owned derivation byte-for-byte; a mismatch
  refuses before any test command.
- Only the exact immutable selection digest may enter the retry identity.
- Memory-cap bytes must be non-negative; teardown summaries must be schema-checked.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; rails are repository-owned adapters.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Rail config validates the exact selector result and stamps its digest. | `_profile_config`; `_require_exact_scope` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:53-80; mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:83-119 |
| Suite/post-coverage rails consume the exact selector-bound config. | `_run_python_suite`; `_run_post_coverage` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:126-203; mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:223-239 |
| Teardown verification requires the clean-room summary schema and passing checkpoint. | `_verify_teardown` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:242-281 |
| The selector result contract validated here. | `RepositorySelectionResult` | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:89-130 |

## Cross-Repo References

None; these are repository-local rail adapters.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 exact-scope binding — `_require_exact_scope` validates the v2 selector result and
  `_profile_config` stamps `selection.selectionDigest` into the rail config.
  Verification is pinned to the owning commit.
