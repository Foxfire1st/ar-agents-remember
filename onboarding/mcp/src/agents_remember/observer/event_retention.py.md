# mcp/src/agents_remember/observer/event_retention.py

## Governing Overview

[observer overview](overview.md)

## Purpose

Workspace River retention owns recent-hour fresh replay and byte admission, not session inactivity or lifecycle deletion.

## Code Commentary

### Workspace compaction and admission

`compact_workspace_river` cuts old/oversize prefixes under the common River lock and advances virtual baseOffset. Serving age compaction remains sixty-second paced. Every append checks the 16 MiB ceiling and trims toward 8 MiB; a row still unable to fit is refused and counted by its caller. This lock is not crash-atomic across separate cursor/event files.

Fresh offsets are workspace base plus `_first_retained_offset`’s recent-hour physical start. Only provably old timestamps are skipped; malformed rows are ignored and trailing partial lines wait. No session dormancy, heartbeat sidecar, series exemption or lifecycle directory deletion remains.

## Evidence

### Docs References

No relevant external documentation was found after checking the in-repo design docs.
This file implements repository-local dashboard retention policy.

No relevant external documentation found after checking in-repo design docs for raw dashboard retention mechanics.

### Repo-Internal References

Fresh offsets and compaction retain the bounded workspace River.


- `initial_event_offsets` gives a fresh `/api/events` connection the workspace river's start: the stored virtual base plus the first row still inside the replay TTL. The river is also cut by size on admission — a ceiling and a trim level — so the retained window is bounded by age and bytes. [1]

- Unparseable timestamps are retained rather than guessed old. [6]
