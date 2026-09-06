# mcp/src/agents_remember/serving/conversation/active/projector/echo_ingestion.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/echo_ingestion.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Owns the Claude transcript-submission echo and live-evidence zipper.

## Code Commentary

### Logic

Evidence frames queue until `poll` can place them around retained transcript entries in exact
turn order. Only transcript rows with `role == "user"` become submission echoes; assistant and
result rows merely advance the transcript watermark. Initial hydration reads all retained
transcript pages and, when evidence has already evicted, realigns orphan echoes and surviving
turn bodies without timestamp guesses.

### Conventions

The transcript is an echo channel, not history authority. Off-shape echoes degrade to a safe
unknown-vendor row.

### Invariants And Boundaries

- A user echo precedes the evidence body it opened.
- A result closes the current turn before the next echo.
- Non-user transcript rows never mint user or unknown-vendor items.
- Release drops pending zipper frames when the projector retires.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Claude echo mapping. | `map_transcript_echo` | mcp/src/agents_remember/serving/conversation/projectors/claude.py:621-662 |


## Cross-Repo References

No meaningful cross-repository references found.

## 260731-EFA-L2 Current Delta

The constructor is now `EchoIngestion(spine, readers)` — the shared machinery arrives as one
`SessionProjectionSpine` and the transcript reader as part of the one substitutable `BridgeReaders`
set (see [wiring.py](wiring.py.md)). The drain loop was split into `_zip_entry` (advance one
transcript entry against the pending frames) and `_drain_one_turn_body` (close one open turn and
flush its buffered frames); the zip/turn semantics themselves are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 4 citation findings (2 rows); scoped recheck clean.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: constructor now takes `SessionProjectionSpine` + `BridgeReaders`; drain loop split into `_zip_entry` / `_drain_one_turn_body`.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the Claude
  echo-zipper sidecar after projector decomposition. Verification metadata remains blank until
  commit.
