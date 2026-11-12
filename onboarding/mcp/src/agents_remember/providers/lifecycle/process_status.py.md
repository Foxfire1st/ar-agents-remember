# mcp/src/agents_remember/providers/lifecycle/process_status.py

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`process_status.py` owns process namespace safety checks for provider lifecycle
commands.

## Code Commentary

### Logic

The module detects ephemeral PID namespaces supervised with `--die-with-parent`,
reports whether the namespace is durable for daemon processes, and enforces the
durable namespace gate for long-running actions. It no longer checks PID
liveness, reads `/proc/<pid>/cmdline`, or resolves provider venv Python paths.

### Invariants And Boundaries

- Lifecycle actions using the durable-namespace guard fail fast in ephemeral namespaces; the retained CGC and aggregate watcher consumers enforce it for real stop-class actions.
- This helper must not reintroduce host venv executable path resolution for
  managed providers, nor PID liveness or `/proc/<pid>/cmdline` inspection.

## Evidence

### Repo-Internal References

- The retained CGC stop path uses the shared durable-process-namespace gate. process_status.py does not inspect provider PID liveness or /proc/<pid>/cmdline; Docker watcher inspection remains with the runner helper. [1]

- Watcher aggregation applies durable-namespace checks to non-dry-run stop and shutdown-all actions. Aggregate start/status branches are absent. [2]
