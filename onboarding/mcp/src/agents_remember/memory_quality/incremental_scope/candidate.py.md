# mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `1ad9d51f743c5b17de51cc46d8b29e004736022d` |
| lastVerifiedCommitDate | 2026-09-02T06:25:51+02:00 |
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
cit:([`observe_scope_candidate`], mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:51-99).
`observe_contract_task_pair` uses the closeout door as the immutable task baseline: it requires a
typed `TaskIntentIdentity`, exact contract/task/base-commit identity, and matching candidate trees,
then builds the baseline `CanonicalTaskObservation` from the door generation, schema version,
topology fingerprint, and intent cit:([`observe_contract_task_pair`], mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:102-149).
`observe_contract_task` walks the canonical task topology (leaf → master → sprint), derives the R01
topology fingerprint from the authored execution graph, reads R02 `task_intent_identity`, and
re-verifies the JSON/Markdown task sources with the CAS source observer before emitting the
candidate observation cit:([`observe_contract_task`], mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:152-210).
`observe_git_tree_delta` derives roots solely from `git diff-tree -r --name-status -z
--find-renames` between the base tree and candidate tree; `_parse_name_status` splits NUL records
and maps rename endpoints plus add/modify/delete changes with exact blobs
cit:([`observe_git_tree_delta`, `_parse_name_status`], mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:213-296).

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
| Pair identity and roots come from the canonical memory candidate pair owner. | `resolve_memory_candidate_pair`, `MemoryCandidatePairIdentity` | mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pair.py |
| Code candidate tree comes from the closeout future-code capture. | `capture_future_code_candidate` | mcp/src/agents_remember/worktrees/integration/closeout/future_code_candidate.py |
| Intent identity and topology fingerprint come from R02/R01 owners. | `task_intent_identity`, `candidate_task_topology_fingerprint` | mcp/src/agents_remember/tasks/task_intent.py; mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py |
| The typed refusal vocabulary (`task-base-unavailable`, `git-change-unclassified`, ...) is exercised by the scope candidate tests. | `test_missing_canonical_task_baseline_refuses_before_current_identity_is_derived`; `test_unclassified_git_status_and_candidate_tree_helper_fail_closed` | mcp/tests/test_memory_incremental_scope_candidate.py:91-127; mcp/tests/test_memory_incremental_scope_candidate_edges.py:455-474 |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 1ad9d51f743c5b17de51cc46d8b29e004736022d (CCR-R06@v2/L26): created the card for the new candidate-observation module of the R06v2 successor leaf; no prior sidecar existed.