# dashboard/src/panels/session-cockpit/InspectorPrimitives.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/InspectorPrimitives.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
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

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
