# mcp/src/agents_remember/application/terminal_tools.py

## Governing Overview

[overview](overview.md)

## Purpose

Provides plane-internal hosted-occupant assignment, spawn, retire, and rename operations. Public
agents reach these only through the structural application, which supplies authorized document+role
targets and keeps runtime correlations private.

Preserves plane-internal hosted terminal assignment/spawn operations.

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

**Since 260915-CAPS-L15 the capsule is compiled here, at the launch.** This primitive is the launch
point `dispatch_agent` drives, and it now resolves the seat's instruction delivery **before any host
side effect** through `serving/launch_capsule.py::resolve_launch_capsule`: the application-tier
compiler (`application/role_capsules/launch.py::compile_launch_capsule`) is bound into
`_launch_capsule_resolver` and the decision — `capsule`, `legacy` or `refused` — is made by the
serving-rank gate, which owns it for every launch point. The resolved value is passed onto the launch
request (`_spawn_launch_request(..., capsule)`) and published per run as `instructionMode` on the
`spawn_agent_session` payload, so "ran without instructions" is legible instead of indistinguishable
from "ran correctly". A seat whose capsule cannot be supplied **stops the spawn by name** —
`spawn_refusal("capsule-unavailable", …)` with the compiler's own status and remedy — before
`open_terminal_session` is reached. The previous account of this primitive said the session's
instructions were supplied elsewhere; that was the severed chain this leaf repaired, and it is no
longer true.

**One workspace authority.** `_spawn_launch_request` takes the session's workspace from
`session_workspace(capsule, server_workspace=config.workspace_root)` — the workspace the carrier
itself admits, else the server's own — and hands the settings selection the same value through
`selection_for_workspace`, because `serving/harness_control_runner.py:175` refuses a launch whose
selection names another workspace. So the child's cwd, `ResolvedLaunch.workspace` and the eve
carrier's own `AR_WORKSPACE_ROOT` are one value rather than three that have to agree. A task-attached
seat on eve therefore runs in its task's code worktree; free agents and every legacy launch keep
`config.workspace_root` unchanged, and the Codex carrier admits no workspace, so no Codex launch's cwd
moves.

For polymorphic reviewer generations, `SpawnedBy` additionally carries the plane-owned structural
parent document+role through `SpawnProvenance` into the catalog and spawn response. This is distinct
from ancestry and is never synthesized by the low-level allocator. Retirement forwards both actor
and target parent stamps into the central policy: managers own their leaf execution seats and
same-master reviewer, architects own only their plan reviewer, and orchestrators retain their
broader sprint authority.

Before any settings rung is read, `spawn_agent_session_tool` derives the requested seat role and
calls `_spawn_task_binding`, which is the application-level translator around
`serving.task_binding.resolve_task_binding`. Canonical document, source-lineage, and reviewer-parent
failures therefore precede launch-selection failures and host effects, while the public refusal
dialect has one named owner outside the allocator's orchestration body. The shared opener repeats
the same task-binding authority at the final process boundary to close task-movement races; neither
layer carries a duplicate rule set.

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
- Structural reviewer parent provenance crosses the low-level spawn unchanged; this primitive does
  not decide or infer it.
- Task-binding admission completes before settings resolution and uses the same validator as the
  shared opener.
- **The capsule is resolved at this launch point and before any host side effect.** A refusal returns
  `capsule-unavailable` naming the compiler's own status; the opener is never reached. A second place
  that decides a mode is the severed chain again, one level up.
- **The launch runs where its capsule admits.** `workspace_root` and the settings selection's
  workspace come from the one rule in `serving/launch_capsule.py`; a launch whose capsule admits no
  workspace (a free agent, a Codex carrier, a legacy launch) keeps `config.workspace_root` unchanged.
- **The per-run instruction mode is recorded, never inferred from an absent field.**
  `instructionMode` is on every spawn payload.

### Todos

None.

### Role Runtime and Scope

The legacy harness dispatch path now refuses any resolved service_tier before spawning, with launch-selection-invalid and an explanation that serviceTier requires the Paseo feature channel. It must not silently discard a configured tier. Keep all existing caller spend, provenance and structural dispatch explanations.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Internal task assignment accepts canonical document and role. [1]
- The low-level spawn primitive remains plane-owned composition, and since 260915-CAPS-L15 it resolves the capsule here before any host side effect. [2]
- Caller-kind provenance rides the spawn into the catalog row and payload. [3]
- Exact retire/rename operations remain behind structural resolution. [4]
- The launch request carries the resolved capsule, and takes its workspace from the one rule rather than from the server root unconditionally. [5]
- The application-tier compiler is bound behind the serving-rank port, so this tier calls the compiler directly and the dashboard route does not import it. [6]
- The per-run record of the instruction mode this launch selected, present on every spawn payload. [7]
- The gate itself: the decision, its three modes and the admitted workspace. [8]
- The compiler this launch point reaches through the port. [9]
- The runner refuses a selection whose workspace is not the child's cwd, which is the product-side second axis of the one-workspace rule. [10]
- The named refusal the spawn returns, and the acceptance cases that read the capsule out of each started session's own first prompt. [11]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

### Runtime Source References

- Frozen implementation of _resolve_harness_dispatch supporting the stated file behavior. [12]

## L23 Refusal Translation

Spawn refusal construction moved to `terminal_spawn_results.py`. This facade
now consumes that application-owned translator and preserves source-lineage
detail/projection on attach and spawn, rather than duplicating the terminal
opener's structural policy.
