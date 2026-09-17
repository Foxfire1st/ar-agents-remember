# mcp/src/agents_remember/worktrees/modules/landing_record.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/modules/landing_record.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `overview.md` |

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
cit:([`cleanup_result`], mcp/src/agents_remember/worktrees/modules/cleanup.py:637-712), and the series
abandon guard reads the same cell to decide whether a master's work has left it
cit:([`_require_series_task_terminal`], mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:232-276).
Two writers would therefore mean two definitions of "landed", and the one that was never called is
the one that matters when someone later decides a half-finished master's work was discarded.

## Code Commentary

### Logic

The shared landing record contains strategy, code commit, and optional memory-content commit. The contract writer persists exactly those real outputs for both final and checkpoint landings; the downstream ledger is not an additional landed ref or an integration-completion cell.

The landed facts travel as one frozen record,
`LandedIntegration(strategy, code_commit, memory_content_commit="")`
cit:([`LandedIntegration`], mcp/src/agents_remember/worktrees/modules/landing_record.py:28-33), and the
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
cit:([`integration_strategy`, `integrated_code_commit`, `integrated_memory_content_commit`], mcp/src/agents_remember/worktrees/worktree_contract.py:259-259; mcp/src/agents_remember/worktrees/worktree_contract.py:260-260; mcp/src/agents_remember/worktrees/worktree_contract.py:261-261).
The memory-content commit defaults to `""` because a landing may be recorded before C-11 carryover has run;
the cleanup guard checks carryover separately and refuses until it is done, so an empty memory-content commit
here is not an assertion that memory was carried.

Three callers reach it and no others: the local final integration result
cit:(["def _integrated_result("], mcp/src/agents_remember/worktrees/modules/integrate.py:574-607), the local
checkpoint result cit:(["def _checkpoint_result("], mcp/src/agents_remember/worktrees/modules/integrate.py:890-927),
and the pull-request entry point
cit:([`record_landing_result`], mcp/src/agents_remember/worktrees/modules/record_landing.py:58-142).
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

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `LandedIntegration` contains strategy, code commit, and optional memory-content commit. | `LandedIntegration` | mcp/src/agents_remember/worktrees/modules/landing_record.py:28-33 |
| `record_landed_integration` writes the same actual outputs for final and checkpoint landing states. | `record_landed_integration` | mcp/src/agents_remember/worktrees/modules/landing_record.py:36-41 |

| Finding | Anchor | Source |
| --- | --- | --- |
| The cell, code/memory commit pair, and strategy this function writes are declared here. (`integration_strategy`; `integrated_code_commit`; `integrated_memory_content_commit`) | `integration_strategy` | mcp/src/agents_remember/worktrees/worktree_contract.py:259 |
| The landed facts this writer now takes as one frozen record. (`LandedIntegration`) | `LandedIntegration` | mcp/src/agents_remember/worktrees/modules/landing_record.py:28-33 |
| The local final route calls this writer instead of amending the contract inline. (`_integrated_result`) | `_integrated_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:574-580 |
| The local checkpoint route calls the same writer with `checkpoint=True`. (`_checkpoint_result`) | `_checkpoint_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:890-894 |
| The pull-request route calls the same writer. (`record_landed_integration(`) | `updated` | mcp/src/agents_remember/worktrees/modules/record_landing.py:121 |
| Cleanup refuses until this cell reads completed — which is what keeps a checkpoint from being reclaimed. | `integration_status` | mcp/src/agents_remember/worktrees/modules/cleanup.py:677-677 |
| The series abandon guard reads the same cell before retiring a master's branch, and since 260831-LOCR-L30 refuses on `checkpointed` as well as `completed`. (`_require_series_task_terminal`) | `_require_series_task_terminal` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:232-237 |

## Cross-Repo References

This is an in-process contract write with no separate repository or external-system boundary, so
there is no cross-repository protocol to cite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=4db2c4475bc64fafbcf231bdeb2c00f0a7d60bf84b9337add2ef413b2a24bfc5. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.


- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 3
  claim(s) whose anchor no longer sat in its cited range and normalised 4 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T15:05+02:00 — No content impact: mechanical citation re-derivation after the
  260913-LCA-L8 change set added one import line to `worktrees/modules/cleanup.py`, shifting the
  `integration_status` refusal read from line 664 to 665. The anchor was re-read at
  `cleanup.py:665-665`, where `if contract.integration_status != "completed":` still sits; the cited
  construct and its meaning are unchanged.
- 2026-09-13T18:02+02:00 — 260831-LOCR-L36 terminology: `checkpoint` distinguishes an unfinished
  master landed at a checkpoint from a finished one, not a "paused" master from a finished one.
  Wording only; the two recorded cells (`checkpointed` without cleanup, `completed` with cleanup
  pending) are unchanged and no verification stamp advanced.
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
