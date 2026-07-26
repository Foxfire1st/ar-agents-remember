# mcp/tests/_agent_wire_fixtures.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_agent_wire_fixtures.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:45+02:00 |
| lastVerifiedCommitHash |  `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f`|
| lastVerifiedCommitDate |  2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Shared minimal wire-fixture builders for codex sub-agent traffic (R8). One
module owns the vendored app-server frame shapes — `collabAgentToolCall` /
`subAgentActivity` items, `turn/started`/`turn/completed`, `thread/status/changed`,
`item/started`/`item/completed`, `item/agentMessage/delta`,
`item/commandExecution/requestApproval`, and `serverRequest/resolved` — so every
sub-agent test asserts against shapes proven field-for-field against the vendored codex
protocol instead of hand-rolled per-test guesses.

## Code Commentary

### Logic

Pure builder functions returning `JsonObject` params or full JSON-RPC envelopes
(`notification`, `command_execution_approval_request`, `server_request_resolved`).
Every builder populates only the fields a consumer reads, and every field name is one the
vendor emits: the module docstring (L1-L37) pins each shape to its proving source in the
vendored codex checkout (`app-server-protocol/src/protocol/v2/{item,turn,thread,
notification}.rs` and the live spawn suite `app-server/tests/suite/v2/turn_start.rs`
~3544-3868). Timestamps are stable synthetic constants (L44-L46) — no captured user
content. Intentionally malformed shapes (degrade/unknown-vendor cases) deliberately stay
inline in the test modules that assert them, not here.

### Conventions

Underscore-prefixed non-test module imported by the demux and both projector-agent suites;
pytest collects no tests from it. `senderThreadId` is always populated on collab items
(the vendor emits it on every collab call); deltas are keyed by thread AND turn (partial
deltas exist only as adapter-defense shapes inline in the demux suite).

### Invariants And Boundaries

- Fixtures are minimal and synthetic: only vendor-emitted field names, never invented keys.
- A shape that cannot be proven against the vendored protocol does not belong here.
- Malformed/adversarial shapes stay with the tests that assert the degrade path.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the proving authority is the vendored codex
protocol checkout cited in the module docstring and below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The builder inventory and the per-shape vendored-protocol proof mapping. | L1-L37; L49-L199 | [_agent_wire_fixtures.py](agents-remember/mcp/tests/_agent_wire_fixtures.py) |
| The demux incident-regression suite consuming these builders. | L17-L29 | [test_codex_adapter_thread_demux.py](agents-remember/mcp/tests/test_codex_adapter_thread_demux.py) |
| The codex projector-agent suite consuming these builders. | L25-L35 | [test_conversation_projector_codex_agents.py](agents-remember/mcp/tests/test_conversation_projector_codex_agents.py) |
| The demuxed adapter under test: thread registry, per-thread state, multiplexed pendings. | L1-L50 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |

## Cross-Repo References

The fixture shapes are proven against the vendored codex app-server protocol (a read-only
vendor checkout outside the workspace); the module docstring pins each shape to its proving
file, and the vendored tree is the boundary evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `CollabAgentToolCall` / `SubAgentActivity` item variants and their exact camelCase enums. | L7-L21 (docstring) | [codex app-server protocol v2 item.rs](https://github.com/openai/codex/blob/main/codex-rs/app-server-protocol/src/protocol/v2/item.rs) |
| `TurnStarted`/`TurnCompleted` params `{threadId, turn}`. | L22-L24 (docstring) | [codex app-server protocol v2 turn.rs](https://github.com/openai/codex/blob/main/codex-rs/app-server-protocol/src/protocol/v2/turn.rs) |
| The live V1/V2 sub-agent spawn sequences these builders model. | L30-L32 (docstring) | [codex app-server v2 turn_start suite](https://github.com/openai/codex/blob/main/codex-rs/app-server/tests/suite/v2/turn_start.rs) |

## Update History

- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: created the sidecar for the new shared
  codex sub-agent wire-fixture module (R8). Verification is blank because the new source
  file is uncommitted; closeout owns its first source stamp.
