# mcp/src/agents_remember/application/knowledge_writer/base_side.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The writer's base: the memory worktree's `HEAD`, or its conversion when the candidate is converted and `HEAD` is
not.** The writer compares the candidate with a base for three
things: an existing record's revision before the operation, an entry's `before` anchor, and the validator's carried
anchors and frozen history files. On the converting leaf (the conversion is uncommitted until closeout) and on a
crossing sync whose own side is unconverted, a raw unconverted `HEAD` would make every record and entry look new:
wrong revisions, empty `before` anchors and false `R22.6` refusals. During a merge the incoming parent `MERGE_HEAD`
is a second validation base, converted by the same rule through the same cache, so an anchor the incoming side
carries is judged as carried.

## Code Commentary

### Logic

- `writer_bases(root, candidate, code)` returns `BaseSides(base, problem, incoming)`. A root that is not a Git work
  tree has no base. Otherwise `_head` builds the base from `HEAD`; when `HEAD` yields no problem, `_with_incoming`
  adds the incoming parent `MERGE_HEAD` as `incoming` while a merge is in progress (`_merge_head` resolves) and
  returns `HEAD`'s sides unchanged outside a merge. `BaseSides.validation_bases` is the converted ones of `base`,
  then `incoming`; the writer (`MemoryState.validation_bases`) and the memory-quality check validate against them.
  Revisions and `before` anchors still come from `HEAD` alone.
- `_head`: an unborn `HEAD` means no base (every record is new). `_side(root, label, commit, candidate, code)`
  reads the given commit's tree with `knowledge_tree_from_git`. When that tree is converted, or the candidate is
  not, or no code root is known, the tree is the base as it is. Otherwise the base is that side's conversion from
  `knowledge_worklist.base_cache.converted_base_files`, at the candidate's pinned conversion version and a code
  commit, returned as a `KnowledgeTree` labelled `converted base <label> <commit>` (`label` is `HEAD` or
  `MERGE_HEAD`).
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
- **During a merge the incoming parent is never silently left out.** A `MERGE_HEAD` that names no commit Git can
  read, or whose tree cannot be read, or whose conversion cannot be built, becomes a problem naming "the incoming
  merge parent" or "the converted base of the memory worktree's MERGE_HEAD", and both name the remedy: conclude
  or abort the merge in the memory worktree, then retry. The base is then `None` with that problem, never `HEAD`
  alone and never an empty tree. A problem of `HEAD` is returned before
  `MERGE_HEAD` is read.
- A converted `HEAD` is unchanged: nothing is converted.

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the text-storage cutover's requirement and rulings in the task records; it lives outside
the code and memory repositories, so it is not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: one base for every reader, and a named problem when it cannot be built. [1]

- The writer's bases for a memory worktree, HEAD and during a merge MERGE_HEAD, or the named problem. [2]

- A side's tree, HEAD's or MERGE_HEAD's, or its conversion when that side is unconverted and the candidate is converted. [3]

- What converting an unconverted base reads, and where it is cached. [4]
- The state loads its base through this module. [5]
- An unconverted HEAD is compared through its converted base: the next revision, the base's before anchor, one cache file. [6]
- A trailerless HEAD converts at the gate's code base, and an unreadable one refuses. [7]

### Cross-Repo References

No meaningful cross-repo references found: the module reads one memory repository and one code repository through Git.

No cross-repo boundary is crossed by this file.
