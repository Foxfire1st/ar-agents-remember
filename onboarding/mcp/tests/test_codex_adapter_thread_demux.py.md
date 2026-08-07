# mcp/tests/test_codex_adapter_thread_demux.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_adapter_thread_demux.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash |  `b252c42cca200933d5c9c36e26de47a526a569ce`|
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
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

#

- 260731-EFA-L7 (trace delta): the thread-demux suite now anchors against the `codex_app_server_adapter.py` surface and the `FakeCodexTransport` test double in `test_codex_app_server_adapter.py`; assertions unchanged.
## Logic

Seventeen async tests drive the real `CodexAppServerAdapter` over the shared
`FakeCodexTransport`/`prime_start` seam from `test_codex_app_server_adapter`, with wire
frames built by `_agent_wire_fixtures`:

- cit:([`test_spawned_subagent_traffic_never_fails_the_bridge`], mcp/tests/test_codex_adapter_thread_demux.py:117-180) — the incident shape:
  three sub-agents mid-turn, interleaved with parent traffic; parent busy semantics stay
  parent-scoped, off-wire partial deltas route through the item→thread index, and every
  agent thread lands in the registry with its own completed turns.
- cit:([`test_subagent_approval_is_multiplexed_and_answered_by_request_id`], mcp/tests/test_codex_adapter_thread_demux.py:183-221) — a
  sub-agent approval rides the plural `pending_interactions` (never the singular parent
  slot), is answered by JSON-RPC request-id, and a server-settled request clears per
  thread via `serverRequest/resolved`.
- cit:([`test_collab_items_bind_agent_identity_into_the_registry`], mcp/tests/test_codex_adapter_thread_demux.py:224-283) — parent-thread
  `collabAgentToolCall` and `subAgentActivity` evidence binds status/agentPath into the
  registry, and the bound identity becomes the agent label on multiplexed approvals. Since
  260731-EFA-L2 the collab frame is built as
  `collab_agent_tool_call_item(..., agents=CollabAgents(sender, receiver_thread_ids=…, states=…))`
  — the fixture's three thread-bearing keywords (`sender_thread_id`, `receiver_thread_ids`,
  `agents_states`) are now one `CollabAgents` parameter object, because they are one fact
  about who the call is between. The wire shape emitted, and therefore what this test
  proves, is unchanged.
- cit:([`test_unknown_item_delta_degrades_without_failing`], mcp/tests/test_codex_adapter_thread_demux.py:286-327) — an unbound partial
  delta crosses unmodified (no invented thread); a full-shape foreign-thread delta
  auto-registers its thread as `unresolved`.
- cit:([`test_read_native_page_reads_the_requested_agent_thread`], mcp/tests/test_codex_adapter_thread_demux.py:330-364) — native pages
  demux by `thread_id` (agent thread vs parent default).
- `test_malformed_agent_thread_frames_degrade_to_raw_evidence` (L354-L401, review R5) —
  agent-thread shape drift degrades to preserved raw evidence with a `degraded` reason;
  the bridge stays `ready`.
- `test_malformed_parent_frame_still_fails_loud` (cit:([`test_malformed_parent_frame_still_fails_loud`], mcp/tests/test_codex_adapter_thread_demux.py:418-432)) — the same malformation on
  the PARENT thread still fails the bridge: parent-thread shapes stay load-bearing.
- `test_registry_full_degrades_and_settled_threads_evict` (L422-L463, review R5) — at
  `THREAD_REGISTRY_LIMIT` an unevictable registry degrades the overflow frame; a settled
  agent thread is evicted to make room for the next one.
- cit:([`test_concurrent_parent_server_requests_never_fail_the_bridge`], mcp/tests/test_codex_adapter_thread_demux.py:478-530) — two
  concurrent pendings on the SAME parent thread are normal traffic: both register, the
  singular slot carries the OLDEST for back-compat, each is answerable individually by
  request id (parent guard honored), and a server-settled request clears by rpc id.
- cit:([`test_experimental_server_request_on_parent_degrades`], mcp/tests/test_codex_adapter_thread_demux.py:533-568) — an
  unknown/experimental request METHOD on the parent is declined (`respond_error` -32601)
  and crosses as degraded preserved evidence; the bridge stays `ready` and nothing stays
  outstanding.
- cit:([`test_malformed_known_method_parent_request_fails_loud`], mcp/tests/test_codex_adapter_thread_demux.py:571-594) — a KNOWN stable
  method's malformed params on the parent keeps failing the bridge: never
  declined-and-degraded, no error response, nothing outstanding.
- cit:([`test_known_method_request_with_boolean_rpc_id_fails_loud`], mcp/tests/test_codex_adapter_thread_demux.py:597-626) — `id: true` on
  a known stable method fails the bridge; no silent outstanding.
- cit:([`test_unknown_method_on_parent_degrades`], mcp/tests/test_codex_adapter_thread_demux.py:629-659) — a method outside both the
  stable and experimental sets is declined (-32601, "unsupported") and degraded, never
  fatal.
- cit:([`test_pending_map_overflow_declines_the_newest_request`], mcp/tests/test_codex_adapter_thread_demux.py:662-697) — at 16 pendings
  the bounded per-thread map declines + degrades the NEW request (`map is full`) while
  the older 16 stay intact and answerable.
- cit:([`test_delta_flood_sheds_oldest_deltas_with_an_honest_notice`], mcp/tests/test_codex_adapter_thread_demux.py:700-761) — a 3-agent
  delta flood past the queue limit: no raise, every event sequenced, structural
  completions survive the shed, the shed count is accounted, and one `ar/load-shed`
  notice with the count crosses once the consumer catches up.
