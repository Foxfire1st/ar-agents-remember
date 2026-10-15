# mcp/tests/test_projection_path_directed.py

## Governing Overview

[governing overview](overview.md)

## Purpose

MIK-R81 rule 2 (F09): one-change reads ignore unrelated corpus size.

## Code Commentary

The suite checks documentary rewrite is path local and byte equal; append, delete and cross-document joins; lifecycle append is path local and byte equal; task/lifecycle atomic rewrites and deletes at both corpus sizes; new membership and cross-folder consumers at both sizes; closure validation ignores unrelated document count. The ordered-sibling regression breaks a retained two-child dependency cycle, compares the refreshed projection with a full reference, checks both directional dependency lists and the master frontier, and compares read sets at two unrelated-corpus sizes. This is a controlled assertion, not installed timing proof. The retired gate mutation case is absent with L113's removed gate projection. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- Current path-directed task/lifecycle cases compare bytes and read counts at both corpus sizes. The ordered-sibling case checks dependency lists and master frontier after breaking a cycle; the deleted gate-projection mutation is no current case. [1]
