# mcp/src/agents_remember/application/runtime/startup.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/runtime/startup.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T08:40+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Initializes MCP-process application collaborators after applying the bounded control-plane identity
migration required by strict structural readers.

## Code Commentary

### Logic

`initialize_mcp_application` declares MCP process ownership, migrates recognized durable logs without
the dashboard-owned notifier log, then installs ambient lifecycle state. Dashboard autostart remains
a separate startup hook.

### Conventions

Migration runs before any strict store can parse current records; ownership boundaries determine
which process may migrate which log.

### Invariants And Boundaries

- Migration is one-way, idempotent deployment work.
- MCP startup does not mutate the dashboard-owned notifier log.
- No dual-schema reader is installed.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| MCP startup migrates its owned logs before ambient installation. | `initialize_mcp_application` | mcp/src/agents_remember/application/runtime/startup.py:20-28 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: moved this preserved startup card with its source into the cohesive `application/runtime/` package and rebound all current citations; startup behavior is unchanged. Verification metadata remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current application-layer card for `server_startup.py` with qualified seat resolution and terminal/session orchestration boundaries.
- 2026-08-10T18:31+02:00 — 260731-EFA-L21: split out the idempotent pre-config MCP trust
  declaration while preserving `prepare_mcp_process` as the supervision operation. Verification
  metadata remains pinned until approved closeout.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
