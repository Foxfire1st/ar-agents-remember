# mcp/src/agents_remember/serving/_app_common.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_common.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T10:28+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                                        |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Defines shared serving request/composition models and helper seams used by the split FastAPI route
modules.

## Code Commentary

### Logic

`TerminalAttachTaskRequest` accepts the canonical task-document reference and role used by the
assignment route. Shared runtime/collaborator records keep topology, catalog, host, projection, and
cache dependencies explicit for route handlers.

### Conventions

Wire parsing belongs here; structural qualification and mutation delegate to owned services.

### Invariants And Boundaries

- No leaf-key attach request or compatibility parser remains.
- Request identity is task document plus role.
- Runtime collaborators are server-resolved, not browser-provided authority.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Terminal assignment parses canonical document and role. | `TerminalAttachTaskRequest` | mcp/src/agents_remember/serving/_app_common.py:286-291 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `_app_common.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
