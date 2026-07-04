# mcp/src/agents_remember/controlplane/gate_policy.py

| Field                  | Value                                               |
| ---------------------- | --------------------------------------------------- |
| repository             | agents-remember                                     |
| path                   | `mcp/src/agents_remember/controlplane/gate_policy.py` |
| doc_type               | `file-level-onboarding`                             |
| lastUpdated            | 2026-07-04T12:32+02:00                              |
| lastVerifiedCommitHash | `7679eb76a4c3137f7a4a5e02e455e7759f9d9c19`          |
| lastVerifiedCommitDate | 2026-07-04T12:58:55+02:00|
| governingOverview      | `overview.md`                                       |

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

## Invariants And Boundaries

- Defaults are all-human. A settings file must opt into every delegated kind.
- Human-pinned kinds are not configurable away: integration into main/super
  review, push approval, and destructive cleanup stay human.
- Delegation is additive. Humans can still decide a delegated kind, and delegated
  roles are accepted only by the server policy checks.
- Reviewer verdicts are gate evidence refs; this module checks presence, not the
  external artifact's contents.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Gate records carry `decidedBy`/`decidedVia`/`decidingRole` and evidence refs checked here. | [records.py](agents-remember/mcp/src/agents_remember/controlplane/records.py) |
| The pure resolver consumes this policy. | [enforcement.py](agents-remember/mcp/src/agents_remember/controlplane/enforcement.py) |
| MCP settings parse the named/custom policy into this model. | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| Gate decision payloads reject invalid orchestration decisions before appending. | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |

## Update History

- 2026-07-04T12:32+02:00 — 260703-L4: created for validated opt-in gate
  delegation policy, human-pinned gate protection, no-self-approval attribution,
  and reviewer-verdict evidence requirements. Verification metadata pinned until
  closeout stamps the L4 commit.
