# mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46:26+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Selected closeout certification overview](overview.md)

## Purpose

Executes only the suffix admitted by the current selected closeout generation and hands exact remaining work to the bound memory/finalization owner.

## Code Commentary

### Logic

`execute_selected_closeout` first resumes already prepared publication through `resume_prepared_closeout`. For a selected certification run, `_refresh_selected_recovery` prepares the code view and reobserves current memory before deciding which original certificates remain reusable. This preserves the selected suffix and explicit successor requirements.

`execute_selected_closeout` begins with a live running owner, current contract/profile/route authority and the fully reopened selection. Selected red evidence refuses unchanged retry. The exact original certificate pool and retained terminal publications form `CodeCertificationExecution`; the current recovery decision determines the first gate to run.

Code execution uses the configured profile path and contract code base, supplying callbacks that select real recorded terminals, protect every referenced publication and recheck the live owner immediately before a start. After publication it reopens current state and appends a recovery decision derived from the actual selected prefix. An incomplete code prefix cannot enter memory.

An existing or inherited Gate-5 certificate requires a bound continuation and an actual current `GateFiveSemanticInputs` observation before reuse is considered. The observation is reparsed canonically and followed by a live journal check. Recovery decisions retain exact memory bytes; an unchanged decision is idempotent. Changed inputs for an already selected fifth terminal require an explicit successor. A current inherited fifth terminal is retained by its exact original reference.

First gate 5 hands off to `run_memory`. Finalization-only reuse performs a second current memory observation and exact equality check before `finalize`. The default service bundle binds `PreparedCloseoutContinuation` and `PreparedMemoryCertificationAdapter`; completion still requires the corresponding current runtime evidence.

### Conventions

`CloseoutCertificationHandoff` carries the actual contract, journal record/store and loaded selection. The reuse compiler owns gate choice; the executor does not infer success from missing work or manufacture replacement certificates.

### Invariants And Boundaries

- Wrong/stale owner, cancellation or a non-running record refuses before private execution.
- Original Gate-5 authority cannot be reused from unknown memory state; unavailable current memory invalidates reuse rather than becoming an unchanged assumption.
- The selected graph is rechecked around terminal publication, pruning protection and handoff; only allowed heartbeat-only journal changes are tolerated by the observation owner.
- A finalization result is whatever the bound owner actually returns. An absent continuation still produces an explicit refusal.

### Todos

No missing default continuation binding remains in this IAS source. Runtime certification and finalization evidence remain separate from source composition.

## Docs References

The configured Domain Documentation registry has no entries. The source below establishes this repository-owned boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact owner and selected objects passed to memory or finalization composition. | "class CloseoutCertificationHandoff" | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:58-64 |
| Reprove the live worker and selected authorities for a continuation action. | "def current_certification_handoff" | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:67-91 |
| Execution inputs use original selected and predecessor evidence without latest lookup. | `_execution_inputs`; `_original_input_terminals`; `_inherited_memory_terminal` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:94-121; mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:124-138; mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:141-148 |
| Actual memory changes and selected certificate progress drive append-only recovery decisions. | `_observed_recovery_changes`; `_advance_recovery` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:151-167; mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:170-223 |
| The code gate receives explicit selection, publication protection and last-moment authorization callbacks. | `_run_code` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:226-265 |
| Current memory inputs are canonically reparsed after a live-owner observation. | `_observe_current_memory` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:268-278 |
| Suffix, Gate-5 observation and second-observation finalization dispatch remain explicit. | `execute_selected_closeout` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:316-356 |
| The default application service bundle binds the prepared continuation and memory certification adapter. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:199-207 |

## Cross-Repo References

No cross-repository implementation or external protocol is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |
## Update History

- 2026-09-06T21:46:26+00:00 — Reconciled landed IAS helper ownership and current production composition; refreshed source anchors while preserving verification pins and historical evidence. No certification or delivery is asserted.

- 2026-09-06T14:58:25+00:00 — Created after full source review at `c69d5171187fa1957025e393270db9f5a864ab14`. Records current implementation and remaining composition boundaries; source verification is not gate execution, delivery or acceptance.
