# mcp/src/agents_remember/kernel/coordination_context/markdown_cross_repo.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/markdown_cross_repo.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`markdown_cross_repo.py` owns legacy Markdown `crossRepo.allow` parsing for the
fallback settings parser.

## Code Commentary

### Logic

The module recognizes inline and list-style string allow entries in fenced
Markdown settings and appends them as excluded `CrossRepoAllowEntry` values
with the v2 migration reason. The main Markdown parser delegates only this
legacy cross-repo branch here.

### Invariants And Boundaries

- Legacy string allow entries are never treated as branch-safe inclusions.
- This module parses fallback Markdown only; strict object parsing for JSON
  settings lives in `setting_values.py`.

## Docs References

No external documentation is needed for this local fallback parser helper.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Markdown parser delegates legacy cross-repo lines to this module. | Markdown parser | [markdown_settings.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py) |
| Runtime cross-repo resolution consumes parsed entries after settings selection. | cross-repo resolver | [cross_repo.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/cross_repo.py) |

## Cross-Repo References

No static cross-repository evidence is needed for legacy fallback parsing.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-25T20:57+02:00: Created by extracting legacy Markdown cross-repo parsing from `markdown_settings.py`.
