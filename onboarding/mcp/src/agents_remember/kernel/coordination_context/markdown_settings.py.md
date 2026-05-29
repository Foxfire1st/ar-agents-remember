# mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
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

## Docs References

No external documentation is needed for this project fallback parser.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Settings selection calls this parser only after confirming JSON settings are absent. | settings selector | [settings.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/settings.py) |
| Legacy cross-repo and global path-rule branches are delegated to focused modules. | parser helpers | [markdown_cross_repo.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/markdown_cross_repo.py); [markdown_global_rules.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/markdown_global_rules.py) |
| Worktree support tests cover legacy Markdown and cross-repo settings behavior. | resolver tests | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No cross-repository evidence is needed for this fallback parser.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-29T18:35+02:00: Added `None` guards for `current_list`/`current_rule` (`global_target_list`, `try_apply_storage_rule_value`, `try_select_storage_rule_list`) to clear Pyright optional errors; behavior-preserving (commit `0549b28`).
- 2026-05-25T20:57+02:00: Created by extracting and simplifying the Markdown settings state machine from the C-08 resolver, then amended after legacy branches moved into focused parser helpers.
