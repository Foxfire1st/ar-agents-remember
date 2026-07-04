# mcp/src/agents_remember/controlplane/enforcement.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/controlplane/enforcement.py`  |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-04T12:32+02:00                      |
| lastVerifiedCommitHash | `7679eb76a4c3137f7a4a5e02e455e7759f9d9c19`             |
| lastVerifiedCommitDate | 2026-07-04T12:58:55+02:00|
| governingOverview      | `overview.md`                                          |

## Purpose

`enforcement.py` is the pure gate-policy resolver. Given a lifecycle's current
gate set, a gate kind, and the configured `GatePolicy`, it decides whether the
operation guarded by that kind may proceed. `worktree_closeout_apply` still uses
the closeout wrapper, but the rule is now kind-generic.

## Code Commentary

`evaluate_gate(gates, *, kind, policy)` takes the folded live gate set
(`GateStore.current`, already last-wins by id) and returns a `GateGuard`
(`kind` / `permitted` / `reason` / `gate_id`). No gate of that kind → permitted
(gateless paths still rely on their legacy approval path). Otherwise the latest
snapshot for the kind (max by `ts`) governs: `approved` by the human
`developer` always permits; `approved` through `orchestration` permits only when
`gate_policy.approval_failure_reason` accepts the deciding role, lifecycle
identity, and required evidence. Every other state blocks with a reason the
caller raises. `evaluate_closeout_gate(gates, policy=...)` is the compatibility
wrapper around `kind="closeout-approval"`; `CloseoutGuard` aliases `GateGuard`.

## Invariants And Boundaries

- **Pure / I/O-free.** No store, no clock — callers read the store and raise;
  this module only decides. That keeps the policy unit-testable and lets
  closeout and future gate consumers share one rule.
- **Anti-self-approval is the point.** Human approval is always binding; an
  orchestration approval binds only when the policy delegates that gate kind,
  the deciding lifecycle/session differs from the gate-owning lifecycle, and any
  required reviewer-verdict evidence is attached. The closeout mutation (refuse
  + mark-applied) remains in `worktrees/modules/closeout.py`.
- **Additive.** A gateless lifecycle is permitted, so pre-6b / chat-only closeouts
  are unchanged.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The records + folded gate set this policy reads. | [records.py](agents-remember/mcp/src/agents_remember/controlplane/records.py) |
| The delegation policy validator and attribution checks used by this resolver. | [gate_policy.py](agents-remember/mcp/src/agents_remember/controlplane/gate_policy.py) |
| The mutating tool that enforces this policy (refuse + `apply_gate`). | [worktrees/modules/closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py) |
| The dashboard write-path that produces a developer-attributed approval. | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |

## Update History

- 2026-07-04T12:32+02:00 — 260703-L4: generalized the closeout-only resolver into
  `evaluate_gate(kind=..., policy=...)`, kept `evaluate_closeout_gate` as a
  compatibility wrapper, and documented delegated orchestration approvals as
  policy-checked and never self-approved. Verification metadata pinned until
  closeout stamps the L4 commit.
- 2026-06-26T14:16+02:00 — Task 25: updated the open-gate refusal wording to avoid teaching a lower-level wait helper as live agent choreography.
- 2026-06-18T12:10+02:00 — Created for task 6 slice 6b: the pure `evaluate_closeout_gate` closeout-gate policy + `CloseoutGuard` — the binding rule `worktree_closeout_apply` obeys (a developer-approved gate binds; a model self-approval is rejected; a gateless lifecycle permits). Verification metadata pinned to the task base until closeout stamps the 6b code commit.
