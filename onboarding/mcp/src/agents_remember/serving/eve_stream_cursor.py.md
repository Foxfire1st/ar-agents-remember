# mcp/src/agents_remember/serving/eve_stream_cursor.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Incremental NDJSON decoding for one eve stream connection: bytes in, complete `EveStreamEvent`
frames out, with the **absolute event index derived here** rather than read from any field the
server sends. A caller that persists `next_index` can resume with zero gap and zero duplicate.

The index is computed locally on purpose. eve's envelope carries a stable `meta.id` but no sortable
position, so a reader that trusts a server field for ordering has no defence against the one failure
this adapter cannot repair after the fact.

## Code Commentary

### Logic

`EveNdjsonDecoder` holds a byte buffer and a `_index`. `feed(chunk)` appends the chunk, splits on
newlines while one is present, and decodes each completed line; `finish()` decodes a trailing frame
that arrived without its newline and resets the buffer. `next_index` is the absolute index the next
decoded frame will carry.

`_decode` is where the two rules that protect the cursor live:

- a blank line (eve may keep the connection open with keep-alive blanks) returns `None` and
  **consumes no index**, because advancing on a blank line would drift the persisted cursor away from
  the durable record;
- a frame longer than `max_frame_bytes` (default `DEFAULT_MAX_FRAME_BYTES`, 1 MiB) raises rather than
  buffering without bound.

`feed` also refuses early when the buffer exceeds the ceiling with no newline in it, so an unbounded
frame is caught before it is fully accumulated. `join_frame_text` concatenates one delta field across
events in stream order.

### Conventions

- A non-UTF-8 or malformed frame surfaces as the `HarnessControlError` raised by
  `eve_protocol.parse_event_frame`, not as a decoder-specific error.
- The index is incremented exactly once per decoded frame, after the frame parsed successfully.
- `finish()` is idempotent in effect: it clears the buffer, so a second call yields nothing.

### Invariants And Boundaries

- **The decoder owns the index; the server does not supply it.** No server field is consulted for
  ordering.
- A blank or whitespace-only line never consumes an index.
- The frame ceiling is a refusal, not a truncation: an oversized frame raises and the stream is not
  silently continued past it.
- This module decodes framing and nothing else. It does not deduplicate, translate, or decide
  acceptance; replay protection belongs to the adapter's single `EveEventDeduplicator`, declared in
  the protocol module.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available. NDJSON framing is a generic newline-delimited-JSON convention, not a
repo-specific external contract.

No configured `Domain Documentation` source; NDJSON line framing needs no external citation beyond the eve wire contract cited below.

### Repo-Internal References

- The decoder delegates every frame to the protocol module's schema-exact parser and inherits its refusals. [1]
- Replay protection is not this module's and now has exactly one owner beside the wire contract. [2]
- One stream connection in the transport client feeds this decoder and reconnects from the index the caller persisted. [3]
- The adapter persists the advanced index and uses it as the only resume position. [4]
- Cursor-arithmetic cases cover a frame split across reads, keep-alive blanks, a trailing frame without a newline, and the oversized-frame refusal. [5]

### Cross-Repo References

- The durable NDJSON record and its absolute event-index semantics are eve's published stream contract at the pinned release. [6]
