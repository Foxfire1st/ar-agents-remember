# dashboard/src/panels/review/canvas/canvasHooks.ts

## Governing Overview

[governing route overview](../../overview.md)

## Purpose

The panel's data hooks: reading one saved-first frame state, opening the explicit start, reading and sending the side conversation, and disposing a channel.

## Code Commentary

- `useCanvasFrame` reads the frame state for one target; nothing on the read path starts authoring.
- `CanvasChannel` and its key bind a live channel to the exact comparison, so a moved comparison does not reuse another channel's answer.
- A frame message is taken only when it arrives from the frame's own window, and it is bounded before it is serialized: `MAX_FORWARDED_MESSAGE_BYTES` (4096) per message, `MAX_FORWARD_IN_FLIGHT` (4) in flight and `MAX_FORWARD_IN_FLIGHT_BYTES` (8 KiB) in total. An oversized message, a burst past either ceiling and an unexpected shape are dropped with a named reason (`oversized`, `busy`) instead of being forwarded, so excess messages cost the panel nothing.
- An explicit start is a separate hook call; the panel issues it only from the Generate control.

## Evidence

- Reading a frame state starts nothing. [1]
- A live channel is keyed to its exact comparison. [2]

forwardedBody now admits one bounded array inside the envelope: at most 32 items, at most 64 total fields once an array is encountered, scalar leaves and no nested array or object inside an array item. Non-array envelopes retain their 16-field limit. Own data descriptors avoid executing accessors; depth, character and serialized-byte limits remain distinct. useCanvasMessages attaches the channel listener in a layout effect so it is installed before a mounted frame can post.

- forwardedBody now admits one bounded array inside the envelope: at most 32 items, at most 64 total fields once an array is encountered, scalar leaves and no nested array or object inside an array item. Non-array envelopes retain their 16-field limit. Own data descriptors avoid executing accessors; depth, character and serialized-byte limits remain distinct. useCanvasMessages attaches the channel listener in a layout effect so it is installed before a mounted frame can post. [3]
