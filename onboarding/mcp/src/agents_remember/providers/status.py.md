# mcp/src/agents_remember/providers/status.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/status.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T22:37+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`status.py` composes read-only provider and watcher status packets for
`context_packet` and MCP provider diagnostics.

## Code Commentary

### Logic

`provider_status_packet()` handles skipped/no-provider cases, checks provider
runner integrity before invoking watcher status, returns a structured integrity
failure packet when runner files are unrecorded or changed, writes temporary
provider lifecycle settings for watcher status, and maps raw lifecycle results
into per-provider items.

### Conventions

Provider status is read-only from the MCP caller's perspective. Temporary
lifecycle settings are generated from MCP settings and deleted after watcher
status is read.

### Invariants And Boundaries

- Runner integrity failure must short-circuit watcher probing.
- Coordinator files do not provide authority for provider status.
- Watcher state labels are derived from provider-specific raw status shapes.

### Todos

- `_watcher_state()` is a Phase 06 complexity candidate if provider status grows.

## Docs References

No external documentation is needed for this local status composition.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for the file's local provider status behavior. | n/a | n/a |

## Repo-Internal References

Same-repository source and tests define the provider status contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `provider_status_packet()` returns skipped/no-provider packets, blocks on runner integrity failures, and otherwise includes watcher status, integrity, process namespace, items, and recovery actions. | L14-L76 | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Watcher status uses generated lifecycle settings and cleans the temporary settings file afterward. | L79-L91 | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Provider item and watcher-state helpers convert raw lifecycle results into configured provider diagnostics. | L94-L166 | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Integrity tests assert that unrecorded runner files cause `runnerIntegrityFailed` and a `runtime_install` recovery action. | L49-L64 | [test_integrity.py](agents-remember-md/mcp/tests/test_integrity.py) |

## Cross-Repo References

No meaningful cross-repo boundary is documented here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No sibling repository boundary is needed to explain this file. | n/a | n/a |

## Update History

- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
