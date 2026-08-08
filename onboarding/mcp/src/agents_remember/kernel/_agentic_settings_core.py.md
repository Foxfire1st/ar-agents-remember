# mcp/src/agents_remember/kernel/_agentic_settings_core.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/kernel/_agentic_settings_core.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-08T02:00+02:00                                            |
| lastVerifiedCommitHash | `1b7f6f07c5ccc64627299b5d22463ef9c267e187`                                        |
| lastVerifiedCommitDate | 2026-08-08T02:42:36+02:00|
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
- `SupervisorSettings`
- `EscalationSettings`
- `QualityGateSettings` (260731-EFA-L17: `orchestration.qualityGate.memoryCapBytes`, default 2 GiB)
- `AgenticSettings`
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

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the
  `orchestration.qualityGate` family (known-key set, `QualityGateSettings` model,
  `AgenticSettings.quality_gate` field, seeded 2 GiB default). Verification
  metadata stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
