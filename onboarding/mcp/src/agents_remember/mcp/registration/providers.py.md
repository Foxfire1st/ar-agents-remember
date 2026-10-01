# mcp/src/agents_remember/mcp/registration/providers.py

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
application entry point rejects it with guidance. Indexing runs inside the watcher and is never time-capped.

All three forward keyword-for-keyword to `mcp/tools/providers.py`; the diagnostics and watcher
payloads are report-filed and compacted there, not here.

### Invariants And Boundaries

- Keep raw provider troubleshooting behind `provider_diagnostics`.
- `provider_watchers` is mutating except `action="status"`, and registers `dry_run=False`.

## Evidence

### Repo-Internal References

- The payload builders and their compact/report-filing helpers. [1]
- Watcher action handling and the `refresh` rejection. [2]
