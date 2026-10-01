# test_worktree_support.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Shared temporary Git, external-memory, task-lineage and closeout-component fixtures for retained worktree tests. The current module has no collected `test_*` methods; `WorktreeSupportTests` supplies helper methods to consumers.

## Code Commentary

### Logic

The unused `commit_memory_ledger`, `closed_external_contract_fixture`, `closeout_args`, and
`integrate_args` helpers are retired. This support module no longer fabricates a completed
three-commit closeout. Initial tracked `memory.md` seeds remain deliberately in temporary
repositories so consumers can exercise old history and migration; they do not define the current
publication protocol.

`open_external_contract_fixture` creates real temporary code and memory repositories, a selected fixture profile, a ledger baseline, task lineage and an external-memory contract. Variant fixtures add committed ranges and explicit lineage state. File, overview and entity helpers create controlled onboarding inputs; their existence is not a coverage claim.

Earlier cleanup removed the dead publication-facts and writer-mechanics helpers. LCA-L9 also
removes their remaining unused closed-contract and closeout/integration argument conveniences;
no fixture here represents a synthetic completed closeout as production acceptance.

### Conventions

Helpers operate only on disposable repositories supplied by their callers. Initial historical
cache state is distinct from the operation a consumer test invokes.

### Invariants And Boundaries

- Fixture-created commits and mappings belong to temporary repositories.
- A writer-component fixture must not be reported as full closeout or gate acceptance.
- Consumer tests determine actual protection. Removed slice matrices and their historical outcomes are not current executable coverage.

### Todos

No additional fixture scenario is introduced by this retirement.

## Evidence

### Docs References

No Domain Documentation source is configured for these repository-owned test fixtures.

No configured external source applies.

### Repo-Internal References

- Removed obsolete third-commit writers and their unused closed-state/argument fixture chain; retained historical tracked-cache seeds. [1]
- External-memory fixture supplies real isolated Git repositories and current contract inputs. [2]
- The base class provides helper methods rather than collected test cases. [3]


### Cross-Repo References

Temporary fixture repositories do not establish a live cross-repository integration.

No separate external implementation source applies.
