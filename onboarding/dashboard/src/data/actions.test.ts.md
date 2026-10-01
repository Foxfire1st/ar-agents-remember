# dashboard/src/data/actions.test.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Client under test. [1]
- Targetless actionable drift dismissal omits `target` while still carrying `itemId` and `kind`. [2]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
