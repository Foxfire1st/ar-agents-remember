# mcp/tests/test_observer_no_computed_counter.py

## Governing Overview

[overview](overview.md)

## Purpose

Regression module pinning the removal of the computed token counter: projection
models carry no token fields, the served schema carries none, `tool.completed`
tokens never fold into a lifecycle, a store write over an old-field file reads
back clean, and workspace metrics carry no token total. Old-field fixtures and
absent-name assertions live here as the permitted test-side literals.

## Code Commentary

`NoComputedCounterTests` holds the five cases: model-field absence, served-schema
absence, the no-fold behavior, the old-field store-overwrite readback, and the
metrics absence. Event-level `tokens` inputs stay as fixtures proving the
projection folds nothing from them.

## Evidence

- Projection models carry no token fields. [1]
- The served schema carries no token fields. [2]
- `tool.completed` tokens do not fold into the lifecycle. [3]
- A store write over an old-field file reads back clean. [4]
- Workspace metrics carry no token total. [5]
