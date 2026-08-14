# mcp/src/agents_remember/serving/codex_app_server_history.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_history.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The adapter owns connection/session lifecycle and delegates only native-history acquisition to this
reader. Focused tests pin every probe, continuation, cycle, fallback, and capacity contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter constructs one reader, delegates native pages to it, and resets the probe after reconnect. | `CodexAppServerAdapter` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:91-1115 |
| The protocol defines the separate 128 MiB emergency payload fuse before decoding. | `CODEX_REMOTE_COMPATIBILITY_CEILING_BYTES` | mcp/src/agents_remember/serving/codex_app_server_protocol.py:27-27 |
| Unit regressions cover items-first/turns fallback, linear one-shot walks, cycle termination, exact fallback, aggregate legacy refusal, eviction, and typed IPC survival. | `test_bounded_items_are_probed_and_opaque_cursor_consumes_each_source_page_once`; `test_turns_list_is_used_when_bounded_items_method_is_unavailable`; `test_turns_full_continuation_requests_and_decodes_each_source_turn_once`; `test_two_cursor_cycle_terminates_typed_without_re_requesting_a_source_page`; `test_legacy_whole_thread_read_requires_both_bounded_methods_to_be_unavailable`; `test_legacy_complete_response_aggregate_over_ceiling_is_typed`; `test_evicted_legacy_continuation_expires_without_refetch`; `test_native_history_limit_outcome_survives_both_control_ipc_clients` | mcp/tests/test_codex_native_history.py:134-166; mcp/tests/test_codex_native_history.py:169-202; mcp/tests/test_codex_native_history.py:205-252; mcp/tests/test_codex_native_history.py:350-384; mcp/tests/test_codex_native_history.py:387-419; mcp/tests/test_codex_native_history.py:422-451; mcp/tests/test_codex_native_history.py:487-531; mcp/tests/test_codex_native_history.py:572-589 |
| The production regression crosses measured-size stdio, runtime probe, adapter, Unix IPC, and selected-child projection. | `test_measured_history_crosses_transport_probe_ipc_and_selected_projection` | mcp/tests/test_codex_history_production_path.py:281-365 |

## Cross-Repo References

The module speaks the external Codex app-server JSON-RPC contract, but the repository's source
registry did not authorize a live external documentation route for this pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| No externally health-checked reference was available. | — | — |

## 260731-EFA-L2 Current Delta

**`BoundedPageRequest`** (`thread_id`, `cursor`, `limit`, `byte_budget`) is now the single argument
every bounded native-history read takes: one page — which thread, from where, and how much may come
back. The two bounds are not independent (the reader stops at whichever of `limit` frames or
`byte_budget` bytes is reached first), and the cursor is only meaningful for the thread it was
minted against — reading a page under a mismatched set is how a walk silently returns another
thread's frames. `_scan_bounded_source` and both bounded contracts (`bounded-items`,
`bounded-turns`) take the request; only `contract` stays a separate keyword.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T02:50:24+02:00 — W3-B01 curator: curated 4 Repo-Internal table citations with exact adapter, protocol, unit-regression, and production-path anchors. Verification metadata remains unchanged for closeout.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 3 cross-file line citations into
  `codex_app_server_adapter.py`. Reader construction is now L152-L164 (`class CodexAppServerAdapter`
  through `self._native_history = CodexNativeHistoryReader()` on L164 — the old L133-L146 stopped at
  the `__init__` signature and never actually covered the construction), native-page delegation is
  L489-L515 (`read_native_page` calling `self._native_history.read_page`), and the probe reset is
  L1081-L1091 (`_reconnect` through `self._native_history.reset_probe()`). The old third range
  L969-L980 was wrong even at the pinned commit — it landed on `_handle_settings_updated`, which
  never touches the probe.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `BoundedPageRequest` as the single bounded native-history page selector.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: created strict 1:1 onboarding for the
  runtime-probed items/turns/legacy contract, one-shot opaque continuation, 16 MiB source-response
  ceiling, 64 MiB/64-walk LRU, exact `-32601` fallback, typed cycle/capacity outcomes, shared-fatal
  transport boundary, and dormant library follow-up. Verification metadata remains blank because
  the new source is uncommitted.
