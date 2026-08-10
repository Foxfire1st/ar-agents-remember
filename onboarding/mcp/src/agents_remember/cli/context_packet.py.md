# mcp/src/agents_remember/cli/context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/cli/context_packet.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                         |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`cli/context_packet.py` is the JSON-only CLI adapter for the context packet
application entry point: it parses arguments, loads trusted MCP settings, calls
`build_context_packet`, and prints the packet (or an `ok:false` error object)
as JSON.

## Code Commentary

### Logic

`main(argv)` requires `--config` (trusted MCP settings JSON) and `--repo`
(repository id from those settings), with `--skip-providers`,
`--include-drift`, `--include-freshness` (issue #54: requests the branch
freshness section, which fetches remote-tracking refs), `--provider-detail-limit`,
`--drift-detail-limit`, and `--fetch-timeout` shaping the
`ContextPacketRequest`. `ConfigError`/`ContextPacketError`/`ValueError` become
a single-line `{"ok": false, ...}` JSON with exit code 1; success prints the
indented packet and returns 0.

### Conventions

Thin adapter: no behavior beyond argument-to-request mapping and JSON output.
Flag surface mirrors the MCP `context_packet` tool registration.

### Invariants And Boundaries

- Keep the flag set in lockstep with `ContextPacketRequest` and the MCP tool
  registration; the CLI must not grow behavior the application entry point does not own.

### Todos

No file-local todos.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The application entry point that builds the printed packet and owns request semantics. | `build_context_packet` | mcp/src/agents_remember/application/context_packet.py:59-102 |
| CLI JSON output is covered by the context packet tests. | `ContextPacketTests` | mcp/tests/test_context_packet.py:36-282 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 2 repo-internal citation rows and preserved verification metadata.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-10T08:39+02:00: Created during issue #54 sub-task A when the CLI gained `--include-freshness` and `--fetch-timeout` (first sidecar for this pre-existing adapter).
