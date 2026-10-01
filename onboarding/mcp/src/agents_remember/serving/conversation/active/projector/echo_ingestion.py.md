# mcp/src/agents_remember/serving/conversation/active/projector/echo_ingestion.py

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

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Claude echo mapping. [1]


### Cross-Repo References

No meaningful cross-repository references found.

## 260731-EFA-L2 Current Delta

The constructor is now `EchoIngestion(spine, readers)` — the shared machinery arrives as one
`SessionProjectionSpine` and the transcript reader as part of the one substitutable `BridgeReaders`
set (see [wiring.py](wiring.py.md)). The drain loop was split into `_zip_entry` (advance one
transcript entry against the pending frames) and `_drain_one_turn_body` (close one open turn and
flush its buffered frames); the zip/turn semantics themselves are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
