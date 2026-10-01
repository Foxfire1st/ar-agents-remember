# dashboard/src/panels/session-cockpit/SeatInspector.tsx

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

## Evidence

### Repo-Internal References

- Tab identities, keyboard behavior, and stable mounted panels. [1]
- Full audit surface and explicit set mark-seen action. [2]
- Exact-session capability surface. [3]
- Fleet-first pickup and heartbeat surface. [4]

## Current L5I Maintenance

The inspector threads visibility and active-tab truth to `BusPane`, allowing its age clock to run
only when the visible inspector is actually on the bus tab.
