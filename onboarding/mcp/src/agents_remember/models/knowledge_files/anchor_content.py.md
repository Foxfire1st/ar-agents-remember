# mcp/src/agents_remember/models/knowledge_files/anchor_content.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The one definition of an anchor's `content` bytes (MIK-R21 rule 3, MIK-R08 rule 3; architect ruling
5 of 260928-MIK-L12).** `content` is `sha256:<hex>` of the located bytes: a **line range** `start..end`
(one-based, inclusive) is those lines of the blob, each with its own terminator exactly as the blob holds
it; a **file** anchor is every byte; a **symbol** is the range the extractor binds (the caller resolves it,
this module hashes it).

## Code Commentary

### Logic

- `blob_lines` splits on `\n` only (it rejoins what `splitlines` also splits on `\r`, `\v`, `\f`, `\x85`
  …); the last line may have no newline.
- `line_count` counts lines: a final newline ends the last line rather than opening one.
- `range_bytes` raises `RangeOutsideBlobError` for a zero start, an inverted range, or lines the blob does
  not hold.
- Bytes are never decoded, so a non-UTF-8 blob still has a content identity.

### Conventions

- The module is not re-exported from `models/knowledge_files/__init__.py`; callers import it by path.

### Invariants And Boundaries

- **Exactly one definition.** The writer (MIK-R12) records `content` through this module; L24's converter,
  MIK-R03 and R08 must compute it here too. The Doc14/L21 fixture hashes are illustrative, not computed.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The definition and its pins.

- The content prefix. [1]
- Lines end at `\n` only. [2]
- A range's bytes, or a refusal. [3]
- The content identity. [4]
- The writer's only use: resolving an anchor at C. [5]
- LF, CRLF, lone CR and invalid UTF-8 pinned. [6]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
