# mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00|
| lastVerifiedCommitHash | `b281bcd68261866be306cc80a48241921b6dd0d2` |
| lastVerifiedCommitDate | 2026-09-16T14:24:58+02:00|
| governingOverview      | `overview.md`                              |

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

## Docs References

No external documentation is needed for this project fallback parser.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `parse_coordination_settings` selects JSON settings when present, parses Markdown settings blocks otherwise, and returns the `StorageSettings` defaults — `DEFAULT_STORAGE_MODE` = `"memory-repo"` — when no settings file exists. It takes no `topology` parameter any more. | `parse_coordination_settings` | mcp/src/agents_remember/kernel/coordination_context/settings.py:48-68 |
| The topology-derived storage default is gone; `StorageSettings.mode`/`.default` are the one non-topology default. | `DEFAULT_STORAGE_MODE` | mcp/src/agents_remember/kernel/coordination_context/models.py:40-40 |

## Cross-Repo References

No cross-repository evidence is needed for this fallback parser.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T14:05+02:00 — 260915-CAPS-L12 curator: **deleted-symbol claim re-anchored** for the removal of `internal` memory mode (`CAPS-R12@v1`). The Invariants entry claimed empty storage scalars fall back to a *topology-derived* default from `__post_init__` via `default_storage_mode(self.topology)` — that function no longer exists anywhere in the package, `topology` no longer appears in this module, and the fallback is now the model's own `DEFAULT_STORAGE_MODE` (`"memory-repo"`). The entry was re-worded to the current mechanism (the private `_try_apply_storage_mode` / `_try_apply_storage_default` keep `self.settings.mode` / `.default`) and now records that `repo-sidecar` survives only as a per-path placement. The Repo-Internal row for `parse_coordination_settings` was also corrected: it no longer takes a `topology` parameter and returns `StorageSettings` defaults rather than topology defaults, and its range moved to `settings.py:48-68`. Verification metadata remains closeout-owned: the source is uncommitted, so no stamp was advanced and no commit hash was invented.

- 2026-08-04T14:17+02:00 — 260731-EFA-L6 S18-B13 curator: closed D9 complete settings-selection construct evidence for the same-reviewer residual delta.

- 2026-05-31T12:50+02:00 — `try_apply_storage_mode` consolidated the separate `mode:`/`layout:` branches into one alias branch and `try_apply_storage_default` now falls back to `self.settings.default` instead of a hardcoded `"external"`, so empty storage scalars keep the topology-derived default; recorded the new empty-scalar fallback boundary in Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Added `None` guards for `current_list`/`current_rule` (`global_target_list`, `try_apply_storage_rule_value`, `try_select_storage_rule_list`) to clear Pyright optional errors; behavior-preserving (commit `0549b28`).
- 2026-05-25T20:57+02:00: Created by extracting and simplifying the Markdown settings state machine from the `c-08-ar-coordination-context-resolver` skill resolver, then amended after legacy branches moved into focused parser helpers.
