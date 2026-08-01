# l-01-agent-lifecycles/roles/system-specialist.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/system-specialist.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T17:40+02:00                     |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77` |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [system-specialist.md](agents-remember/skills/l-01-agent-lifecycles/roles/system-specialist.md) |
| The detector this seat investigates: degradation events, metrics snapshot, critical failsafe. | whole module | [degradation.py](agents-remember/mcp/src/agents_remember/providers/degradation.py.md) |
| The orchestrator role file that dispatches this seat on a degradation-alert and reads its report. | n/a | [orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md) |
| The role census / escalation ladder registering `system-specialist` as the ninth portable role. | KNOWN_ROLES | [agentic_settings.py](agents-remember/mcp/src/agents_remember/kernel/agentic_settings.py.md) |
| The inbox role/message-kind schema this seat is addressed through (`AgentRole.system-specialist`, `degradation-alert`). | n/a | [operator_inbox_records.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_records.py.md) |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.


## Update History

- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-08T01:20+02:00 — 260707-HFX-L7 provider degradation protocol: created onboarding for
  the new investigate-first system-specialist seat (report-before-fix, providers-only scope,
  explicit-order fix mode, one-rung escalation to orchestrator). Gap-filled by the manager after
  the curator memory pass omitted this one package-data sidecar and closeout's onboarding-refresh
  gate blocked on it; every other L7 onboarding surface was written by the fresh curator pass
  (see the curator memory-pass report). Verification metadata pinned until closeout stamps the
  HFX-L7 commit.
