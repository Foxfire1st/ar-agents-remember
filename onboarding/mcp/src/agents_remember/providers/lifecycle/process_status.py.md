# mcp/src/agents_remember/providers/lifecycle/process_status.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/process_status.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T13:40+02:00                     |
| lastVerifiedCommitHash | `3f09b75461760479b443f1b04b180772724e7a24` |
| lastVerifiedCommitDate | 2026-05-28T15:10:01+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`process_status.py` owns process namespace safety checks, process liveness, and
process command-line inspection for provider lifecycle commands.

## Code Commentary

### Logic

The module detects ephemeral PID namespaces supervised with `--die-with-parent`,
reports whether the namespace is durable for daemon processes, enforces the
durable namespace gate for long-running actions, checks PID liveness on POSIX
and Windows, and reads `/proc/<pid>/cmdline` when available. It no longer
resolves provider venv Python paths.

### Invariants And Boundaries

- Watcher/process starts must fail fast in ephemeral namespaces.
- Process checks provide facts only; provider modules decide whether stale state
  should be cleaned or reused.
- This helper must not reintroduce host venv executable path resolution for
  managed providers.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC process lifecycle uses namespace gates, liveness checks, and command-line inspection. | [process.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/process.py) |
| Aggregate watcher lifecycle reports namespace durability before starting enabled providers. | [watchers.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/watchers.py) |

## Update History

- 2026-05-28T13:40+02:00: Updated after provider venv Python path resolution was removed.
- 2026-05-25T21:14+02:00: Created from the process/namespace portion of the former shared lifecycle common module.
