# mcp/src/agents_remember/serving/codex_app_server_history.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_history.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns one Codex app-server connection's native-history capability probe and bounded continuation
state. It prefers `thread/items/list`, falls through to `thread/turns/list`, and enters the
explicit legacy `thread/read(includeTurns=true)` compatibility path only when both bounded methods
return exact JSON-RPC `-32601`. It never selects a contract from a Codex version string.

## Code Commentary

### Logic

`CodexNativeHistoryReader.read_page` probes items first and turns second, caches the accepted
contract for the connection, and resets that choice on reconnect. Bounded requests ask for one
source item or turn at a time. One complete parsed source response is then checked against the
16 MiB post-transport materialization ceiling before output is clipped to the caller's smaller
count/byte window.

Turns/full and legacy responses can expand to several native frames while the AR page ends in the
middle of that source response. `_BoundedWalk` therefore retains only the unconsumed suffix behind
a single-use opaque `ar-cnh1` cursor. The cache is a 64 MiB/64-walk LRU: these explicit bounds are
necessary because cancelled callers may abandon opaque cursors, and without them retained source
responses would become an unbounded second history store. Source-cursor cycles, repeated native
ids, empty continued pages, expired continuations, unreadable shapes, and capacity refusal are
typed child-local outcomes.

The legacy path uses the same one-shot walk. It fetches and decodes the complete thread once,
applies the 16 MiB ceiling to the aggregate native-frame bytes, and serves later AR pages from the
retained suffix without issuing another `thread/read`.

### Conventions

The transport fuse, source-response ceiling, retained-continuation ceiling, output byte budget,
and item limit are separate contracts. A source cursor belongs to Codex; an `ar-cnh1` cursor belongs
to this reader and is scoped to the accepted contract, exact thread, and live reader instance.

### Invariants And Boundaries

- The 128 MiB JSONL transport fuse is upstream of this module and remains shared-fatal; this reader
  cannot prevent allocation of one valid response below that fuse.
- The 16 MiB ceiling is post-transport and applies to one complete parsed source response, including
  the aggregate legacy response. It is not advertised as a wire-byte limit.
- Only exact method-unavailable (`-32601`) permits probe fallback. A recognized/refused bounded RPC
  becomes `bounded-rpc-refused`; an accepted method that later fails becomes `bounded-rpc-failed`.
- Items, turns, and legacy continuations each fetch/decode a source response once. Continuation
  consumes retained suffixes and never restarts from source zero.
- One-shot cursors expire after use, reconnect, cycle detection, or LRU eviction.
- `conversation/library/codex.py` is a separate dormant full-read path and remains a named
  follow-up exposure; this reader does not silently repair it.

### Todos

Assess the dormant `conversation/library/codex.py` full-read path separately before enabling it in
production.

## Docs References

`system/sources.md` has no configured Domain Documentation entries, so no live Codex/OpenSrc
documentation route was authorized for this pass.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The adapter owns connection/session lifecycle and delegates only native-history acquisition to this
reader. Focused tests pin every probe, continuation, cycle, fallback, and capacity contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The adapter constructs one reader, delegates native pages to it, and resets the probe after reconnect. | L133-L146; L470-L496; L969-L980 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| The protocol defines the separate 128 MiB emergency payload fuse before decoding. | L18-L23; L217-L240 | [codex_app_server_protocol.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_protocol.py) |
| Unit regressions cover items-first/turns fallback, linear one-shot walks, cycle termination, exact fallback, aggregate legacy refusal, eviction, and typed IPC survival. | L135-L589 | [test_codex_native_history.py](agents-remember/mcp/tests/test_codex_native_history.py) |
| The production regression crosses measured-size stdio, runtime probe, adapter, Unix IPC, and selected-child projection. | L279-L406 | [test_codex_history_production_path.py](agents-remember/mcp/tests/test_codex_history_production_path.py) |

## Cross-Repo References

The module speaks the external Codex app-server JSON-RPC contract, but the repository's source
registry did not authorize a live external documentation route for this pass.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No externally health-checked reference was available. | — | — |

## Update History

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: created strict 1:1 onboarding for the
  runtime-probed items/turns/legacy contract, one-shot opaque continuation, 16 MiB source-response
  ceiling, 64 MiB/64-walk LRU, exact `-32601` fallback, typed cycle/capacity outcomes, shared-fatal
  transport boundary, and dormant library follow-up. Verification metadata remains blank because
  the new source is uncommitted.
