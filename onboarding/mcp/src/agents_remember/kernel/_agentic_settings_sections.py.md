# mcp/src/agents_remember/kernel/_agentic_settings_sections.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/kernel/_agentic_settings_sections.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-08T02:00+02:00                                            |
| lastVerifiedCommitHash | `1b7f6f07c5ccc64627299b5d22463ef9c267e187`                                        |
| lastVerifiedCommitDate | 2026-08-08T02:42:36+02:00|
| governingOverview      | `../../../overview.md`                                          |

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

``orchestration`` section parsers: loops, roles, concurrency, expectations, supervisor,
escalation, spawn, and the quality gate (260731-EFA-L17).

## Code Commentary

- `_parse_loops`
- `_parse_loop_defaults`
- `_parse_loop_complexity`
- `_parse_loop_levels`
- `_parse_roles`
- `_parse_roles_per_level`
- `_parse_concurrency`
- `_parse_expectations`
- `_parse_supervisor`
- `_require_supervisor_floor_seconds`
- `_parse_escalation`
- `_parse_escalation_sla_seconds`
- `_parse_escalation_rung_seconds`
- `_parse_respawn_after_rung`
- `_parse_spawn`
- `_parse_quality_gate` (260731-EFA-L17: `orchestration.qualityGate`, default 2 GiB,
  fail-loud unknown keys, positive-int `memoryCapBytes`)

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

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded `_parse_quality_gate`
  and the family's default/fail-loud/positive-int contract. Verification metadata
  stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
