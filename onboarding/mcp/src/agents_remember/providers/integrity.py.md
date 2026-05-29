# mcp/src/agents_remember/providers/integrity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/integrity.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`integrity.py` records and checks hashes for provider runner files so MCP status
calls can report changed provider runtimes before trusting watcher status.
`providers/_bin` and `providers/_venvs` are no longer managed runner authority
paths for Docker-owned providers, so current checks have no watched filesystem
runner roots and ignore old `_bin` entries that may remain in historic
manifests.

## Code Commentary

### Logic

The manifest path is derived from the trusted MCP settings file path, not from
the coordinator provider tree. `write_provider_runner_manifest()` hashes the
configured watched provider file roots, writes a sorted JSON manifest beside
the MCP settings file, and returns a small status payload. With the current
Docker-owned provider model the watched set is empty.
`check_provider_runner_integrity()` compares current hashes with the recorded
manifest and reports `notInstalled`, `manifestMissing`, `manifestUnreadable`,
`manifestInvalid`, `checked`, or `changed`.

Manifest comparison filters recorded paths under `providers/_bin` before
checking changed or missing files. That keeps old manifests from blocking the
Docker-owned providers after the host-binary contract was removed.

### Invariants And Boundaries

- Hash executable/runtime-managed install roots, not mutable provider data,
  logs, or runner state.
- Store the manifest beside trusted MCP settings so a coordinator-local edit
  cannot trivially update both executable files and the manifest.
- Missing manifest plus watched runner files is a failure state; missing
  manifest with no watched runner files is `notInstalled`.
- `providers/_bin` entries are ignored if they exist in older recorded
  manifests; current manifests no longer hash `_bin`.
- Current manifests do not hash host venv files because CGC and GrepAI provider
  execution is Docker-owned.
- Ignore Python bytecode/cache files.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider status short-circuits to `runnerIntegrityFailed` when integrity checks fail. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Runtime install writes a manifest after non-dry-run installs. | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |
| Integrity tests cover missing, clean, changed, and status short-circuit behavior. | [test_integrity.py](agents-remember-md/mcp/tests/test_integrity.py) |
| MCP tool tests assert that legacy CodeGraphContext venvs and legacy `_bin` entries do not block Docker-mode providers. | [test_tools.py](agents-remember-md/mcp/tests/test_tools.py) |

## Update History

- 2026-05-29T18:35+02:00: Extracted `_recorded_manifest_or_early` (manifest load/validate boundary) from `check_provider_runner_integrity` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-26T12:51+02:00: Updated after CodeGraphContext moved to Docker-owned provider execution and host venv files stopped being runner integrity authority.
- 2026-05-25T18:07+02:00: Updated after `providers/_bin` was removed from the current runner integrity authority and old `_bin` manifest entries became ignored compatibility data.
- 2026-05-25T17:40+02:00: Updated after Docker-mode GrepAI host binaries and old manifest entries for those binaries were removed from provider runner integrity authority.
- 2026-05-24T00:37+02:00: Refreshed verification after MCP service-controller changes; provider runner integrity behavior stayed unchanged.
- 2026-05-23T04:29+02:00: Created for Phase 3 provider runner integrity checks.
