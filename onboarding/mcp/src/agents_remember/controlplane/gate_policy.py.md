# mcp/src/agents_remember/controlplane/gate_policy.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`gate_policy.py` defines the validated delegation policy for durable lifecycle
gates. The default is all-human; orchestration delegation is strictly opt-in and
is additive, so it never removes the human approval path.

## Code Commentary

`DecisionRole` is the small policy vocabulary (`human`, `manager`,
`orchestrator`). `GatePolicyRule(kind, delegated_role, require_reviewer_verdict)`
declares one opt-in delegation rule; `GatePolicy.rule_for(kind)` returns an
explicit rule or an implicit human-only rule for unlisted gate kinds.

`make_gate_policy(...)` is the validation boundary. It normalizes
`delegated_role="human"` back to no delegation, rejects delegation for
human-pinned gate kinds (`integration-approval`, `push-approval`,
`cleanup-approval`), and currently allows non-human delegation only for the L4
leaf gate kinds (`plan-approval`, `closeout-approval`). A rule cannot require
reviewer-verdict evidence unless it actually delegates a non-human role. The
built-in `named_gate_policy` values are `all-human` and
`manager-decides-leaf-gates`.

`delegated_decision_failure_reason(gate, policy)` and
`approval_failure_reason(gate, policy)` are the server-side attribution checks:
delegated approvals must be decided via `orchestration`, name a deciding
lifecycle/session in `decidedBy`, carry a configured `decidingRole`, differ from
the gate-owning lifecycle, and include reviewer-verdict evidence when the rule
requires it.

Since 260731-EFA-L2 the first four of those are a named identity check of their own:
`_decision_attribution_failure_reason(gate)` answers *who decided, and through which channel*
before any policy is consulted — a decision that fails there names no role the policy could be
asked about. `delegated_decision_failure_reason` calls it first, returns its reason verbatim when
there is one, and only then coerces the role and consults `policy.rule_for(gate.kind)`. The
`assert gate.decidingRole is not None` after that call is not a guess: the attribution check
already proved it. Refusal messages and their order are identical to before the split.

## Invariants And Boundaries

- Defaults are all-human. A settings file must opt into every delegated kind.
- Human-pinned kinds are not configurable away: integration into main/super
  review, push approval, and destructive cleanup stay human.
- Delegation is additive. Humans can still decide a delegated kind, and delegated
  roles are accepted only by the server policy checks.
- Reviewer verdicts are gate evidence refs; this module checks presence, not the
  external artifact's contents.

## Evidence

### Repo-Internal References

- Gate records carry `decidedBy`/`decidedVia`/`decidingRole` and evidence refs checked here. [1]
- The pure resolver consumes this policy. [2]
- MCP settings parse the named/custom policy into this model. [3]
- Gate decision payloads reject invalid orchestration decisions before appending. [4]

As of the 260703-L8 seam ruling: `master-handover-approval` joins DELEGABLE_GATE_KINDS; SEAM_GATE_KINDS names the seam set; `apply_seam_verdict_requirement(policy)` binds reviewer-verdict evidence to every DELEGATED seam rule (the requireReviewerVerdictAtSeams wiring — human-decided seam kinds are untouched since the human sees the attached verdict); the named policy manager-decides-leaf-gates now also routes the master-exit handover to the ORCHESTRATOR.
