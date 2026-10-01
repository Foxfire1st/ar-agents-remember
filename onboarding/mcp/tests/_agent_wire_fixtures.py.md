# mcp/tests/_agent_wire_fixtures.py

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

## Evidence

### Docs References

No Domain Documentation source is configured; the proving authority is the vendored codex
protocol checkout cited in the module docstring and below.

No configured domain documentation was available.

### Repo-Internal References

- The local builder inventory, including the `CollabAgents` parameter object. [1]
- The module docstring records external provenance labels for the fixture shapes; those labels are not protocol proof under this frozen source authority. [2]
- The notification builder retains the caller-supplied method and params. [3]
- The collab event builder constructs per-agent status, optional model/effort and tool-call identity. [4]
- The demuxed adapter under test owns the thread registry, per-thread state, and multiplexed pendings. [5]

### Cross-Repo References

The module contains local fixture builders and a docstring record of external protocol provenance.
This bounded card uses the local fixture module and local consumer/adapter suites as source authority;
external protocol files are not treated as frozen source evidence here.
