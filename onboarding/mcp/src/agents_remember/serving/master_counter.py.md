# mcp/src/agents_remember/serving/master_counter.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The series counter's lean projection of the same native commit-range rows.

## Code Commentary

The counter reads the same native commit-range rows the rest of the surface reads, projected leanly, so the counter cannot disagree with the ranges it counts. Busy preparation is named rather than reported as an empty count.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- CounterReader reads the counter from the native rows and names a busy preparation. [1]
