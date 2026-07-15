# mcp/tests/test_pi_rpc_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pi_rpc_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T01:21+02:00 |
| lastVerifiedCommitHash | `06973f6886276d7b3670c2c1e19cbb76928a7892` |
| lastVerifiedCommitDate | 2026-07-16T01:49:31+02:00|
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
Hanging at any of those three stages returns `unknown` without an effective value and releases the
shared bridge queue for a later successful set. State or refreshed-catalog evidence that reports an
unadvertised clamp/model is incoherent: the result remains `unknown`, the prior coherent capability
snapshot stays advertised, and no false promotion occurs. Switching to a non-reasoning model also
re-gates thinking to `off` so an old model's effort token is immediately unsupported.

### Conventions

The module uses `unittest` with deterministic request ids, fixed clocks, provider-qualified fixture
models, and a transport sequence for retry/reconnect ownership. The pinned `0.80.6` fixture remains
protocol evidence only; runtime catalogs come from the fake native request in these tests.

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
  incoherent evidence returns `unknown` without promotion and must release the control queue.
- Model identity remains exact `provider/model-id`, including model ids containing `/`; malformed or
  vendor-unknown values are unsupported rather than guessed.
- `pi_rpc_launch` adds only `--mode rpc`, preserves existing model/thinking flags and environment,
  and rejects the wrong harness id or a conflicting mode.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The test module and native Pi modules directly prove catalog parsing, process ownership, and safe
normalized advertisement.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The fake transport supplies reasoning/non-reasoning models, returns them from `get_available_models`, places a secret-shaped header in state, and emulates mutation responses, clamps, hangs, and catalog drift. | L39-L207 | [test_pi_rpc_adapter.py](agents-remember/mcp/tests/test_pi_rpc_adapter.py) |
| Launch tests preserve every native setting while adding RPC mode and reject a near-miss harness id; parser tests pin provider identity, model-gated thinking, empty catalogs, and malformed maps. | L314-L402 | [test_pi_rpc_adapter.py](agents-remember/mcp/tests/test_pi_rpc_adapter.py) |
| Discovery is prompt-free and entry-free, failure paths stop/reset for retry, and started advertisement preserves selected model/effort while stripping model headers. | L406-L488 | [test_pi_rpc_adapter.py](agents-remember/mcp/tests/test_pi_rpc_adapter.py) |
| Model switching preserves exact provider plus slash-bearing model id, surfaces the vendor unknown-model error, and rejects malformed identities without a write. | L490-L526 | [test_pi_rpc_adapter.py](agents-remember/mcp/tests/test_pi_rpc_adapter.py) |
| Thinking readback proves both exact and silently clamped outcomes without notification evidence; a new model immediately supplies the effort gate. | L528-L585 | [test_pi_rpc_adapter.py](agents-remember/mcp/tests/test_pi_rpc_adapter.py) |
| Missing readback and hangs in mutation, state, or catalog stages return unknown without effect and release the shared queue for a later set. | L587-L629 | [test_pi_rpc_adapter.py](agents-remember/mcp/tests/test_pi_rpc_adapter.py) |
| An unadvertised clamped effort or a selected model missing from the refreshed catalog cannot promote or corrupt the retained advertisement. | L631-L676 | [test_pi_rpc_adapter.py](agents-remember/mcp/tests/test_pi_rpc_adapter.py) |
| `pi_rpc_launch` preserves the launch while adding RPC mode; state parsing sanitizes the model object and catalog parsing builds unique provider-qualified model capabilities. | L114-L130; L176-L234 | [pi_rpc_protocol.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_protocol.py) |
| Adapter startup, transient discovery, cleanup, cached advertisement, and catalog/state validation are owned by the native Pi adapter. | L109-L194; L411-L434 | [pi_rpc_adapter.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_adapter.py) |
| The adapter delegates both setters to one configuration transaction object with a configurable finite timeout. | L68-L107; L208-L214 | [pi_rpc_adapter.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_adapter.py) |
| Configuration validates provider/model identity and the selected model's dynamic effort vocabulary, serializes mutations, and commits only coherent state plus catalog readback. | L27-L131 | [pi_rpc_configuration.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_configuration.py) |
| The whole mutation/readback transaction is bounded; timeout, disconnect, or incoherent catalog evidence returns unknown without an effective value. | L133-L167 | [pi_rpc_configuration.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_configuration.py) |

## Cross-Repo References

No sibling repository or external transport implementation is required for these native Pi tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
