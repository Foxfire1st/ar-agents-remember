# test_terminal.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_terminal.py`                     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb` |
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks real PTY write/read, cleanup when spawning never starts, and real tmux ensure/attach behavior independent of launcher identity. The tmux case remains conditioned on its actual environment availability. The file no longer claims the broad fake-registry, copy-mode, resize and terminal-death matrix.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Write then read roundtrip | `test_write_then_read_roundtrip` | mcp/tests/test_terminal.py:81-84 |
| A spawn that never started leaves no pty fd behind | `test_a_spawn_that_never_started_leaves_no_pty_fd_behind` | mcp/tests/test_terminal.py:88-116 |
| Real tmux ensure and attach ignore launcher identity | `test_real_tmux_ensure_and_attach_ignore_launcher_identity` | mcp/tests/test_terminal.py:143-171 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.

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
