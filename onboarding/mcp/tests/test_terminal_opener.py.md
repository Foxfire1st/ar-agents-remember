# mcp/tests/test_terminal_opener.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_terminal_opener.py`               |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-07-04T11:10+02:00                            |
| lastVerifiedCommitHash | `3c592f76ed607e4c0391fd26d77b869ee837a5af`        |
| lastVerifiedCommitDate | 2026-07-04T11:44:59+02:00|
| governingOverview      | `../overview.md`                                  |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_terminal_opener.py` covers the shared hosted-session opener (`serving.terminal_opener`, L2) — the
ONE spawn path both the dashboard `POST /api/terminal/{session}` route and the agent-facing
`spawn_agent_session` MCP tool compose over. It drives `open_terminal_session` against a fake host
(records the `ensure` call, no real tmux) + a real JSON catalog, pinning the leaf-claim / provenance /
env-seed behaviour both call paths inherit.

## Code Commentary

### Logic

`OpenTerminalSessionTests` drives `open_terminal_session` with a `_FakeHost` (records `ensure`'s sid /
cwd / command / env, adds the tmux name to a known set) + a real `TerminalCatalog` over a temp dir + a
`_detected` `which`. The cases:

- **opened** (`test_opened_records_provenance_env_and_leaf`): the result is `opened`, the catalog row
  carries the leaf, the spawned-by session/lifecycle, and the harness; the knob env was seeded into the
  detached tmux spawn; and the provenance survives the catalog camelCase round-trip
  (`spawnedBySession` / `spawnedByLifecycle`).
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

- 2026-07-04T11:10+02:00 — L2: created coverage for the shared `open_terminal_session` opener —
  opened+provenance+env-seed+leaf, leaf-taken-surfaces-owner-without-spawning, bad-kind, and
  undetected-harness — against a fake host + real JSON catalog. Verification metadata pinned until
  closeout stamps the L2 commit.
