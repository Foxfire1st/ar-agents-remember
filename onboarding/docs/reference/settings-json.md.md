# docs/reference/settings-json.md

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| repository             | agents-remember                         |
| path                   | `docs/reference/settings-json.md`       |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-07-10T13:03+02:00 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`|
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
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

Documented the new `orchestration.supervisor.escalationBudget` reference row: the supervisor now has a settings-owned per-sweep cap for escalation-rung emissions, distinct from `redeliverBudget`, and deferred rung-due rows stay level-triggered for the next sweep.

The page is documentation, not parser code. Runtime parsing lives in `kernel/agentic_settings.py`
for `orchestration.*` and the MCP authority/config loaders for boot infrastructure. HFX2-L8 added the
`orchestration.supervisor` table documenting safe defaults for the deterministic supervisor sweep:
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
- The supervisor redelivery and repeated-signal cadence floor is 900 seconds; docs must not suggest
  a sub-15-minute setting can run.
- The supervisor redelivery budget is a conservative default, not a required operator knob.
- The settings reference should not describe caller-supplied `spawn_agent_session` spend fields as
  a valid precedence rung; HFX2-L10 makes settings the spend authority and treats those caller
  fields as compatibility refusals.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Agentic settings parser that implements the documented `orchestration.*` families. | "Read + merge the global (and optional repo-local) agentic settings, per use." | mcp/src/agents_remember/kernel/agentic_settings.py:221-221 |
| Spawn payload builder that enforces the settings-only spend surface and `spend-override-unsupported` refusals. | `spawn_agent_session_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:46-63 |
| Serving app that reads supervisor settings per sweep. |"logger.exception(\"supervisor sweep failed; retrying next interval\")"|mcp/src/agents_remember/serving/_app_lifespan.py:107-107|
| Supervisor implementation consuming the redelivery budget and repeated-signal cooldown. | `run_supervisor_sweep` | mcp/src/agents_remember/serving/supervisor.py:96-193 |
| Backoff math enforcing the shared 900-second redelivery floor documented here. | "redelivery interval" | mcp/src/agents_remember/controlplane/inbox_backoff.py:45-45 |

## Update History
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 5 citation claims; scoped result 0 findings.
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
