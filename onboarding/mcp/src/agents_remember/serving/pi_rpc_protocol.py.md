# mcp/src/agents_remember/serving/pi_rpc_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:17+02:00 |
| lastVerifiedCommitHash | `bc2958ae2d90ab3d34bffde5402d2dc21100e41b` |
| lastVerifiedCommitDate | 2026-07-14T16:16:44+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving/ overview](overview.md)

## Purpose
Defines the pinned Pi 0.80.6 RPC wire contract: strict JSONL framing, launch/session argv
transforms, response/state/entry parsing, capability policy, activity vocabulary, and extension
UI response shapes.

## Code Commentary
`PiRpcJsonlDecoder` splits only on byte LF, accepts the documented final unterminated record and
trailing CR, bounds incomplete frames, and rejects malformed JSON, non-object frames, Unicode
line-separator reinterpretation, and non-standard numeric constants. Schema helpers validate
correlated responses, `get_state`, `get_entries`, message text, queue counts, and method-specific
dialog responses. Launch helpers add RPC mode and select the exact persisted session without losing
other launch configuration.

## Invariants And Boundaries
- Only version `0.80.6` is supported by this candidate.
- LF is the delimiter; U+2028/U+2029 remain JSON content.
- Parsing fails loudly and does not provide generic framing recovery.
- Extension responses require the matching interaction id and documented dialog method.

## Docs References
| Finding | Citations | Source Path |
| --- | --- | --- |
| Pi RPC framing, commands, events, state, entries, and extension UI contract. | RPC documentation | [Pi RPC](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/rpc.md) |

## Repo-Internal References
| Finding | Source Path |
| --- | --- |
| Process transport consuming frames. | [pi_rpc_process.py](pi_rpc_process.py) |
| Adapter consuming parsed state and entries. | [pi_rpc_adapter.py](pi_rpc_adapter.py) |
| Pinned policy fixtures. | [0.80.6-capabilities.json](../../../../../../tests/fixtures/pi_rpc/0.80.6-capabilities.json), [activity.jsonl](../../../../../../tests/fixtures/pi_rpc/activity.jsonl) |

## Cross-Repo References
No meaningful cross-repo references found; the external Pi contract is recorded under Docs References.

### 260713-PHA-L6 Structured Pi Contract

Pi does not expose a production package-version field in startup. Compatibility is negotiated from
correlated `get_state` and `get_entries` responses plus documented event/interaction fields. The
exact `0.80.6` fixture remains smoke evidence only; malformed required contract remains loud.

## Update History
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: replaced the pinned-version description with the structured
  Pi startup contract and preserved exact fixture-only evidence.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for strict framing, pinned
  capability parsing, launch/session preservation, state/entry schemas, and extension UI mapping.