- cit:([`test_load_shed_notice_crosses_on_consumer_drain_without_new_traffic`], mcp/tests/test_codex_adapter_thread_demux.py:782-812) —
  flood → full drain → producer silent: the CONSUMER side mints the notice as the last
  event the subscriber sees, exactly counted (`_flood_deltas`, L757-L772, supplies the
  pure-delta flood past `ADAPTER_EVENT_QUEUE_LIMIT`).
- cit:([`test_load_shed_notice_precedes_the_close_sentinel_on_stop`], mcp/tests/test_codex_adapter_thread_demux.py:815-843) — flood →
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared fixture/transport seam (FakeCodexTransport, prime_start, launch, make_adapter) this suite reuses. | `FakeCodexTransport`; `prime_start`; `launch`; `make_adapter` | mcp/tests/test_codex_app_server_adapter.py:42-103; mcp/tests/test_codex_app_server_adapter.py:212-222; mcp/tests/test_codex_app_server_adapter.py:187-194; mcp/tests/test_codex_app_server_adapter.py:239-247 |
| The vendored-shape builders the frames come from, now including the `CollabAgents` parameter object. | `CollabAgents` | mcp/tests/_agent_wire_fixtures.py:63-77 |
| The demuxed adapter under test: thread registry, per-thread pending maps, multiplexed pendings, method-first degrade, load-shed queue, native-page demux. | `CodexAppServerAdapter`; `_publish_agent_registry`; `CodexThreadRegistry` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:91-1115; mcp/src/agents_remember/serving/codex_app_server_adapter.py:1075-1083; mcp/src/agents_remember/serving/codex_app_server_threads.py:69-300 |
| The snapshot/evidence models carrying the plural pending tuple and evidence key. | `AdapterSnapshot`; `pending_interactions`; `AR_EVIDENCE_KEY` | mcp/src/agents_remember/serving/harness_control_models.py:216-241; mcp/src/agents_remember/serving/harness_control_models.py:58-58 |

## Cross-Repo References

The multiplexed traffic model (auto-attached sub-agent thread listeners on one connection)
is vendored codex app-server behavior; the fixture module pins each shape to its proving
file in the vendor checkout.

| Finding | Anchor | Source |
| --- | --- | --- |
## 260727-CHATS-IM-L2 Runtime-Probed Thread Read Delta

The selected-thread native-page regression now supplies the items-list capability response and
asserts the one-item bounded request for both agent and parent thread ids. The demux contract is
unchanged: an explicit child id routes only that thread, while absent selection reads the parent;
the acquisition implementation is now contract-probed rather than a direct whole-thread request.

## Update History

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 curator (trace delta): body verified against the current code and updated (260731-EFA-L7 (trace delta): the thread-demux suite now anchors against the `codex_app_server_adapte...). Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-03T11:10+02:00 — 260731-EFA-L6 W3-B07 curator: repaired 8 of 8 retained citation findings (6 table anchor/source findings and 2 prose citations). Deleted the external Codex vendor-suite row (2 diagnostics) under the max-reviewer 2026-08-02 14:10 disposition because its source is outside the frozen roots.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the `PLR0913` pass reached the wire fixtures, so
  the collab-frame call shape and every line citation in this card were re-derived from the current
  source. `collab_agent_tool_call_item` no longer takes `sender_thread_id=`, `receiver_thread_ids=`
  and `agents_states=`; those three vendor thread fields are now one `CollabAgents` parameter object
  passed as `agents=`, and the card names it where it describes
  `test_collab_items_bind_agent_identity_into_the_registry`. Adding that import shifted the whole
  import block, so the four Repo-Internal References ranges were corrected (fixtures L17-L30 to
  L16-L29, adapter L31-L35 to L30-L34, models L37-L42 to L36-L41, shared seam L43-L51 to L42-L50),
  each re-read at its new position. All eighteen per-test anchors were likewise recomputed against
  the current file and now cite each test from its `def` line to its last body line; most of that
  correction is older drift this leaf merely exposed, since the anchors were already several lines
  off at the L2 base commit and the leaf itself only moved lines by one before the collab test and
  three after it. No assertion, decline path, degrade reason, bound, or ordering claim changed —
  the emitted wire shape is identical, so every behavioural claim in this card still holds.
  Verification metadata stays pinned until closeout stamps the code commit.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: updated the thread-demux native-page
  coverage record for items-first runtime probing and exact parent/child request selection.
  Verification metadata remains pinned while uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the nine new remediation
  tests — concurrent parent server requests answered per id with the oldest in the
  singular slot, the method-first degrade split (experimental/unknown methods decline +
  degrade on the parent, known-method malformed shapes and boolean rpc ids still fail
  loud), the bounded pending map declining only the newest request, and the load-shed
  queue pins (delta flood sheds oldest deltas with structural completions surviving, the
  consumer-side notice mint, and the notice-before-close-sentinel ordering). Refreshed
  the import-block citations (cit:(["class CodexAppServerAdapter:", "class FakeCodexTransport:"], mcp/src/agents_remember/serving/codex_app_server_adapter.py:91-91; mcp/tests/test_codex_app_server_adapter.py:45-45)) and the per-test anchors. Verification metadata
  stays pinned — the change is uncommitted.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: created the sidecar for the new
  thread-demux incident-regression suite (R1; review R5 degrade/registry-eviction pins).
  Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
