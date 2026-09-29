# mcp/src/agents_remember/memory/conversion/convert.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/conversion/convert.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `../overview.md` |

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

The entry point, its version pin and its steps.

| Finding | Anchor | Source |
| --- | --- | --- |
| The pinned version and the rule that a changed output ships as a new version. | `CONVERSION_FORMAT_VERSION`; `SUPPORTED_VERSIONS` | mcp/src/agents_remember/memory/conversion/convert.py:44-51 |
| An unsupported version is refused. | `require_version`; `ConversionVersionError` | mcp/src/agents_remember/memory/conversion/convert.py:91-100; mcp/src/agents_remember/memory/conversion/convert.py:56-57 |
| The inputs: files, database, and the converted state the marker decides. | `MemoryInput` | mcp/src/agents_remember/memory/conversion/convert.py:68-78 |
| The anchor commit: exact, prefix-resolved, or the listed fallback; an ambiguous prefix refuses. | `_anchor_commit` | mcp/src/agents_remember/memory/conversion/convert.py:177-206 |
| Cards become Markdown plus a file or route sidecar. | `_convert_cards` | mcp/src/agents_remember/memory/conversion/convert.py:233-286 |
| The per-card audit, including the governing-overview and path mismatches. | `_audit_card`; `nearest_overview` | mcp/src/agents_remember/memory/conversion/convert.py:289-309; mcp/src/agents_remember/memory/conversion/convert.py:117-127 |
| Exported entries join their file's sidecar; a path without a card gets a sidecar without Markdown. | `_merge_entries` | mcp/src/agents_remember/memory/conversion/convert.py:312-329 |
| The whole tree is validated before anything is returned for writing. | `_require_valid`; `ConversionRefused` | mcp/src/agents_remember/memory/conversion/convert.py:368-384; mcp/src/agents_remember/memory/conversion/convert.py:60-65 |
| The conversion's steps, the no-op and the marker. | `convert_memory` | mcp/src/agents_remember/memory/conversion/convert.py:387-431 |
| The report's measures. | `_report` | mcp/src/agents_remember/memory/conversion/convert.py:434-479 |
| Determinism, the version refusal and the no-op. | `test_conversion_is_deterministic_version_pinned_and_a_no_op_once_converted` | mcp/tests/test_knowledge_conversion.py:222-263 |
| Version 1's pinned bytes. | `test_conversion_format_version_1_reproduces_its_pinned_bytes`; `VERSION_1_FIXTURE_DIGEST` | mcp/tests/test_knowledge_conversion.py:349-354; mcp/tests/test_knowledge_conversion.py:346-346 |
| A refused conversion writes nothing and names what failed. | `test_a_refused_conversion_writes_nothing_and_names_what_failed` | mcp/tests/test_knowledge_conversion.py:266-303 |

## Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
