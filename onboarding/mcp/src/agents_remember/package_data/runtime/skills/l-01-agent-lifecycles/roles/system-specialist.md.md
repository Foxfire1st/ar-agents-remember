# l-01-agent-lifecycles/roles/system-specialist.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

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

## Evidence

### Repo-Internal References

- Canonical source this bundle copy is sync-propagated from. [1]
- The detector this seat investigates: degradation events, metrics snapshot, critical failsafe. [2]
- The shared provider-degradation response protocol this seat operates inside. [3]
- The recovery moves this seat's investigation feeds. [4]
- The role census / escalation ladder registering `system-specialist` as the ninth portable role. [5]
- The inbox role/message-kind schema this seat is addressed through (`AgentRole.system-specialist`, `degradation-alert`) — vocabulary moved to models/operator_inbox.py by L9. [6]

### Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

No meaningful cross-repo references found.

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.
