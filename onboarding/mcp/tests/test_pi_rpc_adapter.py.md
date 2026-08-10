# mcp/tests/test_pi_rpc_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pi_rpc_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fake-transport and protocol conformance coverage for the native Pi RPC adapter, including dynamic
installed/authenticated model advertisement, bounded model/thinking mutation with correlated
readback, model-gated thinking levels, launch preservation, session behavior, reconnect
reconciliation, and strict transport framing.

## Code Commentary

### Logic

Protocol tests pin LF-only JSON framing, malformed/overlong refusal, native launch preservation, and
the fixture-owned RPC surface. Async adapter tests cover handshake/state, source-specific busy
queueing, retry/compaction/settlement, extension UI, disconnect before/after acknowledgement,
session-identity reconnect, cursor reconciliation without resend, and loud malformed transport
failure.

ACPUI-L1 extends the fake transport with a native `get_available_models` catalog and a full
`get_state.model` containing a deliberately secret-shaped header. Parser tests prove provider-
qualified model identities, duplicate bare model ids across providers, per-model thinking menus,
the non-reasoning `off` boundary, empty authenticated catalogs, and loud malformed thinking maps.
Discovery calls only `get_state` and `get_available_models`, sends no prompt, skips entry history,
and always stops its transient RPC process. Failed startup/discovery catalog validation stops the
process and resets adapter state so a later start can succeed. Started advertisement retains the
selected model and thinking level, while normalized handshake state strips provider headers.

ACPUI-L3 extends the fake transport with real-shaped `set_model` and `set_thinking_level` responses,
vendor failures, silent thinking clamps, controllable hangs, and post-mutation catalog changes.
Setter tests prove that model keys split only once into the exact `provider/model-id` pair, unknown
models surface the vendor `Model not found` error as `unsupported`, and malformed unqualified keys
cause no write. Thinking values come only from the selected model's dynamic menu. Pi's silent clamp
is reported as `echo-verified` with different requested and effective values after correlated
`get_state` plus refreshed `get_available_models`; no notification is treated as acceptance.

One finite configurable budget covers the mutation response, state readback, and catalog refresh.
Hanging at any of those three stages returns `unknown` without an effective value, and an unresolved
mutation retains the authority barrier rather than allowing a later set to pass behind it. State or
refreshed-catalog evidence that reports an unadvertised clamp/model is incoherent: the result remains
`unknown`, the prior coherent capability snapshot stays advertised, and no false promotion occurs.
Switching to a non-reasoning model also re-gates thinking to `off` so an old model's effort token is
immediately unsupported.

### Conventions

The module uses `unittest` with deterministic request ids, fixed clocks, provider-qualified fixture
models, and a transport sequence for retry/reconnect ownership. The capability recording remains
protocol evidence only; runtime catalogs come from the fake native request in these tests.

### The Capability Recording Guard (260731-EFA-L2)

`test_capability_fixture_documents_the_smoke_baseline` is the **offline** half of the
capability anti-drift contract. It imports `PI_RPC_VERSION` from `test_pi_rpc_real_smoke.py`
and reads `FIXTURES / f"{PI_RPC_VERSION}-capabilities.json"` — never a literal filename —
then asserts:

- `fixture["package"] == PI_RPC_PACKAGE` and `fixture["version"] == PI_RPC_VERSION`;
- the recorded `dialogMethods` / `fireAndForgetMethods` equal the adapter's
  `PI_RPC_DIALOG_METHODS` / `PI_RPC_FIRE_AND_FORGET_METHODS`;
- `sorted(FIXTURES.glob("*-capabilities.json"))` is **exactly** the one file for the pinned
  version, because "a second capability recording leaves no rule about which one is
  authoritative".

Why this test and not the smoke test: re-recording lives behind
`@pytest.mark.ar_run_pi_rpc_smoke`, which needs npm and a network and can stay unrun. This
one runs in the ordinary suite, so bumping the pin without re-recording fails immediately
with `FileNotFoundError` on the version-addressed path. Keeping the superseded recording
beside the new one also fails here. The 0.80.6 file was therefore renamed to 0.80.7, not
copied.

### Invariants And Boundaries

- Enumeration is token-free and uses only Pi RPC `get_state` plus `get_available_models`; no prompt
  or composer paste is allowed.
- Model identity is `provider/id`, and effort/thinking options remain nested under each model.
- Full provider model objects may contain credential-bearing headers; normalized state retains only
  safe identity fields and must not expose headers.
- Catalog/state disagreement and malformed thinking maps fail loudly; failed transient or started
  processes are stopped rather than leaked.
