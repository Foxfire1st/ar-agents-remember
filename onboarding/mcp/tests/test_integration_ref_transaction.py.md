# mcp/tests/test_integration_ref_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_ref_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Protected-ref transaction recovery after checkout-refresh refusal.

## Code Commentary

### Logic

The retained real-Git case injects an untracked file after ref CAS. Checkout refresh refuses while preserving both the new protected ref and concurrent file. Once the obstruction is resolved, retry refreshes the exact intended checkout rather than repeating arbitrary mutations.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Ref publication and checkout materialization are distinct stages. Recovery must retain user files and prove the original transaction identity.

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
| Post cas untracked file refuses checkout refresh and recovers exactly. | `test_post_cas_untracked_file_refuses_checkout_refresh_and_recovers_exactly` | mcp/tests/test_integration_ref_transaction.py:94-176 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.

- 2026-08-26T14:32+02:00 — Replaced the duplicate-code refusal regression with the required
  settings-only memory-history proof while retaining missing/unreachable/dropped-history and
  multi-prefix refusals. Verification remains closeout-owned.


- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: re-pointed imports to the
  worktrees/integration package and added the no-landed-mapping and unreachable-memory-content
  refusal proofs for `require_integrated_ledger_mapping`. Verified at code commit e5cb139f.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — No content impact: L5 extends the suite for the organizational-completion super-to-leaf ledger mapping; the documented transaction behavior is unchanged and the additions are covered by the new completion cards.

- 2026-08-16T08:12+02:00 — Dagger coverage repair: expanded exact transaction forcing across preparation races, both recovery sides, checkout refusal branches, and the durable-before-crash external retry order.
- 2026-08-16T05:18+02:00 — Dagger fixture repair: the checkout-refresh crash/retry case isolates queue publication/completion while retaining the real integration recovery and named-ref transaction owners under test.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created integration ref transaction forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
