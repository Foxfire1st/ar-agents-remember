# mcp/tests/test_knowledge_conversion_toolchain.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_conversion_toolchain.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R24 rules 5 and 9: the master line's toolchain reads the text format, and unconverted memory is read
as legacy-format and refused elsewhere once its official line is converted.** Five cases in the
`unit-regression` lane.

## Code Commentary

### Logic

- `test_read_ar_files_returns_legacy_format_or_resolved_references`:
  - an unconverted tree's file result is `legacy-format`, with no references or sidecar, and its knowledge
    section is `legacy-format`;
  - after conversion, the knowledge section read **through `read_ar_files`** is `recorded`, with index
    `complete`, and holds the exported invariant. This is the converted-tree coverage that replaced the
    displaced ICR-R19 route assertions (architect ruling). Since 260928-MIK-L01 the statement is read from
    the seed's leaf `rows` (the family-complete leaf read, MIK-R01) rather than the scope `items`;
  - the file result is `text/v2`, with the sidecar, numbered references, a filled-in own path, and an
    invariant target carrying its record summary.
- `test_references_are_checked_and_only_mechanical_moves_are_fixed`:
  - stale references are report-only (`findingCount` 0);
  - a quoted literal moved two lines down is re-found exactly once;
  - blobs are refreshed;
  - a changed body is left stale for the curator.
- `test_memory_quality_reads_the_converted_format`: the run is `ok`, `knowledge.converted` is present,
  the legacy-format checks are `not-applicable-converted`, and there is no drift check.
- `test_an_unconverted_leaf_is_refused_only_once_its_official_line_is_converted`: no refusal while the
  official line is unconverted; afterwards the refusal names the crossing sync and `worktree_sync`.
- `test_memory_init_creates_new_memory_in_the_text_format_only`: a new root gets the marker with exactly
  `LAYOUT_MARKER_TEXT` (`created`); a root holding a legacy card is `unconverted-existing-memory` and gets
  no marker.

### Conventions

- `_convert_in_place` converts a fixture memory tree in place through the product's own conversion (`convert_memory`, then `write_changed`).

### Invariants And Boundaries

- The rule 9 refusal case pins that nothing changes before the official line converts, the ruling that
  keeps every route unchanged before MIK-R37.

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

The cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| The read tool on both formats, with the converted knowledge section through the tool. | `test_read_ar_files_returns_legacy_format_or_resolved_references` | mcp/tests/test_knowledge_conversion_toolchain.py:42-84 |
| The reference check and fixer. | `test_references_are_checked_and_only_mechanical_moves_are_fixed` | mcp/tests/test_knowledge_conversion_toolchain.py:87-115 |
| Memory quality on a converted tree. | `test_memory_quality_reads_the_converted_format` | mcp/tests/test_knowledge_conversion_toolchain.py:118-135 |
| The rule 9 refusal. | `test_an_unconverted_leaf_is_refused_only_once_its_official_line_is_converted` | mcp/tests/test_knowledge_conversion_toolchain.py:138-167 |
| `memory_init` in the text format. | `test_memory_init_creates_new_memory_in_the_text_format_only` | mcp/tests/test_knowledge_conversion_toolchain.py:170-202 |
| Its lane row. | "mcp/tests/test_knowledge_conversion_toolchain.py" | mcp/tests/test-evidence-lanes.toml:115-115 |

## Cross-Repo References

No meaningful cross-repo references found: the fixtures are `tmp_path` Git repositories built by the tests themselves.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`test-evidence-lanes.toml`) moved with the leaf's inserted lines: 1 row(s) re-pointed by the installed fixer (its generated bullets kept). No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:26:59+00:00: Generated citation repair: "mcp/tests/test_knowledge_conversion_toolchain.py" repointed to mcp/tests/test-evidence-lanes.toml:115-115. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): MIK-R01 makes a converted tree's path seed the family-complete leaf read, so `test_read_ar_files_returns_legacy_format_or_resolved_references` reads the statement from `rows` instead of `items` (a one-line adaptation; the case's intent is unchanged). The Logic bullet says so; the rows were projected by the installed fixer.
- 2026-09-30T00:00:18+00:00: Generated citation repair: "mcp/tests/test_knowledge_conversion_toolchain.py" repointed to mcp/tests/test-evidence-lanes.toml:113-113. No content impact: mechanical anchor-range projection bound to citation source snapshot af78c18a536ac2f00d794dbac67f4d678cae173b43b31e0e7de2b8d520b727b6; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
