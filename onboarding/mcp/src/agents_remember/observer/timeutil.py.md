# mcp/src/agents_remember/observer/timeutil.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/timeutil.py`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-13T19:30+02:00                           |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`       |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

`timeutil.py` provides the observer's injectable `Clock` type and shared time boundary. The current
age calculation lives with the observer control-plane stamp implementation, while heartbeat, stale,
and TTL thresholds are owned by their consuming layers rather than by this module.

## Code Commentary

`Clock = Callable[[], datetime]` is the injectable now-source: passing it at the
edges keeps a reduction a pure function of `(events, snapshots, now)` and the
tests deterministic. The `age_seconds` implementation is owned by the observer
control-plane stamp module. The heartbeat/stale/TTL constants are likewise read
from the producer and reducer layers that consume them.

## Invariants And Boundaries

- `Clock` is the shared injectable boundary; age calculation and threshold ownership
  remain with their respective observer control-plane and producer/consumer modules.
- `providers.setup_progress` keeps its *own* `_age_seconds` and
  `STALE_AFTER_SECONDS` (90.0): it predates the observer package and is a
  provider-layer concern, deliberately not consolidated here.
- Pure: no I/O, no package-internal imports beyond the standard library.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The write side imports the cadence and TTL, and `_inactive_seconds_locked` ages the last real non-heartbeat event. | "HEARTBEAT_SECONDS,"; "TTL_SECONDS,"; "def _inactive_seconds_locked"; "Seconds since the last real (non-heartbeat) event for the current lifecycle."; "age_seconds(last, self._clock())" | mcp/src/agents_remember/observer/ambient.py:53-54; mcp/src/agents_remember/observer/ambient.py:592-597 |
| The read side imports the stale/TTL thresholds for the inferred layer. | "STALE_AFTER_SECONDS, TTL_SECONDS" | mcp/src/agents_remember/observer/reducer.py:111-111 |
| The provider-layer heartbeat/stale idiom with its own separate copy. | `HEARTBEAT_SECONDS`; `STALE_AFTER_SECONDS`; `Clock` | mcp/src/agents_remember/providers/setup_progress.py:21-21; mcp/src/agents_remember/providers/setup_progress.py:25-25; mcp/src/agents_remember/providers/setup_progress.py:27-27 |
| The design sections describe lifecycle TTL/heartbeat semantics and defer implementation ownership. | `# Observable Lifecycle, Events, and Gates — the Agents Remember 3.0 Design`; `### 1.5 Fleeting vs persistent; save gate; TTL`; `### 1.6 Ambient attribution and the heartbeat`; `## 8. Deferred to Implementation Phases` | docs/design/observable-lifecycle.md:1-402 |

## Update History

- 2026-08-04T13:54+02:00 — 260731-EFA-L6 S18-B13 curator: corrected heartbeat-age semantics to the last real non-heartbeat event and reissued its whole-claim evidence for same-reviewer closure.

- 2026-08-03T10:25+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 8 assigned citation findings (4 missing anchors and 4 malformed sources); final scoped check is clean.

- 2026-06-13T19:30+02:00: Created for slice 3a — the shared time leaf
  (`age_seconds`, `Clock`) and the relocated timing thresholds
  (`HEARTBEAT_SECONDS`/`STALE_AFTER_SECONDS`/`TTL_SECONDS`, moved out of
  `ambient` so the read side shares one definition). Verification metadata is
  pinned until closeout stamps the 3a code commit.
