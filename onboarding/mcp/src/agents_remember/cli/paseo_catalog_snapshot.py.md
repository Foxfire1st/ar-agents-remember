# mcp/src/agents_remember/cli/paseo_catalog_snapshot.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Serves saved catalog data while a fresh launcher question is pending.

## Code Commentary

### Logic

`register_saved_catalog_route` registers GET /api/role-launch/saved-catalog. It returns agents, catalogDiscovery and catalogOrigin from the shared saved reader without querying Paseo or deciding whether to start. Named bridge configuration errors use the existing HTTP error mapping.

## Repo-Internal References

- The source implements the behavior and boundaries described above. [1]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
