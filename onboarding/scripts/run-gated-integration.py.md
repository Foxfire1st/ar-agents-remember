# scripts/run-gated-integration.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/run-gated-integration.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T16:10+02:00                     |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

One command per environment-gated integration path, plus the readiness table for all of
them. It exists because `pyproject.toml` registers eight `AR_*` markers for suites that skip
unless a variable opts them in, and **before this script, nothing could select them as
intentional integration paths** — fifteen tests over
the Pi RPC transport, the Codex app-server, the Claude stream-json transport, the L3 control
routes, the production evidence seam and the real MCP stdio server were never executed by
anything. Running them for the first time exposed two real bugs.

```text
python scripts/run-gated-integration.py                       # 'list' is the default
python scripts/run-gated-integration.py credential-free       # both credential-free paths
python scripts/run-gated-integration.py ar-run-pi-rpc-smoke --require-passed 3
python scripts/run-gated-integration.py agents-remember-real-mcp-config --dry-run-only
```

## Code Commentary

### The Declaration Table

`PATHS` is a tuple of frozen `GatedPath` records — `name`, `marker`, the `environment`
variables that opt the suite in, a `category`, a prose `requires`, and the `binaries` whose
presence `readiness()` probes. `BY_NAME` indexes it, and the argparse `choices` are built
from it, so an unknown path name is rejected by the parser rather than handed to pytest.

The category is the whole policy in one field:

| Category | Paths | What it needs |
| --- | --- | --- |
| `CREDENTIAL_FREE` ("no vendor account") | `ar-run-pi-rpc-smoke`, `agents-remember-real-mcp-config` | node + npm and the npm registry; or nothing but a generated settings file |
| `VENDOR_CREDENTIALS` ("vendor credentials required") | `ar-codex-app-server-live-smoke`, `ar-codex-app-server-live-conformance`, `ar-claude-stream-smoke`, `ar-run-control-plane-installed`, `ar-run-control-installed`, `ar-run-evidence-installed` | an installed, signed-in vendor CLI; three additionally pin exactly `codex 0.144.5` and `pi 0.80.7`; **four bill for real model turns**, and `ar-run-evidence-installed` writes a persisted thread into the operator's real `CODEX_HOME` |

`requires` is not decoration — `test_gated_integration_runner.py` asserts every path states
what it requires, and that `CREDENTIAL_FREE` is exactly the two paths that can run without
vendor credentials inside the lifecycle-owned Dagger graph.

### `--require-passed` Is The Anti-Skip Guard

This is the load-bearing behaviour. **A skipped test exits pytest 0**, and several of these
suites skip themselves when a binary is missing from PATH or its version does not match —
which is precisely the state the acceptance selection exists to expose. A runner that only checked the exit
code would report success for a job that ran nothing.

So when `--require-passed N` is given, `invoke` adds `--junit-xml` and `verify_passed`
parses pytest's **own** JUnit report: `passed = tests - skipped - errors - failures`, and the
run fails unless that equals `N` **exactly**. A missing report file and a report with no
`testsuite` element both fail rather than pass. Any Dagger-owned acceptance selection that
depends on an exact count supplies this flag explicitly.

### Generated Fixtures, Never Credentials

`agents-remember-real-mcp-config` is the one path that needs a file rather than an account.
`settings_document` builds it — temp coordination and workspace roots, this repository as
the single repo id, the two self-hosted provider entries (`codegraphcontext-code`,
`grepai-memory`), timeout caps — and it **holds no credential of any kind**, which is why
the planning half of that suite is safe to run in Dagger without credentials. A test asserts
exactly that.

`write_settings` also creates the tree the document names, including
`<coordinationRoot>/memory-repos/ar-<repo id>`, because the provider layer refuses to plan a
search against a path that does not exist. Everything is written under a
`TemporaryDirectory` per run.

`--dry-run-only` narrows that path to the single node named by `DRY_RUN_NODE`
(`test_real_mcp_grepai_search_dry_run_uses_workspace_scope`), which asserts the command the
server *would* run and executes nothing. Its sibling in the same class performs a live
grepai search and needs the self-hosted docker stack up and indexed. A test asserts
`DRY_RUN_NODE` names a test that actually exists.

### Argument Handling

`main` uses `parse_known_args`, not an `argparse.REMAINDER` positional: REMAINDER swallows
every token after the path name, so `... real-mcp-config --dry-run-only` would forward this
script's own flag to pytest and fail there. Unrecognised arguments are collected into
`RunRequest.extra` and appended to the pytest command line verbatim.

