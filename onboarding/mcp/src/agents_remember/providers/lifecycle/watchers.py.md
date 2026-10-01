# mcp/src/agents_remember/providers/lifecycle/watchers.py

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`watchers.py` aggregates enabled provider watcher lifecycle operations across
GrepAI and CodeGraphContext.

## Code Commentary

### Logic

The module reads provider enablement from lifecycle settings
(`context_provider_enabled` with the explicit `--from-settings` path — since
260703-L13 there is no coordination-root fallback, so watcher commands need the
generated settings file), maps generic watcher actions to provider-specific
actions, calls GrepAI or CGC lifecycle
functions, normalizes provider errors into structured results, and collects
recovery actions from partial failures. Non-dry-run long-running actions require
a durable process namespace. CGC aggregate status now includes FalkorDB backend
status, and the provider-level `ok` flag requires both backend health and all
configured repo watchers to be ok.

### Invariants And Boundaries

- Watcher aggregation should not perform provider-specific Docker or CGC work
  itself.
- CGC watcher status must include the shared backend status so current provider
  state can distinguish repo watcher health from FalkorDB health.
- Start/stop/shutdown actions must respect durable process namespace checks.
- Partial provider failures should be reported as structured lifecycle results,
  not hidden.

## Evidence

### Repo-Internal References

- GrepAI watcher behavior lives in the Docker runner module. [1]
- CGC start/stop/status behavior lives in the CGC process-control and installation modules. [2]
- CGC backend status is reported through the backend module and folded into watcher aggregate status. [3]
