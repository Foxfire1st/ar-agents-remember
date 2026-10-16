# mcp/src/agents_remember/observer/ulid.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`ulid.py` mints ULIDs for observer event ids: 48 bits of
millisecond timestamp + 80 bits of randomness, rendered as 26 Crockford Base32
characters, so the strings sort lexicographically by creation time.

## Code Commentary

`new_ulid()` builds `(millis << 80) | os.urandom(10)` and Crockford-encodes the
128-bit value most-significant-char-first. `now_ms` overrides the clock for
deterministic tests. `_CROCKFORD` is the ambiguity-free alphabet (digits +
uppercase minus I, L, O, U).

## Invariants And Boundaries

- **Stateless and concurrent:** request threads can call `new_ulid` without a mint lock. Within one millisecond two IDs have no ordering guarantee; JSONL append order orders the feed, while the ULID supplies a merge/unique key. There is no lifecycle-heartbeat caller contract.
- Mint-and-compare only: IDs are never parsed back.
- The dependency-free local mint owns the stable format across Python upgrades.

## Evidence

### Repo-Internal References

- Events carry a ULID `id`. [1]
