# dashboard/src/panels/session-cockpit/BusPane.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/BusPane.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact focused-seat identity predicate and row facts. | `pickupMatchesFocusedSeat` | dashboard/src/panels/session-cockpit/BusPane.tsx:46-60 |
| Entry-keyed state, authoritative pruning, filters, and list rendering. | `BusPane` | dashboard/src/panels/session-cockpit/BusPane.tsx:116-276 |
| Separately rendered agent-notifier heartbeat. | "<InspectorSection title=\"Agent notifier heartbeat\" testId=\"bus-heartbeat\">" | dashboard/src/panels/session-cockpit/BusPane.tsx:197-197 |
| Reverse reply write boundary. | `developerReplyRequest` | dashboard/src/panels/session-cockpit/BusDeveloperReply.tsx:37-59 |
| Shared virtualized-list threshold and semantics. | `INSPECTOR_VIRTUALIZE_THRESHOLD` | dashboard/src/panels/session-cockpit/VirtualizedInspectorList.tsx:11-11 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Current L5I Maintenance

`BusPane` now receives an `ageClockActive` gate and advances its local age clock only while the
visible inspector is showing the bus tab. Hidden inspector tabs retain their data but do not perform
unseen clock-driven rendering.

## Update History
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 5 repository-internal citations for the focused predicate, pane projection, heartbeat, reverse reply, and virtualized-list threshold.
- 2026-07-24T13:17:17Z — Curator: documented inspector-tab age-clock gating; verification fields
  remain pre-commit.

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Records the
  fleet-first projection, exact filter, honest empty states, and entry-keyed reply persistence.
  Verification metadata remains pinned to the leaf base until closeout.
