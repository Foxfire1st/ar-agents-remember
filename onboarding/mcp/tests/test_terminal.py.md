# test_terminal.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal.py`                     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-13T07:53+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb` |
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_terminal.py` covers the Mode B2 terminal host (slice 6d-1, `serving.terminal`):
tmux command construction, the session registry, and real-PTY write/read/resize/exit —
with the tmux integration path gated so CI without tmux still passes. The reopened-L6 pass injects a
recording `tmux_configurer` fake into the registry fixture and pins that `ensure` asserts session
options (mouse mode) after both the create and the idempotent already-exists paths and that every
`attach` re-asserts them against the durable session. The copy-mode escape suite
(`TerminalHostCopyModeCancelTests`, pipe-backed writes + a recording `tmux_mode_canceller` fake) pins
the scroll-then-type state machine: mouse-report-only frames pass through without cancelling, typing
without prior mouse never cancels, the first typed byte after mouse traffic cancels exactly once (and
still writes through), another scroll re-arms the cancel, and a mixed mouse+typing frame counts as
typing.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

The unit suite proves that the tmux client environment strips `TMUX`/`TMUX_PANE`, forces
`TERM=xterm-256color`, and preserves unrelated variables. A six-client matrix checks probe, kill,
detached create, mouse enable, copy-mode cancel, and pane-mode probe. The real tmux integration now
skips only when tmux itself is unavailable and runs ensure plus attach under a contaminated launcher
environment, reading output from the concrete attached PTY before closing it.

### Logic

`BuildCommandTests` assert the pure builders: `_build_tmux_command` emits
`tmux new-session -A -s <name> -c <cwd> -- <harness>`, and `_tmux_session_name`
collapses tmux-illegal chars (`.`/`:`) and falls back to `ar-session`.
`TerminalHostRegistryTests` drive a pipe-backed `_FakeSpawner` (a real master fd, no
child): open records the tmux argv + registers + correlates `lifecycle_id`
(`get`/`sessions`/`for_lifecycle`), open is idempotent for a live session and replaces a
dead one, `close` unregisters, an unknown sid raises `KeyError` on write/resize, and a
custom `name` overrides the derived one. The custom-name proof finds tmux's `-s`
option and asserts its following token rather than assuming a fixed argv slot, so the
same semantic assertion holds whether capability detection inserts the modern optional
`-T sync` frame or produces the older/unavailable-capability command shape. Task 22
extends these registry tests with injectable tmux
probe/kill fakes: `has_session` delegates to the probe, `terminate` kills the resolved tmux name and
unregisters the local session, terminating an unknown sid uses a supplied tmux name, and
`attach` creates unregistered per-connection clients that can be `close_session`ed without removing the
durable registry entry. The opener regression coverage adds an injectable tmux creator and asserts
`ensure` creates a detached tmux session without registering a client, while an already-present tmux
session makes `ensure` idempotent. Since L2 the fake `_create_tmux` creator gained the `env`
parameter (matching the `TmuxCreator` seam that now carries spawn env) and records `created_env`, so
the registry fixture is signature-compatible with the `tmux new-session -e KEY=VALUE` knob-injection
seam.
`TerminalHostPtyTests` (skipped without `cat`)
run the host against a **real kernel PTY** via `_raw_spawn` (which strips the tmux
wrapper): a `cat` write/read round-trip, an idle non-blocking read returning `b""`,
`resize` verified by reading the winsize back with `TIOCGWINSZ`, and (with `true`) an
empty read + dead `is_alive` after the child exits. `TerminalHostTmuxIntegrationTests`
(skipped without tmux) exercises the real default spawner end-to-end: a tmux-wrapped
`sh -c 'printf MARKER; sleep 2'` whose output is read back, proving the tmux client
attaches to the PTY. `test_spawn_seeds_default_winsize` (slice 6e-4) opens a real-PTY
`cat` session and reads back `TIOCGWINSZ` to assert the seeded **24×80** default, so tmux
never starts at 0×0 before the first browser resize lands. The tmux integration skip also
requires the current `TERM` to expose a terminfo `clear` capability; noninteractive push hooks
often run with `TERM=dumb`, where tmux itself fails before launching the child. The 6f-hardening cases assert
the **Ctrl-Z (`0x1a`) suspend strip is scoped**: the real-PTY tests cover a harness session
(`suspend_unsafe=True`) dropping `0x1a`, and `TerminalHostSuspendScopingTests` drives a
`_PipeWriteSpawner` (master fd = a pipe write end, so bytes are read back with no PTY line
discipline turning `0x1a` into a signal) to prove a harness strips Ctrl-Z, a **shell keeps
it** (job control), an all-Ctrl-Z harness frame writes nothing, and an unknown sid still
raises `KeyError` (the require-before-strip ordering).

### Conventions

Inserts `mcp/src` on `sys.path` (the suite idiom) before importing
`agents_remember.serving.terminal`. Every host fixture constructs the host as
`TerminalHost(TerminalHostSeams(spawn=…, tmux_probe=…, tmux_killer=…, tmux_creator=…,
tmux_configurer=…, tmux_mode_canceller=…))`, and every `open`/`attach`/`ensure` call passes the sid
followed by one `TerminalSessionSpec(cwd=…, command=(…,), lifecycle_id=…, name=…,
suspend_unsafe=…)`. The seam and per-session field names are unchanged — they moved onto those two
objects — but `command` is now a tuple rather than a list.
`_read_until` polls `read_nonblocking` via
`select` to a deadline; `_wait_dead` spins on `is_alive`. Skips key off
`shutil.which("tmux"|"cat"|"true")`, plus `_term_supports_clear()` for the real tmux
integration case, so the slice's PTY/tmux integration tests degrade to skips rather than
failures where the binaries or required terminal capabilities are absent (the slice-plan CI rule).

### Invariants And Boundaries

Unit subprocess fakes must inspect the exact environment, while the optional real-tmux case skips
only for missing tmux and owns/cleans its attached client explicitly.
Tmux command assertions locate owned flags and their operands; optional capability flags may shift
positions without weakening the asserted session-name contract.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Docs References

No relevant documentation was found after checking the configured sources; the regression claims
are proven by repository source and the test suite itself.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local test module. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The terminal host under test. | `TerminalHost` | mcp/src/agents_remember/serving/terminal.py:109-255 |
| The serving layer the host joins. | `# mcp/src/agents_remember/serving/ — Dashboard Serving Layer Overview` | onboarding/mcp/src/agents_remember/serving/overview.md:1-1486 |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | — | — |

