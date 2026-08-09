# mcp/src/agents_remember/kernel/_agentic_settings_sections.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/kernel/_agentic_settings_sections.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-08T21:20+02:00                                            |
| lastVerifiedCommitHash | `b7f09a4dc992a7a450a0a37e704475e66df79746`                                        |
| lastVerifiedCommitDate | 2026-08-09T21:31:32+02:00|
| governingOverview      | `../../../overview.md`                                          |

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

``orchestration`` section parsers: loops, roles, concurrency, expectations, agent-notifier,
spawn, and the quality gate (260731-EFA-L17). The agent-notifier parser is
`_parse_agent_notifier` (renamed from `_parse_supervisor` in 260713-TES-L1); the floor validator
is `_require_agent_notifier_floor_seconds` (renamed from `_require_supervisor_floor_seconds`).
The legacy-key normalization itself lives in `agentic_settings._resolve_agent_notifier_alias`,
which runs in `_validated_orchestration_block` before parsing.

## Code Commentary

- `_parse_loops`
- `_parse_loop_defaults`
- `_parse_loop_complexity`
- `_parse_loop_levels`
- `_parse_roles`
- `_parse_roles_per_level`
- `_parse_concurrency`
- `_parse_expectations`
- `_parse_agent_notifier` (renamed from `_parse_supervisor`)
- `_require_agent_notifier_floor_seconds` (renamed from `_require_supervisor_floor_seconds`)
- `_parse_spawn`
- `_parse_quality_gate` (260731-EFA-L17: `orchestration.qualityGate`, default 2 GiB,
  fail-loud unknown keys, positive-int `memoryCapBytes`)

## 260713-TES-L5 Change — Escalation Parsers Deleted

`_parse_escalation`, `_parse_escalation_sla_seconds`, `_parse_escalation_rung_seconds`, and
`_parse_respawn_after_rung` are deleted with the `orchestration.escalation` family; the module
docstring and import block no longer name escalation. Any settings file that sets the retired
family fails loud as an unknown key in `_validated_orchestration_block` before any parser here
runs.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L17 Change

`_parse_quality_gate` (lines 476-494) parses `orchestration.qualityGate` into
`QualityGateSettings`: absent family/key keeps the documented 2 GiB default, unknown keys
fail loud via `_refuse_unknown(block, KNOWN_QUALITY_GATE_FIELDS, ...)`, and
`memoryCapBytes` must be a positive integer (`_require_positive_int`). A `null` at the
family key is refused by `_refuse_null_families` before this parser runs.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/kernel/_agentic_settings_sections.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-09T21:10+02:00 — No content impact: master integration gate repair corrected the source's stale
  `_parse_spawn` self-citation to the declaration's current line. Runtime behavior and the
  parser surface are unchanged. Verification metadata stays pinned until closeout.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the deletion of the four
  `_parse_escalation*`/`_parse_respawn_after_rung` parsers and the fail-loud retirement of the
  `orchestration.escalation` family. Verification metadata pinned until closeout stamps the
  260713-TES-L5 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: recorded the `_parse_agent_notifier` /
  `_require_agent_notifier_floor_seconds` renames and the facade-side alias normalization.
  Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded `_parse_quality_gate`
  and the family's default/fail-loud/positive-int contract. Verification metadata
  stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
