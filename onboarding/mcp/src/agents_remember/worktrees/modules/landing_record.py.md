# mcp/src/agents_remember/worktrees/modules/landing_record.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

The **single writer** of a worktree contract's terminal integration cell. Every landing route
converges here: the local final route moves the code and memory refs itself and then records what it
moved, the local checkpoint route records a partial master's landed line without retiring anything,
and the pull-request route moved nothing locally — `gh pr merge` moved the refs on the remote — and
has only the landed commit to record.

This file exists because the cell it writes is read as an authority, not as a report.
`worktree_cleanup` refuses until `integration_status == "completed"`
cit:([`cleanup_result`], mcp/src/agents_remember/worktrees/modules/cleanup.py:645-720), and the series
abandon guard reads the same cell to decide whether a master's work has left it
cit:([`_require_series_task_terminal`], mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:232-276).
Two writers would therefore mean two definitions of "landed", and the one that was never called is
the one that matters when someone later decides a half-finished master's work was discarded.

## Code Commentary

### Logic

The shared landing record contains strategy, code commit, and optional memory-content commit. The contract writer persists exactly those real outputs for both final and checkpoint landings; the downstream ledger is not an additional landed ref or an integration-completion cell.

The landed facts travel as one frozen record,
`LandedIntegration(strategy, code_commit, memory_content_commit="")`
cit:([`LandedIntegration`], mcp/src/agents_remember/worktrees/modules/landing_record.py:27-33), and the
writer is
`record_landed_integration(contract, *, landed: LandedIntegration, checkpoint: bool = False)`
cit:([`record_landed_integration`], mcp/src/agents_remember/worktrees/modules/landing_record.py:36-66).
It does three things in one call: it records the strategy and two output commits on the contract, amends the
terminal status cells through `ContractCells`, writes the contract, and returns the updated contract
so the caller can keep reporting from it
cit:(["write_contract(contract.contract_path, updated)"], mcp/src/agents_remember/worktrees/modules/landing_record.py:65-65).

`checkpoint` selects *how much* landed, and it is the only difference between an unfinished master
landed at a checkpoint and a finished one
cit:(["ContractCells(integration_status=\"checkpointed\")", "ContractCells(integration_status=\"completed\", cleanup=\"pending\")"], mcp/src/agents_remember/worktrees/modules/landing_record.py:52-52; mcp/src/agents_remember/worktrees/modules/landing_record.py:54-54):
a checkpoint records `checkpointed` and deliberately leaves `cleanup` alone, because nothing is
being reclaimed, while the final landing records `completed` and marks cleanup pending. Keeping both
behind this one function is what stops the two routes drifting into two different meanings of
"landed".

The three replaced fields are declared on the contract
cit:([`integration_strategy`, `integrated_code_commit`, `integrated_memory_content_commit`], mcp/src/agents_remember/worktrees/worktree_contract.py:264-264; mcp/src/agents_remember/worktrees/worktree_contract.py:265-265; mcp/src/agents_remember/worktrees/worktree_contract.py:266-266).
The memory-content commit defaults to `""` because a landing may be recorded before C-11 carryover has run;
the cleanup guard checks carryover separately and refuses until it is done, so an empty memory-content commit
here is not an assertion that memory was carried.

Three callers reach it and no others: the local final integration result
cit:(["def _integrated_result("], mcp/src/agents_remember/worktrees/modules/integrate.py:574-607), the local
checkpoint result cit:(["def _checkpoint_result("], mcp/src/agents_remember/worktrees/modules/integrate.py:939-939),
and the pull-request entry point, which since MIK-R09 first checks the landed memory commit on converted memory
cit:([`record_landing_result`], mcp/src/agents_remember/worktrees/modules/record_landing.py:168-253).
`LandedIntegration` is why the signature could gain `checkpoint` at all: threading a fifth keyword
onto the writer would have pushed it past the enabled argument-count rule, and bundling the landed
facts keeps the one writer the single definition of "landed" that this module exists to be.

### Conventions

The module deliberately has no `__all__`, no CLI surface, and no MCP tool: it is a shared write, not
an operation. Callers own approval, validation, and reporting; this function owns the cell.

The docstring states the non-obvious rule — one writer — because a future contributor adding a
second route is the exact failure this shape prevents.

#### Invariants And Boundaries

- **One writer, two outcomes.** No second path may set `integration_status="completed"` or
  `integration_status="checkpointed"` directly; route new landings through this function so the
  code/memory commit pair travels with the cell and the checkpoint/final distinction stays one decision.
- **`checkpoint` selects the claim, not the ref move.** The caller has already moved the refs; this
  flag only decides whether the contract says "completed, cleanup pending" or "checkpointed, cleanup
  untouched". A checkpoint must never mark cleanup pending, and a final landing must never leave it
  untouched.
- **The cell is an authority, not a report.** Never weaken it to make a cleanup or an abandon
  proceed; the guard it satisfies is the reason the cell exists.
- **It performs no validation.** Reachability, approval, and the "nothing to record" case all belong
  to the caller. This function assumes an already-admitted landing.
- **It never moves refs, commits, or pushes.** The local route moves refs before calling; the PR
  route's refs were moved remotely.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `LandedIntegration` contains strategy, code commit, and optional memory-content commit. [1]
- `record_landed_integration` writes the same actual outputs for final and checkpoint landing states. [2]

- The cell, code/memory commit pair, and strategy this function writes are declared here. (`integration_strategy`; `integrated_code_commit`; `integrated_memory_content_commit`) [3]
- The landed facts this writer now takes as one frozen record. (`LandedIntegration`) [4]
- The local final route calls this writer instead of amending the contract inline. (`_integrated_result`) [5]
- The local checkpoint route calls the same writer with `checkpoint=True`. (`_checkpoint_result`) [6]
- The pull-request route calls the same writer. (`record_landed_integration(`) [7]
- Cleanup refuses until this cell reads completed — which is what keeps a checkpoint from being reclaimed. (`integration_status`) [8]
- The series abandon guard reads the same cell before retiring a master's branch, and since 260831-LOCR-L30 refuses on `checkpointed` as well as `completed`. (`_require_series_task_terminal`) [9]

### Cross-Repo References

This is an in-process contract write with no separate repository or external-system boundary, so
there is no cross-repository protocol to cite.

No additional cross-repository evidence applies.
