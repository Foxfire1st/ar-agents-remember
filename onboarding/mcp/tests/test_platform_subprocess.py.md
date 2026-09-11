# mcp/tests/test_platform_subprocess.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_platform_subprocess.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash |  `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate |  2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises the POSIX subprocess boundary: Windows-backed PATH entries are filtered, enclosure reports own native temporary files, native tool resolution ignores Windows shims, and explicit Windows commands or temporary roots refuse. Native Windows inputs remain unchanged. These cases use temporary paths and explicit platform arguments; they do not execute a Windows installation.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Native environment uses enclosure reports and filters windows path | `test_native_environment_uses_enclosure_reports_and_filters_windows_path` | mcp/tests/test_platform_subprocess.py:16-33 |
| Native command prefers the linux tool after a windows path | `test_native_command_prefers_the_linux_tool_after_a_windows_path` | mcp/tests/test_platform_subprocess.py:36-48 |
| Native command refuses an explicit windows shim | `test_native_command_refuses_an_explicit_windows_shim` | mcp/tests/test_platform_subprocess.py:51-55 |
| Native environment refuses windows backed temp root | `test_native_environment_refuses_windows_backed_temp_root` | mcp/tests/test_platform_subprocess.py:58-64 |
| Windows runner keeps its environment and paths unchanged | `test_windows_runner_keeps_its_environment_and_paths_unchanged` | mcp/tests/test_platform_subprocess.py:67-72 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-12T15:19+02:00 — Created with L23's native POSIX subprocess boundary regressions; verification provenance remains closeout-owned.
