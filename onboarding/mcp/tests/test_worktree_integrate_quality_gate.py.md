# mcp/tests/test_worktree_integrate_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_integrate_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-14T12:13:26+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Integration-seam suite for leaf closeout-proof reuse versus master/full code-quality altitude.

## Code Commentary

### Logic

Leaf integration returns the explicit `certified-at-leaf-closeout` result without calling the
quality decider or executor. Series integration builds the `QualityGateTarget` and uses the full
gate, host-managed when no explicit cap is configured. Dry-run reports without executing and a
master refusal prevents merge. Source-tip cases distinguish unchanged from moved tips, prove a move after
quality blocks before memory replay, and prove the second post-memory recheck blocks immediately
before merge. The memory replay unit matrix pins existing scratch-branch refusal, checkout failure,
rebase conflict, and successful content/ledger rewrite so those legacy helper branches remain
covered without restoring integration-time replay for stale leaf ancestry.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the owning seam directly.

### Invariants And Boundaries

Acceptance ownership is contract-kind based: leaf integration never reruns targeted acceptance,
while master integration owns full acceptance and carries the worktree group. No
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

Integration forcing proves leaf no-rerun versus full master Dagger altitude, mandatory task-derived
diff base, complete pre/post-quality lineage rechecks, pinned source tips, and failure atomicity
before any source ref moves.

## R39 Integration Forcing Evidence

The integration suite now proves leaf integration reuses closeout acceptance without invoking a
gate, while master integration owns full acceptance and blocks before merge on a missing
self-owned wrapper or failed Dagger result. Leaf mode cannot be requested from the integration
gate selector.

## R43 Self Versus Consumer Wrapper Policy

The altitude suite now proves both arms at master integration: Agents Remember without its
self-owned wrapper blocks before merge, while a consumer repository without an opted-in wrapper
reports `wrapper-unavailable` and remains non-blocking. The full gate still runs once when present.

## Update History

- 2026-08-14T12:13:26+02:00 — R43 curator: added the consumer-master non-blocking counterpart to
  the self-repository missing-wrapper refusal. Verification remains closeout-owned.

- 2026-08-14T11:27+02:00 — R39 curator: replaced leaf rerun expectations with certified-commit
  reuse and master-only full enforcement. Verification remains closeout-owned.
- 2026-08-14T09:37+02:00 — Reopened L23 cadence proof: the leaf seam asserts zero quality-decider
  and executor calls, while the series seam retains the single full Dagger run and refusal boundary.
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
