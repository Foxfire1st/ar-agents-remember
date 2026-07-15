# mcp/src/agents_remember/serving/codex_app_server_session.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_session.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa` |
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns Codex app-server initialization, complete paginated model discovery, selected model/effort
evidence, thread start/resume, the retained running catalog, and a separate thread-free discovery
path.

## Code Commentary

### Logic

`connect` starts transport, initializes the app-server, reads every `model/list` page including
hidden models, selects the configured/default model, validates its advertised reasoning effort, and
starts or resumes the exact thread. It validates echoed thread identity, CLI version, model, cwd, and
effective effort before retaining the selected model plus full catalog. `discover` performs only
transport start, initialize, and the same paginated model read, then returns a normalized snapshot
with no current selection and always stops transport. `advertise` normalizes the retained running
catalog and current evidence without another RPC.

### Conventions

The runtime user-agent proves the client/opaque-version form, and the token must agree with thread
`cliVersion`. `model` is the normalized model key; descriptions and effort descriptions are retained.
Reasoning effort travels through session config and turn parameters rather than an invented argv map.

### Invariants And Boundaries

- `model/list` pagination includes hidden rows, rejects repeated cursors, and fails on the configured
  page bound rather than returning a partial catalog.
- Cold discovery never starts/resumes a thread or sends a turn.
- Start/resume preserves exact thread, model, cwd, sandbox, approval, config, and effective effort.
- Missing, conflicting, or unadvertised effort fails loudly; no global effort enum is accepted.
- Failed connect/discover always stops its transient transport.

### Todos

L2/L3 extend how selected model/effort are applied; the L1 catalog and thread boundary is complete.

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
| Model pages validate descriptions, per-model effort menus/defaults, visibility, and identity. | L142-L240 | [codex_app_server_state.py](codex_app_server_state.py) |
| Adapter start, discover, and advertise consume this session boundary. | L88-L127 | [codex_app_server_adapter.py](codex_app_server_adapter.py) |

## Cross-Repo References

No external repository boundary is implemented by this session owner.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
