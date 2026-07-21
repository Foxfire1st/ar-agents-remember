# dashboard/src/panels/session-cockpit/InspectorPrimitives.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/InspectorPrimitives.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T05:30+02:00 |
| lastVerifiedCommitHash | `1119b64ff1564c5fc76fd518f88e529535c04b34` |
| lastVerifiedCommitDate | 2026-07-21T08:14:40+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Shared pane, fact, note, raw, and action grammar. | L1-L135 | [InspectorPrimitives.tsx](InspectorPrimitives.tsx) |
| Evidence consumer. | L169-L374 | [EvidencePane.tsx](EvidencePane.tsx) |
| Capability consumer. | L78-L240 | [CapabilitiesPane.tsx](CapabilitiesPane.tsx) |
| Bus consumer. | L116-L274 | [BusPane.tsx](BusPane.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the V2 value-wrapping fix — `dd`
  `overflowWrap` `anywhere → break-word` (whole-token wrapping), noting its dependency on the `index.css`
  `word-break: normal` root override (RV-1). Verification pinned to the leaf base (`352d5cd`) until
  closeout stamps the candidate commit.
- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
