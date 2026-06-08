# test_sync_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_sync_runtime.py`           |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-08T11:53+02:00                     |
| lastVerifiedCommitHash | `19b33573a71c8634acfb836d4245f1ead8594f06`                         |
| lastVerifiedCommitDate | 2026-06-08T12:38:40+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

This test module verifies the repository-local `scripts/sync-runtime.py` helper.
It covers stale-copy diff reporting, target replacement behavior, ignored cache
directories, and the invariant that default runtime asset targets write only to
MCP package data rather than harness starter packages.

## Code Commentary

### Logic

The module loads `scripts/sync-runtime.py` through `importlib.util` because the
script filename contains a hyphen. The first test builds temporary source and
target trees and verifies that `diff_target` reports one missing file, one extra
file, and one changed file. The second test verifies `sync_target` removes stale
target files, copies source content, ignores `__pycache__`, and leaves the
target in sync. The third test inspects the script's default `TARGETS` and
asserts they are exactly `agents-md-files`, `benchmarks`, `providers`, and
`system`, with target paths under `mcp/src/agents_remember/package_data/` and
not under harness starter package folders.

### Conventions

The tests use temporary directories for copy/diff behavior and do not mutate the
real repository package-data tree.

### Invariants And Boundaries

- The runtime sync helper remains package-data-only.
- Cache directories and `.pyc` files are ignored during sync.
- Stale generated targets are detected by digest comparison.

### Todos

No open file-local todos.

## Docs References

No external documentation is needed for this repository-local test.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests load `scripts/sync-runtime.py` from the repository root despite its hyphenated filename. | L11-L21 | [mcp/tests/test_sync_runtime.py](agents-remember-md/mcp/tests/test_sync_runtime.py) |
| The diff test verifies missing, extra, and changed file reporting. | L24-L46 | [mcp/tests/test_sync_runtime.py](agents-remember-md/mcp/tests/test_sync_runtime.py) |
| The sync test verifies target replacement and cache-directory ignore behavior. | L48-L69 | [mcp/tests/test_sync_runtime.py](agents-remember-md/mcp/tests/test_sync_runtime.py) |
| The target-boundary test verifies default targets are package-data-only and exclude harness starter package folders. | L71-L83 | [mcp/tests/test_sync_runtime.py](agents-remember-md/mcp/tests/test_sync_runtime.py) |

## Cross-Repo References

No sibling repository evidence is needed for this test module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-08T11:53+02:00: Created onboarding for the focused runtime sync helper tests. Verification metadata is pending until the code commit exists.
