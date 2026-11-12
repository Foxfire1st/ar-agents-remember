# scripts/agent_evals/run_curator.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Dispatches the private eval preflight, census, regrade, trials, case, summary, comparison and text-capture commands.

## Code Commentary

### Invariants And Boundaries

The trial command calls trials.run_trials. The removed eval look-back command is absent; product memory-baseline functionality is a separate surface.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
