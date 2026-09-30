# mcp/tests/test_knowledge_conversion.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_conversion.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `overview.md` |

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

The cases and the renderer.

| Finding | Anchor | Source |
| --- | --- | --- |
| Rule 1 and 2 over every row case. | `test_a_card_becomes_prose_one_evidence_section_and_numbered_references` | mcp/tests/test_knowledge_conversion.py:75-159 |
| Rule 4, the export. | `test_the_database_exports_head_records_and_entries_in_their_recorded_blobs` | mcp/tests/test_knowledge_conversion.py:176-219 |
| Rule 6, determinism, the version refusal and the no-op. | `test_conversion_is_deterministic_version_pinned_and_a_no_op_once_converted` | mcp/tests/test_knowledge_conversion.py:222-263 |
| A refused conversion writes nothing. | `test_a_refused_conversion_writes_nothing_and_names_what_failed` | mcp/tests/test_knowledge_conversion.py:266-303 |
| Back to prose. | `test_a_converted_card_renders_back_to_its_content_without_history`; `render_legacy` | mcp/tests/test_knowledge_conversion.py:306-330; mcp/tests/test_knowledge_conversion.py:431-454 |
| The version 1 golden digest. | `conversion_digest`; `VERSION_1_FIXTURE_DIGEST`; `test_conversion_format_version_1_reproduces_its_pinned_bytes` | mcp/tests/test_knowledge_conversion.py:333-339; mcp/tests/test_knowledge_conversion.py:346-346; mcp/tests/test_knowledge_conversion.py:349-354 |
| Its lane row. | "mcp/tests/test_knowledge_conversion.py" | mcp/tests/test-evidence-lanes.toml:113-113 |

## Cross-Repo References

No meaningful cross-repo references found: the fixtures are `tmp_path` Git repositories built by the tests themselves.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`test-evidence-lanes.toml`) moved with the leaf's inserted lines: 1 row(s) re-pointed by the installed fixer (its generated bullets kept). No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:26:55+00:00: Generated citation repair: "mcp/tests/test_knowledge_conversion.py" repointed to mcp/tests/test-evidence-lanes.toml:113-113. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
