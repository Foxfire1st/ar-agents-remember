# mcp/tests/test_seed_timeouts.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_seed_timeouts.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00                     |
| lastVerifiedCommitHash | `642cca15f206cf8cf43ff7ffd6dadc5c27af2879`|
| lastVerifiedCommitDate | 2026-06-10T01:44:33+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

Tests that provider seed operations detect wedges without punishing index
size: the GrepAI clone's stall watchdog (`_run_with_stall_watchdog`) and the
scan-marker parser behind GrepAI indexing-state parity.

## Code Commentary

### Logic

Watchdog tests use real short-lived `sys.executable -c` subprocesses:
completion returns a `CompletedProcess`, a sleeping command with constant
progress is killed (returns `None`), advancing progress resets the stall
clock, and a nonzero exit is reported (not treated as a stall). Clone
integration tests mock the watchdog to verify structured phase-named `stalled`
results (`dump`/`restore`), the `seed_stall_seconds` override, and that **no
total-time cap reaches the subprocesses** — the watchdog is the only bound.
Marker tests drive `grepai_scan_state_from_log` with real watcher log shapes.

### Invariants And Boundaries

- The no-total-cap assertion is the contract from the 2026-06-10 design
  review: clone duration scales with index size by design; only silence
  (zero progress for the stall window) may kill it.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The watchdog and clone under test. | [seed.py](agents-remember/mcp/src/agents_remember/providers/grepai/seed.py) |
| The scan-marker parser under test. | [runner.py](agents-remember/mcp/src/agents_remember/providers/grepai/lifecycle/runner.py) |

## Update History

- 2026-06-10T05:30+02:00: Created with the S2 stall watchdog and S3 GrepAI parity (2.5.1).
