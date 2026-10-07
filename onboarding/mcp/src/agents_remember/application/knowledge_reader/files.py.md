# mcp/src/agents_remember/application/knowledge_reader/files.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The files behind a reader selection: memory prose and sidecars, code paths and code text, and the
census files.** A selection's memory files are read from Git objects (a commit) or from the scope's
working directory (`published`, a leaf); code is always read from the selection's code tree in the
code repository's object store. Every read is confined and nothing is written.

Three answers are kept apart everywhere: **present** (with the text), **absent** (the tree holds
nothing there, a normal fact) and **unavailable** (the tree or object could not be read, with the
reason). The code view adds two bounded notices, **binary** and **too-large**. An unavailable read is
never rendered as absent, and none of them is rendered as an empty result. Since MIK-R79 the
directory-listing helpers live with the tree-coverage module, so this module is the single-file read
boundary again.

## Code Commentary

### Logic

- **Path validation.** `normal_path` refuses any control character (below 0x20, or 0x7f) with
  `ReaderRequestError` before any Git call, so a NUL in a path answers 400 on every view that takes
  one. It then strips surrounding whitespace and slashes (an empty value or `.` is the root) and
  normalizes with `PurePosixPath`; after that normalization only a `..` part is refused — a `.` or an
  empty segment is normalized away and a leading slash has already been stripped, so an absolute form
  is treated as the relative path it normalizes to.
- **Memory files.** `read_memory_file` reads a working-tree file under `confine_rel` of the memory
  root, or a commit's blob with `cat-file -t` then `cat-file blob`. A working-tree file that is not
  there, and a Git path whose initial type probe fails or is not a blob, are `absent`; a later failed
  blob read, or a read/decode exception, is `unavailable` with its reason.
- **Code text.** `code_text` first locates the blob (`_code_blob`): a path the tree does not hold is
  `absent`; a path that is a tree (or a submodule) is `absent` with "is a tree, not a file". It then
  asks the blob's **size** (`cat-file -s`) before reading any bytes: above `CODE_TEXT_LIMIT` (2 MiB)
  the answer is `too-large` with the size; otherwise the bytes are read and a NUL in the first 8 KiB,
  or a failed strict UTF-8 decode, answers `binary` with the size. The bytes are never served in
  either case.
- **Code kind.** `code_kind` tells a file from a directory of the code tree (`cat-file -t`).
- **Census files.** `census_files` returns every file under `knowledge/census/` of the selected tree,
  from disk or from `ls-tree -r` plus one batched blob read.

### Conventions

- Code paths are handed to `ls-tree`, `cat-file` and `rev-parse` as `<tree>:<path>` object names,
  never to the file system. Memory paths on disk go through `confine_rel`.
- `ReaderRequestError` is a `ValueError` subclass; the entry point turns it into `invalid-request`.

### Invariants And Boundaries

- **A failed source is shown as partial or unavailable, never as empty:** `FileRead` keeps `absent`
  and `unavailable` apart everywhere.
- **Every read is bounded:** the code view never loads a blob above the bound (the size is asked
  first, and a test proves the bytes are never read for a `too-large` blob).
- **One enumeration owner per side:** directory listings are answered by
  `application/knowledge_reader/tree_coverage.py`; this module does not list directories.
- Nothing here writes.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R29@v1` with its rulings, and MIK-R79@v1 for the moved listing owner; they
live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The three file states and the bounded code text. [11]
- Control characters are refused before any Git call; after whitespace/slash stripping and PurePosixPath normalization only a `..` part is refused. [12]

- A memory file comes from disk or a commit; a missing file or a failed/not-blob type probe is absent, a later blob-read or decode failure is unavailable. [13]
- The size asked before the bytes; a tree is not a file; binary detection. [14]
- The census files of the selected tree. [15]
- The one pathname inventory that now answers directory listings. [16]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