## 260718-CHATS-L5I Current Delta

Terminal regressions now pin capability-aware synchronized tmux frame setup and its older-tmux fallback without weakening durable session and attachment semantics.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History
- 2026-08-13T07:53+02:00 — 260731-EFA-L23 super-line reconciliation: re-reviewed this card and its Repo-Internal citation targets after absorbing the super-integration memory line. Retained claims remain supported by the current tree. Verification is pinned to real code HEAD `1580f92715ff93c988f9a15439ad9bec60ef4c5d`; the new-line memory mapping remains closeout-owned.

- 2026-08-12T22:50+02:00 — 260731-EFA-L23 Dagger follow-up: made the custom-session-name regression assert the operand following tmux `-s` instead of fixed argv slot 6, preserving coverage across optional `-T sync` and older/unavailable-capability shapes. The owner reports the exact focused pytest passing and Ruff clean. Verification remains closeout-owned.
- 2026-08-02T18:15+02:00 — 260731-EFA-L6 curator W1-B06: anchored 2 Repo-Internal reference rows; scoped result 0 findings.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2: every fixture in this suite was rewritten onto two new
  parameter objects, so Conventions now records them. `TerminalHost` is constructed from one
  `TerminalHostSeams` carrying the same `spawn`/`tmux_probe`/`tmux_killer`/`tmux_creator`/
  `tmux_configurer`/`tmux_mode_canceller` fakes this card describes, and `open`/`attach`/`ensure`
  take the sid plus one `TerminalSessionSpec` carrying `cwd`/`command`/`lifecycle_id`/`name`/
  `suspend_unsafe`, with `command` now a tuple instead of a list. Every field name the body cites
  survives on those objects, and no test, argv assertion, Ctrl-Z scoping case, winsize check or
  skip guard changed.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-18T12:43+02:00 — FEUI-L9R: documented owned-environment unit coverage and contaminated
  launcher end-to-end ensure/attach proof; verification metadata remains pinned pending closeout.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-04T11:10+02:00 — L2 (knob injection): the registry fixture's fake tmux `_create_tmux` creator
  gained the `env` parameter (and a `created_env` recorder) to match the `TmuxCreator` seam now carrying
  `tmux new-session -e KEY=VALUE` spawn env. Test-fixture signature alignment only — the existing
  assertions are unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-02T17:25+02:00 — Reopened L6 copy-mode escape: added `TerminalHostCopyModeCancelTests`
  (pipe-backed writes, recording `tmux_mode_canceller` fake) pinning that mouse-report frames arm but
  never trigger the cancel, the first typed input after scrolling cancels copy-mode exactly once and
  passes through, scrolling re-arms it, and mixed frames count as typing. Verification metadata pinned
  until closeout stamps the follow-up commit.
