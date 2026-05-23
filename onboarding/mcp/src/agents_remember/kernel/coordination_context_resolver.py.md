# mcp/src/agents_remember/kernel/coordination_context_resolver.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context_resolver.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T18:05+02:00                     |
| lastVerifiedCommitHash | `a6890ae469b70ef045a127fc774d6aa51a54e65a` |
| lastVerifiedCommitDate | 2026-05-23T18:31:48+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`coordination_context_resolver.py` resolves the active Agents Remember context
for one configured repository.

## Code Commentary

### Logic

The module resolves code repository identity, coordination root, memory root,
onboarding root, task and temp roots, storage/path-rule settings, worktree
contract facts, ledger path, and branch-gated cross-repo allowances. The MCP
package version imports memory-ledger and worktree-contract helpers from
`agents_remember.*` package modules directly.

### Invariants And Boundaries

- C-08 is facts-only and does not mutate Git, onboarding, or worktree state.
- Resolver behavior must not depend on deleted skill-local `_shared` paths.
- Missing supported memory roots should fail explicitly instead of fabricating a
  usable context.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| C-08 skill guidance routes normal use through the MCP/package resolver. | [C-08 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/SKILL.md) |
| Resolver shape is covered by package resolver tests. | [test_resolver_parity.py](agents-remember-md/mcp/tests/test_resolver_parity.py) |

## Update History

- 2026-05-23T18:05+02:00: Created during direct closeout prep after the resolver implementation became package-only and the old skill-local script route was removed.
