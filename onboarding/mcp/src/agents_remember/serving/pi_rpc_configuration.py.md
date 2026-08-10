# pi_rpc_configuration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_configuration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns Pi RPC's serialized, finite, catalog-coherent mid-session model/thinking mutation transaction
and returns honest normalized `SetResult` evidence.

## Code Commentary

### Logic

`PiRpcConfiguration` holds one lock across the native mutation response, candidate `get_state`, and
refreshed `get_available_models` read. One positive configurable `asyncio.timeout` bounds that whole
transaction. `set_model` requires the exact `provider/model-id` shape, splits only the first slash,
surfaces native `success:false` as `unsupported`, and echo-verifies only an exact model readback.
`set_effort` admits only a session-settable token from the currently selected model's dynamic menu;
after readback it preserves a coherent vendor clamp as distinct requested/effective values. The
adapter commits candidate state and catalog together only after these checks pass.

### Conventions

Five seconds is the default mutation budget, but callers may provide another positive finite value.
Vendor refusal and absence of proof are different: a correlated native failure is `unsupported`,
whereas timeout, disconnect, missing readback, catalog disappearance, invalid clamp value, or other
incoherent evidence is `unknown`.

### Invariants And Boundaries

- Model identities remain exact provider-qualified catalog keys; nested model ids survive the
  first-slash split.
- Effort admission is selected-model-gated, never a global or cross-model union.
- Mutation response alone is insufficient. State readback and refreshed catalog must agree before
  the old advertised snapshot is replaced.
- `echo-verified` may report a different effective effort only when Pi's readback is a coherent
  advertised option for the unchanged selected model.
- The lock and timeout are protocol-ordering requirements: they prevent interleaved readback and
  release the shared control queue after lost responses.
- This module does not paste commands, persist defaults, mutate settings, reconnect, or own Pi
  prompt delivery.

### Todos

None known for the L3 Pi mutation transaction.

## Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this creation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The adapter supplies candidate readers and the atomic committer; the transport supplies correlated
request cancellation behavior; protocol parsing validates state and model-local menus.

| Finding | Anchor | Source |
| --- | --- | --- |
| Adapter delegates setters here, reads candidate state without publishing it, and commits state/catalog together. | `_read_configuration_state`; `_commit_configuration` | mcp/src/agents_remember/serving/pi_rpc_adapter.py:550-553; mcp/src/agents_remember/serving/pi_rpc_adapter.py:555-561 |
| Transport removes cancelled pending futures and discards their later valid responses without an unbounded tombstone set. | "except asyncio.CancelledError:"; `_dispatch` | mcp/src/agents_remember/serving/pi_rpc_process.py:112-112; mcp/src/agents_remember/serving/pi_rpc_process.py:226-243 |
| Protocol helpers parse correlated responses, safe state, provider-qualified catalogs, and each model's own effort menu. | `parse_pi_response`; `parse_pi_state`; `parse_pi_models`; `_pi_effort_options` | mcp/src/agents_remember/serving/pi_rpc_protocol.py:180-194; mcp/src/agents_remember/serving/pi_rpc_protocol.py:197-215; mcp/src/agents_remember/serving/pi_rpc_protocol.py:218-255; mcp/src/agents_remember/serving/pi_rpc_protocol.py:450-475 |

## Cross-Repo References

No external repository boundary is implemented beyond Pi's native RPC process.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

Model/effort mutation carries the exact operation guard through request and bounded readback. Busy
preflight is rethrown for authority classification; timeout/unknown does not release the shared
timeline and therefore cannot license a following prompt or setter.

## 260731-EFA-L2 Current Delta

**`ConfigurationPorts`** (`transport`, `read_state`, `read_capabilities`, `capabilities`, `commit`,
`request_id`) is now the single argument a set transaction drives: the adapter surface **from
request to committed evidence**. A set is atomic across all six — it mints a request id, writes
through the transport, re-reads the state and capabilities that must corroborate the write, and
commits both together. Handing them over as one port is what keeps a transaction from reading one
adapter and committing to another. The transaction's steps, timeouts and corroboration
requirements are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-03T03:08:58+02:00 — W3-B04 curator: curated 3 table citations (3 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `ConfigurationPorts` as the one atomic set-transaction surface.
- 2026-07-17T21:39+02:00 — FEUI-L5: corrected timeout-release claims and documented guarded
  configuration plus unknown-barrier behavior.

- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: created the sidecar for serialized finite
  mutation/readback/catalog evidence, exact provider parsing, selected-model effort gating,
  catalog-coherent clamp handling, atomic commit, and honest unsupported/unknown classification.
