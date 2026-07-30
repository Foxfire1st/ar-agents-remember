# mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Owns parent native-history and live-evidence ingestion, source completeness, mapping, and
per-thread live/native twin suppression.

## Code Commentary

### Logic

`NativeEvidenceIngestion` pages native history in 200-frame source windows and live evidence in
500-frame windows. It tracks native/evidence cursors, eviction floors, completion, and per-thread
live turn/request ids. Live evidence is mapped with explicit parent/child demux; malformed shapes
become safe unknown-vendor rows. A later native walk suppresses only turns already proven to have
crossed live, keeping parent and child buckets independent.

An advancing Claude evidence eviction floor raises `ZipperEvidenceEvicted`; a backward evidence
tip raises `EvidenceTimelineRegressed`. Both express lost ordering proof rather than silently
continuing.

### Conventions

Native source reads are blocking and run through `asyncio.to_thread`. Unknown shapes preserve safe
evidence, never raw payloads.

### Invariants And Boundaries

- Parent and each child thread use independent twin-suppression buckets.
- Hydration clears live buckets before walking prior native history.
- Source cursor progress is retained only for the active projector generation.
- Completeness remains parent-scoped; child hydration cannot widen it.

### Todos

The already-recorded mid-session fresh-projector overlap boundary remains a separate follow-up if
captured on a live reconnect.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Harness-specific mapping contracts. | [projectors/](agents-remember/mcp/src/agents_remember/serving/conversation/projectors/) |
| Project-once and ordering regressions. | [test_conversation_active_service.py](agents-remember/mcp/tests/test_conversation_active_service.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the native-ingestion
  sidecar while preserving the monolith's source-order and twin-suppression boundaries.
  Verification metadata remains blank until commit.
