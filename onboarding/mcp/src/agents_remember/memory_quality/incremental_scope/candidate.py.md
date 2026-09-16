# mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-11T10:26:37+02:00 |
| lastVerifiedCommitHash | `806649b91bdce18f7b915bfbbf6727967f4e7a88` |
| lastVerifiedCommitDate | 2026-09-16T12:23:53+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

CCR-R06@v2 candidate observation: captures one exact external-memory leaf candidate by composing
the existing canonical owners — memory-candidate pair, Git trees, closeout-door baseline, R01
semantic topology, and R02 task intent — into an immutable `ScopeCandidateIdentity`. It is the
"exact code/memory candidate and validator generation" input of the R06 manifest and never invents
roots, identities, or fallbacks (worker handover: notes/reports/260831-CCR-L26-worker-delivery.md).

## Code Commentary

### Logic

`ContractScopeAuthority` is a frozen re-observable adapter over a `WorktreeContract`; its
`observe()` delegates to `observe_scope_candidate`
cit:([`ContractScopeAuthority`], mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:41-48).
`observe_scope_candidate` refuses non-leaf or non-external contracts (`candidate-not-external-leaf`,
`candidate-memory-root-missing`), resolves the pair, captures the future code candidate tree and the
memory candidate tree (a Git index staged from the memory worktree under
`reports/.scope-candidate-*/`), observes the task pair, and derives code/memory `GitTreeDelta`s
cit:([`observe_scope_candidate`], mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:51-95).
`observe_contract_task_pair` uses the closeout door as the immutable task baseline: it requires a
typed `TaskIntentIdentity`, exact contract/task/base-commit identity, and matching candidate trees,
then builds the baseline `CanonicalTaskObservation` from the door generation, schema version,
topology fingerprint, and intent cit:([`observe_contract_task_pair`], mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:98-111).
`observe_contract_task` walks the canonical task topology (leaf → master → sprint), derives the R01
topology fingerprint from the authored execution graph, reads R02 `task_intent_identity`, and
re-verifies the JSON/Markdown task sources with the CAS source observer before emitting the
candidate observation cit:([`observe_contract_task`], mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:114-172).
`observe_git_tree_delta` derives roots solely from `git diff-tree -r --name-status -z
--find-renames` between the base tree and candidate tree; `_parse_name_status` splits NUL records
and maps rename endpoints plus add/modify/delete changes with exact blobs
cit:([`observe_git_tree_delta`, `_parse_name_status`], mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:175-198; mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:201-258).

### Conventions

- Refusals are typed `ScopeUnprovenError(ScopeFailure(...))`; known owner failures are wrapped as
  `candidate-owner-unavailable` while already-typed refusals propagate unchanged.
- Candidate trees are produced through the existing `worktree_candidate_tree` helper so memory-index
  artifacts never enter the hashed candidate.
- All paths are canonical absolute POSIX; Git statuses outside A/M/D/R are an unclassified refusal.

## Invariants And Boundaries

- Changed roots come from exact Git tree diffs only; mtimes, directory scans, and caller filenames
  are not root authority.
- The closeout-door baseline must equal the exact contract authority (task id/name, base commits,
  candidate trees, leaf document) or the scope is `task-base-*` unproven.
- R01 topology and R02 intent projections are consumed, never copied or privately reissued.
- Task source mutation during observation (`task-source-moved`) fails closed.

## Docs References

No configured Domain Documentation applies; the observation contracts are repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external authority governs candidate observation. | — | — |

## Repo-Internal References

The observation seam reuses the exact R06 prerequisite owners: memory candidate pair resolution,
future code candidate capture, R02 task intent, R01 topology fingerprint, and the worktree Git
helpers.

| Finding | Anchor | Source |
| --- | --- | --- |
| Pair identity and roots come from the canonical memory candidate pair owner. | `resolve_memory_candidate_pair`, "return MemoryCandidatePairIdentity(" | mcp/src/agents_remember/memory_quality/memory_candidate_pair.py:48-144 |
| Code candidate tree comes from the memory-quality future-code capture. | `capture_future_code_candidate` | mcp/src/agents_remember/memory_quality/future_code_candidate.py:25-52 |
| Intent identity and topology fingerprint come from R02/R01 owners. | `task_intent_identity`, `candidate_task_topology_fingerprint` | mcp/src/agents_remember/tasks/task_intent.py:180-193; mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py:190-209 |
| Candidate observation owns exact code/memory identity and typed refusal; deleted tests provide no current execution proof. | `observe_scope_candidate` | mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:51-95 |

## Update History
- 2026-09-11T23:05:00+00:00: The pair-owner row anchored `MemoryCandidatePairIdentity`, which resolves three times in `memory_candidate_pair.py` (import, return annotation, and construction), so the claim could not be compared with its provenance. That anchor is now the exact constructor call text `return MemoryCandidatePairIdentity(`, which occurs once inside the cited extent; `resolve_memory_candidate_pair`, the cited range, and the claim's wording are unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `observe_contract_task_pair` repointed to mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:98-111. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `observe_contract_task` repointed to mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:114-172. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `observe_git_tree_delta`; `_parse_name_status` repointed to mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:175-198; mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:201-258. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: repointed the pair-resolver and future-code-capture citations to their relocated `memory_quality/` paths (commits `0b63d6fc`). Verification metadata remains pinned because only the cut-affected reference was reconciled; source documentation only, no acceptance claim.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=bb14594e277a8bc3ba7a0c8937f85adb359aa250a6a7cbd9793600d0bee68048; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 1ad9d51f743c5b17de51cc46d8b29e004736022d (CCR-R06@v2/L26): created the card for the new candidate-observation module of the R06v2 successor leaf; no prior sidecar existed.