# mcp/src/agents_remember/kernel/coordination_context_resolver.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context_resolver.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T10:06+02:00                     |
| lastVerifiedCommitHash | `f48a34619fbe37c405419acfa60580b95ed8812c` |
| lastVerifiedCommitDate | 2026-05-24T10:04:28+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`coordination_context_resolver.py` resolves the active Agents Remember context
for one configured repository.

## Code Commentary

### Logic

The module resolves code repository identity, coordination root, memory root,
onboarding root, task and temp roots, storage/path-rule settings, worktree
contract facts, ledger path, and branch-gated cross-repo allowances. MCP
controllers pass the coordination root from MCP settings; package-local resolver
fallbacks no longer read source-checkout `.env` or `.env.example` files. The
MCP package version imports memory-ledger and worktree-contract helpers from
`agents_remember.*` package modules directly.

### Invariants And Boundaries

- C-08 is facts-only and does not mutate Git, onboarding, or worktree state.
- Source-checkout `.env` files are not resolver authority; MCP settings or an
  explicit coordination root own that path.
- Resolver behavior must not depend on deleted skill-local `_shared` paths.
- Missing supported memory roots should fail explicitly instead of fabricating a
  usable context.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| C-08 skill guidance routes normal use through the MCP/package resolver. | [C-08 SKILL.md](agents-remember-md/runtime/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/SKILL.md) |
| Resolver shape is covered by package resolver tests. | [test_resolver_parity.py](agents-remember-md/mcp/tests/test_resolver_parity.py) |

## Update History

- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` removed source-checkout `.env` resolver authority.
- 2026-05-24T09:52+02:00: Updated after `.env` and `.env.example` coordination-root discovery were removed from the package resolver.
- 2026-05-23T18:05+02:00: Created during direct closeout prep after the resolver implementation became package-only and the old skill-local script route was removed.
