# docs/reference/settings-json.md

## Governing Overview

[root repo overview](../../overview.md) — the `docs/reference` route has no route-local overview
of its own (pre-existing registered gap; see the skills reference sidecar).

## Purpose

Public settings reference for Agents Remember. It separates the four settings homes (MCP
authority, memory topology, agentic orchestration, provider lifecycle), documents their read
cadence, and gives examples for internal/external memory and MCP authority files.

## Code Commentary

**260707-HFX2-L15 current contract.** The settings reference now names Codex's explicit
`--model`/`--config model_reasoning_effort=` mapping, describes post-bind harness-log verification
for session commands, and sets the default supervisor `redeliverBudget` to `1`. The single-row
budget is part of the delivery latency bound: one log-confirmed input may consume three calibrated
acceptance windows, so one sweep must not multiply that synchronous wait across a backlog.

### 260707-HFX2-L12 CS-6 Update

Documented the new `orchestration.agent-notifier.escalationBudget` reference row: the supervisor now has a settings-owned per-sweep cap for escalation-rung emissions, distinct from `redeliverBudget`, and deferred rung-due rows stay level-triggered for the next sweep.

**260713-TES-L4 — escalationBudget reserved (N3).** The `escalationBudget` reference row now
states the timed escalation ladder is demolished as policy: inbox rows resolve by the 5-attempt
ceiling (`unresolved`), the 5-minute rebind grace, or explicit supersession. The knob no longer
gates sweep behavior and is removed with the L5 demolition leaf.

**260713-TES-L5 — escalationBudget is a load-shed cap.** The L4 "reserved/removed" row is
superseded: `escalationBudget` (250) is now the per-sweep load-shed cap on owner-signal
emissions (seat-liveness + dead-upstream), the twin of `redeliverBudget`; shed findings re-fire
next sweep (level-triggered). The timed escalation ladder is retired — rows resolve by
landing/ceiling/grace, never a rung.

The page is documentation, not parser code. Runtime parsing lives in `kernel/agentic_settings.py`
for `orchestration.*` and the MCP authority/config loaders for boot infrastructure. HFX2-L8 added the
`orchestration.agentNotifier` table documenting safe defaults for the deterministic agent-notifier sweep:
`enabled`, `intervalSeconds`, `staleCutoffSeconds`, `redeliverRateLimitSeconds`, and
`redeliverBudget` (default 250) so an empty supervisor block remains bounded during large inbox
backlogs. HFX2-L9 updates that table for the production redelivery incident:
`redeliverRateLimitSeconds` inherits a store default of 900 seconds, `signalCooldownSeconds` defaults
to 900 seconds, both reject below-floor values, `redeliverBudget` remains the per-sweep backlog cap,
and `enabled: false` is documented as the emergency supervisor kill switch used until the
cadence/cooldown fix lands and passes smoke. HFX2-L10 updates the role-knob and spawn sections to
make settings the ordinary developer-controlled spend surface: callers declare role/level, while
legacy `harness`/`model`/`effort`, direct launch/session controls, namespaced spawn model/effort env,
and maintained Claude/Anthropic + Codex/OpenAI harness-native spend/endpoint env keys refuse with
`spend-override-unsupported`; the doc points readers to `docs/reference/harnesses.md` for the full
spawn-surface manual.

## Invariants And Boundaries

- Settings families have exactly one home; do not present coordinator `system/settings.json` as an
  MCP authority file.
- Unknown keys under `orchestration.*` fail loud in the parser; docs must track parser field names.
- The agent-notifier redelivery and repeated-signal cadence floor is 900 seconds; docs must not suggest
  a sub-15-minute setting can run.
- The agent-notifier redelivery budget is a conservative default, not a required operator knob.
- The settings reference should not describe caller-supplied `spawn_agent_session` spend fields as
  a valid precedence rung; HFX2-L10 makes settings the spend authority and treats those caller
  fields as compatibility refusals.

## Evidence

### Repo-Internal References

- Agentic settings parser that implements the documented `orchestration.*` families. [1]
- Spawn payload builder that enforces the settings-only spend surface and `spend-override-unsupported` refusals. [2]
- Serving app that reads supervisor settings per sweep. [3]
- Supervisor implementation consuming the redelivery budget and repeated-signal cooldown. [4]
- Backoff math enforcing the shared 900-second redelivery floor documented here. [5]
