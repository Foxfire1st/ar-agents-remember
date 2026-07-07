# mcp/tests/test_spawn_agent_session.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/tests/test_spawn_agent_session.py`           |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-07-07T23:20+02:00                            |
| lastVerifiedCommitHash | `551695279f403ab19c0eba4ce6f6cfde6a8bb1f5`        |
| lastVerifiedCommitDate | 2026-07-07T20:09:01+02:00|
| governingOverview      | `../overview.md`                                  |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

`test_spawn_agent_session.py` covers the agent-facing `spawn_agent_session` MCP tool (L2 dispatch) and
the serving `POST /api/terminal/{session}/paste` endpoint. It exercises the whole composition —
opener + leaf claim + capture-verified paste + submit — against a fake host + fake paster + a fake
`which`, so no real tmux server, no real daemon, and no real sleeping are involved. Since 260703-L13
`SpawnHarnessResolutionTests` pins the settings-driven harness seam through the payload builder with
REAL settings files in temp roots: omitted harness reads the global `orchestration.spawn.harness`,
the repo-local file (selected via the qualified leaf key against a configured `RepositoryScope`)
overrides global, leafless/unconfigured-repo spawns read global only, an explicit argument beats
every layer, no-settings falls back to the first DETECTED registry harness, nothing-detected and
configured-but-undetected both REFUSE (`harness-not-detected`, the latter naming
`orchestration.spawn.harness` and the source file) — never a silent default. 260703-L16 adds three
classes: `SpawnKnobApplicationTests` (per-harness knob application + the free-form escape hatch),
`SettingsDefinedHarnessTests` (orchestration.harnesses registry openness), and
`SpawnLevelResolutionTests` (the dispatch `level` + rolesPerLevel resolution chain).

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
- **spawn role** (`test_spawn_records_role_from_env_and_reports_it`, L14): a spawn whose `env`
  carries `AR_SPAWN_ROLE` persists it on the catalog row (`spawn_role`) and reports it as
  `spawnRole` in the `spawned` payload — the Chats command-tree grouping key.
- **draft** (`test_draft_paste_does_not_submit`): `submit=False` pastes without submitting and omits the
  `submitted` key.
- **no context** (`test_spawn_without_context_skips_paste`): no paste is attempted.
- **verified delivery ships no capture** (`test_verified_delivery_omits_the_failure_capture`,
  260707-HFX-L3): the capture is failure evidence — a verified delivery omits `deliveryCapture`.
- **loud failure** (`test_unverified_delivery_reports_false_with_the_pane_capture_attached`,
  260707-HFX-L3/SF-1 — reviewer 46b2e267 got `contextDelivered: true` over a codex pane that booted
  clean with no payload): an unverified delivery on a spawned session reports
  `contextDelivered: false` / `submitted: false` WITH `deliveryCapture` carrying the fake paster's
  pane snapshot.

`SpawnKnobApplicationTests` (L16) pin the dispatch-seam knob application: a flag-vocabulary effort
(`max`) rides the argv as `--model`/`--effort` with NO session command; `ultracode` stays OFF the
flag and arrives as the FIRST paste (`/effort ultracode`, submitted) before the brief with
`sessionCommands`/`sessionCommandsDelivered` reported; an unknown effort (`turbo`) refuses
`effort-invalid` naming claude and BOTH value sets with nothing spawned; a mapping-less builtin
(codex) stays env-only; `launchArgs` ride the argv verbatim and are recorded (payload + row);
`promptKeywords` prepend to the brief paste (the original acceptance case: strategist as
effort:max + promptKeywords:["ultracode"] → `--effort max` + the keyword riding the paste; keywords
alone still deliver with no brief); the session-layer order is effort vehicle → caller
sessionCommands → keyword-bearing brief with the RESOLVED list as provenance; and an undelivered
session command reports `sessionCommandsDelivered: false` WITH the failing pane capture as
`deliveryCapture` (`test_undelivered_session_command_is_reported_with_capture`, 260707-HFX-L3).

`SettingsDefinedHarnessTests` (L16 registry openness) write REAL settings files: a new
`orchestration.harnesses.hermes` entry spawns with its declared argv; a builtin override replaces
claude's argv while the curated knob mapping survives; an unknown-everywhere id refuses
`harness-unknown` naming the known set + `orchestration.harnesses` + the
`docs/reference/harnesses.md` manual; a vocab-less settings harness refuses effort
(`effort-invalid`) and model (`model-invalid`) with declare-or-launchArgs guidance; a declared
custom vocabulary maps the knobs onto the harness's own flags; and a repo-local entry overrides the
global one via the qualified leaf key (leafless spawns read global).

`SpawnLevelResolutionTests` (L16 rolesPerLevel, the developer's reviewer economics as the canonical
fixture) pin the resolution chain: a master-level dispatch deep-merges the level override over the
flat default (harness inherited, model/effort overridden, resolved knobs riding env + argv); the
leaf default uses the flat knobs with `spawnLevel: leaf` / `spawnLevelSource: default`; the
portfolio tier delivers `fable` + the `ultracode` session vehicle end-to-end; explicit args beat
every settings rung; a repo-local level override beats the global level override; provenance
records the resolved level + source on payload and row; default-level dispatch is unchanged for
existing callers; an unknown level refuses `level-invalid` pre-spawn; and the strategist
acceptance case expressed purely in settings (effort ultracode + promptKeywords) dispatches with
the session command + keyword-bearing brief and full provenance.
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
`TestClient`: a known running session delivers+submits (200), an unknown session is `404`
`unknown-session` with no paste attempted, and — 260707-HFX-L3 — an unconfirmed paste ships the
pane `capture` in the body while a delivered one omits it.

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

- 2026-07-07T23:20+02:00 — 260707-HFX-L3 round 2: two evidence pins added —
  `test_unconfirmed_submit_attaches_the_capture_even_when_delivered` and
  `test_failed_delivery_with_empty_capture_ships_an_explicit_marker` (the
  `"(empty pane capture)"` wording, aligned with inbox delivery).
- 2026-07-07T22:15+02:00 — 260707-HFX-L3 (capture-verified delivery): `_FakePaster` gained a scripted
  `capture`; new `test_verified_delivery_omits_the_failure_capture` and
  `test_unverified_delivery_reports_false_with_the_pane_capture_attached` (the SF-1 blind-seat
  regression); the undelivered session-command case now asserts the attached `deliveryCapture`; the
  endpoint tests pin capture-on-unconfirmed / omitted-on-delivered. Verification metadata pinned
  until closeout stamps the HFX-L3 commit.
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): added `SpawnKnobApplicationTests`,
  `SettingsDefinedHarnessTests`, and `SpawnLevelResolutionTests` (see Logic) covering the
  per-harness flag mapping, the two-vehicle claude effort vocabulary, the dispatch refusals
  (`effort-invalid`/`model-invalid`/`level-invalid`/`harness-unknown` with the manual pointer),
  the free-form escape hatch + provenance, orchestration.harnesses openness, and the rolesPerLevel
  resolution chain. Existing spawn/paste tests unmodified (one typed-access narrowing for pyright
  in a NEW L16 test only). Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-06T23:59:00+02:00 — 260703-L14 (visual hierarchy + chat grouping): added
  `test_spawn_records_role_from_env_and_reports_it` — an `env={"AR_SPAWN_ROLE": "manager"}` spawn
  persists `spawn_role` on the catalog row and reports `spawnRole` in the payload.
  Verification metadata pinned until closeout stamps the L14 commit.
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
