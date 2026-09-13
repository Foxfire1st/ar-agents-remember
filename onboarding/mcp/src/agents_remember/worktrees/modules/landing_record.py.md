# mcp/src/agents_remember/worktrees/modules/landing_record.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/modules/landing_record.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-12T00:33+02:00 |
| lastVerifiedCommitHash | `c4fc0ee2418ccef5a02de3823141a82092b84080` |
| lastVerifiedCommitDate | 2026-09-13T11:55:12+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[worktrees/modules/overview.md](overview.md)

## Purpose

The **single writer** of a worktree contract's terminal integration cell. Every landing route
converges here: the local final route moves the code and memory refs itself and then records what it
moved, the local checkpoint route records a partial master's landed line without retiring anything,
and the pull-request route moved nothing locally — `gh pr merge` moved the refs on the remote — and
has only the landed commit to record.

This file exists because the cell it writes is read as an authority, not as a report.
`worktree_cleanup` refuses until `integration_status == "completed"`
cit:([`cleanup_result`], mcp/src/agents_remember/worktrees/modules/cleanup.py:632-707), and the series
abandon guard reads the same cell to decide whether a master's work has left it
cit:([`_require_series_task_terminal`], mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:233-279).
Two writers would therefore mean two definitions of "landed", and the one that was never called is
the one that matters when someone later decides a half-finished master's work was discarded.

## Code Commentary

### Logic

The landed facts travel as one frozen record,
`LandedIntegration(strategy, code_commit, memory_content_commit="", ledger_commit="")`
cit:([`LandedIntegration`], mcp/src/agents_remember/worktrees/modules/landing_record.py:28-36), and the
writer is
`record_landed_integration(contract, *, landed: LandedIntegration, checkpoint: bool = False)`
cit:([`record_landed_integration`], mcp/src/agents_remember/worktrees/modules/landing_record.py:37-68).
It does three things in one call: it replaces the four integration cells on the contract, amends the
terminal status cells through `ContractCells`, writes the contract, and returns the updated contract
so the caller can keep reporting from it
cit:(["write_contract(contract.contract_path, updated)"], mcp/src/agents_remember/worktrees/modules/landing_record.py:67-67).

`checkpoint` selects *how much* landed, and it is the only difference between a paused master and a
finished one
cit:(["ContractCells(integration_status=\"checkpointed\")", "ContractCells(integration_status=\"completed\", cleanup=\"pending\")"], mcp/src/agents_remember/worktrees/modules/landing_record.py:53-55):
a checkpoint records `checkpointed` and deliberately leaves `cleanup` alone, because nothing is
being reclaimed, while the final landing records `completed` and marks cleanup pending. Keeping both
behind this one function is what stops the two routes drifting into two different meanings of
"landed".

The four replaced fields are declared on the contract
cit:([`integration_strategy`, `integrated_code_commit`, `integrated_memory_content_commit`, `integrated_ledger_commit`], mcp/src/agents_remember/worktrees/worktree_contract.py:260-263).
The memory pair defaults to `""` because a landing may be recorded before C-11 carryover has run;
the cleanup guard checks carryover separately and refuses until it is done, so an empty memory pair
here is not an assertion that memory was carried.

Three callers reach it and no others: the local final integration result
cit:(["def _integrated_result("], mcp/src/agents_remember/worktrees/modules/integrate.py:598-633), the local
checkpoint result cit:(["def _checkpoint_result("], mcp/src/agents_remember/worktrees/modules/integrate.py:922-961),
and the pull-request entry point
cit:([`record_landing_result`], mcp/src/agents_remember/worktrees/modules/record_landing.py:58-131).
`LandedIntegration` is why the signature could gain `checkpoint` at all: threading a fifth keyword
onto the writer would have pushed it past the enabled argument-count rule, and bundling the landed
facts keeps the one writer the single definition of "landed" that this module exists to be.

### Conventions

The module deliberately has no `__all__`, no CLI surface, and no MCP tool: it is a shared write, not
an operation. Callers own approval, validation, and reporting; this function owns the cell.

The docstring states the non-obvious rule — one writer — because a future contributor adding a
second route is the exact failure this shape prevents.

### Invariants And Boundaries

- **One writer, two outcomes.** No second path may set `integration_status="completed"` or
  `integration_status="checkpointed"` directly; route new landings through this function so the
  commit triple travels with the cell and the checkpoint/final distinction stays one decision.
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
| The landed facts this writer now takes as one frozen record. | `LandedIntegration` | mcp/src/agents_remember/worktrees/modules/landing_record.py:28-36 |
| The local final route calls this writer instead of amending the contract inline. | "def _integrated_result(" | mcp/src/agents_remember/worktrees/modules/integrate.py:598-633 |
| The local checkpoint route calls the same writer with `checkpoint=True`. | "def _checkpoint_result(" | mcp/src/agents_remember/worktrees/modules/integrate.py:922-961 |
| The pull-request route calls the same writer. | "record_landed_integration(" | mcp/src/agents_remember/worktrees/modules/record_landing.py:121-121 |
| Cleanup refuses until this cell reads completed — which is what keeps a checkpoint from being reclaimed. | `integration_status` | mcp/src/agents_remember/worktrees/modules/cleanup.py:664-664 |
| The series abandon guard reads the same cell before retiring a master's branch, and since 260831-LOCR-L30 refuses on `checkpointed` as well as `completed`. | `_require_series_task_terminal` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:233-279 |

## Cross-Repo References

This is an in-process contract write with no separate repository or external-system boundary, so
there is no cross-repository protocol to cite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `_integrated_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:598-633. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `_checkpoint_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:922-961. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `_integrated_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:598-633. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `_checkpoint_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:922-961. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:26:36+00:00: Generated citation repair: "record_landed_integration(" repointed to mcp/src/agents_remember/worktrees/modules/record_landing.py:121-121. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b5cbe38ab438de766feb0fc3860228f5125b623ebbee641f90211d51326d68e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: widened the single writer with
  `checkpoint: bool = False` and bundled the landed facts into the frozen `LandedIntegration`
  record, so the two landing outcomes (`completed` + `cleanup="pending"` versus `checkpointed` with
  cleanup untouched) stay one decision behind one writer; recorded the third caller
  (`integrate.py::_checkpoint_result`), why the bundling was required (a fifth keyword would have
  tripped the argument-count rule), and updated every reference range in this card. Verification
  metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T23:05:00+00:00: The `write_contract`, `record_landed_integration`, and `integration_status != "completed"` anchors were ambiguous or not anchors at all, so four claims could not be compared with their verification provenance; each now names the construct that carries the behaviour — the exact writer call `write_contract(contract.contract_path, updated)` at `landing_record.py` line 47, the shared-writer call in `integrate.py` line 376, the same call in `record_landing.py` line 106, and the `integration_status` identifier the cleanup refusal reads at `cleanup.py` line 664. Claim wording and cited extents are otherwise unchanged; the missing-anchor row previously cited `cleanup.py:664-664` with a backticked expression that the anchor grammar cannot read.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `cleanup_result` repointed to mcp/src/agents_remember/worktrees/modules/cleanup.py:632-707. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_integrated_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:369-400. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-12T00:33+02:00 — Created by the LOCR-L29 curator pass (task-terminal retirement, PR
  landing record, and series resume). Documents the extracted single writer that both landing routes
  now share, the two callers that reach it, and the two guards that read the cell it writes.
  Verification metadata is pinned to the leaf base commit and remains closeout-owned.
