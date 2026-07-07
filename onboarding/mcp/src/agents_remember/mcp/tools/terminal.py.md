# mcp/src/agents_remember/mcp/tools/terminal.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/src/agents_remember/mcp/tools/terminal.py`   |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-07-07T23:20+02:00                            |
| lastVerifiedCommitHash | `551695279f403ab19c0eba4ce6f6cfde6a8bb1f5`        |
| lastVerifiedCommitDate | 2026-07-07T20:09:01+02:00|
| governingOverview      | `overview.md`                                     |

## Governing Overview

[mcp/tools overview](overview.md)

## Purpose

`terminal.py` contains MCP payload builders for dashboard terminal-session catalog operations. It
exposes the agent-facing path for moving an already-created hosted terminal/chat session to a durable
task leaf (`attach_terminal_session_to_leaf`), and — since L2 — `spawn_agent_session`, which
**creates** a role-configured, leaf-attached, context-primed hosted session by composing the existing
serving primitives so an orchestrator can spawn a manager and a manager a worker without dashboard
clicks.

## Code Commentary

### Logic

`attach_terminal_session_to_leaf_payload(config, session_id, leaf_key)` opens the dashboard terminal
catalog at `terminal_catalog_path(config.coordination_root)`, calls the serving-layer
`assign_terminal_session_to_leaf` helper, and returns the result through `_tool_payload` under the
`attach_terminal_session_to_leaf` operation. The payload reports `ok` only for `attached`, and always
includes the requested session/leaf plus optional `previousLeafKey`, `ownerSession`, and role.

`spawn_agent_session_payload(config, *, harness=None, leaf_key, context, submit, label, model, effort,
env, launch_args, prompt_keywords, session_commands, level, spawned_by_session, spawned_by_lifecycle,
kind, session_id, host, paster, which)` composes the L2 dispatch, now the full 260703-L16 knob
resolution + application seam. For a `harness` kind it:

1. **Resolves the dispatch level** (`level` param, `leaf|master|portfolio`, default `leaf`;
   `_SPAWN_LEVELS` mirrors the `loops.perLevel` vocabulary) — an unknown level refuses
   `level-invalid` before anything else; the resolved level + its source (`explicit`/`default`) ride
   to spawn provenance.
2. **Reads the agentic settings per-use** (`load_agentic_settings`, repo-local layer selected by the
   qualified leaf key via `_spawn_repo_root`) and computes the settings rungs:
   `settings.resolved_role_knobs(env["AR_SPAWN_ROLE"], level)` — the `rolesPerLevel[level]` override
   deep-merged over the flat `roles` default (no role riding = no settings rung). Unset explicit
   args fold in from the knobs (model, effort, launchArgs, promptKeywords, sessionCommands), giving
   the chain explicit args > repo-local level override > global level override > repo-local role
   default > global role default > spawn preference > detection-gated default.
3. **Resolves the harness against the EFFECTIVE registry** (`_resolve_spawn_harness(settings,
   harness or knobs.harness, which)` — `settings.harnesses` is the builtin table merged with
   `orchestration.harnesses`, so settings-defined harnesses and pre-customized builtins resolve;
   an id known nowhere refuses `harness-unknown` with the `unknown_harness_detail` text naming the
   known set + the `docs/reference/harnesses.md` manual; undetected → `harness-not-detected`,
   configured-preference refusals still name the settings source).
4. **Validates the knobs pre-spawn**: `invalid_model_detail`/`invalid_effort_detail` on the
   EFFECTIVE values (env wins over arg wins over settings) — `model-invalid`/`effort-invalid`
   refusals name the harness and its valid sets (the L16 silent-degrade prevention); a
   session-vocabulary effort (claude `ultracode`) contributes `effort_session_commands` as the FIRST
   post-launch session command instead of a flag.
5. **Spawns through the shared opener** (`open_terminal_session`, the SAME opener the dashboard
   route uses — no parallel spawn path) with the env-folded knobs (`_spawn_env` — resolved
   model/effort ride as `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT`, caller env keys win), the verbatim
   `launch_args`, the free-form provenance, the level provenance, and the effective registry.
6. **Delivers the session layer**: each resolved session command is its own capture-verified paste
   with `submit=True` (an unexecuted `/effort ultracode` would be a silent downgrade;
   `sessionCommandsDelivered` aggregates delivered+submitted), THEN the brief — `prompt_keywords`
   are prepended as its first line (delivered alone when no `context` is given) — with the existing
   `submit` semantics and `contextDelivered`/`submitted` reporting. Since 260707-HFX-L3
   `_deliver_spawn_pastes` returns the frozen `_SpawnDelivery` bundle: every `True` is
   capture-verified by the paster (a `False` means the pane provably shows no trace of the paste),
   and `failure_capture` carries the pane capture of the latest failed paste. `_spawned_payload`
   ships it as `deliveryCapture` — attached on ANY `False` outcome, `None` (omitted) on full
   success — so a blind seat (SF-1: `contextDelivered: true` over a clean-booted codex pane) is
   diagnosable from the result itself, never trusted from a boolean.

