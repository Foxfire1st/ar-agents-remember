# mcp/tests/test_workspace_wake_zero_census.py

## Governing Overview

[governing overview](overview.md)

## Purpose

L166-bound checks (L81-R1-F08/F09 added evidence, MIK-R81 rule 3 unchanged).

## Code Commentary

The two retained workspace-only wake cases check zero closeout walks, document relists, live fingerprints and worktree snapshots while retaining queue objects; unscoped and live touches still verify. Their probe.json input is an inert workspace file, not a health publisher. The five health-publisher assertion sites belonged to L113-deleted owners and are absent with that class. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- The two retained workspace-only wake cases assert zero closeout read/census calls and retained queue objects, while unscoped/live touches still verify; probe.json is an inert workspace input and no retired health-publisher case remains. [1]
