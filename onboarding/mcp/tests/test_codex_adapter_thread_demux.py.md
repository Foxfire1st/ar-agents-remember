# mcp/tests/test_codex_adapter_thread_demux.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_adapter_thread_demux.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:45+02:00 |
| lastVerifiedCommitHash |  `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f`|
| lastVerifiedCommitDate |  2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Thread-demux regression tests for multiplexed codex sub-agent traffic (R1).
The codex app-server auto-attaches sub-agent thread listeners to the seat's connection, so
one transport carries interleaved parent + sub-agent notifications and server requests;
before the demux the first foreign-thread notification failed the whole bridge (the
2026-07-24 production seat death). These tests pin the anti-death behavior.

## Code Commentary

### Logic

Eight async tests drive the real `CodexAppServerAdapter` over the shared
`FakeCodexTransport`/`prime_start` seam from `test_codex_app_server_adapter`, with wire
frames built by `_agent_wire_fixtures`:

- `test_spawned_subagent_traffic_never_fails_the_bridge` (L104-L166) — the incident shape:
  three sub-agents mid-turn, interleaved with parent traffic; parent busy semantics stay
  parent-scoped, off-wire partial deltas route through the item→thread index, and every
  agent thread lands in the registry with its own completed turns.
- `test_subagent_approval_is_multiplexed_and_answered_by_request_id` (L169-L209) — a
  sub-agent approval rides the plural `pending_interactions` (never the singular parent
  slot), is answered by JSON-RPC request-id, and a server-settled request clears per
  thread via `serverRequest/resolved`.
- `test_collab_items_bind_agent_identity_into_the_registry` (L212-L269) — parent-thread
  `collabAgentToolCall` and `subAgentActivity` evidence binds status/agentPath into the
  registry, and the bound identity becomes the agent label on multiplexed approvals.
- `test_unknown_item_delta_degrades_without_failing` (L272-L312) — an unbound partial
  delta crosses unmodified (no invented thread); a full-shape foreign-thread delta
  auto-registers its thread as `unresolved`.
- `test_read_native_page_reads_the_requested_agent_thread` (L315-L346) — native pages
  demux by `thread_id` (agent thread vs parent default).
- `test_malformed_agent_thread_frames_degrade_to_raw_evidence` (L349-L397, review R5) —
  agent-thread shape drift degrades to preserved raw evidence with a `degraded` reason;
  the bridge stays `ready`.
- `test_malformed_parent_frame_still_fails_loud` (L400-L414) — the same malformation on
  the PARENT thread still fails the bridge: parent-thread shapes stay load-bearing.
- `test_registry_full_degrades_and_settled_threads_evict` (L417-L457, review R5) — at
  `THREAD_REGISTRY_LIMIT` an unevictable registry degrades the overflow frame; a settled
  agent thread is evicted to make room for the next one.

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
| The shared fixture/transport seam (FakeCodexTransport, prime_start, launch, make_adapter) this suite reuses. | L41-L49 | [test_codex_app_server_adapter.py](agents-remember/mcp/tests/test_codex_app_server_adapter.py) |
| The vendored-shape builders the frames come from. | L17-L29 | [_agent_wire_fixtures.py](agents-remember/mcp/tests/_agent_wire_fixtures.py) |
| The demuxed adapter under test: thread registry, per-thread state, multiplexed pendings, native-page demux. | L30-L33 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| The snapshot/evidence models carrying the plural pending tuple and evidence key. | L35-L39 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |

## Cross-Repo References

The multiplexed traffic model (auto-attached sub-agent thread listeners on one connection)
is vendored codex app-server behavior; the fixture module pins each shape to its proving
file in the vendor checkout.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The live sub-agent spawn sequences (V1 collab / V2 subAgentActivity) the demux must survive. | L30-L32 of the fixture docstring | [codex app-server v2 turn_start suite](https://github.com/openai/codex/blob/main/codex-rs/app-server/tests/suite/v2/turn_start.rs) |

## Update History

- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: created the sidecar for the new
  thread-demux incident-regression suite (R1; review R5 degrade/registry-eviction pins).
  Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
