# scripts/canvas-panel-probe.tsx

## Governing Overview

[governing route overview](../overview.md)

## Purpose

A development probe that mounts the canvas panel against a stubbed transport for manual inspection; it is not product code and asserts nothing.

## Code Commentary

- It is a developer-run witness, not product runtime code: nothing in the serving path imports it.
- Its value is the record it produces, which the proof consumer reads.

## Evidence

- This script is a proof/inspection harness, not product runtime code. [1]
