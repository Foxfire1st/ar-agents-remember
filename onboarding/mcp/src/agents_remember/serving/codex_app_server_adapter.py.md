# mcp/src/agents_remember/serving/codex_app_server_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T17:18:47+02:00 |
| lastVerifiedCommitHash | `8fc3ecb0cb22da53ba639ad37dee37ce0e8d7c9b`|
| lastVerifiedCommitDate | 2026-07-14T17:24:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Adapts the Codex app-server session and JSON-RPC transport to the normalized hosted harness adapter
contract.

## Code Commentary

The adapter starts and snapshots the session, submits correlated turns, applies explicit steer or
bounded-queue busy policy, reduces status/turn/item/server-request events, resolves approvals and
elicitation, and reconnects by reading the exact thread and reconciling evidence. It publishes
normalized activity, terminal results, transcript entries, capability details, and interaction state.
For a terminal completion with null protocol `requestId`, it resolves the protocol-owned vendor
correlation against exactly one accepted inbox row in the same hosted session and records completion
on that row. Production uses the consumed structured capabilities/messages/fields; exact 2.1.207,
0.144.3, and 0.80.6 values are fixture/smoke evidence only.

## Conventions

Acceptance is proven by correlated `turn/start`/`turn/steer` responses. Null-requestId completion
requires a present, text, exact, same-session vendor correlation; missing, non-text, unmatched, or
ambiguous evidence fails loudly. Reconnect records `resend: false`; event and submission retention
are bounded.

## Invariants And Boundaries

- Protocol readiness and acceptance are authoritative; pane, terminal, or log text is not used.
- No blind resend follows an ambiguous send.
- Completion writes adapter delivery metadata on the matched row without consuming its explicit
  inbox state; a completed turn with no actual queued replacement reports `idle` / `immediate`.
  `settling` / `queued` is reserved for an actual replacement turn.
- R9 rolling compatibility permits only optional `adapterDeliveryState` and
  `adapterDeliveryDetail`; unrelated extras remain rejected. R10 resource performance is queued,
  not implemented or current behavior.
- The adapter is leaf-local: no production registration, cutover, credential handling, or vendor
  fallback is owned here.

## Todos

None known for this leaf.

## Docs References

No Domain Documentation entries are configured in the resolved source registry.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Protocol and session responsibilities are split into dedicated modules. | L87-L110 | [codex_app_server_session.py](codex_app_server_session.py) |
| Fake and live tests cover handshake, R11, busy policy, approvals, reconnect, and terminal mapping. | L186-L477 | [test_codex_app_server_adapter.py](../../../../tests/test_codex_app_server_adapter.py) |

## Cross-Repo References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Reviewer PASS confirms stable protocol behavior and no cutover/registration escape. | L5-L15; L25-L32 | [260713-PHA-L3-reviewer-verdict.md](../../../../../../../../../../../../ar-coordination/tasks/agents-remember/260713_protocol-backed-harness-adapters/notes/reports/260713-PHA-L3-reviewer-verdict.md) |

### 260713-PHA-L6 Capability Negotiation

The adapter identity reports `codex-app-server:<negotiated opaque version>` after the structured
session handshake. It does not require an exact installed package version; malformed or missing
initialization, model, thread, policy, or cross-message identity evidence fails loudly.

## Update History
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: documented null-requestId/vendor-correlation completion,
  loud correlation validation, terminal idle/immediate projection, and replacement-only queued state.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented structured Codex identity and negotiated adapter
  reporting; exact versions remain fixture/smoke baselines only.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for normalized Codex
  lifecycle, correlated acceptance, busy policy, approvals, reconnect, and no-cutover boundary.
  Verification remains unset until closeout stamps the code commit.
