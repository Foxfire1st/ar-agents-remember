# test_provider_setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T20:45+02:00     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_provider_setup.py` verifies the package-local MCP provider setup helper used by benchmark and worktree preparation flows. It protects explicit provider settings requirements, the typed `ProviderSetupRequest` service entry point, CGC bundle path rewriting, and isolated worktree CGC settings so provider setup can seed or prepare context providers without mutating the main coordinator backend.

## Code Commentary

### Logic

The test module imports `agents_remember.providers.provider_setup` from
`mcp/src`. The explicit-settings tests assert that `settings_path()` rejects
missing provider settings (called as `settings_path(None)` with the single
settings-path argument, no separate root), the CLI parser requires
`--from-settings`, and
`run_provider_setup(ProviderSetupRequest)` accepts a side-effect-free typed
request with providers disabled. Provider setup reporting coverage asserts
dry-runs report unwritten summary paths, real runs write compact setup
summaries under `logs/providers/setup`, and recovered final watcher status is
reported separately from strict phase `ok`. CGC prepare fallback coverage
asserts that a missing seed source does not fail the whole prepare payload when
the refresh fallback is EXPLICITLY opted in — since 260707-HFX-L2 both
fallback tests pass `cgc_refresh_fallback=True`, because the fallback no
longer fires by default — and dry-run refresh is planned.
`test_cgc_refresh_fallback_is_off_by_default` pins the flip itself: the
`ProviderSetupRequest` dataclass default is `False`, the parser default is
`False`, and the positive `--cgc-refresh-fallback` flag is the opt-in.
`test_benign_seed_skips_never_fail_a_prepare` pins `result_ok_for_prepare`'s
forgiveness split directly: a benign skip (no seed intended — no `sourceHead`)
passes without any fallback, a REFUSAL (unrelatable heads, carrying
`sourceHead`/`targetHead`) fails without the opt-in and passes with
`cgc_refresh_fallback=True`.

`test_rewrite_cgc_bundle_paths_rewrites_json_jsonl_and_text` builds a synthetic `.cgc` zip bundle containing JSON, JSONL, and text entries with source repository paths, runs `rewrite_cgc_bundle_paths`, then asserts that the rewritten bundle removes the source root and contains the target root.

`test_cgc_seed_uses_container_mounted_runtime_bundle_paths` asserts the seed export/load argv carries bundle and repo paths in **container form** (`to_container_path`, imported from `providers.context.common`): the expected seed-bundle roots are wrapped in `to_container_path(...)`, and the in-container portion of each command (after `--`) must not match `[A-Za-z]:/` — on Windows hosts that drive-letter guard pins GitHub #58 (host-form `C:/` argv made every seed export fail into the silent reindex fallback); on POSIX the mapping is identity, so the assertions hold tautologically there.

`test_isolated_cgc_settings_targets_worktree_backend` builds a minimal provider
settings object and calls `isolated_cgc_settings`. It asserts that the isolated
settings point CGC roots at the target worktree repository, put CGC runtime and
FalkorDB data under the isolated provider runtime, write watcher logs under the
central workflow-local `logs/providers` tree, omit host `venvRoot` fields, and
derive isolated FalkorDB and runner container names. GrepAI isolated-settings
coverage also asserts that watch logs use `logs/providers/grepai/<instance>`
and that provider setup exposes isolated workflow settings only through the
canonical `isolatedProviderSettings` payload.
UTF-8 subprocess coverage monkey-patches `subprocess.run` and asserts `run_command` passes
`PYTHONUTF8=1`, `PYTHONIOENCODING=utf-8`, and `stdin=subprocess.DEVNULL` to
lifecycle children.

`BenchmarkSeedGuardTests` asserts the hermetic boundary directly: a
benchmark-scoped target (`instance.scope == "benchmark"`) makes
`grepai_seed._resolve_clone_context` and `cgc_seed._resolve_seed_context` return
a `skipped` result even when a seed source is configured, so a benchmark never
clones/seeds from another provider stack.

### Conventions

The tests use temporary directories and synthetic settings; they do not require Docker, FalkorDB, CGC, GrepAI, or network access. They call package-local helper and service functions directly. CLI coverage is limited to parser behavior for required settings, not lifecycle execution.

