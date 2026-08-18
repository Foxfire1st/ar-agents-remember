# mcp/src/agents_remember/worktrees/integration_quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration_quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-17T12:09+02:00 |
| lastVerifiedCommitHash | `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b` |
| lastVerifiedCommitDate | 2026-08-18T03:31:59+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Runs altitude-aware acceptance for integration: ordinary leaves reuse their targeted closeout certification, while a final organizational leaf or atomic series runs one exact full gate.

## Code Commentary

### Logic

`quality_gate_mode` returns `GATE_FULL` for any branch-owning master integration and refuses a leaf. `run_integration_quality_gate` short-circuits a leaf with no completion plan to `_leaf_closeout_certification`; otherwise it runs (or reuses) the exact full gate against a detached checkout of the exact commit, binds the completion fingerprint to the Dagger result, and persists a crash-safe `IntegrationQualityCertification`. `organizational_quality_failure_payload` returns the repair handoff (`worktree_operation_cancel`) for a failed final-leaf gate.

### Invariants And Boundaries

- A final organizational leaf and an atomic series both use the detached exact-commit checkout.
- Only the organizational result is persisted for crash-safe reuse because its gate and master publication share the queue-owned transaction.
- A reused certification must match the current completion fingerprint, code commit, candidate tree, and Dagger plan.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Mode is full for branch-owning integration; leaves reuse closeout. | `quality_gate_mode` | mcp/src/agents_remember/worktrees/integration_quality.py:46-51 |
| Dry-run preview carries the organizational completion scope and fingerprint. | `quality_gate_preview` | mcp/src/agents_remember/worktrees/integration_quality.py:54-76 |
| One exact full gate runs or reuses a matching certification. | `run_integration_quality_gate` | mcp/src/agents_remember/worktrees/integration_quality.py:79-171 |
| Failed final-leaf gate returns the cancel-repair handoff. | `organizational_quality_failure_payload` | mcp/src/agents_remember/worktrees/integration_quality.py:195-232 |
| Certification binds completion fingerprint, commit, tree, and attestation. | `_certification`, `_require_matching_certification` | mcp/src/agents_remember/worktrees/integration_quality.py:235-249; mcp/src/agents_remember/worktrees/integration_quality.py:269-294 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for altitude-aware integration acceptance.
