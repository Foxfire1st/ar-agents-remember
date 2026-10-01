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

- Watcher/process starts must fail fast in ephemeral namespaces.
- This helper must not reintroduce host venv executable path resolution for
  managed providers, nor PID liveness or `/proc/<pid>/cmdline` inspection.

## Evidence

### Repo-Internal References

- CGC process lifecycle uses namespace gates, liveness checks, and command-line inspection. [1]
- Aggregate watcher lifecycle reports namespace durability before starting enabled providers. [2]
