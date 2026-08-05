# mcp/src/agents_remember/application/terminal_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/terminal_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Application operations for terminal-session lifecycle tools.

## Code Commentary

### Logic

Module-level surface:

- `_result` (function, lines 70-72) — Return the raw use-case result for the MCP adapter to finalize.
- `_leaf_ref_refusal_result` (function, lines 75-92)
- `attach_terminal_session_to_leaf_tool` (function, lines 140-177) — Move an existing hosted terminal/chat session to a durable leaf key.
- `_spawn_env` (function, lines 180-196) — Fold the role knobs into the spawn env the terminal host seeds at ``tmux new-session``.
- `_ambient_lifecycle_id` (function, lines 199-204) — The active (spawning) lifecycle id, for default spawned-by provenance. Best-effort, never raises.
- `_spawn_repo_root` (function, lines 207-219) — The code-repo root whose repo-local agentic settings apply to this spawn.
- `_resolve_spawn_harness` (function, lines 222-243) — Resolve the harness for a spawn (260703-L13 seam; effective registry 260703-L16).
- `_requested_harness` (function, lines 246-265) — The caller named a harness: it must be a known id AND installed.
- `_preferred_harness` (function, lines 268-285) — Settings named a spawn harness: a configured-but-missing one names its source file.
- `_first_detected_harness` (function, lines 288-304) — Nothing asked for and nothing configured: the first registry harness on PATH.
- `_HarnessDispatch` (class, lines 308-325) — The pre-spawn knob bundle for one harness-kind dispatch (260703-L16).
- `_resolve_harness_dispatch` (function, lines 328-420) — Resolve + validate every knob BEFORE anything spawns (260703-L16).
- `_knob_refusal` (function, lines 423-441) — Preserve explicit static validation for settings-defined non-native harnesses.
- `SpawnSeat` (class, lines 445-455) — The seat a spawn creates: which leaf it binds to (or replaces), at what dispatch level,
- `RetiredSpawnInputs` (class, lines 459-476) — Spawn inputs this tool no longer honours, accepted only so they can be refused loudly
- `SpawnedBy` (class, lines 480-485) — The spawner's own provenance: the catalog session and lifecycle that requested the
- `SpawnOverrides` (class, lines 489-511) — Real collaborators a caller may substitute. The seam is the whole content of this
- `_caller_spend_override_refusal` (function, lines 527-564) — Reject legacy caller-controlled spend knobs before any spawn-side effect.
- `_brief_delivery_separate_refusal` (function, lines 567-581) — Refuse the retired one-call brief contract before any settings, catalog, or spawn work.
- `_SpawnDelivery` (class, lines 585-589) — Launch-phase session-command outcome; task instructions are never represented here.
- `_spawn_request_refusal` (function, lines 592-602) — Refuse a request this tool no longer honours, before any settings, catalog, or spawn work.
- `_resolve_spawn_leaf` (function, lines 605-614) — Resolve one optional spawn leaf reference, preserving the public refusal payload.
- `_resolve_spawn_leaves` (function, lines 617-629) — Resolve both spawn leaf references; the first unresolvable one refuses the spawn.
- `_open_terminal_refusal` (function, lines 632-660) — Translate a non-opened terminal outcome into its public refusal payload.
- `_SpawnLaunchPlan` (class, lines 664-681) — What one spawn will actually launch, after the settings rungs have been read.
- `_spawn_launch_plan` (function, lines 684-732) — The launch plan for one spawn, or the refusal that stops it before any side effect.
- `_spawn_launch_request` (function, lines 735-766) — The launch request the terminal opener receives, assembled from the plan.
- `spawn_agent_session_tool` (function, lines 769-842) — Spawn one role-configured, leaf-attached hosted session without a leaf brief.
- `_spawned_payload` (function, lines 845-877) — The spawned-unbriefed row plus settings-owned launch-command outcome.
- `_spawn_refusal` (function, lines 880-905) — A pre-spawn refusal payload (unknown/undetected harness or bad kind) -- nothing was spawned.
- `_retire_payload` (function, lines 914-941) — One ``session_retire`` result: the status, plus whichever half of the shape it carries.
- `session_retire_tool` (function, lines 944-1001) — Retire ``session_id`` (issue #12): terminal mark + provenance, authority enforced server-side.
- `_rename_payload` (function, lines 1004-1025) — One ``session_rename`` result: the REQUESTED label on a refusal, the stored pair on success.
- `session_rename_tool` (function, lines 1028-1042) — Rename ``session_id``'s display label post-spawn (issue #4). Identity text only -- never role.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the function `_result` (lines 70-72) — Return the raw use-case result for the MCP adapter to finalize.. | `_result` | mcp/src/agents_remember/application/terminal_tools.py:70-72 |
| Defines the function `_leaf_ref_refusal_result` (lines 75-92). | `_leaf_ref_refusal_result` | mcp/src/agents_remember/application/terminal_tools.py:75-92 |
| Defines the function `attach_terminal_session_to_leaf_tool` (lines 140-177) — Move an existing hosted terminal/chat session to a durable leaf key.. | `attach_terminal_session_to_leaf_tool` | mcp/src/agents_remember/application/terminal_tools.py:140-177 |
| Defines the function `_spawn_env` (lines 180-196) — Fold the role knobs into the spawn env the terminal host seeds at ``tmux new-session``.. | `_spawn_env` | mcp/src/agents_remember/application/terminal_tools.py:180-196 |
| Defines the function `_ambient_lifecycle_id` (lines 199-204) — The active (spawning) lifecycle id, for default spawned-by provenance. Best-effort, never raises.. | `_ambient_lifecycle_id` | mcp/src/agents_remember/application/terminal_tools.py:199-204 |
| Defines the function `_spawn_repo_root` (lines 207-219) — The code-repo root whose repo-local agentic settings apply to this spawn.. | `_spawn_repo_root` | mcp/src/agents_remember/application/terminal_tools.py:207-219 |
| Defines the function `_resolve_spawn_harness` (lines 222-243) — Resolve the harness for a spawn (260703-L13 seam; effective registry 260703-L16).. | `_resolve_spawn_harness` | mcp/src/agents_remember/application/terminal_tools.py:222-243 |
| Defines the function `_requested_harness` (lines 246-265) — The caller named a harness: it must be a known id AND installed.. | `_requested_harness` | mcp/src/agents_remember/application/terminal_tools.py:246-265 |
| Defines the function `_preferred_harness` (lines 268-285) — Settings named a spawn harness: a configured-but-missing one names its source file.. | `_preferred_harness` | mcp/src/agents_remember/application/terminal_tools.py:268-285 |
| Defines the function `_first_detected_harness` (lines 288-304) — Nothing asked for and nothing configured: the first registry harness on PATH.. | `_first_detected_harness` | mcp/src/agents_remember/application/terminal_tools.py:288-304 |
| Defines the class `_HarnessDispatch` (lines 308-325) — The pre-spawn knob bundle for one harness-kind dispatch (260703-L16).. | `_HarnessDispatch` | mcp/src/agents_remember/application/terminal_tools.py:307-325 |
| Defines the function `_resolve_harness_dispatch` (lines 328-420) — Resolve + validate every knob BEFORE anything spawns (260703-L16).. | `_resolve_harness_dispatch` | mcp/src/agents_remember/application/terminal_tools.py:328-420 |
| Defines the function `_knob_refusal` (lines 423-441) — Preserve explicit static validation for settings-defined non-native harnesses.. | `_knob_refusal` | mcp/src/agents_remember/application/terminal_tools.py:423-441 |
| Defines the class `SpawnSeat` (lines 445-455) — The seat a spawn creates: which leaf it binds to (or replaces), at what dispatch level,. | `SpawnSeat` | mcp/src/agents_remember/application/terminal_tools.py:444-455 |
| Defines the class `RetiredSpawnInputs` (lines 459-476) — Spawn inputs this tool no longer honours, accepted only so they can be refused loudly. | `RetiredSpawnInputs` | mcp/src/agents_remember/application/terminal_tools.py:458-476 |
| Defines the class `SpawnedBy` (lines 480-485) — The spawner's own provenance: the catalog session and lifecycle that requested the. | `SpawnedBy` | mcp/src/agents_remember/application/terminal_tools.py:479-485 |
| Defines the class `SpawnOverrides` (lines 489-511) — Real collaborators a caller may substitute. The seam is the whole content of this. | `SpawnOverrides` | mcp/src/agents_remember/application/terminal_tools.py:488-511 |
| Defines the function `_caller_spend_override_refusal` (lines 527-564) — Reject legacy caller-controlled spend knobs before any spawn-side effect.. | `_caller_spend_override_refusal` | mcp/src/agents_remember/application/terminal_tools.py:527-564 |
| Defines the function `_brief_delivery_separate_refusal` (lines 567-581) — Refuse the retired one-call brief contract before any settings, catalog, or spawn work.. | `_brief_delivery_separate_refusal` | mcp/src/agents_remember/application/terminal_tools.py:567-581 |
| Defines the class `_SpawnDelivery` (lines 585-589) — Launch-phase session-command outcome; task instructions are never represented here.. | `_SpawnDelivery` | mcp/src/agents_remember/application/terminal_tools.py:584-589 |
| Defines the function `_spawn_request_refusal` (lines 592-602) — Refuse a request this tool no longer honours, before any settings, catalog, or spawn work.. | `_spawn_request_refusal` | mcp/src/agents_remember/application/terminal_tools.py:592-602 |
| Defines the function `_resolve_spawn_leaf` (lines 605-614) — Resolve one optional spawn leaf reference, preserving the public refusal payload.. | `_resolve_spawn_leaf` | mcp/src/agents_remember/application/terminal_tools.py:605-614 |
| Defines the function `_resolve_spawn_leaves` (lines 617-629) — Resolve both spawn leaf references; the first unresolvable one refuses the spawn.. | `_resolve_spawn_leaves` | mcp/src/agents_remember/application/terminal_tools.py:617-629 |
| Defines the function `_open_terminal_refusal` (lines 632-660) — Translate a non-opened terminal outcome into its public refusal payload.. | `_open_terminal_refusal` | mcp/src/agents_remember/application/terminal_tools.py:632-660 |
| Defines the class `_SpawnLaunchPlan` (lines 664-681) — What one spawn will actually launch, after the settings rungs have been read.. | `_SpawnLaunchPlan` | mcp/src/agents_remember/application/terminal_tools.py:663-681 |
| Defines the function `_spawn_launch_plan` (lines 684-732) — The launch plan for one spawn, or the refusal that stops it before any side effect.. | `_spawn_launch_plan` | mcp/src/agents_remember/application/terminal_tools.py:684-732 |
| Defines the function `_spawn_launch_request` (lines 735-766) — The launch request the terminal opener receives, assembled from the plan.. | `_spawn_launch_request` | mcp/src/agents_remember/application/terminal_tools.py:735-766 |
| Defines the function `spawn_agent_session_tool` (lines 769-842) — Spawn one role-configured, leaf-attached hosted session without a leaf brief.. | `spawn_agent_session_tool` | mcp/src/agents_remember/application/terminal_tools.py:769-842 |
| Defines the function `_spawned_payload` (lines 845-877) — The spawned-unbriefed row plus settings-owned launch-command outcome.. | `_spawned_payload` | mcp/src/agents_remember/application/terminal_tools.py:845-877 |
| Defines the function `_spawn_refusal` (lines 880-905) — A pre-spawn refusal payload (unknown/undetected harness or bad kind) -- nothing was spawned.. | `_spawn_refusal` | mcp/src/agents_remember/application/terminal_tools.py:880-905 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
