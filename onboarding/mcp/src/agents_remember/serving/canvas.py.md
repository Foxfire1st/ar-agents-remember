# mcp/src/agents_remember/serving/canvas.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The generated page's host and the presenter's start/session surface. The frame route serves one admitted revision's own bytes and nothing else; the trusted API route serves the panel's saved-first view and is the only place an explicit start exists.

## Code Commentary

- `page` serves the one document a live session may load, with its policy headers; `page_asset` serves one asset of that same revision and nothing else.
- `open_session` opens a frame for viewing with a fresh bound session; `session_message` validates a host-protocol request against that session before it is applied.
- `generate` is the one explicit authoring start; `frame_state`, `attempt_operation` and `revoke_session` are the trusted read, operation and disposal surface.
- `register_canvas_routes` registers both surfaces after the API routes and before the static mount.

## Evidence

- The frame route serves one live session's own document and admitted assets. [1]
- An explicit start is the only path that begins authoring. [2]
- A frame message is bound, bounded and refused by name before it is applied. [3]
- Both surfaces are registered before the static mount. [4]
