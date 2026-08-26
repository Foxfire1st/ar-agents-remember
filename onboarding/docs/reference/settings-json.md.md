# docs/reference/settings-json.md

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| repository             | agents-remember                         |
| path                   | `docs/reference/settings-json.md`       |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-07-10T13:03+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `../../overview.md`                     |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Agentic settings parser that implements the documented `orchestration.*` families. | "Read + merge the global (and optional repo-local) agentic settings, per use." | mcp/src/agents_remember/kernel/agentic_settings.py:213-213 |
| Spawn payload builder that enforces the settings-only spend surface and `spend-override-unsupported` refusals. | `spawn_agent_session_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:46-63 |
| Serving app that reads supervisor settings per sweep. |"logger.exception(\"agent-notifier sweep failed; retrying next interval\")"|mcp/src/agents_remember/serving/_app_lifespan.py:174-174|
| Supervisor implementation consuming the redelivery budget and repeated-signal cooldown. | `run_agent_notifier_sweep` | mcp/src/agents_remember/serving/agent_notifier.py:93-195 |
| Backoff math enforcing the shared 900-second redelivery floor documented here. | "redelivery interval" | mcp/src/agents_remember/kernel/primitives/inbox_backoff.py:69-69 |

## Update History
- 2026-08-10T09:45+02:00 — 260731-EFA-L9 curator repair: repaired agent-notifier settings and sweep citations.


- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the `escalationBudget` re-wiring in
  the settings reference — load-shed cap on owner-signal emissions (twin of
  `redeliverBudget`), superseding the L4 "reserved and removed with the demolition leaf"
  wording; dispatch-brief deadline-row wording updated. Verification metadata pinned until
  closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the `escalationBudget` reserved
  wording (N3 — ladder demolished as policy; knob no longer gates sweep behavior; removed with
  the L5 demolition leaf). Verification metadata pinned until closeout stamps the 260713-TES-L4
  commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 5 citation claims; scoped result 0 findings.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: refreshed the settings contract for Codex argv knobs,
  bound-log command verification, and the supervisor's one-row redelivery budget. Verification
  metadata remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 (spawn settings authority): the settings reference now
  states that role/level settings are the ordinary spend surface for spawned seats and that legacy
  caller spend fields plus maintained harness-native spend/endpoint env keys return
  `spend-override-unsupported`. It also removes the old explicit-argument precedence rung from
  `orchestration.spawn.harness`. Verification metadata pinned until closeout stamps the
  260707-HFX2-L10 commit.
- 2026-07-09T11:19+02:00 — 260707-HFX2-L9 (settings docs): refreshed the supervisor settings
  reference for the 900-second redelivery floor, new `signalCooldownSeconds`, fail-loud sub-floor
  validation, and `enabled: false` kill-switch mitigation wording. Verification metadata pinned
  until closeout stamps the 260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (settings docs): created sidecar after the settings
  reference gained the `orchestration.supervisor` section including `redeliverBudget` default 250
  and the safe-empty-block posture. Verification metadata pinned until closeout stamps the
  260707-HFX2-L8 commit.
