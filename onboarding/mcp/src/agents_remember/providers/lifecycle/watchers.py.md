# mcp/src/agents_remember/providers/lifecycle/watchers.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/watchers.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T22:32+02:00                     |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| GrepAI watcher behavior lives in the Docker runner module. | `grepai_watcher_container_status` | mcp/src/agents_remember/providers/grepai/lifecycle/runner.py:81-107 |
| CGC start/stop/status behavior lives in the CGC process-control and installation modules. | `cgc_start`, `cgc_stop`, `cgc_status` | mcp/src/agents_remember/providers/cgc/lifecycle/installation.py:317-352; mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py:175-201; mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py:497-521 |
| CGC backend status is reported through the backend module and folded into watcher aggregate status. | ["def cgc_backend_status(args: argparse.Namespace)"], `watchers_run` | mcp/src/agents_remember/providers/cgc/lifecycle/backend.py:194-194; mcp/src/agents_remember/providers/lifecycle/watchers.py:186-205 |


## Update History

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 4 repository-internal watcher, CGC, backend, and aggregate-test references; final scoped result 0 (checker-clean).

- 2026-07-06T22:32+02:00 — 260703-L13 ride-along: `watcher_enabled_providers` calls
  `context_provider_enabled` without the dropped `coordination_root` parameter (the implicit
  coordinator-settings fallback was deleted; behavior with an explicit `--from-settings` is
  unchanged). Verification metadata pinned until closeout stamps the L13 commit.

- 2026-05-28T12:32+02:00: Updated after CGC watcher status began including FalkorDB backend health in aggregate status packets.
- 2026-05-26T12:51+02:00: Updated after watcher CGC args stopped carrying a Python executable and references moved to process-control/status modules.
- 2026-05-25T19:09+02:00: Updated references after CGC and GrepAI modules moved under package subfolders.
- 2026-05-25T19:01+02:00: Created from watcher aggregation logic extracted out of provider lifecycle.
