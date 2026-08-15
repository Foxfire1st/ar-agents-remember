# mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-14T05:26Z |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate |  2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Own exact staged-candidate materialization and Dagger quality enforcement for closeout. The
extraction keeps disposable-worktree refusal, conflict refusal, candidate-tree proof, configured
fast-hook handling, and the strict targeted gate in one cohesive pre-commit boundary.

## Code Commentary

### Logic

`gate_staged_code` refuses the primary checkout and unresolved conflicts before replacing the
index. It proves an accepted candidate before staging, resets and stages the entire task worktree,
proves the staged tree, runs the configured pre-commit hook, restages, proves the hook did not
change the reviewed tree, and finally invokes the targeted strict Dagger plan.

### Conventions

Candidate comparisons use exact Git tree ids; the fast hook is a reviewed pre-gate transformer,
while `commit_verified_staged` later commits the certified index without rerunning hooks.

### Invariants And Boundaries

- Only a disposable linked task worktree may have its index replaced.
- Conflicts are refused before `git reset --mixed` can erase unmerged-index evidence.
- The candidate tree is immutable across acceptance, staging, and the configured hook.
- Acceptance runs through `QualityGatePlan(mode="targeted", executor="dagger")`; there is no host
  test compatibility path.
- This module stages and certifies; approval claim and commit ordering remain in `closeout.py`.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-internal enforcement seam.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Linked-worktree and conflict refusals precede any index rewrite. | `_refuse_outside_a_linked_worktree`; `_refuse_conflicted_worktree` | mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:20-51 |
| The staged gate proves the accepted tree around reset, staging, hook execution, and the targeted Dagger call. | `gate_staged_code` | mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:77-129 |
| Closeout imports this owner under the established private call name. | "gate_staged_code as _gate_staged_code" | mcp/src/agents_remember/worktrees/modules/closeout.py:37-37 |

## Cross-Repo References

No cross-repository implementation source governs this module.

## Update History

- 2026-08-14T05:26Z — Created for the L23 final candidate after staged-candidate enforcement was
  extracted from `closeout.py`; documented the same ordering with Dagger as the sole acceptance
  executor. Verification remains closeout-owned.
