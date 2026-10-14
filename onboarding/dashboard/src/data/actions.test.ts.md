# dashboard/src/data/actions.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Three retained Vitest source cases for the attention-dismiss POST client: a stale-session lifecycle target, targetless actionable drift and non-202 error mapping. Gate-decision/gate-id-only cases are removed; this card declares assertions, not executed coverage.

## Code Commentary

Historical removed case inventory (not current tests): the tests previously stubbed global `fetch` and exercised `postGateDecision` directly. One case asserts a targeted
reject sends `{target, gateId, note}` to `/api/actions/reject` and maps `202` to `recorded`. Another
case asserts gate-id-only `cancel` omits `target` for stale queue cleanup. The final case asserts
`409` payloads distinguish `stale-gate` from `no-open-gate`. The earlier `postAttentionDismiss` cases included targeted lifecycle/gate and gate-id-only payloads. Current cases instead assert stale-session itemId/kind/target, actionable-drift itemId/kind with no target, and status 500 mapping to error; none retains gateId.

## Invariants And Boundaries

These source assertions concern client transport/status mapping only. They establish no server-side gate mutation, acknowledgement write or rejection validation, and this renewal ran no test.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The retained client builds attention-dismiss itemId/kind and optional lifecycle target, maps 202 to dismissed and other/network failures to error; gate-decision export is removed. [1]

- The actionable-drift case asserts itemId/kind without target; the old stale-gate locator is not the current proving body. [2]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
