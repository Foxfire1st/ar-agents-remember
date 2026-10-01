# mcp/src/agents_remember/models/knowledge_files/__init__.py

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
  (file and route sidecars under `onboarding/` and the layout marker), `history` (the per-leaf
  history files, `ar-history/v1`, MIK-R07), `documents` (locations and the schema dispatch) and `canonical` (the formatting applied by `agents-remember knowledge-format`).
- It states the Markdown marker rule once: a file's `[n]` markers are local numbers that resolve
  through the paired sidecar's `references`; text that merely looks like a marker sits in a code
  span or is written `\[0]`. Parsing markers is the validator's job (MIK-R22), not this package's.
- The body is imports plus `__all__`; no logic lives here. Since MIK-R07 the surface also carries
  `HISTORY_ROW_KINDS`, `HistoryFile`, `HistoryRow`, `InvariantRow`, `FamilyRow`,
  `frozen_history_violation`, `history_path` and `parse_history_document`; the finer history
  helpers (`empty_history`, `is_closed_history`, the writer-support checks) are imported from
  `history` directly.

### Conventions

- `__all__` is the supported surface. Deeper names (for example `split_record_filename`,
  `crockford_base32`) are imported from their submodules directly by the tests.

### Invariants And Boundaries

- The models check **shape and formatting only**. Integrity — IDs resolve, markers match
  references, one owner per relationship, family route coverage — belongs to the validator (MIK-R22).
- **Nothing in the installed runtime reads or writes these files before MIK-R37.** The package is
  reached only from `agents-remember knowledge-format` and the tests; the live memory repository
  is still read and written through the SQLite knowledge store until the layout switch.

### Todos

None recorded. Doc14 §4 still shows the older illustrative shapes (see the tests' refusal case); updating Doc14 is outside this leaf.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The re-export list is what the tests and the formatter command import.

- The format map and the shape-only boundary. [1]
- The marker and escaping rule the validator will enforce. [2]
- The public surface. [3]
- The formatter command is the package's only production consumer. [4]

### Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

No cross-repo boundary is crossed by this file.
