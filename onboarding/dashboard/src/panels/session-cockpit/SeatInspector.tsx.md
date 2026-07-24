# dashboard/src/panels/session-cockpit/SeatInspector.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/SeatInspector.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Owns only the accessible FEUI-L7 Evidence / Capabilities / Bus tab host. Domain projection and
actions live in the three pane components so the already dense `SessionsView` remains composition
rather than absorbing inspector logic.

## Code Commentary

### Logic

- A roving native tablist supports click, Left/Right wrap, Home, and End. Stable `useId`-derived
  tab/panel ids maintain `aria-controls` and `aria-labelledby` relationships.
- All three tabpanels remain mounted and inactive panels use the native `hidden` attribute. This
  removes their controls from layout, accessibility, and keyboard traversal while preserving the
  Bus component instance, drafts, virtual-row state, and in-flight reply settlements.
- Evidence accepts no focus and still exposes lifecycle residuals; Capabilities states the exact-
  session limitation; Bus remains fleet-global and reachable without a focused seat.
- **V2 tab label (260718-CHATS-L5P)** (L47-L53, L102-L106): each `tab` is `whiteSpace:nowrap` +
  `overflow:hidden` + `textOverflow:ellipsis` and carries `title={item.label}`, so a long tab label
  truncates to `Capabili…` on one line (h=22) instead of wrapping mid-word to `Capabil/ities`; the full
  label stays reachable via the tooltip.

### Conventions

The host exports `setLedgerEntryLine` from `EvidencePane` for compatibility with the established
test/import surface; evidence ownership itself resides in that pane.

### Invariants And Boundaries

- The host is composition-only: no evidence derivation, capability reads, inbox writes, or
  acknowledgement effects belong here.
- Inactive panes stay mounted but must remain natively hidden.
- Viewing, tab changes, and seat changes never mark set evidence seen.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Tab identities, keyboard behavior, and stable mounted panels. | L18-L151 | [SeatInspector.tsx](SeatInspector.tsx) |
| Full audit surface and explicit set mark-seen action. | L34-L374 | [EvidencePane.tsx](EvidencePane.tsx) |
| Exact-session capability surface. | L35-L240 | [CapabilitiesPane.tsx](CapabilitiesPane.tsx) |
| Fleet-first pickup and heartbeat surface. | L41-L274 | [BusPane.tsx](BusPane.tsx) |
| Host integration and off-tab state regressions. | L28-L185 | [SeatInspector.test.tsx](SeatInspector.test.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Current L5I Maintenance

The inspector threads visibility and active-tab truth to `BusPane`, allowing its age clock to run
only when the visible inspector is actually on the bus tab.

## Update History

- 2026-07-24T13:17:17Z — Curator: documented visible-bus age-clock ownership; verification fields
  remain pre-commit.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the V2 tab-label fix — `nowrap` +
  ellipsis + full-label `title` on each tab so `Capabilities` truncates on one line rather than wrapping
  mid-word. Tablist keyboard behavior + mounted-hidden panels unchanged. Verification pinned to the leaf
  base (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 replaced the interim provenance/ledger card with the
  accessible three-pane inspector host. Round 3 fixed the final integration gap by keeping every
  panel mounted and using native `hidden`, preserving Bus state and async settlement off-tab.
  Verification metadata remains pinned to the leaf base until closeout.
- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 added the explicit set-ledger mark-seen boundary.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 added pane archetype, stop residual, and raw pending-
  interaction evidence now owned by `EvidencePane`.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 as the interim focused-seat fact card.
