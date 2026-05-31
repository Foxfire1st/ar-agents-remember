# mcp/src/agents_remember/controllers/coordination_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/coordination_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`coordination_tools.py` exposes the `resolve_context` MCP controller.

## Code Commentary

The controller validates the requested repo ID against MCP settings via
`require_repo()` and confines an optional contract path under the coordination
root via `require_within_coordination()` — both now imported from the shared
`agents_remember.controllers._guards` module rather than defined locally (the
former private `_repo` / `_coord_path` helpers were removed). It then narrows
topology to supported values with `_topology()`, calls
`resolve_coordination_context()`, and serializes the result with
`context_to_dict()`. The guards raise `AuthorityError` (not `ValueError`) when a
repo is disallowed or a path escapes the coordination root.

## Invariants And Boundaries

- MCP settings are the authority for allowed repos and workspace roots; repo
  resolution and path confinement run through the shared `_guards` module so the
  security boundary is written and reviewed once.
- Caller-provided coordination paths must remain under the configured
  coordination root; a disallowed repo or an escaping path raises
  `AuthorityError` rather than a generic `ValueError`.
- Topology values should stay explicit rather than free-form strings.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Runtime/coordination response models include `ResolveContextResponse`. | [runtime.py](agents-remember-md/mcp/src/agents_remember/models/runtime.py) |
| Coordination context resolver owns the actual context construction. | [coordination_context_resolver.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |
| `require_repo` and `require_within_coordination` (repo resolution and path confinement) now live in the shared guards module. | [_guards.py](agents-remember-md/mcp/src/agents_remember/controllers/_guards.py) |
| `AuthorityError` is the authority-violation error type the guards raise. | [errors.py](agents-remember-md/mcp/src/agents_remember/errors.py) |

## Update History

- 2026-05-31T12:50+02:00 — Source dropped the local `_repo`/`_coord_path` helpers in favor of `require_repo`/`require_within_coordination` imported from shared `controllers/_guards`, switching authority failures from `ValueError` to `AuthorityError` and removing the `Path`/`RepositoryScope`/`path_is_relative_to` imports; corrected Code Commentary, Invariants And Boundaries, and References accordingly (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Created when resolver MCP control moved into its own controller module.
