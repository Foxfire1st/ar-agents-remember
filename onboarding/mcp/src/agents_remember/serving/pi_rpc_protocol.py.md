# mcp/src/agents_remember/serving/pi_rpc_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa` |
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines Pi's strict native RPC wire contract: JSONL framing, launch/session argv transforms,
response/state/model/entry parsing, activity vocabulary, content extraction, and extension UI
response shapes.

## Code Commentary

### Logic

`PiRpcJsonlDecoder` splits only on LF bytes, accepts a bounded final unterminated record and trailing
CR, and rejects malformed/non-object/non-standard JSON. Launch helpers add RPC mode and preserve
exact persisted-session selection. `parse_pi_state` validates readiness state, derives the
provider-qualified current model, and retains only safe model identity fields. `parse_pi_models`
maps the auth-filtered live catalog to normalized model rows and delegates each model's thinking
menu to `_pi_effort_options`. Remaining helpers validate response correlation, entries, messages,
queue counts, and method-specific dialog responses.

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

### Todos

L2 extends native launch argv with settings-owned model/thinking flags; L3 consumes Pi's asymmetric
set-model and clamping set-thinking semantics.

## Docs References

No Domain Documentation source is configured for this repository, so the previously recorded live
Pi link was not treated as configured evidence for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The adapter consumes these parsers in a deliberate startup/discovery order, while the process module
owns raw subprocess transport.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Adapter startup/discovery reads state and catalog, validates current selection, and keeps entries out of discovery. | L87-L156; L318-L384 | [pi_rpc_adapter.py](pi_rpc_adapter.py) |
| Process transport uses this module's JSONL encoder/decoder and exact response correlation. | L33-L147 | [pi_rpc_process.py](pi_rpc_process.py) |

## Cross-Repo References

No external repository boundary is implemented by this protocol parser.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented provider-qualified live catalog
  parsing, per-model thinking rules, current-state identity, and explicit provider-header credential
  exclusion; recorded the L1/L2 launch boundary and unconfigured documentation status.
- 2026-07-14T17:00:00+02:00 — 260713-PHA-L6 master-exit correction: removed the obsolete
  exact-0.80.6 supported-version invariant and made consumed structured Pi fields authoritative.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: replaced the pinned-version description with the structured
  Pi startup contract and preserved exact fixture-only evidence.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for strict framing, pinned
  capability parsing, launch/session preservation, state/entry schemas, and extension UI mapping.
