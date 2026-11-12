# mcp/tests/test_observer_no_computed_counter.py

## Governing Overview

[overview](overview.md)

## Purpose

Regression module pinning the removal of the computed token counter: projection
models carry no computed token fields, the served schema carries none, a store
write over an old-field file reads back clean, and workspace metrics carry no token total. Old-field fixtures and
absent-name assertions live here as the permitted test-side literals.

## Code Commentary

`NoComputedCounterTests` checks model/schema absence, old-field store-overwrite readback and metrics absence. Metrics has no totalTokens, TaskEntry has no seriesTokenTotal, and token helper names remain absent. The old persisted fixture is overwritten with a task/enclosure projection that contains neither legacy token fields nor a lifecycles root; there is no remaining lifecycle-event fold case.

## Evidence


- Projection models carry no token fields. [1]

- The served schema carries no token fields. [2]

- A store write over an old-field file reads back clean. [4]


- Workspace metrics carry no token total. [5]
