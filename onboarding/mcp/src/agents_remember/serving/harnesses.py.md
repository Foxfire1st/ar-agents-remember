# mcp/src/agents_remember/serving/harnesses.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/harnesses.py`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T13:03+02:00                           |
| lastVerifiedCommitHash | `c881828542f0ca916ce8b1d4fd5ab8a914e24110`       |
| lastVerifiedCommitDate | 2026-07-10T13:18:50+02:00|
| governingOverview      | `overview.md`                                     |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`harnesses.py` is the **harness launch registry + per-harness knob mapping** (slice 6e-2b;
knob application 260703-L16): the curated table of TUI coding agents the framework can spawn, plus
`shutil.which` detection, plus — per harness — how the spawn knobs (`AR_SPAWN_MODEL`/
`AR_SPAWN_EFFORT`) map onto that harness's concrete CLI. It is the data behind the dashboard launch
buttons AND the `spawn_agent_session` dispatch seam. Since the L16 registry-openness ruling
(2026-07-07) the table is **good defaults, not a wall**: the `orchestration.harnesses` settings
family (parsed in `kernel/agentic_settings.py`, manual in `docs/reference/harnesses.md`) merges
over it by id — new ids add harnesses, builtin ids can be pre-customized. Deliberately **not** a
mirror of `scripts/sync-skills.py`'s skill-install targets (those include GUI editors that can't
run in a PTY).

## Code Commentary

### Logic

**260707-HFX2-L15 Codex mapping.** The Codex builtin now carries `model_flag="--model"` and an
effort `--config` vehicle with `model_reasoning_effort={value}`. Its accepted effort values are
exactly `none|minimal|low|medium|high|xhigh`; `max`, `ultracode`, and `auto` are excluded because
the first-turn API enum does not accept them. `knob_argv` renders the optional value template while
Pi.dev remains the only env-only builtin.

A frozen `Harness` dataclass carries `id` / `name` / `command` (the PATH command to detect) /
`argv` (the fixed launch argv) plus the L16 knob-mapping fields: `model_flag`, `effort_flag` +
`effort_flag_values` (the values the flag ACCEPTS), `effort_session_values` +
`effort_session_command` (values the flag rejects but the running session accepts as a pasted
command — the `{value}` template renders it), and `defined_in` (`"registry"` for these curated
defaults, `"settings"` for a new `orchestration.harnesses` id). `HARNESSES` is the curated tuple —
**Claude Code (`claude`) / Codex (`codex`) / Pi.dev (`pi`)** — in display order, indexed by
`_BY_ID`; claude carries the full mapping (`--model`, `--effort` with `low|medium|high|xhigh|max`,
session value `ultracode` → `/effort {value}`), codex/pi carry none (env-only). Helpers:

- `find_harness(id, *, registry=None)` — lookup in the builtin table OR an injected EFFECTIVE
  registry (`AgenticSettings.harnesses`).
- `unknown_harness_detail(id, *, registry=None)` — the loud teach-it-via-settings refusal text
  (names the known set + the manual; never a crash).
- `is_detected` / `detect_harnesses(*, which=None, registry=None)` — call-time `shutil.which`
  detection over the builtin or effective set, preserving order.
- `effort_vocabulary(harness)` — flag values + session values (empty = no vocabulary).
- `invalid_effort_detail(harness, effort)` — `None` when fine; the dispatch refusal text naming
  the harness and BOTH value sets otherwise. Mapping-less BUILTINS pass everything (documented
  env-only); a mapping-less SETTINGS-defined harness refuses with declare-or-launchArgs guidance.
- `invalid_model_detail(harness, model)` — refuses only a settings-defined harness with no
  `modelFlag` (explicit over guessing); model names are never enum-validated.
- `knob_argv(harness, *, model, effort)` — the extra argv the knobs map to (session-vocabulary
  effort values stay OFF the flag); `effort_session_commands(harness, effort)` — the post-launch
  paste line(s) delivering a session-level effort value.

### Invariants And Boundaries

- **Curated defaults, settings-extensible.** The builtin set is hand-listed; users extend/override
  it ONLY through `orchestration.harnesses` (fail-loud loader), never by wire input.
- **Fixed argv, id on the wire (the 6d posture).** Callers send a harness **id**; argv lives in the
  registry or the validated settings entry, so there is no command-injection surface. Knob values
  are appended as discrete argv elements — never shell-interpolated.
- **Silent-degrade prevention (the L16 defect).** The claude CLI warns-then-silently-degrades on
  unknown `--effort` values (probed 2026-07-07), so `invalid_effort_detail` refuses BEFORE launch;
  the two-vehicle vocabulary keeps `ultracode` (a session-only mode) off the flag entirely.
- **Detection is injectable + deterministic.** `which` defaults to `shutil.which` resolved at call
  time, so the unit tests pin detection regardless of what is installed on the test machine.
- **Pure / no I/O beyond `which`.** No FastAPI, no PTY, no settings reads — `agentic_settings.py`
  builds the effective registry; `terminal_opener.py`/`tools/terminal.py` enforce at spawn.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The opener that applies `knob_argv`/`launch_args` and enforces the vocabularies at launch resolution. | [serving/terminal_opener.py](agents-remember/mcp/src/agents_remember/serving/terminal_opener.py) |
| The dispatch layer that pre-validates knobs and delivers session commands. | [mcp/tools/terminal.py](agents-remember/mcp/src/agents_remember/mcp/tools/terminal.py) |
| The `orchestration.harnesses` parser that builds the effective registry over these defaults. | [kernel/agentic_settings.py](agents-remember/mcp/src/agents_remember/kernel/agentic_settings.py) |
| The `GET /api/harnesses` + open endpoints that consume the effective registry. | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The terminal host the resolved argv is spawned through (fixed-argv posture). | [serving/terminal.py](agents-remember/mcp/src/agents_remember/serving/terminal.py) |
| The serving layer this joins (localhost transport). | [serving overview](overview.md) |
| The spawn-surface manual documenting entries, vocabularies, and refusals. | [docs/reference/harnesses.md](agents-remember/docs/reference/harnesses.md) |
| The skill-install target list this is intentionally *not* a mirror of. | [scripts/sync-skills.py](agents-remember/scripts/sync-skills.py) |

## Update History

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: added Codex's explicit model/effort argv mapping,
  value-template support, and first-turn-safe effort enum; Pi.dev remains env-only. Verification
  metadata remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): grew the per-harness knob→flag
  mapping (`model_flag`/`effort_flag`+values/`effort_session_values`+command/`defined_in` on
  `Harness`; claude mapped `--model`/`--effort` with the two-vehicle effort vocabulary incl. the
  session-only `ultracode` → `/effort` paste; codex/pi documented env-only) and the enforcement
  helpers (`effort_vocabulary`, `invalid_effort_detail`, `invalid_model_detail`, `knob_argv`,
  `effort_session_commands`, `unknown_harness_detail`); `find_harness`/`detect_harnesses` accept an
  injected EFFECTIVE registry so `orchestration.harnesses` settings entries (new ids or builtin
  overrides) resolve everywhere. Verification metadata pinned until closeout stamps the L16 commit.
- 2026-06-18T21:27+02:00 — Created for task 6 slice 6e-2b: the harness launch registry (`Harness` +
  `HARNESSES` Claude Code/Codex/Pi.dev + `find_harness`/`is_detected`/`detect_harnesses` with an
  injectable call-time `which`) — the data behind `GET /api/harnesses` detection + the
  `kind="harness"` opener resolution. Verification metadata pinned to the task base until closeout
  stamps the 6e-2b code commit.
