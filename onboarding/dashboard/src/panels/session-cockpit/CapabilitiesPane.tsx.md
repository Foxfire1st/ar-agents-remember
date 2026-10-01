# dashboard/src/panels/session-cockpit/CapabilitiesPane.tsx

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

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Capability shaping and authority separation. [1]
- Exact-session and pre-session rendering plus existing refresh actions. [2]
- Capability derivation consumed by the pane is owned by `modelRowByKey`, `deriveEffortMenu`, and `effectiveSelection`. [3]
- The pane calls the derived-selection and effort-menu helpers and resolves the selected model row from that derived state. [4]
- Existing capability read clients. [5]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
