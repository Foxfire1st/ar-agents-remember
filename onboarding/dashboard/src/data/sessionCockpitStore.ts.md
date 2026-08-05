# dashboard/src/data/sessionCockpitStore.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionCockpitStore.ts`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[data overview](overview.md)

## Purpose

The **sessions-cockpit client store** (260715-FEUI-L2 S3, expanded by FEUI-L4): per-seat cockpit
state — typed exact-session snapshots, snapshot/set-route status, echo evidence, serialized pair
state, pending sets, ledgers, evidence tiers, clocks, freshness, and queues — plus view-level facts
(focus, layout mirrors, palette, the orchestration-tree toggle, poll health). Deliberately
SEPARATE from `sessionStore` (the catalog mirror) and `dashboardStore` (the projection). The
HONESTY INVARIANTS live in this shape: server truth is mirrored, never invented — `requested` and
`effective` are separate fields everywhere, **a queued set NEVER moves the effective marker**, and
evidence tiers start at `pending` until server evidence or readback proves better.

FEUI-L5 extends each session with bounded submission history, the authoritative queued projection,
pending withdrawal, one explicit recovery slot, and draft/answer revision counters. These fields are
projections of server lifecycle truth plus local CAS state; they are not a second queue authority.

## Code Commentary

### Logic

- **FEUI-L4 live-control slice**: cit:([`liveSnapshot`], dashboard/src/data/sessionCockpitStore.ts:114-114) carries a typed
  `CapabilitySnapshotWire`; `snapshotLoading`/`snapshotError` keep exact-session GET status;
  timestamped per-kind `echoEvidence` competes with snapshots by freshness;
  `setRouteError` keeps HTTP-boundary failures distinct; and `pairChange` holds the serialized
  model→effort machine. Successful snapshots clear fetch errors, failures clear loading, and
  per-kind echo writes never overwrite the other knob.
