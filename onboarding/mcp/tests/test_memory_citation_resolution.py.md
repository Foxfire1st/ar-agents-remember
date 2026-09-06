# mcp/tests/test_memory_citation_resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Citation range, anchor and source-path resolution contracts.

## Code Commentary

### Logic

Whole identifier boundaries reject longer-name false matches while valid names and pooled ranges pass. Prose citations share table range/anchor errors, fenced examples are ignored and misplaced prose serialization in table cells is reported. Parent traversal is malformed; absent code-root context reports no-code-repository-root rather than a silent pass.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The resolver must preserve valid pooled claims while refusing escaped or unsupported sources. This is repository-owned resolution evidence, not an external documentation authority.

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
| 1 a word boundary is not satisfied by a longer identifier. | `test_1_a_word_boundary_is_not_satisfied_by_a_longer_identifier` | mcp/tests/test_memory_citation_resolution.py:112-123 |
| 1b the same names pass when the range really holds them. | `test_1b_the_same_names_pass_when_the_range_really_holds_them` | mcp/tests/test_memory_citation_resolution.py:125-131 |
| 4 two ranges one anchor are pooled not paired. | `test_4_two_ranges_one_anchor_are_pooled_not_paired` | mcp/tests/test_memory_citation_resolution.py:133-142 |
| A well formed citation resolves and passes. | `test_a_well_formed_citation_resolves_and_passes` | mcp/tests/test_memory_citation_resolution.py:153-160 |
| An out of bounds prose range fails with the shared code. | `test_an_out_of_bounds_prose_range_fails_with_the_shared_code` | mcp/tests/test_memory_citation_resolution.py:162-166 |
| An absent prose anchor fails with the shared code. | `test_an_absent_prose_anchor_fails_with_the_shared_code` | mcp/tests/test_memory_citation_resolution.py:168-170 |
| A citation inside a fence is not scanned. | `test_a_citation_inside_a_fence_is_not_scanned` | mcp/tests/test_memory_citation_resolution.py:172-175 |
| A cit written into a finding cell is reported. | `test_a_cit_written_into_a_finding_cell_is_reported` | mcp/tests/test_memory_citation_resolution.py:181-192 |
| A parent step can no longer reach a file at a shallower depth. | `test_a_parent_step_can_no_longer_reach_a_file_at_a_shallower_depth` | mcp/tests/test_memory_citation_resolution.py:198-205 |
| Without a code root the result says so instead of passing quietly. | `test_without_a_code_root_the_result_says_so_instead_of_passing_quietly` | mcp/tests/test_memory_citation_resolution.py:211-218 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
