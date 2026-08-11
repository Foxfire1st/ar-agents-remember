# mcp/tests/test_worktree_integrate_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_integrate_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-08T02:00+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Integration-seam suite for leaf-targeted versus master/full code-quality altitude.

## Code Commentary

### Logic

Leaf integration builds a `QualityGateTarget` from both the code worktree and enclosure worktree group, so the targeted gate can use enclosure-local evidence; series integration uses the full capped gate. Dry-run reports without executing and a refusal prevents merge.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the owning seam directly.

### Invariants And Boundaries

Altitude routing is contract-kind based; the worktree group accompanies the code checkout; no integration mutation occurs after a failed quality gate.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `integration_contract` | mcp/tests/test_worktree_integrate_quality_gate.py:26-26 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-08-11T19:58+02:00 — Reconciled `test_worktree_integrate_quality_gate.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new integration-altitude suite; content derived from
  the current worktree source. Verification metadata pinned until closeout
  stamps the 260731-EFA-L17 commit.
