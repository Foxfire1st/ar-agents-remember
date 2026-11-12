# mcp/src/agents_remember/providers/setup_progress.py

## Governing Overview

[providers overview](../../../overview.md)

## Purpose

Retained phase-progress reporting for internal provider setup and old progress artifacts (GitHub #53). The sink, heartbeat-stamped file and compact status reader survive. `worktree_status` can still report an existing progress file; the retired provider dashboard is not a current consumer, and both retired identities are disabled for new setup.

## Code Commentary

### Logic

`SetupProgress` is the no-op sink interface provider setup announces through:
`phase_start(provider, action, note=, seed_fallback=)`, `phase_update(metrics)`
(reserved for future per-item indexing progress — `itemsDone/itemsTotal/
percent/unit`; nothing fills it yet because subprocess output is captured at
completion, not streamed), and `phase_done(result)`.

`SetupProgressFile` persists every event as JSON (schema
`ar-provider-setup-progress/v1`) with top-level identity fields
(`repoName`, `taskName`, `worktreeGroup`) so dashboards need not parse paths.
A daemon ticker thread refreshes `updatedAt` every `HEARTBEAT_SECONDS` (15s)
while setup runs; `finish(state, error=, summary=)` stops the ticker and
records the terminal state. The clock is injectable for tests. Write errors
are remembered (`progressWriteError`) instead of raised: progress reporting
must never fail the setup it observes.

`read_setup_progress(path)` returns the dict or None (absent/unreadable/not
schema v1). `progress_status(progress)` projects the compact status shape the
tools report: `running` carries `currentPhase` (+`elapsedSeconds`),
`heartbeatAgeSeconds`, `seedFallback`, and compact `completedPhases` lines; a
heartbeat older than `STALE_AFTER_SECONDS` (90s = six missed beats) projects
as `stale` — the writer died, so readers should offer retry rather than wait.
Terminal states pass through (`ok`, `ready-with-failed-phases`, `failed`,
`failed-unchecked` — the `setup_reporting.setup_state` vocabulary) with
`failedPhases` lines.

### Invariants And Boundaries

- Progress reporting must never raise into the provider setup chain.
- `stale` is a READER projection of a fresh-state `running` file, never a
  written state; the heartbeat is the only liveness signal.
- Retained progress files keep their identity fields and reserved `currentPhase.metrics` shape. Internal/old-artifact readers do not establish a current provider-dashboard contract; breaking file-schema changes still require a version change.
- `seedFallback` is written the moment the fallback phase starts, not after it
  finishes — surfacing the seconds→minutes expectation change is the point.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- Provider setup functions announce phases through `setup_progress_from(args)`. [1]
- The worktree launcher creates the file and finishes it from the setup payload. [2]

## Historical provider-surface wording

The following earlier wording is retained as provenance, not a current consumer or operation contract:

> Durable phase-progress reporting for background provider setup (GitHub #53):
> the observable that lets a model (or dashboard) watch a running setup instead
> of holding a multi-minute tool call open.
>
> - The schema is dashboard-facing: identity fields and the reserved
>   `currentPhase.metrics` shape must stay forward-compatible (bump the schema
>   version on breaking changes).

## Current retirement-boundary evidence

- The retained no-op sink and file schema preserve phase events and bounded write errors. [3]
- Retained progress projection computes heartbeat age, stale state, elapsed time and compact phase lines. [4]
- The old progress-file reader retains terminal/stale status and retry arguments. [5]
- Worktree status can include existing setup progress through the retained port. [6]
- The shared enablement predicate always disables the two retired provider identities. [7]
