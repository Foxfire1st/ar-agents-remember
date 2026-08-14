# mcp/src/agents_remember/kernel/_agentic_settings_core.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/kernel/_agentic_settings_core.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-08T02:00+02:00                                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../../../overview.md`                                          |

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Typed agentic settings models, constants, and validation primitives. The settings family (``orchestration.*``) is merged from a global and an optional repo-local settings file. This module owns the typed models, the fail-loud key vocabularies, the shared shape/type validators, and the seeded defaults; the parsers live in responsibility-split siblings and the loader in :mod:`agents_remember.kern...

## Code Commentary

L23 adds the closed `QualityExecutor` choice and defaults `orchestration.qualityGate.executor` to `local`; `dagger` is the only clean-environment alternative.

- `AgenticSettingsError`
- `LoopComplexity`
- `LoopDefaults`
- `LoopSettings`
- `RoleKnobs`
- `ConcurrencySettings`
- `ExpectationSettings`
- `SupervisorSettings`
- `EscalationSettings`
- `QualityGateSettings` (260731-EFA-L17/L24: optional `orchestration.qualityGate.memoryCapBytes`; absent means host-managed RAM and swap)
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

## 260731-EFA-L17/L24 Quality-Gate Settings

The module owns the `orchestration.qualityGate` family:
`KNOWN_QUALITY_GATE_FIELDS` contains `memoryCapBytes` and the Dagger-only `executor`; the frozen
`QualityGateSettings` model uses `None` for the container-runtime-managed default; and the
generated settings seed deliberately omits the family. An explicit positive
integer remains available for a constrained Dagger lifecycle run. Unknown keys fail loud through
the shared `_refuse_unknown` machinery exactly like every other orchestration
family.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/kernel/_agentic_settings_core.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## L23 Final Candidate Disposition

Quality settings accept the one Dagger executor contract and do not preserve `local` as a selectable
acceptance mode. Optional resource policy configures the graph; it does not select a second runner.

## R39 Dagger Resource Ownership

The quality-gate executor remains closed to Dagger. An omitted memory cap means the Dagger
container runtime owns RAM and swap; an explicit cap reaches the graph inner wrapper. No host
systemd or address-space fallback is part of lifecycle acceptance.

## Update History

- 2026-08-14T11:25+02:00 — R39 curator: reconciled resource prose with the container-only
  executor. Verification remains closeout-owned.
- 2026-08-14T06:32+02:00 — L23 final candidate review: quality settings preserve Dagger as the
  only accepted executor; parsing no longer implies a local compatibility runner. Verification
  remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: replaced the seeded 2 GiB
  ceiling with an absent/`None` host-managed default while retaining one
  explicit positive-integer cap. Verification metadata remains pinned until
  closeout stamps the L24 code commit.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the
  `orchestration.qualityGate` family (known-key set, `QualityGateSettings` model,
  `AgenticSettings.quality_gate` field, seeded 2 GiB default). Verification
  metadata stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
