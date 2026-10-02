# mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The two inputs the validator reads.** A `KnowledgeTree` is the exact bytes of every file under `knowledge/` and `onboarding/` of one memory tree, keyed by repository-relative POSIX path; it is *converted* exactly when it holds `knowledge/layout.json` (MIK-R21 rule 1). A `CodeTree` answers two questions: does the paired code tree hold a file at this path (anchor path existence, MIK-R22 rule 6), and, since MIK-R04, does it hold a directory at this path (a family route, MIK-R04 rule 1)? Both can be read from a working directory or from Git.

## Code Commentary

### Logic

- `is_excluded_from_knowledge(relative)` is the one predicate for "not knowledge": a `*.index.json` route-index cache, or a path with a dot-named *directory* component (such as `.ar-index/`). A dot-named *file* is knowledge, so `onboarding/.git-blame-ignore-revs.md` is validated (review R1 finding 1). `cli/knowledge_format.py` imports the same predicate.
- `is_knowledge_path` adds the `knowledge/` or `onboarding/` prefix.
- `knowledge_tree_from_directory` walks both roots with `os.walk`, pruning dot directories, and reads each file's bytes.
- `knowledge_tree_from_git` resolves the tree-ish with `rev-parse --verify`, lists regular files (`100644`/`100755` blobs) from `read_git_tree_bytes`, and reads all wanted blobs through one `kernel.git_command.read_git_blobs_bytes` call, so the bytes are exact: no decoding and no newline normalisation.
- `code_tree_from_git` returns a `CodePathSet` of every regular file path; `CodeDirectory` answers `has_file` from a working tree.
- `has_directory` (MIK-R04): `CodePathSet` derives a cached `directories` set, every directory that holds a file of the set at any depth, and answers the root route `.` (`ROOT_ROUTE_PATH`) as always present; `CodeDirectory` answers with `is_dir()`, which also holds for `.`. The empty string and a file path are not directories.
- A tree-ish that names no tree raises `KnowledgeTreeReadError` (a `ValueError`).
- `history_tree_from_git(repository, treeish)` (L37) reads only the files under `knowledge/history/` of a commit
  or tree, as a `KnowledgeTree`. It is all the freeze rules read of a commit that is not a comparison base: the
  commit a leaf's candidate sits on.

### Conventions

- `CodeTree` is a `Protocol` with `label`, `has_file` and `has_directory`, so tests pass a literal `CodePathSet`. Any future structural implementation must add `has_directory`; pyright catches the omission.
- Paths are POSIX and repository-relative on both readers, so the directory and Git readers yield identical trees (a route test asserts it).

### Invariants And Boundaries

- The route-index cache is never read as knowledge, and no file escapes validation by its name.
- Git bytes are read raw, so the canonical-format check sees what will be committed.
- `converted` is decided by the marker alone.
- The two implementations can disagree on a directory that holds only ignored or untracked files (`__pycache__`, a build directory): `CodeDirectory` sees it, the Git `CodePathSet` of a commit route does not. This mirrors `has_file`/`is_file` and is accepted (review R1 finding 3).

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The predicate, the tree types and the two readers.

- The shared exclusion predicate: cache files and hidden directories only. [1]
- A tree is converted exactly when it holds the layout marker. [2]
- The code-tree protocol and its two implementations, each answering file and directory existence. [3]
- Both code trees answer directory existence, the root route included. [4]
- The directory reader prunes dot directories. [5]
- The Git readers: regular files only, blobs read in one batch as exact bytes. [6]
- The formatter shares the predicate. [7]
- A dot-named card and its sidecar are validated. [8]
- The Git reader reads exact bytes, ignores the cache, and matches the directory reader. [9]

- Only the history files of a commit that is not a comparison base. [10]

### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.
