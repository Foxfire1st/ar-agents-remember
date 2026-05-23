# mcp/src/agents_remember/providers/integrity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/integrity.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T00:37+02:00                     |
| lastVerifiedCommitHash | `ddf6fcd5981664813c915e94e1c5229b542a28a4` |
| lastVerifiedCommitDate | 2026-05-24T00:25:39+02:00                 |
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`integrity.py` records and checks hashes for provider runner executable files so
MCP status calls can report changed provider runtimes before trusting watcher
status.

## Code Commentary

### Logic

The manifest path is derived from the trusted MCP settings file path, not from
the coordinator provider tree. `write_provider_runner_manifest()` hashes files
under `<coordinationRoot>/providers/_bin` and
`<coordinationRoot>/providers/_venvs`, writes a sorted JSON manifest beside the
MCP settings file, and returns a small status payload. `check_provider_runner_integrity()`
compares current hashes with the recorded manifest and reports `notInstalled`,
`manifestMissing`, `manifestUnreadable`, `manifestInvalid`, `checked`, or
`changed`.

### Invariants And Boundaries

- Hash executable/runtime-managed install roots, not mutable provider data,
  logs, or runner state.
- Store the manifest beside trusted MCP settings so a coordinator-local edit
  cannot trivially update both executable files and the manifest.
- Missing manifest plus existing runner files is a failure state; missing
  manifest with no runner files is `notInstalled`.
- Ignore Python bytecode/cache files.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider status short-circuits to `runnerIntegrityFailed` when integrity checks fail. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Runtime install writes a manifest after non-dry-run installs. | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |
| Integrity tests cover missing, clean, changed, and status short-circuit behavior. | [test_integrity.py](agents-remember-md/mcp/tests/test_integrity.py) |

## Update History

- 2026-05-24T00:37+02:00: Refreshed verification after MCP service-controller changes; provider runner integrity behavior stayed unchanged.
- 2026-05-23T04:29+02:00: Created for Phase 3 provider runner integrity checks.
