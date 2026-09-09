# mcp/tests/test_activation_admission_registered.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_activation_admission_registered.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-08T19:24:00+02:00 |
| lastVerifiedCommitHash | `602143bd1d48226f4d53b83ff7c5002a695dcdff` |
| lastVerifiedCommitDate | 2026-09-09T00:26:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Registered FastMCP proof for actionable atomic-series activation admission and read-only status
evidence.

## Code Commentary

### Logic

`RegisteredActivationAdmissionTests` builds temporary code/coordination roots and calls the real
registered `worktree_status`, `worktree_sync`, and `worktree_start` tools. The cases prove that
status exposes an active source-pair fact without mutating selector bytes, a foreign selected master
is named with a contract-bound `worktree_status` action, vacant and unreadable activation snapshots
remain distinct corrective evidence, oversized unreadable diagnostics retain a bounded parser-error
prefix, and persisted master edge mismatches retain expected/observed branch facts across both the
initial and authoritative reread paths. The unreadable-contract case also proves that a malformed
parser's 9099-character reason remains bounded in top-level and nested refusal detail while its
source bytes remain unchanged. The fixture is disposable; it does not prove a live control-plane
run or acceptance.

### Conventions

This file is integration evidence because it crosses the registered MCP transport. Its assertions
describe response shape and byte-preservation boundaries; collected counts and focused passes remain
worker evidence rather than Gate 5 certification.

### Invariants And Boundaries

- Selector/status projections remain read-only in the status and refusal paths.
- A logical `active` or `reconciling` selection is not treated as proof of a live process.
- Temporary fixture state cannot establish production scheduler, Dagger, or master-aggregate behavior.

## Docs References

No Domain Documentation entries are configured for this repository-owned integration fixture.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain evidence applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Registered status projects activation without mutation. | `test_registered_status_projects_activation_without_mutation` | mcp/tests/test_activation_admission_registered.py:154-175 |
| Foreign-holder refusal exposes blocker identity and contract-bound status action. | `test_registered_sync_refusal_names_foreign_holder_and_read_status` | mcp/tests/test_activation_admission_registered.py:177-215 |
| Vacant and unreadable snapshots remain distinct and unchanged. | `test_registered_sync_refusal_distinguishes_vacant_and_unreadable` | mcp/tests/test_activation_admission_registered.py:217-261 |
| Oversized unreadable detail is bounded in both status and sync projections without changing source bytes. | `test_registered_status_and_sync_bound_oversized_unreadable_detail` | mcp/tests/test_activation_admission_registered.py:263-316 |
| Startup edge mismatch retains expected and observed branch evidence. | `test_registered_start_refusal_reports_contract_edges` | mcp/tests/test_activation_admission_registered.py:318-365 |
| Authoritative startup reread preserves edge evidence when the contract drifts after upstream refresh. | `test_registered_start_reread_refusal_preserves_edges_and_guidance` | mcp/tests/test_activation_admission_registered.py:367-419 |
| Unreadable startup contracts retain the concrete parser reason in refusal and observed evidence, including bounded oversized parser detail and unchanged source bytes. | `test_registered_start_unreadable_contract_keeps_parser_reason` | mcp/tests/test_activation_admission_registered.py:421-494 |

## Cross-Repo References

No cross-repository implementation evidence is required for this disposable registered fixture.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture does not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-08T19:24:00+02:00 — CCR-L38 CQ04 preparation reconciled the registered oversized-parser proof and helper extraction into the seven current source cases, rebinding all test anchors to the current file. The public-boundary result is preparation evidence only; verification remains closeout-owned with no acceptance claim.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ01/CQ04 preparation rebound the registered fixture to its seven current source cases: bounded oversized activation detail, authoritative reread edge refusal, and concrete unreadable-contract parser evidence. Focused worker checks are retained as preparation evidence only; verification remains closeout-owned and no acceptance claim is made.
- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: created the one-to-one sidecar for the frozen registered activation/admission proof. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.
