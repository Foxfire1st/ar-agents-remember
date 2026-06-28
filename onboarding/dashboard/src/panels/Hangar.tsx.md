# dashboard/src/panels/Hangar.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Hangar.tsx`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-23T13:45+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The hangar (notes 01/06): persistent worktree-backed lifecycles are NEVER auto-reaped — when they
rot, this surfaces the staleness for the developer to step in (the TTL reaper is fleeting-only).

## Code Commentary

### Logic

Lists every enclosure (sorted) with closeout/integration/cleanup `badge`s + the cross-ref lifecycle's
staleness. `isStale` (cleanup pending / integration completed / inferred lifecycle) toggles the `row`
`cva`'s `stale` boolean variant (amber border). A captured `lifecycleId` guards the ghost open button.
When the bound lifecycle has a worktree-bound gate (`closeout` / `push` / `integration` / `cleanup`),
the actions row renders compact `GateResponder`; otherwise enclosure actions remain display-only
`Affordance`s.

### Invariants And Boundaries

Reflects the enclosure node statuses, not a recomputation. Non-gate affordances remain read-only.
Gate responses are instructional chat injections through `GateResponder`, not enclosure status mutation.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `EnclosureNode` statuses (closeout/integration/cleanup) shown. | — | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The shared chat-routed gate responder. | — | [GateResponder.tsx](GateResponder.tsx) |

## Update History

- 2026-06-23T13:45+02:00 — Task 11: rows with a bound worktree gate now render compact
  `GateResponder` instead of inert gate-like affordances; non-gate action availability still renders
  through `Affordance`. Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-15T17:00 — Created for slice 5d: migrated onto `Panel` + Panda css/cva (local `badge`).
  Verification metadata pinned until closeout stamps the 5d code commit.
