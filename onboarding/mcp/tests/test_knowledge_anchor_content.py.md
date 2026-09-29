# mcp/tests/test_knowledge_anchor_content.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_anchor_content.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T10:05:46+02:00 |
| lastVerifiedCommitHash | `cd3e943d740b490d391722389af0a6bca0ccf93e`|
| lastVerifiedCommitDate | 2026-09-29T10:38:08+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| Terminators kept, bytes undecoded. | `test_a_line_range_names_its_lines_with_their_own_terminators` | mcp/tests/test_knowledge_anchor_content.py:22-38 |
| Line count, file content and refusals. | `test_line_count_file_content_and_ranges_outside_the_blob` | mcp/tests/test_knowledge_anchor_content.py:41-51 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
