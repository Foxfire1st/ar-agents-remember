# mcp/tests/test_standalone_master_route.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Covers the repaired curator-coherence route for a task of a master that no sprint commands: the
production status, prepare, publish and validate operations act on the real external-memory leaf,
and the memory-quality readiness join reaches closeout readiness.

## Code Commentary

### Logic

`_standalone` writes the fixture's master and leaf, marks the master atomic and removes its sprint, so
the master stands alone. The publication case drives `curator_coherence_action` through status,
prepare, publish and validate with the master as the declared caller; the readiness case drives
`_attach_coherence_readiness` and requires `closeoutReady: true` and `coherenceStatus: current`.
On the base tree the same cases refuse with `task-document-parent-missing`.

### Conventions

The cases use the external contract fixture and the curator-coherence and memory-quality test
support; they do not invent a sprint for the standalone master.

### Invariants And Boundaries

A standalone master's coherence record can be published and read current, and the readiness join
reaches closeout readiness without a sprint. This is test evidence about the route, not a closeout or
integration acceptance.

## Evidence

- Status, prepare, publish and validate act on a standalone master's task and validate current. [1]
- The memory-quality readiness join reaches closeout-ready and current coherence for a standalone master's task. [2]
