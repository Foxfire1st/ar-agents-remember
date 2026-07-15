# mcp/src/agents_remember/serving/codex_app_server_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T23:00+02:00 |
| lastVerifiedCommitHash | `5fa7026c644edfb4eb884173b64d31c9a14a6585` |
| lastVerifiedCommitDate | 2026-07-15T23:33:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Adapts one native Codex app-server session and JSON-RPC transport to the normalized hosted adapter
contract, including cached model/effort advertisement, transient token-free catalog discovery, and
settings-resolved initial model/effort carried through native app-server thread configuration.

## Code Commentary

### Logic

The adapter delegates initialize/model discovery/thread ownership to `CodexAppServerSession`, then
submits correlated turns, applies explicit steer or bounded-queue busy policy, reduces status/turn/
item/server-request events, resolves approvals and elicitation, and reconnects through the exact
thread. `launch_knobs` validates a complete selection, places `model` and
`model_reasoning_effort` in app-server session config, and declares every adapter-owned model/config
selector so free-form argv conflicts can be refused before discovery. `discover` initializes and
lists models without starting a thread; `advertise` returns the catalog retained by the running
session. Turns and settings-update validation reuse the session's resolved desired effort, keeping
roleless dynamic defaults and settings-selected launches on the same thread-owned value.

### Conventions

Acceptance is proven by correlated `turn/start`/`turn/steer` responses. Running advertise is a
synchronous no-RPC read. Initial model/effort belongs to `thread/start`/`thread/resume` config; this
native adapter never uses the codex-acp-only `CODEX_CONFIG` environment path. Adapter identity
reports `codex-app-server:<opaque negotiated version>`; exact package values remain fixture/smoke
evidence only.

### Invariants And Boundaries

- Cold discovery performs initialize plus paginated `model/list` only: no thread and no turn.
- Running advertise uses the catalog fetched for that same connected session; it does not refetch,
  hardcode, or silently filter the selected model's effort choices.
- Adapter-owned `--model`/`-m` and `model`/`model_reasoning_effort` config selectors cannot compete
  with the normalized launch selection; the runner preflights all accepted spellings.
- The effort used for later turns and settings-update validation is the exact effort resolved while
  opening the thread, including a model-local dynamic default for a roleless pre-L4 session.
- Protocol readiness and acceptance are authoritative; pane, terminal, log, ACP transport, and Toad
  hosting are not used.
- No blind resend follows an ambiguous send; retention remains bounded.
- Completion metadata does not consume durable inbox state, and queued state requires an actual
  replacement.

### Todos

L3 adds honest same-thread model/effort mutation on top of this initial launch channel.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Session ownership and strict model-page parsing remain dedicated modules rather than adapter-local
policy.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Session connect resolves the selected model and model-local effort, while discover stops before thread creation. | L106-L195 | [codex_app_server_session.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_session.py) |
| Thread parameters persist model and effort in app-server config and reject conflicting values. | L295-L337 | [codex_app_server_session.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_session.py) |
| The launch boundary refuses duplicate adapter-owned argv/config selectors before discovery. | L149-L226 | [harness_launch.py](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) |
| Model pages preserve display/description metadata and model-local reasoning effort options. | L142-L213 | [codex_app_server_state.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_state.py) |

## Cross-Repo References

No external repository boundary is implemented by this adapter; prior task-review artifacts are not
runtime boundary contracts.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented native thread config launch knobs,
  adapter-owned selector refusal, roleless model-local defaults, and reuse of the resolved effort
  for subsequent turns and settings-update evidence.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented harness-id validation,
  initialize/list-only discovery, and cached same-session advertise while preserving correlated
  delivery, boundedness, and inbox-consumption boundaries.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: documented null-requestId/vendor-correlation completion,
  loud correlation validation, terminal idle/immediate projection, and replacement-only queued state.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented structured Codex identity and negotiated adapter
  reporting; exact versions remain fixture/smoke baselines only.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for normalized Codex
  lifecycle, correlated acceptance, busy policy, approvals, reconnect, and no-cutover boundary.
  Verification remains unset until closeout stamps the code commit.
