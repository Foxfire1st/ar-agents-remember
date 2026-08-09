# mcp/src/agents_remember/kernel/_agentic_settings_core.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/kernel/_agentic_settings_core.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T06:48+02:00                                            |
| lastVerifiedCommitHash | `2dea095cd68454a7a68893e37c07dbd8daa86d32`                                        |
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
| governingOverview      | `../../../overview.md`                                          |

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Typed agentic settings models, constants, and validation primitives. The settings family (``orchestration.*``) is merged from a global and an optional repo-local settings file. This module owns the typed models, the fail-loud key vocabularies, the shared shape/type validators, and the seeded defaults; the parsers live in responsibility-split siblings and the loader in :mod:`agents_remember.kern...

## Code Commentary

- `AgenticSettingsError`
- `LoopComplexity`
- `LoopDefaults`
- `LoopSettings`
- `RoleKnobs`
- `ConcurrencySettings`
- `ExpectationSettings`
- `AgentNotifierSettings` (renamed from `SupervisorSettings` in 260713-TES-L1)
- `QualityGateSettings` (260731-EFA-L17: `orchestration.qualityGate.memoryCapBytes`, default 2 GiB)
- `AgenticSettings`
- `KNOWN_AGENT_NOTIFIER_FIELDS` (renamed from `KNOWN_SUPERVISOR_FIELDS`; the legacy
  `supervisor` key remains in `KNOWN_ORCHESTRATION_FIELDS` during the compatibility window)
- `DEFAULT_AGENT_NOTIFIER_INTERVAL_SECONDS` / `DEFAULT_AGENT_NOTIFIER_STALE_CUTOFF_SECONDS` /
  `DEFAULT_AGENT_NOTIFIER_REDELIVER_BUDGET` / `DEFAULT_AGENT_NOTIFIER_ESCALATION_BUDGET`
  (renamed from `DEFAULT_SUPERVISOR_*`; `AgenticSettings.agent_notifier` is the renamed
  `supervisor` field)
- `agentic_settings_path`
- `default_agentic_settings_seed`
- `default_agentic_settings_seed_text`
- `merge_settings`
- `_refuse_unknown`
- `_require_object`
- `_require_string`
- `_require_positive_int`
- `_require_positive_number`
- `_require_bool`
- `_require_string_list`
- `_require_harness_id`

## 260713-TES-L2 Change — Expectation-Kind Surface Retired

`KNOWN_EXPECTATION_KINDS` cit:([`KNOWN_EXPECTATION_KINDS`], mcp/src/agents_remember/kernel/_agentic_settings_core.py:123-123) is now `{"briefed-by", "verdict-by"}` and
`DEFAULT_EXPECTATION_SLA_SECONDS` cit:([`DEFAULT_EXPECTATION_SLA_SECONDS`], mcp/src/agents_remember/kernel/_agentic_settings_core.py:125-128) carries only those two kinds:
the settings surface retires `ack-by` (N16: landing is terminal, no post writes an ack-by row)
and `turn-report-by` (catalog-truth relay) -- 260713-TES-L2 retired the latter, 260713-TES-L5
retires the former. The record Literal in `controlplane/expectation_rows.py` keeps both for
legacy-row parse compatibility; a settings override for a retired kind is refused.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260713-TES-L5 Change — Escalation Settings Family Demolished

The whole `orchestration.escalation` settings family is deleted: `EscalationSettings`,
`KNOWN_ESCALATION_FIELDS`, `KNOWN_ESCALATION_MESSAGE_KINDS`, `KNOWN_ESCALATION_RUNGS`,
`DEFAULT_ESCALATION_SLA_SECONDS`, `DEFAULT_ESCALATION_RUNG_SECONDS`, and
`DEFAULT_RESPAWN_AFTER_RUNG` are gone from the module, `escalation` is removed from
`KNOWN_ORCHESTRATION_FIELDS`, and a settings file that sets it now fails loud as an unknown key.
`escalationBudget` (default 250) stays under `orchestration.agentNotifier` as a per-sweep
load-shed cap on owner-signal findings (seat-liveness + dead-upstream), the twin of
`redeliverBudget`; shed findings re-fire next sweep (level-triggered).

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L17 Change

The module owns the new `orchestration.qualityGate` family: `KNOWN_QUALITY_GATE_FIELDS`
(line 65, exactly `{"memoryCapBytes"}`), the frozen `QualityGateSettings` model
(lines 317-330, defaulting to `DEFAULT_FULL_GATE_MEMORY_CAP_BYTES` = 2 GiB from
`code_quality.memory_cap`), the `AgenticSettings.quality_gate` field (lines 331-389), and the
seeded default (`default_agentic_settings_seed`, lines 395-425). Unknown keys in the family
fail loud through the shared `_refuse_unknown` machinery exactly like every other
orchestration family.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/kernel/_agentic_settings_core.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the demolition of the
  `orchestration.escalation` family (models, known-key sets, defaults, fail-loud unknown key),
  the retirement of `ack-by` from `KNOWN_EXPECTATION_KINDS`/`DEFAULT_EXPECTATION_SLA_SECONDS`,
  and the re-wiring of `escalationBudget` as the per-sweep owner-signal load-shed cap.
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the `state-signal` message kind in
  `KNOWN_ESCALATION_MESSAGE_KINDS` and its 300s SLA default (N12/N13); noted the dormant-ladder
  retention of the escalation SLA surface (N3, L5 deletes). Verification metadata pinned until
  closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the `turn-report-by` retirement
  from `KNOWN_EXPECTATION_KINDS`/`DEFAULT_EXPECTATION_SLA_SECONDS` (legacy Literal retained in
  the controlplane record). Verification metadata pinned until closeout stamps the
  260713-TES-L2 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: recorded the `AgentNotifierSettings` /
  `KNOWN_AGENT_NOTIFIER_FIELDS` / `DEFAULT_AGENT_NOTIFIER_*` renames and the retained legacy
  `supervisor` key in `KNOWN_ORCHESTRATION_FIELDS` for the alias window. Verification metadata
  pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the
  `orchestration.qualityGate` family (known-key set, `QualityGateSettings` model,
  `AgenticSettings.quality_gate` field, seeded 2 GiB default). Verification
  metadata stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
