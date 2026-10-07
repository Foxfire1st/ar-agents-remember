# mcp/src/agents_remember/application/knowledge_reader/tree_coverage.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

One pathname inventory per side supplies the Knowledge tree and its coverage (MIK-R79 rule 3 and the
OR-R009 design): code is enumerated once with a recursive `ls-tree`, memory once from the selected
working tree (or from the tree's objects), and the immediate children of one directory are composed
from both. The only content read is the selected memory's scope settings, so the tree never opens
source files, cards, hashes or a persistent cache.

## Code Commentary

### Logic

- `read_tree_listing(selection, directory, entries)` is the route's listing entry point. It reads the
  code paths and the memory paths, composes the children with `_children`, adds knowledge presence
  with `_presence`, computes directory coverage with `_coverage`, and names a code or memory
  enumeration failure in the result's `code` state or on each affected directory.
- `_git_paths` runs one recursive `ls-tree -r -t` for the directory (blobs, trees and, for mode
  `100644`/`100755`, the source files), so coverage never asks Git per file.
- `_memory_paths` walks `onboarding/<directory>` of the working tree (directories without dot names)
  or enumerates the tree's objects, then applies the knowledge-format exclusions, so a generated or
  excluded path never appears.
- `_presence` marks a row's `hasKnowledge` (a card/overview of its own, prose at or below it, or an
  indexed entry) and a directory's `hasOverview`; when the memory enumeration failed it omits both
  fields, because an unknown presence is not `false`.
- `_coverage` reads `system/settings.json` of the selected tree and resolves each source path's
  storage rule; per immediate child it counts the in-scope files and the files with a card, and a
  failure to read the scope (or the code pass) yields `{"state": "unavailable", "detail": ...}` on
  every directory instead of a zero.

### Conventions

- Everything is immediate-child and linear; the aggregation reads no source or card content and keeps
  no cache.
- Failure is named: a missing code tree, an unreadable memory path or a scope/settings failure each
  carries its own detail rather than degrading to empty counts.

### Invariants And Boundaries

- **Coverage is truthful or named unavailable** (rule 6): a directory's row says how many of its
  in-scope files have a card, and a scope, path or settings failure is reported as unavailable, never
  as `0`.
- **An unknown presence is not false:** `hasKnowledge`/`hasOverview` are omitted when the memory
  enumeration failed.
- **No contents, hashes, per-file Git or persistent cache:** one code pass and one memory
  enumeration feed every row; this module reads only the selected scope settings besides names.
- **Excluded and generated paths stay out** through the knowledge-format exclusions.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rules 3 and 6) with ruling OR-R009; it lives outside the code and
memory repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The one listing entry point and its truthful failure states. [1]
- One recursive code pass supplies names, kinds and source files. [2]
- One memory enumeration, with excluded paths dropped. [3]
- Presence fields are omitted when the memory enumeration failed. [4]
- Directory coverage counts cards against in-scope files or says unavailable. [5]
- The route entry that delegates its listing here. [6]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
