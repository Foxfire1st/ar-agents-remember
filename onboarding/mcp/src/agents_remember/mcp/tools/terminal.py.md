# mcp/src/agents_remember/mcp/tools/terminal.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/src/agents_remember/mcp/tools/terminal.py`   |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated | 2026-08-11T09:50+02:00 |
| lastVerifiedCommitHash | `3eafc555c848ac45a07a07720641f1735f8df0eb`|
| lastVerifiedCommitDate | 2026-08-21T05:15:52+02:00|
| governingOverview      | `overview.md`                                     |

## Governing Overview

[mcp/tools overview](overview.md)

## Purpose

Adapts internal terminal-session application operations. Structural public tools do not call these
exact-id payloads directly; runtime ids remain available here for operator/control-plane seams.

## Code Commentary

### Logic

Task assignment accepts a runtime session correlation plus canonical task document and role.
Spawn/retire/rename adapters continue to wrap internal application primitives. Public agent
registration uses `mcp/tools/structural_agent.py` instead.

### Conventions

This is an internal response-adapter family, not the agent-facing address vocabulary.

### Invariants And Boundaries

- Do not register exact-id terminal adapters as public agent cognition.
- Assignment has no leaf-key compatibility shape.
- Structural authorization occurs before internal runtime mutation.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Internal assignment carries session correlation plus structural binding. | `attach_terminal_session_to_task_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:27-44 |
| Legacy internal spawn/retire/rename primitives remain behind the structural application. | `spawn_agent_session_payload`; `session_retire_payload`; `session_rename_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:47-96 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 curator: repaired 2 stale citation ranges surfaced by the leaf-scoped quality check (`_RETIRE_OK_STATUSES` terminal_tools.py:914→921; `SessionRenameStatus` models/terminal.py:193→194) after the DAG line movement; no content impact on the documented contracts. Verification metadata remains closeout-owned.

- 2026-08-12T20:25+02:00 — L23 curator: re-read the typed refusal seam after spawn refusal construction moved to `application/terminal_spawn_results.py`; the wrapper still delegates and the centralized builder now owns lineage-capable refusal shape. Verification remains closeout-owned.

- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n- 2026-08-04T03:21:00+02:00 — S18-SR3-B05 curator: regenerated the separate exact-session refusal protocol binding with the locked scoped fixer and inspected the complete generated function extent; no approved semantic claim changes.
- 2026-08-04T03:03:32+02:00 — S18-SR3-B05 worker: replaced the declaration-only anchor with the refusal function and protocol-detail anchors, then returned the whole binding to provisional fixer input.
- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: removed the retired spawn-time paste/log/expectation protocol and documented the current spawned-unbriefed → readiness → durable dispatch-brief sequence; application ownership and new bindings remain provisional.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T01:22+02:00 — 260731-EFA-L4 curator: the card described `session_retire_payload` and
  `session_rename_payload` as building their own payload dicts and said nothing about status
  typing; both are now incomplete. Verified against the diff and the current source and added a
  typed-seam section: cit:([`spawn_refusal`], mcp/src/agents_remember/application/terminal_spawn_results.py:13-31)
  takes `SpawnAgentSessionStatus` at the centralized application translator, and the current `_knob_refusal` check table retains that alias while delegating refusal construction
  cit:(["def _knob_refusal("], mcp/src/agents_remember/application/terminal_tools.py:466-484); the new
  cit:([`_retire_payload`], mcp/src/agents_remember/application/terminal_tools.py:917-952)
  and cit:([`_rename_payload`], mcp/src/agents_remember/application/terminal_tools.py:1090-1111) are the
  single builders for their tools' results, so
  cit:([`session_retire_payload`], mcp/src/agents_remember/mcp/tools/terminal.py:66-83) and
  cit:([`session_rename_payload`], mcp/src/agents_remember/mcp/tools/terminal.py:86-95) no
  longer restate the shape at each call site;
  cit:([`_RETIRE_OK_STATUSES`], mcp/src/agents_remember/application/terminal_tools.py:921-921) gives
  `SessionRetireResponse.ok` one owner. The aliases are imported from `models/terminal.py`
  cit:([`SpawnAgentSessionStatus`, `SessionRetireStatus`, `SessionRenameStatus`], mcp/src/agents_remember/models/terminal.py:51-82; mcp/src/agents_remember/models/terminal.py:161-167; mcp/src/agents_remember/models/terminal.py:194-194)
  to avoid the cycle. Recorded
  the finding that `SpawnAgentSessionStatus` folds in `worktrees/leaf_refs.py::LeafRefStatus`, so
  two of the thirteen spawn statuses are produced entirely outside any file enumerating spawn
  refusals — and that the `spawn_agent_session` docstring rosters only eleven of the thirteen, a
  gap pinned by `test_every_status_the_session_tools_roster_validates` rather than edited, because
  the docstring is the published MCP tool description. Every status, field and `ok` value is
  otherwise unchanged. Added three invariants and four reference rows. **Citation repairs** — all
  ten line ranges in the two reference tables were re-checked and none of the numeric ones landed
  on their claimed symbol: `terminal.py` L16-L42 (a docs row about serving behaviour) → the
  module's serving imports L1-L60; `terminal_opener.py` L170-L648 → `open_terminal_session`
  L620-L672; `terminal_paste.py` L133-L229 → `TerminalPaster` L206-L511; `harnesses.py` L41-L73 →
  `HARNESSES` L76-L103, `find_harness` L105-L114, `is_detected` L130-L137; `base.py` L18-L20 →
  `PUBLIC_TOOLS` L18-L77 (the two names sit at L23-L24, outside the old range);
  `mcp/tools/__init__.py` L86; L94 → imports L72-L75 and the `__all__` entries at L97/L143-L144/L146
  (and the row widened to four builders, since retire/rename are re-exported too);
  `tool_registry.py` L82-L88; L111-L114 → imports L83-L87, registry L121-L125 (and the row widened
  to name all four models). The two rows citing bare symbol names (`attach_terminal_session_to_leaf_payload`,
  `spawn_agent_session_payload`) gained verified ranges.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: `spawn_agent_session_payload` took the
  `seat`/`retired`/`spawned_by`/`overrides` parameter objects (`SpawnSeat`, `RetiredSpawnInputs`,
  `SpawnedBy`, `SpawnOverrides` — the last renamed from `SpawnPorts`, with the reason recorded on the
  type), and `_resolve_spawn_harness` split into `_requested_harness` / `_preferred_harness` /
  `_first_detected_harness`. `retire_entry` now takes a `SeatClosure`. Refusal vocabulary, precedence
  and every payload field are unchanged, and the published MCP signature stays flat. Verification
  metadata pinned until closeout stamps the L2 code commit.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented role-spawn conflict mapping,
  no alternate spawn or provenance rewrite, and corrected the inherited overbroad lock-free-reader
  statement while preserving settings-owned role dispatch.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented complete role selection,
  typed native launch carriage, runner-side dynamic validation, provenance-only spawn env, the
  no-synthesized-paste invariant, and the retained explicit non-native mapping path. Verification
  metadata remains pinned until closeout stamps the L2 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T21:05+02:00 — Super-exit curator correction: clarified that only session-command
  rows use `envelope=False`; the brief row uses `envelope=True` with its existing unique id envelope.

