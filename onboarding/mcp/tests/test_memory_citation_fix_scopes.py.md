# mcp/tests/test_memory_citation_fix_scopes.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_memory_citation_fix_scopes.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `723fd2f1becc130d85d7a6b285b93115be0df852`                                        |
| lastVerifiedCommitDate | 2026-09-13T02:07:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Document-scoped citation repair isolation and normalization, plus the refusal to retarget a claim across the tree while its cited file is still live or its continuity is unproven.

## Code Commentary

### Logic

A scoped repair leaves another document byte-identical. Invalid exact paths refuse before discovery or source acquisition. Expanded source ranges deduplicate and a second run writes nothing. A malformed source segment blocks normalization while retaining the original evidence and typed finding.

`LiveCitedFileRetargetTests` records the production defect and pins BOTH refusal directions on one tree shape: a claim cited two adjacent tool names in `mcp/tools/base.py` and the tuple holding them was relocated while the cited file kept existing, so the wider-tree lookup found each name's single definition — the registrar functions that declared them — and rebound the claim to a different fact that never supported it. An anchor that left a live cited file is now declined as `anchor_left_live_file`; a deleted cited file whose extent is not readable at the card's stamp is declined as `anchor_continuity_unproven`; the legitimate relocation still repairs once the cited file is gone and continuity holds; and a mention rebound to that name's declaration is declined as `anchor_kind_changed` (the `PUBLIC_TOOLS` tuple mention versus the `@server.tool()` registrar definition). `DocumentScopeTests._two_failing_cards` was rewritten to build real provenance: `kernel/gone.py` held both anchors at the recorded stamp, that stamp is committed, the file is then deleted, and both cards carry that stamp. The four existing scoped-fix tests remain.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Scope is a write boundary in a shared memory worktree. Failure to normalize must not delete the malformed claim or broaden to neighboring documents. An exact name match elsewhere is not by itself a safe retarget: the cited file must be gone and the extent the claim was verified against must be readable at its stamp with the same kind, or the claim is declined instead of rebound.

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
| An anchor that left a still-existing cited file is declined instead of retargeted. | `test_an_anchor_that_left_a_live_cited_file_is_declined_not_retargeted` | mcp/tests/test_memory_citation_fix_scopes.py:46-57 |
| A deleted cited file without continuity at the stamp is declined. | `test_a_deleted_cited_file_without_provable_continuity_is_declined` | mcp/tests/test_memory_citation_fix_scopes.py:59-69 |
| The same anchor relocates once the cited file is gone and continuity holds. | `test_the_same_anchor_relocates_once_the_cited_file_is_gone` | mcp/tests/test_memory_citation_fix_scopes.py:71-78 |
| A mention rebound to that name's declaration is declined as a kind change. | `test_a_mention_rebound_to_that_names_declaration_is_declined` | mcp/tests/test_memory_citation_fix_scopes.py:80-109 |
| Two anchors that left one cited file, each still declared where the move put it. | "    def _two_failing_cards(self) -> None:" | mcp/tests/test_memory_citation_fix_scopes.py:120-145 |
| A scoped fix leaves every other document byte identical. | `test_a_scoped_fix_leaves_every_other_document_byte_identical` | mcp/tests/test_memory_citation_fix_scopes.py:147-161 |
| Invalid exact paths refuse without memory discovery or source acquisition. | `test_invalid_exact_paths_refuse_without_memory_discovery_or_source_acquisition` | mcp/tests/test_memory_citation_fix_scopes.py:163-199 |
| Expanded sources are deduplicated and the second run is byte identical. | `test_expanded_sources_are_deduplicated_and_the_second_run_is_byte_identical` | mcp/tests/test_memory_citation_fix_scopes.py:205-240 |
| A malformed source segment blocks normalisation without deleting evidence. | `test_a_malformed_source_segment_blocks_normalisation_without_deleting_evidence` | mcp/tests/test_memory_citation_fix_scopes.py:242-270 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded the new `LiveCitedFileRetargetTests` class, which pins both refusal directions on one tree shape — `anchor_left_live_file` while the cited file exists, `anchor_continuity_unproven` when the extent is not readable at the stamp, `anchor_kind_changed` for a mention rebound to that name's declaration — while the legitimate relocation still repairs once the cited file is gone. Also recorded that `_two_failing_cards` now commits the verified `kernel/gone.py` tree and deletes it so both card stamps carry real provenance, and corrected every reference range to the measured source. Verification metadata remains closeout-owned.

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
