# mcp/src/agents_remember/observer/timeutil.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/timeutil.py`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-13T19:30+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

`timeutil.py` is the observer substrate's shared time leaf: the one definition of
"age a stamp against a clock" and the timing thresholds that the write side
(`ambient`) and the read side (`reducer`) both depend on, so the two can never
drift apart on duplicate copies (slice 3a).

## Code Commentary

`age_seconds(stamp, now)` parses an ISO-8601 `stamp` with `datetime.fromisoformat`,
assumes UTC when the stamp is naive, and returns the seconds elapsed to `now`;
an unparseable stamp returns `None` rather than raising, so a hand-edited or
legacy log degrades gracefully instead of crashing the projection.

`Clock = Callable[[], datetime]` is the injectable now-source: passing it at the
edges keeps a reduction a pure function of `(events, snapshots, now)` and the
tests deterministic.

The timing thresholds live here because they are shared across the write/read
split: `HEARTBEAT_SECONDS = 15.0` (the ticker cadence, mirroring
`setup_progress`), `STALE_AFTER_SECONDS = 180.0` (the projection's
paused-by-dormancy threshold), and `TTL_SECONDS = 3600.0` (the fleeting-only
abandon TTL). `ambient` imports `HEARTBEAT_SECONDS`/`TTL_SECONDS`; `reducer`
imports `STALE_AFTER_SECONDS`/`TTL_SECONDS`.

## Invariants And Boundaries

- **One definition, shared.** This module exists so the heartbeat ticker + TTL
  sweep (write) and the paused/abandoned inference (read) agree by construction.
- `providers.setup_progress` keeps its *own* `_age_seconds` and
  `STALE_AFTER_SECONDS` (90.0): it predates the observer package and is a
  provider-layer concern, deliberately not consolidated here.
- Pure: no I/O, no package-internal imports beyond the standard library.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The write side that imports the cadence + TTL and ages the last heartbeat. | [ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The read side that imports the stale/TTL thresholds for the inferred layer. | [reducer.py](agents-remember/mcp/src/agents_remember/observer/reducer.py) |
| The provider-layer heartbeat/stale idiom with its own separate copy. | [providers/setup_progress.py](agents-remember/mcp/src/agents_remember/providers/setup_progress.py) |
| The design that assigns these defaults (§1.5-1.6, §8). | [docs/design/observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |

## Update History

- 2026-06-13T19:30+02:00: Created for slice 3a — the shared time leaf
  (`age_seconds`, `Clock`) and the relocated timing thresholds
  (`HEARTBEAT_SECONDS`/`STALE_AFTER_SECONDS`/`TTL_SECONDS`, moved out of
  `ambient` so the read side shares one definition). Verification metadata is
  pinned until closeout stamps the 3a code commit.
