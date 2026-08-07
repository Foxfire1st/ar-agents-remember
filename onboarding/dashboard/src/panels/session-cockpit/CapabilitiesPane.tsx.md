# dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Displays read-only capability truth while keeping a focused session's exact live snapshot separate
from the harness's pre-session launch envelope.

## Code Commentary

### Logic

- The exact-session section renders only the focused session snapshot and its model-local effort
  options/current selection. Missing effort echo remains explicitly `effort not echoed`.
- A separate pre-session section renders the broader harness envelope; it is never promoted into
  exact-session truth.
- Refresh controls reuse only the existing exact-session and harness capability reads. Copy states
  generic native-process cost without inventing fixed latency seconds.

### Invariants And Boundaries

- Capability data is read-only in this pane; model/effort mutations remain in the stage control.
- Pre-session availability and exact-session support are different authorities and must stay
  visually and logically separate.
- Unsupported or un-echoed values remain absent/worded rather than inferred.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Capability shaping and authority separation. | `modelFlags`; `CapabilityModelRow`; `CapabilitiesPane` | dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx:39-48; dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx:50-82; dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx:84-240 |
| Exact-session and pre-session rendering plus existing refresh actions. | `CapabilitiesPane` | dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx:84-240 |
| Capability derivation consumed by the pane is owned by `modelRowByKey`, `deriveEffortMenu`, and `effectiveSelection`. | `modelRowByKey`; `deriveEffortMenu`; `effectiveSelection` | dashboard/src/data/sessionCapabilities.ts:139-145; dashboard/src/data/sessionCapabilities.ts:157-178; dashboard/src/data/sessionCapabilities.ts:219-248 |
| The pane calls the derived-selection and effort-menu helpers and resolves the selected model row from that derived state. | "const selection = effectiveSelection(cockpit);"; "const effortMenu = snapshot ? deriveEffortMenu(snapshot) : undefined;"; "const selectedModel = snapshot" | dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx:100-102 |
| Existing capability read clients. | `fetchHarnessCapabilities` | dashboard/src/data/capabilityCatalog.ts:192-268 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T16:40:00+02:00 — 260731-EFA-L6 S18-B12 curator correction (reviewer-BLOCK repair): replaced the not-consumed `classifySessionCapabilitiesResponse` with the actual consumed `modelRowByKey` derivation, bound to its `sessionCapabilities.ts` definition and the pane's real helper calls; the scoped fixer confirmed the final ranges with no writes.
- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 8 citation finding(s); scoped recheck clean.

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Documents the
  exact-session/pre-session authority split and read-only refresh boundary. Verification metadata
  remains pinned to the leaf base until closeout.
