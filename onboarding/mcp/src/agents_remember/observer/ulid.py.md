# mcp/src/agents_remember/observer/ulid.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/ulid.py`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-13T11:15+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                     |

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
- A dependency-free local mint by design (stdlib `uuid.uuid7` would supersede it
  once the Python floor reaches 3.14; keeping minting in one module makes that a
  one-function swap).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Events carry a ULID `id`. | `id` | mcp/src/agents_remember/observer/events.py:54-54 |

## Update History

- 2026-06-13T11:15+02:00: Created for slice 2a. Verification metadata is pinned
  until closeout stamps the 2a code commit.
