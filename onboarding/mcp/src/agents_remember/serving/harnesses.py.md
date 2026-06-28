# mcp/src/agents_remember/serving/harnesses.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/harnesses.py`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-18T21:27+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                     |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`harnesses.py` is the **harness launch registry** (slice 6e-2b): the small, curated table of TUI
coding agents the dashboard-owned terminal (Mode B2) can spawn, plus `shutil.which` detection. It is
the data behind the per-harness launch buttons — `GET /api/harnesses` reports the set + which are
installed, and the `POST /api/terminal/{id}` opener resolves a `{kind:"harness", harness:"<id>"}` to
the harness's fixed argv. It is deliberately **not** a mirror of `scripts/sync-skills.py`'s
skill-install targets (those include GUI editors that can't run in a PTY).

## Code Commentary

### Logic

A frozen `Harness` dataclass carries `id` / `name` / `command` (the PATH command to detect) / `argv`
(the fixed launch argv). `HARNESSES` is the curated tuple — **Claude Code (`claude`) / Codex
(`codex`) / Pi.dev (`pi`)** — in display order, indexed by `_BY_ID`. `find_harness(id)` returns the
`Harness | None`. `is_detected(harness, *, which=None)` resolves `which` to `shutil.which` **at call
time** (so a test can either inject a fake or monkeypatch the module attribute) and returns whether
the command is on `PATH`. `detect_harnesses(*, which=None)` maps the whole registry to
`DetectedHarness(id, name, detected)` rows (a frozen dataclass — the `GET /api/harnesses` shape),
preserving registry order.

### Invariants And Boundaries

- **Curated, not derived.** The supported set is hand-listed here, *not* read from `sync-skills.py`;
  Gemini CLI is unsupported and GUI editors (Cursor, VS Code/Copilot, Antigravity) are excluded
  because they are not spawnable TUIs.
- **Fixed argv, id on the wire (the 6d posture).** The browser sends a harness **id**; the argv lives
  only here, so there is no command-injection surface. `resolve_terminal_launch` (in `app.py`) rejects
  an absent / unknown / not-installed harness before any spawn.
- **Detection is injectable + deterministic.** `which` defaults to `shutil.which` resolved at call
  time, so the unit tests pin detection regardless of what is installed on the test machine.
- **Pure / no I/O beyond `which`.** No FastAPI, no PTY — `app.py` owns the endpoints + spawn.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The opener + `GET /api/harnesses` endpoint that consume this registry. | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The terminal host the resolved argv is spawned through (fixed-argv posture). | [serving/terminal.py](agents-remember/mcp/src/agents_remember/serving/terminal.py) |
| The serving layer this joins (localhost transport). | [serving/overview.md](agents-remember/mcp/src/agents_remember/serving/overview.md) |
| The skill-install target list this is intentionally *not* a mirror of. | [scripts/sync-skills.py](agents-remember/scripts/sync-skills.py) |

## Update History

- 2026-06-18T21:27+02:00 — Created for task 6 slice 6e-2b: the harness launch registry (`Harness` +
  `HARNESSES` Claude Code/Codex/Pi.dev + `find_harness`/`is_detected`/`detect_harnesses` with an
  injectable call-time `which`) — the data behind `GET /api/harnesses` detection + the
  `kind="harness"` opener resolution. Verification metadata pinned to the task base until closeout
  stamps the 6e-2b code commit.
