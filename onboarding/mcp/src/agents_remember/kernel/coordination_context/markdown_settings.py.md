# mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`markdown_settings.py` parses fenced Markdown settings blocks when a sibling
`settings.json` is absent.

## Code Commentary

### Logic

The parser is a small state machine for legacy fenced YAML-like settings. It
recognizes onboarding storage settings and nested path-rule include/exclude
sections, while delegating legacy string-style `crossRepo.allow` entries and
global path-rule branches to focused helper modules.

### Invariants And Boundaries

- Markdown settings are a fallback format, not the preferred machine-readable
  authority when `settings.json` exists.
- The parser only converts text into settings models; it does not resolve
  repositories or storage decisions.
- Legacy cross-repo strings remain invalid for v2 and are surfaced as excluded.
- Legacy cross-repo and global path-rule helper modules keep this state machine
  below the repository maintainability threshold.
- Empty `mode:`/`layout:`/`default:` scalars fall back to the settings model's own
  value (`_try_apply_storage_mode` keeps `self.settings.mode`,
  `_try_apply_storage_default` keeps `self.settings.default`), not to a hardcoded
  `"external"`; `mode:` and `layout:` share one branch and are treated as aliases,
  and `mode:` also writes `default` from `mode`. That fallback value is now the
  module-level `DEFAULT_STORAGE_MODE` (`"memory-repo"`) declared in
  `kernel/coordination_context/models.py`: with `internal` removed,
  `default_storage_mode(topology)` no longer exists and no storage default is
  topology-derived. `repo-sidecar` survives as a declarable per-path placement
  (`is_sidecar_storage`), not as a memory topology.

## Evidence

### Docs References

No external documentation is needed for this project fallback parser.

No relevant external documentation is needed.

### Repo-Internal References

- `parse_coordination_settings` selects JSON settings when present, parses Markdown settings blocks otherwise, and returns the `StorageSettings` defaults — `DEFAULT_STORAGE_MODE` = `"memory-repo"` — when no settings file exists. It takes no `topology` parameter any more. [1]
- The topology-derived storage default is gone; `StorageSettings.mode`/`.default` are the one non-topology default. [2]

### Cross-Repo References

No cross-repository evidence is needed for this fallback parser.

No meaningful cross-repo references found.
