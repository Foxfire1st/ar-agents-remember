# dashboard/src/panels/detail-panel/body-hydration.test.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Declare mounted DetailPanel regression assertions for restoring nonGoals and acceptance from on-demand body content for an ordinary master and a task.

## Code Commentary

The source identifies its literal summary/body pairs as native F01 producer operands from L162-F01-native-reader-operands.json. Both summaries omit nonGoals and acceptance; each body supplies those fields, objective, design and a legacy freeform section at the same bodyRevision. The two pairs crossed with the two fixed-prose fields declare four cases. This inspection does not independently reproduce that historical producer opportunity. [1]

Each summary is wrapped in TaskEntry and selected by its qualified taskdoc key. The body stub checks the canonical qualified key, not absolute docPath. NonGoals/acceptance/design, fixed prose order, Further notes and exactly one body request remain hydration-composition assertions, not direct full-body renderer setup. [2] [3] [4] [5] [6]

## Boundaries

Source inspection only: no fresh test, native producer/server request or acceptance was run here. HTTP is stubbed, ancillary counters are fixture stubs, and these cases do not assert stale-revision ownership, failures, request priority, or analytics churn. Those claims stay with their separate controls. No task state or lifecycle authority is authored by this module.

## Evidence

- Operand declarations, four-case parameterization and same-revision/missing-summary-field assertions. Source-defined assertions; not fresh execution. [1]

- Stubbed body-request path assertion and mounted exact selection key. Source-defined assertions; not fresh execution. [2]

- Body-only fixed prose and design restoration assertions. Source-defined assertions; not fresh execution. [3]

- Fixed-block adjacency assertions. Source-defined assertions; not fresh execution. [4]

- Legacy freeform content remains reachable through Further notes. Source-defined assertions; not fresh execution. [5]

- Exactly one task-document request is asserted. Source-defined assertions; not fresh execution. [6]
