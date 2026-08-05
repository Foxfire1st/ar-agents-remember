# test_setup_progress.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_setup_progress.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Module under test. | `SetupProgressFile` | mcp/src/agents_remember/providers/setup_progress.py:54-170 |

## Update History

- 2026-08-04T18:38+02:00 — 260731-EFA-L6 S18-B14 curator: repaired the citation row with the `SetupProgressFile` anchor and its ledger-verified class extent (54-84). Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_setup_progress.py`
  since the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 6
  line(s) with no token change whatsoever. Checked by parsing both revisions and comparing the
  abstract syntax trees (identical) and the comment tokens (identical), so no symbol, signature,
  default, decorator, control-flow branch, docstring, or assertion this card describes has moved,and every claim this card makes about its own source still holds.

- 2026-06-10T07:30+02:00 — Created with the GitHub #53 progress infrastructure.
