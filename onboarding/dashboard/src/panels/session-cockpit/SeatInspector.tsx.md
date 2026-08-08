# dashboard/src/panels/session-cockpit/SeatInspector.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/SeatInspector.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af` |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Tab identities, keyboard behavior, and stable mounted panels. | `SeatInspector`; `tab`; `panel` | dashboard/src/panels/session-cockpit/SeatInspector.tsx:37-58; dashboard/src/panels/session-cockpit/SeatInspector.tsx:60-161 |
| Full audit surface and explicit set mark-seen action. | `EvidencePane` | dashboard/src/panels/session-cockpit/EvidencePane.tsx:407-463 |
| Exact-session capability surface. | `CapabilitiesPane` | dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx:84-240 |
| Fleet-first pickup and heartbeat surface. | `BusPane` | dashboard/src/panels/session-cockpit/BusPane.tsx:116-276 |

## Current L5I Maintenance

The inspector threads visibility and active-tab truth to `BusPane`, allowing its age clock to run
only when the visible inspector is actually on the bus tab.

## Update History
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T13:15:12+02:00 — 260731-EFA-L6 S18-B02 curator: retained the four exact component-source anchors (`SeatInspector`, `EvidencePane`, `CapabilitiesPane`, and `BusPane`); no test source was claimed.

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
