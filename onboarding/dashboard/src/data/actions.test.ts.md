# dashboard/src/data/actions.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Vitest source assertions for the attention-dismiss client send only stable `itemId` and `kind`, include an explicit targetless actionable-drift case, and map non-202 replies to error. This card describes transport assertions, not executed coverage.

## Code Commentary

The fetch stub records `/api/actions/dismiss` and the exact JSON body. There is no lifecycle target or gateId in current dismiss requests. Successful 202 replies map to `dismissed`; the error case maps a non-202 reply to `error`. Removed gate-decision cases are not current coverage.

## Invariants And Boundaries

These source assertions concern client transport/status mapping only. They establish no server-side gate mutation, acknowledgement write or rejection validation, and this renewal ran no test.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The attention-dismiss client posts only itemId/kind as JSON to /api/actions/dismiss. HTTP 202 maps to dismissed, other statuses and thrown/network failures map to error; the exported target shape has no lifecycle target and the module exports no gate-decision client. Source tests assert the exact provider-down and actionable-drift bodies and a non-202 error. [1]

- The actionable-drift case asserts itemId/kind without target; the old stale-gate locator is not the current proving body. [2]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
