# test_sync_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_sync_runtime.py`           |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-08T11:53+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                         |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                              |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The tests load `scripts/sync-runtime.py` from the repository root despite its hyphenated filename. | `load_sync_runtime` | mcp/tests/test_sync_runtime.py:13-20 |
| The diff test verifies missing, extra, and changed file reporting. | `test_diff_reports_missing_extra_and_changed_files` | mcp/tests/test_sync_runtime.py:24-45 |
| The sync test verifies target replacement and cache-directory ignore behavior. | `test_sync_target_replaces_target_with_source_tree` | mcp/tests/test_sync_runtime.py:47-70 |
| The target-boundary test verifies default targets are package-data-only and exclude harness starter package folders. | `test_default_targets_only_write_to_mcp_package_data` | mcp/tests/test_sync_runtime.py:72-84 |

## Cross-Repo References

No sibling repository evidence is needed for this test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T18:43+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 4 citation rows with exact anchors (`load_sync_runtime` + `SCRIPT_PATH` extent and the three named test functions) and ledger-verified ranges. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/tests/test_sync_runtime.py` and moved the lines this card cites, so the Citations column no
  longer pointed at the code its rows name. Corrected the ranges (L48-L69 → L48-L71; L71-L83 →
  L73-L85). The behaviour described is unchanged — the file's AST is identical to the base
  revision — this is a citation repair only. Verification metadata pinned until closeout stamps
  the L2 commit.

- 2026-06-08T11:53+02:00: Created onboarding for the focused runtime sync helper tests. Verification metadata is pending until the code commit exists.
