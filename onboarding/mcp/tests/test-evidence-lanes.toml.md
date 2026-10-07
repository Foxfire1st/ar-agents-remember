# mcp/tests/test-evidence-lanes.toml

## Governing Overview

[tests route overview](overview.md)

## Purpose

The canonical evidence-lane catalog: which test modules belong to which lane, so a leaf's checks can
name the population they ran.

## Code Commentary

### Logic

MIK-R79 adds `mcp/tests/test_knowledge_reader_tree_coverage.py` to the `unit-regression` lane, since
the coverage module's tests are a unit-regression obligation. No other lane or module changes.

### Conventions

TOML lists, one module path per row, kept sorted within the lane.

### Invariants And Boundaries

Both test catalogs stay in one canonical form; every loader refuses a duplicate or malformed entry.
A new test module that belongs to a lane is added here in the same pass.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1`; it lives outside the code and memory repositories, so it is named
here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The new module joins this lane. [19]
- The module the lane names. [20]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
