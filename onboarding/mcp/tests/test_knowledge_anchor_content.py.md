# mcp/tests/test_knowledge_anchor_content.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The one definition of an anchor's `content` bytes, pinned.** Registered in the `unit-regression`
lane; 5 collected cases (4 parametrized plus 1).

## Code Commentary

### Logic

- A line range keeps each line's own terminator: LF, CRLF, a lone `\r`, `\x0b` and `\x85` inside a line,
  no final newline, and invalid UTF-8.
- `line_count`, whole-file content, and ranges outside the blob or starting at zero.

### Conventions

- Expected hashes are computed with `hashlib` in the test, not hard-coded.

### Invariants And Boundaries

- Any change to which bytes a range names is a visible test change.

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

The cases.

- Terminators kept, bytes undecoded. [1]
- Line count, file content and refusals. [2]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
