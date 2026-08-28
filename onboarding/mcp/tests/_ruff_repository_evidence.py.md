# mcp/tests/_ruff_repository_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_ruff_repository_evidence.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This shared test-support boundary runs Ruff against the repository's real configuration and tracked
Python inventory for architecture-fitness assertions.

## Logic

`ruff_lint_configuration` reads the canonical lint table. `run_ruff_over_tracked_python` resolves
the inventory through the quality support's Git reader, while
`run_ruff_with_repository_configuration` forces the real `pyproject.toml` for temporary samples.
The module centralizes subprocess/configuration mechanics only; individual tests own policy claims.

## Invariants And Boundaries

- It is test support, not operational product code.
- It never supplies a fallback Ruff configuration.
- Its exact consumers are `test_code_quality_check.py`, `test_code_quality_check_scope.py`,
  `test_code_quality_tool_signature_exemption.py`, and `test_file_size_detector.py`, registered in
  `evidence-lifecycle.toml`.
- The stable executable replacement contract is `repository-ruff-policy-evidence`.

## Update History

- 2026-08-27T13:32+02:00 — Extracted the shared repository-configured Ruff boundary while splitting
  the oversized quality test by policy responsibility. Verification metadata remains pinned until
  PDLS closeout stamps the candidate commits.
