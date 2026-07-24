# dashboard/src/panels/session-cockpit/BusPane.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/BusPane.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Renders the fleet-global pending-pickup projection, an optional exact focused-seat filter, the
supervisor heartbeat, and sender-addressed developer reply controls without claiming full inbox
history or bus health.

## Code Commentary

### Logic

- `pickupMatchesFocusedSeat` matches only explicit session, agent, owner, sender, or lifecycle
  identities. The pane defaults fleet-global and resets to that view when focus disappears.
- Rows expose sender-to-owner edges, delivery/state, target and owner identities, attempts,
  redelivery times, age/TTL, escalation, and artifact facts. Empty copy distinguishes a filtered
  miss from a fleet projection with no pending rows; neither is presented as healthy.
- Reply interaction state is keyed by durable `entryId` above the filter and virtual rows. It is
  pruned only when an entry leaves the full authoritative pickup projection; a late request
  settlement cannot resurrect a removed entry, and pristine closed state is discarded.
- The heartbeat is rendered as a separate projection fact, including never-ticked, stale, counts,
  cutoff, and last-sweep truth.

### Invariants And Boundaries

- `pickups` is a live pending projection, not a history ledger or health verdict.
- Filter and virtualization unmounts must not lose or reassign drafts, posted state, or failures.
- The only mutation is the isolated new-message POST in `BusDeveloperReply`.

### Todos

Integration smoke should exercise a long virtualized Bus list while a reply settles off-tab.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Exact focused-seat identity predicate and row facts. | L41-L114 | [BusPane.tsx](BusPane.tsx) |
| Entry-keyed state, authoritative pruning, filters, and list rendering. | L116-L222 | [BusPane.tsx](BusPane.tsx) |
| Separately rendered supervisor heartbeat. | L224-L274 | [BusPane.tsx](BusPane.tsx) |
| Reverse reply write boundary. | L37-L196 | [BusDeveloperReply.tsx](BusDeveloperReply.tsx) |
| Shared virtualized-list threshold and semantics. | L39-L107 | [VirtualizedInspectorList.tsx](VirtualizedInspectorList.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Current L5I Maintenance

`BusPane` now receives an `ageClockActive` gate and advances its local age clock only while the
visible inspector is showing the bus tab. Hidden inspector tabs retain their data but do not perform
unseen clock-driven rendering.

## Update History

- 2026-07-24T13:17:17Z — Curator: documented inspector-tab age-clock gating; verification fields
  remain pre-commit.

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Records the
  fleet-first projection, exact filter, honest empty states, and entry-keyed reply persistence.
  Verification metadata remains pinned to the leaf base until closeout.
