# mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00|
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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
- Empty `mode:`/`layout:`/`default:` scalars fall back to the topology-derived
  default from `__post_init__` (`default_storage_mode(self.topology)`), not a
  hardcoded `"external"`; `mode:` and `layout:` share one branch and are treated
  as aliases.

## Docs References

No external documentation is needed for this project fallback parser.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `parse_coordination_settings` selects JSON settings when present, parses Markdown settings blocks otherwise, and returns topology defaults when no settings file exists. | `parse_coordination_settings` | mcp/src/agents_remember/kernel/coordination_context/settings.py:50-72 |

## Cross-Repo References

No cross-repository evidence is needed for this fallback parser.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T14:17+02:00 — 260731-EFA-L6 S18-B13 curator: closed D9 complete settings-selection construct evidence for the same-reviewer residual delta.

- 2026-05-31T12:50+02:00 — `try_apply_storage_mode` consolidated the separate `mode:`/`layout:` branches into one alias branch and `try_apply_storage_default` now falls back to `self.settings.default` instead of a hardcoded `"external"`, so empty storage scalars keep the topology-derived default; recorded the new empty-scalar fallback boundary in Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Added `None` guards for `current_list`/`current_rule` (`global_target_list`, `try_apply_storage_rule_value`, `try_select_storage_rule_list`) to clear Pyright optional errors; behavior-preserving (commit `0549b28`).
- 2026-05-25T20:57+02:00: Created by extracting and simplifying the Markdown settings state machine from the `c-08-ar-coordination-context-resolver` skill resolver, then amended after legacy branches moved into focused parser helpers.
