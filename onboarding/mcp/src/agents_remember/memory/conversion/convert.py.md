# mcp/src/agents_remember/memory/conversion/convert.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**`convert_memory`: one memory tree and its knowledge database into the text format, as a pure function
(MIK-R24 rules 1–4 and 6).** The output depends only on four inputs: the memory tree's files, its
database, the code objects it resolves in (each card's anchor commit and every exported claim's recorded
blob, read through `CodeObjects`) and the conversion-format version. The paired code commit matters only
for rule 2 fallback cards and the report's currentness counts. The conversion validates the whole
converted tree before it returns anything to write, and it produces the report the packet's expected
evidence names.

## Code Commentary

### Logic

- `convert_memory(memory, objects, *, paired_commit, version="1")`:
  1. refuses a version this build does not reproduce (`require_version` raises `ConversionVersionError`);
  2. returns a tree that already holds `knowledge/layout.json` unchanged, as `already-converted` (a no-op);
  3. refuses a paired commit missing from the object store;
  4. converts every card (`_convert_cards`) and exports the database (`legacy_db.export_database`);
  5. merges the exported entries into their files' sidecars (`_merge_entries`);
  6. adds the layout marker `{schema: ar-memory-layout/v2, conversion: <version>}`;
  7. computes the changed files (`_changed_files`, which refuses to overwrite a file the unconverted tree
     already has);
  8. validates the whole result (`_require_valid`).
- **The anchor tree (rule 2)** is found by `_anchor_commit`. A card's citations are anchored at the commit
  its `lastVerifiedCommitHash` names. A full ID is looked up exactly. An abbreviated one is resolved
  against every commit of the store with that prefix (`CodeObjects.commits_with_prefix`): exactly one
  resolves it, none takes the listed fallback (the paired commit), and more than one refuses the
  conversion, naming the card. It never falls back silently (review R1 finding 3). Every abbreviated value
  is listed in the report (`abbreviatedAnchorCommits`; two cards on the real tree, both resolving to
  `cb906188f2572c…`).
- `_convert_cards` splits each card (`cards.split_card`) and builds one reference per real row
  (`citations.row_reference`), numbered by position. It renders the Markdown (`cards.render_card`) and
  writes a file sidecar (`ar-onboarding-file/v1`, `{path, references, realizes: []}`) or, for an
  `overview.md`, a route sidecar (`overview.json`, `references{}` only; `.` for the root route). A card
  with no references gets no sidecar.
- `_audit_card` counts the report's measures: cards, rows, placeholders, Update History bytes, residual
  metadata and stray citation rows. It also lists every `governingOverview` whose resolved value is not
  the nearest ancestor overview (`nearest_overview`), and every `path` metadata value that disagrees
  with the card's location.
- `_merge_entries` puts exported `realizes` entries into their file's sidecar. A path with no card gets a
  sidecar without Markdown, which is listed.
- `_entry_states` counts exported entries by MIK-R03 state at the paired commit (`current`, `stale`,
  `stale:path-absent`).
- `_require_valid` runs `validate_tree(..., conversion=True)`. Any refusing violation raises
  `ConversionRefused` naming every failing file. The report records the refusing and report-only counts.
- `_report` returns the before and after counts: files, rows, references, targets by kind, covered
  ranges, references keeping anchor text, unresolved targets by reason, invariants, families,
  realizations, revision depths and realization states. It also lists the fallback cards, the
  abbreviated anchor commits, the stray citation rows, the `governingOverview` mismatches, the path
  mismatches, the residual metadata keys, the escaped-marker files and every unresolved target.

### Conventions

- The documents are serialized through `canonical_text` after `parse_document` has accepted them, so
  every written JSON file is in the MIK-R21 canonical format.
- `route_of` and `nearest_overview` are shared with `crossing_sync` (the marker subjects).

### Invariants And Boundaries

- **The conversion is deterministic and version-pinned (rule 6).** `CONVERSION_FORMAT_VERSION = "1"` is
  the one version this build reproduces byte for byte. `test_conversion_format_version_1_reproduces_its_pinned_bytes`
  pins version 1's complete output over the fixture tree (a golden digest, `2e3b3110…`). Any change that
  alters that output (in the cards, the citations, the export, the marker escaping, or the shipped
  extractor and its grammars) ships as a new version, never as version 1 (review R1 finding 2, resolved).
  This master drops no version.
- **A refused conversion writes nothing:** this module returns bytes, and only the CLI writes, after
  validation.
- **Converting an already converted tree is a no-op.**
- It authors no knowledge: no invariant is invented from prose, and every reference note is the row's own
  finding.
- On the real repository (clones at memory `2285b3b2e`, code `cd3e943d`) the conversion wrote 5,184 files:
  19,276 references, 86 unresolved targets, 94 invariants, 14 families and 178 realizations. Two clones
  are byte-identical, and a clone converted at a different paired commit is byte-identical too
  (reviewer), because every card is anchored at its own verified commit.

### Todos

Rule 2's fallback cards (none on the real tree) are the only cards whose output depends on the paired
code tree. The commit route's converted base and the crossing sync choose that tree differently (see
`base.py`).

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

The entry point, its version pin and its steps.

- The pinned version and the rule that a changed output ships as a new version. [1]
- An unsupported version is refused. [2]
- The inputs: files, database, and the converted state the marker decides. [3]
- The anchor commit: exact, prefix-resolved, or the listed fallback; an ambiguous prefix refuses. [4]
- Cards become Markdown plus a file or route sidecar. [5]
- The per-card audit, including the governing-overview and path mismatches. [6]
- Exported entries join their file's sidecar; a path without a card gets a sidecar without Markdown. [7]
- The whole tree is validated before anything is returned for writing. [8]
- The conversion's steps, the no-op and the marker. [9]
- The report's measures. [10]
- Determinism, the version refusal and the no-op. [11]
- Version 1's pinned bytes. [12]
- A refused conversion writes nothing and names what failed. [13]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
