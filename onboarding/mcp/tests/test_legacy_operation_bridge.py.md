# mcp/tests/test_legacy_operation_bridge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_legacy_operation_bridge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00|
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate | 2026-09-04T09:56:23+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Forces the isolated schema-1 lifecycle bridge.

## Code Commentary

### Logic

The suite proves inspect, migrate, resume, archive, identity mismatch, corrupt input, and bridge-removal behavior without a generic fallback.

### Conventions

Tests execute production owners and use shared builders only for canonical setup. Scenario-specific
differences remain in the test so fixtures do not become a parallel implementation.

### Invariants And Boundaries

- The suite preserves loud negative cases and exact identity/refusal assertions; it does not obtain
  green through a fallback, allowlist, or weakened production threshold.
- Dagger owns certifying execution. Any direct execution remains bounded diagnostic evidence only.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required for this repository-owned test contract. | `_byte_tree` | mcp/tests/test_legacy_operation_bridge.py:1-1123 |

## Repo-Internal References

The test file is direct evidence for the production boundary named above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The selected scenarios and assertions implement this test unit's forcing proof. | `_byte_tree` | mcp/tests/test_legacy_operation_bridge.py:1-1123 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_byte_tree` | mcp/tests/test_legacy_operation_bridge.py:1-1123 |

## CCR-R18@v1 Legacy Recovery-Required Result

260831-CCR-L18 updated the schema-1 bridge forcing: while the launched recovery worker is live with a retained exact worker binding, the active legacy closeout operation projects `legacy-closeout-recovery-required` with `nextAction: recover` (not a synthetic `worker-termination-required` result) and advertises only the `cancel` legal control — a live retained worker binding is ordinary authority until a real cancellation/termination transition records durable termination evidence (`worker_termination_required_result`).

## Update History

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the legacy bridge live-worker projection update (recovery-required, not synthetic termination). Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
