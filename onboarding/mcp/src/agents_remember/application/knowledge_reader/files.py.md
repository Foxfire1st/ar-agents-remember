# mcp/src/agents_remember/application/knowledge_reader/files.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_reader/files.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:06:02+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The files behind a reader selection: memory prose and sidecars, code paths and code text, and the
census files.** A selection's memory files are read from Git objects (a commit) or from the scope's working
directory (`published`, a leaf); code is always read from the selection's code tree in the code repository's
object store. Every read is confined and nothing is written.

Three answers are kept apart everywhere: **present** (with the text), **absent** (the tree holds nothing
there, a normal fact) and **unavailable** (the tree or object could not be read, with the reason). The code
view adds two bounded notices, **binary** and **too-large**. An unavailable read is never rendered as absent,
and none of them is rendered as an empty result.

## Code Commentary

### Logic

- **Path validation.** `normal_path` returns a repository-relative POSIX path (`.` for the root). It refuses
  any control character (below 0x20, or 0x7f) with `ReaderRequestError` before any Git call, so a NUL in a
  path answers 400 on every view that takes one (ruling 2026-09-30T10:44:14, F15). It also refuses `..`, `.`
  segments, empty segments and absolute paths.
- **Memory files.** `read_memory_file` reads a working-tree file under `confine_rel` of the memory root, or
  a commit's blob with `cat-file -t` then `cat-file blob`. A missing file is `absent`; a failed read or a
  decode error is `unavailable` with its reason.
- **Listings.** `list_onboarding_directory` lists `onboarding/<directory>` of the memory tree (skipping dot
  files); `list_code_directory` lists the code tree with `ls-tree`, or answers `unavailable` with the
  selection's code note when there is no code tree. `code_kind` tells a file from a directory of the code
  tree (`cat-file -t`).
- **Code text (F14, F18).** `code_text` first locates the blob (`_code_blob`): a path the tree does not hold
  is `absent`; a path that is a tree (or a submodule) is `absent` with "is a tree, not a file" (F18, which was
  `unavailable` before). It then asks the blob's **size** (`cat-file -s`) before reading any bytes: above
  `CODE_TEXT_LIMIT` (2 MiB) the answer is `too-large` with the size; otherwise the bytes are read and a NUL in
  the first 8 KiB, or a failed strict UTF-8 decode, answers `binary` with the size. The bytes are never
  served in either case (the real 8.7 MB mp4 answers 673 bytes, `too-large`).
- **Census files.** `census_files` returns every file under `knowledge/census/` of the selected tree, from
  disk or from `ls-tree -r` plus one batched blob read, for MIK-R20's report (the index does not read them).

### Conventions

- Code paths are handed to `ls-tree`, `cat-file` and `rev-parse` as `<tree>:<path>` object names, never to the
  file system. Memory paths on disk go through `confine_rel`.
- `ReaderRequestError` is a `ValueError` subclass; the entry point turns it into `invalid-request`.

### Invariants And Boundaries

- **A failed source is shown as partial or unavailable, never as empty** (a candidate invariant recorded on
  the package entry card): `FileRead` keeps `absent` and `unavailable` apart everywhere.
- **Every read is bounded:** the code view never loads a blob above the bound (the size is asked first, and
  a test proves the bytes are never read for a `too-large` blob, F17).
- Nothing here writes.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of present, absent and unavailable. | "Three answers are kept apart everywhere" | mcp/src/agents_remember/application/knowledge_reader/files.py:1-12 |
| The file states and the 2 MiB code bound. | `FileState`; `CODE_TEXT_LIMIT` | mcp/src/agents_remember/application/knowledge_reader/files.py:49-49; mcp/src/agents_remember/application/knowledge_reader/files.py:52-52 |
| A request error, and one file's answer. | `ReaderRequestError`; `FileRead` | mcp/src/agents_remember/application/knowledge_reader/files.py:58-59; mcp/src/agents_remember/application/knowledge_reader/files.py:63-77 |
| Control characters, `..` and absolute paths refused before any Git call (F15). | `normal_path` | mcp/src/agents_remember/application/knowledge_reader/files.py:86-99 |
| A memory file from disk or from a commit, absent kept apart from unavailable. | `read_memory_file` | mcp/src/agents_remember/application/knowledge_reader/files.py:102-129 |
| The onboarding mirror's and the code tree's children; a missing code tree named. | `list_onboarding_directory`; `list_code_directory`; `code_kind` | mcp/src/agents_remember/application/knowledge_reader/files.py:132-148; mcp/src/agents_remember/application/knowledge_reader/files.py:151-163; mcp/src/agents_remember/application/knowledge_reader/files.py:166-179 |
| The size asked before the bytes; a tree is not a file; binary detection (F14, F18). | `code_text`; `_code_blob`; `_text`; `_blob_size` | mcp/src/agents_remember/application/knowledge_reader/files.py:182-200; mcp/src/agents_remember/application/knowledge_reader/files.py:203-215; mcp/src/agents_remember/application/knowledge_reader/files.py:218-225; mcp/src/agents_remember/application/knowledge_reader/files.py:228-232 |
| The census files of the selected tree. | `census_files` | mcp/src/agents_remember/application/knowledge_reader/files.py:239-254 |
| The route case: control characters answer 400 on every path view. | `_assert_control_characters_refused` | mcp/tests/test_knowledge_reader.py:1129-1139 |
| The route case: a directory is absent, a binary blob and a blob above the bound are named and never read. | `test_bad_requests_are_400_and_large_or_binary_code_is_a_bounded_notice` | mcp/tests/test_knowledge_reader.py:1142-1182 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:06:02+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, with R3-1 and R3-2 fixed): created this card for the new module MIK-R29 adds, recording rulings 09:42:58 F14 (a binary or oversize blob answers a bounded notice) and F11, and 10:44:14 F15 (NUL and control characters answer 400), F17 (the size is asked before the bytes, tested) and F18 (the code view of a directory is a typed absent). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
