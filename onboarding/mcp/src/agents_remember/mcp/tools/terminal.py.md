# mcp/src/agents_remember/mcp/tools/terminal.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/src/agents_remember/mcp/tools/terminal.py`   |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-07-04T11:10+02:00                            |
| lastVerifiedCommitHash | `3c592f76ed607e4c0391fd26d77b869ee837a5af`        |
| lastVerifiedCommitDate | 2026-07-04T11:44:59+02:00|
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

`spawn_agent_session_payload(config, *, harness, leaf_key, context, submit, label, model, effort, env,
spawned_by_session, spawned_by_lifecycle, kind, session_id, host, paster, which)` composes the L2
dispatch. It first validates a `harness` kind against the detection set (`find_harness` /
`is_detected`) — an unknown or uninstalled harness short-circuits to `harness-unknown` /
`harness-not-detected` **before any spawn** (`_spawn_refusal`). It then folds `model`/`effort`/`env`
into the spawn env (`_spawn_env` — model/effort ride as namespaced `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT`
vars, caller `env` keys win), defaults spawned-by-lifecycle to the active ambient lifecycle
(`_ambient_lifecycle_id`, best-effort), and calls the shared `serving.terminal_opener`
`open_terminal_session` (the SAME opener the dashboard route uses — no parallel spawn path). On the
opener's `bad-kind`/`leaf-taken` it returns the matching `ok: false` payload (surfacing the
server-arbitrated `leaf-taken` owner, never overriding it). On `opened`, when `context` is present it
delivers the packet through a `TerminalPaster` echo-confirmed paste (`submit` presses Enter so a worker
auto-starts; a draft leaves `submit=False`) and reports `contextDelivered`/`submitted`. `host` /
`paster` / `which` / `session_id` are injectable seams for fake-driven tests.

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
  the dashboard can render the orchestration tree; the tool also carries it on its response.
- The responses remain AR-owned and strict; provider-flexible models are not used here.

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
| The spawn builder composes the shared serving opener, then an echo-confirmed context paste. | L82-L189 | [terminal.py](terminal.py) |
| The shared opener (create + leaf claim + env-seeded tmux ensure + catalog upsert) both call paths reuse. | L84-L174 | [../../serving/terminal_opener.py](../../serving/terminal_opener.py) |
| The server-side echo-confirmed paste helper that delivers the context packet. | L133-L229 | [../../serving/terminal_paste.py](../../serving/terminal_paste.py) |
| The harness detection registry (`find_harness` / `is_detected`) that gates a spawn before tmux. | L60-L72 | [../../serving/harnesses.py](../../serving/harnesses.py) |
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
