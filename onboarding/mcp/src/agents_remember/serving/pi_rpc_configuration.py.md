# pi_rpc_configuration.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this creation.

No configured domain documentation could be checked.

### Repo-Internal References

The adapter supplies candidate readers and the atomic committer; the transport supplies correlated
request cancellation behavior; protocol parsing validates state and model-local menus.

- Adapter delegates setters here, reads candidate state without publishing it, and commits state/catalog together. [1]
- Transport removes cancelled pending futures and discards their later valid responses without an unbounded tombstone set. [2]
- Protocol helpers parse correlated responses, safe state, provider-qualified catalogs, and each model's own effort menu. [3]

### Cross-Repo References

No external repository boundary is implemented beyond Pi's native RPC process.

No meaningful cross-repo references found.

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