- 2026-07-02T16:35+02:00 — Reopened L6 wheel fix: the registry fixture injects a recording
  `tmux_configurer` fake and pins that `ensure` asserts session options after both the create and the
  idempotent already-exists paths, and that every `attach` re-asserts them against the durable session.
  Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-06-27T02:28+02:00 — Task 22 follow-up: added `TerminalHost.ensure` registry coverage proving
  detached tmux creation records no durable PTY client, and proving the creator is skipped when the tmux
  probe already reports the session. Verification metadata pinned until closeout stamps the task-22
  follow-up code commit.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: added registry coverage for `TerminalHost.attach` /
  `close_session`, proving per-WebSocket clients are distinct from the durable `open` registry session
  and can be detached without unregistering it. Verification metadata pinned until closeout stamps the
  task-22 follow-up code commit.
- 2026-06-26T23:05+02:00 — Task 22: `TerminalHostRegistryTests` now injects tmux probe/kill fakes and
  covers `has_session`, explicit `terminate` killing/unregistering a live session, and terminating an
  unknown sid by supplied tmux name. Verification metadata pinned until closeout stamps the task-22 code
  commit.
- 2026-06-26T16:20+02:00 — Push-hook stability: the real tmux integration test now requires both
  `tmux` and a current `TERM` entry with `clear` capability, so noninteractive `TERM=dumb` push hooks
  skip the optional tmux end-to-end case instead of failing before the child command starts.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T20:30 — Task 6 slice 6f hardening: added the harness-scoped Ctrl-Z strip coverage — real-PTY `test_harness_write_strips_ctrl_z_suspend_byte` / `test_harness_write_all_ctrl_z_is_noop` (now opened `suspend_unsafe=True`) and a new `TerminalHostSuspendScopingTests` (via a `_PipeWriteSpawner`) proving harness-strips / shell-keeps / all-Ctrl-Z-noop / unknown-sid-still-raises. Verification metadata pinned until closeout stamps the 6f code commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: added `test_spawn_seeds_default_winsize` — opens a real-PTY session and reads back `TIOCGWINSZ` to assert the seeded 24×80 default (the controlling-terminal/winsize hardening so tmux honors resize). Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-18T15:40+02:00 — Created for task 6 slice 6d-1: covers `serving.terminal` (pure tmux command/name builders, the fake-spawner registry suite, real-PTY write/read/resize/exit, and a tmux-gated integration case). Verification metadata pinned to the task base until closeout stamps the 6d-1 code commit.
