# mcp/src/agents_remember/kernel/_agentic_settings_core.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/kernel/_agentic_settings_core.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                        |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
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

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/kernel/_agentic_settings_core.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
