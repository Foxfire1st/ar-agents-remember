# mcp/src/agents_remember/application/orchestration_tools.py

## Governing Overview

[overview](overview.md)

## Purpose

Application operations for orchestration communication.

## Code Commentary

### Logic

Module-level surface:

- `_result` (function, lines 30-32) — Return the raw use-case result for the MCP adapter to finalize.
- `NudgeTarget` (class, lines 36-42) — The manager seat a nudge is delivered to, addressed by its hosted-session agent id, its
- `NudgeSubject` (class, lines 46-53) — What the nudge is about: the human-readable subject line that names the stalled work, the
- `orchestration_nudge_manager_tool` (function, lines 56-127) — Record and push a manager nudge for inactivity or a missing turn report.
- `nudge_manager` (function, lines 130-149) — Compose the flat nudge request into target and subject decisions.
- `_log_nudge_event` (function, lines 152-170)

A nudge is recorded and its observed system event is appended before delivery is considered.
If the rate-limit owner returns `rate-limited`, this application returns that status immediately
and does not create a second operator-inbox post. Both sent and rate-limited outcomes retain the
durable event with state, reason, target, subject, and artifact attribution.

cit:([`orchestration_nudge_manager_tool`], mcp/src/agents_remember/application/orchestration_tools.py:58-129)
cit:([`_log_nudge_event`], mcp/src/agents_remember/application/orchestration_tools.py:154-172)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the function `_result` (lines 30-32) — Return the raw use-case result for the MCP adapter to finalize.. [1]
- Defines the class `NudgeTarget` (lines 36-42) — The manager seat a nudge is delivered to, addressed by its hosted-session agent id, its. [2]
- Defines the class `NudgeSubject` (lines 46-53) — What the nudge is about: the human-readable subject line that names the stalled work, the. [3]
- Defines the function `orchestration_nudge_manager_tool` (lines 56-127) — Record and push a manager nudge for inactivity or a missing turn report.. [4]
- Defines the function `nudge_manager` (lines 130-149) — Compose the flat nudge request into target and subject decisions.. [5]
- Defines the function `_log_nudge_event` (lines 152-170). [6]
