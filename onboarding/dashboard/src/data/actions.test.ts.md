# dashboard/src/data/actions.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/actions.test.ts`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`       |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Vitest unit coverage for `dashboard/src/data/actions.ts`, the dashboard action POST client for gate
decisions, lifecycle-scoped attention dismissals, gate-only dismissals, and repo-level actionable-drift
dismissals.

## Code Commentary

The tests stub global `fetch` and exercise `postGateDecision` directly. One case asserts a targeted
reject sends `{target, gateId, note}` to `/api/actions/reject` and maps `202` to `recorded`. Another
case asserts gate-id-only `cancel` omits `target` for stale queue cleanup. The final case asserts
`409` payloads distinguish `stale-gate` from `no-open-gate`. The `postAttentionDismiss` cases assert
targeted lifecycle/gate payloads, gate-id-only gate-open payloads, targetless actionable-drift payloads,
and non-202 response mapping.

## Invariants And Boundaries

These tests cover the transport/status mapping only; server-side gate mutation, lifecycle acknowledgement
writes, and rejection-reason validation are covered in `mcp/tests/test_serving.py`.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Client under test. | "export type GateDecisionStatus" | dashboard/src/data/actions.ts:7-7 |
| Serving tests cover the backend action route. | `AppTests` | mcp/tests/test_serving.py:480-554 |
| Targetless actionable drift dismissal omits `target` while still carrying `itemId` and `kind`. | "distinguishes stale gates from missing open gates" | dashboard/src/data/actions.test.ts:51-64 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: added/recorded client coverage for targetless
  actionable-drift dismiss payloads, the repo-level one-shot attention case. Verification metadata
  pinned until closeout stamps the task-29 code commit.
- 2026-06-28T03:05+02:00 — Task 28 S5.2: updated `postAttentionDismiss` coverage for lifecycle-targeted rows, gate-id-only gate-open rows, and error mapping. Verification metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: added coverage that gate-id-only cancel omits `target` from the POST body.
- 2026-06-25T07:17+02:00 — Created for Task 19: targeted gate-decision request body and stale/no-open status mapping coverage. Verification metadata pinned until closeout stamps the task-19 code commit.
