# mcp/src/agents_remember/providers/lifecycle/process_status.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/process_status.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/providers/lifecycle/process_status.py` since the L2 base commit is the
  whole-tree `ruff format` pass in `00e8379`, which re-wrapped 1 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-05-31T12:30+02:00 — Removed `process_alive`, `windows_process_alive`, and `process_cmdline` (and the now-unused `ctypes`/`sys` imports); module now owns only namespace safety checks (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Added a `sys.platform != 'win32'` guard in `windows_process_alive` so the Windows-only `ctypes.windll`/`get_last_error` type-check; behavior-preserving (commit `0549b28`).
- 2026-05-28T13:40+02:00: Updated after provider venv Python path resolution was removed.
- 2026-05-25T21:14+02:00: Created from the process/namespace portion of the former shared lifecycle common module.
