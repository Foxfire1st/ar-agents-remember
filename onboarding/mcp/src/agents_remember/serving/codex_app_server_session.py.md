# mcp/src/agents_remember/serving/codex_app_server_session.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_session.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T23:00+02:00 |
| lastVerifiedCommitHash | `5fa7026c644edfb4eb884173b64d31c9a14a6585` |
| lastVerifiedCommitDate | 2026-07-15T23:33:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns Codex app-server initialization, complete paginated model discovery, dynamic model/effort
resolution, configured thread start/resume, retained acceptance evidence, and a separate
thread-free discovery path.

## Code Commentary

### Logic

`connect` starts transport, initializes the app-server, reads every `model/list` page including
hidden models, selects either the requested model or the single visible advertised default, and
resolves either the requested effort or that model's advertised default. It validates the pair,
writes both values into `thread/start`/`thread/resume` config, rejects pre-existing conflicting
config, and verifies echoed thread identity, CLI version, model, cwd, and effective effort before
retaining the full catalog. The resolved desired effort is also the value used for later turns and
settings-update checks. `discover` initializes/lists only and always stops transport; `advertise`
normalizes retained running evidence without another RPC.

### Conventions

The runtime user-agent proves the client/opaque-version form, and the token must agree with thread
`cliVersion`. `model` is the normalized model key; descriptions and effort descriptions are retained.
Reasoning effort travels through app-server session config and turn parameters. A roleless pre-L4
open derives both defaults from the authenticated catalog, never ambient role-spawn environment.

### Invariants And Boundaries

- `model/list` pagination includes hidden rows, rejects repeated cursors, and fails on the configured
  page bound rather than returning a partial catalog.
- Cold discovery never starts/resumes a thread or sends a turn.
- Start/resume preserves exact thread, model, cwd, sandbox, approval, config, and effective effort.
- Missing, conflicting, or unadvertised effort fails loudly; no global effort enum is accepted.
- `config.model` and `config.model_reasoning_effort` must agree with the dynamically selected pair;
  the session never accepts a second configuration authority.
- Failed connect/discover always stops its transient transport.

### Todos

L3 adds same-thread switching while preserving this initial thread configuration and evidence.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Strict model-page parsing is isolated from session lifecycle, while the adapter consumes retained
catalog and thread evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Model pages validate descriptions, per-model effort menus/defaults, visibility, and identity. | L142-L240 | [codex_app_server_state.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_state.py) |
| Adapter launch knobs supply the owned model/effort session config and later turns reuse the resolved effort. | L88-L146; L259-L280 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| The factory deliberately leaves a roleless Codex selection empty so this session resolves catalog defaults. | L22-L56 | [harness_control_factories.py](agents-remember/mcp/src/agents_remember/serving/harness_control_factories.py) |

## Cross-Repo References

No external repository boundary is implemented by this session owner.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented settings-selected and roleless
  catalog-default resolution, native thread config for model/effort, duplicate config refusal, and
  retention of the resolved desired effort for later turns.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented full retained model metadata,
  include-hidden pagination, no-thread discovery, cached advertise, and fail-clean transport
  ownership.
- 2026-07-14T17:00:00+02:00 — 260713-PHA-L6 master-exit correction: replaced the exact-0.144.3
  convention with consumed initialize/thread identity and field validation; fixture pins are
  historical evidence only.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented cross-message Codex capability negotiation and
  loud failure for inconsistent structured identity.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for exact initialize,
  model/effort discovery, thread start/resume, and preserved settings. Verification remains unset
  until closeout stamps the code commit.
