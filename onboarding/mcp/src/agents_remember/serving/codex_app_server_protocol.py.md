# mcp/src/agents_remember/serving/codex_app_server_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation entries are configured in the resolved source registry; the validated
protocol snapshot is recorded in the repository fixture instead.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture pins the CLI version, protocol, and stable method inventory. | "codex-app-server/0.144.3", "initialize", "model/list" | mcp/tests/fixtures/codex_app_server_0_144_3.json:4-16 |
| Adapter uses this transport for correlated fresh-turn settings application on the existing thread. | `CodexAppServerSession`, `set_model`, `set_effort` | mcp/src/agents_remember/serving/codex_app_server_session.py:102-458; mcp/src/agents_remember/serving/codex_app_server_adapter.py:163-194; mcp/src/agents_remember/serving/codex_app_server_adapter.py:196-224 |

## Cross-Repo References

The transport is an external-process boundary to the installed Codex CLI.

| Finding | Anchor | Source |
| --- | --- | --- |

### 260713-PHA-L6 Capability Boundary

The protocol identity is `codex-app-server`; the negotiated opaque CLI token is validated from
structured initialization and thread evidence by the session layer. Exact package versions are
fixture/smoke evidence, not production protocol pins.

## 260715-FEUI-L5 Submission Authority Delta

JSON-RPC request writes share a transport lock and accept a final authority guard immediately before
the first byte. A rejected guard removes the pending request without writing. No await occurs between
the final claim and write, making withdrawal-vs-dispatch linearization observable and exact.

## 260727-CHATS-IM-L2 Emergency Framing Fuse Delta

The former 4 MiB normal-operation cap is replaced by
cit:([`CODEX_REMOTE_COMPATIBILITY_CEILING_BYTES`], mcp/src/agents_remember/serving/codex_app_server_protocol.py:22-22). This number is the available
Codex remote app-server compatibility precedent and an emergency malformed/runaway JSON payload
fuse only; it is not paging and does not bound retained history. cit:([`_read_messages`], mcp/src/agents_remember/serving/codex_app_server_protocol.py:217-246) removes exactly
one JSONL newline before comparing payload bytes: a 128 MiB payload plus delimiter is
valid, 128 MiB + 1 is shared-fatal, and the same explicit failure reaches pending RPCs and the event
stream because the JSONL transport cannot safely resynchronize after a partial oversized record.

## Update History

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 8 citations (citation_anchor_missing=3, citation_prose_not_in_cit_form=2, citation_source_malformed=3); final scoped citation check clean.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: documented the 128 MiB emergency payload
  fuse, delimiter-excluded boundary, shared-fatal above-fuse behavior, and separation from native
  history paging/materialization bounds. Verification metadata remains pinned while the source
  change is uncommitted.

- 2026-07-17T21:39+02:00 — FEUI-L5: documented the guarded first-write seam, shared lock, and
  pending-request cleanup when authority rejects dispatch.
- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented cancellation reclamation,
  syntactically valid late-response discard, absence of abandoned-id tombstones, and continued
  strict failure for malformed correlation evidence.
- 2026-07-14T17:00:00+02:00 — 260713-PHA-L6 master-exit correction: historicized the obsolete
  exact-0.144.3 transport convention; structured initialize/thread evidence is authoritative.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: removed the stale pinned-version description and documented
  the unversioned protocol boundary.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for bounded JSON-RPC
  stdio transport, pinned protocol version, and loud failure boundaries. Verification remains
  unset until closeout stamps the code commit.
