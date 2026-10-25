# mcp/src/agents_remember/observer/tool_events.py

## Governing Overview

[observer overview](overview.md)

## Purpose

Writes every tool call of an agent to the workspace Event River (MIK-R114 rule 1).
One `tool.completed` event per call holds facts and no content — tool, ok, code, state,
delivered token count, caller, target role — under the river lock with per-append size
admission. A failed write never breaks the call: it is counted, and the next written
event carries `dropped`.

## Code Commentary

`ToolEventWriter` is the one process-wide writer, installed at server start with the
caller snapshot; `record` never raises. `build_tool_event` assembles the facts-only row:
`_answer_facts` reads the fixed keys out of the completed answer (delivered tokens are
the log-line count of the delivered answer, never whole-result metadata), `_caller_facts`
names the bound agent or a chat, and over-long scalars are left out past
`TOOL_EVENT_VALUE_MAX_CHARS` (120). `call_target_role` carries the started/addressed role
around the completion choke on a context variable, because the choke receives the answer,
not the call. `record_tool_completed` is the choke's one call into the river; outside a
server process there is no writer and the call is simply not observed. `ToolCaller.scope_key` is snapshotted from launch binding and emitted as optional `Event.scopeKey`. No active ambient session or alternate lifecycle-event route is required; every recorded completion targets the workspace River.

## Evidence

- One process-wide writer per tool server; record never raises, losses counted. [1]

- Facts-only row: fixed answer keys plus caller, never content. [2]

- The started/addressed role rides a context variable around the choke. [3]
- The choke writes one river event per completed call. [4]
