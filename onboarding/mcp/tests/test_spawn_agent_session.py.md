# mcp/tests/test_spawn_agent_session.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_spawn_agent_session.py`           |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-07-06T22:46+02:00                            |
| lastVerifiedCommitHash | `9d58058e3ce4815b0356794fc21973ebe9c71345`        |
| lastVerifiedCommitDate | 2026-07-06T11:47:10+02:00|
| governingOverview      | `../overview.md`                                  |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_spawn_agent_session.py` covers the agent-facing `spawn_agent_session` MCP tool (L2 dispatch) and
the serving `POST /api/terminal/{session}/paste` endpoint. It exercises the whole composition —
opener + leaf claim + echo-confirmed paste + submit — against a fake host + fake paster + a fake
`which`, so no real tmux server, no real daemon, and no real sleeping are involved. Since 260703-L13
`SpawnHarnessResolutionTests` pins the settings-driven harness seam through the payload builder with
REAL settings files in temp roots: omitted harness reads the global `orchestration.spawn.harness`,
the repo-local file (selected via the qualified leaf key against a configured `RepositoryScope`)
overrides global, leafless/unconfigured-repo spawns read global only, an explicit argument beats
every layer, no-settings falls back to the first DETECTED registry harness, nothing-detected and
configured-but-undetected both REFUSE (`harness-not-detected`, the latter naming
`orchestration.spawn.harness` and the source file) — never a silent default.

## Code Commentary

### Logic

`SpawnAgentSessionTests` drives `spawn_agent_session_payload` with a `_FakeHost` (records `ensure`
calls + the seeded `env`), a `_FakePaster` (records paste calls + returns a scripted
delivered/submitted `PasteResult`), a `_detected` `which`, and a fixed `session_id`. The cases pin the
L2 contracts:

- **spawn + submit** (`test_spawns_and_delivers_context_with_submit`): the payload is `ok`/`spawned`,
  carries the leaf, spawned-by session/lifecycle, and delivered+submitted flags; the model/effort knobs
  are seeded as `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT` in the spawn env; the provenance persists on the
  catalog row; and the packet was pasted-and-submitted into the session's tmux pane.
- **draft** (`test_draft_paste_does_not_submit`): `submit=False` pastes without submitting and omits the
  `submitted` key.
- **no context** (`test_spawn_without_context_skips_paste`): no paste is attempted.
- **leaf-taken** (`test_leaf_taken_is_surfaced_never_overridden`): a running chat already owning the leaf
  makes the spawn return `ok: false` / `leaf-taken` with the owner, and nothing is spawned, pasted, or
  upserted (the never-override invariant).
- **pre-spawn refusals** (`test_unknown_harness_refused_before_spawn` /
  `test_undetected_harness_refused_before_spawn`): an unknown or undetected harness returns the matching
  refusal status with no `ensure` call.
- **ambient provenance** (`test_spawned_by_lifecycle_defaults_to_active_ambient`): with no explicit
  `spawned_by_lifecycle`, the spawn defaults it to the active ambient lifecycle id (installed over a temp
  `EventStore`).

`TerminalPasteEndpointTests` builds the app with `create_app(..., terminal_host=fake,
terminal_catalog=…, terminal_paster=fake)` and drives `POST /api/terminal/{session}/paste` through
`TestClient`: a known running session delivers+submits (200), and an unknown session is `404`
`unknown-session` with no paste attempted.

### Conventions

`unittest` + `tempfile` + the `sys.path` insertion idiom. `reset_ambient()` in setUp/tearDown keeps the
process-singleton lifecycle isolated between tests. The fakes duck-type `TerminalHost` /
`TerminalPaster` and are passed through the tool's injectable `host`/`paster`/`which`/`session_id`
seams (or `create_app`'s injectable params for the endpoint).

### Invariants And Boundaries

- No real tmux, no real daemon, no real sleep — the whole spawn/paste composition runs against fakes.
- `leaf-taken` must not spawn, paste, or upsert; the test asserts all three did not happen.
- Provenance defaults to the active ambient lifecycle only when not explicitly supplied.

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation found; the behavior is local MCP/serving dispatch policy.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests pin the local agent-facing dispatch composition, not an external protocol. | L116-L273 | [test_spawn_agent_session.py](test_spawn_agent_session.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tool under test composes the opener + echo-confirmed paste and returns the strict spawn payload. | L82-L211 | [../src/agents_remember/mcp/tools/terminal.py](../src/agents_remember/mcp/tools/terminal.py) |
| The shared opener the tool composes (leaf claim + env-seeded ensure + upsert). | L84-L174 | [../src/agents_remember/serving/terminal_opener.py](../src/agents_remember/serving/terminal_opener.py) |
| The `PasteResult` the fake paster returns + the paste helper the endpoint drives. | L62-L67; L133-L229 | [../src/agents_remember/serving/terminal_paste.py](../src/agents_remember/serving/terminal_paste.py) |
| The `POST /api/terminal/{session}/paste` endpoint under test. | L653-L676 | [../src/agents_remember/serving/app.py](../src/agents_remember/serving/app.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests cover local MCP/serving behavior only. | - | - |

## Update History

- 2026-07-06T22:46+02:00 — 260703-L13 (settings unification): added
  `SpawnHarnessResolutionTests` — eight cases pinning explicit > repo-local > global >
  detection-gated resolution, refusal-not-fallback behavior, and source-naming refusal
  details, all through `spawn_agent_session_payload` with real temp settings files.
  Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-04T11:10+02:00 — L2: created coverage for the agent-facing `spawn_agent_session` tool
  (spawn+submit, draft, no-context, leaf-taken-never-overridden, unknown/undetected-harness refusals,
  ambient-lifecycle provenance default) and the `POST /api/terminal/{session}/paste` endpoint (delivered
  + 404), all against fake host/paster/which — no real tmux, daemon, or sleep. Verification metadata
  pinned until closeout stamps the L2 commit.
