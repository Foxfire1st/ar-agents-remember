# mcp/test_support/agents_remember_test_support/testing/evidence_governance.py

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Owns the threshold-aware discovery predicate for durable evidence and test-support artifacts.

## Code Commentary

### Logic

`governed_artifact_paths` walks configured test roots and selects non-test Python support,
known durable data suffixes, policy manifests, task/date-shaped proof, and any non-Python file at
or above the configured byte threshold. Python source remains governed by source/file-size rails,
so the fixture threshold cannot accidentally reclassify ordinary implementation files. The
lifecycle catalog is the policy input that supplies the threshold and is explicitly outside its
own artifact population; otherwise a sufficiently large catalog would recursively require an
entry in itself.

### Conventions

The configured threshold is positive and operational. Unknown suffixes are governed by size rather
than falling through a fixed extension allowlist.

### Invariants And Boundaries

- Discovery is repository-relative and returns one exact path set.
- A non-positive threshold refuses instead of disabling large-fixture governance.
- The lifecycle catalog must exactly cover this discovered population.
- The lifecycle catalog is not a durable evidence artifact governed by itself.
- No compatibility suffix list shadows this predicate.

### Todos

None recorded.

## Evidence

### Docs References

No external domain documentation governs this repository-owned predicate.

### Repo-Internal References

- Discovery combines support, durable suffix, policy, task/date, and configured-size authority while excluding the lifecycle catalog policy input. [1]
- The lifecycle validator consumes this exact predicate. [2]

### Cross-Repo References

No cross-repository boundary applies.
