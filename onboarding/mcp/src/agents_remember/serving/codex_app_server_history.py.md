# mcp/src/agents_remember/serving/codex_app_server_history.py

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

## Evidence

### Docs References

`system/sources.md` has no configured Domain Documentation entries, so no live Codex/OpenSrc
documentation route was authorized for this pass.

No configured domain documentation could be checked.

### Repo-Internal References

The adapter owns connection/session lifecycle and delegates only native-history acquisition to this
reader. Focused tests pin every probe, continuation, cycle, fallback, and capacity contract.

- The adapter constructs one reader, delegates native pages to it, and resets the probe after reconnect. [1]
- The protocol defines the separate 128 MiB emergency payload fuse before decoding. [2]



### Cross-Repo References

The module speaks the external Codex app-server JSON-RPC contract, but the repository's source
registry did not authorize a live external documentation route for this pass.

No externally health-checked reference was available.

## 260731-EFA-L2 Current Delta

**`BoundedPageRequest`** (`thread_id`, `cursor`, `limit`, `byte_budget`) is now the single argument
every bounded native-history read takes: one page — which thread, from where, and how much may come
back. The two bounds are not independent (the reader stops at whichever of `limit` frames or
`byte_budget` bytes is reached first), and the cursor is only meaningful for the thread it was
minted against — reading a page under a mismatched set is how a walk silently returns another
thread's frames. `_scan_bounded_source` and both bounded contracts (`bounded-items`,
`bounded-turns`) take the request; only `contract` stays a separate keyword.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
