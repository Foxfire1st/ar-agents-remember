# mcp/src/agents_remember/serving/terminal.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/terminal.py`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T12:43+02:00                           |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                     |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`terminal.py` is the **Mode B2 terminal host backend** (slice 6d-1): a registry of
tmux-wrapped PTY sessions that launch the real harness *inside* a dashboard-owned
terminal. It is render-not-scrape plumbing — the raw VT/ANSI bytes a PTY emits are
exactly what xterm.js will render (slice 6e) — and it is backend-only here: the
WebSocket bridge that drives it live is slice 6d-2, the visual is 6e. Task 22 adds the
tmux probe/create/kill hooks the durable terminal-session catalog needs to create a detached session,
distinguish a still-live external tmux session from a stale catalog row, and terminate explicitly,
plus per-WebSocket tmux-client attachment so multiple browser tabs can share one durable chat without
racing one PTY fd.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

Every dashboard-owned tmux client now receives an owned terminal environment: inherited `TMUX` and
`TMUX_PANE` are removed, `TERM` is forced to `xterm-256color`, and unrelated environment entries are
preserved. The same helper is applied to session probe, kill, detached create, mouse enable,
copy-mode cancel, pane-mode probe, and the attached PTY spawn. This prevents the daemon's launcher
tmux identity or `TERM=dumb` from contaminating child client behavior.

### Logic

