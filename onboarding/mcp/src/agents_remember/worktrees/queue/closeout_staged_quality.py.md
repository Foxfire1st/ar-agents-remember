# mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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
| Linked-worktree and conflict refusals precede any index rewrite. | `_refuse_outside_a_linked_worktree`; `_refuse_conflicted_worktree` | mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:24-40; mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:43-55 |
| The staged gate proves the accepted tree around reset, staging, hook execution, and the targeted Dagger call. | `gate_staged_code` | mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:81-141 |
| Closeout imports this owner under the established private call name. | "gate_staged_code as _gate_staged_code" | mcp/src/agents_remember/worktrees/modules/closeout.py:87-87 |

## Cross-Repo References

No cross-repository implementation source governs this module.

## 260824-PDLS — Closeout Accepts Certifying Evidence Only

The staged closeout quality edge requires `CertifyingTestEvidence` for the closeout consumer after
the Dagger gate returns. A direct diagnostic exit code, JSON payload, node report, or candidate
binding cannot authorize the commit.

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the clean executor and quality-gate package relocations; exact staged-candidate enforcement is unchanged.
- 2026-08-24T21:23+02:00 — 260824-PDLS applied the evidence-altitude firewall at closeout.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner. Verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-14T05:26Z — Created for the L23 final candidate after staged-candidate enforcement was
  extracted from `closeout.py`; documented the same ordering with Dagger as the sole acceptance
  executor. Verification remains closeout-owned.
