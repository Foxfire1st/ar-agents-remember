# mcp/src/agents_remember/serving/codex_app_server_protocol.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns the bounded newline-delimited JSON-RPC stdio transport for the Codex app-server. The transport
is version-neutral; `0.144.3` is fixture/smoke evidence, while production compatibility is decided
by the structured messages and fields consumed by the session and adapter.

## Code Commentary

### Logic

`CodexStdioTransport` launches the supplied command and environment unchanged, correlates request
responses, and forwards notifications/server requests. Cancellation removes the request's pending
future immediately. A later response with a syntactically valid positive integer id but no live
future is stale and ignored, so no unbounded abandoned-id tombstone is needed and the reader remains
usable for subsequent requests. Invalid ids, malformed JSON/RPC objects, oversized lines, process
failure, and live-request protocol errors remain loud typed failures. The transport does not
interpret thread, turn, or setter semantics.

### Conventions

JSON objects are validated at the transport boundary and event delivery uses a bounded queue. A
missing pending future is treated as cancellation evidence only after the response id itself passes
syntax validation. The transport does not infer compatibility from package text.

### Invariants And Boundaries

- Unterminated, malformed, unknown-id, and over-limit messages fail loudly.
- Queue saturation and subprocess disconnect resolve pending callers; no resend or compatibility
  fallback belongs here.
- Cancelling a request reclaims its pending entry; a late response cannot satisfy another request or
  kill the shared stdout reader.
- Launch argv, cwd, environment, and authentication are supplied by the caller and preserved.

### Todos

None known for the L3 cancellation boundary.

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved source registry; the validated
protocol snapshot is recorded in the repository fixture instead.

No configured live documentation source was available for this pass.

### Repo-Internal References

- Fixture pins the CLI version, protocol, and stable method inventory. [1]
- Adapter uses this transport for correlated fresh-turn settings application on the existing thread. [2]

### Cross-Repo References

The transport is an external-process boundary to the installed Codex CLI.

#### 260713-PHA-L6 Capability Boundary

The protocol identity is `codex-app-server`; the negotiated opaque CLI token is validated from
structured initialization and thread evidence by the session layer. Exact package versions are
fixture/smoke evidence, not production protocol pins.

## 260715-FEUI-L5 Submission Authority Delta

JSON-RPC request writes share a transport lock and accept a final authority guard immediately before
the first byte. A rejected guard removes the pending request without writing. No await occurs between
the final claim and write, making withdrawal-vs-dispatch linearization observable and exact.

## 260727-CHATS-IM-L2 Emergency Framing Fuse Delta

The former 4 MiB normal-operation cap is replaced by
cit:([`CODEX_REMOTE_COMPATIBILITY_CEILING_BYTES`], mcp/src/agents_remember/serving/codex_app_server_protocol.py:27-27). This number is the available
Codex remote app-server compatibility precedent and an emergency malformed/runaway JSON payload
fuse only; it is not paging and does not bound retained history. cit:([`_read_messages`], mcp/src/agents_remember/serving/codex_app_server_protocol.py:217-246) removes exactly
one JSONL newline before comparing payload bytes: a 128 MiB payload plus delimiter is
valid, 128 MiB + 1 is shared-fatal, and the same explicit failure reaches pending RPCs and the event
stream because the JSONL transport cannot safely resynchronize after a partial oversized record.
