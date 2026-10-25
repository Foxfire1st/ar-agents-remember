# mcp/tests/test_projection_incremental.py

## Governing Overview

[governing overview](overview.md)

## Purpose

MIK-R81 rule 2 (F09): path-directed incremental projection, no full-bore refresh.

## Code Commentary

The suite checks documentary draft skips the downstream cascade; structural task change flips the cascade; noop passes reach no surface reader until the ttl lapses. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence


- MIK-R81 rule 2 (F09): path-directed incremental projection, no full-bore refresh. [1]
