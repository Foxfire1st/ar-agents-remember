# mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:49:57+02:00 |
| lastVerifiedCommitHash | `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d`|
| lastVerifiedCommitDate | 2026-09-29T09:20:54+02:00|
| governingOverview | `../overview.md` |

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
| The shared exclusion predicate: cache files and hidden directories only. | `is_excluded_from_knowledge`; `is_knowledge_path` | mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:50-63; mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:66-69 |
| A tree is converted exactly when it holds the layout marker. | `KnowledgeTree` | mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:72-86 |
| The code-tree protocol and its two implementations, each answering file and directory existence. | `CodeTree`; `CodePathSet`; `CodeDirectory` | mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:89-97; mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:101-121; mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:125-135 |
| Both code trees answer directory existence, the root route included. | `test_code_trees_answer_directory_existence` | mcp/tests/test_knowledge_family_routes.py:263-273 |
| The directory reader prunes dot directories. | `knowledge_tree_from_directory` | mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:138-153 |
| The Git readers: regular files only, blobs read in one batch as exact bytes. | `_tree_blobs`; `knowledge_tree_from_git`; `code_tree_from_git` | mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:168-179; mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:182-195; mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:198-202 |
| The formatter shares the predicate. | `iter_json_files` | mcp/src/agents_remember/cli/knowledge_format.py:35-45 |
| A dot-named card and its sidecar are validated. | `test_a_dot_named_card_and_its_sidecar_are_validated` | mcp/tests/test_knowledge_validator.py:296-316 |
| The Git reader reads exact bytes, ignores the cache, and matches the directory reader. | `test_git_trees_are_read_exactly_and_the_route_index_cache_is_ignored` | mcp/tests/test_knowledge_validator_routes.py:73-95 |

## Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — `CodeTree.has_directory` on the protocol and both implementations (MIK-R04 rule 1).** Purpose, Logic, Conventions and Invariants now state the second question, the root route `.` and the working-tree/Git difference (review R1 finding 3). The reopened `CodeTree`/`CodePathSet`/`CodeDirectory` row was re-read, reworded and re-derived from the three constructs' real extents; one row added. No verification stamp was advanced.
- 2026-09-29T06:45:40+00:00: Generated citation repair: `knowledge_tree_from_directory` repointed to mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:138-153. No content impact: mechanical anchor-range projection bound to citation source snapshot 1a5c7dd5cb87835c8b4e585975574124e545ed7ed5b56804bf2cecaf1ab8ce6b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
