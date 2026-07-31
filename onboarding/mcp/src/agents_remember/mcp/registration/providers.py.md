# mcp/src/agents_remember/mcp/registration/providers.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/mcp/registration/providers.py`       |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-07-31T15:31+02:00                                        |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                    |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[registration route overview](overview.md)

## Purpose

`register_provider_tools(server, config)` declares the three provider-control tools:
`provider_status`, `provider_diagnostics`, `provider_watchers`.

## Code Commentary

### Logic

The smallest family, and the split is deliberate: `provider_status` is the compact readiness summary
(per-provider ready/degraded/stopped, watcher up, indexing state; `noProviders` when none are
enabled), and `provider_diagnostics` is the escape hatch for raw provider-native detail (container
states, ports, backend/embedder health, ping output) used when status reports degraded. Keeping the
raw internals behind the second tool is what stops `context_packet` and `provider_status` from
growing into diagnostics dumps.

`provider_watchers(action, dry_run=False)` documents its action vocabulary in the docstring because
two of the actions are not interchangeable: `restart` stops and starts the watchers, which then pick
changes up through their incremental scan **without** rebuilding indexes (the way to wake a stale
watcher), while `invalidate-indexes` DELETEs and rebuilds every index from scratch — a full re-embed
plus a full graph re-index, slow and CPU-heavy. The retired `refresh` action is not listed; the
controller rejects it with guidance. Indexing runs inside the watcher and is never time-capped.

All three forward keyword-for-keyword to `mcp/tools/providers.py`; the diagnostics and watcher
payloads are report-filed and compacted there, not here.

### Invariants And Boundaries

- Keep raw provider troubleshooting behind `provider_diagnostics`.
- `provider_watchers` is mutating except `action="status"`, and registers `dry_run=False`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The payload builders and their compact/report-filing helpers. | [tools/providers.py](agents-remember/mcp/src/agents_remember/mcp/tools/providers.py) |
| Watcher action handling and the `refresh` rejection. | [controllers/provider_tools.py](agents-remember/mcp/src/agents_remember/controllers/provider_tools.py) |

## Update History

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The three provider
  declarations moved out of `server.py` unchanged. Verification metadata pinned to the pre-change
  commit until closeout stamps the L2 code commit.
