# mcp/tests/test_memory_citation_fix_scopes.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_memory_citation_fix_scopes.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`                                        |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Document-scoped citation repair isolation and normalization.

## Code Commentary

### Logic

A scoped repair leaves another document byte-identical. Invalid exact paths refuse before discovery or source acquisition. Expanded source ranges deduplicate and a second run writes nothing. A malformed source segment blocks normalization while retaining the original evidence and typed finding.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Scope is a write boundary in a shared memory worktree. Failure to normalize must not delete the malformed claim or broaden to neighboring documents.

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
| A scoped fix leaves every other document byte identical. | `test_a_scoped_fix_leaves_every_other_document_byte_identical` | mcp/tests/test_memory_citation_fix_scopes.py:30-44 |
| Invalid exact paths refuse without memory discovery or source acquisition. | `test_invalid_exact_paths_refuse_without_memory_discovery_or_source_acquisition` | mcp/tests/test_memory_citation_fix_scopes.py:46-82 |
| Expanded sources are deduplicated and the second run is byte identical. | `test_expanded_sources_are_deduplicated_and_the_second_run_is_byte_identical` | mcp/tests/test_memory_citation_fix_scopes.py:88-123 |
| A malformed source segment blocks normalisation without deleting evidence. | `test_a_malformed_source_segment_blocks_normalisation_without_deleting_evidence` | mcp/tests/test_memory_citation_fix_scopes.py:125-153 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
