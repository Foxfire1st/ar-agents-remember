# mcp/src/agents_remember/controlplane/enforcement.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/controlplane/enforcement.py`  |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-08-01T19:45+02:00                      |
| lastVerifiedCommitHash | `a714114ef94eedb8042fb4caa38d9469f4767dd6`             |
| lastVerifiedCommitDate | 2026-08-01T18:06:36+02:00|
| governingOverview      | `overview.md`                                          |

## Purpose

`enforcement.py` is the pure gate-policy resolver. Given a lifecycle's current
gate set, a gate kind, and the configured `GatePolicy`, it decides whether the
operation guarded by that kind may proceed. `worktree_closeout_apply` still uses
the closeout wrapper, but the rule is now kind-generic.

## Code Commentary

### 260731-EFA-L5 The `applied` Refusal Is Now Load-Bearing, And This Module Is Called Under A Lock

Nothing in this module's logic changed — the only source edit is that `CLOSEOUT_GATE_KIND` gained
its `: GateKind` annotation, which puts the literal in front of the type checker instead of leaving
it a bare `str`. What changed is **what depends on the `applied` branch**, and a reader of this card
needs it.

`evaluate_gate`'s `applied` arm returns *"{kind} gate {id} was already applied; open a fresh gate
for a new mutation"*. That refusal is now the **sole** mechanism stopping one human approval from
being spent twice — there is no counter, no ledger and no second check anywhere. Two things had to
happen elsewhere before it could carry that weight:

- **The record it reads has to still be there.** `interaction_retention` pruned `applied` at any
  age until this leaf; the reclaim pass erased the marker within milliseconds of the next decision,
  and this function then returned *permitted-gateless* — not "already applied" — because it saw no
  gate of the kind at all. `CONSUMED_APPROVAL_GATE_KINDS` closed that.
- **The fold has to still be true when the verdict is used.** This function is pure and has no way
  to know how stale its `gates` argument is. `store.GateStore.claim_approval` now calls it **inside
  a held `exclusive_access`** on the gate log, with the `applied` append in the same critical
  section, which is what makes `approved -> applied` a compare-and-swap rather than a check followed
  much later by an act.

The purity of this module is why that was possible: because it takes a `Mapping` and no store, the
call could be moved under a lock without moving any I/O into it.

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
  required reviewer-verdict evidence is attached.
- **The mutation moved out of `closeout.py` (260731-EFA-L5).** The earlier "the closeout mutation
  (refuse + mark-applied) remains in `worktrees/modules/closeout.py`" is retracted. Closeout's
  `_mark_closeout_gate_applied` was **deleted**; the `applied` append now happens in
  `store.GateStore.claim_approval`, in the same held lock as the `evaluate_gate` call that permitted
  it. Closeout keeps only a deny-only early read (`_refuse_unsatisfied_closeout_gate`) and the call
  to `claim_approval`.
- **The `applied` refusal is the whole replay defence.** It is the only thing that stops one
  approval being spent twice, so its arm must never be softened to a warning, and the record it
  reads must stay retained (`interaction_retention.CONSUMED_APPROVAL_GATE_KINDS`). If the record is
  gone this function does not report "already applied" — it reports *permitted-gateless*, which
  permits.
- **Additive.** A gateless lifecycle is permitted, so pre-6b / chat-only closeouts
  are unchanged.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The records + folded gate set this policy reads. | [records.py](agents-remember/mcp/src/agents_remember/controlplane/records.py) |
| The delegation policy validator and attribution checks used by this resolver. | [gate_policy.py](agents-remember/mcp/src/agents_remember/controlplane/gate_policy.py) |
| The mutating tool that enforces this policy: `_refuse_unsatisfied_closeout_gate` at L424-L446 (deny-only, writes nothing) and `_claim_closeout_gate` at L449-L499 (the spend). It no longer appends an `applied` snapshot itself. | [worktrees/modules/closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py) |
| `GateStore.claim_approval` — the compare-and-swap that calls `evaluate_gate` and appends `applied` in one held lock. | [store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| `CONSUMED_APPROVAL_GATE_KINDS` — what keeps the `applied` snapshot this resolver's refusal depends on from being reclaimed. | [interaction_retention.py](agents-remember/mcp/src/agents_remember/controlplane/interaction_retention.py) |
| The dashboard write-path that produces a developer-attributed approval. | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |

## Update History

- 2026-08-01T19:45+02:00 — 260731-EFA-L5 (durable store integrity). Source edit is one line —
  `CLOSEOUT_GATE_KIND` gained its `: GateKind` annotation — but the card's account of where the
  mutation lives was stale and is corrected: `_mark_closeout_gate_applied` was **deleted** from
  `closeout.py` and the `applied` append now happens in `GateStore.claim_approval`, inside the same
  held `exclusive_access` as the `evaluate_gate` call that permitted it, so this pure verdict is now
  consumed under a lock. Recorded that the `applied` refusal arm is the **sole** replay defence, and
  the two conditions it depends on: the record surviving reclamation
  (`CONSUMED_APPROVAL_GATE_KINDS`) and the fold still being true when the verdict is used. Noted the
  failure mode that makes this sharp — with the record gone this function returns *permitted-gateless*,
  not "already applied". Replaced the closeout reference row with the two current symbols and added
  two rows. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-07-04T12:32+02:00 — 260703-L4: generalized the closeout-only resolver into
  `evaluate_gate(kind=..., policy=...)`, kept `evaluate_closeout_gate` as a
  compatibility wrapper, and documented delegated orchestration approvals as
  policy-checked and never self-approved. Verification metadata pinned until
  closeout stamps the L4 commit.
- 2026-06-26T14:16+02:00 — Task 25: updated the open-gate refusal wording to avoid teaching a lower-level wait helper as live agent choreography.
- 2026-06-18T12:10+02:00 — Created for task 6 slice 6b: the pure `evaluate_closeout_gate` closeout-gate policy + `CloseoutGuard` — the binding rule `worktree_closeout_apply` obeys (a developer-approved gate binds; a model self-approval is rejected; a gateless lifecycle permits). Verification metadata pinned to the task base until closeout stamps the 6b code commit.
