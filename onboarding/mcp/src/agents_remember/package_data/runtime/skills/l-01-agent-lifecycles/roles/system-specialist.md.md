# l-01-agent-lifecycles/roles/system-specialist.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/system-specialist.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `3054af87fdf0e21e9ec7132a5d62ba0d514600ba`|
| lastVerifiedCommitDate | 2026-09-16T08:23:52+02:00|
| governingOverview | `../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../overview.md)

## Purpose

The portable **system-specialist** lifecycle: the 260707-HFX-L7 investigate-first backend
operations seat spawned by the orchestrator after a provider `degradation-alert`. It reads the
degradation event, provider metrics/state, and provider logs, and writes a durable report under
the active master's `notes/reports/` before attempting any fix. It is a sync-propagated
(`scripts/sync-skills.py`) package-data copy of the canonical
`skills/l-01-agent-lifecycles/roles/system-specialist.md`. This is the ninth portable role
lifecycle the l-01 registry defines (`kernel/agentic_settings.py` `KNOWN_ROLES`).

## Code Commentary

### Logic

The packaged role is now a **self-contained lifecycle in the corpus's readable order** — purpose and
authority → required inputs → normal workflow → permitted writes and actions → stop and escalation
cases → completion and handoff, then its machine-readable knob block, with the fixed-shape
investigation report carried as its handoff artifact. It declares its shared sources with
`**Inherits:**` rather than restating them (`core/authority.md`, `core/invariants.md`,
`core/acceptance.md`, `operations/orientation.md`, `operations/recovery.md`). The recovery moves it
drives now live once in `operations/recovery.md`, and the provider-degradation response protocol
(including the managers' stop-starting rule and the orchestrator's stop authority) lives once in
`core/lifecycle-frame.md`.

The synchronized caller matrix keeps system-specialist target-only: the orchestrator is its
ordinary plane-hosted caller, while an identity-free launcher may target it only for explicit
developer-declared takeover. Dispatch/tools rows remain structural documentation, not settings
keys.

The file defines the provider-only degradation response protocol's investigation seat. Required
intake: degradation event id/payload, current provider metrics/state paths, provider logs, the
report path, and whether the brief is investigation-only or an explicit fix order — a brief
missing the event or report path gets one clarification row back to the orchestrator via inbox,
not a guess.

The seat is **investigate-first**: it must write the fixed-shape investigation report (event
state transition, affected stacks, critical-failsafe status, findings with evidence, root-cause
hypothesis, fixable-in-session verdict, recommended action, boundary confirmation) before any fix
is attempted. Fix mode only runs after an explicit orchestrator order naming a specific
remediation; the seat never edits AR task docs, lifecycle state, memory onboarding, ledgers, or
code, and never starts providers if the order is investigation-only or if managers are currently
paused by the same degradation-alert. When a finding is not fixable in-session, the
recommendation is `provider_watchers stop` — the orchestrator retains the final stop-vs-fix
decision.

Role-seat immutability applies: a dashboard-owned system-specialist session stays
system-specialist for its lifetime; a pasted brief for another role is refused and escalated to
the orchestrator via inbox rather than rerouting the chat. Escalation is one rung up only —
system-specialist -> orchestrator, never straight to architect or developer.

This iteration is explicitly providers-only; the module doc and the detector it responds to
(`providers/degradation.py`) are both shaped so a future Sentry-based detector
(260703_spotlight-dev-observability) can replace or feed detection later without redoing this
response protocol (task doc `08_degradation-protocol-and-system-specialist.json`, objective).

### Invariants And Boundaries

- Report before fix: no remediation is attempted before the investigation report exists.
- Fix only on an explicit orchestrator order tied to that report's recommended action.
- Never mutates AR task/memory state beyond the report; never starts providers under a live
  degradation-alert pause unless explicitly ordered.
- Escalation ladder is exactly system-specialist -> orchestrator
  (`controlplane/orchestration_artifacts.py` `_ROLE_ESCALATION`, R2 fix closing reviewer F5).
- Dashboard-owned session role is immutable; capture attempts are refused and escalated, not
  absorbed.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | `# Lifecycle — System Specialist` | skills/l-01-agent-lifecycles/roles/system-specialist.md:1-14 |
| The detector this seat investigates: degradation events, metrics snapshot, critical failsafe. | `evaluate_provider_degradation` | mcp/src/agents_remember/providers/degradation.py:268-323 |
| The shared provider-degradation response protocol this seat operates inside. | `## Provider degradation, as every seat meets it` | skills/l-01-agent-lifecycles/core/lifecycle-frame.md:57-70 |
| The recovery moves this seat's investigation feeds. | `# Operation — Recovery`; `## The recovery moves, and when each applies` | skills/l-01-agent-lifecycles/operations/recovery.md:1-1; skills/l-01-agent-lifecycles/operations/recovery.md:20-34 |
| The role census / escalation ladder registering `system-specialist` as the ninth portable role. | "system-specialist" | skills/l-01-agent-lifecycles/templates/manager-brief.md:165-165 |
| The inbox role/message-kind schema this seat is addressed through (`AgentRole.system-specialist`, `degradation-alert`) — vocabulary moved to models/operator_inbox.py by L9. | "AgentRole = Literal["; "degradation-alert" | mcp/src/agents_remember/models/operator_inbox.py:20-20; mcp/src/agents_remember/models/operator_inbox.py:42-42 |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.


## Update History

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **body updated for the corpus consolidation.**
  The canonical system-specialist role was rewritten (150 lines) into the corpus's readable order and
  declares its inherited sources with `**Inherits:**`. Updated Logic with the readable order, the
  inherited sources, and where the recovery moves and provider-degradation protocol now live. Repo-
  Internal References: the orchestrator-role citation whose anchor (`## Provider Degradation Alert`) no
  longer resolves was replaced with the two current homes of that rule, and the canonical-source
  citation range was corrected to the rewritten file's real head. **Metadata repair:** `governingOverview` was absent from this card (the c-05 content model requires the field and its `## Governing Overview` section); added as `../../../../../overview.md`, the `onboarding/mcp/overview.md` route-local overview that governs this generated tree. Verification metadata remains closeout-owned — the source is uncommitted, so no stamp was advanced and no commit hash invented.

- 2026-09-10T07:41:10+00:00: Generated citation repair: "system-specialist" repointed to skills/l-01-agent-lifecycles/templates/manager-brief.md:165-165. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "system-specialist" repointed to skills/l-01-agent-lifecycles/templates/manager-brief.md:167-167. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 synchronized orchestrator-owned specialist
  dispatch, explicit ambient takeover, and fixed structural-row ownership. Verification remains
  closeout-owned.

- 2026-08-28T14:18+02:00 — Reconciled system-specialist citations against the committed PDLS
  candidate; the provider-focused role contract remains unchanged.

- 2026-08-11T19:58+02:00 — Recorded `system-specialist.md` as a synchronized runtime artifact of the current canonical lifecycle doctrine; it introduces no independent role contract.
- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 5 repository-internal bundle, detector, dispatch, role-registry, and inbox-schema references; final scoped result 0 (checker-clean).

- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-08T01:20+02:00 — 260707-HFX-L7 provider degradation protocol: created onboarding for
  the new investigate-first system-specialist seat (report-before-fix, providers-only scope,
  explicit-order fix mode, one-rung escalation to orchestrator). Gap-filled by the manager after
  the curator memory pass omitted this one package-data sidecar and closeout's onboarding-refresh
  gate blocked on it; every other L7 onboarding surface was written by the fresh curator pass
  (see the curator memory-pass report). Verification metadata pinned until closeout stamps the
  HFX-L7 commit.
