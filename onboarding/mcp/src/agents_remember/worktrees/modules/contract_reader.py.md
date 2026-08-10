# mcp/src/agents_remember/worktrees/modules/contract_reader.py

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/worktrees/modules/contract_reader.py` |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-08-08T14:38+02:00                                        |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                    |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

`worktrees/modules/contract_reader.py` (260731-EFA-L9) is the worktree-backed contract reader
bound into the kernel coordination resolver. The kernel resolver declares `ContractReaderPort`;
this adapter implements it with the worktree contract-file primitives (contract loading,
task-root and leaf-enclosure path resolution).

## Code Commentary

### Logic

`WorktreeContractReader` (cit:(["class WorktreeContractReader"], mcp/src/agents_remember/worktrees/modules/contract_reader.py:27-27)) loads the leaf series contract and
resolves the task root and enclosure paths the resolver needs. The reader degrades cleanly on
reader failure so the resolver can report the missing/unreadable contract rather than crashing.

### Invariants And Boundaries

- The resolver only consumes the declared port; this adapter is the one production binding.
- `__all__` exports only `WorktreeContractReader`.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The kernel resolver declares the port this adapter implements. | "class ContractReaderPort" | mcp/src/agents_remember/kernel/coordination_context/models.py:108-108 |
| Reader-failure degradation is pinned by the structural-coverage suite. | `test_resolver_missing_reader_and_contract_edges` | mcp/tests/test_leaf_structural_coverage.py:247-247 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the contract-reader adapter added
  by the layering cleanup. Verification metadata pinned until closeout stamps the L9 code commit.
