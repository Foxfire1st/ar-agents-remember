# scripts/agent_evals/adapters/text_delivery.py

## Governing Overview

[overview](../overview.md)

## Purpose

Binds frozen details through the production composer and observes the instruction-only marker in native received fields.

## Code Commentary

### Invariants And Boundaries

Outbound configuration alone is not receipt evidence. Secret-named or symlink inputs refuse marker proof before reading.

Binding replays the captured instruction origins, reads every emitted detail file and refuses unless each one is ready; the bound delivery carries those read bytes as its frozen contents for later detail-read checks.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]

- Binding validates captured instruction origins, reads each emitted detail file, refuses any detail that is not ready and returns the read bodies as frozen contents. [2]
