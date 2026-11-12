# mcp/src/agents_remember/cli/paseo_catalog_parts.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Separates catalog part success from unanswered data before persistence.

## Code Commentary

### Logic

`merge_reply` merges provider identities, model identities, modes, tool-server support, efforts, features and service tiers independently. An empty successful list remains known-empty; a missing or failed list may use its saved answer and otherwise stays unknown. `merge_selected_reply` accepts selected features only for the named provider/model and reuses the same part store.

## Repo-Internal References

- The source implements the behavior and boundaries described above. [1]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
