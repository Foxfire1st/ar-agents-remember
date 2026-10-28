# mcp/src/agents_remember/canvas/explainer_inputs.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The product-side facts one explainer tool server needs beside its workspace, in a module light enough for a registration entry to import while it is being discovered.

## Code Commentary

- `ExplainerInputs` carries the task folder, the coordination root, both repositories, and takes the fingerprint reader, the report sender and the clock as injectable callables, so a tool server composes without a host.
- `now_iso` answers whole seconds in UTC, so a stored timestamp and its rendered form cannot disagree about the moment.
- The tool server re-exports the class only: its `__all__` names `ExplainerInputs`, and `now_iso` is imported for its own use [2]

## Evidence

- The tool server's inputs are one frozen record, with the root, both repositories and the effectful readers supplied by the caller [1]
- One clock, in UTC, to whole seconds, is what every stored moment is stamped with [3]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/explainer_inputs.py:46-54 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
