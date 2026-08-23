# mcp/src/agents_remember/worktrees/integration/integration_quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Runs altitude-aware acceptance for integration: ordinary leaves reuse their targeted closeout certification, while a final organizational leaf or atomic series runs one exact full gate.

## Code Commentary

### Logic

`quality_gate_mode` returns `GATE_FULL` for any branch-owning master integration and refuses a leaf. `run_integration_quality_gate` short-circuits a leaf with no completion plan to `_leaf_closeout_certification`; otherwise it runs (or reuses) the exact full gate against a detached checkout of the exact commit, binds the completion fingerprint to the Dagger result, and persists a crash-safe `IntegrationQualityCertification`. `organizational_quality_failure_payload` returns the repair handoff (`worktree_operation_cancel`) for a failed final-leaf gate.

### Invariants And Boundaries

- A final organizational leaf and an atomic series both use the detached exact-commit checkout.
- Organizational certification and publication evidence is persisted for crash-safe reuse in the
  integration journal; queue projection may schedule the door candidate but does not own repair.
- A reused certification must match the current completion fingerprint, code commit, candidate tree, and Dagger plan.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Mode is full for branch-owning integration; leaves reuse closeout. | `quality_gate_mode` | mcp/src/agents_remember/worktrees/integration/integration_quality.py:84-89 |
| Dry-run preview carries the organizational completion scope and fingerprint. | `quality_gate_preview` | mcp/src/agents_remember/worktrees/integration/integration_quality.py:92-114 |
| One exact full gate runs or reuses a matching certification. | `run_integration_quality_gate` | mcp/src/agents_remember/worktrees/integration/integration_quality.py:117-211 |
| Failed final-leaf gate returns the cancel-repair handoff. | `organizational_quality_failure_payload` | mcp/src/agents_remember/worktrees/integration/integration_quality.py:235-290 |
| Certification binds completion fingerprint, commit, tree, and attestation. | `_certification`, `_require_matching_certification` | mcp/src/agents_remember/worktrees/integration/integration_quality.py:293-307; mcp/src/agents_remember/worktrees/integration/integration_quality.py:327-352 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Contract

The current source seams include `IntegrationQualityFailure`, `integration_quality_failure`, `IntegrationQualityOutcome`. Organizational quality and completion evidence is persisted in the canonical integration journal and repaired through journal-owned transitions. The earlier description of a queue-owned quality transaction is obsolete.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `IntegrationQualityFailure`, `integration_quality_failure`, `IntegrationQualityOutcome` at this ownership boundary. | L41-L60; L63-L75; L79-L81 | `mcp/src/agents_remember/worktrees/integration/integration_quality.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/integration_quality.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for altitude-aware integration acceptance.
