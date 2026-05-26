# mcp/src/agents_remember/providers/cgc/lifecycle/query.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/query.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`query.py` owns bounded native `cgc run` commands and explicit CGC visualizer
lifecycle commands.

## Code Commentary

### Logic

The module strips native args after `--`, rejects `visualize` through bounded
`run`, checks status before live commands, executes bounded native commands
with captured output, builds visualizer server commands, validates ports, and
runs visualizer foreground commands only after durable namespace checks.

### Invariants And Boundaries

- `cgc run` is only for bounded native commands and must reject visualizer
  server startup.
- `cgc visualize` is the explicit long-running server command and requires a
  durable process namespace.
- Watcher start/stop behavior lives in `process_control.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC status checks are provided by the installation module. | [installation.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/installation.py) |
| Provider lifecycle tests cover visualizer rejection, dry-run visualize command construction, and bounded `cgc run`. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-25T21:14+02:00: Split from `process.py` so bounded query and visualizer behavior is separate from watcher process control and refresh.
