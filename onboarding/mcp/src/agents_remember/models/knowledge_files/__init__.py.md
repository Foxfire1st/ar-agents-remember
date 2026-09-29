# mcp/src/agents_remember/models/knowledge_files/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T04:55:39+02:00 |
| lastVerifiedCommitHash | `45fe37749b388de348d16ced50c28c03490dce64`|
| lastVerifiedCommitDate | 2026-09-29T05:18:17+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The one declaration of the text knowledge format (MIK-R21), and its public surface.** Text files
in the memory repository become the source of truth for knowledge (D18, Doc14): Markdown for prose,
canonical JSON for structured facts. This package declares their shapes, IDs, locations and
formatting, and the validator (MIK-R22), the derived index (MIK-R23), the writer (MIK-R12) and the
conversion (MIK-R24) are meant to read and write through it rather than restating any of it.
`__init__.py` holds the format overview (what each submodule owns, the `[n]` marker and escaping
rule) and re-exports the names those consumers need.

## Code Commentary

### Logic

- The module docstring is the format's map: `ids` (branch-safe IDs), `shapes` (anchors, references,
  links, admission, origin), `records` (the ten global record kinds under `knowledge/`), `sidecars`
  (file and route sidecars under `onboarding/` and the layout marker), `documents` (locations and the
  schema dispatch) and `canonical` (the formatting applied by `agents-remember knowledge-format`).
- It states the Markdown marker rule once: a file's `[n]` markers are local numbers that resolve
  through the paired sidecar's `references`; text that merely looks like a marker sits in a code
  span or is written `\[0]`. Parsing markers is the validator's job (MIK-R22), not this package's.
- The body is imports plus `__all__`; no logic lives here.

### Conventions

- `__all__` is the supported surface. Deeper names (for example `split_record_filename`,
  `history_path`, `crockford_base32`) are imported from their submodules directly by the tests.

### Invariants And Boundaries

- The models check **shape and formatting only**. Integrity — IDs resolve, markers match
  references, one owner per relationship, family route coverage — belongs to the validator (MIK-R22).
- **Nothing in the installed runtime reads or writes these files before MIK-R37.** The package is
  reached only from `agents-remember knowledge-format` and the tests; the live memory repository
  is still read and written through the SQLite knowledge store until the layout switch.

### Todos

None recorded. Doc14 §4 still shows the older illustrative shapes (see the tests' refusal case); updating Doc14 is outside this leaf.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The re-export list is what the tests and the formatter command import.

| Finding | Anchor | Source |
| --- | --- | --- |
| The format map and the shape-only boundary. | "Integrity (IDs resolve, markers match" | mcp/src/agents_remember/models/knowledge_files/__init__.py:23-23 |
| The marker and escaping rule the validator will enforce. | "only an unescaped" | mcp/src/agents_remember/models/knowledge_files/__init__.py:21-21 |
| The public surface. | `__all__` | mcp/src/agents_remember/models/knowledge_files/__init__.py:69-102 |
| The formatter command is the package's only production consumer. | `format_bytes` | mcp/src/agents_remember/cli/knowledge_format.py:22-22 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): created this card for the new file MIK-R21 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
