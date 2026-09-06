# mcp/src/agents_remember/kernel/coordination_context_resolver.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context_resolver.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

Since 260731-EFA-L2 the facade's `resolve_coordination_context` mirrors the resolver's new
signature — `(code_repository_name=None, workspace_root=None, code_repository_root=None, *,
hints: CoordinationHints | None = None, selector: EnclosureSelector | None = None)` — forwarding
the two bundles through `_with_facade_agents_repo` as keywords while the three repository
arguments stay positional. `__all__` gained the four new model names: `CodeRepository`,
`CoordinationHints`, `CoordinationRoots`, `EnclosureSelector`. Importing them from this facade is
the supported path for callers outside the `coordination_context` package.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The compatibility facade exposes the package resolver entry point. | "def resolve_coordination_context" | mcp/src/agents_remember/kernel/coordination_context_resolver.py:129-129 |
| The facade delegates context resolution through its current canonical package owner. | `resolve_coordination_context` | mcp/src/agents_remember/kernel/coordination_context_resolver.py:129-142 |
| Focused implementation modules live under the coordination-context package. | "def build_coordination_context" | mcp/src/agents_remember/kernel/coordination_context/resolver.py:272-272 |

## Series-Contract Notes

The compatibility facade preserves the old import path while forwarding `parent_task` and `leaf_id` into the focused resolver package.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 3 repository-reference citations (3/3 anchored and sourced; scoped citation check clean).

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  the facade's `resolve_coordination_context` was re-signed onto keyword-only `hints=` /
  `selector=` to match `coordination_context.resolver`, and `__all__` gained `CodeRepository`,
  `CoordinationHints`, `CoordinationRoots` and `EnclosureSelector`. The `_with_facade_agents_repo`
  test seam and every other re-export are unchanged. Verification metadata pinned until closeout
  stamps the L2 commit.
- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): the facade now also re-exports `find_worktree_contract` (import + `__all__`) for the MCP 2.9.3 worktree-name contract fallback. Grafted onto the series' `parent_task`/`leaf_id` forwarding.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the facade resolver signature now forwards `parent_task` and `leaf_id` to the package resolver while preserving the legacy facade bridge. Verification metadata pinned until closeout stamps the code commit.
- 2026-05-31T12:50+02:00 — Source renamed the cross-repo re-export `git_head` to `git_head_or_empty`, swapped the storage re-export `sidecar_storage_label` for the `is_sidecar_storage` predicate (import + `__all__`), and documented `_with_facade_agents_repo` as an identity rebind that is load-bearing only as a test seam; corrected the Logic prose to name the new re-exports and the documented seam (1.0.0 review remediation).
- 2026-05-25T20:57+02:00: Updated after the monolithic resolver was split into the `coordination_context/` implementation package and this file became the public facade.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` removed source-checkout `.env` resolver authority.
- 2026-05-24T09:52+02:00: Updated after `.env` and `.env.example` coordination-root discovery were removed from the package resolver.
- 2026-05-23T18:05+02:00: Created during direct closeout prep after the resolver implementation became package-only and the old skill-local script route was removed.
