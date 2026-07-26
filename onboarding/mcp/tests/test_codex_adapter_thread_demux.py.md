# mcp/tests/test_codex_adapter_thread_demux.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_adapter_thread_demux.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T21:59+02:00 |
| lastVerifiedCommitHash |  `a401e3dba0bc6e9723451edbfdefb8d77c42945d`|
| lastVerifiedCommitDate |  2026-07-27T00:27:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Thread-demux regression tests for multiplexed codex sub-agent traffic (R1).
The codex app-server auto-attaches sub-agent thread listeners to the seat's connection, so
one transport carries interleaved parent + sub-agent notifications and server requests;
before the demux the first foreign-thread notification failed the whole bridge (the
2026-07-24 production seat death). These tests pin the anti-death behavior, plus the two
follow-on production kill seams: concurrent server requests on one thread (normal vendor
traffic, never a bridge failure) and the adapter event queue shedding load instead of
raising queue-full.

## Code Commentary

### Logic

Seventeen async tests drive the real `CodexAppServerAdapter` over the shared
`FakeCodexTransport`/`prime_start` seam from `test_codex_app_server_adapter`, with wire
frames built by `_agent_wire_fixtures`:

- `test_spawned_subagent_traffic_never_fails_the_bridge` (L106-L169) — the incident shape:
  three sub-agents mid-turn, interleaved with parent traffic; parent busy semantics stay
  parent-scoped, off-wire partial deltas route through the item→thread index, and every
  agent thread lands in the registry with its own completed turns.
- `test_subagent_approval_is_multiplexed_and_answered_by_request_id` (L171-L212) — a
  sub-agent approval rides the plural `pending_interactions` (never the singular parent
  slot), is answered by JSON-RPC request-id, and a server-settled request clears per
  thread via `serverRequest/resolved`.
- `test_collab_items_bind_agent_identity_into_the_registry` (L214-L272) — parent-thread
  `collabAgentToolCall` and `subAgentActivity` evidence binds status/agentPath into the
  registry, and the bound identity becomes the agent label on multiplexed approvals.
- `test_unknown_item_delta_degrades_without_failing` (L274-L315) — an unbound partial
  delta crosses unmodified (no invented thread); a full-shape foreign-thread delta
  auto-registers its thread as `unresolved`.
- `test_read_native_page_reads_the_requested_agent_thread` (L317-L349) — native pages
  demux by `thread_id` (agent thread vs parent default).
- `test_malformed_agent_thread_frames_degrade_to_raw_evidence` (L351-L400, review R5) —
  agent-thread shape drift degrades to preserved raw evidence with a `degraded` reason;
  the bridge stays `ready`.
- `test_malformed_parent_frame_still_fails_loud` (L402-L417) — the same malformation on
  the PARENT thread still fails the bridge: parent-thread shapes stay load-bearing.
- `test_registry_full_degrades_and_settled_threads_evict` (L419-L460, review R5) — at
  `THREAD_REGISTRY_LIMIT` an unevictable registry degrades the overflow frame; a settled
  agent thread is evicted to make room for the next one.
- `test_concurrent_parent_server_requests_never_fail_the_bridge` (L462-L513) — two
  concurrent pendings on the SAME parent thread are normal traffic: both register, the
  singular slot carries the OLDEST for back-compat, each is answerable individually by
  request id (parent guard honored), and a server-settled request clears by rpc id.
- `test_experimental_server_request_on_parent_degrades` (L515-L546) — an
  unknown/experimental request METHOD on the parent is declined (`respond_error` -32601)
  and crosses as degraded preserved evidence; the bridge stays `ready` and nothing stays
  outstanding.
- `test_malformed_known_method_parent_request_fails_loud` (L548-L572) — a KNOWN stable
  method's malformed params on the parent keeps failing the bridge: never
  declined-and-degraded, no error response, nothing outstanding.
- `test_known_method_request_with_boolean_rpc_id_fails_loud` (L574-L604) — `id: true` on
  a known stable method fails the bridge; no silent outstanding.
- `test_unknown_method_on_parent_degrades` (L606-L637) — a method outside both the
  stable and experimental sets is declined (-32601, "unsupported") and degraded, never
  fatal.
- `test_pending_map_overflow_declines_the_newest_request` (L639-L675) — at 16 pendings
  the bounded per-thread map declines + degrades the NEW request (`map is full`) while
  the older 16 stay intact and answerable.
