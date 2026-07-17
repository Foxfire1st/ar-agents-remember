# dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Capability shaping and authority separation. | L35-L76 | [CapabilitiesPane.tsx](CapabilitiesPane.tsx) |
| Exact-session and pre-session rendering plus existing refresh actions. | L78-L240 | [CapabilitiesPane.tsx](CapabilitiesPane.tsx) |
| Capability derivation consumed by the pane. | L1-L246 | [../../data/sessionCapabilities.ts](../../data/sessionCapabilities.ts) |
| Existing capability read clients. | L1-L151 | [../../data/catalogPoll.ts](../../data/catalogPoll.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Documents the
  exact-session/pre-session authority split and read-only refresh boundary. Verification metadata
  remains pinned to the leaf base until closeout.
