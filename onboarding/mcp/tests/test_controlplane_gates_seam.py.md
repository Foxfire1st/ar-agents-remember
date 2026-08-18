# mcp/tests/test_controlplane_gates_seam.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_controlplane_gates_seam.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-16T04:06+02:00                                            |
| lastVerifiedCommitHash | `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b`                                        |
| lastVerifiedCommitDate | 2026-08-18T03:31:59+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_controlplane_gates_seam.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

L23 makes the handover integration seam test invoke dry-run, proving gate-policy forwarding without starting a detached lifecycle mutation.
Its gate-only unit explicitly mocks `_integration_lineage_block`: source-lineage behavior is proved
by the dedicated integration/lineage suites, so this seam isolates gate forwarding rather than
constructing a second incomplete topology fixture.

- `_handover_gate`
- `MasterHandoverSeamTests`
- `HandoverEnforcementHelperTests`
- `IntegrateDryRunGuardTests`
- `SeamChannelTests`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_controlplane_gates_seam.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## L23 Final Candidate Disposition

The seam tests prove that current lineage and an exact candidate-bound passing route review are
checked before curator host creation and again at lifecycle exit. Neither brief prose nor a stale
verdict can bypass control-plane admission.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## Update History

- 2026-08-17T12:30+02:00 — No content impact: L5 coverage-pragma alignment only; the documented seam behavior is unchanged.

- 2026-08-16T07:10+02:00 — L4 review repair: the apply-only handover seam models the real operation record's empty recovery tuple so completed-recovery admission remains type-faithful.
- 2026-08-16T05:18+02:00 — Dagger fixture repair: the application plumbing case supplies a real absolute settings file and configured repository alias before asserting the selected gate policy reaches integration preview.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: dry-run integration gate tests provide configured-path and replay-source facts so they reach the intended handover guard rather than fail earlier authority construction.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-14T06:38+02:00 — L23 final candidate review: seam tests prove curator dispatch and
  lifecycle exit cannot bypass current-lineage or candidate-bound route-review admission.

- 2026-08-13T12:53+02:00 — No content impact: the gate-only dry-run seam now mocks the independent
  source-lineage boundary so it continues testing gate-policy forwarding only. Production behavior
  and gate assertions are unchanged; verification provenance remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
