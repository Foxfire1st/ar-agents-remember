# mcp/src/agents_remember/cli/paseo_catalog_features.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Asks only the finally selected model for its features during a start.

## Code Commentary

### Logic

`selected_model_features` reuses full or already fresh feature data; otherwise it asks the bridge in selected mode for the final provider/model. The current operation deduplicates the target in feature_answers. The answer and a named bridge failure both pass through the shared durable per-part merger; this owner creates no second persistent offer cache.

## Repo-Internal References

- The source implements the behavior and boundaries described above. [1]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
