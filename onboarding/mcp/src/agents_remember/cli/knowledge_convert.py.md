# mcp/src/agents_remember/cli/knowledge_convert.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_convert.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `e40c314ca55305f7e4334b4e8e16a10297f6f175`|
| lastVerifiedCommitDate | 2026-09-29T18:13:06+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**CLI adapter: `agents-remember knowledge-convert MEMORY_ROOT --code CODE_REPOSITORY [--code-commit REV]
[--version V] [--report FILE] [--check]` (MIK-R24).** It converts a memory working tree (its `onboarding/`
cards and its `knowledge.sqlite`) into the text knowledge format, in place. Every card's citations are
anchored in the tree of the card's `lastVerifiedCommitHash`, read from the object store of `--code`.
`--code-commit` (default `HEAD` of `--code`) is the paired code tree, used for fallback cards and for the
report's currentness counts.

## Code Commentary

### Logic

- `add_arguments` declares the memory root, `--code` (required), `--code-commit`, `--version` (default and
  only supported value `1`), `--report` (the JSON report) and `--check` (convert and report, write
  nothing).
- `run` reads the tree (`inputs.memory_from_directory`), builds `CodeObjects` and calls `convert_memory`.
  It writes the report if asked. An already converted tree prints a no-op message. Unless `--check`, it
  then writes the changed files (`inputs.write_changed`) and prints the counts: files, references,
  unresolved targets, invariants, families, realizations.
- Exit status: 0 converted (or already converted); 1 refused (an unsupported version, validation, the
  export, or an unreadable code object); 2 an invocation or read error.

### Conventions

- Registered by `cli/__main__.py` as the `knowledge-convert` subcommand.

### Invariants And Boundaries

- **The command commits nothing.** Committing a conversion to a real memory line is the cutover's
  (MIK-R37), or a crossing sync's (rule 8).
- It writes only after the whole converted tree validated.
- No installed route calls it before MIK-R37. Later leaves use it to make the converted scratch copies
  their evidence runs on.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The arguments, the run and its registration.

| Finding | Anchor | Source |
| --- | --- | --- |
| The arguments. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_convert.py:40-54 |
| The run: convert, report, write unless checking, exit status. | `run` | mcp/src/agents_remember/cli/knowledge_convert.py:57-89 |
| The umbrella registration. | `knowledge_convert`; "knowledge-convert" | mcp/src/agents_remember/cli/__main__.py:78-83 |
| The conversion it drives. | `convert_memory` | mcp/src/agents_remember/memory/conversion/convert.py:387-431 |

## Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R08 moved lines in `__main__.py`, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). No claim, anchor or source file of this card changed.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
