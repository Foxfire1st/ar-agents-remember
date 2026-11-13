# mcp/tests/test_semantic_topology_standalone.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Covers the sprint-less branch of `semantic-topology/v2`: a task of a master that no sprint commands
gets a stable atomic projection, and the sprint case keeps its existing canonical value.

## Code Commentary

### Logic

`test_a_standalone_master_fingerprint_is_stable_and_differs_from_its_sprint_case` projects the same
fixture with a null sprint twice, requires equal fingerprints, and requires the result to differ from
the fixture's sprint-bound fingerprint. `test_the_sprint_cases_fingerprint_is_unchanged` pins the
sprint-bound projection with and without an execution graph to values computed on the clean base
tree, so a change to the sprint case's canonical value fails here.

### Conventions

The cases reuse the closeout projection member helpers and compare fingerprints only; they do not
execute a closeout or publish a coherence record.

### Invariants And Boundaries

A standalone master's null sprint is the atomic placement, and every sprint case's canonical value
must stay byte-stable. The file asserts projection behavior, not acceptance of a task.

## Evidence

- A standalone master's fingerprint is stable across runs and differs from the same documents' sprint case. [1]
- The sprint case's fingerprint is pinned unchanged with and without an authored graph. [2]
