# mcp/src/agents_remember/serving/pi_rpc_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Composes Pi's native RPC process/protocol/event seams into the normalized hosted adapter, including
provider-qualified native model/thinking launch flags, echo-verified startup, live capability
advertisement, bounded catalog-coherent mid-session mutation, transient prompt-free discovery,
session delivery, interactions, reconnect, and durable no-resend reconciliation. 260718-CHATS-L0E
adds a `get_entries`-backed native history page with typed entry identity. 260718-CHATS-L2E
implements the structural `InterruptCapableAdapter`/`AssetSubmitCapable` seams: an RPC `abort`
guarded pre-write by the caller's expected active-operation identity with replay-once, and
verified base64 image content on the prompt command.

## Code Commentary

### Logic

`launch_knobs` emits `--model <provider/id> --thinking <level>` while `pi_rpc_launch` adds
protocol-owned `--mode rpc`. Startup reads state/catalog and verifies configured echoes as before.
`set_model` and `set_effort` delegate to `PiRpcConfiguration`, which serializes mutation response,
candidate `get_state`, and refreshed `get_available_models` under one finite deadline. The adapter's
configuration readers deliberately do not publish candidate state; `_commit_configuration` replaces
state and catalog together only after correlation, requested postcondition, and catalog coherence
pass. Thus an incoherent model, clamp token, disappearing row, timeout, or lost readback leaves the
previous advertised snapshot callable. Existing prompt delivery, settlement, interactions,
reconnect, and post-cursor reconciliation remain intact.

L0E's `read_native_page` implements the structural native-page protocol over the durable entry
read: `get_entries(since=cursor)` performs the continuation natively, each entry is flattened with
its typed `(id, parentId, type)` identity and honest optional timestamp, and a repeated entry id
fails closed rather than silently overlapping or skipping across pages. The shared window helper
bounds the fresh read (called with `cursor=None`, since the native branch already applied the
cursor), so `nextCursor` is always minted from the current native branch.

L2E's `interrupt` writes one native RPC `abort` guarded pre-write by AR operation identity: pi
has no turn identity, so a caller `turn_id` is refused typed, a missing active operation fails
typed, and a caller `expected_operation_id` unequal to the current `active_operation.operation_id`
fails typed before any native bytes — a stale reconcile can never abort a successor operation.
The acknowledgement replays once per (expected, active) pair with no second write, and a native
failure crosses as a `rejected` acknowledgement; settlement still flows through the normal settle
path (the abort is asynchronous in effect). `submit_with_assets` pre-verifies staged bytes before
any native write — a verification failure returns a clean `rejected` receipt with zero prompt
commands — and `_image_content` attaches verified base64 `images[]` content
(`{type:"image", mimeType, data}`) to the prompt command, re-verifying sha256/size at
construction. Receipt raw gains additive `assetIds` only when assets ride.

### Conventions

Internal request ids are monotonically generated per adapter. Model keys are exact
provider-qualified `provider/id` values; bare ids are not aliases. Setter timeout is configurable
and positive, with five seconds as the production default. Running advertise is synchronous and
no-RPC; discovery is asynchronous because it owns a transient Pi process.

### Invariants And Boundaries

- The current `get_state` model must exist in `get_available_models`, and its thinking level must
  belong to that model's own menu; contradictions fail loudly.
- A configured launch must use the exact provider-qualified catalog key and must echo both model
  and thinking after startup, countering Pi's native silent thinking clamp.
- Mid-session effort admission uses only the selected model's dynamic effort menu, never a catalog
  union or hardcoded token list.
- A successful mutation is `echo-verified` only after response, state readback, refreshed catalog,
  and atomic commit agree. A coherent clamp keeps requested/effective values distinct; incoherent
  readback is `unknown` and is not published.
- Mutation/readback timeout is bounded and releases the shared control queue for later work.
- Discovery sends no prompt and does not read durable entries.
- Failed startup/discovery cannot leak a subprocess or leave the instance half-started.
- `get_state` governs readiness/activity and corroborates settlement; reconnect preserves exact
  session identity.
- Ambiguous submissions remain unresolved without durable post-cursor evidence and are never resent.
- Native entry paging requires exact per-entry identity: an entry without id/type fails parsing and
  a duplicate id fails closed; timestamps are reported only when the entry schema carries them.
- No pane/log fallback, ACP transport, Toad host, or composer-paste capability change is present.
- The abort write is guarded pre-write by the caller's expected active-operation identity —
  mismatch, no-active, or any `turn_id` fails typed before native bytes — and replays once per
  (expected, active) pair, so a stale reconcile writes nothing into a successor operation.
- Asset bytes are re-verified (sha256/size) at construction before base64 image content crosses;
  a verification failure is a clean `rejected` receipt with zero prompt commands.

### Todos

