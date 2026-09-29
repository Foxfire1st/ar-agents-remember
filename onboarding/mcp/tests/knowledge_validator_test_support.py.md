# mcp/tests/knowledge_validator_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/knowledge_validator_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**Builds the converted fixture memory tree the MIK-R22 validator tests start from.** `fixture_tree_files()` assembles the MIK-R21 Doc14 §4 fixtures (`fixtures/knowledge_files`) into one converted tree: the layout marker; the invariant, family, decision and incident records; and the file and route sidecars of `direct_landing.py`, its test, `integrate.py` and the `worktrees` route, each beside its Markdown card. It is a helper module, not a test module (no `test_` prefix).

## Code Commentary

### Logic

- It adds the two invariants the fixtures name but do not define (`INV-R8M2TD`, `INV-C0VR4G`), so the tree is whole.
- `DIRECT_LANDING_MARKDOWN` carries markers `[1]`–`[7]` plus an escaped `\[9]`, an inline `signals[0]` code span and a fenced `journal[1]`, so the passing tree exercises the marker grammar.
- `CODE_PATHS` lists the real repository paths the anchors name; `code()` returns them as a `CodePathSet`.
- Helpers: `encode` (canonical bytes), `invariant_document`/`invariant_path`, `tree`, `edit_json` (a changed copy of one JSON file) and `write_tree` (materialise a tree on disk for the Git and CLI route tests).

### Conventions

- Every file is written through `canonical_text`, so the base tree passes `R22.1-canonical`.

### Invariants And Boundaries

- The assembled tree passes every registered rule with no violation (`test_converted_fixture_tree_passes_every_rule`).

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The fixture assembly and its helpers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The real code paths the anchors name. | `CODE_PATHS` | mcp/tests/knowledge_validator_test_support.py:27-27 |
| The card with markers, an escape, a code span and a fenced block. | `DIRECT_LANDING_MARKDOWN` | mcp/tests/knowledge_validator_test_support.py:37-54 |
| The converted fixture tree. | `fixture_tree_files` | mcp/tests/knowledge_validator_test_support.py:76-104 |
| Editing one JSON file and writing a tree to disk. | `edit_json`; `write_tree` | mcp/tests/knowledge_validator_test_support.py:115-122; mcp/tests/knowledge_validator_test_support.py:125-129 |

## Cross-Repo References

No meaningful cross-repo references found: the helper reads the repository's own fixtures.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
