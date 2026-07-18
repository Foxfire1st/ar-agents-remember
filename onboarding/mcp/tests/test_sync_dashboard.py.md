# test_sync_dashboard.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_sync_dashboard.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-18T21:05+02:00                     |
| lastVerifiedCommitHash | `522959ce7dac7402b8085089c1835310adee858b` |
| lastVerifiedCommitDate | 2026-07-18T21:21:15+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This test module verifies the repository-local `scripts/sync-dashboard.py` helper, which
ships the built dashboard cockpit by copying `dashboard/dist/` into
`mcp/src/agents_remember/package_data/dashboard/` (mirroring `sync-runtime.py` /
`sync-skills.py`). It covers digest computation, the copy-then-swap replace, the check/sync
round-trip, the no-op-without-a-build path, and the source/target path contract. A second
`SourceFingerprintTests` class covers the task-35 source-freshness gate: that an unbuilt
`src`/config change trips `--check`, that test/spec/story edits do not, and that the gate is skipped
without a recorded fingerprint or a source tree.

`GeneratedDashboardWhitespacePolicyTests` covers the repository-level Git policy that permits
semantically significant whitespace-only lines in direct shipped Vite JavaScript chunks without
relaxing authored dashboard source. It copies the real root `.gitattributes` into a temporary Git
repository, stages both a generated JavaScript template literal containing the CodeMirror-style
tab-only indentation line and an authored TSX file containing trailing spaces, and proves
`git diff --cached --check` ignores only the generated path while still rejecting the authored
source.

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

`GeneratedDashboardWhitespacePolicyTests` resolves the real root policy through
`GIT_ATTRIBUTES_PATH`, initializes an isolated Git repository, and copies that policy without
reimplementing its matching rules. The test writes a direct shipped
`package_data/dashboard/assets/index-generated.js` fixture whose tab-only line is inside a
JavaScript template literal, plus `dashboard/src/main.tsx` with ordinary trailing spaces. After
staging both paths, it invokes Git's actual cached-diff whitespace checker. The result must remain
nonzero, omit the generated path from diagnostics, and contain the exact authored-source failure.
This is a behavioral Git regression, not a parser or mock of attribute semantics.

### Conventions

The tests use temporary directories and `patch.object` for the module-global
`SOURCE`/`TARGET`/`SOURCE_TREE`/`FINGERPRINT_FILE` so they never mutate or read the real repository tree.
A `_seed` helper builds a minimal temp dashboard checkout for the fingerprint tests.

The whitespace-policy regression also stays hermetic: it copies the checked-out root attribute into
its temporary repository and runs Git there. It deliberately uses the production-shaped direct
`assets/*.js` path and an authored `dashboard/src` near-miss so path scope and source strictness are
exercised together.

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
- Vite owns the emitted JavaScript bytes and `sync-dashboard.py` preserves raw dist/package equality;
  this test must not normalize the tab-only template-literal line because doing so changes the
  CodeMirror completion indentation at runtime.
- The root attribute applies only to direct shipped dashboard `assets/*.js` and disables only
  `blank-at-eol`. Authored source, generated CSS, nested or unrelated JavaScript, `blank-at-eof`, and
  `space-before-tab` remain outside that exception.
- The temporary-repository assertion must prove both halves of the contract in one Git invocation:
  the significant generated line is allowed and the authored TSX contamination still fails.

### Todos

No open file-local todos.

## Docs References

The resolved Domain Documentation registry has no entries. This repository-local Git-policy test
is documented from the checked-out policy, build/sync owners, and executable regression.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module resolves both the hyphenated sync script and the real root attribute from the repository checkout. | L14-L26 | [mcp/tests/test_sync_dashboard.py](agents-remember/mcp/tests/test_sync_dashboard.py) |
| The check/sync round trip, no-build behavior, and package/fingerprint path contract remain hermetic. | L29-L101 | [mcp/tests/test_sync_dashboard.py](agents-remember/mcp/tests/test_sync_dashboard.py) |
| The source-freshness matrix covers source/config staleness, test exclusion, skip paths, and sync-recorded fingerprints. | L104-L213 | [mcp/tests/test_sync_dashboard.py](agents-remember/mcp/tests/test_sync_dashboard.py) |
| The Git-policy regression copies the actual attribute, stages significant generated whitespace beside contaminated authored source, and requires only the authored path to be diagnosed. | L216-L247 | [mcp/tests/test_sync_dashboard.py](agents-remember/mcp/tests/test_sync_dashboard.py) |
| The root policy is scoped to direct shipped dashboard JavaScript assets and disables only `blank-at-eol`. | L1-L3 | [.gitattributes](agents-remember/.gitattributes) |
| The sync helper hashes raw bytes and copy-swaps the Vite output without normalization before verifying dist/package equality. | L59-L68; L133-L172 | [scripts/sync-dashboard.py](agents-remember/scripts/sync-dashboard.py) |
| The production build ends in Vite, which owns and recreates `dashboard/dist`. | package L6-L10; config L61-L67 | [dashboard/package.json](agents-remember/dashboard/package.json); [dashboard/vite.config.ts](agents-remember/dashboard/vite.config.ts) |

## Cross-Repo References

No sibling repository evidence is needed for this test module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-18T21:05+02:00 — FEUI-MX-FIX-5 added the real-Git generated-whitespace policy
  regression: the temporary repository copies the checked-out root attribute, permits a significant
  tab-only line in a direct shipped JavaScript template literal, and still rejects trailing spaces in
  authored `dashboard/src/main.tsx`. Recorded the Vite/raw-sync ownership boundary and corrected the
  card's governing link to the nearest `mcp/tests` overview. Verification metadata remains pinned to
  the last committed source authority until closeout stamps the candidate commit.
- 2026-06-28T16:17+02:00 — Task 35: added `SourceFingerprintTests` for the source-freshness gate (unbuilt source/config change fails `--check`, test/spec/story edits do not, gate skipped without a recorded fingerprint or a source tree, `sync` records and re-verifies a 64-hex fingerprint) and made the existing dist-focused tests hermetic by also patching `FINGERPRINT_FILE`/`SOURCE_TREE`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-14T15:52+02:00 — Created for slice 5a: onboarding for the `scripts/sync-dashboard.py` tests (digests, copy-then-swap replace, check/sync round-trip, no-op-without-build, path contract). Verification metadata pinned until closeout stamps the 5a code commit.