None known for the L3 Pi configuration seam.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Protocol helpers own launch transformation, state sanitization, catalog mapping, and thinking-level
rules; process/event modules remain transport and event boundaries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Configuration owns the finite locked mutation/readback/catalog transaction, exact provider split, selected-model effort gate, clamp evidence, and atomic commit decision. | L29-L193; L196-L202 | [pi_rpc_configuration.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_configuration.py) |
| Pi protocol parsing provides RPC launch validation, safe state identity, and provider-qualified model-local effort menus. | L114-L130; L176-L234; L383-L427 | [pi_rpc_protocol.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_protocol.py) |
| The launch validator requires exact Pi catalog keys and model-local launch effort before the configured process starts. | L78-L119 | [harness_launch.py](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) |
| The subprocess boundary correlates requests, reclaims cancellation state, and ignores valid late responses without tombstones. | L28-L98; L177-L199 | [pi_rpc_process.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_process.py) |
| The event mapper owns normalized state, settlement, and extension interaction projections. | L41-L170 | [pi_rpc_events.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_events.py) |
| Entry identity/timestamp helpers keep native paging coordinates honest. | L264-L288 | [pi_rpc_protocol.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_protocol.py) |
| Contract tests pin the entries native page, message_update/message_end evidence forwarding, and the installed 0.80.7 production-seam capture. | L1033-L1179 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |
| The content-less `message_end` evidence mapping that keeps a real abort from failing the bridge. | L226-L244 | [pi_rpc_events.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_events.py) |
| The control-plane contract suite pins the guarded abort, replay-once per pair, the successor stale-reconcile typed refusal with zero writes, and the image content construction. | L641-L752; L1336-L1395 | [test_harness_control_plane.py](agents-remember/mcp/tests/test_harness_control_plane.py) |
| The installed-runtime suite captures the live 0.80.7 abort, timeline, and asset evidence behind the fixture rows. | L262-L364 | [test_harness_control_plane_installed.py](agents-remember/mcp/tests/test_harness_control_plane_installed.py) |
| The fixture records the redacted `control-plane/*` observed rows this adapter produced through the production seam. | — | [pi-0.80.7.json](agents-remember/mcp/tests/fixtures/conversation_runtime/pi-0.80.7.json) |

## Cross-Repo References

No external repository boundary is implemented by this adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

Pi is dispatch-now under the shared authority and never sends `streamingBehavior` steer/follow-up.
Fresh state preflight plus generation/activity/event tokens guard prompt and setter writes; the exact
operation is bound before bytes. Completion requires settled plus fresh idle. Unknown remains the
active barrier until exact resolution, so native queue state never becomes a second authority.

## 260731-EFA-L2 Current Delta

**`PiAdapterLimits`** (`submission=256`, `interaction=64`, `configuration_timeout_seconds`; module
default `DEFAULT_PI_ADAPTER_LIMITS`) replaces the three loose bounds: how much one Pi adapter may
retain, and how long a set transaction may take. The retained submission and interaction ledgers
plus the mutation timeout are **one bounded budget** for a single live Pi session — raising one
alone just moves where the session first misbehaves under load. The default values are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the `pi_rpc_configuration.py` citation
  (2 ranges), verified by reading the 220-line file end to end. Now L29-L193 — the finite
  `DEFAULT_PI_MUTATION_TIMEOUT_SECONDS` bound at L29, the six-port `ConfigurationPorts` at L32-L47,
  the `asyncio.Lock` taken by both setters at L80/L126, the selected-model effort vocabulary gate at
  L106-L124, the clamp-evidence detail at L143-L146, the two `self._commit` atomic-commit decisions
  at L96 and L142, and `_transaction`'s bounded mutation/readback/catalog body at L155-L193 — plus
  L196-L202 for `_provider_model`, the exact `provider/model-id` split. Claim unchanged.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `PiAdapterLimits` / `DEFAULT_PI_ADAPTER_LIMITS` as the single per-session budget (defaults unchanged).
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the `InterruptCapableAdapter`
  implementation (RPC `abort` guarded pre-write by the expected active-operation identity,
  `turn_id` refused typed, replay-once per pair, native failure → `rejected` acknowledgement) and
  the `AssetSubmitCapable` implementation (verified base64 `images[]` content on the prompt
  command, construction-time re-verification, additive receipt `assetIds`). Verification metadata
  stays pinned until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the `get_entries(since)`-backed
  `read_native_page` — native cursor continuation, typed entry id/parentId/type identity,
  duplicate-id fail-closed, honest optional timestamps, and window minting from the current native
  branch. Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: documented no-native-queue dispatch, fresh-state/token guards,
  exact binding, and settled-plus-idle completion.

- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented the bounded serialized Pi
  mutation/readback/catalog transaction, candidate-state isolation, atomic coherent commit,
  selected-model effort gating, honest clamp evidence, and queue-releasing timeout behavior.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented exact provider-qualified
  `--model`, native `--thinking`, protocol-owned RPC mode, and post-start model/thinking echo
  verification that exposes rather than trusts Pi's clamp behavior.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented state/catalog/entry startup order,
  state-plus-catalog-only discovery, cached current-selection validation, provider-qualified models,
  and fail-clean retry semantics.
- 2026-07-14T17:00:00+02:00 — 260713-PHA-L6 master-exit correction: made the version-neutral
  structured Pi contract normative and retained 0.80.6 only as fixture/smoke evidence.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented version-free Pi production startup and retained
  `0.80.6` only as fixture/smoke evidence.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for L1-backed handshake,
  queue behavior, settlement, extension UI, reconnect, cursor reconciliation, and no-resend policy.
