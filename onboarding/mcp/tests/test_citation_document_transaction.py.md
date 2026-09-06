# mcp/tests/test_citation_document_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_citation_document_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `b34f4a59562b76a3e2413027468e0f699117b36f` |
| lastVerifiedCommitDate | 2026-09-06T06:31:12+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Area overview](overview.md)

## Purpose

Forces actual citation-fixer publication and conflict/accounting behavior using temporary code and memory files.

## Code Commentary

### Logic

`Scenario` calls the real fixer, repository source index and document transaction with a fixed clock. Cases cover declined-only and mixed batches, two accepted projections, multiple prose cells, whole-document conflict isolation, projection/lease/cell corruption, atomic replace failure, CRLF, scoped pooled normalization, missing input and stale expected snapshots. Interleaving hooks change actual document bytes or selected bindings at the owner boundary; they do not fabricate successful certificates.

### Conventions

The file has one owner and one mirrored card. Source coordinates below include decorators. The source-index lease and application write-scope authorization remain separate contracts.

### Invariants And Boundaries

The suite proves observed pre-publication conflicts, not exclusion of an uncooperative writer after the final read. Dry-run results are prospective; successful publication counts remain zero. Integration-lane classification does not make the fixture itself a full production closeout.

### Todos

No additional debt is claimed by this card.

## Docs References

No external Domain Documentation source is configured. The cited behavior is a repository-owned contract, without an external documentation claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

The concrete owners and forcing cases below support this file's contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| Apply and preview of a declined-only card leave bytes and successful counters untouched. | `test_a_declined_only_document_never_reaches_the_atomic_writer` | mcp/tests/test_citation_document_transaction.py:77-92 |
| Mixed accepted/declined claims publish only accepted bytes and history and converge on retry. | `test_mixed_claims_publish_only_the_accepted_edit_and_history` | mcp/tests/test_citation_document_transaction.py:95-111 |
| Two-cell previews and later writes share exact complete-batch digests. | `test_preview_digest_matches_later_publication_and_binds_the_complete_batch` | mcp/tests/test_citation_document_transaction.py:114-130 |
| Two prose cells retain independent offsets. | `test_two_prose_source_cells_on_one_line_keep_their_original_offsets` | mcp/tests/test_citation_document_transaction.py:133-146 |
| Six real interleaved document changes refuse one batch while an independent card publishes. | `test_observed_conflict_refuses_the_whole_document_and_preserves_other_batches` | mcp/tests/test_citation_document_transaction.py:159-192 |
| Corrupted projection snapshot, values or prior digest cannot publish. | `test_apply_rejects_a_projection_that_no_longer_binds_its_source_cell_or_lease` | mcp/tests/test_citation_document_transaction.py:195-213 |
| Changed lease identity or accepted cell value refuses before the writer. | `test_changed_publication_preconditions_refuse_before_writing` | mcp/tests/test_citation_document_transaction.py:216-237 |
| An actual atomic-writer replace failure preserves original bytes and cleans the temporary file. | `test_atomic_replace_failure_keeps_the_original_document` | mcp/tests/test_citation_document_transaction.py:240-261 |
| CRLF bytes, grouped history and complete digest survive and a second run is a no-op. | `test_crlf_document_bytes_and_history_line_endings_survive` | mcp/tests/test_citation_document_transaction.py:264-274 |
| Passing pooled evidence normalizes through the transaction without an exact-move projection. | `test_scoped_passing_pooled_evidence_normalises_without_unique_move_projection` | mcp/tests/test_citation_document_transaction.py:277-289 |
| Normalization does not overwrite a concurrent history change. | `test_normalisation_has_the_same_document_conflict_boundary` | mcp/tests/test_citation_document_transaction.py:292-310 |
| Remove/rename during apply or preview retains conflict evidence and reports null remaining findings. | `test_scoped_disappearance_preserves_the_conflict_payload_without_a_fictitious_recheck` | mcp/tests/test_citation_document_transaction.py:313-358 |
| A nonexistent initial document still refuses before index acquisition. | `test_initially_missing_scoped_input_still_refuses_before_source_acquisition` | mcp/tests/test_citation_document_transaction.py:361-374 |
| Real source changes invalidate an explicitly selected old snapshot. | `test_stale_explicit_snapshot_refuses_the_actual_scoped_fixer` | mcp/tests/test_citation_document_transaction.py:377-388 |
| Invalid lines and spans refuse instead of indexing other text. | `test_a_removed_or_invalid_source_site_refuses_instead_of_indexing_unrelated_text` | mcp/tests/test_citation_document_transaction.py:391-395 |

## Cross-Repo References

This file creates no cross-repository protocol. It composes local citation and file-publication owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| No separate cross-repository authority. | N/A | N/A |

## Update History

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Created the production-owner transaction regression card, preserving exact interference, refusal and accounting boundaries without claiming OS-level compare-and-swap. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

