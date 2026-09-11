# mcp/tests/test_memory_citation_fix.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_fix.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

On-disk code/memory tree and assertion helpers for citation-fixer consumers.

## Code Commentary

### Logic

Tree creates temporary source and onboarding files and invokes scoped check/fix boundaries. TreeCase provides repaired/declined/clean assertions. The frozen no-discovery helper supports explicit scoped source acquisition. There are no retained repair-class or write-guard tests in this file.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Historical pure-move/rename/deletion/ambiguity prose describes earlier tests, not current standalone protection. Helpers must not manufacture semantic similarity approval.

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
| Frozen no discovery. | `_frozen_no_discovery` | mcp/tests/test_memory_citation_fix.py:59-92 |
| Document. | `document` | mcp/tests/test_memory_citation_fix.py:95-97 |
| Filler. | `filler` | mcp/tests/test_memory_citation_fix.py:100-101 |
| Tree. | `Tree` | mcp/tests/test_memory_citation_fix.py:104-145 |
| Treecase. | `TreeCase` | mcp/tests/test_memory_citation_fix.py:148-164 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Corrected dry-run write accounting and reconciled the pre-existing split-test inventory with its actual source owners while preserving the related behavioral routes. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