On the opener's `bad-kind`/`leaf-taken` it returns the matching `ok: false` payload (surfacing the
server-arbitrated `leaf-taken` owner, never overriding it). The `spawned` payload echoes the
recorded provenance: `launchArgs`/`promptKeywords`/`sessionCommands` (the RESOLVED list, effort
vehicle first), `spawnLevel`/`spawnLevelSource`. `host` / `paster` / `which` / `session_id` remain
injectable seams for fake-driven tests.

Helper decomposition (CRAP-gate driven): steps 1-4 live in `_resolve_harness_dispatch` (returning a
frozen `_HarnessDispatch` bundle or a refusal, with `_knob_refusal` for the model/effort checks);
step 6 is `_brief_packet` (keyword prepending) + `_deliver_spawn_pastes` (session commands then
brief, returning `_SpawnDelivery`); the `spawned` response dict is `_spawned_payload`.

### Conventions

Builders stay transport-thin: durable spawn/paste behavior lives in `serving.terminal_opener` +
`serving.terminal_paste`, leaf reassignment in `serving.terminal_leaf_assignment`, response validation
is `_tool_payload` + `models/terminal.py`, and server registration lives in `mcp/server.py`.

### Invariants And Boundaries

- These tools mutate the same dashboard catalog as the browser route; `attach` does not create a new
  terminal, and `spawn_agent_session` spawns tmux + upserts a catalog row directly (in-process, over
  the shared opener) rather than calling the running daemon — no HTTP hop, no daemon-reachability
  dependency, the same posture as `attach`.
- `leaf-taken` / `unknown-session` (attach) and `leaf-taken` / `harness-unknown` /
  `harness-not-detected` / `bad-kind` (spawn) are successful tool responses with `ok: false`; callers
  branch on `status`, not exceptions.
- Leaf uniqueness stays server-arbitrated: `spawn_agent_session` surfaces `leaf-taken` (with the owning
  session) and never overrides it.
- Spawned-by provenance (`spawnedBySession` + `spawnedByLifecycle`) is recorded on the catalog row so
  the dashboard can render the orchestration tree; the tool also carries it on its response. Since
  L14 the `spawned` payload also reports `spawnRole` — the `AR_SPAWN_ROLE` the opener persisted from
  the caller's `env` (omitted when the spawn carried no role), the Chats command-tree grouping key.
- The responses remain AR-owned and strict; provider-flexible models are not used here.
- Knob resolution precedence (L16) is explicit args > repo-local level override > global level
  override > repo-local role default > global role default > spawn preference > detection-gated
  default; settings are read PER-USE (an edit applies to the next spawn, no restart), and the
  `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT` env riding is preserved — L16 ADDS the argv application on top
  (per-harness flags via the effective registry; env-only harnesses unchanged at the argv).
- The free-form escape hatch (`launchArgs`/`promptKeywords`/`sessionCommands`) is NEVER validated —
  only recorded in spawn provenance (catalog row + payload); the validated-enum refusals
  (`effort-invalid`/`model-invalid`/`level-invalid`) fire before any spawn, naming the harness and
  its valid sets with launchArgs/sessionCommands guidance.
