# mcp/src/agents_remember/controlplane/gate_policy.py

| Field                  | Value                                               |
| ---------------------- | --------------------------------------------------- |
| repository             | agents-remember                                     |
| path                   | `mcp/src/agents_remember/controlplane/gate_policy.py` |
| doc_type               | `file-level-onboarding`                             |
| lastUpdated            | 2026-07-31T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`          |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Gate records carry `decidedBy`/`decidedVia`/`decidingRole` and evidence refs checked here. | "class GateRecord" | mcp/src/agents_remember/controlplane/records.py:45-45 |
| The pure resolver consumes this policy. | "class GateGuard" | mcp/src/agents_remember/controlplane/enforcement.py:42-42 |
| MCP settings parse the named/custom policy into this model. | "class McpRuntimeConfig" | mcp/src/agents_remember/kernel/primitives/runtime_config.py:123-123 |
| Gate decision payloads reject invalid orchestration decisions before appending. | "def gate_create_payload" | mcp/src/agents_remember/mcp/tools/gates.py:44-44 |

As of the 260703-L8 seam ruling: `master-handover-approval` joins DELEGABLE_GATE_KINDS; SEAM_GATE_KINDS names the seam set; `apply_seam_verdict_requirement(policy)` binds reviewer-verdict evidence to every DELEGATED seam rule (the requireReviewerVerdictAtSeams wiring — human-decided seam kinds are untouched since the human sees the attached verdict); the named policy manager-decides-leaf-gates now also routes the master-exit handover to the ORCHESTRATOR.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0911` armed with no exemptions):
  extracted `_decision_attribution_failure_reason(gate)` — the identity half of
  `delegated_decision_failure_reason` (channel, `decidedBy`, not-the-owning-lifecycle,
  `decidingRole` present) — leaving the policy half in the public function. Same refusal strings,
  same order, no policy change. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-05T16:30+02:00 - L8 seam-ruling remediation (cycle 4): seam kind delegable; at-seams flag wired via apply_seam_verdict_requirement; named policy routes handover to the orchestrator. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T12:32+02:00 — 260703-L4: created for validated opt-in gate
  delegation policy, human-pinned gate protection, no-self-approval attribution,
  and reviewer-verdict evidence requirements. Verification metadata pinned until
  closeout stamps the L4 commit.
