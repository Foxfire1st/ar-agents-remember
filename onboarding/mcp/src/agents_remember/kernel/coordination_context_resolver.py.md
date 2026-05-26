# mcp/src/agents_remember/kernel/coordination_context_resolver.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context_resolver.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`coordination_context_resolver.py` is the public C-08 resolver facade and
`python -m` entrypoint for one configured repository.

## Code Commentary

### Logic

The module re-exports the stable public API from
`agents_remember.kernel.coordination_context.*`, delegates command-line
execution to `coordination_context.cli`, and preserves the existing
`agents_repo_from_script` monkeypatch seam used by resolver tests. The actual
resolution, settings parsing, storage decisions, cross-repo checks,
serialization, and contract loading now live in focused modules under
`coordination_context/`.

### Invariants And Boundaries

- C-08 is facts-only and does not mutate Git, onboarding, or worktree state.
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
| C-08 skill guidance routes normal use through the MCP/package resolver. | [C-08 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/SKILL.md) |
| Resolver shape is covered by package resolver tests. | [test_resolver_parity.py](agents-remember-md/mcp/tests/test_resolver_parity.py) |
| Focused implementation modules now live under the coordination-context package. | [coordination_context overview](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/overview.md) |

## Update History

- 2026-05-25T20:57+02:00: Updated after the monolithic resolver was split into the `coordination_context/` implementation package and this file became the public facade.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` removed source-checkout `.env` resolver authority.
- 2026-05-24T09:52+02:00: Updated after `.env` and `.env.example` coordination-root discovery were removed from the package resolver.
- 2026-05-23T18:05+02:00: Created during direct closeout prep after the resolver implementation became package-only and the old skill-local script route was removed.
