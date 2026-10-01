# mcp/src/agents_remember/serving/pi_rpc_protocol.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines Pi's strict native RPC wire contract: JSONL framing, launch/session argv transforms,
response/state/model/entry parsing, activity vocabulary, content extraction, and extension UI
response shapes. 260718-CHATS-L0E adds honest entry identity and timestamp helpers for native
evidence paging.

## Code Commentary

### Logic

`PiRpcJsonlDecoder` splits only on LF bytes, accepts a bounded final unterminated record and trailing
CR, and rejects malformed/non-object/non-standard JSON. Launch helpers add RPC mode and preserve
exact persisted-session selection. `parse_pi_state` validates readiness state, derives the
provider-qualified current model, and retains only safe model identity fields. `parse_pi_models`
maps the auth-filtered live catalog to normalized model rows and delegates each model's thinking
menu to `_pi_effort_options`. Remaining helpers validate response correlation, entries, messages,
queue counts, and method-specific dialog responses.

L0E's `pi_entry_identity` returns an entry's durable `(id, parentId, type)` coordinates — the only
honest Pi paging identity — failing closed when id or type is missing rather than skipping the
entry and silently gapping a native page. `pi_entry_created_at` reports the entry's own
`timestamp` only when the schema carries non-empty text and never invents one.

### Conventions

Model identity is `provider/id`; bare ids are not globally unique. Non-reasoning models advertise
only `off`. Reasoning models treat `off` through `high` as supported unless explicitly mapped to
null, while `xhigh` and `max` are included only when the model's own map explicitly supplies a string.

### Invariants And Boundaries

- The default path never hardcodes a model catalog; rows come only from `get_available_models`.
- Thinking is model-gated. Duplicate provider/id identities, malformed maps, or contradictory state
  fail loudly.
- Raw provider headers are intentionally excluded from retained `get_state` evidence because that
  vendor object may contain credentials; only provider, id, and optional name are retained. This
  defensive boundary prevents credential propagation at the subprocess trust boundary.
- LF is the delimiter; U+2028/U+2029 remain JSON content, and generic framing recovery is forbidden.
- L1 launch transformation adds only `--mode rpc`; model/thinking launch flags belong to L2.
- Exact package versions remain fixture/smoke evidence rather than production compatibility gates.
- Entry identity is the sole native paging coordinate; missing identity fails closed and timestamps
  are never fabricated.

### Todos

L2 extends native launch argv with settings-owned model/thinking flags; L3 consumes Pi's asymmetric
set-model and clamping set-thinking semantics.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so the previously recorded live
Pi link was not treated as configured evidence for this update.

No configured domain documentation could be checked.

### Repo-Internal References

The adapter consumes these parsers in a deliberate startup/discovery order, while the process module
owns raw subprocess transport.

- Adapter startup/discovery reads state and catalog, validates current selection, and keeps entries out of discovery. [1]
- Process transport uses this module's JSONL encoder/decoder and exact response correlation. [2]

### Cross-Repo References

No external repository boundary is implemented by this protocol parser.

No meaningful cross-repo references found.
