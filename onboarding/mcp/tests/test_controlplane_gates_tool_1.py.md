# mcp/tests/test_controlplane_gates_tool_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_controlplane_gates_tool_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                        |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Gate decision attribution and lifecycle admission tests.

## Code Commentary

### Logic

The public tool records deciding actor and surface, refuses owner self-approval and missing required reviewer verdicts, and expires an older open lifecycle gate. Default lifecycle waiting returns the developer decision and note; a mismatched explicit lifecycle refuses before creating a gate.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Refused decisions leave the durable gate open. Tests use injected stores and timing rather than creating real user approvals.

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
| Create then decide records attribution. | `test_create_then_decide_records_attribution` | mcp/tests/test_controlplane_gates_tool_1.py:18-28 |
| Orchestration decision rejects owner self approval. | `test_orchestration_decision_rejects_owner_self_approval` | mcp/tests/test_controlplane_gates_tool_1.py:30-44 |
| Orchestration decision requires verdict when policy requires it. | `test_orchestration_decision_requires_verdict_when_policy_requires_it` | mcp/tests/test_controlplane_gates_tool_1.py:46-62 |
| Create expires previous open lifecycle gate. | `test_create_expires_previous_open_lifecycle_gate` | mcp/tests/test_controlplane_gates_tool_1.py:64-78 |
| Lifecycle gate default returns after developer decision. | `test_lifecycle_gate_default_returns_after_developer_decision` | mcp/tests/test_controlplane_gates_tool_1.py:80-120 |
| Lifecycle gate rejects explicit lifecycle mismatch. | `test_lifecycle_gate_rejects_explicit_lifecycle_mismatch` | mcp/tests/test_controlplane_gates_tool_1.py:122-134 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
