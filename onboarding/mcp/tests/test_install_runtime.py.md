# test_install_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_install_runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-30T21:51+02:00                     |
| lastVerifiedCommitHash | `8927f038535bdb514526156df72603708bc89e19` |
| lastVerifiedCommitDate | 2026-05-30T19:59:15+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_install_runtime.py` covers MCP package runtime-install behavior that
affects live provider runtime safety from the core-skill test suite.

## Code Commentary

### Logic

The test imports `agents_remember.install.runtime` from the MCP package source,
creates a minimal synthetic runtime source tree, and installs it into a
temporary coordination root. Its regression case seeds stale host provider
artifacts under `providers/_venvs/`, live Docker provider runner state under
`providers/runners/codegraphcontext/` and `providers/runners/grepai/`, plus a
stale legacy `providers/_bin/grepai.exe`, then calls
`install_runtime(..., install_provider_deps=False)`. The assertions prove the
MCP runtime installer keeps live runner artifacts, prunes stale `_bin` and
`_venvs` host artifacts, removes unrelated stale provider files, copies current
provider defaults, removes stale coordinator `scripts/` remnants, and does not
run provider dependency commands.
The second regression proves `providers/data`, central `logs/mcp`, central
`logs/providers`, and default runner folders exist after install while stale
venvs are pruned.

`ProviderDependencyHelperTests` adds hermetic coverage for the provider-dependency
helpers — `any_provider_enabled`, `configured_provider_enabled`, and
`install_provider_dependencies_from_settings` (the none-configured skip, the
run-enabled path with mocked `lifecycle.grepai_install`/`cgc_install_all`, and the
failure-raises path, all with `dry_run=True`). It also covers `no_cache`
threading: `install_provider_dependencies_from_settings` forwards `no_cache=True`
into both the GrepAI and CGC provider args, and defaults `no_cache` to `False`
when unset. `ReadSkillNameTests` covers
`install.skills._read_skill_name` frontmatter parsing (name present, frontmatter
without a name, and no frontmatter). These drive coverage on the previously
untested install helpers so they clear the CRAP threshold.

### Conventions

- Keep installer tests synthetic and file-local; do not require Docker, GrepAI,
  CGC, network access, or a real `ar-coordination` root.
- Import the package-local MCP runtime installer from `mcp/src`; do not import
  deleted source-checkout installer scripts.
- Use the public `install_runtime()` function directly rather than invoking the
  MCP server transport.

### Invariants And Boundaries

The test validates runtime-install file reconciliation only. It does not prove provider
install commands, provider watcher readiness, Docker backends, or runtime search
results; those remain lifecycle/provider integration concerns.

### Todos

None.

## Docs References

No external documentation is needed for this test.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The test creates a synthetic runtime source tree with the MCP installer-required runtime directories and provider defaults, without a runtime `scripts/` tree. | L22-L31 | [test_install_runtime.py](agents-remember-md/mcp/tests/test_install_runtime.py) |
| The provider-runtime preservation regression proves runtime install preserves CGC and GrepAI runner roots while pruning legacy `_bin` and `_venvs`, removing unrelated stale provider files, and copying provider requirements. | L34-L68 | [test_install_runtime.py](agents-remember-md/mcp/tests/test_install_runtime.py) |
| The full-install regression preserves provider data and central log roots, creates default provider data/log/runner directories, and does not install the MCP package into the coordinator. | L96-L140 | [test_install_runtime.py](agents-remember-md/mcp/tests/test_install_runtime.py) |

## Cross-Repo References

No sibling repository evidence is needed for this installer test.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-30T21:51+02:00: Documented the new `no_cache` threading coverage in `ProviderDependencyHelperTests` — `no_cache=True` reaches both provider args and defaults to `False`. Verified against `8927f03`.
- 2026-05-29T20:25+02:00: Documented the new `ProviderDependencyHelperTests` and `ReadSkillNameTests` coverage added to clear the install helpers' CRAP threshold (`dry_run`-default flip task).
- 2026-05-28T12:32+02:00: Updated after runtime install moved operator logs from `providers/logs/` into the central `logs/` tree and tests asserted the new directories.
- 2026-05-26T12:51+02:00: Updated after runtime install began pruning provider venvs because providers are Docker-owned.
- 2026-05-25T18:07+02:00: Updated after dependency-skipped runtime install began pruning legacy `providers/_bin` while preserving live venv and runner state.
- 2026-05-23T14:20+02:00: Updated after tests switched from the deleted `installer/install-runtime.py` to MCP package-local `agents_remember.install.runtime` and asserted stale coordinator `scripts/` cleanup.
- 2026-05-23T05:32+02:00: Updated after source-installer tests stopped using provider-dependency install switches and asserted provider dependency/runtime roots are preserved.
- 2026-05-23T04:29+02:00: Updated after installer tests moved provider instances under `providers/runners` and asserted default data/log/runner folders.
- 2026-05-21T23:55+02:00: Created after adding the dependency-skipped provider-runtime preservation regression test.
