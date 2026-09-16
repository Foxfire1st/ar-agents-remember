# mcp/tests/test_memory_citation_fix.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_fix.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `723fd2f1becc130d85d7a6b285b93115be0df852` |
| lastVerifiedCommitDate | 2026-09-13T02:07:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

On-disk code/memory tree and assertion helpers for citation-fixer consumers.

## Code Commentary

### Logic

Tree creates temporary source and onboarding files, invokes scoped check/fix boundaries, and now builds real Git provenance: `git` runs one command and raises `AssertionError` on a non-zero exit, `history` makes the code root a Git repository with a user config, `stamp` commits every source written so far and returns the resulting commit SHA, and `remove_source` unlinks one already-committed source so the move can be discovered. A fixture that expects a legitimate relocation must therefore create the verified tree first, because a relocation may only follow a name when the extent the claim was verified against is readable at that commit. `document` and `Tree.card` take an optional `stamp` that inserts a `| lastVerifiedCommitHash | \`<sha>\` |` row inside the metadata table — never below the citation header, where a bare row would parse as another claim — and `Tree.row` locates one citation row by finding the `CITATION_HEADER` line and stepping past header and delimiter, so card metadata can no longer shift the row index. TreeCase provides repaired/declined/clean assertions. The frozen no-discovery helper supports explicit scoped source acquisition. There are no retained repair-class or write-guard tests in this file.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The module docstring states a PURE MOVE is applied only when continuity is proved: the anchor kept its name, changed file, and the extent the claim was verified against is readable at its stamp with the same kind. RENAME, DELETION and AMBIGUOUS remain refused. Historical pure-move/rename/deletion/ambiguity prose describes earlier tests, not current standalone protection. Helpers must not manufacture semantic similarity approval.

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
| Frozen no discovery. | `_frozen_no_discovery` | mcp/tests/test_memory_citation_fix.py:65-98 |
| Document. | `document` | mcp/tests/test_memory_citation_fix.py:101-107 |
| Filler. | `filler` | mcp/tests/test_memory_citation_fix.py:110-111 |
| Tree. | `Tree` | mcp/tests/test_memory_citation_fix.py:114-191 |
| One Git command per root, failing loudly on a non-zero exit. | "    def git(self, root: Path, *args: str) -> str:" | mcp/tests/test_memory_citation_fix.py:142-149 |
| The code root is initialised, stamped by committing every source written so far, and one committed source can be removed so the move is discovered. | "    def history(self) -> None:"; "    def stamp(self) -> str:"; "    def remove_source(self, relative: str) -> None:" | mcp/tests/test_memory_citation_fix.py:151-155; mcp/tests/test_memory_citation_fix.py:157-166; mcp/tests/test_memory_citation_fix.py:168-170 |
| A citation row is located by the citation header, not by a fixed row index. | "    def row(self, relative: str, offset: int = 0) -> str:" | mcp/tests/test_memory_citation_fix.py:188-191 |
| Treecase. | `TreeCase` | mcp/tests/test_memory_citation_fix.py:194-214 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded the fixture module's new Git-provenance machinery — `Tree.git`/`history`/`stamp`/`remove_source` build and commit the verified tree so a relocation can only follow a name the claim's extent is readable for at that stamp — plus the optional `stamp` metadata row inserted inside the metadata table and the `CITATION_HEADER`-anchored `Tree.row` locator that replaced the fixed `FIRST_ROW` index. Reconciled every reference range against the current source; source inspection only, not a test run. Verification metadata remains closeout-owned.

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Corrected dry-run write accounting and reconciled the pre-existing split-test inventory with its actual source owners while preserving the related behavioral routes. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
