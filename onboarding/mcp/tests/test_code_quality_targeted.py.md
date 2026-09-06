# mcp/tests/test_code_quality_targeted.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_code_quality_targeted.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Targeted quality scope derived from exact changes and test ownership.

## Code Commentary

### Logic

The retained scenarios derive changed-file lint scope, reverse-import typing closure and direct/name-based test consumers. An ownerless new production module leaves selection incomplete and empty. Shared support selects its static import consumers; verification-package edits never become product coverage.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Incomplete ownership refuses rather than broadening to all tests. Coverage selection is diagnostic scope, not a demand to restore deleted tests or floors.

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
| Changed files closure and test subset are derived. | `test_changed_files_closure_and_test_subset_are_derived` | mcp/tests/test_code_quality_targeted.py:126-179 |
| Changed production module without owner refuses without broadening. | `test_changed_production_module_without_owner_refuses_without_broadening` | mcp/tests/test_code_quality_targeted.py:181-197 |
| Shared support change selects static import consumers. | `test_shared_support_change_selects_static_import_consumers` | mcp/tests/test_code_quality_targeted.py:199-212 |
| Verification package change never becomes product coverage. | `test_verification_package_change_never_becomes_product_coverage` | mcp/tests/test_code_quality_targeted.py:214-227 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): recorded the L19 exact-ownership
  recast — unowned production/unknown support/scripts-only changes now refuse with empty test
  populations (or refuse config before Gate 2), deleted tests resolve complete, and the suite
  forces the `repository-selector-result/v2` selector result and dashboard global-invalidation
  lanes. Verification is pinned to the owning commit.

- 2026-08-27T18:33+02:00 — Reconciled the suite with the dedicated child-environment/import-root
  owner; targeted product-versus-verification semantics are unchanged.
- 2026-08-27T14:04+02:00 — Added an explicit product-versus-verification fixture and regression
  proof that targeted scope never turns a changed Dagger/test-support package into product
  coverage or CRAP scope.
- 2026-08-26T10:44:52+02:00 — Rewrote the targeted-gate contract around canonical dependency ownership, typed selection reasons, global invalidation, and explicit fail-closed full-population fallback.

- 2026-08-24T21:23+02:00 — Added typed Dagger admission to targeted quality fixtures.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new targeted-derivation suite; content derived from
  the current worktree source. Verification metadata pinned until closeout
  stamps the 260731-EFA-L17 commit.
