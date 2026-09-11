# mcp/src/agents_remember/worktrees/modules/landing_record.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/modules/landing_record.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-12T00:33+02:00 |
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[worktrees/modules/overview.md](overview.md)

## Purpose

The **single writer** of a worktree contract's terminal integration cell. Both landing routes
converge here: the local route moves the code and memory refs itself and then records what it moved,
while the pull-request route moved nothing locally — `gh pr merge` moved the refs on the remote — and
has only the landed commit to record.

This file exists because the cell it writes is read as an authority, not as a report.
`worktree_cleanup` refuses until `integration_status == "completed"`
cit:([`cleanup_result`], mcp/src/agents_remember/worktrees/modules/cleanup.py:632-707), and the series
abandon guard reads the same cell to decide whether a master's work has left it
cit:([`_require_series_task_terminal`], mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:233-274).
Two writers would therefore mean two definitions of "landed", and the one that was never called is
the one that matters when someone later decides a half-finished master's work was discarded.

## Code Commentary

### Logic

`record_landed_integration(contract, *, strategy, code_commit, memory_content_commit="", ledger_commit="")`
cit:([`record_landed_integration`], mcp/src/agents_remember/worktrees/modules/landing_record.py:27-48)
does three things in one call: it replaces the four integration cells on the contract, amends the
terminal status cells through `ContractCells(integration_status="completed", cleanup="pending")`
cit:(["ContractCells(integration_status=\"completed\"", "cleanup=\"pending\""], mcp/src/agents_remember/worktrees/modules/landing_record.py:45-45),
writes the contract, and returns the updated contract so the caller can keep reporting from it
cit:(["write_contract(contract.contract_path, updated)"], mcp/src/agents_remember/worktrees/modules/landing_record.py:47-47).

The four replaced fields are declared on the contract
cit:([`integration_strategy`, `integrated_code_commit`, `integrated_memory_content_commit`, `integrated_ledger_commit`], mcp/src/agents_remember/worktrees/worktree_contract.py:260-263).
The memory pair defaults to `""` because a landing may be recorded before C-11 carryover has run;
the cleanup guard checks carryover separately and refuses until it is done, so an empty memory pair
here is not an assertion that memory was carried.

Two callers reach it and no others: the local integration result
cit:([`_integrated_result`], mcp/src/agents_remember/worktrees/modules/integrate.py:369-400) and the
pull-request entry point cit:([`record_landing_result`], mcp/src/agents_remember/worktrees/modules/record_landing.py:55-126).

### Conventions

The module deliberately has no `__all__`, no CLI surface, and no MCP tool: it is a shared write, not
an operation. Callers own approval, validation, and reporting; this function owns the cell.

The docstring states the non-obvious rule — one writer — because a future contributor adding a
second route is the exact failure this shape prevents.

### Invariants And Boundaries

- **One writer.** No second path may set `integration_status="completed"` directly; route new
  landings through this function so the commit triple travels with the cell.
- **The cell is an authority, not a report.** Never weaken it to make a cleanup or an abandon
  proceed; the guard it satisfies is the reason the cell exists.
- **It performs no validation.** Reachability, approval, and the "nothing to record" case all belong
  to the caller. This function assumes an already-admitted landing.
- **It never moves refs, commits, or pushes.** The local route moves refs before calling; the PR
  route's refs were moved remotely.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo, and these are
repository-internal contract semantics, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The cell, commit triple, and strategy this function writes are declared here. | `integration_strategy`; `integrated_code_commit`; `integrated_memory_content_commit`; `integrated_ledger_commit` | mcp/src/agents_remember/worktrees/worktree_contract.py:260-263 |
| The local route calls this writer instead of amending the contract inline. | "record_landed_integration(" | mcp/src/agents_remember/worktrees/modules/integrate.py:376-376 |
| The pull-request route calls the same writer. | "record_landed_integration(" | mcp/src/agents_remember/worktrees/modules/record_landing.py:106-106 |
| Cleanup refuses until this cell reads completed. | `integration_status` | mcp/src/agents_remember/worktrees/modules/cleanup.py:664-664 |
| The series abandon guard reads the same cell before retiring a master's branch. | `_require_series_task_terminal` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:233-274 |

## Cross-Repo References

This is an in-process contract write with no separate repository or external-system boundary, so
there is no cross-repository protocol to cite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-11T23:05:00+00:00: The `write_contract`, `record_landed_integration`, and `integration_status != "completed"` anchors were ambiguous or not anchors at all, so four claims could not be compared with their verification provenance; each now names the construct that carries the behaviour — the exact writer call `write_contract(contract.contract_path, updated)` at `landing_record.py` line 47, the shared-writer call in `integrate.py` line 376, the same call in `record_landing.py` line 106, and the `integration_status` identifier the cleanup refusal reads at `cleanup.py` line 664. Claim wording and cited extents are otherwise unchanged; the missing-anchor row previously cited `cleanup.py:664-664` with a backticked expression that the anchor grammar cannot read.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `cleanup_result` repointed to mcp/src/agents_remember/worktrees/modules/cleanup.py:632-707. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_integrated_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:369-400. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-12T00:33+02:00 — Created by the LOCR-L29 curator pass (task-terminal retirement, PR
  landing record, and series resume). Documents the extracted single writer that both landing routes
  now share, the two callers that reach it, and the two guards that read the cell it writes.
  Verification metadata is pinned to the leaf base commit and remains closeout-owned.
