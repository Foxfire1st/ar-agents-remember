# mcp/src/agents_remember/kernel/_agentic_settings_sections.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/kernel/_agentic_settings_sections.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-08T02:00+02:00                                            |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`                                        |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview      | `../../../overview.md`                                          |

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

``orchestration`` section parsers: loops, roles, concurrency, expectations, supervisor,
escalation, spawn, and the quality gate (260731-EFA-L17).

## Code Commentary

L23 parses `qualityGate.executor` as exactly `local` or `dagger` and refuses any other value instead of selecting a fallback.

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
- `_parse_quality_gate` (260731-EFA-L17/L24: `orchestration.qualityGate`,
  absent/empty means host-managed, fail-loud unknown keys, positive-int
  `memoryCapBytes` when present)

## 260731-EFA-L17/L24 Quality-Gate Parser

`_parse_quality_gate` parses `orchestration.qualityGate` into
`QualityGateSettings`: an absent family/key keeps `memory_cap_bytes=None`, unknown keys
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

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: recorded that absent or
  empty quality-gate settings select host-managed memory and only an explicit
  positive integer enables the cap. Verification metadata remains pinned until
  closeout stamps the L24 code commit.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded `_parse_quality_gate`
  and the family's default/fail-loud/positive-int contract. Verification metadata
  stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
