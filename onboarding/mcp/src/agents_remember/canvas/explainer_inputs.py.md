# mcp/src/agents_remember/canvas/explainer_inputs.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The product-side facts one explainer tool server needs beside its workspace, in a module light enough for a registration entry to import while it is being discovered.

## Code Commentary

- `ExplainerInputs` carries the task folder, the coordination root, both repositories, and takes the fingerprint reader, the report sender and the clock as injectable callables, so a tool server composes without a host.
- `coordination_of` reads `<coordination>/explainer/<repository>/<task>/<leaf>` back to its coordination root, and refuses `workspace-unplaced` for a path too shallow to be one.
- `now_iso` answers whole seconds in UTC, so a stored timestamp and its rendered form cannot disagree about the moment.
- The class and both helpers are the same objects the tool server re-exports, so a caller's import path and a discovery-time import cannot diverge.

## Evidence

- The tool server's inputs are one frozen record, with the root, both repositories and the effectful readers supplied by the caller [1]
- A workspace too shallow to be an explainer placement is refused rather than read as a coordination root [2]
- One clock, in UTC, to whole seconds, is what every stored moment is stamped with [3]
