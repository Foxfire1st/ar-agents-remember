# dashboard/src/panels/engine-room/engineRoomTypes.ts

## Governing Overview

[engine-room overview](overview.md)


## Current enclosure-only composition

EngineRoomModel has processes only. EngineProcessView contains enclosureKey and node; there is no optional lifecycle/gate field or ProviderNode/EngineStack import.

### Maintenance boundaries



Source/test/fixture inspection is not a fresh mounted capture or a passing test run.
Historical provider-shaped input data and retained compatibility definitions do not
restore removed provider visuals or tool exposure.


## Historical superseded account (non-operative)

The prior onboarding below is retained for provenance and unrelated design history.
It is not current provider-render, fallback, prototype-parity or execution guidance.
Current behavior and its limits are the operative contract above.





## Code Commentary

### Logic

Two exported interfaces, both pure type declarations (no runtime code).

- EngineProcessView carries node and stable enclosureKey equal to node.worktreeGroup.
- EngineRoomModel carries processes only, in the deterministic order the pure builder returns.

### Invariants And Boundaries

- Type-only EngineProcessNode import; enclosureKey is worktreeGroup, not node.id.
- Builder phase ordering is not semantic inference.

## Evidence

### Repo-Internal References

- EngineProcessNode is the generated projection contract consumed by this surface. [3]
