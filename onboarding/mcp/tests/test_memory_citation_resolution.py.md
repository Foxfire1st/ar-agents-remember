# mcp/tests/test_memory_citation_resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `723fd2f1becc130d85d7a6b285b93115be0df852` |
| lastVerifiedCommitDate | 2026-09-13T02:07:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Citation range, anchor and source-path resolution contracts, including canonical full/selected document validation, retained prepared-history provenance, and the support question asked of a mechanically projected range.

## Code Commentary

### Logic

Whole identifier boundaries reject longer-name false matches while valid names and pooled ranges pass. Prose citations share table range/anchor errors, fenced examples are ignored and misplaced prose serialization in table cells is reported. Parent traversal is malformed; absent code-root context reports no-code-repository-root rather than a silent pass. The style-surface regression covers both full and selected walks rejecting a symlinked outside document, while retained prepared provenance may anchor history for current bytes and rejects an unrelated history commit.

`MechanicallyProjectedRangeTests` records that a range the mechanical repair wrote is not evidence that the citation is current: the currency test is satisfied by construction by a projected range, because the projection chose the declaration it wrote. Its helpers `git`/`commit`/`card`/`projection_bullet`/`changed_construct` build a real generated Update History bullet through `deterministic_projection.history_bullet`. `test_a_projected_range_is_enforced_with_the_support_question_not_currency` asserts the projected item is **enforced, not surfaced**: `surfacedFindings == []`, exactly one finding, `severity == "error"`, `ok is False`, the no-git-view fail-closed fact (`_modified_onboarding_paths` is `None`, so every finding stays enforced), and it keeps every message assertion (no "the citation is current"; "NOT shown to be current", the generated bullet, "it now reads kernel/build.py:1-2", "does the construct the new range covers support", "mechanical anchor-range projection", "re-cite the location the claim is about", "only then advance the stamp"). `test_history_without_this_claims_bullet_keeps_the_currency_assertion` leaves the ordinary item untouched — one warning in `surfacedFindings`, `findings == []`, the currency assertion present — checked both for an ordinary history and for a bullet naming a different anchor.

### Conventions

This card describes the current candidate source after the CCR-L42 citation-surface additions; historical entries below record earlier test populations and do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The resolver must preserve valid pooled claims while refusing escaped or unsupported sources. A mechanically projected range must not be reported as a current citation: it is **enforced** (`severity == "error"`) with the support question, because evidence the check cannot verify must force an explicit disposition rather than sit in the report-only bucket a curator can read past. The ordinary evidence-change item keeps its `warning`, and the no-git-view path stays fail-closed. This is repository-owned resolution evidence, not an external documentation authority.

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
| 1 a word boundary is not satisfied by a longer identifier. | `test_1_a_word_boundary_is_not_satisfied_by_a_longer_identifier` | mcp/tests/test_memory_citation_resolution.py:116-127 |
| 1b the same names pass when the range really holds them. | `test_1b_the_same_names_pass_when_the_range_really_holds_them` | mcp/tests/test_memory_citation_resolution.py:129-135 |
| 4 two ranges one anchor are pooled not paired. | `test_4_two_ranges_one_anchor_are_pooled_not_paired` | mcp/tests/test_memory_citation_resolution.py:137-146 |
| A well formed citation resolves and passes. | `test_a_well_formed_citation_resolves_and_passes` | mcp/tests/test_memory_citation_resolution.py:157-164 |
| An out of bounds prose range fails with the shared code. | `test_an_out_of_bounds_prose_range_fails_with_the_shared_code` | mcp/tests/test_memory_citation_resolution.py:166-170 |
| An absent prose anchor fails with the shared code. | `test_an_absent_prose_anchor_fails_with_the_shared_code` | mcp/tests/test_memory_citation_resolution.py:172-174 |
| A citation inside a fence is not scanned. | `test_a_citation_inside_a_fence_is_not_scanned` | mcp/tests/test_memory_citation_resolution.py:176-179 |
| A cit written into a finding cell is reported. | `test_a_cit_written_into_a_finding_cell_is_reported` | mcp/tests/test_memory_citation_resolution.py:185-196 |
| A parent step can no longer reach a file at a shallower depth. | `test_a_parent_step_can_no_longer_reach_a_file_at_a_shallower_depth` | mcp/tests/test_memory_citation_resolution.py:202-209 |
| Without a code root the result says so instead of passing quietly. | `test_without_a_code_root_the_result_says_so_instead_of_passing_quietly` | mcp/tests/test_memory_citation_resolution.py:237-244 |

| Full and selected walks share canonical document validation; retained prepared history is accepted only when it is an ancestor and unrelated history is refused. | `test_full_and_selected_walks_share_canonical_document_validation`; `test_retained_prepared_commit_accepts_current_tree_and_rejects_other_history` | mcp/tests/test_memory_citation_resolution.py:215-235; mcp/tests/test_memory_citation_resolution.py:328-349 |
| A range the mechanical repair wrote is not evidence that the citation is current; the class also carries its own `git`/`commit`/`card`/`changed_construct` fixtures. | `MechanicallyProjectedRangeTests` | mcp/tests/test_memory_citation_resolution.py:352-491 |
| The real generated Update History bullet for this card's anchors, exactly as `--fix` writes it. | `MechanicallyProjectedRangeTests.projection_bullet` | mcp/tests/test_memory_citation_resolution.py:420-436 |
| A projected range is enforced at `severity="error"` with the support question, keeps `surfacedFindings` empty, fails the result, and pins the no-git-view fail-closed path. | `test_a_projected_range_is_enforced_with_the_support_question_not_currency` | mcp/tests/test_memory_citation_resolution.py:442-471 |
| History without this claim's bullet keeps the ordinary warning-level currency assertion. | `test_history_without_this_claims_bullet_keeps_the_currency_assertion` | mcp/tests/test_memory_citation_resolution.py:473-491 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-13T02:05+02:00 — 260831-LOCR-L33 curator (delta after publish): re-pointed
  `MechanicallyProjectedRangeTests`. The projected item moved from report-only to enforced, so the
  old assertion that it was *surfaced* at `severity: warning` is replaced: the test is renamed
  `test_a_projected_range_is_enforced_with_the_support_question_not_currency` and now asserts
  `surfacedFindings == []`, exactly one enforced finding, `severity == "error"`, `ok is False`, and
  the no-git-view fail-closed fact, while keeping every original message assertion. The companion
  test additionally asserts `findings == []` and `warning` for the ordinary item. Nothing was removed
  or weakened. Verification metadata remains closeout-owned; no acceptance claim.

- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded the new `MechanicallyProjectedRangeTests` class and both of its tests — a mechanically projected range is surfaced with the support question ("NOT shown to be current", the generated bullet, the new range, the construct question) instead of a currency assertion, while a history without this claim's bullet keeps the older currency assertion — and noted that severity deliberately stays `warning` because whether a projected range should block is an undecided policy call. Corrected every reference range to the measured source. Verification metadata remains closeout-owned. **Superseded by the entry above: the severity call is now made, and the projected item is enforced.**

- 2026-09-10T00:00+02:00 — CCR-L42 current-candidate curation: added the canonical-walk and retained-prepared-provenance regression coverage to the current test card; verification metadata remains closeout-owned.

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
