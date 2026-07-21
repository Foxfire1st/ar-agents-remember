# dashboard/src/panels/session-cockpit/StatusLine.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/StatusLine.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T05:30+02:00 |
| lastVerifiedCommitHash | `1119b64ff1564c5fc76fd518f88e529535c04b34` |
| lastVerifiedCommitDate | 2026-07-21T08:14:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Renders the persistent focused-seat footer in a contractual order, combining proven launch, state,
work-queue, and freshness facts. **Collapse-or-explain (260718-CHATS-L5P, R3/R4/A1/A2):** an absent
value disappears WITH its label rather than chaining em-dash placeholders, and the healthy steady state
collapses to one calm token instead of a row of reassurance zeros.

## Code Commentary

### Logic

- **Order** — harness → model/effort (`pairText`) + `EvidenceBadge` → state dot/word + observed working
  elapsed → leaf/seat (`leafSeatText`) → pending sets / queued messages → freshness (`freshnessText`);
  optional panel actions and the keyboard hint sit at the right edge.
- **No focus (R3/A1)** — when `session === undefined` the footer collapses to a single honest phrase
  `no chat focused — open one from the rail` (`data-testid="status-empty"`), NOT the old five-dash chain.
- **Collapse-or-explain segments (R3/A1)** — `pairText`/`leafSeatText` are built with `joinChips`
  (`data/conversation/format`), so an absent `model`/`effort`/`leaf`/`seat` drops with its label and the
  segment renders only when it carries something; `pending sets`/`queued messages` chips render only when
  `> 0` (R4/A2). A lone absent `harness` still renders (`harness —`) — it is the F6 focus target, one
  honest glyph, not a chain link.
- **Freshness zero-collapse (R4/A2)** — `healthySteady = pollHealth.healthy && missedBeats === 0`
  collapses to `poll ✓`; the reassurance chips (`poll stale · missed N · beat age …`) surface only when
  actually degraded. The PTY `ws` word shows only when a pane reports a ws state (`freshness.ptyWs !==
  "none"`), never `pty ws —`.
- **UA-5 slot REMOVED (R3, was a contract)** — the reserved `ctx — / cost — (UA-5 slot)` segment is
  DELETED (it rendered leaked internal jargon + bare em-dashes on every seat; a real ctx/cost readout
  will render itself when that authority exists). This supersedes the prior "literal UA-5 absence slot
  is a product contract" claim.
- **V25 sentinel** — the `EFFORT_NOT_ECHOED_COPY` sentinel already begins with "effort", so it is NOT
  re-labeled (`effort not echoed`, was the doubled `effort effort not echoed`); a real effort value
  keeps its `effort ` label. Model/effort uses effective selection + exact-session snapshot truth.
  Timers run only when elapsed/freshness needs to advance.

### Invariants And Boundaries

- Absent values collapse with their label or read as a short honest phrase — never an em-dash chain
  (A1); healthy steady-state metrics collapse to `poll ✓` — chips appear only when nonzero/degraded (A2).
- No token, cost, latency, or effort evidence may be synthesized; no ctx/cost slot is rendered until a
  real authority exists.
- Elapsed is client-measured from an observed state transition and is labelled as bounded truth.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Derivations, bounded clocks, collapse-or-explain render order. | L56-L230 | [StatusLine.tsx](StatusLine.tsx) |
| The `joinChips` collapse helper the pair/leaf-seat segments use (A1/A2). | — | [../../data/conversation/format.ts](../../data/conversation/format.ts) |
| Launch-evidence tier machine. | L1-L70 | [../../data/launchEvidence.ts](../../data/launchEvidence.ts) |
| Model-local capability selection. | L1-L246 | [../../data/sessionCapabilities.ts](../../data/sessionCapabilities.ts) |
| Shared state grammar. | L1-L126 | [../../data/stateGrammar.ts](../../data/stateGrammar.ts) |
| The suite pinning the empty state, collapsed segments, and UA-5-slot absence. | — | [StatusLine.test.tsx](StatusLine.test.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: rewrote for collapse-or-explain (R3/R4/A1/A2). No
  focus → one `no chat focused` phrase; pair/leaf-seat segments join via `joinChips` and drop when
  empty; pending/queued chips only when `> 0`; healthy freshness collapses to `poll ✓`; `pty ws —` shows
  only with a real pane; V25 sentinel no longer double-labeled. IMPORTANT correction: the reserved `ctx
  — / cost — (UA-5 slot)` segment is REMOVED — the prior "literal UA-5 absence slot is a product
  contract" claim no longer holds. Verification pinned to the leaf base (`352d5cd`) until closeout stamps
  the candidate commit.
- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Documented the
  contractual status order and (then-current) honest UA-5 absence. Verification metadata remains pinned
  to the leaf base until closeout.