- 2026-07-10T18:30+02:00 — 260707-HFX2-L18: documented the behavior-preserving
  `_resolve_spawn_leaf` extraction and flat dispatch-local controller flow. The strict CRAP score for
  `spawn_agent_session_payload` fell from `34.25` to `23.02`; settings-owned spend protection, L17
  pair arbitration/log binding, public payloads, and threshold/configuration remain unchanged.
  Verification metadata remains pinned until closeout stamps the eventual L18 code commit.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: threaded seat role through attach/spawn payloads and
  expectation rows, and switched retirement checks to binding identity with replacement-leaf
  recovery. Verification metadata remains pinned until closeout stamps L17.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: replaced capture/turn-start spawn credit with bound-log
  user/command evidence, added targeted command reissue and catalog log binding, recorded resolved
  knobs plus `replacementForLeaf`, and extended expectation rows to declared replacements.
  Verification metadata remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 (spawn settings authority): `spawn_agent_session_payload`
  now rejects ordinary caller spend overrides before any side effect (`harness`/`model`/`effort`,
  direct launch/session controls, `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT`, and maintained Claude/Anthropic
  + Codex/OpenAI harness-native spend/env keys) with `spend-override-unsupported`. Harness/model/
  effort/free-form resolution is settings-only: repo-local level override > global level override >
  repo-local role default > global role default > spawn preference/detection. Documented the accepted
  reviewer note that the blocklist is maintained but not mathematically exhaustive. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L10 commit.
- 2026-07-08T22:30+02:00 — 260707-HFX2-L3 (paste injector hardening, R3): `_deliver_spawn_pastes`
  gained `entry_id`/`harness` parameters and now builds session-command `DeliveryRow`s
  (`envelope=False`, raw text unchanged) plus a brief `DeliveryRow` (`envelope=True`, existing
  unique id envelope), all passed to `serving.injector.deliver` — the raw-spawn seam's separate delivery loop is
  retired; the SAME one path `serving/inbox_delivery.py` uses. `_SpawnDelivery`'s boolean fields keep
  their exact pre-existing meaning, mapped from the richer `DeliveryOutcome`. Every existing
  `test_spawn_agent_session.py` assertion (including exact `paster.calls[...]["text"]` equality)
  passes UNCHANGED. Verification metadata pinned until closeout stamps the 260707-HFX2-L3 commit.
- 2026-07-08T14:35+02:00 — 260707-HFX2-L1: `spawn_agent_session_payload` now atomically writes R2 expectation rows via `_write_spawn_expectation_rows` — always a `briefed-by` row, plus a `turn-report-by` row when the spawn claims a leaf (`leaf_key` set). Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-07-08T02:43+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity): two new
  payload builders, `session_retire_payload` (authority-checked retire: unknown-session/
  unknown-actor/already-retired/retire-refused/retired statuses, kills the tmux session + persists
  retirement provenance, idempotent) and `session_rename_payload` (unknown-session/renamed,
  identity text only). Both delegate mechanics to the new `serving/retire.py` + `retire_policy.py` +
  `seat_events.py` modules and conform to the new `SessionRetireResponse`/`SessionRenameResponse`
  models. `actor_session_id` is self-declared (no ambient caller-identity resolution exists in this
  codebase) — an accepted residual risk per the leaf's builder/reviewer record. Verification
  metadata pinned until closeout stamps the HFX-L8 commit.
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
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: attach and spawn now normalize accepted leaf refs to
  canonical qualified task-doc ids before catalog writes/spawn provenance, and return strict
  `leaf-ref-not-found` / `leaf-ref-ambiguous` refusals with expected form plus candidates before any
  mutation. Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
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
