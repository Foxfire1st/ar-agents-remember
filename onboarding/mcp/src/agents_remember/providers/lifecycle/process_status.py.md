# mcp/src/agents_remember/providers/lifecycle/process_status.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/process_status.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC process lifecycle uses namespace gates, liveness checks, and command-line inspection. | [process.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/process.py) |
| Aggregate watcher lifecycle reports namespace durability before starting enabled providers. | [watchers.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/watchers.py) |

## Update History

- 2026-05-31T12:30+02:00 — Removed `process_alive`, `windows_process_alive`, and `process_cmdline` (and the now-unused `ctypes`/`sys` imports); module now owns only namespace safety checks (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Added a `sys.platform != 'win32'` guard in `windows_process_alive` so the Windows-only `ctypes.windll`/`get_last_error` type-check; behavior-preserving (commit `0549b28`).
- 2026-05-28T13:40+02:00: Updated after provider venv Python path resolution was removed.
- 2026-05-25T21:14+02:00: Created from the process/namespace portion of the former shared lifecycle common module.
