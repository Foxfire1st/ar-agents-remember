# mcp/src/agents_remember/application/coordination_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/application/coordination_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`coordination_tools.py` exposes the `resolve_context` MCP application entry point.

## Code Commentary

`resolve_context_tool(config, task: TaskRef, *, worktree_name=None, topology=None)` — since
260731-EFA-L2 the five locators arrive as one `TaskRef` (`application/task_ref.py`), shared with
`worktree_attach_tool` and `worktree_status_tool`. `worktree_name` and `topology` stay separate
because neither identifies the task. The resolver call itself now passes
`hints=CoordinationHints(...)` and `selector=EnclosureSelector(...)` instead of five loose keywords.

The application entry point validates the requested repo ID against MCP settings via
`require_repo()` and confines an optional contract path under the coordination
root via `require_within_coordination()` — both now imported from the shared
`agents_remember.kernel.authority` module rather than defined locally (the
former private `_repo` / `_coord_path` helpers were removed). It then narrows
topology to supported values with `_topology()`, calls
`resolve_coordination_context()`, and serializes the result with
`context_to_dict()`. The guards raise `AuthorityError` (not `ValueError`) when a
repo is disallowed or a path escapes the coordination root.

## Invariants And Boundaries

- MCP settings are the authority for allowed repos and workspace roots; repo
  resolution and path confinement run through the shared `kernel/authority.py` module so the
  security boundary is written and reviewed once.
- Caller-provided coordination paths must remain under the configured
  coordination root; a disallowed repo or an escaping path raises
  `AuthorityError` rather than a generic `ValueError`.
- Topology values should stay explicit rather than free-form strings.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Runtime/coordination response models include `ResolveContextResponse`. | `ResolveContextResponse` | mcp/src/agents_remember/models/runtime.py:30-33 |
| Coordination context resolver owns the actual context construction. | `resolve_coordination_context` | mcp/src/agents_remember/kernel/coordination_context_resolver.py:131-146 |
| `require_repo` and `require_within_coordination` (repo resolution and path confinement) now live in the shared `kernel/authority.py` module. | `require_within_coordination` | mcp/src/agents_remember/kernel/authority.py:27-35 |
| `AuthorityError` is the authority-violation error type the guards raise. | `AuthorityError` | mcp/src/agents_remember/errors.py:17-23 |

## Series-Contract Notes

The context application entry point still resolves nested active task roots and a specific leaf enclosure —
`parent_task` and `leaf_id` now travel inside the `TaskRef` through the same trusted config-bound
resolver path, preserving task-name ergonomics.

## Update History

- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 4 citation findings and one stale-module
  correction. The guards live in `kernel/authority.py` (`application/_guards.py` no longer exists); prose,
  invariant, and the guards row now say so. Re-anchored the resolver row to
  `resolve_coordination_context` and the guards row to `require_within_coordination` with exact spans.
  Scoped recheck clean.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: `resolve_context_tool` took one `TaskRef` in place of the
  five locator keywords, and the `resolve_coordination_context` call moved onto
  `CoordinationHints` / `EnclosureSelector`. Guards, topology narrowing and serialization are
  unchanged. Verification metadata pinned until closeout stamps the L2 code commit.

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: `resolve_context_tool` now forwards `parent_task` and `leaf_id` so source API/MCP callers can resolve nested task roots and a specific leaf enclosure by task name. Verification metadata pinned until closeout stamps the code commit.
- 2026-05-31T12:50+02:00 — Source dropped the local `_repo`/`_coord_path` helpers in favor of `require_repo`/`require_within_coordination` imported from shared `controllers/_guards`, switching authority failures from `ValueError` to `AuthorityError` and removing the `Path`/`RepositoryScope`/`path_is_relative_to` imports; corrected Code Commentary, Invariants And Boundaries, and References accordingly (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Created when resolver MCP control moved into its own controller module.
