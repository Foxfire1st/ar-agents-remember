# mcp/src/agents_remember/serving/codex_app_server_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash | `ca9dd05a295ef5f24c479e2231fdcd174b372e04` |
| lastVerifiedCommitDate | 2026-07-19T10:04:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Adapts one native Codex app-server session and JSON-RPC transport to the normalized hosted adapter
contract, including cached model/effort advertisement, transient token-free catalog discovery,
settings-resolved initial configuration, and ordered same-thread model/effort switching.
260718-CHATS-L0E stops the adapter dropping native frames: full notification/item/usage params now
ride the reserved `arEvidence` key into the bridge's evidence buffer, and a `thread/read`-backed
native history page exposes persisted threads.

## Code Commentary

### Logic

The adapter delegates initialize/model discovery/thread ownership to `CodexAppServerSession`.
Setters mutate only the session's desired selection: an already-effective value is `immediate`,
while a real pending change is `queued` for the next fresh `turn/start` on the existing thread.
Each submitted prompt captures its model/effort selection when reserved, so later setters cannot
rewrite earlier accepted queue work. A pending switch disables steer and queues behind an active
turn. `turn/start` promotes only `inProgress` or `completed`; `failed`/`interrupted` reject the
prompt and retain the prior effective selection plus pending fresh-turn barrier. Matching
`thread/settings/updated` is supplementary evidence, while unrelated drift fails loudly.
Launch-knob ownership, token-free discovery, interactions, events, and bounded reconciliation remain
on their existing native paths.

L0E forwarding places the full `params` of each previously trimmed emit under the reserved
`arEvidence` raw key at six sites — the notification fallback (item/started, deltas, rate-limit and
compaction shapes), `thread/status/changed`, `thread/settings/updated`, `turn/completed`, and both
`item/completed` paths — while every pre-existing raw key (`codexMethod`, `turnId`) keeps its exact
shape; the bridge diverts the payload so no projection changes. `read_native_page` implements the
structural native-page protocol over `thread/read` with `includeTurns`: it reconnects a disconnected
session, requires the echoed thread id to match the adapter's own, flattens items through
`native_evidence_frames_from_thread`, and windows them with an opaque cursor; native window errors
raise as typed `CodexAppServerError`, and ephemeral threads' native `includeTurns` refusal crosses
typed with the native reason rather than a guessed page. Reconcile, submission, and interaction
behavior is byte-preserved.

### Conventions

Acceptance is proven by correlated `turn/start`/`turn/steer` responses. A setter's `queued` result
does not claim an effective value; the fresh turn is the effect boundary. Running advertise is a
synchronous no-RPC read. Initial model/effort belongs to `thread/start`/`thread/resume` config; this
native adapter never uses the codex-acp-only `CODEX_CONFIG` environment path. Adapter identity
reports `codex-app-server:<opaque negotiated version>`.

### Invariants And Boundaries

- Cold discovery performs initialize plus paginated `model/list` only: no thread and no turn.
- Running advertise uses the catalog fetched for that same connected session; it does not refetch,
  hardcode, or silently filter the selected model's effort choices.
- Adapter-owned `--model`/`-m` and `model`/`model_reasoning_effort` config selectors cannot compete
  with the normalized launch selection; the runner preflights all accepted spellings.
- The effort used for later turns and settings-update validation is the exact effort resolved while
  opening the thread, including a model-local dynamic default for a roleless pre-L4 session.
- Model changes rebase an unavailable desired effort to the target row's dynamic default; effort
  remains gated by the desired model's own menu.
- Prompt-before-set and set-before-prompt preserve their captured selection order. No setter
  reconnects or changes the thread id.
- Failed/interrupted fresh turns cannot promote desired settings; reversing desired back to the
  effective pair clears pending/fresh state and returns `immediate`.
- Protocol readiness and acceptance are authoritative; pane, terminal, log, ACP transport, and Toad
  hosting are not used.
- No blind resend follows an ambiguous send; retention remains bounded.
- Completion metadata does not consume durable inbox state, and queued state requires an actual
  replacement.
- Evidence payloads ride only the reserved `arEvidence` key; the adapter never merges that key into
  any projection itself and never mints `bridgeEpoch`.
- Native pages are for persisted threads: a native refusal (e.g. ephemeral `includeTurns`) crosses
  typed with its reason instead of being retried into a less truthful shape.

### Todos

None known for the L3 same-thread mutation seam.

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
| Session keeps desired and effective settings separate, validates dynamic model-local choices, and promotes only accepted selection evidence. | L210-L319 | [codex_app_server_session.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_session.py) |
| Submission evidence captures the exact model/effort pair accepted at reservation time. | L74-L118 | [codex_app_server_state.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_state.py) |
| The transport removes cancelled requests and ignores their syntactically valid late responses without retaining tombstones. | L93-L108; L220-L250 | [codex_app_server_protocol.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_protocol.py) |
| The launch boundary refuses duplicate adapter-owned argv/config selectors before discovery. | L149-L226 | [harness_launch.py](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) |
| Model pages preserve display/description metadata and model-local reasoning effort options. | L142-L213 | [codex_app_server_state.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_state.py) |
| The thread flatten helper enforces unique typed item identity for native paging. | L378-L415 | [codex_app_server_state.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_state.py) |
| Contract tests pin the evidence round-trip, unknown-vendor pass-through, thread/read paging, and the installed 0.144.5 production-seam capture. | L791-L1033 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |

## Cross-Repo References

No external repository boundary is implemented by this adapter; prior task-review artifacts are not
runtime boundary contracts.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

Codex is now dispatch-now under the shared authority: it does not queue or steer an active turn.
Prompt/setter writes are guarded and carry the exact operation ref; native turn ids bind to that ref.
Synchronous or asynchronous terminal events share one once-only completion latch. Live correlations
and terminal dedupe are bounded, removed on completion, and keyed strongly enough that stale events
or turn-id reuse cannot release a successor.

## Update History

- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented stop-dropping `arEvidence`
  forwarding at the six emit sites and the `thread/read`-backed `read_native_page` with thread-id
  echo check, duplicate-id fail-closed, and typed ephemeral `includeTurns` refusal. Verification
  metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: replaced adapter-queue/steer semantics with guarded fresh-turn
  dispatch, exact turn-operation binding, once-only completion, and bounded correlation maps.

- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented desired/pending/effective settings,
  next-fresh-turn application, captured prompt selection epochs, failed-turn non-promotion,
  model-local effort rebasing, reversal collapse, and same-thread/no-reconnect switching.
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
