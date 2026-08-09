# mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T16:43+02:00 |
| lastVerifiedCommitHash |  `2dea095cd68454a7a68893e37c07dbd8daa86d32`|
| lastVerifiedCommitDate |  2026-08-09T18:00:39+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Owns parent native-history and live-evidence ingestion, source completeness, mapping, and
per-thread live/native twin suppression. It is also the shared fail-soft boundary for native-page
payloads whose transport envelope retains identity but whose body is truncated or schema-invalid.

## Code Commentary

### Logic

`NativeEvidenceIngestion` pages native history in 200-frame source windows and live evidence in
500-frame windows. It tracks native/evidence cursors, eviction floors, completion, and per-thread
live turn/request ids. Live evidence is mapped with explicit parent/child demux; malformed shapes
become safe unknown-vendor rows. Both the parent-history walk and eager native continuation route
through `map_native_frame`: truncation envelopes become bounded `<harness>:evidence-truncated` rows
and mapper `UnmappableShape` failures become `<harness>:malformed` rows. Those fallbacks deliberately
take `item_id`, `turn_id`, type, and timestamp from `NativeEvidenceFrame`, outside the damaged raw
body, so one oversized tool result cannot make the conversation rebuild fail or erase its native
identity. A later native walk suppresses only turns already proven to have crossed live, keeping
parent and child buckets independent.

An advancing Claude evidence eviction floor raises `ZipperEvidenceEvicted`; a backward evidence
tip raises `EvidenceTimelineRegressed`. Both express lost ordering proof rather than silently
continuing.

### Conventions

Native source reads are blocking and run through `asyncio.to_thread`. Unknown shapes preserve safe
evidence, never raw payloads. Harness mappers own valid payload interpretation; this ingestion
boundary owns identity-preserving degradation when exact interpretation is impossible.

### Invariants And Boundaries

- Parent and each child thread use independent twin-suppression buckets.
- Hydration clears live buckets before walking prior native history.
- Source cursor progress is retained only for the active projector generation.
- Completeness remains parent-scoped; child hydration cannot widen it.
- Native-page degradation must always key the visible row by `NativeEvidenceFrame.native_id`; it
  must never attempt to recover an id from a clipped `preview` or invent one from payload content.
- A malformed or truncated frame must not abort the remaining page or the conversation rebuild.

### Todos

The already-recorded mid-session fresh-projector overlap boundary remains a separate follow-up if
captured on a live reconnect.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Harness-specific mapping contracts. | `projector_for` | mcp/src/agents_remember/serving/conversation/projectors/__init__.py:120-121 |
| Project-once and ordering regressions. | `test_settled_live_turns_project_once_when_native_ids_disjoint` | mcp/tests/test_conversation_active_service.py:320-405 |
| Native truncation and malformed-shape regressions preserve Codex and Pi transport identity through both native ingestion modes. | `NativeFrameIdentityFallbackTests` | mcp/tests/test_conversation_native_ingestion.py:49-107 |

## Cross-Repo References

No meaningful cross-repository references found.

## 260731-EFA-L2 Current Delta

The constructor is now `NativeEvidenceIngestion(spine, readers)`: identity, controlled session,
mapper, mutation stream, agent authority and evidence refs come from the one
`SessionProjectionSpine`, and both the evidence reader and the native-page reader come from the one
`BridgeReaders` set (see [wiring.py](wiring.py.md)). Substituting a single reader is exactly the
mistake the set exists to prevent — a faked evidence reader beside a live transcript reader is
reading two different sessions. Watermark, completeness, mapping and live/native dedupe behaviour
are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History
- 2026-08-09T16:43+02:00 — 260713-TES-L5 hotfix curator: documented the shared native-page
  fail-soft boundary. Truncated and schema-invalid Codex/Pi payloads now retain the transport-owned
  native item and parent ids and degrade to bounded unknown-vendor rows instead of killing rebuild.
  Verification metadata remains pinned to the pre-commit source history until closeout.

- 2026-08-03T03:01:58+02:00 — W3-B05 curator: resolved 2 Tier-2 table findings with exact anchors and source paths; fixer generated all final ranges.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: constructor now takes `SessionProjectionSpine` + `BridgeReaders`.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the native-ingestion
  sidecar while preserving the monolith's source-order and twin-suppression boundaries.
  Verification metadata remains blank until commit.
