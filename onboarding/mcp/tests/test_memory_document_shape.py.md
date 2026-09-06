# mcp/tests/test_memory_document_shape.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_document_shape.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `201b0599e5d79049252033c7b737df631135b11d` |
| lastVerifiedCommitDate | 2026-08-10T13:54:43+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Memory table parsing and history timestamp repair boundaries.

## Code Commentary

### Logic

Windows citation cells keep their three columns and fenced diffs are valid content. Missing cells report their original text. Mixed timezone frames are caught and refused for sorting; newly added naive timestamps fail within the closing diff, while a renamed old document is not treated as newly authored.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

History repair may not guess an offset or reorder incomparable timestamps. Existing examples and source evidence must survive a style check.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| The same windows cell in a three column table keeps its columns. | `test_the_same_windows_cell_in_a_three_column_table_keeps_its_columns` | mcp/tests/test_memory_document_shape.py:88-98 |
| A diff quoted in a fenced block is the document working. | `test_a_diff_quoted_in_a_fenced_block_is_the_document_working` | mcp/tests/test_memory_document_shape.py:100-101 |
| A missing cell is reported. | `test_a_missing_cell_is_reported` | mcp/tests/test_memory_document_shape.py:111-115 |
| The live mixed frame pair is caught instead of passing silently. | `test_the_live_mixed_frame_pair_is_caught_instead_of_passing_silently` | mcp/tests/test_memory_document_shape.py:128-133 |
| The fixer refuses to sort a section that mixes frames. | `test_the_fixer_refuses_to_sort_a_section_that_mixes_frames` | mcp/tests/test_memory_document_shape.py:135-144 |
| A naive bullet this closeout adds fails. | `test_a_naive_bullet_this_closeout_adds_fails` | mcp/tests/test_memory_document_shape.py:172-188 |
| A renamed document is not treated as newly written. | `test_a_renamed_document_is_not_treated_as_newly_written` | mcp/tests/test_memory_document_shape.py:190-196 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-10T00:00+02:00 — 260731-EFA-L9 follow-up: the default-style surface assertion now includes entity-catalog alignment so the full suite proves registration of the new fail-fast preflight check. Verification metadata remains pinned until closeout stamps the code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
