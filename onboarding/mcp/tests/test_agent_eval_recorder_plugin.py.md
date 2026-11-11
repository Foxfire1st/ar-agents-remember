# mcp/tests/test_agent_eval_recorder_plugin.py

## Governing Overview

[overview](overview.md)

## Purpose

The test runs the agent-eval recorder plugin in Node against the pinned Paseo hook shape and proves that it records a native seat's helper rows and its ended turn, read through `agents.ref(id).timeline.refetch` because the turn-ended hook carries an empty timeline.

## Code Commentary

`RECORDER_DRIVER` is a Node module that imports the plugin, registers its `agent.open.before` and `agent.turn.after` handlers through a fake `server.addHook`, refuses any subscription other than `agent.provider_subagents.update` without notifications, and feeds one helper upsert and its removal. It then ends the turn with an empty `timeline` and answers the refetch only for the owning agent with `direction: "tail"` and `limit: 0`.

The test needs `node` on the path and runs the plugin source with `--experimental-strip-types`. It requires three rows in `host-events.jsonl`, the first naming the helper, and a complete observed window. Merging those rows into a native capture leaves no unknowns, and the last event carries the ended turn's `turnId` and the refetched entries with their `turnId`. Writing an error into the window marker makes the same window incomplete.

## Relationships

The plugin under test is `scripts/agent_evals/adapters/recorder_plugin/index.server.ts`. The case reads its output with `host_window` and `merge_host_events` from `scripts/agent_evals/adapters` and borrows `_TrialSources` from `test_agent_eval_adapters.py`.

## Evidence

- The driver registers the plugin's open and turn-ended handlers through `addHook`. [1]
- The turn-ended event carries an empty timeline and the turn is read through a whole-tail refetch. [2]
- The plugin source runs in Node with type stripping. [3]
- Three host-event rows are written, the first for the helper, and the window is complete. [4]
- The merged capture has no unknowns and its last event holds the refetched turn. [5]
- A recorded subscription error makes the window incomplete. [6]
