# mcp/src/agents_remember/memory/knowledge_index/tree.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge_index/tree.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:01:17+02:00 |
| lastVerifiedCommitHash | `ffd043f1354e94a7dcf435e10b4b7224495cbcba`|
| lastVerifiedCommitDate | 2026-09-29T08:30:03+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The filter, the two readers and the capture.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two sources, the captured-state key and what the capture never writes. | "computing a key changes nothing in the repository" | mcp/src/agents_remember/memory/knowledge_index/tree.py:1-23 |
| The snapshot value and the read error. | `MemoryTreeSnapshot`; `MemoryTreeError` | mcp/src/agents_remember/memory/knowledge_index/tree.py:55-62; mcp/src/agents_remember/memory/knowledge_index/tree.py:51-52 |
| The indexed-file filter, sharing the validator's exclusion predicate. | `is_indexed_path`; `is_excluded_from_knowledge` | mcp/src/agents_remember/memory/knowledge_index/tree.py:65-77 |
| The Git-object reader: one batch read, nothing checked out. | `git_tree_snapshot`; `read_git_blobs_bytes` | mcp/src/agents_remember/memory/knowledge_index/tree.py:80-89 |
| The directory reader and its key, with the blob-id check and retry. | `directory_snapshot`; `directory_key`; `_blob_id` | mcp/src/agents_remember/memory/knowledge_index/tree.py:92-119; mcp/src/agents_remember/memory/knowledge_index/tree.py:203-208 |
| The isolated capture and the index-flag clearing on the scratch copy. | `_capture`; `_clear_index_flags` | mcp/src/agents_remember/memory/knowledge_index/tree.py:122-176 |
| Source and key cases: directory and Git tree agree, a historical tree needs no checkout, the key is the captured tree id and content-only, capture writes nothing, a plain directory has no key. | `test_a_working_tree_and_its_git_tree_index_to_the_same_key_and_answers`; `test_a_historical_git_tree_is_read_through_objects_without_a_checkout`; `test_the_key_is_the_tree_id_of_the_captured_state_and_depends_on_content_only`; `test_capturing_a_key_writes_nothing_into_the_repository`; `test_a_directory_outside_git_has_no_key` | mcp/tests/test_knowledge_index.py:67-78; mcp/tests/test_knowledge_index.py:81-94; mcp/tests/test_knowledge_index.py:100-124; mcp/tests/test_knowledge_index.py:127-143; mcp/tests/test_knowledge_index.py:146-150 |
| An index flag never hides an edit; the index reads the files the validator reads. | `test_an_index_flag_never_hides_an_edit_from_the_key`; `test_the_index_reads_the_files_the_validator_reads` | mcp/tests/test_knowledge_index.py:366-381; mcp/tests/test_knowledge_index.py:436-445 |

## Cross-Repo References

No meaningful cross-repo references found: the index reads one memory tree, addressed explicitly by the caller, and nothing else.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
