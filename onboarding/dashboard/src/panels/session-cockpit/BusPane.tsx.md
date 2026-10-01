# dashboard/src/panels/session-cockpit/BusPane.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Renders the fleet-global pending-pickup projection, an optional exact focused-seat filter, the
agent-notifier heartbeat, and sender-addressed developer reply controls without claiming full inbox
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

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Exact focused-seat identity predicate and row facts. [1]
- Entry-keyed state, authoritative pruning, filters, and list rendering. [2]
- Separately rendered agent-notifier heartbeat. [3]
- Reverse reply write boundary. [4]
- Shared virtualized-list threshold and semantics. [5]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.

## Current L5I Maintenance

`BusPane` now receives an `ageClockActive` gate and advances its local age clock only while the
visible inspector is showing the bus tab. Hidden inspector tabs retain their data but do not perform
unseen clock-driven rendering.
