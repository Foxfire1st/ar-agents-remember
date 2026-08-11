# mcp/src/agents_remember/application/terminal_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/terminal_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T10:10+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Provides plane-internal hosted-occupant assignment, spawn, retire, and rename operations. Public
agents reach these only through the structural application, which supplies authorized document+role
targets and keeps runtime correlations private.

## Code Commentary

### Logic

`attach_terminal_session_to_task_tool` applies a canonical task-document binding through the
generalized assignment primitive. `spawn_agent_session_tool` remains the low-level settings-owned
occupant allocator used by structural dispatch; it resolves harness/launch facts and opens the
terminal without owning the public dispatch brief contract. Retire and rename operate on exact ids
only after a trusted caller has resolved the current occupant.

### Conventions

`SpawnSeat`, provenance, and override objects are internal composition seams. Agent-facing
requests are the strict structural DTOs in `application/structural/`.

### Invariants And Boundaries

- No leaf-key assignment or public exact-id compatibility path remains.
- Structural authorization precedes internal mutation.
- New hosted environment identity is plane-seeded and caller identity is scrubbed.
- Initial brief persistence/delivery belongs to structural dispatch, not the raw spawn primitive.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Internal task assignment accepts canonical document and role. | `attach_terminal_session_to_task_tool` | mcp/src/agents_remember/application/terminal_tools.py:171-205 |
| The low-level spawn primitive remains plane-owned composition. | `spawn_agent_session_tool` | mcp/src/agents_remember/application/terminal_tools.py:818-890 |
| Exact retire/rename operations remain behind structural resolution. | `session_retire_tool`; `session_rename_tool` | mcp/src/agents_remember/application/terminal_tools.py:1018-1191 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current application-layer card for `terminal_tools.py` with qualified seat resolution and terminal/session orchestration boundaries.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
