# mcp/src/agents_remember/canvas/document.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Delivers the channel binding to the admitted document itself, never to a navigated window. The bootstrap runs before generated scripts; leaving the document announces revocation even when navigation happens while parsing.

## Code Commentary

- `bound_document` injects a bootstrap that delivers the binding as a synthetic local `message` event on the document's own window at `DOMContentLoaded`, so the admitted document receives it after its own listeners exist and a page cannot inherit a binding it navigated away from; the `MessageChannel` it opens is a liveness path rather than the binding's carrier — `port2` is transferred to the parent and `port1` echoes whatever arrives, which is the challenge answer the panel waits 250 ms for.
- Departure is announced on pagehide, which is what lets the panel revoke a channel whose document left before its first load event.
- Navigation remains a browser capability; this module reports the departure rather than claiming to prevent it.

The bootstrap also injects `kit_protocol_helper_js` before dispatching the document’s binding. The helper accepts only this host/session/revision/comparison’s stale-part notices and emits bounded selection or explanation requests; it does not widen the document channel’s authority.

## Evidence

- The binding is delivered to the admitted document after its listeners exist. [1]
- The bootstrap posts `entered` to the parent with the session and transfers the echo port, and posts `departed` on `pagehide`, so leaving is announced even when navigation happens during parsing; the host revokes on that notice, and a missing echo or a second entry is a channel it will not use. [2]

- The current implementation injects the shared kit protocol helper; the admitted-document, departure and echo-channel statements remain valid. [3]
