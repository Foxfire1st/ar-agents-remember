# mcp/src/agents_remember/mcp/registration/providers.py

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- The entire provider registrar file was deleted.
- provider_status, provider_diagnostics and provider_watchers are not registered here anymore.

### Source and authority bounds

- Source comparison: `git diff HEAD -- mcp/src/agents_remember/mcp/registration/providers.py (deleted file)`.
- Source comparison: `mcp/src/agents_remember/mcp/registration/__init__.py:23-45`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

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

All three forward keyword-for-keyword to `mcp/tools/providers.py`; the watcher
payload is report-filed and compacted there, not here, while diagnostics answers carry the compact diagnosis with no per-call report (rule 6).

### Invariants And Boundaries

- Keep raw provider troubleshooting behind `provider_diagnostics`.
- `provider_watchers` is mutating except `action="status"`, and registers `dry_run=False`.

## Evidence

### Repo-Internal References

- The payload builders and their compact/report-filing helpers. [1]
- Watcher action handling and the `refresh` rejection. [2]

</details>
