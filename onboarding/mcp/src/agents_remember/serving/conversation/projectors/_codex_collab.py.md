# mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

Codex sub-agent collab and agent-thread mapping. The app-server auto-attaches sub-agent thread listeners to the seat connection, so one evidence stream carries many threads demuxed by ``threadId``. This module owns the roster upserts, collab tool calls, agent-thread lifecycle notifications, and the turn/completed outcome mapping; the frame router lives in :mod:`agents_remember.serving.conversat...

## Code Commentary

- `_LiveItemContext`
- `ItemPlacement`
- `_roster_item`
- `_collab_status`
- `_collab_final_message`
- `_CollabCall`
- `_collab_receiver_ids`
- `_collab_call_shape`
- `_collab_call_input_block`
- `_collab_call_agent`
- `_collab_roster_ids`
- `_collab_roster_upserts`
- `_map_collab_tool_call`
- `_map_sub_agent_activity`
- `_map_thread_started`
- `_agent_notification_thread_id`
- `_map_agent_thread_status`
- `_map_agent_turn_started`
- `_map_agent_turn_completed`
- `_map_turn_completed`
- `_tool_phase`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py`.

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.
