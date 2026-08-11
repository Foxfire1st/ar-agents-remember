# mcp/src/agents_remember/serving/_app_lifespan.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_lifespan.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T10:20+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                                        |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

Composes serving-process startup and background loops. It migrates all recognized control-plane
identity logs, including the serving-owned notifier log, before accepting clients.

## Code Commentary

### Logic

The lifespan first runs `migrate_control_plane_identity_logs` in a worker thread, then performs
compaction/priming and starts the existing projection, liveness, agent-notifier, and diagnostic
loops. Shutdown cancels those tasks through the established lifecycle.

### Conventions

Startup ordering is the compatibility boundary: migrate once before strict current readers.

### Invariants And Boundaries

- Serving owns the notifier-log migration.
- Migration completes before clients or sweeps can parse current rows.
- No live fallback reader accepts both schemas.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The serving lifespan performs migration before compaction and loop startup. | `_serving_lifespan` | mcp/src/agents_remember/serving/_app_lifespan.py:176-201 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `_app_lifespan.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
