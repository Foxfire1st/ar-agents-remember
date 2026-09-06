# mcp/tests/test_direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Existing-code direct landing with memory content and ledger publication.

## Code Commentary

### Logic

A foreign requested code commit refuses before dereference. Preview reports would-land without changing any file. Apply verifies the current series HEAD, creates separate memory-content and ledger commits and records the exact code/memory mapping.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The local wrapper exercises below the independently owned scheduling fence. This case does not imply route-review acceptance, creation of a new code commit or permission to bypass production admission.

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
| Direct landing verifies code commit then ledger. | `test_direct_landing_verifies_code_commit_then_ledger` | mcp/tests/test_direct_landing.py:164-243 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-26T15:20+02:00 — Replaced the obsolete conflicting-mapping refusal claim with the
  current ledger-history contract: exact-current re-land is idempotent, while a historical
  same-code row is superseded by a recovered memory-only change without losing audit history.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: forced preview/landed results through the closed public outcome model. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T11:29+02:00 — 260821-CLIVE-L1 candidate12 rebind: corrected the
  overbroad explicit-message claim and recorded internal-memory omission as typed not-applicable,
  followed by the existing mutation-time `direct-landing-memory-required` refusal. Bound to reviewed
  candidate tree `8f03b256fe24aa77262da805f1538ee39ccb4dd6`, full diff SHA
  `ccb36a898b455cd67ca00c378e5ba0f18851be01faf3d26eced3b9af062f429e`, same-reviewer PASS;
  verification metadata remains pinned until governed closeout.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the direct landing operation and
  branch-addressed route-review binding (L16-R6/R7/R8/R9); covers the policy gate, commit
  verification, pre-commit candidate-tree gate, idempotent re-land, ledger conflict, and the
  recovery-naming refusal dialect. Verified at code commit a9d50e08.