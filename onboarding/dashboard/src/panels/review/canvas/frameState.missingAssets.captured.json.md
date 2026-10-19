# dashboard/src/panels/review/canvas/frameState.missingAssets.captured.json

## Governing Overview

[governing route overview](../../overview.md)

## Purpose

A recorded canvas frame-state answer used by the panel's cases: the frame state of a saved page whose assets are unavailable.

## Code Commentary

- It is a fixture, not a live answer: the panel's own cases read it to reproduce a server response exactly.
- It carries the same fields the API serves, so a change in the served shape surfaces in the panel's cases.

## Evidence

- The recorded answer the frame state of a saved page whose assets are unavailable. [1]
