# mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The two inputs the validator reads.** A `KnowledgeTree` is the exact bytes of every file under `knowledge/` and `onboarding/` of one memory tree, keyed by repository-relative POSIX path; it is *converted* exactly when it holds `knowledge/layout.json` (MIK-R21 rule 1). A `CodeTree` answers the one question anchor path existence asks (rule 6): does the paired code tree hold a file at this path? Both can be read from a working directory or from Git.

## Code Commentary

### Logic

- `is_excluded_from_knowledge(relative)` is the one predicate for "not knowledge": a `*.index.json` route-index cache, or a path with a dot-named *directory* component (such as `.ar-index/`). A dot-named *file* is knowledge, so `onboarding/.git-blame-ignore-revs.md` is validated (review R1 finding 1). `cli/knowledge_format.py` imports the same predicate.
- `is_knowledge_path` adds the `knowledge/` or `onboarding/` prefix.
- `knowledge_tree_from_directory` walks both roots with `os.walk`, pruning dot directories, and reads each file's bytes.
- `knowledge_tree_from_git` resolves the tree-ish with `rev-parse --verify`, lists regular files (`100644`/`100755` blobs) from `read_git_tree_bytes`, and reads all wanted blobs through one `kernel.git_command.read_git_blobs_bytes` call, so the bytes are exact: no decoding and no newline normalisation.
- `code_tree_from_git` returns a `CodePathSet` of every regular file path; `CodeDirectory` answers `has_file` from a working tree.
- A tree-ish that names no tree raises `KnowledgeTreeReadError` (a `ValueError`).

### Conventions

- `CodeTree` is a `Protocol` with `label` and `has_file`, so tests pass a literal `CodePathSet`.
- Paths are POSIX and repository-relative on both readers, so the directory and Git readers yield identical trees (a route test asserts it).

### Invariants And Boundaries

- The route-index cache is never read as knowledge, and no file escapes validation by its name.
- Git bytes are read raw, so the canonical-format check sees what will be committed.
- `converted` is decided by the marker alone.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The predicate, the tree types and the two readers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared exclusion predicate: cache files and hidden directories only. | `is_excluded_from_knowledge`; `is_knowledge_path` | mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:47-60; mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:63-66 |
| A tree is converted exactly when it holds the layout marker. | `KnowledgeTree` | mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:70-83 |
| The code-tree protocol and its two implementations. | `CodeTree`; `CodePathSet`; `CodeDirectory` | mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:86-92; mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:96-103; mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:107-114 |
| The directory reader prunes dot directories. | `knowledge_tree_from_directory` | mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:117-132 |
| The Git readers: regular files only, blobs read in one batch as exact bytes. | `_tree_blobs`; `knowledge_tree_from_git`; `code_tree_from_git` | mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:147-158; mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:161-174; mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:177-181 |
| The formatter shares the predicate. | `iter_json_files` | mcp/src/agents_remember/cli/knowledge_format.py:35-45 |
| A dot-named card and its sidecar are validated. | `test_a_dot_named_card_and_its_sidecar_are_validated` | mcp/tests/test_knowledge_validator.py:292-312 |
| The Git reader reads exact bytes, ignores the cache, and matches the directory reader. | `test_git_trees_are_read_exactly_and_the_route_index_cache_is_ignored` | mcp/tests/test_knowledge_validator_routes.py:73-95 |

## Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
