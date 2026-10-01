# mcp/src/agents_remember/application/knowledge_writer/base_side.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The writer's base: the memory worktree's `HEAD`, or its conversion when the candidate is converted and `HEAD` is
not (MIK-R24 rule 7; L37 ruling of 2026-10-01T03:56:27).** The writer compares the candidate with a base for three
things: an existing record's revision before the operation, an entry's `before` anchor, and the validator's carried
anchors and frozen history files. On the converting leaf (the conversion is uncommitted until closeout) and on a
crossing sync whose own side is unconverted, a raw unconverted `HEAD` would make every record and entry look new:
wrong revisions, empty `before` anchors and false `R22.6` refusals.

## Code Commentary

### Logic

- `writer_bases(root, candidate, code)` returns `BaseSides(base, problem)`. A root that is not a Git work tree has
  no base. Otherwise the base is `_side(root, "HEAD", candidate, code)`.
- `_side`: an unborn `HEAD` means no base (every record is new). `HEAD`'s tree is read with
  `knowledge_tree_from_git`. When that tree is converted, or the candidate is not, or no code root is known, the
  tree is the base as it is. Otherwise the base is `HEAD`'s conversion from
  `knowledge_worklist.base_cache.converted_base_files`, at the candidate's pinned conversion version and a code
  commit, returned as a `KnowledgeTree` labelled `converted base HEAD <commit>`.
- **The code commit of the conversion.** `converted_base_files` reads the base's own `Code-Commit` trailer first.
  `BaseCode.fallback` is the commit-ish for a base without one: the leaf's code base B on the leaf route (the gate's
  and the worklist's fallback) and the series' code work branch on the crossing route; with no fallback, the code
  tree's `HEAD`.
- `BaseCode(root, fallback, cache_directory)` carries what the conversion reads and where it is cached.

### Conventions

- One conversion, one cache. The key is the memory commit, the conversion-format version and the paired code
  commit, the same key the worklist, the onboarding gate and the census use, so whichever reader runs first pays
  the conversion (about 38 s on the real line) and the others reuse it (about 5 s).

### Invariants And Boundaries

- **Never compare against nothing.** When `HEAD` resolves but its tree cannot be read, `_BaseUnreadable` becomes
  the problem "the base of this operation, the memory worktree's HEAD, cannot be read"; when the conversion cannot
  be built (unknown version or code commit, a failing conversion), the problem names "the converted base (MIK-R24
  rule 7)". `MemoryState` keeps the problem as `base_problem` and the writer refuses with it.
- A converted `HEAD` is unchanged: nothing is converted.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R24@v1` rule 7 and the L37 rulings of 2026-10-01T03:56:27 and 2026-10-01T05:05:16 (F6, F10b) in `37_cutover-to-text-storage.json`; it lives outside the code and memory
repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: one base for every reader, and a named problem when it cannot be built. [1]
- The writer's base for a memory worktree, or the named problem. [2]
- HEAD's tree, or its conversion when HEAD is unconverted and the candidate is converted. [3]
- What converting an unconverted base reads, and where it is cached. [4]
- The state loads its base through this module. [5]
- An unconverted HEAD is compared through its converted base: the next revision, the base's before anchor, one cache file. [6]
- A trailerless HEAD converts at the gate's code base, and an unreadable one refuses. [7]

### Cross-Repo References

No meaningful cross-repo references found: the module reads one memory repository and one code repository through Git.

No cross-repo boundary is crossed by this file.
