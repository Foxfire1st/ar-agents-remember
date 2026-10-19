# mcp/src/agents_remember/canvas/sessions.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The host-created sessions one frame is served under, and their revocation. An origin string authenticates nothing, so a session is a host-created value bound to the exact frame, revision and comparison the bytes came from.

## Code Commentary

- `SessionRegistry.open` creates one session and reports the frames displaced to keep the active-frame ceiling; expiry is resolved on the way out.
- `revoke` and `revoke_frame` end one channel or every channel of a frame with a named reason, and the tombstone keeps the reason rather than the content.
- A request is compared to the recorded binding, never to the message's own claim about its origin.

## Evidence

- One session is created per frame and bound to frame, revision and comparison. [1]
- Revocation names its reason and keeps no content. [2]
