# mcp/src/agents_remember/application/knowledge_reader/paths.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The explorer, the path view and the without-proof list of the knowledge reader (MIK-R29 rules 1 and
2).** Pick a path and see everything linked to it, the way overview and onboarding files work:

- **The explorer** (`tree_listing`) lists one directory level: the code tree's children joined with the
  onboarding mirror's, each with the number of live knowledge entries at or under it, and (since MIK-R79)
  with the knowledge-presence marks and the directory coverage the shared function supplies. A path with
  onboarding but no code (a card whose file is gone) is listed with `inCode: false`.
- **The path view** (`path_view`) of a file or directory: its onboarding Markdown with the sidecar's numbered
  references resolved; its realization and proof entries grouped by invariant, each with its MIK-R03 state;
  the families of those invariants and those routed over the path, each with its other locations; every
  record linking to the path or to those invariants, a decision shown whole; and for a test file, its proofs
  with their facets (`testFile`).
- **The without-proof list** (`without_proof`) is MIK-R28 rule 5's list, filtered to the invariants realized
  at or under a path when one is given.

## Code Commentary

### Logic

- **A directory's listing is one delegated call (MIK-R79).** `tree_listing` normalizes the path and hands the
  selection, the directory and the index's entry counts to
  [`tree_coverage.read_tree_listing`](tree_coverage.py.md), which owns the one code pass, the one memory
  enumeration, the presence marks and the counted-or-unavailable coverage. The route's own answer shape is
  unchanged (`directory`, `code`, `children`), with the optional `hasKnowledge`, `hasOverview` and `coverage`
  fields on a child.
- **A directory's view is bounded (ruling 2026-09-30T09:42:58, F2).** `path_view` reads a file's entries with
  `entries_at_path` and a directory's with `entries_in_directory` (the files directly in it only), and adds
  `_directory_summary`: each immediate child holding knowledge with its live entry count, and
  `subtree: {entries, view: "subtree"}`. The full recursive list is the `subtree` view (`subtree.py`), paged
  through the shared continuation. At the root the remaining size is the root onboarding prose itself.
- **Live only.** `_live_entries` drops entries whose invariant is retired or missing, and `_entry_counts`
  counts through `live_entry_paths_under`, so the explorer, the summary and the subtree agree.
- **Families.** `_families` takes each invariant's families (live only), then the families routed over the
  path: for a file, MIK-R05's `select_chain` (with the route each came `via`); for a directory,
  `families_governing` of the directory itself. `_with_locations` adds the guarantee, routes, members,
  MIK-R03's `staleMembers` and every member entry not at (file) or under (directory) the path.
- **Records.** `_links_to` collects `links_to_path` (anchor and route targets) plus each invariant's
  `linked_from`; `_linked_records` summarises each linking record once and attaches a decision in full.
- **States.** `states_at` is the reader's one currentness call: MIK-R03's `invariant_currentness` at the
  selection's code tree, or the reason it failed. `_currentness_block` reports the counts, or the failure
  with `unverifiableReason`, never an empty state.
- **Kind and references.** `_path_kind` asks the code tree first, then a sidecar, then file prose, then the
  index; otherwise it is a directory. `_references` reads the file or route sidecar and resolves its
  `references` through `records.reference_items`; an unreadable sidecar is `unavailable`, not empty.

### Conventions

- Nothing is re-derived: states come from L03's function, route chains from L05's, decisions from L13's
  helpers, coverage from the tree-coverage owner, and the without-proof list from L28's index lookup.
- The prose path of a file is `onboarding/<path>.md`; a directory's is `onboarding/<path>/overview.md`.

### Invariants And Boundaries

- **A directory view is bounded, and the full subtree is paged by a continuation bound to tree, policy and
  path.** Realized by `path_view`'s own-level read and `_directory_summary` here, and by
  `subtree.subtree_page`. Proved by the bounded-directory and subtree cases.
- **The tree listing has one owner:** `tree_listing` delegates to `read_tree_listing`; the route does not
  enumerate directories itself (MIK-R79).
- **A failed source is shown as partial or unavailable, never as empty:** an unverifiable state carries its
  reason, an unreadable sidecar is named, and a missing code tree still lists the onboarding side.
- A retired invariant is never shown as current, and a sibling that merely shares a prefix is never counted.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packets `MIK-R29@v1` with its rulings, and `MIK-R79@v1` for the delegated listing; they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The explorer level delegates to the one tree-coverage owner. [13]
- The one pathname inventory, presence marks and coverage owner. [14]
- The path view, bounded for a directory. [15]
- The one currentness call, and its failure named. [16]
- The without-proof list, filtered by path. [17]
- The file, directory, test-file, explorer and without-proof cases. [18]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