- Setter acceptance requires a correlated success response, `get_state`, and catalog-coherent
  readback; events alone never prove the effect.
- Thinking clamps remain `echo-verified` only when the effective value is present in the selected
  model's refreshed dynamic menu; requested and effective values remain distinct.
- Mutation, state readback, and catalog refresh share one finite transaction budget. Timeout or
  incoherent evidence returns `unknown` without promotion; an unresolved mutation holds the
  authority barrier until explicitly resolved.
- Model identity remains exact `provider/model-id`, including model ids containing `/`; malformed or
  vendor-unknown values are unsupported rather than guessed.
- `pi_rpc_launch` adds only `--mode rpc`, preserves existing model/thinking flags and environment,
  and rejects the wrong harness id or a conflicting mode.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

The test module and native Pi modules directly prove catalog parsing, process ownership, and safe
normalized advertisement.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fake transport supplies reasoning/non-reasoning models, returns them from `get_available_models`, places a secret-shaped header in state, and emulates mutation responses, clamps, hangs, and catalog drift. | `_FakePiTransport` | mcp/tests/test_pi_rpc_adapter.py:47-292 |
| `pi_rpc_launch` preserves the launch while adding RPC mode without changing other argv, cwd, settings, or environment. | `pi_rpc_launch` | mcp/src/agents_remember/serving/pi_rpc_protocol.py:135-151 |
| Adapter startup, transient discovery, cleanup, cached advertisement, and catalog/state validation are owned by the native Pi adapter. | `PiRpcAdapter`; `start`; `discover`; `advertise`; `_current_capabilities` | mcp/src/agents_remember/serving/pi_rpc_adapter.py:94-768 |
| The adapter delegates both setters to one configuration transaction object with a configurable finite timeout. | `PiRpcAdapter`; `set_model`; `set_effort` | mcp/src/agents_remember/serving/pi_rpc_adapter.py:94-768 |
| Configuration validates provider/model identity and the selected model's dynamic effort vocabulary, serializes mutations, and commits only coherent state plus catalog readback. | `set_model`; `set_effort`; `_provider_model` | mcp/src/agents_remember/serving/pi_rpc_configuration.py:70-103; mcp/src/agents_remember/serving/pi_rpc_configuration.py:196-202; mcp/src/agents_remember/serving/pi_rpc_configuration.py:105-153 |
| The whole mutation/readback transaction is bounded; timeout, disconnect, or incoherent catalog evidence returns unknown without an effective value. | `_transaction` | mcp/src/agents_remember/serving/pi_rpc_configuration.py:155-193 |

## Cross-Repo References

No sibling repository or external transport implementation is required for these native Pi tests.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260715-FEUI-L5 Submission Authority Delta

Pi tests now cover guarded model/effort readback, timeout/unknown barrier resolution, zero candidate
bytes on stale idle, absence of a native queue/steer flag, activity-token settlement, exact
interaction completion, certified disconnect before dispatch, and no resend after acknowledgement.

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T13:54+02:00 — 260731-EFA-L6 S18-B13 curator: narrowed the launch row to its exact protocol owner and reissued the whole claim for same-reviewer closure.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The row's
  four claims live in `PiRpcConfiguration.set_model` / `set_effort` at
  `pi_rpc_configuration.py` L70-L153 — `_provider_model` identity validation, the selected model's
  `session_settable` effort vocabulary, the `async with self._lock` serialization, and the
  `_commit(state, capabilities)` that runs only after the `get_state` readback agrees — plus the
  `_provider_model` parser itself at L196-L203. The old L27-L131 started in the module imports.
  No claim text changed.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the offline capability-recording
  guard (version-addressed path, exactly-one-recording assertion, dialog/fire-and-forget
  agreement) and removed the stale `0.80.6` fixture reference from Conventions. Metadata
  fields left at their FEUI-L5 verification pins; the rest of this card was re-read against
  the file and remains true. Closeout stamps the code commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: corrected timeout-release assumptions and added fresh-state,
  token, no-native-queue, certificate, and exact-settlement proof.

- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented exact provider/model mutation,
  vendor-error mapping, model-gated exact/clamped thinking readback, one finite mutation/readback
  budget, queue release, and catalog-coherent no-promotion behavior. Verification metadata remains
  pinned until closeout stamps the L3 code commit.
- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented provider-qualified dynamic
  catalogs, model-gated thinking, token-free discovery, strict startup/discovery cleanup, retry
  reset, safe state-model sanitization, and preserved native launch flags; corrected the governing
  overview backlink while preserving existing verification metadata.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented version-free Pi startup coverage.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for Pi fake adapter,
  protocol, activity, extension UI, disconnect, and reconciliation coverage.
