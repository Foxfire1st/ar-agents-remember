# mcp/src/agents_remember/observer/ulid.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`ulid.py` mints ULIDs for observer event and lifecycle ids: 48 bits of
millisecond timestamp + 80 bits of randomness, rendered as 26 Crockford Base32
characters, so the strings sort lexicographically by creation time.

## Code Commentary

`new_ulid()` builds `(millis << 80) | os.urandom(10)` and Crockford-encodes the
128-bit value most-significant-char-first. `now_ms` overrides the clock for
deterministic tests. `_CROCKFORD` is the ambiguity-free alphabet (digits +
uppercase minus I, L, O, U).

## Invariants And Boundaries

- **Stateless ⇒ thread-safe.** Called from both the request thread and (later)
  the lifecycle heartbeat thread; `os.urandom` / `time.time_ns` are thread-safe,
  so no lock is held. Within one millisecond two ids share no ordering guarantee
  — order *within* a lifecycle is the JSONL append order; the id is the
  cross-lifecycle merge / unique key.
- Mint-and-compare only: ids are never parsed back, so no decode path exists.
- A dependency-free local mint by design; the ULID format stays stable when the Python runtime is upgraded, and minting stays in one module.

## Evidence

### Repo-Internal References

- Events carry a ULID `id`. [1]
