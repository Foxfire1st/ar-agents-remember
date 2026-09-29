# mcp/src/agents_remember/application/read_files_format.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/read_files_format.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `overview.md` |

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

The format switch and the two readings.

| Finding | Anchor | Source |
| --- | --- | --- |
| The format is decided by the layout marker. | `memory_format`; `TEXT_FORMAT`; `LEGACY_FORMAT` | mcp/src/agents_remember/application/read_files_format.py:29-32; mcp/src/agents_remember/application/read_files_format.py:23-24 |
| An unconverted tree's knowledge section names both conversion routes. | `legacy_published_intent` | mcp/src/agents_remember/application/read_files_format.py:35-49 |
| A converted card's sidecar and resolved references. | `converted_card_parts`; `_record_summary` | mcp/src/agents_remember/application/read_files_format.py:65-93; mcp/src/agents_remember/application/read_files_format.py:52-62 |
| The call site in the entry point. | `_read_one` | mcp/src/agents_remember/application/read_files.py:203-227 |
| `read_ar_files` returns legacy-format or resolved references, and the converted tree's knowledge section through the tool. | `test_read_ar_files_returns_legacy_format_or_resolved_references` | mcp/tests/test_knowledge_conversion_toolchain.py:42-84 |

## Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
