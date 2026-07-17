# dashboard/src/panels/session-cockpit/SeatInspector.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SeatInspector.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T08:33+02:00                           |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786`       |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The focused seat's **identity/provenance and set-ledger card** (260715-FEUI-L2 R7/R17; L6 adds the
pane archetype, retire residual, and raw interaction payload; L4 adds the acknowledging ledger):
the inspector half of moat 1 — catalog facts remain read-only while expanding the set ledger is an
explicit mark-seen action. The L7 inspector
(Evidence / Capabilities / Bus tabs) REPLACES this pane; the card keeps the facts visible until
then.

## Code Commentary

### Logic

- `Fact` (L34-L44): a label/value `dl` row that renders nothing for absent values (absent, never
  invented) with the full value as `title`.
- The card (L139-L218 on the L4 code state): **Seat** (label, grammar state word, harness, the
  L6 `pane` archetype fact — `paneArchetypeCopy`, design §1.4 — and leafKey) → **Provenance**
  (spawn role, seat role, `level (source)`, `model <resolved> · <effort> (requested|tier)` —
  the same honest-tier wording as the HeaderStrip — spawned-by session, the frozen original
  label) → **Outcome** (only when landed/retired reasons exist: landed reason/at, retired
  reason/by — R17) → **Liveness** (only when evidence exists: liveness/exit evidence, first
  failed at). No focused seat ⇒ "no focused seat".
- **L3 tier derivation (R7)**: `tier = launchTier(session)` derives launch truth from the row;
  FEUI-L4 now consumes `cockpit` only for the separate set ledger.
- **L3 vendor-defaults honesty** (L84-L92 on the L3 code state): a PAIRLESS harness row with a
  control state renders the model fact as "vendor defaults — no selection sent (defaults)" —
  the both-null tier stated as a fact, instead of silently omitting the row's launch story;
  non-harness rows still render nothing.
- **Retire stop residual (L6 R5)** (L62-L63, L105-L111): `controlRaw.retireControlStopError`
  (string-guarded) renders inside Outcome as the `stop note` Fact with `retireResidualCopy` —
  informational evidence on a SUCCESSFULLY retired seat, the same posture as the stage notes
  (the data-layer sweep captures it for the stage; retired rows the user can still focus render
  it here too).
- **Pending interaction (raw) (L6 R4)** (L113-L136): the VERBATIM
  `controlPendingInteraction` payload as a scrollable `pre`
  (`inspector-pending-interaction-raw`) — the InteractionBar's honest unrepresentable fallback
  points here.
- **Set ledger (L4 R6/F22)** (L49-L123, L178): a collapsed-by-default section renders only when
  evidence exists. Its summary counts all entries and unacknowledged entries; expansion calls
  `acknowledgeSetAttention`, then shows newest-first lines with acceptance first and requested →
  effective kept distinct. The section is keyed by session id, so a focus switch remounts the
  next seat collapsed before any acknowledgment effect.

### Invariants And Boundaries

- Catalog identity/provenance/outcome/liveness facts are read-only. The single L4 exception is the
  explicit ledger-view acknowledgment; rendering or switching seats never marks evidence seen.
- The requested-pair honesty boundary applies here identically to the HeaderStrip: the tier word
  derives from control-state truth via `launchTier` (weakest wins, never promoted without proof).
- Sections render only when their facts exist — the card never fabricates an empty scaffold (the
  vendor-defaults fact is not fabrication: it states the both-null tier the row actually carries).
- The stop note is INFORMATIONAL (never "fail" — test-asserted); the raw payload stays verbatim,
  never summarized.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Fact primitive + ledger + sectioned card incl. archetype/stop note/raw payload. | L34-L218 | [SeatInspector.tsx](SeatInspector.tsx) |
| The explicit mark-seen action used only after expansion. | L326-L336 | [../../data/setClient.ts](../../data/setClient.ts) |
| The grammar supplying the state word. | L88-L106 | [../../data/stateGrammar.ts](../../data/stateGrammar.ts) |
| The pure tier machine the model wording derives from (L3). | L29-L41 | [../../data/launchEvidence.ts](../../data/launchEvidence.ts) |
| The archetype + retire-residual copy consumed. | L29-L32, L80-L84 | [lifecycleCopy.ts](lifecycleCopy.ts) |
| The view mounting it in the inspector pane. | L680-L684 | [SessionsView.tsx](SessionsView.tsx) |
| The wire fields it mirrors (provenance, outcome, liveness, control raw). | L24-L90 | [../../types/terminalCatalog.ts](../../types/terminalCatalog.ts) |
| The L6 facts plus L4 ledger/acknowledgment/seat-switch suite. | L18-L144 | [SeatInspector.test.tsx](SeatInspector.test.tsx) |

## Update History

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R6/F22 added the collapsed per-seat set ledger.
  Expanding is the explicit viewing/acknowledgment act; lines remain newest-first and keep
  acceptance, requested, effective, detail, and unseen state in words. Session-keyed remounting
  prevents focus changes from acknowledging the next seat. Verification metadata is pinned to
  the contract base pending code commit.
- 2026-07-17T06:10+02:00 — 260715-FEUI-L3 (R7): the launch tier now derives from row
  control-state truth (`launchTier(session)` — same derivation as the HeaderStrip; the `cockpit`
  prop stays for L4's set-evidence), and a pairless harness row states "vendor defaults — no
  selection sent (defaults)" instead of omitting the launch story. Verification metadata pinned
  to the leaf base until closeout stamps the L3 code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (R1/R4/R5): added the `pane` archetype Fact
  (`paneArchetypeCopy` — controlled line-log vs legacy-raw vendor TUI), the informational
  `stop note` for a retired row's `retireControlStopError` (never a failure state), and the
  verbatim pending-interaction payload `pre` the InteractionBar's unrepresentable fallback
  points at; the card gained its own jsdom suite.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 (R7/R17): the read-only provenance card in
  the inspector pane — seat identity + grammar state, spawn role/level/requested-pair at its
  honest tier, spawned-by + original label, landed/retired outcome reasons, and liveness
  evidence; placeholder until the L7 tabbed inspector. Verification metadata pinned to the leaf
  base until closeout stamps the L2 code commit.
