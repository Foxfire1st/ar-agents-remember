# scripts/agent_evals/adapters/recorder_plugin/index.server.ts

## Governing Overview

[governing overview](../../overview.md)

## Purpose

Records exact-owner native helper updates and turn-end events for a fixture host.

## Code Commentary

The recorder registers through `server.addHook` (`agent.open.before` and `agent.turn.after`). The pinned Paseo 0.16.2 SDK does not provide turn history on the event. The server includes an empty wire timeline for compatibility. The recorder reads the agent's whole held timeline through `agents.ref(id).timeline.refetch` with `direction: "tail"` and `limit: 0`. It records each returned item with its row's turn id when present.

### Invariants And Boundaries

Readiness and recording-window markers distinguish subscription snapshots from actual events. Restarts and errors invalidate the window; plugin code alone proves no loaded recorder or captured event.

## Evidence

- The recorder registers the native hooks and refetches the exact owner's timeline for its recorded turn-ended event. [1]

- In the 0.16.2 distribution, `plugins/runtime.js` applies `wireEvent` at 375 and adds the empty compatibility timeline at 1152–1155. `plugins/plugin-process.js:535` passes the input to the hook. [2]
- The 0.16.2 SDK declares the turn-end event at `dist/server/lifecycle.d.ts:107–117` without timeline history. [3]
