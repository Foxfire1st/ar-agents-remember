# docs/reference/harnesses.md

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| repository             | agents-remember                         |
| path                   | `docs/reference/harnesses.md`           |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-07-16T07:25+02:00                  |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../../overview.md`                     |

## Governing Overview

[root repo overview](../../overview.md) — the `docs/reference` route has no route-local overview
of its own (pre-existing registered gap; see the settings reference sidecar).

## Purpose

Manual for the agent-facing spawn and native-capability surface: what a harness is, how the
built-in registry and `orchestration.harnesses` interact, how role/level spend knobs reach native
adapters, which dispatch refusals are fail-loud, and which structured evidence establishes runtime
compatibility. It also distinguishes Claude's initialization, session-init, and dynamic catalog
sources so readers do not infer account/model data from the wrong envelope.

## Code Commentary

### Logic

The current Claude compatibility section is deliberately three-part. A correlated
`control_request/initialize` supplies command rows and pending interaction envelopes;
`system/init` supplies session identity, version, cwd, current model, permission mode, tools, and
slash commands; only a later correlated `control_request/list_models` supplies the dynamic model
rows and each row's own effort metadata. Claude Code 2.1.210 provided no account or catalog payload
in either initialization source. The catalog is live install/auth evidence, not a maintained model
or effort enum, and its observed rows must not be copied into dispatch policy.

**260707-HFX2-L15 current contract.** Codex is no longer an env-only builtin: resolved model and
effort ride `--model` and `--config model_reasoning_effort=<value>`. Spawn session commands remain
separate inputs before the brief, but submitted acceptance now comes only from the unique id in the
bound harness JSONL; command acceptance additionally requires its command record plus non-error
stdout. Pane text is used only to prevent a duplicate re-paste and to attach failure diagnostics,
never to grant acceptance or prove model/effort.

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

Production compatibility is negotiated from structured protocol evidence for Claude, Codex, and
Pi; exact package strings are fixture/smoke baselines only. The full reload boundary includes the
dashboard daemon, every MCP-owning client, each bridge-backed per-session runner/adapter, and open
browser tabs. This documentation does not authorize a restart or settings mutation.

### Conventions

- Role and level selectors are settings authority; ordinary spawn callers cannot override spend.
- Native adapter catalogs remain dynamic and model-gated. Version/account-specific observations
  may be recorded as live evidence, but never become default-path enums.
- Compatibility claims name the exact structured message that proves each field. Initialization,
  current-session state, and catalog discovery are not collapsed into one synthetic payload.

### Invariants And Boundaries

- Harness ids are settings/launch identifiers, not commands; argv is defined only through the
  registry or `orchestration.harnesses`.
- The spend resolution chain is settings-only: repo-local level override > global level override >
  repo-local role default > global role default > spawn preference/detection.
- Harness-native spend env coverage is a maintained blocklist for the built-in Claude/Anthropic and
  Codex/OpenAI families; it is not a mathematical guarantee for every future env variable.
- The manual should point unknown or undetected harness readers to settings fixes, not to caller
  `spawn_agent_session(harness=...)` overrides.
- Claude command rows come from correlated initialize, session/runtime fields come from
  `system/init`, and model/model-local-effort rows come only from correlated `list_models`.
- Captured model keys, row counts, defaults, and effort menus are install/auth observations, not
  normative enums or fallback data.
- Pane/log text, exact package versions, and account assumptions cannot substitute for the
  required structured evidence.

### Todos

None known for the L5 manual correction.

## Docs References

The resolved source registry has no Domain Documentation entries, so no live external
documentation source was available for this pass. The manual is grounded in the consumed protocol
parsers, catalog normalizer, tests, and live/review evidence instead.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain documentation could be checked. | — | — |

## Repo-Internal References

The settings parser, spawn path, and native Claude parsers jointly implement the manual. The
references below use source evidence rather than treating this prose as runtime authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| The effective harness registry merges built-ins with settings and role-per-level knobs deep-merge over role defaults. | `resolved_role_knobs`, "def _parse_harnesses(" | mcp/src/agents_remember/kernel/_agentic_settings_core.py:290-311; mcp/src/agents_remember/kernel/_agentic_settings_harness.py:26-26 |
| Built-in ids are registry identities, while native model validation is dynamic rather than a registry enum. | `find_harness`, `invalid_model_detail` | mcp/src/agents_remember/serving/harnesses.py:61-70; mcp/src/agents_remember/serving/harnesses.py:160-172 |
| Spawn rejects caller spend overrides before side effects and sends settings-resolved model/effort through one typed native runner payload. | `_caller_spend_override_refusal`, `spawn_agent_session_tool` | mcp/src/agents_remember/application/terminal_tools.py:570-607; mcp/src/agents_remember/application/terminal_tools.py:783-867 |
| Claude initialize and `system/init` parse different required fields; the catalog request is a separate control message. | `parse_control_initialization`, `parse_system_initialization`, `list_models_request` | mcp/src/agents_remember/serving/claude_stream_protocol.py:156-161; mcp/src/agents_remember/serving/claude_stream_protocol.py:219-232; mcp/src/agents_remember/serving/claude_stream_protocol.py:235-263 |
| Startup orders correlated initialize/bootstrap before a separate correlated dynamic catalog request. | `negotiate_claude_startup`, `negotiate_claude_catalog` | mcp/src/agents_remember/serving/claude_stream_startup.py:59-81; mcp/src/agents_remember/serving/claude_stream_startup.py:84-111 |
| Catalog parsing preserves native model keys and nests each effort menu under its owning model row. | `parse_list_models_response`, `_parse_model` | mcp/src/agents_remember/serving/claude_stream_capabilities.py:15-32; mcp/src/agents_remember/serving/claude_stream_capabilities.py:50-75 |
| Spawn regressions pin settings-only spend authority and pre-side-effect override refusal. | `test_level_override_deep_merges_harness_inherited`, `test_legacy_model_effort_args_are_refused_instead_of_beating_settings`, `test_spend_env_keys_are_refused_instead_of_overriding_settings` | mcp/tests/test_spawn_agent_session_settings.py:261-277; mcp/tests/test_spawn_agent_session_settings.py:309-318; mcp/tests/test_spawn_agent_session_settings.py:344-360 |

## Cross-Repo References

The manual implements no runtime cross-repository boundary. The coordination task's independent
review is retained as verification provenance because it found and closed the earlier false claim
that initialize carried account/catalog data.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 7 citation rows (all Tier 2), deleted 2 unresolvable task-report rows under the 2026-08-02 14:10 ruling, and scoped-checked the card with zero unresolved sources.
- 2026-07-16T07:25+02:00 — 260714-ACPUI-L5 curator: corrected the manual onboarding to the
  three-source Claude startup truth, made dynamic model/model-local-effort rows explicitly
  non-enumerative, and retained the independent review history that caught the former combined
  account/catalog claim. Verification remains pinned to the latest committed source touch until
  the reviewed L5 working-tree candidate is committed.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented structured capability negotiation, full serving
  reload boundary, and the explicit R10 deferred-performance boundary.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: documented Codex's explicit argv mapping and exact
  effort enum, the bound-harness-log acceptance protocol, separate command verification, and the
  verified-absence/clear-before-replacement retry boundary. Verification metadata remains pinned
  until closeout stamps the eventual L15 code commit.

- 2026-07-09T12:04+02:00 — Created for 260707-HFX2-L10 (spawn settings authority) after the
  harness manual changed from explicit caller spend precedence to settings-only spend authority and
  documented the `spend-override-unsupported` refusal for legacy spend fields and maintained
  harness-native spend/env keys. Verification metadata pinned until closeout stamps the
  260707-HFX2-L10 commit.
