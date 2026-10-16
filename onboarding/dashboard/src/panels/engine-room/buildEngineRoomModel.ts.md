# dashboard/src/panels/engine-room/buildEngineRoomModel.ts

## Governing Overview

[engine-room overview](overview.md)


## Current enclosure-only composition

Builder takes engineProcesses alone, maps node/enclosureKey and sorts by projected phase priority then leafId/taskName. It returns processes only; no lifecycle/gate attachment, provider grouping or fallback. provider-setup remains a projected operation phase name.

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

`buildEngineRoomModel(engineProcesses)` is the sole export. It maps each node to {enclosureKey: node.worktreeGroup, node}, sorts by PHASE_ORDER with unknown phases last, then leafId or taskName, and returns {processes}. No workspace stack or fallback is synthesized; the adapter is pure, clock/React/Git-free and performs no safety inference.

### Invariants And Boundaries



## Evidence

### Repo-Internal References

- The `buildEngineRoomModel` projection function is exported here. [1]
- Each view assigns `enclosureKey` from `node.worktreeGroup`. [2]
- `EngineRoomModel` render shape [3]
- `EngineProcessView` render shape [4]
