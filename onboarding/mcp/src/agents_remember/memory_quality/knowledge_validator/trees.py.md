# mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The two inputs the validator reads.** A `KnowledgeTree` holds the exact bytes of the included files under `knowledge/` and `onboarding/`, keyed by repository-relative POSIX path; it is *converted* exactly when it holds `knowledge/layout.json` (MIK-R21 rule 1). A `CodeTree` answers three questions: does the paired code tree hold a file at this path (anchor path existence, MIK-R22 rule 6), does it hold a directory at this path (a family route, MIK-R04 rule 1), and, since MIK-R198, what exact bytes does that file hold at the commit — `CodePathSet` carries them, so the anchor guard compares a recorded content identity with the paired tree's own bytes and reads each cited file once instead of once per anchor. All three can be read from a working directory or from Git.

## Code Commentary

### Logic

- `is_excluded_from_knowledge(relative)` recognizes generated `*.index.json` route-index caches. Dot-prefixed filenames and directory components under either knowledge root remain visible. `cli/knowledge_format.py` shares the cache predicate and owns its directory-operand traversal.
- `is_knowledge_path` adds the `knowledge/` or `onboarding/` prefix.
- `knowledge_tree_from_directory` walks both roots with `os.walk`, including dot directories, and reads the bytes of each regular file selected by the shared path predicate.
- `knowledge_tree_from_git` resolves the tree-ish with `rev-parse --verify`, selects regular files (`100644`/`100755` blobs) under both roots using the shared path predicate, and reads all selected blobs through one `kernel.git_command.read_git_blobs_bytes` call. The result keeps their exact bytes and line endings.
- `code_tree_from_git` returns a `CodePathSet` of regular Git paths. The standalone working-tree validator uses `code_tree_from_working_directory`: Git cached and ordinary untracked, nonignored paths filtered to current regular non-symlink files. The separate raw `CodeDirectory` answers direct filesystem `has_file`; it is not this Git-visible input owner.
- `has_directory` (MIK-R04): `CodePathSet` derives a cached `directories` set, every directory that holds a file of the set at any depth, and answers the root route `.` (`ROOT_ROUTE_PATH`) as always present; `CodeDirectory` answers with `is_dir()`, which also holds for `.`. The empty string and a file path are not directories.
- A tree-ish that names no tree raises `KnowledgeTreeReadError` (a `ValueError`).
- `history_tree_from_git(repository, treeish)` (L37) reads only the files under `knowledge/history/` of a commit
  or tree, as a `KnowledgeTree`. It is all the freeze rules read of a commit that is not a comparison base: the
  commit a leaf's candidate sits on.

### Conventions

- `CodeTree` is a `Protocol` with `label`, `has_file` and `has_directory`, so tests pass a literal `CodePathSet`. Any future structural implementation must add `has_directory`; Pyrefly catches the omission.
- Paths are POSIX and repository-relative on both readers, so the directory and Git readers yield identical trees (a route test asserts it).

### Invariants And Boundaries

- Dot-prefixed names stay visible inside both roots. Generated route-index caches stay outside the knowledge input.
- Git bytes are read raw, so the canonical-format check sees what will be committed.
- `converted` is decided by the marker alone.
- The two implementations can disagree on a directory that holds only ignored or untracked files (`__pycache__`, a build directory): `CodeDirectory` sees it, the Git `CodePathSet` of a commit route does not. This mirrors `has_file`/`is_file` and is accepted (review R1 finding 3).

### Todos

None recorded.

The Git-visible working-directory reader raises `KnowledgeTreeReadError` when `git ls-files -z --cached --others --exclude-standard` cannot list the input. It includes ordinary untracked regular files but excludes ignored paths, missing paths and symbolic links before deriving `CodePathSet` directories. The historical raw-filesystem/Git disagreement remains a distinction between those separate readers, not the present standalone command's policy.

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

- The shared exclusion predicate recognizes generated route-index caches. [1]
- A tree is converted exactly when it holds the layout marker. [2]



- The code-tree protocol and its two implementations, each answering file and directory existence.  Anchor: `CodeTree` `CodePathSet` `CodeDirectory` [3]


- Both code trees answer directory existence, the root route included. [4]
- The directory reader includes dot directories under both memory roots and excludes route-index caches. [5]



- Git tree selection keeps regular blobs, and the knowledge reader reads their exact bytes in one batch. [6]


- The formatter uses the shared cache predicate and includes dot directories under converted knowledge and onboarding roots. [7]

- A dot-named card and its sidecar are validated. [8]

- Git and directory snapshots both retain the workflow card and sidecar, exclude the cache, and expose the card’s missing reference to validation. [9]




- The history reader loads only files under knowledge/history/. [10]


### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.


- The working-directory validator input is Git-visible current regular non-symlink files, with named listing failure. [11]

The working-directory filter checks a listed path for a symbolic link before testing regular-file existence. This preserves the accepted Git-visible path set while avoiding inspection through a leaf symlink.

- Git supplies tracked and nonignored untracked paths; links are discarded first. [12]
