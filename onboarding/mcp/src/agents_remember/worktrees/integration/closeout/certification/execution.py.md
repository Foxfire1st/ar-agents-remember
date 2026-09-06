# mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:58:25+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Selected closeout certification overview](overview.md)

## Purpose

Executes only the suffix admitted by the current selected closeout generation and hands exact remaining work to the bound memory/finalization owner.

## Code Commentary

### Logic

`execute_selected_closeout` begins with a live running owner, current contract/profile/route authority and the fully reopened selection. Selected red evidence refuses unchanged retry. The exact original certificate pool and retained terminal publications form `CodeCertificationExecution`; the current recovery decision determines the first gate to run.

Code execution uses the configured profile path and contract code base, supplying callbacks that select real recorded terminals, protect every referenced publication and recheck the live owner immediately before a start. After publication it reopens current state and appends a recovery decision derived from the actual selected prefix. An incomplete code prefix cannot enter memory.

An existing or inherited Gate-5 certificate requires a bound continuation and an actual current `GateFiveSemanticInputs` observation before reuse is considered. The observation is reparsed canonically and followed by a live journal check. Recovery decisions retain exact memory bytes; an unchanged decision is idempotent. Changed inputs for an already selected fifth terminal require an explicit successor. A current inherited fifth terminal is retained by its exact original reference.

First gate 5 hands off to `run_memory`. Finalization-only reuse performs a second current memory observation and exact equality check before `finalize`. The default service bundle leaves this continuation unbound, so protocol and fixture wiring alone cannot complete production closeout.

### Conventions

`CloseoutCertificationHandoff` carries the actual contract, journal record/store and loaded selection. The reuse compiler owns gate choice; the executor does not infer success from missing work or manufacture replacement certificates.

### Invariants And Boundaries

- Wrong/stale owner, cancellation or a non-running record refuses before private execution.
- Original Gate-5 authority cannot be reused from unknown memory state; unavailable current memory invalidates reuse rather than becoming an unchanged assumption.
- The selected graph is rechecked around terminal publication, pruning protection and handoff; only allowed heartbeat-only journal changes are tolerated by the observation owner.
- A finalization result is whatever the bound owner actually returns. The default unbound continuation is an explicit refusal, not a success path.

### Todos

The default production memory/finalization continuation is not bound. Its installation and end-to-end proof belong to the composition owner.

## Docs References

The configured Domain Documentation registry has no entries. The source below establishes this repository-owned boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The handoff and currentness gate require the exact running uncancelled owner. | `CloseoutCertificationHandoff`; `_current_handoff` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:58-64; mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:67-90 |
| Execution inputs use original selected and predecessor evidence without latest lookup. | `_execution_inputs`; `_original_input_terminals`; `_inherited_memory_terminal` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:93-120; mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:123-137; mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:140-147 |
| Actual memory changes and selected certificate progress drive append-only recovery decisions. | `_observed_recovery_changes`; `_advance_recovery` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:150-166; mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:169-222 |
| The code gate receives explicit selection, publication protection and last-moment authorization callbacks. | `_run_code` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:225-263 |
| Current memory inputs are canonically reparsed after a live-owner observation. | `_observe_current_memory` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:266-276 |
| Suffix, Gate-5 observation and second-observation finalization dispatch remain explicit. | `execute_selected_closeout` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:279-332 |
| The default application service bundle does not bind a certification continuation. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:197-203 |

## Cross-Repo References

No cross-repository implementation or external protocol is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |
## Update History

- 2026-09-06T14:58:25+00:00 — Created after full source review at `c69d5171187fa1957025e393270db9f5a864ab14`. Records current implementation and remaining composition boundaries; source verification is not gate execution, delivery or acceptance.
