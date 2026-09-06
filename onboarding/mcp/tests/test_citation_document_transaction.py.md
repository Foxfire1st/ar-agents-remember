# mcp/tests/test_citation_document_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_citation_document_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `b34f4a59562b76a3e2413027468e0f699117b36f` |
| lastVerifiedCommitDate | 2026-09-06T06:31:12+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Actual citation-fixer document transaction and conflict isolation.

## Code Commentary

### Logic

Mixed accepted and declined claims publish only accepted edits and history. Preview binds the same complete-batch digest later published; two cells on one line keep original offsets. Concurrent document changes refuse that whole document while another batch can publish; replace failure and stale explicit snapshots preserve original bytes.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

CRLF and append-only history remain intact. Observed interleavings establish the fixer contract without claiming an operating-system compare-and-swap primitive.

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
| Mixed claims publish only the accepted edit and history. | `test_mixed_claims_publish_only_the_accepted_edit_and_history` | mcp/tests/test_citation_document_transaction.py:76-92 |
| Preview digest matches later publication and binds the complete batch. | `test_preview_digest_matches_later_publication_and_binds_the_complete_batch` | mcp/tests/test_citation_document_transaction.py:95-111 |
| Two prose source cells on one line keep their original offsets. | `test_two_prose_source_cells_on_one_line_keep_their_original_offsets` | mcp/tests/test_citation_document_transaction.py:114-127 |
| Observed conflict refuses the whole document and preserves other batches. | `test_observed_conflict_refuses_the_whole_document_and_preserves_other_batches` | mcp/tests/test_citation_document_transaction.py:141-173 |
| Atomic replace failure keeps the original document. | `test_atomic_replace_failure_keeps_the_original_document` | mcp/tests/test_citation_document_transaction.py:176-197 |
| Crlf document bytes and history line endings survive. | `test_crlf_document_bytes_and_history_line_endings_survive` | mcp/tests/test_citation_document_transaction.py:200-210 |
| Stale explicit snapshot refuses the actual scoped fixer. | `test_stale_explicit_snapshot_refuses_the_actual_scoped_fixer` | mcp/tests/test_citation_document_transaction.py:213-224 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Created the production-owner transaction regression card, preserving exact interference, refusal and accounting boundaries without claiming OS-level compare-and-swap. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

