# mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T07:08:26+00:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Own exact staged-candidate materialization and repository-profile quality enforcement for
closeout. The extraction keeps disposable-worktree refusal, conflict refusal, candidate-tree
proof, configured fast-hook handling, and the strict targeted profile gate in one cohesive
pre-commit boundary. Since CCR-R22@v1 (L22, commit `685f83c44055`) the gate consumes a
`QualityGateTarget` (checkout, worktree group, repository id, profile reference) instead of a
bare checkout plus a settings executor; the executor identity and the exact staged contract now
come from the repository's admitted profile.

## Code Commentary

### Logic

`gate_staged_code(target, *, diff_base, candidate_tree)` reads `code_worktree`/
`worktree_group` from the `QualityGateTarget`, refuses the primary checkout and unresolved
conflicts before replacing the index, proves an accepted candidate before staging, resets and
stages the entire task worktree, proves the staged tree, runs the configured pre-commit hook,
restages, proves the hook did not change the reviewed tree, and finally invokes the targeted
strict profile gate with `QualityGatePlan(mode="targeted")`. The old `executor="dagger"`
parameter and `code_worktree`/`worktree_group`/`executor` positional signature were removed:
executor identity belongs to the profile.

### Conventions

Candidate comparisons use exact Git tree ids; the fast hook is a reviewed pre-gate transformer,
while `commit_verified_staged` later commits the certified index without rerunning hooks.

### Invariants And Boundaries

- Only a disposable linked task worktree may have its index replaced.
- Conflicts are refused before `git reset --mixed` can erase unmerged-index evidence.
- The candidate tree is immutable across acceptance, staging, and the configured hook.
- Acceptance runs through `QualityGatePlan(mode="targeted")` against the admitted repository
  profile; there is no host test compatibility path and no settings-level executor.
- This module stages and certifies; approval claim and commit ordering remain in `closeout.py`.

### Todos

None recorded.

## Docs References

CCR-R22@v1 requires the exact staged candidate to run through the profile-declared adapter before
any commit, with missing/invalid profile authority refusing as certification-profile-invalid.

| Finding | Anchor | Source |
| --- | --- | --- |
| Invalid profile resolution produces typed admission failure before any Gate-1 command starts. | `_admitted_selection` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:548-562 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Linked-worktree and conflict refusals precede any index rewrite. | `_refuse_outside_a_linked_worktree`; `_refuse_conflicted_worktree` | mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:24-40; mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:43-55 |
| The staged gate proves the accepted tree around reset, staging, hook execution, and the targeted profile call. | `gate_staged_code` | mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:81-141 |
| Closeout imports this owner under the established private call name. | "from agents_remember.worktrees.queue.closeout_staged_quality import (" | mcp/src/agents_remember/worktrees/modules/closeout.py:103-105 |
| The strict closeout preflight passes the profile-built target, code diff base and candidate tree to this owner before any external-memory preflight. | "def _closeout_quality_preflight(" | mcp/src/agents_remember/worktrees/modules/closeout.py:800-839 |
| The strict gate admits the same target/profile and certifies the index. | `run_strict_code_quality_gate` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:243-324 |

## Cross-Repo References

No cross-repository implementation source governs this module.

## 260824-PDLS — Closeout Accepts Certifying Evidence Only

The staged closeout quality edge requires `CertifyingTestEvidence` for the closeout consumer
after the profile gate returns. A direct diagnostic exit code, JSON payload, node report, or
candidate binding cannot authorize the commit.

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `_admitted_selection` repointed to mcp/src/agents_remember/worktrees/modules/quality/gate.py:548-562. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-05T07:11:24+00:00 — Reviewed the report-only reopened strict-gate claim against both
  `685f83c4405570ca8356e7481e0e2a9a16945757` and frozen `ea359649`: the current runner adds
  certification-record freezing/publication and delegates report composition, while retaining
  the target/profile request and exact candidate-tree evidence checks. Retained the claim and
  expanded its citation to the full current function at lines 243–324. The historical
  verification stamp remains unchanged, so the checker may continue to surface this reviewed
  structural change; this entry does not assert execution or acceptance.

- 2026-09-05T07:08:26+00:00 — L31 final residual curation against frozen code `ea35964985f30080488270e71ac81657ac40682b`: Split the import alias from its caller; read the current Gate-5 ordering and recorded that strict code-quality refusal blocks the following memory preflight. This scoped repair does not promote the card's verification stamp or certify a gate.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `_admitted_selection` repointed to mcp/src/agents_remember/worktrees/modules/quality/gate.py:577-591. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the signature cutover to `QualityGateTarget` (repository context + profile reference) and the removal of the settings-level `executor` parameter; the targeted plan is now profile-owned.

- 2026-08-26T10:44:52+02:00 -- No content impact: reviewed the clean executor and quality-gate package relocations; exact staged-candidate enforcement is unchanged.
- 2026-08-24T21:23+02:00 -- 260824-PDLS applied the evidence-altitude firewall at closeout.

- 2026-08-22T10:39+02:00 -- 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner.

- 2026-08-21T00:45+02:00 -- 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py` (new package route); import paths updated inside the module. Verified at code commit e5cb139f.

- 2026-08-14T05:26Z -- Created for the L23 final candidate after staged-candidate enforcement was extracted from `closeout.py`; documented the same ordering with Dagger as the sole acceptance executor.
