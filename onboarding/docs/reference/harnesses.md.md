# docs/reference/harnesses.md

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

HFX2-L10 reframes the manual around settings-owned spend authority. Public callers give
`dispatch_agent` only the canonical target document, role, and complete brief; the structural plane
derives role environment and dispatch level. They do not pass legacy `harness`/`model`/`effort`, direct
launch/session controls, `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT`, or harness-native spend/endpoint env
keys. Those caller values return `spend-override-unsupported` before any spawn side effect. The
manual still documents `launchArgs`, `sessionCommands`, and `promptKeywords`, but now as
settings-owned escape hatches that are recorded in spawn provenance.

ARSPAWN-L5 corrects the level explanation: the structural dispatcher derives `leaf`, `master`, or
`portfolio` from the canonical target document, not from the role name. This matters for reviewer,
which intentionally occupies leaf, master, and sprint review seats while retaining one role-level
settings family with per-level overrides.

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

## Evidence

### Docs References

The resolved source registry has no Domain Documentation entries, so no live external
documentation source was available for this pass. The manual is grounded in the consumed protocol
parsers, catalog normalizer, tests, and live/review evidence instead.

No configured live domain documentation could be checked.

### Repo-Internal References

The settings parser, spawn path, and native Claude parsers jointly implement the manual. The
references below use source evidence rather than treating this prose as runtime authority.

- The effective harness registry merges built-ins with settings and role-per-level knobs deep-merge over role defaults. [1]
- Built-in ids are registry identities, while native model validation is dynamic rather than a registry enum. [2]
- Spawn rejects caller spend overrides before side effects and sends settings-resolved model/effort through one typed native runner payload. [3]
- Claude initialize and `system/init` parse different required fields; the catalog request is a separate control message. [4]
- Startup orders correlated initialize/bootstrap before a separate correlated dynamic catalog request. [5]
- Catalog parsing preserves native model keys and nests each effort menu under its owning model row. [6]

### Cross-Repo References

The manual implements no runtime cross-repository boundary. The coordination task's independent
review is retained as verification provenance because it found and closed the earlier false claim
that initialize carried account/catalog data.
