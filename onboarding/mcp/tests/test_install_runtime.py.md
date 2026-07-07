# test_install_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_install_runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T22:50+02:00                     |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063` |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_install_runtime.py` covers MCP package runtime-install behavior that
affects live provider runtime safety from the core-skill test suite, including
the provider watcher rebind path used when provider dependencies are refreshed.
`AgenticSettingsSeedTests` (L13) pins the global agentic settings seeding:
`install_runtime` writes `<coordinationRoot>/system/settings.json` when missing
(content equal to `default_agentic_settings_seed()`), NEVER clobbers an
existing file (byte-for-byte preserved), and dry-run counts the seed without
writing.

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

The provider-deps rebind regressions seed a stale runner file, mock watcher and
provider dependency lifecycle calls, and prove ordering: watchers stop before
runner refresh, provider dependency install runs, then watchers start and status
is checked. A dry-run variant proves the same lifecycle plan is reported without
mutating the runner file. Additional cases prove a degraded post-install status
triggers exactly one non-destructive restart/rebind, still-degraded status
records a recovery action, and provider dependency failure attempts watcher
recovery before raising.

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
- Patch watcher lifecycle calls through `install.provider_watchers` when testing
  rebind sequencing; patch provider dependency install calls through
  `install.runtime`.

### Invariants And Boundaries

The test validates runtime-install file reconciliation and watcher lifecycle
sequencing only. It does not prove real provider install commands, Docker
backends, watcher containers, or runtime search results; those remain
lifecycle/provider integration concerns.

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
| The test creates a synthetic runtime source tree with the MCP installer-required runtime directories and provider defaults, without a runtime `scripts/` tree. | L22-L31 | [test_install_runtime.py](agents-remember/mcp/tests/test_install_runtime.py) |
| The provider-runtime preservation regression proves runtime install preserves CGC and GrepAI runner roots while pruning legacy `_bin` and `_venvs`, removing unrelated stale provider files, and copying provider requirements. | L63-L116 | [test_install_runtime.py](agents-remember/mcp/tests/test_install_runtime.py) |
| The full-install regression preserves provider data and central log roots, creates default provider data/log/runner directories, and does not install the MCP package into the coordinator. | L118-L160 | [test_install_runtime.py](agents-remember/mcp/tests/test_install_runtime.py) |
| The provider-deps rebind regression proves watcher stop happens before runner refresh and watcher start/status happens after provider dependency install. | L162-L232 | [test_install_runtime.py](agents-remember/mcp/tests/test_install_runtime.py) |
| The dry-run rebind regression reports watcher stop/start/status and dependency install while preserving the stale runner file. | L234-L297 | [test_install_runtime.py](agents-remember/mcp/tests/test_install_runtime.py) |
| Degraded and unrecovered status regressions prove one non-destructive restart/rebind attempt and recovery-action reporting. | L299-L403 | [test_install_runtime.py](agents-remember/mcp/tests/test_install_runtime.py) |
| Dependency-install failure still attempts watcher recovery before raising a runtime-install failure. | L405-L454 | [test_install_runtime.py](agents-remember/mcp/tests/test_install_runtime.py) |

## Cross-Repo References

No sibling repository evidence is needed for this installer test.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-06T22:50+02:00 — 260703-L13 (settings unification): added
  `AgenticSettingsSeedTests` — seed-when-missing, never-clobber, dry-run-no-write.
  Verification metadata pinned until closeout stamps the L13 commit.

- 2026-06-04T22:15+02:00: Documented the new provider-deps watcher rebind regression coverage: sequencing, dry-run reporting, degraded-status retry, unrecovered recovery action, and dependency-failure recovery.
- 2026-05-30T21:51+02:00: Documented the new `no_cache` threading coverage in `ProviderDependencyHelperTests` — `no_cache=True` reaches both provider args and defaults to `False`. Verified against `8927f03`.
- 2026-05-29T20:25+02:00: Documented the new `ProviderDependencyHelperTests` and `ReadSkillNameTests` coverage added to clear the install helpers' CRAP threshold (`dry_run`-default flip task).
- 2026-05-28T12:32+02:00: Updated after runtime install moved operator logs from `providers/logs/` into the central `logs/` tree and tests asserted the new directories.
- 2026-05-26T12:51+02:00: Updated after runtime install began pruning provider venvs because providers are Docker-owned.
- 2026-05-25T18:07+02:00: Updated after dependency-skipped runtime install began pruning legacy `providers/_bin` while preserving live venv and runner state.
- 2026-05-23T14:20+02:00: Updated after tests switched from the deleted `installer/install-runtime.py` to MCP package-local `agents_remember.install.runtime` and asserted stale coordinator `scripts/` cleanup.
- 2026-05-23T05:32+02:00: Updated after source-installer tests stopped using provider-dependency install switches and asserted provider dependency/runtime roots are preserved.
- 2026-05-23T04:29+02:00: Updated after installer tests moved provider instances under `providers/runners` and asserted default data/log/runner folders.
- 2026-05-21T23:55+02:00: Created after adding the dependency-skipped provider-runtime preservation regression test.