- `test_delta_flood_sheds_oldest_deltas_with_an_honest_notice` (L677-L742) — a 3-agent
  delta flood past the queue limit: no raise, every event sequenced, structural
  completions survive the shed, the shed count is accounted, and one `ar/load-shed`
  notice with the count crosses once the consumer catches up.
- `test_load_shed_notice_crosses_on_consumer_drain_without_new_traffic` (L758-L789) —
  flood → full drain → producer silent: the CONSUMER side mints the notice as the last
  event the subscriber sees, exactly counted (`_flood_deltas`, L744-L756, supplies the
  pure-delta flood past `ADAPTER_EVENT_QUEUE_LIMIT`).
- `test_load_shed_notice_precedes_the_close_sentinel_on_stop` (L791-L819) — flood →
  drain → `stop()`: the notice mints BEFORE the close sentinel, fully counted — the
  minted order ends `[ar/load-shed, close sentinel]`, never the other way around.

### Conventions

`@pytest.mark.anyio` with an explicit `asyncio` backend fixture; synchronous predicates
poll `live_snapshot` (the async message pump) through an `eventually` helper with a
bounded loop — never bare sleeps for convergence. Agent-thread ids use the `agent-*`
prefix; the parent stays `thread-1` from the shared fixture.

### Invariants And Boundaries

- Foreign-thread traffic never fails the bridge; parent-thread shape errors still do.
- Turn WRITES stay parent-only; approvals are answered per request-id regardless of thread.
- Unknown threads auto-register with honest `unresolved` status — identity is learned from
  collab/activity evidence, never fabricated.
- Degraded frames preserve the original params as raw evidence under `AR_EVIDENCE_KEY`.
- Concurrent server requests on one thread never fail the bridge: the singular slot carries
  the oldest pending for back-compat, every pending answers by its own request id, and a
  full per-thread map declines + degrades only the NEWEST request.
- An unknown/experimental request METHOD degrades on ANY thread (declined -32601, preserved
  evidence); a KNOWN stable method's malformed shape keeps failing loud on the parent with
  no decline-and-degrade.
- The event queue sheds oldest delta-method events under load and accounts every shed in
  one `ar/load-shed` notice (minted on consumer catch-up and always before the close
  sentinel) — it never raises queue-full.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the wire shapes are proven against the
vendored codex protocol via the shared fixture module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The shared fixture/transport seam (FakeCodexTransport, prime_start, launch, make_adapter) this suite reuses. | L43-L51 | [test_codex_app_server_adapter.py](agents-remember/mcp/tests/test_codex_app_server_adapter.py) |
| The vendored-shape builders the frames come from. | L17-L30 | [_agent_wire_fixtures.py](agents-remember/mcp/tests/_agent_wire_fixtures.py) |
| The demuxed adapter under test: thread registry, per-thread pending maps, multiplexed pendings, method-first degrade, load-shed queue, native-page demux. | L31-L35 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| The snapshot/evidence models carrying the plural pending tuple and evidence key. | L37-L42 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |

## Cross-Repo References

The multiplexed traffic model (auto-attached sub-agent thread listeners on one connection)
is vendored codex app-server behavior; the fixture module pins each shape to its proving
file in the vendor checkout.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The live sub-agent spawn sequences (V1 collab / V2 subAgentActivity) the demux must survive. | L30-L32 of the fixture docstring | [codex app-server v2 turn_start suite](https://github.com/openai/codex/blob/main/codex-rs/app-server/tests/suite/v2/turn_start.rs) |

## Update History

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the nine new remediation
  tests — concurrent parent server requests answered per id with the oldest in the
  singular slot, the method-first degrade split (experimental/unknown methods decline +
  degrade on the parent, known-method malformed shapes and boolean rpc ids still fail
  loud), the bounded pending map declining only the newest request, and the load-shed
  queue pins (delta flood sheds oldest deltas with structural completions surviving, the
  consumer-side notice mint, and the notice-before-close-sentinel ordering). Refreshed
  the import-block citations (L17-L51) and the per-test anchors. Verification metadata
  stays pinned — the change is uncommitted.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: created the sidecar for the new
  thread-demux incident-regression suite (R1; review R5 degrade/registry-eviction pins).
  Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
