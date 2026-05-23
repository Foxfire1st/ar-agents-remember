# test_install_runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_install_runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T14:20+02:00                     |
| lastVerifiedCommitHash | `a6890ae469b70ef045a127fc774d6aa51a54e65a` |
| lastVerifiedCommitDate | 2026-05-23T18:31:48+02:00|
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
temporary coordination root. Its regression case seeds live provider dependency artifacts
under `providers/_bin/`, `providers/_venvs/`, `providers/runners/codegraphcontext/`,
and `providers/runners/grepai/`, then calls
`install_runtime(..., install_provider_deps=False)`. The assertions prove the
MCP runtime installer keeps those live provider runtime artifacts, removes
unrelated stale provider files, copies current provider defaults, removes stale
coordinator `scripts/` remnants, and does not run provider dependency commands.
The second regression proves `providers/data`, `providers/logs`, and default
runner folders exist after install while stale venvs are preserved for
MCP-owned provider lifecycle operations.

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
| The provider-runtime preservation regression proves runtime install preserves provider binaries, venvs, CGC runner roots, and GrepAI runner roots while removing unrelated stale provider files and copying provider requirements. | L34-L68 | [test_install_runtime.py](agents-remember-md/mcp/tests/test_install_runtime.py) |
| The full-install regression preserves provider data/log/dependency roots, creates default provider data/log/runner directories, and does not install the MCP package into the coordinator. | L77-L116 | [test_install_runtime.py](agents-remember-md/mcp/tests/test_install_runtime.py) |

## Cross-Repo References

No sibling repository evidence is needed for this installer test.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-23T14:20+02:00: Updated after tests switched from the deleted `installer/install-runtime.py` to MCP package-local `agents_remember.install.runtime` and asserted stale coordinator `scripts/` cleanup.
- 2026-05-23T05:32+02:00: Updated after source-installer tests stopped using provider-dependency install switches and asserted provider dependency/runtime roots are preserved.
- 2026-05-23T04:29+02:00: Updated after installer tests moved provider instances under `providers/runners` and asserted default data/log/runner folders.
- 2026-05-21T23:55+02:00: Created after adding the dependency-skipped provider-runtime preservation regression test.
