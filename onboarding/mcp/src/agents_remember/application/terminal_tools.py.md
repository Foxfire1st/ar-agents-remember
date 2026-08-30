# mcp/src/agents_remember/application/terminal_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/terminal_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T12:04+02:00 |
| lastVerifiedCommitHash | `f9f92ca793811b6cb738d7e302dfecdf8636e96e` |
| lastVerifiedCommitDate | 2026-08-30T14:26:46+02:00|
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
only after a trusted caller has resolved the current occupant. Since 260821-ARSPAWN-L1 the spawn
primitive carries caller-kind provenance end to end: `CallerKind` (`plane|ambient|unattributed`)
rides `SpawnedBy.caller_kind` into `SpawnProvenance.spawned_by_kind`, the catalog row
(`spawned_by_kind`), and the `spawnedByKind` payload — set by the public `dispatch_agent` tool by
caller kind (plane seats pass `plane`, ambient callers `ambient`; `None` stays unattributed,
backward compatible).

The primitive's own refusals now name that boundary instead of teaching callers to invoke the
primitive. Unsupported spend overrides point public role callers to `dispatch_agent` and
settings-owned spend. Any attempted context/submit brief delivery points callers to one
`dispatch_agent` request with the canonical task document, target role, and complete brief; it no
longer advertises a public spawn/readiness/inbox sequence.

### Conventions

`SpawnSeat`, provenance, and override objects are internal composition seams. Agent-facing
requests are the strict structural DTOs in `application/structural/`.

### Invariants And Boundaries

- No leaf-key assignment or public exact-id compatibility path remains.
- Structural authorization precedes internal mutation.
- New hosted environment identity is plane-seeded and caller identity is scrubbed.
- Initial brief persistence/delivery belongs to structural dispatch, not the raw spawn primitive.
- Internal primitive refusals never become documentation for a second public spawning workflow.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Internal task assignment accepts canonical document and role. | `attach_terminal_session_to_task_tool` | mcp/src/agents_remember/application/terminal_tools.py:171-205 |
| The low-level spawn primitive remains plane-owned composition. | `spawn_agent_session_tool` | mcp/src/agents_remember/application/terminal_tools.py:785-870 |
| Caller-kind provenance rides the spawn into the catalog row and payload. | `CallerKind`; `SpawnedBy` | mcp/src/agents_remember/application/terminal_tools.py:522-534 |
| Exact retire/rename operations remain behind structural resolution. | `session_retire_tool`; `session_rename_tool` | mcp/src/agents_remember/application/terminal_tools.py:955-1025; mcp/src/agents_remember/application/terminal_tools.py:1114-1128 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## L23 Refusal Translation

Spawn refusal construction moved to `terminal_spawn_results.py`. This facade
now consumes that application-owned translator and preserves source-lineage
detail/projection on attach and spawn, rather than duplicating the terminal
opener's structural policy.

## Update History
- 2026-08-30T12:04+02:00 — 260821-ARSPAWN-L3 rewrote internal primitive remediation to direct
  callers to the one public dispatch transaction rather than a manual spawn/readiness/brief chain.
  Verification remains closeout-owned.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1: `CallerKind` (`plane|ambient|unattributed`) rides `SpawnedBy.caller_kind` through the spawn primitive into `SpawnProvenance.spawned_by_kind`, the catalog row, and the `spawnedByKind` payload; `None` stays unattributed (backward compatible). The primitive remains internal composition for the public `dispatch_agent`. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-12T20:10+02:00 — L23 curator: reconciled centralized spawn refusal translation and lineage evidence propagation; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current application-layer card for `terminal_tools.py` with qualified seat resolution and terminal/session orchestration boundaries.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
