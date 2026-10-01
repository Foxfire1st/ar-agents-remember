# mcp/src/agents_remember/providers/lifecycle/provider_settings.py

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`provider_settings.py` owns lifecycle-time reads of context provider settings
from an EXPLICIT settings file (the lifecycle CLI's `--from-settings`, normally
server-generated from the authority config).

## Code Commentary

### Logic

The module loads CGC and GrepAI provider settings, checks whether a configured
provider is enabled, and exposes context-provider enabled predicates used by
watcher orchestration. Every file reader goes through
`require_lifecycle_settings_path` (260703-L13, GQ3): a `None` settings path
raises `ContextProviderError` naming `--from-settings` — the historic implicit
fallback to `<coordination_root>/system/settings.json` was DELETED (that file is
the global agentic settings home now, and `read_json`'s empty-dict default made
the old fallback fail-open when the file was absent). The readers therefore no
longer take a `coordination_root` parameter.

### Invariants And Boundaries

- Settings lookup is intentionally small and provider-id based.
- Provider-specific validation remains in each provider's lifecycle core.
- Missing CGC settings are an error for CGC lifecycle commands; missing GrepAI
  settings resolve to an empty provider dict for manual/default layout paths.
- A missing settings PATH is always an error: coordinator
  `system/settings.json` is not an authority source (the same posture as
  provider setup's `require_settings_path`).

## Evidence

### Repo-Internal References

- CGC lifecycle core consumes CGC settings from this module. [1]
- GrepAI lifecycle core consumes GrepAI settings from this module. [2]
- Watcher orchestration uses provider-enabled checks from this module. [3]
