# mcp/tests/_agent_wire_fixtures.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_agent_wire_fixtures.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T15:20+02:00 |
| lastVerifiedCommitHash |  `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |  2026-08-12T00:45:15+02:00|
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
local consumer suites exercise against the bounded fixture shapes. The module docstring records
external provenance labels, but those labels are not protocol proof under this frozen source
authority. Timestamps are stable synthetic constants — no captured user
content. Intentionally malformed shapes (degrade/unknown-vendor cases) deliberately stay
inline in the test modules that assert them, not here.

### Conventions

Underscore-prefixed non-test module imported by the demux and both projector-agent suites;
pytest collects no tests from it. `collab_agent_tool_call_item` takes the three thread-bearing
fields as ONE frozen `CollabAgents` parameter object (`sender_thread_id`, `receiver_thread_ids`,
`states`) because the vendor emits them together on every `CollabAgentToolCall` and `agentsStates`
is keyed by the same receiver thread ids; `None` (never an empty collection) still omits the
vendor's optional field entirely. `senderThreadId` is always populated on collab items
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The local builder inventory, including the `CollabAgents` parameter object. | `CollabAgents` | mcp/tests/_agent_wire_fixtures.py:63-77 |
| The module docstring records external provenance labels for the fixture shapes; those labels are not protocol proof under this frozen source authority. | `protocol` | mcp/tests/_agent_wire_fixtures.py:1-37 |
| The notification builder retains the caller-supplied method and params. | "def notification(" | mcp/tests/_agent_wire_fixtures.py:51-54 |
| The collab event builder constructs per-agent status, optional model/effort and tool-call identity. | "def collab_agent_tool_call_item(" | mcp/tests/_agent_wire_fixtures.py:80-106 |
| The demuxed adapter under test owns the thread registry, per-thread state, and multiplexed pendings. | `CodexAppServerAdapter` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:91-1115 |

## Cross-Repo References

The module contains local fixture builders and a docstring record of external protocol provenance.
This bounded card uses the local fixture module and local consumer/adapter suites as source authority;
external protocol files are not treated as frozen source evidence here.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-11T15:20+02:00 — Re-anchored both consumer claims to each suite's unique fixture-import
  declaration instead of a builder name repeated by later calls.
- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: separated local fixture construction from
  external provenance, re-anchored local consumer/adapter suites, and removed out-of-authority protocol rows.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 code-quality gate: `collab_agent_tool_call_item` now
  takes `sender_thread_id` / `receiver_thread_ids` / `agents_states` as one frozen `CollabAgents`
  dataclass to satisfy the max-argument rule, which also shifted every line below the imports.
  Documented the parameter object in Conventions and re-anchored the own-file citations against
  the current source: the builder inventory is now L51-L214 (was L49-L199) and the synthetic
  timestamp constants are L46-L48 (was L44-L46); the docstring proof mapping is still L1-L37. No
  wire shape, vendor field name, or builder function was added, removed, or renamed, so the
  per-shape protocol proofs stand.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: created the sidecar for the new shared
  codex sub-agent wire-fixture module (R8). Verification is blank because the new source
  file is uncommitted; closeout owns its first source stamp.
