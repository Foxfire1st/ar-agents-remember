# test_observer.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_observer.py`                     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-13T11:15+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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

| Finding | Source Path |
| --- | --- |
| The envelope under test. | [events.py](agents-remember/mcp/src/agents_remember/observer/events.py) |
| The id mint under test. | [ulid.py](agents-remember/mcp/src/agents_remember/observer/ulid.py) |
| The store under test. | [store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |

## Update History

- 2026-06-13T11:15+02:00: Created for slice 2a. Verification metadata is pinned
  until closeout stamps the 2a code commit.
