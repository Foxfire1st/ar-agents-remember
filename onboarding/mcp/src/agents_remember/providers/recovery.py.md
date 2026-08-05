# mcp/src/agents_remember/providers/recovery.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/recovery.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-04T22:15+02:00                     |
| lastVerifiedCommitHash |                                            `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |                                            2026-08-05T12:41:24+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`providers/recovery.py` centralizes provider recovery strings that need to be
identical across status projection and runtime-install recovery reporting.

## Code Commentary

### Logic

The module currently exposes `PROVIDER_WATCHER_RESTART_RECOVERY`, the
operator-facing instruction to run `provider_watchers(action='restart')` when a
watcher must rebind to current runner roots without invalidating provider
indexes. Both provider status and runtime install use this text when reporting a
non-destructive recovery action.

### Conventions

- Keep recovery text concrete and operator-actionable.
- Keep destructive index rebuild guidance separate from restart/rebind guidance.

### Invariants And Boundaries

- Restart/rebind guidance must preserve indexes and must not suggest
  `invalidate-indexes`.
- This module holds shared wording only; status classification and watcher
  lifecycle execution live in their respective modules.

### Todos

None.

## Docs References

No external documentation is configured for this repository slice.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking configured sources. | n/a | n/a |

## Repo-Internal References

The shared recovery text is consumed by both provider status and runtime-install
watcher rebind reporting.

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared recovery constant names `provider_watchers(action='restart')`, current runner roots, preserved indexes, and follow-up status/diagnostics checks. | `PROVIDER_WATCHER_RESTART_RECOVERY` | mcp/src/agents_remember/providers/recovery.py:3-7 |
| Runtime-install watcher recovery actions use the shared restart/rebind text when provider watchers remain degraded. | `add_provider_watcher_recovery_actions`, `complete_provider_watcher_rebind` | mcp/src/agents_remember/install/provider_watchers.py:111-125; mcp/src/agents_remember/install/provider_watchers.py:144-166 |
| Provider status adds the same shared recovery text for GrepAI `noWorkspace`. | `noWorkspace` | mcp/src/agents_remember/providers/status.py:273-273 |

## Cross-Repo References

No sibling repository evidence is needed for this shared message module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-03T02:32:19+02:00 — Curator W3-B02 anchored 2 Repo-Internal citation rows with 3 exact identifiers and generated source ranges; verification metadata was preserved.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations into
  `install/provider_watchers.py` that moved when the helper was re-signed onto `ProviderWatcherRebind`
  and the file shrank to 166 lines. `add_provider_watcher_recovery_actions` (which emits the shared
  `PROVIDER_WATCHER_RESTART_RECOVERY` text) is now L111-L125 (was L110-L124), and the degraded
  restart/rebind branch that ends in that call is now L152-L166 (was L180-L214, past end of file).
- 2026-06-04T22:15+02:00 — Created for shared provider watcher restart/rebind recovery guidance.
