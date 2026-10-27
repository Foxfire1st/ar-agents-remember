# mcp/src/agents_remember/application/memory_quality/run_answers.py

## Governing Overview

[../overview.md](../overview.md)

## Purpose

Builds the four shared background-run response shapes used by scope-aware polling.

## Code Commentary

The module owns unfinished-run responses, candidate-pair refusals, scope projection and poll-scope mismatch. These functions were extracted from the quality controller so citation previews can use the same vocabulary and recovery fields. The controller still decides when each response applies; this module neither runs a check nor publishes memory.

### Invariants And Boundaries

A running/failed run response is distinct from a completed computation's quality verdict. Scope mismatches retain the admitted identity and shared quality-named recovery; the controller adapts that recovery for citation previews. No new approval or closeout gate is introduced.

## Evidence

- The response builders preserve shared poll and scope outcomes. [1]
