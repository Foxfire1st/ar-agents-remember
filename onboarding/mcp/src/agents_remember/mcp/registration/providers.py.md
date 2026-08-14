# mcp/src/agents_remember/mcp/registration/providers.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/mcp/registration/providers.py`       |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-08-02T01:05+02:00                                        |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                    |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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
application entry point rejects it with guidance. Indexing runs inside the watcher and is never time-capped.

All three forward keyword-for-keyword to `mcp/tools/providers.py`; the diagnostics and watcher
payloads are report-filed and compacted there, not here.

### Invariants And Boundaries

- Keep raw provider troubleshooting behind `provider_diagnostics`.
- `provider_watchers` is mutating except `action="status"`, and registers `dry_run=False`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The payload builders and their compact/report-filing helpers. | `provider_status_payload`, `provider_diagnostics_payload`, `provider_watchers_payload` | mcp/src/agents_remember/mcp/tools/providers.py:33-37; mcp/src/agents_remember/mcp/tools/providers.py:40-52; mcp/src/agents_remember/mcp/tools/providers.py:73-87 |
| Watcher action handling and the `refresh` rejection. | `provider_watchers_tool` | mcp/src/agents_remember/application/provider_tools.py:48-87 |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:06:18+02:00 — 260731-EFA-L6 curator W2-B10: repaired 4 citation findings (2 reference rows); scoped recheck clean.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The three provider
  declarations moved out of `server.py` unchanged. Verification metadata pinned to the pre-change
  commit until closeout stamps the L2 code commit.
