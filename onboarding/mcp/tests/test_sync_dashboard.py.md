# test_sync_dashboard.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_sync_dashboard.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-28T16:17+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

This test module verifies the repository-local `scripts/sync-dashboard.py` helper, which
ships the built dashboard cockpit by copying `dashboard/dist/` into
`mcp/src/agents_remember/package_data/dashboard/` (mirroring `sync-runtime.py` /
`sync-skills.py`). It covers digest computation, the copy-then-swap replace, the check/sync
round-trip, the no-op-without-a-build path, and the source/target path contract. A second
`SourceFingerprintTests` class covers the task-35 source-freshness gate: that an unbuilt
`src`/config change trips `--check`, that test/spec/story edits do not, and that the gate is skipped
without a recorded fingerprint or a source tree.

## Code Commentary

### Logic

The module loads `scripts/sync-dashboard.py` through `importlib.util` because the script
filename contains a hyphen. `test_file_digests_skips_ignored_and_missing` asserts a missing
dir yields `{}` and that `__pycache__` / `.DS_Store` are skipped.
`test_replace_tree_swaps_target_to_source` builds temp `dist`/`pkg` trees and asserts
`replace_tree` installs the source, drops a stale target file, and omits ignored names.
`test_check_and_sync_roundtrip` patches the module's `SOURCE`/`TARGET` (via
`unittest.mock.patch.object`) to temp dirs and asserts `check()` reports out-of-sync (1)
before `sync()`, then in-sync (0) after. `test_check_noops_without_a_build` asserts a missing
`SOURCE` returns 0 (the shipped placeholder is retained). `test_paths_target_package_data`
asserts `SOURCE` ends `dashboard/dist`, `TARGET` lives under `package_data/dashboard`, and the
`FINGERPRINT_FILE` sidecar sits *beside* `TARGET` (same parent), never inside it. These dist-focused
tests now also patch `FINGERPRINT_FILE` (and where relevant `SOURCE_TREE`) to temp paths so the new
source-freshness gate stays hermetic and never reads the real working tree.

`SourceFingerprintTests` exercises the gate against a temp `_seed`ed dashboard checkout (an `src`
tree plus a `vite.config.ts`), patching `SOURCE_TREE`/`FINGERPRINT_FILE` (and an absent `SOURCE` so the
built-bundle gate no-ops). `test_flags_source_change_without_rebuild` records a fingerprint, asserts
`check()` is 0, then edits a real source module and asserts `check()` becomes 1.
`test_config_change_is_a_build_input` proves the same for a `vite.config.ts` edit.
`test_test_files_do_not_demand_a_rebuild` proves editing a `.test.tsx` module keeps `check()` at 0 while
editing the real module it covers trips it. `test_gate_skipped_until_a_fingerprint_is_recorded` and
`test_gate_skipped_without_a_source_tree` prove the legacy-placeholder and packaged-install no-ops.
`test_sync_records_and_then_verifies_fingerprint` proves `sync()` writes a 64-hex fingerprint and
re-verifies green.

### Conventions

The tests use temporary directories and `patch.object` for the module-global
`SOURCE`/`TARGET`/`SOURCE_TREE`/`FINGERPRINT_FILE` so they never mutate or read the real repository tree.
A `_seed` helper builds a minimal temp dashboard checkout for the fingerprint tests.

### Invariants And Boundaries

- The dashboard sync helper only ever writes `package_data/dashboard` (and the sibling
  `dashboard.fingerprint`).
- Cache/junk names (`__pycache__`, `.DS_Store`) are ignored during sync.
- A stale shipped bundle is detected two ways under `--check`: the `dist`↔`package_data` digest
  comparison (built-bundle gate) and the source-freshness fingerprint (catches `src`/config edits that
  were never rebuilt).
- The fingerprint excludes `.test.`/`.spec.`/`.stories.` modules, so test edits do not demand a rebuild.
- With no `dashboard/dist/` build present, the built-bundle gate is a no-op; the source-freshness gate
  still fires once a fingerprint has been recorded.

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
| The tests load `scripts/sync-dashboard.py` from the repository root despite its hyphenated filename. | L14-L21 | [mcp/tests/test_sync_dashboard.py](agents-remember/mcp/tests/test_sync_dashboard.py) |
| Digest computation and copy-then-swap replace behavior under test. | L25-L57 | [mcp/tests/test_sync_dashboard.py](agents-remember/mcp/tests/test_sync_dashboard.py) |
| The check/sync round-trip, no-op-without-build, and path contract under test (now hermetic against the fingerprint gate). | `SyncDashboardTests` | [mcp/tests/test_sync_dashboard.py](agents-remember/mcp/tests/test_sync_dashboard.py) |
| The source-freshness fingerprint gate under test: unbuilt source/config change fails, test edits do not, skip paths, and sync records a 64-hex fingerprint. | `SourceFingerprintTests` | [mcp/tests/test_sync_dashboard.py](agents-remember/mcp/tests/test_sync_dashboard.py) |
| The script under test (the dashboard build → ship sync + source-freshness fingerprint). | n/a | [scripts/sync-dashboard.py](agents-remember/scripts/sync-dashboard.py) |

## Cross-Repo References

No sibling repository evidence is needed for this test module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-28T16:17+02:00 — Task 35: added `SourceFingerprintTests` for the source-freshness gate (unbuilt source/config change fails `--check`, test/spec/story edits do not, gate skipped without a recorded fingerprint or a source tree, `sync` records and re-verifies a 64-hex fingerprint) and made the existing dist-focused tests hermetic by also patching `FINGERPRINT_FILE`/`SOURCE_TREE`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-14T15:52+02:00 — Created for slice 5a: onboarding for the `scripts/sync-dashboard.py` tests (digests, copy-then-swap replace, check/sync round-trip, no-op-without-build, path contract). Verification metadata pinned until closeout stamps the 5a code commit.
