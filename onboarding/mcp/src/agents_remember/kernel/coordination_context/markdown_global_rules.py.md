# mcp/src/agents_remember/kernel/coordination_context/markdown_global_rules.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/markdown_global_rules.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`markdown_global_rules.py` owns global Markdown path-rule line handling for the
fallback settings parser.

## Code Commentary

### Logic

The module handles the legacy top-level `onboarding.pathRules.include/exclude`
shape, selecting paths or fileTypes lists and appending the final global
storage rule to the parser's settings object.

### Invariants And Boundaries

- The module only operates on the parser state passed by `markdown_settings.py`.
- JSON path-rule parsing remains in `json_settings.py`.
- Global Markdown path rules are appended only when the parser observed a
  global include/exclude section.

## Docs References

No external documentation is needed for this local fallback parser helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Markdown parser delegates global path-rule branches to this module. | Markdown parser | [markdown_settings.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py) |
| Storage evaluation consumes parsed include/exclude paths and file types. | storage policy | [storage.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/storage.py) |

## Cross-Repo References

No cross-repository evidence is needed for local path-rule parsing.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-25T20:57+02:00: Created by extracting global Markdown path-rule parsing from `markdown_settings.py`.
