# mcp/src/agents_remember/kernel/primitives/gate_policy.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/gate_policy.py` is the gate delegation policy for durable lifecycle gates
(policy half), moved into kernel by 260731-EFA-L9 so kernel no longer imports `controlplane`.
The default policy is intentionally today's behavior: every gate is human-decided; orchestration
delegation adds one configured role for specific gate kinds and never removes the human path.

## Code Commentary

### Logic

"class GatePolicyRule:" and "class GatePolicy:" (cit:(["class GatePolicy:"], mcp/src/agents_remember/kernel/primitives/gate_policy.py:54-54)) model the delegation rules;
`DEFAULT_GATE_POLICY` (cit:([`DEFAULT_GATE_POLICY`], mcp/src/agents_remember/kernel/primitives/gate_policy.py:66-66)) is the human-decided default. `coerce_decision_role`
(cit:([`coerce_decision_role`], mcp/src/agents_remember/kernel/primitives/gate_policy.py:69-69)) validates the `DecisionRole` vocabulary,
`make_gate_policy` builds a policy from rules, `named_gate_policy` resolves the named presets, and
`apply_seam_verdict_requirement` (cit:([`apply_seam_verdict_requirement`], mcp/src/agents_remember/kernel/primitives/gate_policy.py:130-130)) pins the seam
verdict requirement.

### Invariants And Boundaries

- Human-pinned gate kinds can never be delegated away; delegation is additive and role-scoped.
- Kernel owns the policy; the control plane consumes it, not the other way around.

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- The decision-role vocabulary is declared here in kernel. [1]
- Decision-role coercion is owned by the current policy primitive. [2]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
