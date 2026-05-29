# mcp/src/agents_remember/providers/lifecycle/provider_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/provider_settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`provider_settings.py` owns lifecycle-time reads of context provider settings
from coordinator `settings.json` files.

## Code Commentary

### Logic

The module loads CGC and GrepAI provider settings, checks whether a configured
provider is enabled, and exposes context-provider enabled predicates used by
watcher orchestration.

### Invariants And Boundaries

- Settings lookup is intentionally small and provider-id based.
- Provider-specific validation remains in each provider's lifecycle core.
- Missing CGC settings are an error for CGC lifecycle commands; missing GrepAI
  settings resolve to an empty provider dict for manual/default layout paths.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC lifecycle core consumes CGC settings from this module. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/core.py) |
| GrepAI lifecycle core consumes GrepAI settings from this module. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/core.py) |
| Watcher orchestration uses provider-enabled checks from this module. | [watchers.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/watchers.py) |

## Update History

- 2026-05-29T18:35+02:00: `context_providers_enabled` is now a `TypeGuard[dict[str, Any]]` so `provider_enabled` narrows `context` before `.get`; behavior-preserving (commit `0549b28`).
- 2026-05-25T21:14+02:00: Created from the provider settings portion of the former shared lifecycle common module.
