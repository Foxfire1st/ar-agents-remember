# mcp/src/agents_remember/kernel/primitives/gate_policy.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/kernel/primitives/gate_policy.py`   |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-08T14:38+02:00                                      |
| lastVerifiedCommitHash | `65cb81f7de4db13c0627264fec1eb46f444e0ee3`                  |
| lastVerifiedCommitDate | 2026-08-12T04:57:26+02:00|
| governingOverview      | `overview.md`                                               |

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

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The decision-role vocabulary is declared here in kernel. | `DecisionRole` | mcp/src/agents_remember/kernel/primitives/gate_policy.py:17-17 |
| Decision-role coercion is owned by the current policy primitive. | `coerce_decision_role` | mcp/src/agents_remember/kernel/primitives/gate_policy.py:69-72 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 citation maintenance: re-anchored the gate-vocabulary
  structural proof after the test responsibility split; documented behavior is unchanged.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the kernel gate-policy
  vocabulary extraction. Verification metadata pinned until closeout stamps the L9 code commit.
