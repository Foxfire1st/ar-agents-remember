# mcp/tests/test_pacer_healing.py

## Governing Overview

[governing overview](overview.md)

## Purpose

MIK-R81 rules 5/6 (F05/F06): healing wakes and invalidation acknowledgement.

## Code Commentary

The suite checks continuous partial traffic still heals on time; misaligned heartbeat never overshoots the heal bound; failed full wake does not advance the heal bound; failed change tick keeps its domains; arrival during work keeps the merged set; cancelled tick keeps queued domains. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- MIK-R81 rules 5/6 (F05/F06): healing wakes and invalidation acknowledgement. [1]
