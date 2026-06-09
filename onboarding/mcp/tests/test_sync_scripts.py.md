# mcp/tests/test_sync_scripts.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_sync_scripts.py`           |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T00:40+02:00                     |
| lastVerifiedCommitHash | `6beccd0545a2d5c161059715d5ed7830917eba03`|
| lastVerifiedCommitDate | 2026-06-09T22:39:28+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

Tests the crash-safe copy-then-swap (`replace_tree`) and Windows
extended-length path helper (`extended_length`) shared by
`scripts/sync-skills.py` and `scripts/sync-runtime.py`.

## Code Commentary

### Logic

The scripts have dashed filenames, so `load_script` loads them via
`importlib.util.spec_from_file_location`, registering each module in
`sys.modules` first (`@dataclass` resolves its defining module there at class
creation). Tests cover: target replaced with source content and stale files
removed, a crash during `copytree` leaving the live target untouched (the
crash-safety contract), re-runs healing stale `.ar-sync-new`/`.ar-sync-old`
leftovers, sync-skills/sync-runtime parity, `extended_length` idempotence and
platform behavior, and cache-name copy ignores.

### Invariants And Boundaries

- The crash-simulation test is the regression guard for the 2026-06-09
  incident where delete-then-copy gutted `package_data` mid-crash; the live
  target must survive any failure before the swap renames.
- Both scripts must keep exposing `replace_tree`, `extended_length`, `shutil`,
  and `os` as module attributes for these tests to patch and inspect.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The scripts under test. | [sync-skills.py](agents-remember-md/scripts/sync-skills.py); [sync-runtime.py](agents-remember-md/scripts/sync-runtime.py) |

## Update History

- 2026-06-10T00:40+02:00: Created with the S7 crash-safe sync rework.
