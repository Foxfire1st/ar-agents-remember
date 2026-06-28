# test_setup_progress.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_setup_progress.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

Unit coverage for `providers/setup_progress.py` (GitHub #53): the durable
phase-progress file and its status projections.

## Code Commentary

### Logic

A `ManualClock` injects deterministic time; the `progress_file` helper builds
`SetupProgressFile` with a 3600s heartbeat interval so the ticker thread stays
quiet and tests observe only explicit event writes. Coverage: the event
lifecycle (initial running state, identity fields, completed-phase records
with note/ok/skipped/reason), `seedFallback` recorded the moment the fallback
phase starts, `phase_update` metrics attaching only to a live phase, `finish`
terminal state/error/summary, write errors never raising (a directory squats
on the file path), and the no-op `SetupProgress` accepting all events.
Projection tests: reader rejection of missing/invalid/foreign-schema files,
the running projection (heartbeat age, current-phase elapsed, seedFallback,
compact completed lines), stale at `STALE_AFTER_SECONDS`+1, failed projection
with `failedPhases` lines, and skipped phases not counting as failed.

### Invariants And Boundaries

- Tests are side-effect free (temp dirs, no Docker/network) and never rely on
  wall-clock sleeps — time moves only through the manual clock.
- The stale threshold is pinned via the exported `STALE_AFTER_SECONDS`, not a
  literal.

## Docs References

No external documentation is needed for these standard-library unit tests.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Module under test. | [setup_progress.py](agents-remember/mcp/src/agents_remember/providers/setup_progress.py) |

## Update History

- 2026-06-10T07:30+02:00 — Created with the GitHub #53 progress infrastructure.
