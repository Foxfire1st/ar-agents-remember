# mcp/src/agents_remember/providers/cgc/lifecycle/query.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/query.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `e1382b9277d48f13b6a1cb065f2fa2638b36feba` |
| lastVerifiedCommitDate | 2026-05-29T07:08:19+02:00|
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
inside the CGC Docker runner with captured output, builds Dockerized visualizer
server commands, validates ports, and runs visualizer foreground commands only
after durable namespace checks.

### Invariants And Boundaries

- `cgc run` is only for bounded native commands and must reject visualizer
  server startup.
- `cgc visualize` is the explicit long-running server command and requires a
  durable process namespace.
- Watcher start/stop behavior lives in `process_control.py`.
- Query and visualizer execution must use the Docker runner image, not a host
  `cgc` executable.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC status checks are provided by the installation module. | [installation.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/installation.py) |
| Docker command construction is provided by the runner module. | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py) |
| Provider lifecycle tests cover visualizer rejection, dry-run visualize command construction, and bounded `cgc run`. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-26T12:51+02:00: Updated after bounded CGC run and visualizer commands moved into the Docker runner.
- 2026-05-25T21:14+02:00: Split from `process.py` so bounded query and visualizer behavior is separate from watcher process control and refresh.
