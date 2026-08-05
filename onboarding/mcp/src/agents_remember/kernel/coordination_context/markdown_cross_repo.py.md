# mcp/src/agents_remember/kernel/coordination_context/markdown_cross_repo.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/markdown_cross_repo.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The Markdown parser delegates legacy cross-repo lines to this module through `handle_cross_repo_line`. | `handle_cross_repo_line` | mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py:101-101 |
| Runtime cross-repo resolution consumes parsed entries through `resolve_cross_repo_entry` after settings selection. | `resolve_cross_repo_entry` | mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:52-73 |

## Cross-Repo References

No static cross-repository evidence is needed for legacy fallback parsing.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 2 table citations for cross-repository markdown handling and entry resolution; fixer-generated ranges verified.

- 2026-05-25T20:57+02:00: Created by extracting legacy Markdown cross-repo parsing from `markdown_settings.py`.
