# dashboard/src/cockpit/RoleExecutionStatus.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The suite verifies the launcher's one failure line and selected-execution Result/Revive wiring.

## Code Commentary

The cases assert that a refused Start names its HTTP reason and clears only after a successful explicit Result, that an ordinary reply adds no reply text to the launcher's DOM (the bar's measured height is proved by the browser run, not by this suite), and that the unresolved-launch sentence appears without calling the agent failed. Host failure shows one line with its reason, and Revive appears only with canRevive. Launcher cases refresh another turn, name an explicit Result held by a launch, keep a held failure through automatic reads, and revive the exact selected request while retaining a refused alert.

## Invariants And Boundaries

These fixtures prove UI behavior rather than native actor resume or task acceptance. They pin the failure line's wording and the unchanged bar, not a pixel layout contract.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- Current source owner or exact assertion described above. [2]
- Current source owner or exact assertion described above. [3]
- Current source owner or exact assertion described above. [4]


### Clock And Settlement Evidence

- The held Result case enables fake time before mount, flushes each initial/result reply and advances the 1,500 ms reread in async `act`. It preserves the exact read count, absent report request and cleared failure/Start assertions after the reread opportunity; teardown restores real timers. [1]
