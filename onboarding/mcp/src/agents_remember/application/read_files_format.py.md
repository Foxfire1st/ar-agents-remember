# mcp/src/agents_remember/application/read_files_format.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**What `read_ar_files` returns beside a card, by the memory tree's format (MIK-R24 rules 5 and 9).** A
converted tree is read in the text format, with its sidecar and resolved references. An unconverted tree is
returned as it is, marked `legacy-format`, with no knowledge section, so the old format is never misread as
the new one.

## Code Commentary

### Logic

- `memory_format(root)` is `text/v2` exactly when the tree holds `knowledge/layout.json`, and
  `legacy-format` otherwise.
- `legacy_published_intent(root)` is the knowledge section of an unconverted tree: `state:
  "legacy-format"`, the memory root, and a detail naming both conversion routes. A line that descends from a
  converted official line converts through the crossing sync (`worktree_sync`). An unconverted official
  line, or a repository without one, converts by running `agents-remember knowledge-convert` on that line
  and committing it through its normal route.
- `converted_card_parts(root, onboarding_rel)` reads `onboarding/<rel>.json` and returns `format:
  "text/v2"`, the sidecar, and the references resolved in number order:
  - a `code` or `test` target has its anchor `path` filled in from the sidecar's own path;
  - an ID target (`invariant`, `family`, `decision`, `incident`, `record`) carries its record's summary
    (`_record_summary`: path, statement or title or guarantee or context, status and revision), or
    `state: unreadable`;
  - each entry keeps its `note`.

  A card without a sidecar, or with an unreadable one, returns an empty reference list.

### Conventions

- `application/read_files.py` calls this module; `models/read_files.FileRead` admits the three optional
  fields.

### Invariants And Boundaries

- **Legacy-format reads are active in this build (architect ruling, 2026-09-29).** This build is not
  installed before MIK-R37. Refusals of unconverted trees elsewhere stay inert until the official line
  is converted.
- Nothing is resolved from sidecars on an unconverted tree.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The format switch and the two readings.

- The format is decided by the layout marker. [1]
- An unconverted tree's knowledge section names both conversion routes. [2]
- A converted card's sidecar and resolved references. [3]
- The call site in the entry point. [4]
- `read_ar_files` returns legacy-format or resolved references, and the converted tree's knowledge section through the tool. [5]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
