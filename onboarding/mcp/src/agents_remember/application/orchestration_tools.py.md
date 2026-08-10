# mcp/src/agents_remember/application/orchestration_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/orchestration_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

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
| Defines the function `_result` (lines 30-32) — Return the raw use-case result for the MCP adapter to finalize.. | `_result` | mcp/src/agents_remember/application/orchestration_tools.py:30-32 |
| Defines the class `NudgeTarget` (lines 36-42) — The manager seat a nudge is delivered to, addressed by its hosted-session agent id, its. | `NudgeTarget` | mcp/src/agents_remember/application/orchestration_tools.py:35-42 |
| Defines the class `NudgeSubject` (lines 46-53) — What the nudge is about: the human-readable subject line that names the stalled work, the. | `NudgeSubject` | mcp/src/agents_remember/application/orchestration_tools.py:45-53 |
| Defines the function `orchestration_nudge_manager_tool` (lines 56-127) — Record and push a manager nudge for inactivity or a missing turn report.. | `orchestration_nudge_manager_tool` | mcp/src/agents_remember/application/orchestration_tools.py:56-127 |
| Defines the function `nudge_manager` (lines 130-149) — Compose the flat nudge request into target and subject decisions.. | `nudge_manager` | mcp/src/agents_remember/application/orchestration_tools.py:130-149 |
| Defines the function `_log_nudge_event` (lines 152-170). | `_log_nudge_event` | mcp/src/agents_remember/application/orchestration_tools.py:152-170 |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
