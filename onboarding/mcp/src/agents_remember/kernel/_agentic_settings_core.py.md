# mcp/src/agents_remember/kernel/_agentic_settings_core.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Typed agentic settings models, constants, and validation primitives. The settings family (``orchestration.*``) is merged from a global and an optional repo-local settings file. This module owns the typed models, the fail-loud key vocabularies, the shared shape/type validators, and the seeded defaults; the parsers live in responsibility-split siblings and the loader in :mod:`agents_remember.kern...

Defines typed role knobs and inherited agentic settings defaults.

## Code Commentary

L23 had added the closed `QualityExecutor` choice defaulting `orchestration.qualityGate.executor` to `local`. CCR-R22@v1 (L22, commit `685f83c44055`) removed the executor field entirely: `QualityExecutor` is deleted, `KNOWN_QUALITY_GATE_FIELDS` now contains only `memoryCapBytes`, and `QualityGateSettings` carries only `memory_cap_bytes` -- executor identity belongs to the repository certification profile, not to agentic settings.

- `AgenticSettingsError`
- `LoopComplexity`
- `LoopDefaults`
- `LoopSettings`
- `RoleKnobs`
- `ConcurrencySettings`
- `ExpectationSettings`
- `SupervisorSettings`
- `EscalationSettings`
- `QualityGateSettings` (260731-EFA-L17/L24: optional `orchestration.qualityGate.memoryCapBytes`; absent means host-managed RAM and swap; CCR-R22 removed the `executor` field -- the profile owns the adapter)
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

### Role Runtime and Scope

RoleKnobs now carries optional service_tier. resolved_role_knobs merges tier independently of harness/model/effort, so a lower-level model or effort does not erase a role/altitude tier. Preserve the existing spend/launch-arg/default explanations and add this independent native capability fact.

## 260731-EFA-L17/L24 Quality-Gate Settings

The module owns the `orchestration.qualityGate` family:
`KNOWN_QUALITY_GATE_FIELDS` contains only `memoryCapBytes` (the `executor` key was removed by
CCR-R22); the frozen `QualityGateSettings` model uses `None` for the adapter-runtime-managed
default; and the generated settings seed deliberately omits the family. An explicit positive
integer remains available for a constrained full-gate run. Unknown keys fail loud through
the shared `_refuse_unknown` machinery exactly like every other orchestration
family.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/kernel/_agentic_settings_core.py`.

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.

### Runtime Source References

- Frozen implementation of RoleKnobs supporting the stated file behavior. [1]
- Frozen implementation of AgenticSettings supporting the stated file behavior. [2]

## L23 Final Candidate Disposition

Quality settings no longer carry an executor field at all (CCR-R22): the one adopted acceptance
adapter comes from the repository's certification profile. Optional resource policy configures the
graph; agentic settings cannot select or constrain a second runner.

## R39 Dagger Resource Ownership

The quality-gate executor remains closed to Dagger. An omitted memory cap means the Dagger
container runtime owns RAM and swap; an explicit cap reaches the graph inner wrapper. No host
systemd or address-space fallback is part of lifecycle acceptance.

## CCR-L42 current candidate

The review budget now has one `MAX_REVIEW_ROUNDS = 3` authority constant, and the seeded loop default uses it so a settings value cannot silently authorize a fourth review.
