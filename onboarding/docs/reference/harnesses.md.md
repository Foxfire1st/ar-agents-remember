# docs/reference/harnesses.md

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| repository             | agents-remember                         |
| path                   | `docs/reference/harnesses.md`           |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-07-10T13:03+02:00                  |
| lastVerifiedCommitHash |                                         `e400ed0ce98752d1b65d00de97c9b84c7ea20814`|
| lastVerifiedCommitDate |                                         2026-07-10T20:04:45+02:00|
| governingOverview      | `../../overview.md`                     |

## Governing Overview

[root repo overview](../../overview.md) — the `docs/reference` route has no route-local overview
of its own (pre-existing registered gap; see the settings reference sidecar).

## Purpose

Manual for the agent-facing spawn surface: what a harness is, the built-in harness registry, how
`orchestration.harnesses` extends or overrides it, role/level spend knobs, dispatch refusal
statuses, and the worked example for adding a new harness id such as `hermes`.

## Code Commentary

**260707-HFX2-L15 current contract.** Codex is no longer an env-only builtin: resolved model and
effort ride `--model` and `--config model_reasoning_effort=<value>`, with the first-turn-safe enum
`none|minimal|low|medium|high|xhigh`. Spawn session commands remain separate inputs before the
brief, but submitted acceptance now comes only from the unique id in the bound harness JSONL;
command acceptance additionally requires its command record plus non-error stdout. Pane text is
used only to prevent a duplicate re-paste and to attach failure diagnostics, never to grant
acceptance or prove model/effort.

The page is documentation, not parser code. Runtime parsing lives in
`kernel/agentic_settings.py`, the built-in registry and per-harness delivery vehicles live in
`serving/harnesses.py`, and enforcement happens in `mcp/tools/terminal.py` during
`spawn_agent_session_payload`.

HFX2-L10 reframes the manual around settings-owned spend authority. Ordinary callers declare
`env.AR_SPAWN_ROLE` and `level`; they do not pass legacy `harness`/`model`/`effort`, direct
launch/session controls, `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT`, or harness-native spend/endpoint env
keys. Those caller values return `spend-override-unsupported` before any spawn side effect. The
manual still documents `launchArgs`, `sessionCommands`, and `promptKeywords`, but now as
settings-owned escape hatches that are recorded in spawn provenance.

## Invariants And Boundaries

- Harness ids are settings/launch identifiers, not commands; argv is defined only through the
  registry or `orchestration.harnesses`.
- The spend resolution chain is settings-only: repo-local level override > global level override >
  repo-local role default > global role default > spawn preference/detection.
- Harness-native spend env coverage is a maintained blocklist for the built-in Claude/Anthropic and
  Codex/OpenAI families; it is not a mathematical guarantee for every future env variable.
- The manual should point unknown or undetected harness readers to settings fixes, not to caller
  `spawn_agent_session(harness=...)` overrides.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Agentic settings parser that validates role knobs, rolesPerLevel, and `orchestration.harnesses`. | [../../mcp/src/agents_remember/kernel/agentic_settings.py](../../mcp/src/agents_remember/kernel/agentic_settings.py.md) |
| Built-in harness registry and delivery-vehicle vocabulary for model/effort application. | [../../mcp/src/agents_remember/serving/harnesses.py](../../mcp/src/agents_remember/serving/harnesses.py.md) |
| Spawn payload builder that enforces settings-only spend authority and pre-side-effect refusals. | [../../mcp/src/agents_remember/mcp/tools/terminal.py](../../mcp/src/agents_remember/mcp/tools/terminal.py.md) |
| Spawn tests pin settings-owned launch/session knobs and `spend-override-unsupported` refusals. | [../../mcp/tests/test_spawn_agent_session.py](../../mcp/tests/test_spawn_agent_session.py.md) |

## Update History

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: documented Codex's explicit argv mapping and exact
  effort enum, the bound-harness-log acceptance protocol, separate command verification, and the
  verified-absence/clear-before-replacement retry boundary. Verification metadata remains pinned
  until closeout stamps the eventual L15 code commit.

- 2026-07-09T12:04+02:00 — Created for 260707-HFX2-L10 (spawn settings authority) after the
  harness manual changed from explicit caller spend precedence to settings-only spend authority and
  documented the `spend-override-unsupported` refusal for legacy spend fields and maintained
  harness-native spend/env keys. Verification metadata pinned until closeout stamps the
  260707-HFX2-L10 commit.
