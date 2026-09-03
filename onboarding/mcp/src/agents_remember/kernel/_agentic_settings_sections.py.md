# mcp/src/agents_remember/kernel/_agentic_settings_sections.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/kernel/_agentic_settings_sections.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview      | `../../../overview.md`                                          |

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

``orchestration`` section parsers: loops, roles, concurrency, expectations, supervisor,
escalation, spawn, and the quality gate (260731-EFA-L17).

## Code Commentary

L23 parsed `qualityGate.executor` as exactly `local` or `dagger` and refused any other value. CCR-R22@v1 (L22, commit `685f83c44055`) removed the executor key from the quality gate parser entirely: `_parse_quality_gate` now rejects any `executor` key as an unknown key (fail loud via the shared machinery) and returns `QualityGateSettings(memory_cap_bytes=...)` only -- executor identity belongs to the repository certification profile.

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
  absent/empty means adapter-runtime-managed, fail-loud unknown keys, positive-int
  `memoryCapBytes` when present; CCR-R22 removed the `executor` key)

## 260731-EFA-L17/L24 Quality-Gate Parser

`_parse_quality_gate` parses `orchestration.qualityGate` into
`QualityGateSettings`: an absent family/key keeps `memory_cap_bytes=None`, unknown keys
fail loud via `_refuse_unknown(block, KNOWN_QUALITY_GATE_FIELDS, ...)`, and
`memoryCapBytes` must be a positive integer (`_require_positive_int`). Since CCR-R22 the
former `executor` key is no longer a known field: any value under it is rejected as an
unknown key (the old permissive `dagger`-only acceptance branch was deleted). A `null` at the
family key is refused by `_refuse_null_families` before this parser runs.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/kernel/_agentic_settings_sections.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## L23 Final Candidate Disposition

The orchestration quality section projects Dagger-only executor policy through strict settings
models. Unknown or legacy executor values fail validation instead of activating compatibility code.

## R39 Dagger-Only Settings Refusal

The parser accepts only the Dagger executor and describes every other value as forbidden host test
execution, not a lower-authority diagnostic option. The optional cap is a container resource
policy.

## Update History
- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the executor-key removal from the quality-gate section parser -- the old dagger-only acceptance branch was deleted and `executor` now fails loud as an unknown key; memoryCapBytes-only parsing remains.


- 2026-08-14T11:25+02:00 — R39 curator: recorded the host-test refusal and container-owned cap
  semantics. Verification remains closeout-owned.
- 2026-08-14T06:32+02:00 — L23 final candidate review: orchestration quality settings project the
  Dagger-only execution contract and exact policy fields without adding fallback selection.
  Verification remains closeout-owned.

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
