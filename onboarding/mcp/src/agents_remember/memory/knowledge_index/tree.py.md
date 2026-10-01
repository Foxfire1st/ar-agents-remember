# mcp/src/agents_remember/memory/knowledge_index/tree.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**A memory tree as the index reads it: its key and the bytes of its knowledge files (MIK-R23 rules 1, 2).** A tree reaches the index as a Git tree read through objects (`ls-tree` plus one `cat-file --batch`, nothing checked out; the key is the tree id) or as a working-tree directory (the key is the tree id of its *captured state*). Both end as a `MemoryTreeSnapshot`: key, source kind, location and the files the index reads.

## Code Commentary

### Logic

- `is_indexed_path(path)` is the file filter: a `.json` file not excluded by MIK-R22's shared `is_excluded_from_knowledge` (no `*.index.json` route cache, nothing in a hidden directory), under `knowledge/` but not `knowledge/census/` (MIK-R20 owns those schemas), or under `onboarding/`. Everything else contributes to the key only.
- `git_tree_snapshot(repository, revision)` resolves `revision^{tree}`, lists it with `read_git_tree_bytes`, and reads every indexed blob with one `kernel.git_command.read_git_blobs_bytes` call, bytes unchanged.
- `directory_snapshot(directory)` refuses a directory outside a Git working tree, then captures: `_capture` copies the repository's own index (for its stat cache) into a temporary directory, clears `assume-unchanged` and `skip-worktree` on the copy (`_clear_index_flags`, one `update-index` per flag because it applies only the last such option), runs `git add --all -- .` and `git write-tree [--prefix=…]` with an isolated index and object directory whose alternate is the real object database, and lists the captured tree. It then reads the files from disk and checks each against its captured blob id (`_blob_id`, SHA-1 or SHA-256 by the tree id's length); a mismatch retakes the capture, up to three attempts, and then raises `MemoryTreeError`.
- `directory_key(directory)` is the capture alone, without reading files — what the cache uses to decide reuse.

### Conventions

- All Git goes through `kernel/git_command.py` (`run_git`, `run_git_with_isolated_index_and_objects`, `read_git_tree_bytes`, `read_git_blobs_bytes`), per the single-owner rule for Git argv.

### Invariants And Boundaries

- **Computing a key changes nothing in the repository**: the temporary index and every object the capture writes live in a disposable directory, and the real index keeps its flags.
- The capture honours `.gitignore` as a commit would, so identical content gets an identical key and ignored caches (`overview.index.json`) never reach it.
- A snapshot's bytes are always the bytes its key names; mixed state is never served.
- An index flag never hides an edit from the key.

### Todos

Review R1 noted that a sparse checkout would capture its skipped files as deleted; memory repositories are not sparse.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The filter, the two readers and the capture.

- The two sources, the captured-state key and what the capture never writes. [1]
- The snapshot value and the read error. [2]
- The indexed-file filter, sharing the validator's exclusion predicate. [3]
- The Git-object reader: one batch read, nothing checked out. [4]
- The directory reader and its key, with the blob-id check and retry. [5]
- The isolated capture and the index-flag clearing on the scratch copy. [6]
- Source and key cases: directory and Git tree agree, a historical tree needs no checkout, the key is the captured tree id and content-only, capture writes nothing, a plain directory has no key. [7]
- An index flag never hides an edit; the index reads the files the validator reads. [8]

### Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

No cross-repo boundary is crossed by this file.
