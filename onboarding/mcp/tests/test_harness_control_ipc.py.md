# mcp/tests/test_harness_control_ipc.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_harness_control_ipc.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`                                        |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Private harness IPC identity, lifecycle and receipt-loss contracts.

## Code Commentary

### Logic

Actual private sockets expose status and queued withdrawal with restrictive directory/socket permissions. Lost outer receipt reconciles retained truth with one adapter submit; a public duplicate also preserves the original payload and one write. Exact endpoint identity and malformed-request refusals remain enforced.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

IPC ambiguity does not authorize resend or a control fallback. Native adapter behavior is doubled while the local socket and public routing paths are real.

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
| Private lifecycle status and withdraw round trip. | `test_private_lifecycle_status_and_withdraw_round_trip` | mcp/tests/test_harness_control_ipc.py:63-130 |
| Outer socket lost receipt reconciles retained known truth. | `test_outer_socket_lost_receipt_reconciles_retained_known_truth` | mcp/tests/test_harness_control_ipc.py:132-171 |
| Public duplicate returns retained result with one adapter call. | `test_public_duplicate_returns_retained_result_with_one_adapter_call` | mcp/tests/test_harness_control_ipc.py:173-272 |
| Private endpoint exact identity and submission. | `test_private_endpoint_exact_identity_and_submission` | mcp/tests/test_harness_control_ipc.py:276-312 |
| Malformed ipc request is rejected without control fallback. | `test_malformed_ipc_request_is_rejected_without_control_fallback` | mcp/tests/test_harness_control_ipc.py:314-334 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-13T13:08+02:00 — L23 full-Dagger stability repair: documented the duplicate-submit
  test's five-second synchronization margin; ordering and production IPC behavior are unchanged.
  Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
