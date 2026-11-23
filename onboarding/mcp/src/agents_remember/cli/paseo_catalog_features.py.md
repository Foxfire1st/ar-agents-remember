# mcp/src/agents_remember/cli/paseo_catalog_features.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Reads features for the shown provider and model in the panel and for the resolved pair during Start.

## Code Commentary

### Logic

`launcher_model_options` asks the bridge directly for the supplied provider and model and returns the pair’s public controls and provenance. The pane owns reuse across requests. During Start validation, `selected_model_features` uses fresh exact-pair data when available and memoizes an on-demand answer in the operation’s `LauncherCatalog.feature_answers`. Both readers merge answers and named bridge failures into the same runtime-scoped durable part store.

## Repo-Internal References


- The options route projects one pair. Start deduplicates selected feature reads within its operation. Both use the runtime-scoped durable result merger. [1]


## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
