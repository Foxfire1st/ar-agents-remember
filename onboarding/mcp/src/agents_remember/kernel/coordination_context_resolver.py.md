# mcp/src/agents_remember/kernel/coordination_context_resolver.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context_resolver.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-28T19:10+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`coordination_context_resolver.py` is the public `c-08-ar-coordination-context-resolver` skill resolver facade and
`python -m` entrypoint for one configured repository.

## Code Commentary

### Logic

The module re-exports the stable public API from
`agents_remember.kernel.coordination_context.*`, delegates command-line
execution to `coordination_context.cli`, and preserves the existing
`agents_repo_from_script` monkeypatch seam used by resolver tests. The actual
resolution, settings parsing, storage decisions, cross-repo checks,
serialization, and contract loading now live in focused modules under
`coordination_context/`. The re-exported contract helpers are `resolve_contract`,
`find_task_contract`, and `find_worktree_contract` (the worktree-name fallback),
all kept in sync in `__all__`.

The cross-repo re-export is `git_head_or_empty` (formerly `git_head`), and the
storage re-export is the boolean predicate `is_sidecar_storage` (the former
`sidecar_storage_label` is no longer re-exported); both names are kept in sync
in `__all__`. The `_with_facade_agents_repo` swap is documented in-source as an
identity rebind under normal use (the facade re-exports `agents_repo_from_script`
from `_paths`) that stays load-bearing only as a test seam: patching the
facade-level name propagates into `_paths`, where `resolve_coordination_root_hint`
invokes it.

### Invariants And Boundaries

- `c-08-ar-coordination-context-resolver` skill is facts-only and does not mutate Git, onboarding, or worktree state.
- Source-checkout `.env` files are not resolver authority; MCP settings or an
  explicit coordination root own that path.
- Resolver behavior must not depend on deleted skill-local `_shared` paths.
- Missing supported memory roots should fail explicitly instead of fabricating a
  usable context.
- New implementation logic belongs under `coordination_context/`; this file
  stays a facade for imports and module execution.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `c-08-ar-coordination-context-resolver` skill guidance routes normal use through the MCP/package resolver. | [`c-08-ar-coordination-context-resolver` SKILL.md](agents-remember/runtime/skills/c-08-ar-coordination-context-resolver/SKILL.md) |
| Resolver shape is covered by package resolver tests. | [test_resolver_parity.py](agents-remember/mcp/tests/test_resolver_parity.py) |
| Focused implementation modules now live under the coordination-context package. | [coordination_context overview](agents-remember/mcp/src/agents_remember/kernel/coordination_context/overview.md) |

## Series-Contract Notes

The compatibility facade preserves the old import path while forwarding `parent_task` and `leaf_id` into the focused resolver package.

## Update History

- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): the facade now also re-exports `find_worktree_contract` (import + `__all__`) for the MCP 2.9.3 worktree-name contract fallback. Grafted onto the series' `parent_task`/`leaf_id` forwarding.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the facade resolver signature now forwards `parent_task` and `leaf_id` to the package resolver while preserving the legacy facade bridge. Verification metadata pinned until closeout stamps the code commit.
- 2026-05-31T12:50+02:00 — Source renamed the cross-repo re-export `git_head` to `git_head_or_empty`, swapped the storage re-export `sidecar_storage_label` for the `is_sidecar_storage` predicate (import + `__all__`), and documented `_with_facade_agents_repo` as an identity rebind that is load-bearing only as a test seam; corrected the Logic prose to name the new re-exports and the documented seam (1.0.0 review remediation).
- 2026-05-25T20:57+02:00: Updated after the monolithic resolver was split into the `coordination_context/` implementation package and this file became the public facade.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` removed source-checkout `.env` resolver authority.
- 2026-05-24T09:52+02:00: Updated after `.env` and `.env.example` coordination-root discovery were removed from the package resolver.
- 2026-05-23T18:05+02:00: Created during direct closeout prep after the resolver implementation became package-only and the old skill-local script route was removed.
