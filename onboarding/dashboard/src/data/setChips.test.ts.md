# dashboard/src/data/setChips.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Pure regression suite for all shared set-chip, queued-hint, and attention derivations.

## Code Commentary

### Logic

Cases cover quiet state, honest ~35-second in-flight copy, coexisting queued/unknown pendings,
clamp, unsupported, acknowledgment suppression, pair progress/partial outcomes, route retry
classes, composer hints, and attention gates. The evidence-backed unsupported sibling remains
pinned beside the fix-round-3 route-unknown behavior.

### Conventions

Minimal `PerSessionCockpit` builders isolate presentation derivation from I/O.

### Invariants And Boundaries

Test-only; production path route failures are also asserted in `setClient.test.ts`.

### Todos

The two documented sev-4 presentation edges are not closed by this suite.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Pure presentation model under test. [1]
- Pair copy/provenance source. [2]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo evidence applies.

## 260715-FEUI-L5 Reliable Submit Delta

No set-chip behavior changed. The test fixture gained the required empty `submitHistory` field so it
continues to construct the expanded cockpit session state without claiming any relationship between
model/effort chips and prompt lifecycle authority.
