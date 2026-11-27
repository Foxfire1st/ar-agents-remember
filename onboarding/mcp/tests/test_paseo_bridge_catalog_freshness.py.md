# mcp/tests/test_paseo_bridge_catalog_freshness.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks the real JavaScript bridge against a fake Paseo client, keeping successful empty catalog answers distinct from unavailable parts.

## Code Commentary

The fixture extends AgentCommandScriptTests with controlled provider discovery, model, feature and configuration responses. Cases assert that a failed part is omitted with its own error while successful parts survive. A discovery deadline can use the available provider snapshot; an unanswered discovery and snapshot still fail. Default and explicit metadata requests skip model features. The six-provider fixture lists all 350 models in the returned catalogue and checks Refresh runs before discovery. Selected mode requests only the named pair, even when metadata is unavailable. Creation with a supplied feature value validates it against one model and submits one create request.

## Invariants And Boundaries

These are source assertions over the real bridge and a fake client, not a report of executing against a live Paseo host. A timeout is never asserted to mean that the provider offers an empty list.

## Evidence

### Repo-Internal References

- Successful empty lists retain read time and projected launcher daemonConfig (profiles and provider options/params without env); ordinary and refresh questions reach the provider boundary. [1]

- Model, mode, effort and tool-server failures leave other metadata parts available. [2]

- Unavailable discovery fails; an available provider snapshot can survive a discovery wait. [3]

- Timed-out model listing and tool-server configuration leave another provider’s model available. [4]

- Metadata mode reads provider/model metadata without querying features. [5]

- One selected-model query distinguishes offered, explicitly empty, unavailable and timed-out feature answers. [6]


## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
