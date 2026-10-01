# mcp/tests/test_knowledge_conversion.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R24 rules 1–4 and 6: the conversion command over fixture cards and a legacy database.** Six cases
in the `unit-regression` lane. It also carries the evidence-only back-to-prose renderer (`render_legacy`),
which lives here, beside its only consumer, rather than in the product (review R1 finding 7).

## Code Commentary

### Logic

- `test_a_card_becomes_prose_one_evidence_section_and_numbered_references` checks:
  - metadata, Update History and tables are gone, and `signals[0]` is escaped;
  - there is one `## Evidence` section, and placeholder sentences stay as prose;
  - symbol targets with covered ranges, a quoted anchor's range, the unresolved removed path and the range
    past the end;
  - the test, file and external targets;
  - notes that keep unbound anchor text byte for byte;
  - the route sidecar;
  - the report's counts, fallback card, governing mismatch, abbreviated commit and stray row
    (`_assert_listed`).
- `test_the_database_exports_head_records_and_entries_in_their_recorded_blobs` checks:
  - head revision depth, statement, conditions without hand-off lines, and origin (including a leaf
    learned from a document path);
  - `legacy-unassessed`, family members and `routes: []`;
  - entries in their recorded blobs, and `incidental` written as `support`;
  - a Markdown-less sidecar for the deleted file, and realization states.
- `test_conversion_is_deterministic_version_pinned_and_a_no_op_once_converted` runs the CLI: `--version 2`
  refuses and writes nothing, two clones convert byte-identically, a rerun is a no-op, and
  `knowledge-validate` passes on the committed conversion.
- `test_a_refused_conversion_writes_nothing_and_names_what_failed` checks three refusals:
  - a colliding entry ID refuses through the CLI (exit 1, both legacy claims named), and the tree is
    unchanged;
  - an ambiguous abbreviated anchor commit refuses naming the card (`failing == (other card,)`);
  - a validation refusal names the failing sidecar.
- `test_a_converted_card_renders_back_to_its_content_without_history`: the back-to-prose render restores
  the prose and the anchor text kept in notes.
- `test_conversion_format_version_1_reproduces_its_pinned_bytes`: the SHA-256 over every converted path
  and byte (`conversion_digest`) equals `VERSION_1_FIXTURE_DIGEST`.

### Conventions

- The fixture comes from `knowledge_conversion_test_support`, and each case converts in `tmp_path`.

### Invariants And Boundaries

- **The golden digest pins conversion-format version 1.** If it changes, the change must ship as a new
  version, never as a new digest for `1` (the comment beside the constant).

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

The cases and the renderer.

- Rule 1 and 2 over every row case. [1]
- Rule 4, the export. [2]
- Rule 6, determinism, the version refusal and the no-op. [3]
- A refused conversion writes nothing. [4]
- Back to prose. [5]
- The version 1 golden digest. [6]
- Its lane row. [7]

### Cross-Repo References

No meaningful cross-repo references found: the fixtures are `tmp_path` Git repositories built by the tests themselves.

No cross-repo boundary is crossed by this file.