### Invariants And Boundaries

The tests protect provider setup boundaries: provider setup must not silently
fall back to coordinator `system/settings.json`, typed setup requests must work
without CLI round-tripping, setup summaries must make failed phases
diagnosable, CGC seed failure must not fail prepare when the refresh fallback
is explicitly opted in (and the fallback must stay OFF by default,
260707-HFX-L2), seeded CGC bundles must not retain source checkout paths
after being adapted to a target worktree, worktree provider setup must isolate
runtime/data/log roots, and lifecycle subprocesses must run with UTF-8
environment overrides. These tests should stay side-effect free, should not
start provider watchers or containers, and must not reintroduce host executable
install fields into isolated provider settings.

### Todos

- Add lifecycle fixture coverage only when there is a side-effect-free provider lifecycle fixture that does not require Docker or network access.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The test module imports package-local provider setup code from `mcp/src`, extending the loaded `agents_remember` package path when needed. | `agents_remember` | mcp/tests/test_provider_setup.py:12-24 |
| Explicit-settings coverage asserts missing provider settings are rejected, the parser requires `--from-settings`, and a typed `ProviderSetupRequest` can execute a disabled-provider dry run with setup summary metadata. | `ProviderSetupRequest` | mcp/tests/test_provider_setup.py:20-60 |
| Setup reporting coverage asserts compact summary writes and recovered final status reporting while preserving strict failed-phase `ok=false`. | `ProviderSetupTests` | mcp/tests/test_provider_setup.py:25-899 |
| CGC prepare fallback coverage asserts a missing seed source still yields an overall successful dry-run payload when refresh fallback is enabled and `refresh-all` is planned. | `test_cgc_prepare_is_ok_when_seed_falls_back_to_refresh` | mcp/tests/test_provider_setup.py:281-322 |
| The CGC bundle rewrite test builds JSON, JSONL, and text zip entries that contain a source path, calls `rewrite_cgc_bundle_paths`, then asserts the source path disappeared and the target path appears. | `test_rewrite_cgc_bundle_paths_rewrites_json_jsonl_and_text` | mcp/tests/test_provider_setup.py:372-416 |
| The isolated settings tests build synthetic CGC and GrepAI provider settings and assert target worktree roots, isolated runtime/data/log roots, no CGC `venvRoot` emission, canonical isolated setup payload shape, and derived container names. | `ProviderSetupTests` | mcp/tests/test_provider_setup.py:25-899 |
| The UTF-8 subprocess test monkey-patches `subprocess.run` and asserts `run_command` passes `PYTHONUTF8=1`, `PYTHONIOENCODING=utf-8`, and `stdin=subprocess.DEVNULL`. | `test_run_command_forces_utf8_for_lifecycle_children` | mcp/tests/test_provider_setup.py:876-899 |
| Package-local provider setup owns the typed request and runner path used by this test module. | `ProviderSetupRequest`; `run_provider_setup` | mcp/src/agents_remember/providers/provider_setup.py:57-120; mcp/src/agents_remember/providers/provider_setup.py:547-555 |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-04T13:25:51+02:00 — 260731-EFA-L6 S18-B01 same-reviewer semantic-binding repair: bound provider rewrite and subprocess claims to complete test bodies under the adversarial verdict, then the exact scoped fixer/check passed.
- 2026-08-02T21:40:21+02:00 — 260731-EFA-L6 curator W2-B10: repaired 10 citation findings (4 reference rows and 2 prose citations); scoped recheck clean.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file citation after source
  movement. The four helper surfaces are re-exported by `provider_setup.py`, while the module owns
  the typed request and runner path: cit:([`require_settings_path`], mcp/src/agents_remember/providers/setup_common.py:46-52); cit:([`run_command`], mcp/src/agents_remember/providers/setup_common.py:109-146); cit:([`isolated_cgc_settings`], mcp/src/agents_remember/providers/cgc/setup.py:42-54); cit:([`rewrite_cgc_bundle_paths`], mcp/src/agents_remember/providers/cgc/bundle.py:79-99) and
  cit:([`ProviderSetupRequest`, `run_provider_setup`], mcp/src/agents_remember/providers/provider_setup.py:57-120; mcp/src/agents_remember/providers/provider_setup.py:547-555).
  Separators normalized from commas to semicolons. Not repaired and reported upward instead: the
  seven self-citations above this row still point at a much older, smaller revision of
  `test_provider_setup.py` (now 942 lines) despite the 16:40 entry below.

- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/tests/test_provider_setup.py` and moved the lines this card cites, so the Citations column
  no longer pointed at the code its rows name. Corrected the ranges (L62-L192 → L62-L193;
  L194-L235 → L195-L236; L102-L146 → L102-L147; L285-L626 → L286-L623; L214-L237 → L215-L238). The
  behaviour described is unchanged — the file's AST is identical to the base revision — this is a
  citation repair only. Verification metadata pinned until closeout stamps the L2 commit.

- 2026-07-07T20:45+02:00 — 260707-HFX-L2 review follow-up: added
  `test_benign_seed_skips_never_fail_a_prepare`, pinning `result_ok_for_prepare` directly — a
  benign skip (no `sourceHead`) passes with the fallback off, a refusal fails without the opt-in
  and passes with it. Verification metadata pinned until closeout stamps the HFX-L2 commit.
- 2026-07-07T19:30+02:00 — 260707-HFX-L2 (index lifecycle): the two refresh-fallback tests now opt
  IN explicitly (`cgc_refresh_fallback=True`) because the fallback default flipped off; new
  `test_cgc_refresh_fallback_is_off_by_default` pins the dataclass default, the parser default,
  and the positive `--cgc-refresh-fallback` opt-in flag. Verification metadata pinned until
  closeout stamps the HFX-L2 commit.
- 2026-06-19T13:42: Added `BenchmarkSeedGuardTests` — asserts the GrepAI clone and CGC seed resolvers refuse a benchmark-scoped target (return a `skipped` hermetic result) even with a source configured (task 260619).
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-10T07:30+02:00 — Added `test_prepare_announces_phases_in_order_with_seed_fallback`: a recording `SetupProgress` driven through a full dry-run prepare (mocked seed/clone bundles) pins the phase order (grepai install, cgc install-all, grepai clone-db, cgc seed, cgc refresh-all, watchers start/status) and that ONLY the refresh-all fallback start carries `seed_fallback` with the seed's refusal reason (GitHub #53).
- 2026-06-10T07:05+02:00 — Seed argv assertions switched to container form (`to_container_path` from `providers.context.common`) plus a no-drive-letter regex guard on the post-`--` argv, pinning the GitHub #58 Windows seed-export fix.
- 2026-06-01T20:45+02:00 — Updated the isolated-grepai assertion to expect the workspace-scoped `workspace` key (clone-reuse fix).
- 2026-05-31T12:50+02:00 — `test_settings_path_requires_explicit_provider_settings` now calls `provider_setup.settings_path(None)` (single settings-path arg) instead of `settings_path(root, None)` and drops its `TemporaryDirectory`, following `settings_path()` losing its leading `root` parameter; noted the single-arg call in Logic (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Replaced `assertIsNotNone` with `assert ... is not None` so the isolated-settings locals narrow before subscript; behavior-preserving (commit `0549b28`).
- 2026-05-28T14:21:08+02:00: Updated after provider setup tests asserted
  duplicate per-provider isolated settings payload keys are absent.
- 2026-05-28T13:40+02:00: Updated after provider setup tests removed CGC `venvRoot` from settings fixtures and isolated settings expectations.
- 2026-05-28T12:32+02:00: Updated after provider setup tests added setup summary reporting and central isolated provider log path assertions.
- 2026-05-24T05:48+02:00: Updated after provider setup tests added CGC seed failure plus refresh fallback coverage.
- 2026-05-24T00:04+02:00: Updated after provider setup tests added explicit settings requirements and typed `ProviderSetupRequest` service coverage.
- 2026-05-23T13:46+02:00: Updated after provider setup moved into `agents_remember.providers.provider_setup` and source scripts were removed.
- 2026-05-23T05:32+02:00: Updated after provider setup script tests switched from installed runtime scripts to top-level source/package-owned scripts.
- 2026-05-21T23:18+02:00: Updated after adding UTF-8 lifecycle child environment coverage.
- 2026-05-21T08:14+02:00: Created onboarding for provider setup unit tests and their isolated CGC settings coverage.
