# mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea` |
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Selected closeout certification overview](overview.md)

## Purpose

Executes only the suffix admitted by the current selected closeout generation and hands exact remaining work to the bound memory/finalization owner.

## Code Commentary

### Logic

**Since MIK-R09 (leaf 260928-MIK-L09, ruling 2026-09-30T14:38:47 gap 3)** `execute_selected_closeout` first asks `worktrees.knowledge_gate.prepared_closeout_refusal(contract)`, before recovery: this certified (prepared) path binds its memory commit to the curator-attested candidate, so it cannot set `closed: true` in the leaf's history file (MIK-R07 rule 7), and on converted memory it refuses through the path's own `refuse(...)` with `prepared-closeout-knowledge-history-unclosable`, naming why and that the leaf should close out through the worktree closeout commit. Unconverted memory is untouched (`None`). The path has no production caller today; `application/prepared_certification._realize_prepared_memory` carries the same check. Tested by `test_the_prepared_closeout_path_fails_closed_on_converted_memory`.

`execute_selected_closeout` then resumes already prepared publication through `resume_prepared_closeout`. For a selected certification run, `_refresh_selected_recovery` prepares the code view and reobserves current memory before deciding which original certificates remain reusable. This preserves the selected suffix and explicit successor requirements.

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
| Execution inputs use original selected and predecessor evidence without latest lookup. | `_execution_inputs`; `_original_input_terminals`; `_inherited_memory_terminal` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:99-126; mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:129-143; mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:146-153 |
| Actual memory changes and selected certificate progress drive append-only recovery decisions. | `_observed_recovery_changes`; `_advance_recovery` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:156-172; mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:175-251 |
| The code gate receives explicit selection, publication protection and last-moment authorization callbacks. | `_run_code` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:254-297 |
| Current memory inputs are canonically reparsed after a live-owner observation. | `_observe_current_memory` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:300-310 |
| The prepared path refuses on converted memory before recovery (MIK-R09 gap 3). | "unclosable = prepared_closeout_refusal(contract)" | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:359-361 |
| Suffix, Gate-5 observation and second-observation finalization dispatch remain explicit. | `execute_selected_closeout` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:348-391 |
| The default application service bundle binds the prepared continuation and memory certification adapter (beside, since MIK-R24, the knowledge validator's base converter and the knowledge crossing). | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:211-224 |

## Cross-Repo References

No cross-repository implementation or external protocol is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |
## Update History
- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **body updated for MIK-R09.** Logic records the new first step of `execute_selected_closeout`: on converted memory the prepared path refuses `prepared-closeout-knowledge-history-unclosable` before recovery, because it cannot close the leaf's history file (ruling 14:38:47 gap 3); one row added. The rows below the insertion were normalised by the installed fixer.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Reopened claim re-read (MIK-R24).** `build_default_worktree_services` changed: it binds the base converter and the knowledge crossing. The row still holds and was reworded to name them. This folds in the fixer projection of this pass. No claim about this card's own source changed.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `_observe_current_memory` repointed to mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:296-306. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=838e6af3d423e498e13a179e926b86d3a68150c359c44211a378378635e7073f; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-06T21:46:26+00:00 — Reconciled landed IAS helper ownership and current production composition; refreshed source anchors while preserving verification pins and historical evidence. No certification or delivery is asserted.

- 2026-09-06T14:58:25+00:00 — Created after full source review at `c69d5171187fa1957025e393270db9f5a864ab14`. Records current implementation and remaining composition boundaries; source verification is not gate execution, delivery or acceptance.
