# mcp/src/agents_remember/kernel/coordination_context/markdown_cross_repo.py

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

## Evidence

### Docs References

No external documentation is needed for this local fallback parser helper.

No relevant external documentation is needed.

### Repo-Internal References

- The Markdown parser delegates legacy cross-repo lines to this module through `handle_cross_repo_line`. [1]
- Runtime cross-repo resolution consumes parsed entries through `resolve_cross_repo_entry` after settings selection. [2]

### Cross-Repo References

No static cross-repository evidence is needed for legacy fallback parsing.

No meaningful cross-repo references found.
