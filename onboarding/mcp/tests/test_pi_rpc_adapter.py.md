# mcp/tests/test_pi_rpc_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pi_rpc_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05:47+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa` |
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fake-transport and protocol conformance coverage for the native Pi RPC adapter, including dynamic
installed/authenticated model advertisement, model-gated thinking levels, launch preservation,
session behavior, reconnect reconciliation, and strict transport framing.

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
| The fake transport supplies reasoning and non-reasoning models, returns them from `get_available_models`, and places a secret-shaped header in full state-model evidence. | L39-L148 | [test_pi_rpc_adapter.py](agents-remember/mcp/tests/test_pi_rpc_adapter.py) |
| Launch tests preserve every native setting while adding RPC mode and reject a near-miss harness id; parser tests pin provider identity, model-gated thinking, empty catalogs, and malformed maps. | L265-L353 | [test_pi_rpc_adapter.py](agents-remember/mcp/tests/test_pi_rpc_adapter.py) |
| Discovery is prompt-free and entry-free, failure paths stop/reset for retry, and started advertisement preserves selected model/effort while stripping model headers. | L357-L439 | [test_pi_rpc_adapter.py](agents-remember/mcp/tests/test_pi_rpc_adapter.py) |
| `pi_rpc_launch` preserves the launch while adding RPC mode; state parsing sanitizes the model object and catalog parsing builds unique provider-qualified model capabilities. | L114-L130; L176-L234 | [pi_rpc_protocol.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_protocol.py) |
| Adapter startup, transient discovery, cleanup, cached advertisement, and catalog/state validation are owned by the native Pi adapter. | L87-L156 | [pi_rpc_adapter.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_adapter.py) |

## Cross-Repo References

No sibling repository or external transport implementation is required for these native Pi tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented provider-qualified dynamic
  catalogs, model-gated thinking, token-free discovery, strict startup/discovery cleanup, retry
  reset, safe state-model sanitization, and preserved native launch flags; corrected the governing
  overview backlink while preserving existing verification metadata.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented version-free Pi startup coverage.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for Pi fake adapter,
  protocol, activity, extension UI, disconnect, and reconciliation coverage.
