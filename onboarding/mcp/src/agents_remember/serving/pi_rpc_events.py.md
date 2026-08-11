# mcp/src/agents_remember/serving/pi_rpc_events.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_events.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References
| Finding | Anchor | Source |
| --- | --- | --- |
| Pi frame schemas and UI policy. | `PI_RPC_DIALOG_METHODS`, `PI_RPC_FIRE_AND_FORGET_METHODS`, `PiRpcJsonlDecoder` | mcp/src/agents_remember/serving/pi_rpc_protocol.py:20-23; mcp/src/agents_remember/serving/pi_rpc_protocol.py:59-103 |
| Adapter event-stream owner. | `PiRpcAdapter`, `_event_stream`, `subscribe` | mcp/src/agents_remember/serving/pi_rpc_adapter.py:94-768; mcp/src/agents_remember/serving/pi_rpc_adapter.py:268-305; mcp/src/agents_remember/serving/pi_rpc_adapter.py:307-308 |
| Event/settlement coverage. | `test_retry_compaction_and_agent_settled_are_not_early_idle`, `test_extension_ui_round_trip_and_reclamation_scale` | mcp/tests/test_pi_rpc_adapter_ops_2.py:79-110; mcp/tests/test_pi_rpc_adapter_ops_2.py:112-167 |
| The guarded abort whose interrupted turns produce the content-less `message_end` shape this mapper crosses evidence-only. | `message_end` | mcp/tests/test_harness_control_evidence_installed.py:352-355 |
| The control-plane contract test pins the evidence-only mapping and the preserved role/object strictness (bad role still fails the bridge). | `test_contentless_message_end_crosses_as_evidence_without_failing` | mcp/tests/test_harness_control_plane_assets.py:113-139 |

## Cross-Repo References
No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

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

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:59:59+02:00 — Curated 8 citation findings (4 table rows, 4 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `EventPayload` / `EMPTY_EVENT_PAYLOAD` as the per-frame event payload choice.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the content-less `message_end`
  relaxation — the abort's own native shape crosses as an evidence-only `pi:message_end` event
  with no transcript entry and no bridge failure; exactly one raise class is relaxed, the role
  check precedes the extraction, and role/object strictness is preserved (the reviewer's
  implementation-found substrate defect, accepted as deviation 1). Verification metadata stays
  pinned until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the reserved-key `arEvidence`
  forwarding at `message_end` and the `pi:<type>` fallback — full frames with native identity cross
  into the evidence buffer while `piEvent` stays byte-identical. Verification metadata stays
  pinned until closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: documented exact-ref event translation and fresh-idle terminal
  evidence.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: removed version fabrication from mapped Pi event evidence and
  documented the structured protocol boundary.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for normalized activity,
  queue, transcript, extension UI, retry/compaction, and settled completion mapping.