- **`PerSessionCockpit`**: cit:([`PerSessionCockpit`], dashboard/src/data/sessionCockpitStore.ts:113-153) — per-kind `pendingSets` (`{model?, effort?}` — clobber-proof
  by construction: `recordPendingSet` spreads per kind, so a pair change never clobbers the other
  knob's in-flight set); `setLedger: SetLedgerEntry[]` with the explicit `acknowledged` operator
  act (F22 — feeds the unacked attention class); five-tier
  `launchEvidence` (`EvidenceTier = pending|readback|model-validated|defaults|refused`, starting
  `pending`); composer draft shell (`draft` + `draftRevision`; submit lifecycle lands in L5);
  `surfaceTab: 'terminal'` (transcript joins when UA-1 lands); client `turnClock` (~-labeled,
  observed transitions only); `freshness {ptyWs: none|connected|reconnecting|dropped, lastOutputAt}`
  (R15 — fed by the pane's real WS state since L6, via `terminal.ts`'s `onSocketState`); the
  client `queue` of `QueuedSubmit`s (a LIST, not a chip — F13; `supersedeLastQueued` = the alt+↑
  pop-back, requestId never resent); and (260715-FEUI-L6 R4, design §4.3's F7 field)
  **`interactionAnswer?: InteractionAnswerState`** — cit:([`InteractionAnswerState`], dashboard/src/data/sessionCockpitStore.ts:156-169) — the InteractionBar's answer
  round-trip: `{interactionId, inflight, error?, answeredAt?}` — in-flight → verbatim POST error
  (cleared by retry) → `answeredAt` on 202 ("answered — waiting for the agent" until the row
  clears). Store-backed rather than component state so it SURVIVES VIEW SWITCHES (worker decision
  3); the bar clears it whenever the row's interactionId changes under it (including to
  undefined — fix round finding 5). Appended via `setInteractionAnswer` (L148, L291-L294);
  `emptyPerSession` untouched (absent = nothing in flight).
- **Ledger and acknowledgment**: cit:([`appendSetLedger`], dashboard/src/data/sessionCockpitStore.ts:236-239) accepts an explicit acknowledgment
  default so benign immediate/non-clamp echo/queued evidence does not create fleet attention;
  unsupported, clamp, and unknown remain unacknowledged. `acknowledgeMatchingOutcomes` clears only
  the exact kind/request resolved by definitive readback. Ledger writes deliberately never move
  the effective marker.
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
- **`startCockpitMirror()`**: cit:([`startCockpitMirror`], dashboard/src/data/sessionCockpitStore.ts:522-542) — the refcounted catalog-mirror subscription — watches
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
- `launchEvidence.tier` starts `pending`; set-control effectiveness lives separately in typed
  snapshots and timestamped echo evidence, and only the L4 client promotes from actual evidence.
- Client-only fields (freshness, queue, turnClock) are client measurements and must be presented
  as such (`~`-labels, sweep-bound tooltips) — never as server truth.
- Known follow-up nit (worker report, deliberate): `recordPollBeat` creates a fresh `pollHealth`
  object per 2.5 s beat (re-renders the banner subscriber); an identity-preserving write is a
  candidate follow-up, out of the leaf's minimal-fix mandate.

### 2026-07-24 Curator Delta

Interaction retry state can now retain a structured answers map alongside its human-readable summary.
The exact map, keyed by the authoritative question text, is what a retry resends; it is not rebuilt
from rendered controls.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The per-seat shape, L4 live-control state/actions, honesty invariants, poll health, toggle persistence, and mirror. | `PerSessionCockpit`; `SessionCockpitState`; `recordPollBeat`; `setOrchestrationTreeView`; `startCockpitMirror` | dashboard/src/data/sessionCockpitStore.ts:113-153; dashboard/src/data/sessionCockpitStore.ts:209-268; dashboard/src/data/sessionCockpitStore.ts:227-228; dashboard/src/data/sessionCockpitStore.ts:522-542 |
| The exact snapshot and five-value set-acceptance wire vocabulary mirrored by the store. | `CapabilitySnapshotWire`; `SetAcceptance` | dashboard/src/types/harnessCapabilities.ts:59-65; dashboard/src/types/harnessCapabilities.ts:86-86 |
| The sole I/O driver for snapshot, route-error, echo, pair, and matching-ack writes. | `refreshSessionSnapshot`; `sendSet`; `applySetResult`; `startPairChangeFlow`; `acknowledgeSetAttention`; `cycleEffortRequested` | dashboard/src/data/setClient.ts:68-115; dashboard/src/data/setClient.ts:157-244; dashboard/src/data/setClient.ts:247-300; dashboard/src/data/setClient.ts:327-335; dashboard/src/data/setClient.ts:338-343; dashboard/src/data/setClient.ts:352-374 |
| The beat writer (every catalog read records poll health). | `currentCatalogTransportAttempt` | dashboard/src/data/catalogPoll.ts:62-77 |
| The catalog registry the mirror subscribes to. | `sessionStore` | dashboard/src/data/sessions.ts:271-437 |
| The view that mirrors layout/palette in and consumes focus + perSession. | `focusedSessionId`; `perSession`; `setLayout`; `setPaletteOpen` | dashboard/src/panels/session-cockpit/SessionsView.tsx:258-258; dashboard/src/panels/session-cockpit/SessionsView.tsx:260-260; dashboard/src/panels/session-cockpit/SessionsView.tsx:501-509 |
| The freshness/provenance consumers (HeaderStrip diagnostics, inspector tiers). | `WS_WORDS`; `HeaderStrip`; `freshness` | dashboard/src/panels/session-cockpit/HeaderStrip.tsx:81-86; dashboard/src/panels/session-cockpit/HeaderStrip.tsx:88-169; dashboard/src/panels/session-cockpit/HeaderStrip.tsx:101-101 |
| The unit suite incl. the QUEUED-never-moves-the-marker and per-kind clobber cases. | `recordPendingSet`; "QUEUED NEVER MOVES THE EFFECTIVE MARKER: ledger writes leave launchEvidence untouched" | dashboard/src/data/sessionCockpitStore.test.ts:41-56; dashboard/src/data/sessionCockpitStore.test.ts:75-89 |
| The answer round-trip driver (writes in-flight/error/answered; clears on interaction change). | `interactionAnswer`; `submitInteractionAnswer`; `setInteractionAnswer`; `retryStoredInteractionAnswer` | dashboard/src/panels/session-cockpit/InteractionBar.tsx:298-315; dashboard/src/panels/session-cockpit/InteractionBar.tsx:352-379; dashboard/src/panels/session-cockpit/InteractionBar.tsx:492-515 |
| The answer path whose outcomes the round-trip state records. | `answerPendingInteraction`; `submitInteractionAnswer`; `retryStoredInteractionAnswer` | dashboard/src/data/interactionAnswer.ts:449-481; dashboard/src/data/interactionAnswer.ts:504-618; dashboard/src/data/interactionAnswer.ts:620-640 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

Per-session state now includes `submitHistory`, the authoritative queue projection, pending
withdrawal, and one recovery slot, with pure compactors protecting live rows and bounding settled
tails. Draft and interaction-answer revisions support compare-and-swap clearing/restoration. Queue
rows are server lifecycle projections only; locally sending or ambiguous requests never masquerade
as withdrawable queued work.

## FEUI-L8 Reviewed Candidate Delta

The canonical Chats inspector now initializes collapsed. Deliberate inspector opt-in is persisted by the view; this store default establishes the product posture without conflating it with responsive geometry.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-08-03T03:59:59+02:00 — Curated 15 citation claims (10 table rows, 5 prose citations): added exact anchors and source paths; scoped fixer generated the final ranges.
- 2026-07-24T13:17:50Z — Documented structured-interaction retry state. Verification hash/date remain
  pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — FEUI-L5: documented bounded submit history/queue state, pending
  withdrawal, exact recovery, and draft/answer revision-CAS actions.

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 added the typed exact-session snapshot/error/loading
  slice, timestamped per-kind echo evidence, route errors, serialized pair state, selective
  readback acknowledgment, and pre-acknowledged benign ledger evidence. Requested and effective
  state remain separate. Verification metadata is pinned to the contract base pending code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (R4, F7): appended the optional per-seat
  `interactionAnswer` slice (`InteractionAnswerState` + `setInteractionAnswer`) — the
  InteractionBar's answer round-trip (in-flight → verbatim error → answered-waiting), store-backed
  so it survives view switches and cleared when the interactionId changes under it. Append-only;
  `emptyPerSession` untouched. Verification metadata pinned to the leaf base until closeout
  stamps the L6 code commit.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S3 (R3/R15/F13/F22): the cockpit client
  store — per-kind pending sets, acknowledged set ledger that never moves launch evidence,
  five-tier evidence starting pending, composer shell, turn clock, per-pane freshness, client
  queue with alt+↑ supersession, poll-health beats with the 3-miss stale cutoff, the persisted
  orchestration-tree toggle, one-way view mirrors, and the refcounted catalog mirror.
  Verification metadata pinned to the leaf base until closeout stamps the L2 code commit.
