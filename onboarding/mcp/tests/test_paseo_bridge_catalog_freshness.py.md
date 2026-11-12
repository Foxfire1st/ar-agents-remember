# mcp/tests/test_paseo_bridge_catalog_freshness.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks the real JavaScript bridge against a fake Paseo client, keeping successful empty catalog answers distinct from unavailable parts.

## Code Commentary

The fixture extends AgentCommandScriptTests with controlled provider discovery, model, feature and configuration responses. Cases assert that a failed part is omitted with its own error while successful parts survive. A discovery deadline can use the available provider snapshot; an unanswered discovery and snapshot still fail. Metadata mode reads no model features, and selected mode asks only the named provider/model, even when metadata is unavailable. Explicit refresh invokes the provider refresh; ordinary questions still reach Paseo.

## Invariants And Boundaries

These are source assertions over the real bridge and a fake client, not a report of executing against a live Paseo host. A timeout is never asserted to mean that the provider offers an empty list.

## Evidence

### Repo-Internal References

- Successful empty lists retain read time; ordinary and refresh questions reach the provider boundary. [1]
- Model, mode, effort, feature and tool-server failures stay distinct from valid parts. [2]
- Unavailable discovery fails; an available provider snapshot can survive a discovery wait. [3]
- Timed-out model, feature and configuration parts remain unknown while other answers survive. [4]
- Metadata mode reads provider/model metadata without querying features. [5]
- Selected mode queries only the chosen model and names unanswered feature parts. [6]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
