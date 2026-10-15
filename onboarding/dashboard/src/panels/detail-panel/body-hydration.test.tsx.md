# dashboard/src/panels/detail-panel/body-hydration.test.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Declare mounted DetailPanel regression assertions for restoring nonGoals and acceptance from on-demand body content for an ordinary master and a task.

## Code Commentary

The source identifies its literal summary/body pairs as native F01 producer operands from L162-F01-native-reader-operands.json. Both summaries omit nonGoals and acceptance; each body supplies those fields, objective, design and a legacy freeform section at the same bodyRevision. The two pairs crossed with the two fixed-prose fields declare four cases. This inspection does not independently reproduce that historical producer opportunity. [1]

Each case seeds only the summary, mounts DetailPanel by its exact taskdoc:docPath key, and stubs the /api/task-document? transport with the body while retaining the ancillary fetch stub. Assertions check the requested canonical path, restored nonGoals/acceptance/design, objective → nonGoals → design → acceptance block order, reachable legacy Further notes, and exactly one body request. This exercises the production summary-to-body hydration composition when run; it is distinct from directly hand-populating fixed prose in renderer input fixtures. [2] [3] [4] [5] [6]

## Boundaries

Source inspection only: no fresh test, native producer/server request or acceptance was run here. HTTP is stubbed, ancillary counters are fixture stubs, and these cases do not assert stale-revision ownership, failures, request priority, or analytics churn. Those claims stay with their separate controls. No task state or lifecycle authority is authored by this module.

## Evidence

- Operand declarations, four-case parameterization and same-revision/missing-summary-field assertions. Source-defined assertions; not fresh execution. [1]

- Stubbed body-request path assertion and mounted exact selection key. Source-defined assertions; not fresh execution. [2]

- Body-only fixed prose and design restoration assertions. Source-defined assertions; not fresh execution. [3]

- Fixed-block adjacency assertions. Source-defined assertions; not fresh execution. [4]

- Legacy freeform content remains reachable through Further notes. Source-defined assertions; not fresh execution. [5]

- Exactly one task-document request is asserted. Source-defined assertions; not fresh execution. [6]
