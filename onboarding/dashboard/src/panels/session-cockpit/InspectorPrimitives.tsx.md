# dashboard/src/panels/session-cockpit/InspectorPrimitives.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Supplies the small shared visual and semantic grammar used by the Evidence, Capabilities, and Bus
panes: pane/section layout, optional facts, notes, raw payloads, and compact inspector actions.

## Code Commentary

### Logic

- `InspectorSection` provides a consistent titled section; `InspectorFact` omits only truly absent
  values and preserves full content/title; `InspectorNote` states explanatory limits.
- **V2 value wrapping (260718-CHATS-L5P)** (L34): the `fact` `& > dd` value uses `overflowWrap:
  break-word` (was `anywhere`), so a long inspector value wraps on token boundaries rather than
  per-character (`the pane sho/ws the runne/r line-log`). NOTE: this holds only because the leaf's
  `index.css` root override neutralizes `@webtui/css`'s inherited `word-break: break-all` (RV-1) — under
  `break-all` the `overflowWrap` value is inert and the mid-word breaks return. See
  [../../index.css](../../index.css.md).
- `InspectorRaw` renders strings verbatim or JSON values as formatted raw evidence in a scrollable
  ledger treatment.
- `inspectorAction` is the shared compact button style with visible focus and disabled states.

### Invariants And Boundaries

- These are presentation primitives only; evidence derivation and mutations stay in owning panes.
- Raw values must not be summarized or silently truncated by the primitive.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Shared pane, fact, note, raw, and action grammar in `InspectorSection`. [1]
- Evidence consumer, `EvidencePane`. [2]
- Capability consumer, `CapabilitiesPane`. [3]
- Bus consumer, `BusPane`. [4]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
