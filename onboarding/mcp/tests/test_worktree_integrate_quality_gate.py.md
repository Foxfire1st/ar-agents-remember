# mcp/tests/test_worktree_integrate_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_integrate_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T12:53+02:00 |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038` |
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Integration-seam suite for leaf-targeted versus master/full code-quality altitude.

## Code Commentary

### Logic

Leaf integration builds a `QualityGateTarget` from both the code worktree and enclosure worktree
group, so the targeted gate can use enclosure-local evidence; series integration uses the full
gate, host-managed when no explicit cap is configured. Dry-run reports without executing and a
refusal prevents merge. Source-tip cases distinguish unchanged from moved tips, prove a move after
quality blocks before memory replay, and prove the second post-memory recheck blocks immediately
before merge. The memory replay unit matrix pins existing scratch-branch refusal, checkout failure,
rebase conflict, and successful content/ledger rewrite so those legacy helper branches remain
covered without restoring integration-time replay for stale leaf ancestry.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the owning seam directly.

### Invariants And Boundaries

Altitude routing is contract-kind based; the worktree group accompanies the code checkout; no
integration mutation occurs after a failed quality gate or either post-quality source movement
check. A stale leaf must sync before integration; replay helpers do not bypass that admission gate.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `integration_contract` | mcp/tests/test_worktree_integrate_quality_gate.py:28-48 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## L23 Final Candidate Disposition

Integration forcing proves targeted leaf versus full master Dagger altitude, mandatory task-derived
diff base, complete pre/post-quality lineage rechecks, pinned source tips, and failure atomicity
before any source ref moves.

## Update History
- 2026-08-14T06:40+02:00 — L23 final candidate review: integration tests prove targeted leaf versus
  full master Dagger altitude, mandatory diff base, pre/post-quality lineage rechecks, pinned source
  tips, and failure atomicity before refs move.

- 2026-08-13T12:53+02:00 — L23 Dagger-rail coverage: recorded exact source-tip unchanged/moved
  behavior, both post-quality/pre-merge rechecks, and the complete memory replay helper branch
  matrix. Verification provenance remains closeout-owned.


- 2026-08-13T08:40+02:00 — L23 integration-gate repair: added the post-quality source-tip movement refusal and proved memory replay plus source merge remain untouched. Verification metadata remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: added the
  absent-cap/host-managed integration proof while retaining explicit settings-
  cap and altitude-routing coverage. Verification metadata remains pinned
  until closeout stamps L24.

- 2026-08-11T19:58+02:00 — Reconciled `test_worktree_integrate_quality_gate.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new integration-altitude suite; content derived from
  the current worktree source. Verification metadata pinned until closeout
  stamps the 260731-EFA-L17 commit.
