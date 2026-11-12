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
260703-L13 there is no coordination-root fallback, so watcher commands need an
explicit settings path), maps generic watcher actions to provider-specific
actions, calls GrepAI or CGC lifecycle
functions, normalizes provider errors into structured results, and collects
recovery actions from partial failures. The action maps carry the stop family
only: `grepai` maps `stop` and `shutdown-all` to `stop`, and `cgc` maps them to
`stop-all` and `shutdown-all`. Non-dry-run stop actions require a durable process
namespace, and combined success is computed from the included provider results.

### Invariants And Boundaries

- Watcher aggregation should not perform provider-specific Docker or CGC work
  itself.
- A watcher action outside the stop family has no branch here: `status` and
  `start` were removed with the provider surface.
- Stop and shutdown-all actions must respect durable process namespace checks.
- Partial provider failures should be reported as structured lifecycle results,
  not hidden.

## Evidence

### Repo-Internal References

- GrepAI watcher behavior lives in the Docker runner module. [1]

- The CGC aggregate branch imports cgc_stop_all and maps only stop/shutdown-all to the retained stop closure; it imports no start or status aggregator. [2]

- The backend module retains cgc_backend_status as an internal implementation. watchers_run combines stop-class action results and does not fold backend status into an aggregate status response. [3]
