# test_cgc_seed_bundle_path.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_cgc_seed_bundle_path.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T23:40+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                              |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_cgc_seed_bundle_path.py` protects the OQ5 fix: the cgc seed must write
the rewritten bundle under the worktree's cgc instance runtime root, not the
workspace runner root the worktree runner cannot see. Tests confirm that
`_seed_target_runtime_root` resolves from the isolated worktree settings when
isolated and falls back to the caller's workspace settings otherwise, and that
`_cgc_settings_path` honors the `cgc_from_settings > provider_from_settings >
from_settings` priority chain.

## Code Commentary

### Logic

`SeedTargetRuntimeRootTests` imports `_cgc_settings_path` and
`_seed_target_runtime_root` directly from `seed` and patches `seed_module` internals
via `mock.patch.object`:

- `test_isolated_resolves_from_worktree_settings_not_passed_settings`: args
  has `cgc_isolated_runtime_root` set and `from_settings` pointing at the
  worktree settings file. `load_settings` returns a fake isolated-settings
  dict. Asserts that `_seed_target_runtime_root` calls `load_settings` with
  `args.from_settings` (the isolated path) and calls `_seed_runtime_root` with
  the isolated settings — never the caller's workspace `settings` dict. The
  returned path is the resolved instance root.

- `test_isolated_falls_back_when_settings_unreadable`: `load_settings` returns
  `None` (file missing). Asserts that the function falls back to calling
  `_seed_runtime_root` with the caller's workspace `settings` dict — the same
  behavior as a non-isolated seed.

- `test_settings_path_matches_the_import_priority_chain`: constructs args with
  all three settings attributes set and asserts `_cgc_settings_path` returns
  `cgc_from_settings` (highest priority). Then constructs args with only
  `from_settings` and asserts that is returned. Verifies the chain matches
  `cgc_extra_args`.

- `test_non_isolated_uses_passed_settings`: `cgc_isolated_runtime_root` is
  `None`. Asserts `_seed_runtime_root` is called with the caller's workspace
  `settings` — the isolated branch is never entered.

All tests use `SimpleNamespace` for args and `mock.patch.object` to isolate
`load_settings` and `_seed_runtime_root`. No Docker, FalkorDB, or filesystem
access is required.

### Conventions

Pure unit tests with no I/O or network access. Args are constructed with
`types.SimpleNamespace` and cast to `object` to satisfy the type checker.
Module-level symbols are patched via `mock.patch.object(seed_module, ...)` so
the patches target the same symbol the function under test resolves.

### Invariants And Boundaries

The tests protect that: an isolated worktree seed always resolves the bundle
path from the isolated settings (matching the `--from-settings` the `bundle
import` itself uses); unreadable isolated settings degrade gracefully to the
workspace path; the `_cgc_settings_path` priority chain is identical to the
chain in `cgc_extra_args` so the settings file used by the import and the file
used for path resolution are always the same.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `_seed_target_runtime_root` and `_cgc_settings_path` live in the CGC seed module. | [seed.py](agents-remember/mcp/src/agents_remember/providers/cgc/seed.py) |
| `cgc_extra_args` uses `_cgc_settings_path` with the same priority chain verified here. | [seed.py](agents-remember/mcp/src/agents_remember/providers/cgc/seed.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/tests/test_cgc_seed_bundle_path.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 4 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-06-01T23:40+02:00 — Created onboarding for the new OQ5 seed bundle-path resolution tests.
