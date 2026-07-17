# dashboard/src/data/sessionCockpitStore.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionCockpitStore.ts`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The **sessions-cockpit client store** (260715-FEUI-L2 S3, design §4.3): per-seat cockpit state —
drafts, set ledgers, evidence tiers, clocks, freshness, queues — plus the view-level facts
(focus, layout mirrors, palette, the orchestration-tree toggle, poll health). Deliberately
SEPARATE from `sessionStore` (the catalog mirror) and `dashboardStore` (the projection). The
HONESTY INVARIANTS live in this shape: server truth is mirrored, never invented — `requested` and
`effective` are separate fields everywhere, **a queued set NEVER moves the effective marker**, and
evidence tiers start at `pending` until control state proves better (L4 wires the promotions).

## Code Commentary

### Logic

- **`PerSessionCockpit`** (L56-L81): per-kind `pendingSets` (`{model?, effort?}` — clobber-proof
  by construction: `recordPendingSet` spreads per kind, so a pair change never clobbers the other
  knob's in-flight set); `setLedger: SetLedgerEntry[]` with the explicit `acknowledged` operator
  act (F22 — feeds the unacked attention class); five-tier
  `launchEvidence` (`EvidenceTier = pending|readback|model-validated|defaults|refused`, starting
  `pending`); composer draft shell (`draft` + `draftRevision`; submit lifecycle lands in L5);
  `surfaceTab: 'terminal'` (transcript joins when UA-1 lands); client `turnClock` (~-labeled,
  observed transitions only); `freshness {ptyWs: none|connected|reconnecting|dropped, lastOutputAt}`
  (R15 — `none` until L6 attaches a pane); the client `queue` of `QueuedSubmit`s (a LIST, not a
  chip — F13; `supersedeLastQueued` = the alt+↑ pop-back, requestId never resent).
- **`appendSetLedger`** (L196-L204) — deliberately NEVER touches `launchEvidence`: a set outcome —
  even `immediate` — is its own ledger fact; the effective marker moves only via
  `setLaunchEvidence` with proof (the "QUEUED NEVER MOVES THE EFFECTIVE MARKER" test).
- **Poll health** (L83-L84, L162-L172): `recordPollBeat(ok)` — success resets, failure increments
  `missedBeats`; `POLL_STALE_MISSED_BEATS = 3` flips `healthy=false` → the rail's stale banner
  (R15/F3). Beats arrive from `catalogPoll.hydrateTerminalSessionsFromCatalog` on EVERY read.
- **Orchestration-tree toggle** (L86-L105, L158-L161): persisted PER USER via localStorage
  (`cockpit.sessions.orchestration-tree`) — the leaf doc's open question, decided as an inspection
  preference (the calm-cockpit idiom), not session state.
- **View mirrors** (L109-L111, L155-L157): `focusedSessionId`, `layout
  {railCollapsed, inspectorCollapsed}`, `paletteOpen` — ONE-WAY mirrors from SessionsView (the
  view's imperative panel handles stay the source of truth); mirrored so later leaves/commands can
  read them without a view reference.
- **`startCockpitMirror()`** (L286-L309): the refcounted catalog-mirror subscription — watches
  `sessionStore` and records per-seat turn-state transitions into the client `turnClock`
  (`recordTurnObservation`: `workingSince` starts at the OBSERVED transition into working —
  poll/sweep-bounded, never a claim about when the harness really started).

### Conventions

zustand vanilla `createStore` + the `useSessionCockpit` `useStore` hook (the `data/store.ts` /
`sessions.ts` idiom); `withPerSession` materializes the honest `emptyPerSession()` defaults on
first touch.

### Invariants And Boundaries

- Requested ≠ effective, everywhere: `SetResultSnapshot.effectiveValue` is present ONLY when the
  server proved the value took effect — never inferred client-side.
- `launchEvidence.tier` starts `pending`; nothing in this store self-promotes it (L4 owns the
  promotion paths with evidence).
- Client-only fields (freshness, queue, turnClock) are client measurements and must be presented
  as such (`~`-labels, sweep-bound tooltips) — never as server truth.
- Known follow-up nit (worker report, deliberate): `recordPollBeat` creates a fresh `pollHealth`
  object per 2.5 s beat (re-renders the banner subscriber); an identity-preserving write is a
  candidate follow-up, out of the leaf's minimal-fix mandate.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The per-seat shape, honesty invariants, poll health, toggle persistence, mirror. | L14-L309 | [sessionCockpitStore.ts](sessionCockpitStore.ts) |
| The acceptance vocabulary the ledger snapshots mirror (`HarnessAcceptanceState`). | L11 | [../types/terminalCatalog.ts](../types/terminalCatalog.ts) |
| The beat writer (every catalog read records poll health). | L40-L51 | [catalogPoll.ts](catalogPoll.ts) |
| The catalog registry the mirror subscribes to. | — | [sessions.ts](sessions.ts) |
| The view that mirrors layout/palette in and consumes focus + perSession. | L206-L344 | [../panels/session-cockpit/SessionsView.tsx](../panels/session-cockpit/SessionsView.tsx) |
| The freshness/provenance consumers (HeaderStrip diagnostics, inspector tiers). | L66-L143 | [../panels/session-cockpit/HeaderStrip.tsx](../panels/session-cockpit/HeaderStrip.tsx) |
| The unit suite incl. the QUEUED-never-moves-the-marker and per-kind clobber cases. | L25-L150 | [sessionCockpitStore.test.ts](sessionCockpitStore.test.ts) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S3 (R3/R15/F13/F22): the cockpit client
  store — per-kind pending sets, acknowledged set ledger that never moves launch evidence,
  five-tier evidence starting pending, composer shell, turn clock, per-pane freshness, client
  queue with alt+↑ supersession, poll-health beats with the 3-miss stale cutoff, the persisted
  orchestration-tree toggle, one-way view mirrors, and the refcounted catalog mirror.
  Verification metadata pinned to the leaf base until closeout stamps the L2 code commit.
