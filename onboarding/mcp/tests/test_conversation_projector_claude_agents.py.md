# mcp/tests/test_conversation_projector_claude_agents.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_projector_claude_agents.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:45+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Claude projector sub-agent mapping tests (D6): sidechain correlation by
`parent_tool_use_id`, the `task_*` roster lifecycle, and the `--forward-subagent-text`
launch-flag floor — proving claude sub-agent work is bound to an honest agent identity
instead of being silently flattened into the parent timeline.

## Code Commentary

### Logic

Fixtures are synthesized minimal frames matching the shapes probe-locked on the installed
claude 2.1.220 (2026-07-26 live stream-json probes; the module docstring L1-L17 pins the
exact verified field sets: `task_progress`/`task_notification` `usage` is exactly
`{total_tokens, tool_uses, duration_ms}`, `background_tasks_changed` entries exactly
`{task_id, task_type, description}`, Agent spawn `input` exactly `{description, prompt,
run_in_background, subagent_type}`, and sidechain `tool_result` content crosses as a plain
string while the parent-carried Agent result keeps list content). Each test drives a
distinct vendor session id so the session-keyed binding registry never leaks across cases.

cit:([`ClaudeAgentLifecycleTests`], mcp/tests/test_conversation_projector_claude_agents.py:219-466) maps frames directly through
`claude.map_evidence_frame`: the full lifecycle (spawn tool_use → `task_started` →
sidechain user/assistant/tool-cycle → `task_progress` → `task_notification` → Agent
tool_result) binds identity and upserts one roster row.
`test_full_lifecycle_binds_identity_and_upserts_roster` is a six-line sequence over six
`_assert_*` helpers, one per frame stage —
`_assert_spawn_call_is_untagged`, `_assert_task_started_binds_the_roster_and_tags_the_call`,
`_assert_sidechain_records_are_bound`, `_assert_task_progress_upserts_usage`,
`_assert_task_notification_completes_the_roster_row`, and
`_assert_tool_result_settles_the_bound_call`. They are stages, not independent tests: they share
one session and the projector's per-session binding state, so they must run in that order (the
ninth frame's settlement only means something because the second frame bound the identity it
settles). Across the six: the spawning Agent call stays an
untagged parent tool-call until `task_started` tags it and mints the roster
(`claude-agent-<task_id>` with join key, role, description); sidechain items bind the
agent ref; `task_progress` carries usage + last tool; the terminal `task_notification`
keeps the roster row whole across a replacement upsert that carries no
description/subagent_type; the Agent tool_result carrier settles the tool-call with the
bound identity. Parent-timeline items carry no agent ref. A sidechain arriving BEFORE
`task_started` falls back honestly: the join key IS the id, status `unknown`, until the
binder lands. Malformed `task_*`/`background_tasks_changed` frames degrade to preserved
unknown-vendor (`claude-system:<subtype>`); unmapped system subtypes keep dropping
silently. `background_tasks_changed` registers an unknown task once — the richer `task_*`
authority owns the row afterward, and a late `task_started` still binds the join key onto
the same row; an empty task set reconciles nothing.

cit:([`ClaudeLaunchFlagTests`], mcp/tests/test_conversation_projector_claude_agents.py:469-491) pin the fail-closed `--forward-subagent-text` floor
(fix-round finding 8): the flag is emitted only when the caller proved the floor
(`forward_subagent_text=True`), never by default and never duplicated;
`forward_subagent_text_supported` accepts 2.1.220/2.2.0 and refuses 2.1.219 and below,
unparseable versions, and `None`.

### Conventions

Direct mapper tests on `unittest.TestCase` with fixed timestamps; per-test unique session
ids isolate the session-keyed binding registry. Probe captures are evidence references
(retained in local probe scratch space at implementation time), not committed fixtures.

### Invariants And Boundaries

- Identity is evidence-bound: the join key stands in until `task_started` proves the real
  task id; no fabricated names.
- Terminal roster upserts merge: a notification lacking description/subagent_type never
  wipes the bound record.
- The launch flag is fail-closed: emitted only behind a proven version floor.
- Malformed task frames degrade to preserved unknown-vendor; unmapped subtypes stay silent.

### Todos

The claude floor probe + re-launch has a startup cost and no flagless fallback (accepted
residual N3): below-floor or unparseable installs run without sub-agent text forwarding.

## Docs References

No Domain Documentation source is configured; the frame shapes are probe-locked against
the installed claude runtime as recorded in the module docstring.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The claude mapper under test: sidechain binding registry, task_* roster grammar, unknown-vendor degrade. | `_AgentBindingRegistry` | mcp/src/agents_remember/serving/conversation/projectors/claude.py:122-159; mcp/src/agents_remember/serving/conversation/projectors/claude.py:210-210; mcp/src/agents_remember/serving/conversation/projectors/claude.py:286-299 |
| The launch-flag builder and floor verdict under test. | `forward_subagent_text_supported` | mcp/src/agents_remember/serving/claude_stream_protocol.py:77-114 |
| The reordered-binder engine companion (tool_result settling before task_started keeps the terminal phase). | `test_reordered_task_started_tagging_never_regresses_a_terminal_phase` | mcp/tests/test_conversation_active_service_queues.py:104-177 |
| The flag-floor probe/relaunch flow at the adapter level. | `test_forward_subagent_text_relaunches_with_the_flag_at_or_above_the_floor` | mcp/tests/test_harness_control_claude_stream_1.py:248-273 |

## Cross-Repo References

No neighboring repository participates; the vendor boundary is the installed claude
stream-json runtime probed live during implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 4 citation rows (mapper
  registry/grammar ranges, floor verdict + argv builder 77-114, the reordered-binder engine
  companion 982-1053, the adapter floor flow 471-496). Zero findings remain.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep.
  `test_full_lifecycle_binds_identity_and_upserts_roster` was too complex for the tightened
  `C901`/`PLR0915` gate and has been split: the test body is now six calls to six `_assert_*`
  helper methods, one per frame stage, each carrying the comment that used to sit inline as its
  docstring. Rewrote the `ClaudeAgentLifecycleTests` paragraph to name the six helpers and to
  record that they are ordered stages sharing one session and the projector's per-session binding
  state, not independent tests. Also corrected both class line ranges — `ClaudeAgentLifecycleTests`
  L219-L466 (was L219-L452) and `ClaudeLaunchFlagTests` L469-L491 (was L455-L477) — for the lines
  the split and the `ruff format` reflow moved. The mapped frames, the nine sequence numbers, and
  every assertion are unchanged.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: created the sidecar for the new claude
  projector sub-agent suite (D6; fix-round finding 8 flag-floor pins). Verification is
  blank because the new source file is uncommitted; closeout owns its first source stamp.
