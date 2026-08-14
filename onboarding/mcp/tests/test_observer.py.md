# test_observer.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_observer.py`                     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-13T11:15+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_observer.py` covers the observer write-side substrate (slice 2a): ULID
minting, the `ar-observer-event/v1` envelope, and the append-only `EventStore`.

## Code Commentary

### Logic

`UlidTests` assert a minted id is 26 Crockford chars, that a larger `now_ms`
sorts lexicographically after a smaller one, and that 2,000 ids in one
millisecond are unique. `EventEnvelopeTests` assert camelCase wire keys
(`schema`/`lifecycleId`/`repoId`), a dump→`model_validate_json` round-trip,
omission of `None` optionals, Literal rejection of bad `trust`/`actor`, and that
`extra="forbid"` rejects unknown fields. `EventStoreTests` assert per-lifecycle
vs workspace path routing, a store round-trip where a self-contained
`lifecycle.started` replays from its log alone, and that reading an absent log is
empty.

### Conventions

The module inserts `mcp/src` on `sys.path` (the test-suite idiom) before
importing `agents_remember.observer`. `EventStore` is exercised against a
`tempfile.TemporaryDirectory`. Events are constructed with camelCase field names
(`lifecycleId=`), matching the envelope.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The envelope under test. | `Event` | mcp/src/agents_remember/observer/events.py:39-64 |
| The id mint under test. | `new_ulid` | mcp/src/agents_remember/observer/ulid.py:30-41 |
| The store under test. | `EventStore` | mcp/src/agents_remember/observer/store.py:103-171 |

## Update History

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 3 citation items; scoped citation check now passes.

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_observer.py` since
  the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s)
  with no token change whatsoever. Checked by parsing both revisions and comparing the abstract
  syntax trees (identical) and the comment tokens (identical), so no symbol, signature, default,
  decorator, control-flow branch, docstring, or assertion this card describes has moved, and every
  claim this card makes about its own source still holds.

- 2026-06-13T11:15+02:00: Created for slice 2a. Verification metadata is pinned
  until closeout stamps the 2a code commit.
