# mcp/src/agents_remember/application/read_files_format.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**Memory-format detection and converted-card helper functions (MIK-R24 rules 5 and 9).** `memory_format` distinguishes `text/v2` from `legacy-format`; `converted_card_parts` can return a converted card's sidecar and resolved references, and `legacy_published_intent` constructs an unconverted-format explanation. The naming route uses format selection without carrying card or reference bodies.

## Code Commentary

### Logic

- `memory_format(root)` is `text/v2` exactly when the tree holds `knowledge/layout.json`, and
  `legacy-format` otherwise.
- `legacy_published_intent(root)` reports `state: "legacy-format"`, the memory root
  and why no knowledge is read; this is a format/refusal explanation, not a legacy
  knowledge dataset. The helper's explanation says onboarding is returned as `legacy-format`; the current naming route instead reports `memoryState: unconverted` and names no card. A line
  descending from converted memory crosses through `worktree_sync` with `merge-memory`.
  A never-converted repository follows `first_conversion_procedure()`: run
  `agents-remember knowledge-convert MEMORY_ROOT --code CODE_REPOSITORY` in place
  before baseline adoption when no attributed baseline exists, or on one new leaf
  as its first memory change when an official line exists, then close out and land.
  The refusal names the first-conversion command `agents-remember knowledge-convert
  MEMORY_ROOT --code CODE_REPOSITORY` (MIK-R46 rule 6).
- `converted_card_parts(root, onboarding_rel)` reads `onboarding/<rel>.json` and returns `format:
  "text/v2"`, the sidecar, and the references resolved in number order:
  - a `code` or `test` target has its anchor `path` filled in from the sidecar's own path;
  - an ID target (`invariant`, `family`, `decision`, `incident`, `record`) carries its record's summary
    (`_record_summary`: path, statement or title or guarantee or context, status and revision), or
    `state: unreadable`;
  - each entry keeps its `note`.

  A card without a sidecar, or with an unreadable one, returns an empty reference list.

### Conventions

- `application/read_files.py` imports `TEXT_FORMAT` and `memory_format` for memory selection. `NamedFile` and `ReadArFilesResponse` admit naming fields, not card/sidecar/reference bodies.

### Invariants And Boundaries

- **An unconverted tree is named without a card by `read_ar_files`; ordinary operations refuse unconditionally
  (MIK-R46@v2).** The refusal is not deferred until an official line or another branch
  is converted. Read the old cards, convert through the named procedure, then repeat
  the ordinary converted operation.
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



- The naming entry point checks memory format and dataset selection; it carries no card body, sidecar body or resolved-reference document. [4]




- read_ar_files names the converted records that govern a path - existence, the card's location and the records' states - and carries none of their text; an unconverted tree is answered as unconverted rather than with a knowledge section. [5]


### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