- Paste ordering is a contract: session commands (effort vehicle first, then the caller's) BEFORE
  the promptKeywords-bearing brief — session-level modes must be active before the brief submits.
- Delivery booleans are capture-verified, never optimistic (260707-HFX-L3): `contextDelivered` /
  `sessionCommandsDelivered` report `True` only after the paster proved the paste on the pane, and
  any `False` outcome ships the failing pane capture as `deliveryCapture` — callers must treat such
  a seat as blind, never assume the brief landed.

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation found; this is a local MCP wrapper around the dashboard
catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The operation is defined by same-repository serving/catalog behavior rather than external documentation. | L16-L42 | [terminal.py](terminal.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The attach builder delegates durable assignment to the shared serving helper and returns previous leaf, owner, status, and role. | L25-L51 | [terminal.py](terminal.py) |
| The spawn builder composes the shared serving opener, then a capture-verified context paste. | L82-L189 | [terminal.py](terminal.py) |
| The shared opener (create + leaf claim + env-seeded tmux ensure + catalog upsert) both call paths reuse. | L84-L174 | [../../serving/terminal_opener.py](../../serving/terminal_opener.py) |
| The server-side capture-verified paste helper that delivers the context packet (and attaches the failure capture). | L133-L229 | [../../serving/terminal_paste.py](../../serving/terminal_paste.py) |
| The harness detection registry (`find_harness` / `is_detected` / `HARNESSES` order) that gates a spawn before tmux and orders the detection-gated default. | L41-L72 | [../../serving/harnesses.py](../../serving/harnesses.py) |
| The per-use agentic-settings loader supplying `spawn_harness` (registry-id validated). | load_agentic_settings | [../../kernel/agentic_settings.py](../../kernel/agentic_settings.py) |
| The public tool tuple advertises `attach_terminal_session_to_leaf` and `spawn_agent_session`. | L18-L20 | [base.py](base.py) |
| The facade re-exports both payload builders. | L86; L94 | [__init__.py](__init__.py) |
| The FastMCP server registers `attach_terminal_session_to_leaf` and the L2 `spawn_agent_session(harness, leaf_key, context, submit, model, effort, env, …)`. | L146-L189 | [../server.py](../server.py) |
| The strict response models (`AttachTerminalSessionToLeafResponse`, `SpawnAgentSessionResponse`) are registered for conformance validation. | L82-L88; L111-L114 | [../../models/tool_registry.py](../../models/tool_registry.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tool operates on the local dashboard terminal catalog only. | - | - |

## Update History

- 2026-07-07T23:20+02:00 — 260707-HFX-L3 round 2: a False outcome never ships evidence-less —
  `_deliver_spawn_pastes` gained a `failed` flag and the explicit `"(empty pane capture)"` marker
  (wording aligned with `inbox_delivery`) so `deliveryCapture` is present on every failure, and the
  capture also attaches on submit-failure (not only undelivered).
- 2026-07-07T22:15+02:00 — 260707-HFX-L3 (capture-verified delivery): `_deliver_spawn_pastes` returns
  the frozen `_SpawnDelivery` bundle — `contextDelivered`/`sessionCommandsDelivered` are `True` only
  from verified delivery, and `failure_capture` (the paster's final pane snapshot from the latest
  failed paste) rides `_spawned_payload` as `deliveryCapture` on any `False` outcome (omitted on
  full success). Closes the SF-1 blind seat: `contextDelivered: true` once masked a codex pane that
  booted clean with no payload. Verification metadata pinned until closeout stamps the HFX-L3
  commit.
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application; four developer rulings 2026-07-07):
  the dispatch seam now RESOLVES role knobs from settings (`resolved_role_knobs(AR_SPAWN_ROLE,
  level)` — `rolesPerLevel` over flat `roles`; new `level` param leaf|master|portfolio with
  provenance), resolves harnesses against the EFFECTIVE registry (`orchestration.harnesses` — new
  ids add, builtin ids pre-customize; unknown-everywhere ids refuse pointing at the
  `docs/reference/harnesses.md` manual), VALIDATES model/effort per-harness before spawning
  (`effort-invalid`/`model-invalid`/`level-invalid` refusal statuses; claude's two-vehicle effort
  vocabulary with `ultracode` delivered as a post-launch `/effort` session command), and delivers
  the free-form escape hatch (`launch_args` verbatim argv; `session_commands` pasted+submitted
  before the brief; `prompt_keywords` prepended to the brief paste) — never validated, recorded in
  spawn provenance and echoed on the payload. Verification metadata pinned until closeout stamps
  the L16 commit.

- 2026-07-06T23:58:24+02:00 — 260703-L14 (visual hierarchy + chat grouping): the `spawned` payload now
  reports `spawnRole` (`entry.spawn_role` — the AR_SPAWN_ROLE the shared opener recorded on the
  catalog row from the caller's env; `_tool_payload` omits it when `None`). No builder logic
  changed. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T22:25+02:00 — 260703-L13 (settings unification): `harness` became optional —
  `_resolve_spawn_harness` implements explicit arg > repo-local settings > global settings >
  detection-gated default, reading the agentic settings per-use with the repo-local layer
  derived from the qualified leaf key (`_spawn_repo_root`); refusal payloads name the
  settings source; `_spawn_refusal` accepts a None harness. Verification metadata pinned
  until closeout stamps the L13 commit.
- 2026-07-04T11:10+02:00 — L2: added `spawn_agent_session_payload` (+ `_spawn_env` / `_ambient_lifecycle_id`
  / `_spawn_refusal` helpers) — the agent-facing dispatch tool that composes the shared serving opener
  (`terminal_opener.open_terminal_session`) plus an echo-confirmed context paste
  (`terminal_paste.TerminalPaster`). It validates the harness against the detection set before spawning,
  injects model/effort/env at spawn, records spawned-by provenance, surfaces server-arbitrated
  `leaf-taken` without override, and optionally submits so a worker auto-starts. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-02T17:04+02:00 — L9: created the agent-facing `attach_terminal_session_to_leaf` payload
  builder so agents can move their own hosted dashboard chats between task leaves without raw dashboard
  curl or browser clicks. Verification metadata pinned to the task base until closeout stamps the L9
  commit.
