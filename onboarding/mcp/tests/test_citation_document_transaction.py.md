# mcp/tests/test_citation_document_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_citation_document_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `723fd2f1becc130d85d7a6b285b93115be0df852` |
| lastVerifiedCommitDate | 2026-09-13T02:07:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Actual citation-fixer document transaction and conflict isolation.

## Code Commentary

### Logic

Mixed accepted and declined claims publish only accepted edits and history. Preview binds the same complete-batch digest later published; two cells on one line keep original offsets. Concurrent document changes refuse that whole document while another batch can publish; replace failure and stale explicit snapshots preserve original bytes.

The `Scenario` fixture now carries a `stamp` field and a static `git(root, *args)` helper that raises on a non-zero exit, and `Scenario.card` writes a metadata table carrying `| lastVerifiedCommitHash | \`{self.stamp}\` |` above the citation header. The `scenario` fixture writes the VERIFIED tree first — `src/gone.py`/`unique` and `src/missing.py`/`another` held the anchors — git-inits and commits it, records the stamp, and only then deletes both files, so the mixed-claim transaction test still exercises an accepted edit alongside a claim declined by the continuity rule rather than by a missing source.

The file also carries a second, independent transaction: **migration**, driven through the real `migrate_onboarding_root` entry point over the same continuity authority. Its `Migration` fixture is a code tree plus a superseded three-column card (`Finding | Citations | Source Path`), with `source`/`stamp`/`card`/`migrate`/`row` helpers and a `build_migration` constructor. Three cases pin the reachable behaviour: a live cited file that no longer holds the anchor declines the row as `anchor_left_live_file` and the pointer is **not** moved; a gone cited file is refused far earlier as `source_unresolvable` (parametrized over a stamped and an unstamped card, i.e. both origin shapes) with the row's own evidence retained; and a deliberately-labelled **seam test** monkeypatches `migration.row_paths` to carry an unresolvable spelling through, reaching the two branches production cannot currently reach — an unproven origin declines as `anchor_continuity_unproven`, and a stamped kind-preserving relocation converts. That seam test's docstring states in its own words that production cannot reach those branches and that its value is **regression protection only**, so a green run must not be read as end-to-end coverage of a relocated file.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance. The migration seam test declares its own limitation at the point of use; keep that declaration when the test is edited.

### Invariants And Boundaries

CRLF and append-only history remain intact. Observed interleavings establish the fixer contract without claiming an operating-system compare-and-swap primitive. A declined claim in the mixed batch is declined under the continuity rule: the card names a stamp whose tree still held the anchor, while the current tree no longer does. The fixtures build provenance through Git, so no test asserts a semantic-similarity approval the fixer must not invent. **A green migration section is not end-to-end relocation coverage:** the only relocation refusal production reaches is `anchor_left_live_file`, because `row_paths`/`plan_row` refuse a gone source as `source_unresolvable` before placement; the continuity branches are pinned through a declared seam, not through the entry point.

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
| Scenario fixture: code/onboarding roots, the recorded stamp. | `Scenario` | mcp/tests/test_citation_document_transaction.py:41-78 |
| One Git command per root, failing loudly on a non-zero exit. | "    def git(root: Path, *args: str) -> str:" | mcp/tests/test_citation_document_transaction.py:48-54 |
| A card writes its metadata stamp above the citation header. | "    def card(self, name: str, *rows: str) -> Path:" | mcp/tests/test_citation_document_transaction.py:56-67 |
| The verified tree is committed and stamped before both cited files are deleted. | `scenario` | mcp/tests/test_citation_document_transaction.py:79-111 |
| Mixed claims publish only the accepted edit and history. | `test_mixed_claims_publish_only_the_accepted_edit_and_history` | mcp/tests/test_citation_document_transaction.py:112-130 |
| Preview digest matches later publication and binds the complete batch. | `test_preview_digest_matches_later_publication_and_binds_the_complete_batch` | mcp/tests/test_citation_document_transaction.py:131-149 |
| Two prose source cells on one line keep their original offsets. | `test_two_prose_source_cells_on_one_line_keep_their_original_offsets` | mcp/tests/test_citation_document_transaction.py:150-175 |
| Observed conflict refuses the whole document and preserves other batches. | `test_observed_conflict_refuses_the_whole_document_and_preserves_other_batches` | mcp/tests/test_citation_document_transaction.py:176-211 |
| Atomic replace failure keeps the original document. | `test_atomic_replace_failure_keeps_the_original_document` | mcp/tests/test_citation_document_transaction.py:212-235 |
| Crlf document bytes and history line endings survive. | `test_crlf_document_bytes_and_history_line_endings_survive` | mcp/tests/test_citation_document_transaction.py:236-248 |
| Stale explicit snapshot refuses the actual scoped fixer. | `test_stale_explicit_snapshot_refuses_the_actual_scoped_fixer` | mcp/tests/test_citation_document_transaction.py:249-276 |
| The migration fixture: a code tree plus the superseded three-column card the transaction rewrites. | `Migration`; `build_migration`; "def migration_tree(tmp_path: Path) -> Migration:" | mcp/tests/test_citation_document_transaction.py:277-326; mcp/tests/test_citation_document_transaction.py:327-341; mcp/tests/test_citation_document_transaction.py:342-346 |
| A live cited file that lost the anchor declines the row as `anchor_left_live_file` and the pointer is not moved. | `test_migration_declines_a_claim_whose_anchor_left_a_live_cited_file` | mcp/tests/test_citation_document_transaction.py:347-374 |
| A gone cited file is refused earlier as `source_unresolvable`, both stamped and unstamped, with the row's evidence retained. | `test_migration_refuses_a_gone_cited_file_before_the_continuity_authority` | mcp/tests/test_citation_document_transaction.py:375-402 |
| A declared seam reaching the two production-unreachable continuity branches: unproven origin declines, stamped kind-preserving relocation converts. | `test_the_continuity_authority_decides_once_an_absent_source_reaches_placement` | mcp/tests/test_citation_document_transaction.py:403-462 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-13T02:05+02:00 — 260831-LOCR-L33 curator (delta after publish): recorded the new
  **migration** section, which drives the real `migrate_onboarding_root` entry point over the same
  continuity authority — a live cited file declines as `anchor_left_live_file` with the pointer
  unmoved; a gone cited file is refused earlier as `source_unresolvable` (parametrized over stamped
  and unstamped cards) with the row's evidence retained; and one deliberately-labelled **seam test**
  wraps `migration.row_paths` to reach the two branches production cannot currently reach (unproven
  origin → `anchor_continuity_unproven`; stamped kind-preserving relocation → converts). Recorded the
  seam test's own declaration that a green run is regression protection only and must not be read as
  end-to-end relocation coverage. Re-measured every reference range and made the decorator-inclusive
  ranges explicit (`scenario`, the parametrized conflict test, `migration_tree`). Verification
  metadata remains closeout-owned; no acceptance claim.

- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded that `Scenario` gained a `stamp` field and a `git` helper, that `Scenario.card` now writes a `lastVerifiedCommitHash` metadata row above the citation header, and that the `scenario` fixture writes and commits the verified tree holding both anchors before deleting `src/gone.py` and `src/missing.py` — so the mixed-claim transaction still proves an accepted edit beside a claim declined under the continuity rule. Corrected every reference range to the measured source. Verification metadata remains closeout-owned.

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Created the production-owner transaction regression card, preserving exact interference, refusal and accounting boundaries without claiming OS-level compare-and-swap. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.
