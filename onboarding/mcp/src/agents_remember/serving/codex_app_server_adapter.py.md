# mcp/src/agents_remember/serving/codex_app_server_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `38c3fd81bdf851dce96e9b2b14e2bff741e7b383` |
| lastVerifiedCommitDate | 2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Adapts one native Codex app-server session and JSON-RPC transport to the normalized hosted adapter
contract, including cached model/effort advertisement, transient token-free catalog discovery,
settings-resolved initial configuration, and ordered same-thread model/effort switching.
260718-CHATS-L0E stops the adapter dropping native frames: full notification/item/usage params now
ride the reserved `arEvidence` key into the bridge's evidence buffer, and a `thread/read`-backed
native history page exposes persisted threads. 260718-CHATS-L2E implements the structural
`InterruptCapableAdapter`/`AssetSubmitCapable` seams: a native `turn/interrupt` write against the
exact active turn with replay-once, and verified `localImage` asset construction on `turn/start`.
260718-CHATS-L5F R1 additionally carries each notification's native method under the reserved
`AR_EVIDENCE_METHOD_KEY` so the codex projector recognizes the 0.144.5 startup burst instead of
re-guessing it from params shape and flooding one unknown-vendor row per MCP server.

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
shape; the bridge diverts the payload so no projection changes. 260718-CHATS-L5F R1 additionally
sets `AR_EVIDENCE_METHOD_KEY: method` on the `codex-notification` emit (L598-L601) and on the
`item/completed` evidence emit (L667-L670), so the notification's native method reaches the
projector as typed evidence rather than being stripped with the trimmed event; the bridge preserves
it onto `EvidenceFrame.native_method` and strips the reserved key, keeping the redacted snapshot
byte-identical. `codexMethod` still rides for diagnostics; the method-carry key is the discriminator
the projector reads. `read_native_page` implements the
structural native-page protocol over `thread/read` with `includeTurns`: it reconnects a disconnected
session, requires the echoed thread id to match the adapter's own, flattens items through
`native_evidence_frames_from_thread`, and windows them with an opaque cursor; native window errors
raise as typed `CodexAppServerError`, and ephemeral threads' native `includeTurns` refusal crosses
typed with the native reason rather than a guessed page. Reconcile, submission, and interaction
behavior is byte-preserved.

L2E's `interrupt` writes one native `turn/interrupt(threadId, turnId)` against the exact active
turn: a missing active turn or a caller `turn_id` mismatching it fails typed before any write
(`expected_operation_id` is result evidence, never a guard input — the codex guard is the native
turn identity), and the write parameters use the captured active id so a completion interleaving
can never redirect the write into a successor turn. The acknowledgement is replayed once per
(turn_id-or-active, active) pair with no second native write, and an RPC failure crosses as a
`rejected` acknowledgement; the bridge stamps the epoch. `submit_with_assets` pre-verifies every
staged asset before any native write — a verification failure returns a clean `rejected` receipt
with zero `turn/start` requests — and `_turn_input` appends verified `localImage{path}` blocks
after the text block, with sha256/size re-verified at construction (`_verified_asset_path`).
Receipt raw gains additive `assetIds` only when assets ride.

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
- The native notification method rides the reserved `AR_EVIDENCE_METHOD_KEY` beside the `arEvidence`
  payload (R1); the adapter only emits it and never reads or merges it — the bridge alone diverts it
  onto the frame and strips it from the republished event.
- Native pages are for persisted threads: a native refusal (e.g. ephemeral `includeTurns`) crosses
  typed with its reason instead of being retried into a less truthful shape.
- The interrupt write targets only the exact active turn (native `turnId` guard, no-active typed)
  and replays once per (expected, active) pair; it never settles the operation — settlement stays
  with the landed completion path, and a post-settlement interrupt fails typed.
- Asset bytes are re-verified (sha256/size) at construction before the native process sees a
  `localImage` path; a verification failure is a clean `rejected` receipt with zero native writes,
  and unknown/unverified native shapes are never guessed.

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
| The structural sub-protocols this adapter implements; the caller's identity guards ride the write. | L92-L115 | [harness_control_adapter.py](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) |
| The control-plane contract suite pins the interrupt write/replay/turnId guard/no-active typed refusal and the `localImage` construction with zero-write rejection. | L454-L522; L1270-L1335 | [test_harness_control_plane.py](agents-remember/mcp/tests/test_harness_control_plane.py) |
| The installed-runtime suite captures the live 0.144.5 interrupt, timeline, asset, and withdrawal-recovery evidence behind the fixture rows. | L126-L261 | [test_harness_control_plane_installed.py](agents-remember/mcp/tests/test_harness_control_plane_installed.py) |
| The fixture records the redacted `control-plane/*` observed rows this adapter produced through the production seam. | — | [codex-0.144.5.json](agents-remember/mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json) |

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

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R1 — documented the native-method carry: the
  `codex-notification` (L598-L601) and `item/completed` (L667-L670) emits now set
  `AR_EVIDENCE_METHOD_KEY: method` so the codex projector recognizes the 0.144.5 startup burst by
  method instead of re-guessing from params shape; added the emit-only invariant. Verification
  metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the `InterruptCapableAdapter`
  implementation (native `turn/interrupt` on the exact active turn, no-active/mismatch typed,
  replay-once per pair, RPC failure → `rejected` acknowledgement) and the `AssetSubmitCapable`
  implementation (pre-verified `localImage{path}` blocks on `turn/start`, construction-time
  sha256 re-verification, additive receipt `assetIds`, zero native writes on verification
  failure). Verification metadata stays pinned until closeout stamps the candidate commit.
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
