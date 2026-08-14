# mcp/tests/test_codex_adapter_thread_routing_and_registry.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/tests/test_codex_adapter_thread_routing_and_registry.py` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-07-31T15:32+02:00                                       |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                   |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

What the Codex adapter does with frames **it did not initiate**, and with **partial collab
shapes**. Three seams meet here, and each decides something the seat cannot recover from if
it is wrong.

## The Three Seams

**`turn/start` params decide what the vendor is told about policies it would otherwise
keep.** `test_turn_start_sends_only_the_policies_the_seat_configured`: an unset policy is
**omitted entirely**; sending `null` would tell the server to clear what the thread was
started with. A configured mapping rides as plain JSON data.

**`turn/started` and `thread/settings/updated` decide whether a frame is the *seat's* state
or a sub-agent's evidence** — the same wire shape means opposite things depending on its
`threadId`.

- `test_a_turn_the_seat_did_not_dispatch_still_makes_it_busy` — the human at the terminal
  can start a turn the bridge never wrote, and a resumed thread can already be mid-turn. The
  seat has to read as running from that notification **alone**.
- `test_a_sub_agents_settings_frame_is_evidence_not_the_seats_settings` — routed by thread,
  a sub-agent's frame crosses as raw evidence and the seat keeps the selection it
  deliberately made; the same frame on the seat's own thread is authoritative.

**Collab items arrive partially populated in the wild**, so each field must bind on its own
without the missing ones discarding what is already known.

- `test_sub_agent_activity_binds_only_the_facets_it_carries` — the vendor's own struct
  requires all four fields, so anything short of that is a shape this adapter must **survive
  rather than trust**. Losing a bound `agentPath` because a later frame omitted it would
  rename a live agent.
- `test_collab_tool_call_registers_only_well_formed_receivers_and_states` —
  `receiverThreadIds` is *who the call is addressed to*, which is why it may create a
  registry entry. `agentsStates` is a *claim about* threads, so a status for a thread this
  connection has never seen may only update, never create.

## Method

`anyio`-driven (`pytest.mark.anyio`). `settled_evidence` waits for the raw-evidence event a
collab item produces before asserting: collab items have no transcript projection, so every
one crosses as exactly one `codex-notification`, and waiting for it is what makes the
registry assertions a statement about a **settled** frame rather than a race.

## Invariants And Boundaries

- Thread identity is the routing key. Never treat a frame's shape as evidence of whose state
  it describes.
- Partial vendor payloads enrich the registry; they never erase it.
- Registry creation is allowed only from an addressing field, never from a reported state.
- An unset policy is omitted from `turn/start`, never sent as `null`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The Codex app-server adapter, its thread demux and agent registry. | "class CodexAppServerAdapter:"; "self._threads = CodexThreadRegistry(" | mcp/src/agents_remember/serving/codex_app_server_adapter.py:91-1115; mcp/src/agents_remember/serving/codex_app_server_threads.py:69-300 |
| The demux suite this module extends. | "test_spawned_subagent_traffic_never_fails_the_bridge" | mcp/tests/test_codex_adapter_thread_demux.py:118-158 |
| The sub-agent projector whose roster these registry bindings feed. | "class CodexAgentEngineTests1(unittest.IsolatedAsyncioTestCase):" | mcp/tests/test_conversation_projector_codex_agents_engine_1.py:97-97 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T11:15+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 6 assigned citation findings (3 missing anchors and 3 malformed sources); final scoped check is clean.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new Codex
  thread-routing / registry-binding suite. Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
