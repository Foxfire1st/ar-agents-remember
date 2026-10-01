# mcp/src/agents_remember/serving/pi_rpc_events.py

## Governing Overview
[serving/ overview](overview.md)

## Purpose
Maps documented Pi RPC frames into the normalized L1 adapter event and snapshot vocabulary while
retaining bounded dialogs and transcript entries. 260718-CHATS-L0E forwards full native frames
under the reserved `arEvidence` key into the bridge evidence buffer. 260718-CHATS-L2E lets a
content-less `message_end` — the abort's own native shape — cross as evidence-only instead of
failing the bridge.

## Code Commentary
`PiRpcEventMapper` applies `get_state` activity, translates start/end/retry/compaction/queue/
message/extension frames, and only emits terminal completion after `agent_settled` is corroborated
by an idle state. Dialog methods become durable pending interactions; fire-and-forget UI methods
become notices. Event/transcript sequences, raw Pi detail, and bounded interaction retention are
maintained locally.

L0E's optional `evidence` parameter on `_next_event` places the full native frame under the
reserved `arEvidence` raw key at two sites: `message_end` (the complete frame with native message
identity, beside the byte-identical flattened transcript entry) and the `pi:<type>` fallback
(message_update text/thinking/tool-call deltas, tool execution lifecycle, and unknown events, whose
raw crosses with semantics never guessed). The status-quo `piEvent` key keeps its exact current
shape for snapshot consumers; only the bridge sees and diverts the reserved key.

L2E relaxes exactly one raise class at `_message_end`: the role check (`user`/`assistant`) now
precedes the text extraction, and a valid-role message whose content carries no text/thinking
block — the shape an interrupted assistant turn ends with — crosses as an evidence-only
`pi:message_end` event with no transcript entry and no bridge failure. Non-dict `message` and bad
roles still fail the bridge with the exact reason; no fake empty entry is minted (the pi
projector mints terminal items from durable entries, so the suppressed entry starves nothing).

## Invariants And Boundaries
- Event raw evidence records the structured Pi protocol and cursor without fabricating a package
  version. Mapping remains responsible only for normalized state/events, not compatibility guesses.
- Retry and compaction remain settling; `agent_end` is not sufficient for terminal idle.
- Dialog responses are correlated; fire-and-forget UI events do not solicit responses.
- The `piEvent` raw key stays byte-identical; full frames ride only the reserved `arEvidence` key,
  which the bridge diverts before any projection.
- A content-less `message_end` crosses as evidence-only only when the role is valid and no
  text/thinking content exists; non-dict messages and bad roles still fail the bridge, and no fake
  transcript entry is ever minted.
- Mapping does not launch processes, reconnect sessions, or register vendors.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References
- Pi frame schemas and UI policy. [1]
- Adapter event-stream owner. [2]
- Event/settlement coverage. [3]
- Valid-role contentless message_end frames cross as evidence without fabricated transcript text. [4]


### Cross-Repo References
No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Submission Authority Delta

Pi event translation attaches the exact operation ref. Completion requires the settled event plus a
fresh idle observation for the same generation/activity token; `agent_end` or queue depth zero alone
is insufficient and stale events cannot release the successor.

## 260731-EFA-L2 Current Delta

**`EventPayload`** (`snapshot`, `transcript`, `operation`, `evidence`; module constant
`EMPTY_EVENT_PAYLOAD`) replaces the four independently-defaulted switches an adapter event used to
carry: what one event carries besides its kind and raw frame. An event may republish the snapshot,
append transcript entries, name the operation it settles and carry the full frame as evidence —
each combination belongs to a specific kind of frame, so it is chosen **once** as a payload rather
than as four separate arguments. The emitted events are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