`TerminalHost` holds a `dict[str, TerminalSession]` registry for attached PTY clients.
`ensure(sid, *, cwd, command, lifecycle_id=None, name=None, suspend_unsafe=False, env=None)` creates the
durable tmux session with `tmux new-session -d ...` when it is absent, returns a `TerminalSessionBinding`
metadata object, and deliberately registers no PTY client. This is the POST-opener path: the browser
WebSocket later attaches with its own client. **L2 knob injection:** `env` (a `Mapping[str, str]`) is
flattened by `_env_flags` into `tmux new-session -e KEY=VALUE` flags that seed the new session's — and
thus the child harness's — environment at spawn; it is empty-safe (an empty mapping yields the
byte-identical legacy no-env argv), stays argv items on the fixed `Sequence[str]` spawn (no
shell-injection surface), and is **inert on a re-attach** (a durable session keeps its creation env).
This is the same injection seam the planned T3 analytics env wiring and the role-knob (model/effort)
resolution layer target; `open`, `_build_tmux_command`, and `_ensure_binding` thread the same `env`
through. `open(sid, *, cwd, command, lifecycle_id=None, name=None,
suspend_unsafe=False)` is idempotent — a live
registered session for `sid` is returned as-is, a dead one reaped and replaced — and spawns
`_build_tmux_command(name, cwd, harness)` =
`tmux new-session -A -s <name> -c <cwd> -- <harness>` via the injectable `self._spawn`.
`attach(...)` uses the same spawn path but does **not** register the returned `TerminalSession`: it is a
per-connection tmux client for one WebSocket. This matters because one PTY master fd is a single-reader
stream; two browser tabs must not call `read_nonblocking(sid)` on the same registered fd. The WebSocket
bridge uses `read_session`/`write_session`/`resize_session`/`close_session` against the concrete
attachment object, while existing sid-keyed `write`/`read_nonblocking`/`resize`/`close` remain for the
registered-session API and tests. `-A` is attach-or-create, so the tmux **server** outliving this process
means a restart or dropped socket re-attaches the same live harness (persistence). `write` resolves the
session first (so an unknown sid still raises `KeyError`) and `write_session` applies the same write rules
to a concrete client: for a **suspend-unsafe**
session (`suspend_unsafe=True`, set by the opener for bare-pane harnesses), strips the
Ctrl-Z byte `_SUSPEND_BYTE` (`0x1a`) before `os.write` — that byte makes Claude Code
self-suspend and a bare pane has no shell to `fg` it back, so the harness soft-locks and
the operator's message is lost; a plain shell session leaves `suspend_unsafe=False`, so its
Ctrl-Z (legitimate job control) passes through and an all-Ctrl-Z frame to a harness is a
no-op write (slice 6f hardening). `write_session` also runs the reopened-L6 **copy-mode escape**
state machine: a stdin frame made only of SGR mouse reports (`_SGR_MOUSE_EVENT`) arms the
per-connection `mouse_seen` flag (wheel scrolling under `mouse on` may have entered tmux copy-mode,
which captures the keyboard); the first non-mouse input afterwards clears the flag and calls the
injectable mode canceller (`tmux send-keys -X cancel` by default, harmless no-op outside a mode)
before writing — so typing anywhere in the scrollback snaps the view to the live bottom and reaches
the pane app, at most one cancel subprocess per scroll-then-type cycle, and never triggered by
mouse-aware panes that don't enter copy-mode. `read_nonblocking`/`resize`/`close` key off the session's
PTY `master_fd`:
`read_nonblocking` returns `b""` both when idle (`BlockingIOError`) and after the child
exits (`OSError`/EIO once the slave closes) — callers use `is_alive` to disambiguate;
`resize` packs `struct.pack("HHHH", rows, cols, 0, 0)` into a `TIOCSWINSZ` ioctl
(SIGWINCH to the child / tmux client). `_tmux_session_name` sanitizes an arbitrary sid
into a tmux-legal name (`.`/`:` collapse to `-`, `ar-` prefix). Registry views:
`get`/`sessions`/`for_lifecycle`. Durability helpers: since **260707-HFX-L5** the probe is
**evidence-bearing** — `TmuxProbeResult(exists, evidence)` with
`TmuxProbeEvidence = "alive" | "pane-gone" | "tmux-command-failed"`.
`probe_session(tmux_name)` returns the full result and `has_session(tmux_name)` keeps the old
boolean view over it. The production default `_tmux_probe_session` runs
`tmux has-session -t <name>` with **stderr captured** (`stderr=subprocess.PIPE, text=True`) and
classifies: returncode 0 ⇒ `alive`; a nonzero exit whose stderr matches
`_tmux_missing_session_stderr` (case-insensitive `can't find session` / `session not found`) ⇒
`pane-gone` (the session is definitively missing); any other nonzero exit — including a transient
`error connecting to tmux server` — and any `OSError`/`SubprocessError`/timeout ⇒
`tmux-command-failed` (transient, so catalog liveness hysteresis applies rather than an immediate
exit mark; an unrecognized future tmux stderr wording degrades toward hysteresis, i.e. toward
FEWER false exits). An injected legacy boolean `TmuxProbe` is wrapped via
`_tmux_probe_result_from_bool` (`True` ⇒ `alive`, `False` ⇒ `pane-gone`), preserving old fake/test
semantics. `ensure` delegates missing-session
creation to the injectable creator (`tmux new-session -d -s <name> ...` by default), and
`terminate(sid, tmux_name=None)` kills the resolved tmux name via the injectable killer
(`tmux kill-session -t <name>` by default), then drops/discards any in-process PTY client. `close`
remains detach-only and does **not** kill tmux. The reopened L6 wheel fix adds an injectable
**configurer** (`_tmux_enable_mouse` by default: `tmux set-option -t <name> mouse on`, failures
suppressed) that `ensure` re-asserts after the create/probe step — so durable sessions predating the
option pick it up — and `attach` re-asserts against the existing session (attach cannot race creation).
With per-session `mouse on`, tmux requests mouse tracking from the browser client, so wheel input
scrolls tmux's own pane history (copy-mode) for normal-buffer TUIs (Codex) and passes through to panes
whose app tracks the mouse itself (Claude Code); the known tradeoff is Shift+drag for pane text
selection. All default tmux helpers
(`_tmux_probe_session` — which `_tmux_has_session` now delegates to —
/`_tmux_kill_session`/`_tmux_create_detached`/`_tmux_enable_mouse`) run
`subprocess.run(..., stdin=subprocess.DEVNULL, ...)` — the probe pipes stderr for evidence
classification (HFX-L5) while the fire-and-forget helpers keep `stderr=DEVNULL`; the
`stdin=DEVNULL` is the subprocess-hygiene guard (GitHub #49): under the stdio MCP transport the
parent's stdin *is* the JSON-RPC protocol pipe, so a fire-and-forget tmux call must never inherit and
consume it.

The default spawner `_spawn_pty` is the one impure seam: `pty.openpty()`, **seed a sane
`_DEFAULT_PTY_SIZE` (24×80) winsize** on the master (`TIOCSWINSZ`) so tmux never starts at 0×0, then
`subprocess.Popen(argv, stdin=stdout=stderr=slave, preexec_fn=lambda: os.login_tty(slave_fd),
pass_fds=(slave_fd,))`. **`os.login_tty` (setsid + `TIOCSCTTY` + dup2) makes the slave the child's
controlling terminal** — without it tmux has no `/dev/tty` to size against and stays stuck at 80×24,
ignoring every resize; `pass_fds` keeps the slave open past `close_fds` so `login_tty` can re-claim it,
and the explicit `stdin/stdout/stderr=slave` is the deliberate handle that keeps the child off the
inherited MCP stdio pipe (the subprocess-hygiene guard, GitHub #49 — the `preexec_fn` body is
async-signal-safe syscalls only, hence the local `# noqa: PLW1509`). The parent closes the slave →
`os.set_blocking(master_fd, False)`. `PtyProcess` (the spawner
return shape) carries `master_fd`/`pid`/`terminate`/`poll` as plain values + callables,
so a fake spawner can back a session with any process object.

### Invariants And Boundaries

- **Impure seams are injectable.** Attached-client PTY I/O is behind `Spawner`, detached tmux creation
  is behind `TmuxCreator`, explicit termination is behind `TmuxKiller`, session-option assertion
  (mouse mode) is behind `TmuxConfigurer`, and copy-mode escape is behind `TmuxModeCanceller`; tests
  drive a real kernel
  PTY with the tmux wrapper stripped (`cat`), and the tmux path itself is one skip-when-unavailable
  integration test. The pure command/name builders are I/O-free.
- **Fixed-argv security posture (B2).** The spawn is a `Sequence[str]`, never a shell
  string — no shell-injection surface. The child runs as the dashboard's own OS user with
  that user's existing credentials (`~/.claude`, no re-auth). The driving WebSocket
  (6d-2) stays `127.0.0.1`-bound like the rest of `serving/`.
- **Persistence is tmux's, not ours.** `close` terminates the registered local client + reaps it but the
  tmux server keeps the session; `close_session` does the same for one per-WebSocket attachment without
  mutating the registry. A later `open`/`attach` with the same name re-attaches.
- **Rehydrate must probe first.** Callers must use `has_session` before using `open(..., name=...)` for a
  catalog row. `tmux new-session -A` would create a fresh session if the named one is gone, which would
  turn stale catalog state into a false resume.
- **Terminate is explicit.** Only `terminate` kills a tmux session. UI detach/`close` stays non-destructive.
- **No subprocess inherits the MCP stdio pipe (GitHub #49).** Under the stdio transport the parent's
  stdin is the JSON-RPC protocol pipe, so every spawn must redirect stdin: the three default tmux
  `subprocess.run` helpers pass `stdin=subprocess.DEVNULL`, and the `_spawn_pty` child is wired to the
  PTY slave (`stdin=stdout=stderr=slave_fd`). Enforced by `mcp/tests/test_subprocess_hygiene.py`.
- **Backend-only.** No FastAPI import here — `app.py` wires the WebSocket endpoint over
  this host in 6d-2; the xterm.js viewport is 6e.

### Conventions

All dashboard-owned tmux subprocesses receive the same copied environment helper; unrelated parent
variables are retained and the caller's environment mapping is never mutated.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Docs References

No relevant documentation was found after checking the configured sources; terminal-host behavior
is proven by repository source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local terminal host. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The serving layer this host joins (transport; localhost posture). | `TerminalHost` | mcp/src/agents_remember/serving/terminal.py:109-255 |
| The FastAPI app wires the WebSocket bridge and terminal-session routes over this host. | "async def _serve_terminal_websocket("; "def _register_terminal_session_routes(app: FastAPI" | mcp/src/agents_remember/serving/_app_terminal_routes.py:86-86; mcp/src/agents_remember/serving/_app_terminal_routes.py:130-130 |
| Catalog entries declare durable identity/cwd/tmux/command/lifecycle/status fields, and "class TerminalCatalogEntry:" persists and reads those entries. | "class TerminalCatalogEntry:"; "class TerminalCatalogEntry:" | mcp/src/agents_remember/models/terminal_catalog.py:44-474; mcp/src/agents_remember/serving/terminal_catalog.py:48-386 |
| The opener resolves the spawn environment, builds the terminal session spec, calls the host ensure operation, and upserts the catalog entry. | `_open_terminal_transaction` | mcp/src/agents_remember/serving/terminal_opener.py:619-708 |
| The terminal host registry behavior is exercised by the dedicated registry test class. | `TerminalHostRegistryTests` | mcp/tests/test_terminal.py:300-466 |
| The optional real-tmux integration is exercised by the dedicated integration test class. | `TerminalHostTmuxIntegrationTests` | mcp/tests/test_terminal.py:792-844 |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local terminal host.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | — | — |

## 260718-CHATS-L5I Current Delta

Terminal creation now uses synchronized tmux frame support only when the installed tmux capability permits it, preserving a fallback for older hosts. The terminal host continues to separate durable session identity from browser attachment and does not treat unsupported terminal features as a reason to fail a session.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

Two named concepts now define this module's surface:

- **`TerminalSessionSpec`** (`cwd`, `command`, `lifecycle_id`, `name`, `suspend_unsafe`, `env`) —
  **how ONE hosted tmux session is created**: what runs, where, and under whose identity. It is the
  request half of the pair whose answer is `TerminalSessionBinding` / `TerminalSession`.
  `TerminalHost.open`, `.ensure` and `.attach` now ALL take the same spec, because they create (or
  re-reach) the *same* durable session through different client shapes — keeping it one object is
  what makes that sameness checkable instead of six parallel parameter lists drifting apart.
  `__post_init__` normalizes `cwd` to `Path` and `command` to a tuple, and `tmux_name_for(sid)` is
  the one place the durable tmux identity is decided (the spec's explicit `name`, else the derived
  one). `env` keeps its documented meaning: spawn env seeded at CREATION (`tmux new-session -e
  KEY=VALUE`, the L2 knob-injection seam), inert once the durable session exists, and **never used
  by `attach`**.
- **`TerminalHostSeams`** (`spawn`, `tmux_probe`, `tmux_killer`, `tmux_creator`, `tmux_configurer`,
  `tmux_mode_canceller`) — the **one impure boundary** of `TerminalHost`: the PTY spawner and the
  tmux commands. These are not independent switches; they are a single surface, the host's entire
  contact with the operating system. A test that fakes tmux replaces the surface, so the
  substitution is visible as one decision at the call site. `TerminalHost(seams=None)` keeps every
  real implementation, and `None` on any individual field keeps that seam real.

Callers updated accordingly: the opener and `app.py` both call `host.ensure(sid,
TerminalSessionSpec(...))`.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-04T11:34:10+02:00 — 260731-EFA-L6 S18-B12 curator: restored the terminal application route family, catalog field/persistence body, and opener environment/spec/ensure/upsert flow with a single full-transaction anchor; the scoped fixer will generate citation ranges.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `TerminalSessionSpec` (shared by open/ensure/attach, with `tmux_name_for`) and `TerminalHostSeams` (the one impure OS boundary).
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded owned tmux-client terminal identity across all six
  administrative clients and attached PTY spawn; verification metadata remains pinned pending
  candidate closeout.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-07T23:45+02:00 — 260707-HFX-L5 (catalog liveness hysteresis): the tmux probe is now
  **evidence-bearing** — new `TmuxProbeResult(exists, evidence)` +
  `TmuxProbeEvidence = "alive"|"pane-gone"|"tmux-command-failed"`, `TerminalHost.probe_session`
  beside the boolean `has_session`. The production `_tmux_probe_session` captures stderr and is
  **stderr-aware** (L5R2 fix round): only explicit missing-session stderr
  (`can't find session` / `session not found`, via `_tmux_missing_session_stderr`) classifies as
  `pane-gone`; every other nonzero exit and every subprocess error/timeout classifies as the
  transient `tmux-command-failed` so catalog hysteresis applies — an unrecognized future tmux
  wording fails toward fewer false exits. Injected legacy boolean probes are wrapped by
  `_tmux_probe_result_from_bool` (back-compat for fakes/tests). Consumed by
  `terminal_liveness.py`'s sweeper + shared observation path. Verification metadata pinned until
  closeout stamps the HFX-L5 commit.
- 2026-07-04T11:10+02:00 — L2 (agent-orchestration knob injection): `TmuxCreator` gained an `env`
  parameter and `_tmux_create_detached`/`_build_tmux_command` now emit `tmux new-session -e KEY=VALUE`
  flags (via the new pure `_env_flags`); `ensure`/`open`/`_ensure_binding` thread an optional
  `env: Mapping[str, str]` through, seeded only at creation and inert on re-attach. Empty-safe (an empty
  mapping keeps the byte-identical legacy argv). This is the minimal env-passthrough seam the agent-facing
  `spawn_agent_session` tool composes over to inject role knobs (model/effort/env) at spawn. Verification
  metadata pinned until closeout stamps the L2 commit.
- 2026-07-02T17:25+02:00 — Reopened L6 copy-mode escape: `write_session` now recognizes SGR
  mouse-report-only stdin frames (arming a per-connection `mouse_seen` flag) and cancels tmux
  copy-mode via the new injectable `TmuxModeCanceller` (`tmux send-keys -X cancel`, suppressed
  failures, DEVNULL hygiene) on the first typed input after scrolling. Rationale: copy-mode captures
  the keyboard, so scrolled-up non-mouse panes (Codex) swallowed typing until the operator scrolled
  back to the bottom; tmux offers no any-key-cancels binding, but the host sees every stdin frame.
  Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-07-02T16:35+02:00 — Reopened L6 wheel fix: added the injectable `TmuxConfigurer` seam with the
  `_tmux_enable_mouse` default (`tmux set-option -t <name> mouse on`, suppressed failures, DEVNULL
  hygiene), asserted by `ensure` after create/probe and by `attach` against the existing durable
  session. Rationale: xterm always sees the tmux client's alternate screen, so browser wheel input can
  only scroll correctly when tmux itself handles it as mouse reports (pane history for normal-buffer
  TUIs, pass-through for mouse-aware TUIs). Verification metadata pinned until closeout stamps the
  follow-up commit.
- 2026-06-27T18:43+02:00 — Subprocess-hygiene fix (GitHub #49): added `stdin=subprocess.DEVNULL` to the
  three default tmux `subprocess.run` call sites (`_tmux_has_session`/`_tmux_kill_session`/
  `_tmux_create_detached`) so a fire-and-forget tmux call cannot inherit and consume the stdio MCP
  transport's protocol pipe. Behavior-preserving; the `_spawn_pty` Popen child (already wired to the PTY
  slave) was unchanged. Repo enforces it via `mcp/tests/test_subprocess_hygiene.py`. Verification metadata
  left pinned until closeout stamps the code commit.
- 2026-06-27T02:28+02:00 — Task 22 follow-up: added `TerminalHost.ensure` and
  `TerminalSessionBinding` so the opener can create a detached durable tmux session without spawning a
  starter PTY client that then gets closed. This keeps a new chat alive until the first WebSocket
  attaches while preserving per-tab `attach` clients. Verification metadata pinned until closeout
  stamps the task-22 follow-up code commit.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: added unregistered `attach` clients plus
  `read_session`/`write_session`/`resize_session`/`close_session` so each browser WebSocket gets its own
  tmux client PTY while the durable catalog identity remains one tmux session. This fixes multi-tab
  terminal sharing by removing shared-fd read/close contention. Verification metadata pinned until
  closeout stamps the task-22 follow-up code commit.
- 2026-06-26T23:05+02:00 — Task 22: added injectable tmux probe/kill hooks, `has_session`, and
  `terminate`. The catalog rehydrate path can now verify a tmux name exists before calling `open`, and
  the UI terminate route can kill tmux explicitly without changing detach semantics. Verification
  metadata pinned until closeout stamps the task-22 code commit.
- 2026-06-19T20:30 — Task 6 slice 6f hardening: `TerminalSession` gained `suspend_unsafe` and `TerminalHost.write` now strips the Ctrl-Z byte `0x1a` for **suspend-unsafe (bare-pane harness)** sessions only — it self-suspends Claude Code with no shell to `fg`, soft-locking the session and dropping the operator's message; a plain shell session keeps Ctrl-Z (job control). `write` resolves the sid before stripping (unknown sid still raises), and `open` carries the new `suspend_unsafe` flag (the opener sets it `True` for `kind="harness"`). Verification metadata pinned until closeout stamps the 6f code commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: `_spawn_pty` now makes the PTY slave the child's **controlling terminal** via `os.login_tty` in a `preexec_fn` (setsid + `TIOCSCTTY` + dup2) and seeds a `_DEFAULT_PTY_SIZE` winsize before exec — without a controlling tty tmux ignored every resize and stayed at 80×24. Kept the explicit `stdin/stdout/stderr=slave` (deliberate handle off the MCP stdio pipe, GitHub #49 hygiene) + `pass_fds=(slave_fd,)`; the `preexec_fn` is async-signal-safe, so it carries a local `# noqa: PLW1509`. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-18T15:40+02:00 — Created for task 6 slice 6d-1: the `TerminalHost` + `PtyProcess`/`TerminalSession` + the pure `_build_tmux_command`/`_tmux_session_name` builders + the stdlib-`pty` default spawner `_spawn_pty` — the backend half of Mode B2 (tmux-wrapped PTY sessions; injectable spawn; localhost/fixed-argv posture). The WebSocket bridge is 6d-2. Verification metadata pinned to the task base until closeout stamps the 6d-1 code commit.
