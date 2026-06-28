# mcp/src/agents_remember/controlplane/enforcement.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/controlplane/enforcement.py`  |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-06-26T14:16+02:00                      |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`             |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                          |

## Purpose

`enforcement.py` is the pure closeout-gate policy (slice 6b): given a lifecycle's
current gate set, may its closeout proceed? It is the binding layer over 6a's
records — the rule `worktree_closeout_apply` obeys server-side.

## Code Commentary

`evaluate_closeout_gate(gates)` takes the folded live gate set
(`GateStore.current`, already last-wins by id) and returns a `CloseoutGuard`
(`permitted` / `reason` / `gate_id`). No `closeout-approval` gate → permitted
(gateless: the chat commit gate still governs). Otherwise the latest
closeout-approval snapshot (max by `ts`) governs: `approved` **by `developer`**
permits; every other state — `open`, `rejected`, `revision-requested`,
`cancelled`, `expired`, `applied`, or **`approved` by `model`/`system`** — blocks
with a `reason` the caller raises. Open-gate refusal text now points the agent
back to the lifecycle gate channel rather than naming a lower-level wait helper.
`CLOSEOUT_GATE_KIND` / `BINDING_DECIDER` name the two constants the rule turns on.

## Invariants And Boundaries

- **Pure / I/O-free.** No store, no clock — the worktree tool reads the store and
  raises; this module only decides. That keeps the policy unit-testable and lets
  the tool and any future caller share one rule.
- **Anti-self-approval is the point.** Only `decidedBy="developer"` is binding; the
  agent's own `gate_decide` records `decidedBy="model"`, which this rejects. The
  *enforcement* (refuse + mark-applied) lives in `worktrees/modules/closeout.py`.
- **Additive.** A gateless lifecycle is permitted, so pre-6b / chat-only closeouts
  are unchanged.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The records + folded gate set this policy reads. | [records.py](agents-remember/mcp/src/agents_remember/controlplane/records.py) |
| The mutating tool that enforces this policy (refuse + `apply_gate`). | [worktrees/modules/closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py) |
| The dashboard write-path that produces a developer-attributed approval. | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |

## Update History

- 2026-06-26T14:16+02:00 — Task 25: updated the open-gate refusal wording to avoid teaching a lower-level wait helper as live agent choreography.
- 2026-06-18T12:10+02:00 — Created for task 6 slice 6b: the pure `evaluate_closeout_gate` closeout-gate policy + `CloseoutGuard` — the binding rule `worktree_closeout_apply` obeys (a developer-approved gate binds; a model self-approval is rejected; a gateless lifecycle permits). Verification metadata pinned to the task base until closeout stamps the 6b code commit.
