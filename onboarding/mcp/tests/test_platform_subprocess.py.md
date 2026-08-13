# mcp/tests/test_platform_subprocess.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_platform_subprocess.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T15:19+02:00 |
| lastVerifiedCommitHash |  `1580f92715ff93c988f9a15439ad9bec60ef4c5d`|
| lastVerifiedCommitDate |  2026-08-13T00:18:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite proves the POSIX subprocess boundary rejects every known Windows interop path while preserving native Windows behavior and valid Linux command resolution.

## Code Commentary

### Logic

Parameterized cases cover UNC, drive, mounted-Windows, shim suffixes, symlink resolution, empty PATH, direct and missing executables, environment temp normalization, native command selection, and empty command refusal.

### Conventions

Tests inject the platform string where possible and use temporary executable files for actual resolution behavior.

### Invariants And Boundaries

- Linux automation never crosses into a Windows command or scratch path.
- Native Windows inputs remain unchanged.
- Resolution errors are explicit and deterministic.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this repository policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source is required for the fail-closed regression contract. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Environment, path, executable, command, Windows, and symlink cases are forced. | `test_native_environment_uses_enclosure_reports_and_filters_windows_path`; `test_existing_symlink_that_resolves_to_windows_storage_is_refused` | mcp/tests/test_platform_subprocess.py:18-143 |

## Cross-Repo References

This tests an OS boundary, not a sibling repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| Windows-mounted paths and command shims are refused by Linux execution. | `test_native_environment_uses_enclosure_reports_and_filters_windows_path`; `test_native_executable_resolution_covers_direct_missing_and_incompatible` | mcp/tests/test_platform_subprocess.py:18-80; mcp/tests/test_platform_subprocess.py:98-128 |

## Update History

- 2026-08-12T15:19+02:00 — Created with L23's native POSIX subprocess boundary regressions; verification provenance remains closeout-owned.
