# mcp/src/agents_remember/serving/pi_rpc_adapter.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

Protocol helpers own launch transformation, state sanitization, catalog mapping, and thinking-level
rules; process/event modules remain transport and event boundaries.

- Configuration owns the finite locked mutation/readback/catalog transaction, exact provider split, selected-model effort gate, clamp evidence, and atomic commit decision. [1]
- Pi protocol parsing provides RPC launch validation, safe state identity, and provider-qualified model-local effort menus. [2]
- The launch validator requires exact Pi catalog keys and model-local launch effort before the configured process starts. [3]
- The subprocess boundary correlates requests, reclaims cancellation state, and ignores valid late responses without tombstones. [4]
- The event mapper owns normalized state, settlement, and extension interaction projections. [5]
- Entry identity/timestamp helpers keep native paging coordinates honest. [6]

| The content-less `message_end` evidence mapping that keeps a real abort from failing the bridge. | ["pi:message_end"] | mcp/src/agents_remember/serving/pi_rpc_events.py:260-260 |

| Historical evidence (retired with the d3610903 suite reduction): The installed-runtime suite captures the live 0.80.7 abort, timeline, and asset evidence behind the fixture rows. These removed artifacts provide no current execution or capability-enablement proof. | N/A | N/A |
| Historical evidence (retired with the d3610903 suite reduction): The fixture recorded the redacted `control-plane/*` observed rows this adapter produced through the production seam. These removed artifacts provide no current execution or capability-enablement proof. | N/A | N/A |

### Cross-Repo References

No external repository boundary is implemented by this adapter.

No meaningful cross-repo references found.

## 260715-FEUI-L5 Submission Authority Delta

Pi is dispatch-now under the shared authority and never sends `streamingBehavior` steer/follow-up.
Fresh state preflight plus generation/activity/event tokens guard prompt and setter writes; the exact
operation is bound before bytes. Completion requires settled plus fresh idle. Unknown remains the
active blocker until exact resolution, so native queue state never becomes a second authority.

## 260731-EFA-L2 Current Delta

**`PiAdapterLimits`** (`submission=256`, `interaction=64`, `configuration_timeout_seconds`; module
default `DEFAULT_PI_ADAPTER_LIMITS`) replaces the three loose bounds: how much one Pi adapter may
retain, and how long a set transaction may take. The retained submission and interaction ledgers
plus the mutation timeout are **one bounded budget** for a single live Pi session — raising one
alone just moves where the session first misbehaves under load. The default values are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
