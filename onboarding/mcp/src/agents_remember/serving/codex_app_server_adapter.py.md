# mcp/src/agents_remember/serving/codex_app_server_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa` |
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Adapts one native Codex app-server session and JSON-RPC transport to the normalized hosted adapter
contract, including cached model/effort advertisement and transient token-free catalog discovery.

## Code Commentary

### Logic

The adapter delegates initialize/model discovery/thread ownership to `CodexAppServerSession`, then
submits correlated turns, applies explicit steer or bounded-queue busy policy, reduces status/turn/
item/server-request events, resolves approvals and elicitation, and reconnects through the exact
thread. `discover` validates the Codex harness id and asks a transient session to initialize and list
models without starting a thread. `advertise` requires ready state and returns the catalog retained
by the running session. Existing terminal completion, transcript, interaction, and bounded
submission-evidence behavior remains unchanged.

### Conventions

Acceptance is proven by correlated `turn/start`/`turn/steer` responses. Running advertise is a
synchronous no-RPC read. Adapter identity reports `codex-app-server:<opaque negotiated version>`;
exact package values remain fixture/smoke evidence only.

### Invariants And Boundaries

- Cold discovery performs initialize plus paginated `model/list` only: no thread and no turn.
- Running advertise uses the catalog fetched for that same connected session; it does not refetch,
  hardcode, or silently filter the selected model's effort choices.
- Protocol readiness and acceptance are authoritative; pane, terminal, log, ACP transport, and Toad
  hosting are not used.
- No blind resend follows an ambiguous send; retention remains bounded.
- Completion metadata does not consume durable inbox state, and queued state requires an actual
  replacement.

### Todos

L2 and L3 add settings-owned initial overrides and honest per-turn model/effort mutation.

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
| Session connect retains all model pages and current effort, while discover stops before thread creation. | L100-L239 | [codex_app_server_session.py](codex_app_server_session.py) |
| Model pages preserve display/description metadata and model-local reasoning effort options. | L142-L213 | [codex_app_server_state.py](codex_app_server_state.py) |

## Cross-Repo References

No external repository boundary is implemented by this adapter; prior task-review artifacts are not
runtime boundary contracts.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
