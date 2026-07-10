# mcp/tests/test_terminal_opener.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_terminal_opener.py`               |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-07-10T13:03+02:00                            |
| lastVerifiedCommitHash | `c881828542f0ca916ce8b1d4fd5ab8a914e24110`        |
| lastVerifiedCommitDate | 2026-07-10T13:18:50+02:00|
| governingOverview      | `../overview.md`                                  |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_terminal_opener.py` covers the shared hosted-session opener (`serving.terminal_opener`, L2) — the
ONE spawn path both the dashboard `POST /api/terminal/{session}` route and the agent-facing
`spawn_agent_session` MCP tool compose over. It drives `open_terminal_session` against a fake host
(records the `ensure` call, no real tmux) + a real JSON catalog, pinning the leaf-claim / provenance /
env-seed behaviour both call paths inherit — and, since 260703-L16, the per-harness knob→argv
application (`KnobApplicationTests`).

## Code Commentary

### Logic

**260707-HFX2-L15 coverage.** The Codex opener now asserts explicit `--model` plus
`--config model_reasoning_effort=...` argv and catalog persistence of replacement-leaf,
resolved-knob, and existing log-binding provenance.

`OpenTerminalSessionTests` drives `open_terminal_session` with a `_FakeHost` (records `ensure`'s sid /
cwd / command / env, adds the tmux name to a known set) + a real `TerminalCatalog` over a temp dir + a
`_detected` `which`. The cases:

- **opened** (`test_opened_records_provenance_env_and_leaf`): the result is `opened`, the catalog row
  carries the leaf, the spawned-by session/lifecycle, the harness, and (L14) the `spawn_role` read
  from the env's `AR_SPAWN_ROLE`; the knob env was seeded into the
  detached tmux spawn; and the provenance survives the catalog camelCase round-trip
  (`spawnedBySession` / `spawnedByLifecycle` / `spawnRole`).
- **role preservation** (`test_reopen_preserves_spawn_role_and_hand_open_records_none`, L14): a
  role-less re-open keeps the recorded `spawn_role` (write-once, like the spawned-by pair), and a
  hand-opened session (no env role) records `None` with `spawnRole` absent from its JSON.

`KnobApplicationTests` (L16) pin the opener-side knob application: env `AR_SPAWN_MODEL`/
`AR_SPAWN_EFFORT` become `--model`/`--effort` on claude's ensured command while the env keeps
riding; a session-vocabulary effort (`ultracode`) stays OFF the flag; an unknown effort refuses
`bad-kind` BEFORE any spawn with the detail naming claude and both value sets; a mapping-less
builtin (codex) is env-only; `launch_args` append verbatim after the knob flags; the free-form
provenance (`launch_args`/`prompt_keywords`/`session_commands`) is recorded on the row, JSON
round-trips camelCase, survives a free-form-less re-open, and stays absent for hand-opened rows;
an injected effective registry resolves a settings-defined harness (custom argv) while an
unknown-everywhere id refuses pointing at `orchestration.harnesses` + the
`docs/reference/harnesses.md` manual; and a vocab-less settings-defined harness refuses the effort
knob with declare-or-launchArgs guidance.
- **leaf-taken** (`test_leaf_taken_surfaces_owner_without_spawning`): a running chat already owning the
  leaf makes the opener return `leaf-taken` with the owner and never spawn or upsert the intruder.
- **bad kind** (`test_bad_kind_reports_detail`): an unknown launch kind returns `bad-kind` with a detail
  and no ensure.
- **undetected harness** (`test_undetected_harness_is_bad_kind`): an undetected harness (`which`
  returning `None`) also resolves to `bad-kind` with no ensure.

### Conventions

`unittest` + `tempfile` + the `sys.path` insertion idiom. The `_FakeHost` duck-types `TerminalHost`
(only `has_session` + `ensure`), and `_running_chat` seeds a running harness catalog row with
deterministic timestamps. `open_terminal_session` is called through a `_open` helper that fills the
required kwargs.

### Invariants And Boundaries

- No real tmux — the fake host records the `ensure` call and the catalog is a plain JSON store.
- `leaf-taken` / `bad-kind` must not spawn or upsert; the tests assert `host.ensured == []` and no
  intruder row.
- Provenance must survive the catalog JSON round-trip (migration-safe camelCase keys).

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation found; the behavior is local opener policy.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests pin the local shared-opener composition, not an external protocol. | L89-L149 | [test_terminal_opener.py](test_terminal_opener.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The opener under test (resolve + leaf claim + env-seeded ensure + catalog upsert). | L84-L174 | [../src/agents_remember/serving/terminal_opener.py](../src/agents_remember/serving/terminal_opener.py) |
| The catalog whose provenance/leaf columns the opener writes and the tests read back. | L47-L54; L108-L111 | [../src/agents_remember/serving/terminal_catalog.py](../src/agents_remember/serving/terminal_catalog.py) |
| The role-scoped leaf-conflict probe the opener reuses. | L28-L42 | [../src/agents_remember/serving/terminal_leaf_assignment.py](../src/agents_remember/serving/terminal_leaf_assignment.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests cover local serving behavior only. | - | - |

## Update History

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: replaced env-only Codex expectations with explicit
  argv and covered the new opener provenance fields. Verification metadata remains pinned until
  closeout stamps the eventual L15 code commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): added `KnobApplicationTests` —
  env-knob→argv flag mapping (env still riding), session-vocabulary effort off the flag, the
  pre-spawn refusal naming both value sets, env-only mapping-less builtins, verbatim `launch_args`,
  free-form provenance recording/round-trip/preservation, effective-registry resolution of
  settings-defined harnesses, the unknown-everywhere manual-pointing refusal, and the vocab-less
  settings-harness guidance refusal. Existing opener tests unmodified. Verification metadata pinned
  until closeout stamps the L16 commit.

- 2026-07-06T23:58:54+02:00 — 260703-L14 (visual hierarchy + chat grouping): the opened case now seeds
  `AR_SPAWN_ROLE` and asserts it lands on the row + round-trips as `spawnRole`; added
  `test_reopen_preserves_spawn_role_and_hand_open_records_none` (write-once role across a role-less
  re-open; hand-opened rows record none).
  Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-04T11:10+02:00 — L2: created coverage for the shared `open_terminal_session` opener —
  opened+provenance+env-seed+leaf, leaf-taken-surfaces-owner-without-spawning, bad-kind, and
  undetected-harness — against a fake host + real JSON catalog. Verification metadata pinned until
  closeout stamps the L2 commit.
