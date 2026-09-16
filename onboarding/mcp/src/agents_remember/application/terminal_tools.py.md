# mcp/src/agents_remember/application/terminal_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/terminal_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash | `c1dbebf883f22710b71d40a66ec92c1ac134918f` |
| lastVerifiedCommitDate | 2026-09-16T13:48:06+02:00|
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

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Internal task assignment accepts canonical document and role. | `attach_terminal_session_to_task_tool` | mcp/src/agents_remember/application/terminal_tools.py:180-227 |
| The low-level spawn primitive remains plane-owned composition. | `spawn_agent_session_tool` | mcp/src/agents_remember/application/terminal_tools.py:804-894 |
| Caller-kind provenance rides the spawn into the catalog row and payload. | `CallerKind`; `SpawnedBy` | mcp/src/agents_remember/application/terminal_tools.py:530-530; mcp/src/agents_remember/application/terminal_tools.py:534-543 |
| Exact retire/rename operations remain behind structural resolution. | `session_retire_tool`; `session_rename_tool` | mcp/src/agents_remember/application/terminal_tools.py:989-1068; mcp/src/agents_remember/application/terminal_tools.py:1157-1171 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## L23 Refusal Translation

Spawn refusal construction moved to `terminal_spawn_results.py`. This facade
now consumes that application-owned translator and preserves source-lineage
detail/projection on attach and spawn, rather than duplicating the terminal
opener's structural policy.

## Update History
- 2026-09-16T11:42:57+00:00: Generated citation repair: `CallerKind`; `SpawnedBy` repointed to mcp/src/agents_remember/application/terminal_tools.py:530-530; mcp/src/agents_remember/application/terminal_tools.py:534-543. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: **the refusal text now names the missing
  component.** `_requested_harness` and `_preferred_harness` no longer say "harness not installed:
  <id>"; they call `harness_detection_detail(found, which=which)`, so a runtime-probed harness reports
  the readiness probe's own sentence (application root missing, or no usable Node at or above the
  floor) instead of a generic not-installed message, and the settings-source suffix is preserved on
  the preferred-harness path. `_first_detected_harness`'s docstring and its no-harness refusal now say
  "launchable here" rather than "on PATH", because detection is no longer a PATH question for every
  row. `_spawn_launch_request` sets `session_backend=True` — a seat spawn starts the control runner,
  which owns the harness's runtime, so it asks the detection question rather than the terminal-program
  question. Verification metadata moves to the leaf's synced base `ff97072c`; the candidate is
  deliberately uncommitted, so the governed closeout stamps the real code commit and no hash or
  fingerprint was invented here.
- 2026-08-31T13:04+02:00 — ARSPAWN-L5 A005 closeout repair extracted task-binding/refusal
  translation into `_spawn_task_binding`, keeping `spawn_agent_session_tool` below the structural
  function-length rail without duplicating binding policy. Verification remains closeout-owned.

- 2026-08-31T12:00+02:00 — ARSPAWN-L5 A005 review repair moved complete task-binding admission
  ahead of settings selection and replaced the local document resolver with the shared
  `serving.task_binding` API. Verification remains closeout-owned.

- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: recorded propagation of
  reviewer parent provenance through the internal spawn response and plane-specific retirement
  checks. Verification remains closeout-owned.

- 2026-08-30T12:04+02:00 — 260821-ARSPAWN-L3 rewrote internal primitive remediation to direct
  callers to the one public dispatch transaction rather than a manual spawn/readiness/brief chain.
  Verification remains closeout-owned.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1: `CallerKind` (`plane|ambient|unattributed`) rides `SpawnedBy.caller_kind` through the spawn primitive into `SpawnProvenance.spawned_by_kind`, the catalog row, and the `spawnedByKind` payload; `None` stays unattributed (backward compatible). The primitive remains internal composition for the public `dispatch_agent`. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-12T20:10+02:00 — L23 curator: reconciled centralized spawn refusal translation and lineage evidence propagation; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current application-layer card for `terminal_tools.py` with qualified seat resolution and terminal/session orchestration boundaries.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
