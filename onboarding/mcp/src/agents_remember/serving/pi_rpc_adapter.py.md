# mcp/src/agents_remember/serving/pi_rpc_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash | `ca9dd05a295ef5f24c479e2231fdcd174b372e04` |
| lastVerifiedCommitDate | 2026-07-19T10:04:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Composes Pi's native RPC process/protocol/event seams into the normalized hosted adapter, including
provider-qualified native model/thinking launch flags, echo-verified startup, live capability
advertisement, bounded catalog-coherent mid-session mutation, transient prompt-free discovery,
session delivery, interactions, reconnect, and durable no-resend reconciliation. 260718-CHATS-L0E
adds a `get_entries`-backed native history page with typed entry identity.

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
| Configuration owns the finite locked mutation/readback/catalog transaction, exact provider split, selected-model effort gate, clamp evidence, and atomic commit decision. | L24-L167; L170-L194 | [pi_rpc_configuration.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_configuration.py) |
| Pi protocol parsing provides RPC launch validation, safe state identity, and provider-qualified model-local effort menus. | L114-L130; L176-L234; L383-L427 | [pi_rpc_protocol.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_protocol.py) |
| The launch validator requires exact Pi catalog keys and model-local launch effort before the configured process starts. | L78-L119 | [harness_launch.py](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) |
| The subprocess boundary correlates requests, reclaims cancellation state, and ignores valid late responses without tombstones. | L28-L98; L177-L199 | [pi_rpc_process.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_process.py) |
| The event mapper owns normalized state, settlement, and extension interaction projections. | L41-L170 | [pi_rpc_events.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_events.py) |
| Entry identity/timestamp helpers keep native paging coordinates honest. | L264-L288 | [pi_rpc_protocol.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_protocol.py) |
| Contract tests pin the entries native page, message_update/message_end evidence forwarding, and the installed 0.80.7 production-seam capture. | L1033-L1179 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |

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

## Update History

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
