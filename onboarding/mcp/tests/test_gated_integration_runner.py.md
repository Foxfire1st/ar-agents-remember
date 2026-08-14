# mcp/tests/test_gated_integration_runner.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/tests/test_gated_integration_runner.py` |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-31T15:32+02:00                       |
| lastVerifiedCommitHash | `aeca9a2839c965218a61a3040e15cb84367ebeca`   |
| lastVerifiedCommitDate | 2026-08-14T13:35:55+02:00|
| governingOverview      | `overview.md`                                |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The gated integration paths have a runner, and the runner reaches all of them.

`pyproject.toml` registered **eight** markers for suites that skip unless an `AR_*`
variable opts them in, and `test_code_quality_check.py` already held that registry in step
with the suite's skip decorators. Both of those were true while **nothing ran any of the
eight**: the markers were registered but never *applied*, so `pytest -m ar_run_pi_rpc_smoke`
selected nothing at all, and no job or script set any of the variables. This module closes
that third gap.

## Why The Gap Was Silent

`--strict-markers` rejects an *unknown* marker. A registered marker that decorates nothing
selects zero tests, and pytest reports that as a **successful run of an empty selection**.
All eight were in that state until 260731-EFA-L2.

## Code Commentary

### `GatedPathInventoryTests` — two-way reconciliation

- `test_every_registered_marker_is_applied_to_at_least_one_test` — runs a real
  `pytest -m <marker> --collect-only` per marker (`selected_test_count`) and requires a
  non-zero selection. This is the assertion that was missing.
- `test_the_runner_covers_every_registered_marker_and_invents_none` — the marker set of
  `scripts/run-gated-integration.py`'s `PATHS` equals the registered set exactly, in both
  directions: a path cannot be registered, documented and still unreachable, and the runner
  cannot claim a path the suite no longer has.
- `test_every_path_states_what_it_requires` — each path carries a non-empty `requires` and
  a category of `CREDENTIAL_FREE` or `VENDOR_CREDENTIALS`.
- `test_the_credential_free_paths_are_exactly_the_two_dagger_safe_runs` — the two credential-free paths are
  `ar-run-pi-rpc-smoke` (installs its own Pi and drives it offline against 127.0.0.1) and
  `agents-remember-real-mcp-config` (spawns this repository's own server against a
  generated settings file). The other **six** need an installed, signed-in vendor CLI, and
  four of those bill for real turns — which is why they stay behind the local runner.
  Asserting it here rather than leaving it to a workflow file nobody reads is the point.
- `test_github_pr_checks_do_not_bypass_dagger_for_gated_pytest_paths` — no GitHub workflow invokes
  the gated runner or host pytest; the repository-wide Dagger attestation guard remains authoritative.
- `test_the_dry_run_selection_names_a_test_that_exists` — a stale `DRY_RUN_NODE` would make
  an acceptance selection run nothing and still exit 0, so the node id is split and looked up in source.

### `RunnerBehaviourTests` — the runner itself

- **Anti-skip guard**: `verify_passed` must fail a short run. A skipped test exits pytest 0,
  so without a required-count check a runner reports success for a job that ran nothing.
  A missing report and a report with no `<testsuite>` both fail too.
- **No credentials on disk**: the generated settings file is scanned for `apiKey`,
  `api_key`, `token`, `password`, `secret`.
- **A plannable tree**: `write_settings` creates `ar-coordination/`, `workspace/` and
  `ar-coordination/memory-repos/ar-agents-remember/`.
- **Child environment**: the opt-in variable is set (`AR_RUN_PI_RPC_SMOKE=1`), `MCP_SRC` is
  on `PYTHONPATH`, and the settings path travels as `AGENTS_REMEMBER_REAL_MCP_CONFIG`.
- **Readiness** names a missing binary by name and answers "no binary needed" when a path
  needs none; `list` reports readiness without running anything.
- **Selection**: `pytest_command` selects by marker unless a node id is named, in which case
  the node and `--junit-xml` are used.

`load_runner()` path-imports `scripts/run-gated-integration.py` via `importlib.util` and
registers it in `sys.modules` before executing it.

## Invariants And Boundaries

- Registered marker set, applied marker set, and runner path set are **one set**, asserted
  in both directions. Adding a marker without applying it, or without a runner entry, fails.
- GitHub PR workflows run none of these pytest selections outside Dagger.
- The runner never reports success for a run that collected or passed nothing.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The runner under test: `PATHS`, `BY_NAME`, `write_settings`, `child_environment`, `readiness`, `verify_passed`, `pytest_command`. | `PATHS`; `write_settings`; `verify_passed`; `readiness` | scripts/run-gated-integration.py:76-173; scripts/run-gated-integration.py:203-221; scripts/run-gated-integration.py:282-307; scripts/run-gated-integration.py:310-314 |
| Where the eight markers are registered. | "ar_run_pi_rpc_smoke: opt in with AR_RUN_PI_RPC_SMOKE=1" | pyproject.toml:197-207 |
| The PR-workflow refusal proof scans all workflow YAML for the retired host runner and pytest spellings. | `test_github_pr_checks_do_not_bypass_dagger_for_gated_pytest_paths` | mcp/tests/test_gated_integration_runner.py:137-146 |
| The complementary registry check: markers reconciled against the suite's real `AR_*` environment gates. | `test_registered_markers_and_the_suite_environment_gates_agree` | mcp/tests/test_code_quality_check_scope.py:253-261 |

## R39 Credential And Environment Proofs

The runner tests rename CI-safe/local-only categories to credential-free/vendor-credentials and
prove the two credential-free selectors exactly. They also forbid GitHub workflows from invoking
the gated pytest runner, preserving Dagger as the only test-capable environment.

## Update History

- 2026-08-14T11:27+02:00 — R39 curator: reconciled category semantics and GitHub no-pytest
  ownership. Verification remains closeout-owned.

- 2026-08-14T09:37+02:00 — Reopened L23 Dagger-only PR repair: retired the stale host-pytest
  workflow and added a repository-wide workflow assertion preventing that bypass from returning.

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 4 citation rows: the runner under test (run-gated-integration.py PATHS/write_settings/verify_passed/readiness extents), the pyproject marker registry L194-L204, the CI job L75-L112, and the complementary registry check L741-L749. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  gated-integration inventory and runner-behaviour suite. Verification metadata is pinned
  to the leaf's reformat commit until closeout stamps the code commit.