`child_environment` copies `os.environ`, applies the path's opt-in variables, prepends
`mcp/src` to `PYTHONPATH`, and sets `AGENTS_REMEMBER_REAL_MCP_CONFIG` when a settings file
was generated. Every run prints the path, its category, its `requires` line and the exact
command before executing, so an operator sees what they are about to spend before it starts.

`list` (the default) prints the same table with `readiness()` resolved on this machine —
"binaries present", "missing on PATH: codex", or "no binary needed" — and runs nothing.

## Invariants And Boundaries

- **Exit code alone is not proof a gated suite ran.** Any automation that must know the
  tests executed passes `--require-passed`; the count comes from the JUnit report, never
  from pytest's summary text.
- The inventory is enforced in the suite, not here and not in GitHub workflows:
  `mcp/tests/test_gated_integration_runner.py` asserts that every marker registered in
  `pyproject.toml` is applied to at least one test **and** has an entry in this script, in
  both directions. Adding a marker without a `GatedPath` fails the gate.
- Nothing in this script authenticates, stores or reads a credential. The only file it
  writes is a settings document containing paths.
- `CREDENTIAL_FREE` is a claim that Dagger can hold everything the path needs without a
  vendor account. It does not grant a GitHub workflow permission to run pytest directly.
- The six `VENDOR_CREDENTIALS` paths are deliberately not faked in automation. Four bill; one persists a
  thread into the operator's real `CODEX_HOME`.
- The script is a runner, not a gate: `python -m agents_remember.code_quality.check` does
  not invoke it.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The eight opt-in integration markers, each naming its opt-in variable and the test file it decorates. | "ar_run_pi_rpc_smoke:"; "ar_run_control_plane_installed:"; "ar_run_control_installed:"; "ar_run_evidence_installed:"; "ar_claude_stream_smoke:"; "ar_codex_app_server_live_smoke:"; "ar_codex_app_server_live_conformance:"; "agents_remember_real_mcp_config:" | pyproject.toml:206-212; pyproject.toml:214-214 |
| GitHub workflows are forbidden from invoking this runner or host pytest; lifecycle acceptance owns these paths through Dagger. | `test_github_pr_checks_do_not_bypass_dagger_for_gated_pytest_paths` | mcp/tests/test_gated_integration_runner.py:139-146 |
| The inventory test: every marker is applied, every marker has a runner entry, `CREDENTIAL_FREE` is exactly the two no-vendor-account paths, and the dry-run node exists. | `GatedPathInventoryTests` | mcp/tests/test_gated_integration_runner.py:86-157 |
| The Pi RPC smoke suite this runner installs and drives offline. | `install_pinned_pi`; `PiRpcRealSmokeTests` | mcp/tests/test_pi_rpc_real_smoke.py:52-83; mcp/tests/test_pi_rpc_real_smoke.py:236-499 |
| The real-MCP class whose planning test the generated settings file serves. | `RealMcpIntegrationTests`; `test_real_mcp_grepai_search_dry_run_uses_workspace_scope` | mcp/tests/test_tools.py:1020-1100 |

## R39 Gated-Path Selection

The runner classifies two paths as credential-free and six as requiring vendor credentials,
without making either class a host/CI execution authority. GitHub workflows no longer invoke this
pytest runner; credential-free paths may run only inside lifecycle-owned Dagger acceptance, and
vendor paths remain explicit provisioned opt-ins under the same test-environment guard.

## Update History

- 2026-08-14T11:25+02:00 — R39 curator: replaced CI/local categories with credential semantics and
  removed GitHub test-runner authority. Verification remains closeout-owned.
- 2026-08-04T14:01:47+02:00 — 260731-EFA-L6 S18-B01 second same-reviewer residual correction: split the eight opt-in markers from the Pi and real-MCP workflow jobs under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-07-31T16:10+02:00 — Created for 260731-EFA-L2 (requirement L2-R8). Records the one
  command per gated path, the `CREDENTIAL_FREE`/`VENDOR_CREDENTIALS` split and what each side needs, the
  `--require-passed` anti-skip guard reading pytest's JUnit report because a skipped test
  exits 0, the credential-free generated settings document, `--dry-run-only`, and the
  in-suite inventory test that keeps the markers and this table in step in both directions.
  Verification metadata is pinned to the leaf's reformat commit until closeout stamps the
  code commit.
