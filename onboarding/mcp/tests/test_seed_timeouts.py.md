# mcp/tests/test_seed_timeouts.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_seed_timeouts.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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
clock, and a nonzero exit is reported (not treated as a stall). The tuning
travels as one `grepai_seed._StallWatchdog(progress=..., stall_seconds=...,
poll_seconds=...)` passed positionally right after the command, with `cwd`
and the pipe handles still loose keywords. Clone
integration tests mock the watchdog to verify structured phase-named `stalled`
results (`dump`/`restore`), the `seed_stall_seconds` override, and that **no
total-time cap reaches the subprocesses** — the watchdog is the only bound.
Marker tests drive `grepai_scan_state_from_log` with real watcher log shapes.

### Invariants And Boundaries

- The no-total-cap assertion is the contract from the 2026-06-10 design
  review: clone duration scales with index size by design; only silence
  (zero progress for the stall window) may kill it. It is proven as
  `assertNotIn("timeout", call.kwargs)` plus
  `call.args[1].stall_seconds == GREPAI_CLONE_STALL_SECONDS` — the cap is read off the
  `_StallWatchdog` object, not off a loose kwarg.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The watchdog and clone under test. | `_StallWatchdog`; `_run_with_stall_watchdog`; `_clone_database`; `GrepaiCloneContext` | mcp/src/agents_remember/providers/grepai/seed.py:38-52; mcp/src/agents_remember/providers/grepai/seed.py:266-310; mcp/src/agents_remember/providers/grepai/seed.py:313-324; mcp/src/agents_remember/providers/grepai/seed.py:327-379 |
| The scan-marker parser under test. | `grepai_scan_state_from_log`; `GREPAI_SCAN_PROGRESS_MARKERS`; `GREPAI_SCAN_COMPLETE_MARKER` | mcp/src/agents_remember/providers/grepai/lifecycle/runner.py:77-78; mcp/src/agents_remember/providers/grepai/lifecycle/runner.py:137-142 |

## Update History

- 2026-08-03T11:20+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 4 assigned citation findings (2 missing anchors and 2 malformed sources); final scoped check is clean.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep.
  `_run_with_stall_watchdog` now takes its `progress`/`stall_seconds`/`poll_seconds` trio as a
  single `_StallWatchdog` passed positionally after the command, which changed all four
  `StallWatchdogTests` call sites and, more substantively, the clone-cap assertion in
  `GrepaiCloneStallTests`: it reads `call.args[1].stall_seconds` where it used to read
  `call.kwargs.get("stall_seconds")`. Recorded `_StallWatchdog` in the Logic paragraph and spelled
  out both halves of the no-total-cap proof in Invariants so the contract is tied to the assertion
  that actually carries it. The tested behavior — completion, kill-on-silence, progress resetting
  the clock, nonzero exit reported, and no `timeout` kwarg reaching a subprocess — is unchanged.
- 2026-06-10T05:30+02:00: Created with the S2 stall watchdog and S3 GrepAI parity (2.5.1).
