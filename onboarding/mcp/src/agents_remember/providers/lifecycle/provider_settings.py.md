# mcp/src/agents_remember/providers/lifecycle/provider_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/provider_settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| CGC lifecycle core consumes CGC settings from this module. | `cgc_apply_settings` | mcp/src/agents_remember/providers/cgc/lifecycle/core.py:298-319 |
| GrepAI lifecycle core consumes GrepAI settings from this module. | `grepai_runtime_settings` | mcp/src/agents_remember/providers/grepai/lifecycle/core.py:137-139 |
| Watcher orchestration uses provider-enabled checks from this module. | `watcher_enabled_providers` | mcp/src/agents_remember/providers/lifecycle/watchers.py:88-97 |

## Update History

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 3 citation claims; scoped recheck clean (0 findings).

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/providers/lifecycle/provider_settings.py` since the L2 base commit is
  the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-06T22:30+02:00 — 260703-L13 (GQ3): deleted the implicit coordinator
  `system/settings.json` fallback — `require_lifecycle_settings_path` refuses a missing
  `--from-settings` with a `ContextProviderError`; the `coordination_root` parameter dropped
  from all three readers; explicit settings paths keep working unchanged. Verification
  metadata pinned until closeout stamps the L13 commit.

- 2026-05-29T18:35+02:00: `context_providers_enabled` is now a `TypeGuard[dict[str, Any]]` so `provider_enabled` narrows `context` before `.get`; behavior-preserving (commit `0549b28`).
- 2026-05-25T21:14+02:00: Created from the provider settings portion of the former shared lifecycle common module.
